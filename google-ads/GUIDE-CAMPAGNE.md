# Campagne Google Ads Search – Plombier Toulouse (CPC manuel)

Fichiers générés par `python3 tools/build_ads.py` (modifiez le script puis relancez-le pour tout régénérer).
Ce dossier n'est **pas publié** sur le site (bloqué dans `netlify.toml` et `robots.txt`).

| Fichier | Contenu |
|---|---|
| `1-campagnes.csv` | 2 campagnes Search, CPC manuel, budgets |
| `2-mots-cles.csv` | 933 mots-clés en **exact** et **expression** avec enchère et URL finale |
| `3-groupes-annonces.csv` | 32 groupes d'annonces et leur enchère par défaut |
| `4-annonces-rsa.csv` | 1 annonce responsive par groupe : 15 titres, 4 descriptions, chemins |
| `5-mots-cles-negatifs.csv` | 125 mots-clés négatifs par campagne (emploi, bricolage, magasins, autres villes…) |
| `6-composants-extensions.csv` | Liens annexes, accroches, extraits de site, extension d'appel |

---

## 1. Structure

### Campagne 1 – `Search - Plombier Toulouse - Urgence` (budget de départ 50 €/jour)

| Groupe d'annonces | Page de destination | Enchère exacte | Enchère expression |
|---|---|---|---|
| Plombier Urgence Toulouse | `/` | 7,50 € | 6,00 € |
| Plombier Toulouse | `/` | 6,00 € | 4,80 € |
| Plombier Près de Moi (exact seulement, ciblage géo) | `/` | 5,50 € | – |
| Fuite d'eau | `/fuite-d-eau-toulouse/` | 5,00 € | 4,00 € |
| Débouchage canalisation | `/debouchage-canalisation-toulouse/` | 5,00 € | 4,00 € |
| Recherche de fuite | `/recherche-de-fuite-toulouse/` | 4,50 € | 3,60 € |
| WC bouché | `/debouchage-wc-toulouse/` | 4,50 € | 3,60 € |
| Chauffe-eau | `/depannage-chauffe-eau-toulouse/` | 4,50 € | 3,60 € |
| Dégât des eaux | `/degat-des-eaux-toulouse/` | 4,50 € | 3,60 € |
| Robinet | `/reparation-robinet-toulouse/` | 2,50 € | 2,00 € |

### Campagne 2 – `Search - Plombier Communes 25 km` (budget de départ 20 €/jour)

