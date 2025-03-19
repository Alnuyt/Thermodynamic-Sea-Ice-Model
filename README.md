# Thermodynamic-Sea-Ice-Model
Le réchauffement climatique a un impact majeur sur l’évolution de la glace de mer arctique. Ce projet, réalisé dans le cadre du coursLPHYS2265, vise à modéliser ces changements en simulant l’épaisseur de la glace à l’aide d’un modèle thermodynamique en une dimension. En s’appuyant sur les lois de la diffusion thermique et du bilan énergétique, nous avons développé et amélioré plusieurs approches successives :
1. **Modèle thermique de la glace de mer :** évolution avec flux de chaleur constant, ajout de la température de surface, prise en compte de la neige et des flux océaniques.
2. **Modèle thermodynamique de la glace :** ajustement des paramètres physiques, ajout du contrôle expérimental et amélioration de la représentation de l’albédo.
3. **Analyse multi-modèle :** étude comparative et projections climatiques sur 100 ans avec différents scénarios de forçage radiatif.

## Partie 1 : Modèle Thermodynamique de la Glace de Mer
Dans cette première partie, nous avons modélisé l'évolution de l'épaisseur de la glace en fonction des flux de chaleur conductifs et des variations de température. Les étapes principales sont :

- Simulation de la croissance de la glace avec un flux de chaleur constant provenant de l'océan.
- Intégration de l'évolution de la température de surface dans le modèle.
- Ajout d'une couche de neige et d'un mélange océanique pour plus de réalisme.

Les résultats montrent que l'épaisseur finale de la glace est bien corrélée aux prévisions théoriques et dépend fortement du flux océanique.

## Partie 2 : Modèle Thermodynamique Amélioré
Dans cette seconde phase, nous avons affiné le modèle en ajoutant :

- Un contrôle expérimental comparant notre simulation à des modèles de référence (hiMU71).
- Une correction des valeurs d'épaisseur de glace pour assurer une meilleure correspondance avec les données observées.
- Une prise en compte améliorée de l'albédo pour différentes conditions de surface (neige sèche, glace nue, etc.).

L'évolution saisonnière de l'épaisseur de glace montre une dynamique réaliste avec une variation annuelle significative.

## Partie 3 : Analyse Multi-Modèle
Dans cette dernière étape, une approche collaborative a permis de comparer plusieurs modèles étudiants. Nous avons effectué des projections sur 100 ans en prenant en compte différentes hypothèses de forçage radiatif (augmentation du rayonnement infrarouge descendant) avec trois scénarios :

- PR03 (+3 W/m²)
- PR06 (+6 W/m²)
- PR12 (+12 W/m²)

Les principaux résultats sont :

- Une tendance générale à la diminution de l'épaisseur de la glace au fil des années.
- Une fonte plus marquée en été lorsque la température de surface dépasse le seuil de fusion.
- Une sensibilité accrue du modèle aux variations des paramètres d’entrée, notamment l’albédo et la couche de neige.

## Conclusion
Les résultats obtenus confirment la forte influence des forçages radiatifs sur l’évolution de la glace de mer. Nos simulations montrent que même avec un faible forçage (PR03), l’épaisseur de la glace diminue progressivement. Sous un scénario plus sévère (PR12), la perte de glace atteint 50 % en un siècle. Cette tendance est cohérente avec les observations climatiques actuelles et souligne l’urgence de limiter les émissions de gaz à effet de serre.

Une amélioration du modèle pourrait inclure l'interaction entre la glace et les courants océaniques, ainsi que l'intégration d'une dynamique atmosphérique plus détaillée. De futures recherches pourraient également se concentrer sur les impacts de cette fonte sur l'écosystème arctique et le climat global.

## Utilisation 
Exécutez les scripts des codes pour : 
- Modèle Thermodynamique de la Glace de Mer : [Ice_growth_with_constant_temperature_ANTIM.py](Ice_growth_with_constant_temperature_ANTIM.py)
- Modèle Thermodynamique Amélioré : [Freeing_surface_temperature_ANTIM.py](Freeing_surface_temperature_ANTIM.py)
