"""Lot AS — remontée dans Moodle des positionnements (entrée / sortie) et de la vérification finale.
Décision de Marc du 10/11/2026 : « J'ai besoin de savoir comment ils ont progressé ».
Aligne la couche SCORM du module sur le gabarit noyau v1.6 (interactions autorisées, aucun score).
Plan des cmi.interactions (SCORM 1.2) :
  0-5   PRE_n_<dimension>   numeric, 1 à 5 (autorité ajustée convertie de 1-10 vers 1-5)
  6-11  POST_n_<dimension>  numeric, 1 à 5
  12-16 MGTEVAL_Qn          choice, result correct / wrong
Idempotent (marqueur ux18i-lot-as). Usage : python3 tools/patch_lot_as.py src/index.html
"""
import sys
path = sys.argv[1]
h = open(path, encoding='utf8').read()
if 'ux18i-lot-as' in h:
    print('Lot AS déjà appliqué'); sys.exit(0)

def rep(old, new):
    global h
    assert h.count(old) == 1, f'{h.count(old)} occurrence(s) : {old[:80]}'
    h = h.replace(old, new)

# 1. Couche SCORM : interactions autorisées (id, type, student_response, result), score toujours proscrit
rep('var PROSCRITS=["cmi.core.score","cmi.interactions","cmi.objectives","cmi.student_data.mastery_score"];',
    'var PROSCRITS=["cmi.core.score","cmi.objectives","cmi.student_data.mastery_score"]; /* ux18i-lot-as : interactions autorisées (gabarit v1.6) */')
rep('function autorise(k){return BLANCHE.indexOf(k)!==-1}',
    'function autorise(k){return BLANCHE.indexOf(k)!==-1||/^cmi\\.interactions\\.\\d+\\.(id|type|student_response|result)$/.test(k)}')

# 2. Fonctions d'écriture (reprises du gabarit v1.6 ; positionnement en « numeric » pour les moyennes)
rep('function enregistrerPositionnement(){return}\nfunction enregistrerEval(){return}',
'''function enregistrerPositionnement(phase,numeroQuestion,valeur,opts){
 if(!config.reportPositionnement)return;opts=opts||{};
 var n=config.items.length,index=phase==="pre"?numeroQuestion:n+numeroQuestion;
 SCORM.set("cmi.interactions."+index+".id",opts.id||((phase==="pre"?"PRE":"POST")+"_COMPETENCE_"+String(numeroQuestion+1)));
 SCORM.set("cmi.interactions."+index+".type",opts.type||"numeric");
 SCORM.set("cmi.interactions."+index+".student_response",String(valeur));
 SCORM.set("cmi.interactions."+index+".result","neutral");
 SCORM.commit()}
function enregistrerEval(numeroQuestion,reussi,opts){
 if(!config.reportEval)return;opts=opts||{};
 var base=(config.reportPositionnement?config.items.length*2:0),index=base+numeroQuestion;
 SCORM.set("cmi.interactions."+index+".id",opts.id||("EVAL_Q"+(numeroQuestion+1)));
 SCORM.set("cmi.interactions."+index+".type",opts.type||"choice");
 SCORM.set("cmi.interactions."+index+".student_response",String(opts.reponse!=null?opts.reponse:(reussi?"correct":"incorrect")));
 SCORM.set("cmi.interactions."+index+".result",reussi?"correct":"wrong");
 SCORM.commit()}''')
rep('evalResultat:evalResultat,evalTerminee:evalTerminee,', 'evalResultat:evalResultat,evalTerminee:evalTerminee,enregistrerPositionnement:enregistrerPositionnement,')

# 3. Configuration du module
rep('reportPositionnement:false,\n reportEval:false,', 'reportPositionnement:true,\n reportEval:true,')

# 4. Le module envoie chaque dimension dès qu'elle est complète (dans la portée du module)
rep("""  GABARIT.etat[pass][i]=Math.round(score);\n }\n}""",
    """  GABARIT.etat[pass][i]=Math.round(score);\n  /* ux18i-lot-as : envoi de la dimension à Moodle (échelle 1 à 5, deux décimales) */\n  if(pass==='pre'||pass==='post')GABARIT.enregistrerPositionnement(pass,i,Math.round(score*100)/100,{id:(pass==='pre'?'PRE_':'POST_')+(i+1)+'_'+String(d.id).toUpperCase()});\n }\n}""")

# 5. Informations données aux élus : alignées sur ce qui est réellement enregistré
rep('<b>Vos réponses restent personnelles.</b> Elles ne sont transmises ni à l’IFAP ni au Congrès ; la plateforme ne suit que votre progression.',
    '<b>Vos productions restent personnelles.</b> La plateforme enregistre votre progression, vos positionnements d’entrée et de sortie et vos réponses à la vérification finale, pour mesurer l’effet du parcours. Rien n’est transmis nominativement au Congrès.')
rep('<strong>Vos réponses personnelles ne sont transmises ni à l’IFAP ni au Congrès comme données de reporting.</strong>',
    '<strong>Vos productions personnelles ne sont transmises ni à l’IFAP ni au Congrès.</strong>')
rep('Les réponses aux scénarios, vos productions personnelles et votre feuille de route ne sont pas transmises comme données pédagogiques nominatives. Les restitutions destinées au pilotage sont agrégées et anonymes.',
    'Elle enregistre aussi, pour mesurer la progression, vos positionnements d’entrée et de sortie (six dimensions) et vos réponses à la vérification finale (juste ou non), sans note ni classement ; seuls les personnels IFAP habilités y ont accès. Les réponses aux scénarios, vos productions personnelles et votre feuille de route ne sont pas transmises. Le Congrès ne reçoit que des résultats collectifs et anonymisés.')
rep('Vos réponses ne sont transmises à personne.',
    'Vos réponses (juste ou non) sont enregistrées pour mesurer la progression du parcours ; seuls les personnels IFAP habilités y ont accès.')
rep('Seuls vos positionnements, votre avancement et la complétion du module sont accessibles aux personnels IFAP habilités.',
    'Seuls vos positionnements, vos réponses à la vérification finale, votre avancement et la complétion du module sont accessibles aux personnels IFAP habilités.')
rep('Les données de suivi pédagogique (progression, complétion) sont gérées par la plateforme de diffusion',
    'Les données de suivi pédagogique (progression, complétion, positionnements d’entrée et de sortie, réponses à la vérification finale) sont gérées par la plateforme de diffusion')

h = h.replace('</head>', '<meta name="ux18i-lot-as" content="interactions SCORM">\n</head>', 1)
open(path, 'w', encoding='utf8').write(h)
print('Lot AS appliqué')