- 21 groupes, un par commune principale (Blagnac, Colomiers, Tournefeuille, Balma, L'Union, Muret, Cugnaux, Ramonville, Saint-Orens, Plaisance-du-Touch, Castanet, Portet, Villeneuve-Tolosane, Saint-Jean, Aucamville, Labège, Fenouillet, Launaguet, Castelginest, Cornebarrieu, Pibrac). Pour chacun : « plombier X », « plombier urgence X », « fuite d'eau X », « débouchage X », « wc bouché X », « chauffe eau X »… Exact 4,00 € / expression 3,20 €.
- 1 groupe « Autres communes » couvrant les 56 autres communes du rayon de 25 km (3,50 € / 2,80 €).
- Le titre n°1 de chaque annonce contient le nom de la commune, et il est **épinglé en position 1** pour la pertinence.

> **Pourquoi deux campagnes ?** Les recherches « Toulouse / urgence » coûtent plus cher et convertissent le mieux. Les communes coûtent moins cher. En séparant les budgets, Toulouse ne « mange » pas le budget des communes, et inversement.

> **Pourquoi pas de requête large ?** En CPC manuel, la requête large déclenche beaucoup de recherches hors sujet. Exact + expression = contrôle total du budget.

> **Les enchères sont des points de départ.** Les guides du secteur indiquent 6 à 12 € par clic pour « plombier urgence » en France, et environ 4 € pour les artisans du bâtiment en général. Vérifiez-les dans le **Planificateur de mots clés** de votre compte (ciblage Toulouse + 25 km), puis ajustez après 7 à 14 jours (voir § 6).

---

## 2. Paramètres de campagne (à régler à la main, identiques pour les 2 campagnes)

| Paramètre | Valeur |
|---|---|
| Objectif | Prospects (leads), sans objectif automatique |
| Type | Réseau de Recherche |
| Réseaux | **Décocher** « Partenaires du Réseau de Recherche » et « Réseau Display » |
| Zones | Toulouse **+ rayon de 25 km** |
| Option de zone | **« Présence : personnes se trouvant dans vos zones ciblées ou y étant régulièrement »** (jamais « intérêt ») |
| Langues | Français |
| Enchères | **CPC manuel** |
| Calendrier | 24h/24, 7j/7 |
| Rotation des annonces | Optimiser |
| Ajustements appareils | Mobile **+20 %**, Ordinateur **–20 %**, Tablette **–30 %** (les urgences se font au téléphone) |
| Ajustements horaires | 19h–8h **+15 %**, samedi-dimanche **+10 %** (urgences = moins de concurrence, plus d'intention) |
| Suivi | Auto-marquage (GCLID) activé |

---

## 3. Composants (extensions)

- **Appel** : 09 70 70 71 29, rapports d'appels **activés**, conversion « Appels depuis les annonces » ≥ **60 secondes**. Google peut demander de vérifier le numéro.
- **Liens annexes** (8) : Fuite d'eau, Recherche de fuite, Débouchage canalisation, WC bouché, Chauffe-eau en panne, Dégât des eaux, Devis gratuit en ligne, Zones d'intervention, chacun avec 2 lignes de description.
- **Accroches** (10) : Disponible 24h/24 7j/7, Devis Avant Travaux, Intervention Rapide, Nuit, Week-end, Fériés, Toutes Marques, Paiement CB Accepté, Facture pour l'Assurance, Plombiers Qualifiés, Détection Sans Casse, Toulouse + 25 km.
- **Extraits de site** : en-tête « Services » : Fuite d'eau, Recherche de fuite, Débouchage, WC bouché, Chauffe-eau, Dégât des eaux, Robinetterie.
- **Lieu** : associez votre **fiche Google Business Profile**, c'est très important pour les recherches locales.
- **Images** : ajoutez 4 à 6 photos du site (dossier `/images/`, versions `-hd.jpg`).

---

## 4. Suivi des conversions : à vérifier AVANT de lancer

Le site envoie aujourd'hui **la même conversion** (`AW-18317420737/2JlZCOOYyfkcEMHRtp5E`) pour un clic sur le numéro ET pour un formulaire envoyé. Recommandation :

1. Créer 3 actions de conversion distinctes dans Google Ads :
   - **Appel depuis l'annonce** (extension d'appel, durée ≥ 60 s) : principale
   - **Clic sur le numéro du site** (`tel:`) : principale
   - **Formulaire de devis envoyé** : principale
2. Remplacer le libellé du formulaire dans `assets/main.js` par celui de la nouvelle conversion « Formulaire ».
3. Idéalement, activer les **appels depuis le site via un numéro de transfert Google** (conversion « appels vers un numéro de téléphone sur votre site web »). Seuls les vrais appels de plus de 60 s sont alors comptés, et non les simples clics.
4. Vérifier dans Google Tag Manager / Google Tag que la balise `GT-T944WWWS` envoie bien vers le compte `AW-18317420737` (« Destinations »).

---

## 5. Importer dans Google Ads Editor

1. Ouvrez **Google Ads Editor**, téléchargez votre compte.
2. Créez les 2 campagnes avec les paramètres du § 2 (ou importez `1-campagnes.csv`, puis vérifiez zones et réseaux).
3. **Compte > Importer > Depuis un fichier**, dans cet ordre : `3-groupes-annonces.csv`, `2-mots-cles.csv`, `4-annonces-rsa.csv`, `5-mots-cles-negatifs.csv`. À chaque import, vérifiez que les colonnes sont bien reconnues.
4. Ajoutez les composants du fichier `6-composants-extensions.csv` au niveau des campagnes.
5. Vérifiez, puis **Publier**. Les campagnes sont créées **en pause** : activez-les quand le suivi des conversions est validé.

---

## 6. Routine d'optimisation (c'est ce qui fait la rentabilité)

**Les 14 premiers jours, tous les 2 à 3 jours :**
- **Rapport sur les termes de recherche** : ajoutez en négatif tout ce qui n'est pas une demande de plombier (prix de pièces, tutos, emploi, autres villes…). Ajoutez en mot-clé exact les bonnes requêtes qui convertissent.
- **Taux d'impressions en haut de page** sur « Plombier Urgence » : visez plus de 70 %. S'il est trop bas, augmentez l'enchère de 10 à 15 %.

**Ensuite, chaque semaine :**
- Mot-clé avec coût > 2× votre coût par contact cible **et** 0 conversion : baissez l'enchère de 20 % ou mettez-le en pause.
- Mot-clé qui convertit, avec un coût par contact sous l'objectif : montez l'enchère de 10 à 20 %.
- Regardez le **Niveau de qualité** (colonne à ajouter). En dessous de 5, retravaillez l'annonce ou la page de destination de ce groupe.
- Testez de nouveaux titres sur les annonces ayant une « efficacité » faible.

**Repères** (sources : guides d'agences, à confirmer avec vos propres données) : coût par contact qualifié souvent entre 25 et 80 € pour un artisan, objectif courant de 30 à 60 € par appel.

---

## 7. Règles Google à respecter

- Pas de superlatif non prouvé (« le n°1 », « le meilleur », « le moins cher ») : les annonces n'en contiennent pas.
- Les prix et délais annoncés doivent être tenus : les annonces disent « 30 min environ », et non « garanti ».
- Selon votre pays et votre catégorie, Google peut exiger une **vérification de l'annonceur** pour les services de dépannage à domicile : faites-la dès qu'elle est demandée, sinon les annonces sont limitées.
