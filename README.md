# Artisans France Plomberie – Toulouse

Site statique hébergé sur Netlify : https://plomberietoulouse.artisansfrance.com

## Structure

| Page | URL |
|---|---|
| Accueil : plombier urgence Toulouse | `/` |
| Fuite d'eau | `/fuite-d-eau-toulouse/` |
| Recherche de fuite | `/recherche-de-fuite-toulouse/` |
| Débouchage canalisation | `/debouchage-canalisation-toulouse/` |
| WC bouché | `/debouchage-wc-toulouse/` |
| Chauffe-eau | `/depannage-chauffe-eau-toulouse/` |
| Dégât des eaux | `/degat-des-eaux-toulouse/` |
| Robinetterie | `/reparation-robinet-toulouse/` |
| Zones d'intervention (Toulouse + 77 communes à 25 km) | `/zones-intervention/` |
| Mentions légales, confidentialité, 404 | `/mentions-legales/`, `/politique-de-confidentialite/`, `/404.html` |

Fichiers SEO : `sitemap.xml` (avec images), `robots.txt` (moteurs et IA autorisés), `llms.txt` et `llms-full.txt` (résumé et contenu complet pour ChatGPT, Claude, Perplexity…).

`assets/style.css` et `assets/main.js` sont partagés par toutes les pages. Les images sont dans `images/` : originaux + versions `-hd.jpg` pour les écrans retina.

## Modifier le contenu

- Accueil : éditer `index.html` directement.
- Pages services, zones, légales, sitemap, llms : éditer `tools/site_data.py` (textes, communes, quartiers), puis lancer `python3 tools/build.py`.
- Campagne Google Ads : éditer `tools/build_ads.py`, puis lancer `python3 tools/build_ads.py`. Voir `google-ads/GUIDE-CAMPAGNE.md`.

## Pour être premier sur Google : à faire hors du site

Le site est optimisé techniquement. Pour la carte Google (le « pack local », les 3 résultats avec la carte), qui capte la majorité des appels, ce qui compte le plus se passe ailleurs :

1. **Google Search Console** : ajouter le domaine, puis soumettre `https://plomberietoulouse.artisansfrance.com/sitemap.xml`. Demander l'indexation de l'accueil et des 7 pages services.
2. **Fiche Google Business Profile** (indispensable pour la carte) : catégorie principale « Plombier », catégories secondaires (« Service de débouchage de canalisations », « Service de détection de fuites »…), zone desservie Toulouse + communes, horaires 24h/24, même nom, même numéro et même site que sur le site, photos réelles, publications chaque semaine.
3. **Avis Google** : demander un avis après chaque intervention (lien direct par SMS). Le nombre, la fréquence et les mots-clés des avis (« fuite », « Blagnac »…) sont le premier facteur du classement local.
4. **Annuaires (citations NAP)** : PagesJaunes, Bing Places, Apple Plans, Yelp, Hoodspot, 118000… avec exactement le même nom, téléphone et site.
5. **Liens entrants** : partenariats locaux (agences immobilières, syndics, assureurs), articles de presse locale.

> Personne ne peut garantir une 1re place sur Google. Avec ce site, une fiche Google complète et des avis réguliers, vous mettez toutes les chances de votre côté. Les premiers effets apparaissent en général après quelques semaines à quelques mois.
