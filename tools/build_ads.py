# -*- coding: utf-8 -*-
"""Génère la campagne Google Ads Search (CPC manuel) dans google-ads/.

Usage : python3 tools/build_ads.py
Produit des fichiers CSV importables dans Google Ads Editor
(Compte > Importer > Coller du texte / Depuis un fichier) et vérifie
les limites de caractères de Google (titres 30, descriptions 90, chemins 15).
"""
import csv
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from site_data import SITE, COMMUNES  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "google-ads")
BASE = SITE["base_url"]

C1 = "Search - Plombier Toulouse - Urgence"
C2 = "Search - Plombier Communes 25 km"

# ---------------------------------------------------------------------------
# Groupes d'annonces : (campagne, nom, url, enchère exacte, enchère expression, mots-clés, titres, descriptions, chemin1, chemin2)
# Les enchères sont des points de départ (en €), à ajuster après 7 à 14 jours.
# ---------------------------------------------------------------------------
COMMON_DESC = [
    "Plombier disponible 24h/24 et 7j/7, nuit, week-end et jours fériés. Appelez maintenant !",
    "Devis écrit remis sur place avant travaux. Rien ne commence sans votre accord.",
    "Toulouse et 25 km autour : Blagnac, Colomiers, Tournefeuille, Balma, Muret...",
    "Facture détaillée pour votre assurance. Paiement CB, espèces ou chèque.",
]

AD_GROUPS = [
    (C1, "Plombier Urgence Toulouse", "/", 7.50, 6.00,
     ["plombier urgence toulouse", "urgence plombier toulouse", "plombier urgent toulouse", "sos plombier toulouse",
      "plombier 24h 24 toulouse", "plombier 24 24 toulouse", "plombier de garde toulouse", "plombier nuit toulouse",
      "plombier dimanche toulouse", "plombier week end toulouse", "plombier jour ferie toulouse", "depannage plomberie urgence toulouse",
      "plombier urgence 31", "plombier urgence haute garonne"],
     ["Plombier Urgence Toulouse", "SOS Plombier 24h/24 7j/7", "Plombier en 30 min Environ", "Appelez le 09 70 70 71 29",
      "Devis Écrit Avant Travaux", "Plombier Nuit et Week-end", "Intervention Rapide", "Dépannage Plomberie Urgent",
      "Disponible Dimanche et Férié", "Fuite, Bouchon, Chauffe-eau", "Plombiers Qualifiés", "Facture pour l'Assurance",
      "Toulouse et 25 km Autour", "Un Plombier Vous Répond", "Paiement CB Accepté"],
     ["Urgence plomberie à Toulouse ? Un plombier se déplace rapidement, de jour comme de nuit.",
      "Fuite d'eau, WC bouché, chauffe-eau en panne : intervention 24h/24 à Toulouse et autour."] + COMMON_DESC[1:3],
     "Plombier", "Urgence"),

    (C1, "Plombier Toulouse", "/", 6.00, 4.80,
     ["plombier toulouse", "plombier a toulouse", "plombier toulouse 31", "plombier 31000", "plombier 31", "artisan plombier toulouse",
      "entreprise plomberie toulouse", "plomberie toulouse", "depannage plomberie toulouse", "plombier depannage toulouse",
      "plombier toulouse centre", "bon plombier toulouse", "plombier toulouse devis", "plombier sanitaire toulouse"],
     ["Plombier à Toulouse 24h/24", "Dépannage Plomberie Toulouse", "Devis Gratuit Avant Travaux", "Appelez le 09 70 70 71 29",
      "Plombier en 30 min Environ", "Tous Quartiers de Toulouse", "Fuite, Bouchon, Chauffe-eau", "Intervention Rapide",
      "Plombiers Qualifiés", "Toutes Marques", "Facture pour l'Assurance", "Disponible 7j/7",
      "Toulouse et 25 km Autour", "Prix Annoncé Avant Travaux", "Paiement CB Accepté"],
     ["Votre plombier à Toulouse : fuite, débouchage, chauffe-eau. Intervention 24h/24 et 7j/7.",
      "Un plombier qualifié évalue votre panne au téléphone et se déplace avec le bon matériel."] + COMMON_DESC[1:3],
     "Plombier", "Toulouse"),

    (C1, "Plombier Pres de Moi", "/", 5.50, 0,
     ["plombier", "plombier urgence", "plombier pres de moi", "plombier autour de moi", "plombier proche de moi",
      "plombier ouvert maintenant", "sos plombier", "urgence plombier", "depannage plomberie", "plombier 24h 24",
      "plombier de garde", "plombier dimanche", "plombier nuit"],
     ["Plombier Près de Chez Vous", "Plombier Urgence 24h/24", "Intervention Rapide", "Appelez le 09 70 70 71 29",
      "Devis Écrit Avant Travaux", "Plombier Disponible Maintenant", "Nuit, Week-end et Fériés", "Toulouse et 25 km Autour",
      "Fuite, Bouchon, Chauffe-eau", "Plombiers Qualifiés", "Facture pour l'Assurance", "Un Plombier Vous Répond",
      "SOS Plombier Toulouse", "Toutes Marques", "Paiement CB Accepté"],
     ["Besoin d'un plombier maintenant ? Nous intervenons à Toulouse et 25 km autour, 24h/24.",
      COMMON_DESC[0], COMMON_DESC[1], COMMON_DESC[3]],
     "Plombier", "Urgence"),

    (C1, "Fuite d'eau", "/fuite-d-eau-toulouse/", 5.00, 4.00,
     ["fuite d'eau toulouse", "fuite eau toulouse", "plombier fuite d'eau toulouse", "reparation fuite d'eau toulouse",
      "fuite d'eau urgence", "fuite d'eau plombier", "fuite canalisation toulouse", "fuite tuyau toulouse", "fuite sous evier",
      "fuite chasse d'eau", "reparer fuite d'eau", "fuite d'eau appartement", "fuite d'eau plafond", "fuite d'eau maison"],
     ["Fuite d'Eau à Toulouse ?", "Plombier Fuite d'Eau 24h/24", "Fuite Stoppée Rapidement", "Appelez le 09 70 70 71 29",
      "Réparation Dès le 1er Passage", "Devis Écrit Avant Travaux", "Coupez l'Eau et Appelez-Nous", "Plombier en 30 min Environ",
      "Canalisation, Flexible, Joint", "Facture pour l'Assurance", "Nuit, Week-end et Fériés", "Toulouse et 25 km Autour",
      "Intervention Rapide", "Plombiers Qualifiés", "Fuite Sous Évier ou Plafond"],
     ["Fuite d'eau ? Coupez l'eau et appelez : un plombier stoppe la fuite et répare, 24h/24.",
      "Flexible, joint, raccord ou canalisation : réparé dès le premier passage le plus souvent."] + COMMON_DESC[1:3],
     "Fuite-d-eau", "Toulouse"),

    (C1, "Recherche de fuite", "/recherche-de-fuite-toulouse/", 4.50, 3.60,
     ["recherche de fuite toulouse", "recherche fuite toulouse", "detection fuite toulouse", "detection de fuite d'eau toulouse",
      "recherche de fuite non destructive", "recherche fuite non destructive toulouse", "recherche de fuite d'eau", "fuite d'eau cachee",
      "detection fuite canalisation", "recherche fuite plancher chauffant", "camera thermique fuite", "recherche de fuite assurance",
      "fuite d'eau compteur qui tourne", "fuite d'eau introuvable"],
     ["Recherche de Fuite Toulouse", "Détection Sans Casse", "Fuite Cachée ? On la Trouve", "Caméra Thermique, Gaz Traceur",
      "Rapport pour l'Assurance", "Appelez le 09 70 70 71 29", "Recherche Non Destructive", "Devis Écrit Avant Travaux",
      "Fuite Sous Dalle ou Mur", "Plancher Chauffant", "Intervention Rapide", "Toulouse et 25 km Autour",
      "Techniciens Équipés", "Compteur Qui Tourne ?", "Disponible 7j/7"],
     ["Fuite d'eau cachée ? Localisation précise sans casse : caméra thermique, gaz traceur.",
      "Rapport détaillé avec photos pour votre déclaration de sinistre dégât des eaux."] + COMMON_DESC[1:3],
     "Recherche-fuite", "Toulouse"),

    (C1, "Debouchage canalisation", "/debouchage-canalisation-toulouse/", 5.00, 4.00,
     ["debouchage canalisation toulouse", "deboucher canalisation toulouse", "canalisation bouchee toulouse", "debouchage toulouse",
      "debouchage evier toulouse", "evier bouche", "douche bouchee", "baignoire bouchee", "lavabo bouche", "hydrocurage toulouse",
      "plombier debouchage toulouse", "canalisation bouchee urgence", "colonne bouchee", "debouchage canalisation urgence"],
     ["Débouchage Canalisation", "Canalisation Bouchée ?", "Débouchage 24h/24 Toulouse", "Appelez le 09 70 70 71 29",
      "Évier, Douche, Baignoire", "Furet et Hydrocurage", "Devis Écrit Avant Travaux", "Intervention Rapide",
      "Inspection Caméra", "Nuit, Week-end et Fériés", "Toulouse et 25 km Autour", "Débouchage Propre",
      "Plombiers Qualifiés", "Refoulement ? On Intervient", "Paiement CB Accepté"],
     ["Évier, douche ou canalisation bouchée ? Débouchage au furet ou par hydrocurage, 24h/24.",
      "Bouchons répétés ? Inspection caméra pour trouver la cause et régler le problème."] + COMMON_DESC[1:3],
     "Debouchage", "Toulouse"),

    (C1, "WC bouche", "/debouchage-wc-toulouse/", 4.50, 3.60,
     ["wc bouche toulouse", "toilettes bouchees toulouse", "debouchage wc toulouse", "deboucher wc toulouse", "wc bouche urgence",
      "toilette bouchee", "wc bouche", "debouchage toilettes", "sanibroyeur bouche", "sanibroyeur en panne toulouse",
      "plombier wc bouche", "wc qui deborde"],
     ["WC Bouché à Toulouse ?", "Débouchage WC 24h/24", "Toilettes Bouchées ?", "Appelez le 09 70 70 71 29",
      "Intervention Propre", "Sanibroyeur Bloqué ?", "Devis Écrit Avant Travaux", "Intervention Rapide",
      "Nuit, Week-end et Fériés", "Toulouse et 25 km Autour", "Plombier en 30 min Environ", "Plombiers Qualifiés",
      "Paiement CB Accepté", "Débouchage Toilettes", "WC Qui Déborde ?"],
     ["WC bouché ou qui déborde ? Un plombier débouche vos toilettes rapidement, 24h/24.",
      "Débouchage et dépannage de sanibroyeur toutes marques, intervention propre."] + COMMON_DESC[1:3],
     "WC-bouche", "Toulouse"),

    (C1, "Chauffe-eau", "/depannage-chauffe-eau-toulouse/", 4.50, 3.60,
     ["chauffe eau en panne toulouse", "depannage chauffe eau toulouse", "reparation chauffe eau toulouse", "ballon d'eau chaude en panne",
      "plus d'eau chaude", "chauffe eau qui fuit", "cumulus en panne", "remplacement chauffe eau toulouse", "changer chauffe eau toulouse",
      "plombier chauffe eau toulouse", "chauffe eau ne chauffe plus", "groupe de securite chauffe eau fuit", "ballon eau chaude toulouse",
      "chauffe eau thermodynamique panne"],
     ["Chauffe-eau en Panne ?", "Dépannage Chauffe-eau 24h/24", "Plus d'Eau Chaude ?", "Appelez le 09 70 70 71 29",
      "Toutes Marques", "Atlantic, Thermor, Ariston", "Réparation ou Remplacement", "Devis Écrit Avant Travaux",
      "Ballon d'Eau Chaude", "Chauffe-eau Qui Fuit ?", "Toulouse et 25 km Autour", "Intervention Rapide",
      "Plombiers Qualifiés", "Résistance, Thermostat", "Paiement CB Accepté"],
     ["Plus d'eau chaude ? Dépannage et remplacement de chauffe-eau toutes marques, 24h/24.",
      "Résistance, thermostat, groupe de sécurité : diagnostic et devis clair sur place."] + COMMON_DESC[1:3],
     "Chauffe-eau", "Toulouse"),

    (C1, "Degat des eaux", "/degat-des-eaux-toulouse/", 4.50, 3.60,
     ["degat des eaux toulouse", "degat des eaux plombier", "degat des eaux urgence", "inondation appartement plombier",
      "rupture canalisation", "tuyau eclate", "tuyau perce", "flexible eclate", "degat des eaux voisin", "plombier degat des eaux toulouse",
      "infiltration d'eau plafond"],
     ["Dégât des Eaux à Toulouse ?", "Plombier Urgence 24h/24", "Fuite Stoppée Rapidement", "Appelez le 09 70 70 71 29",
      "Rapport pour l'Assurance", "Tuyau Éclaté ? On Intervient", "Devis Écrit Avant Travaux", "Nuit, Week-end et Fériés",
      "Recherche de Fuite", "Toulouse et 25 km Autour", "Intervention Rapide", "Plombiers Qualifiés",
      "Facture Détaillée", "Coupez l'Eau et Appelez", "Maison ou Appartement"],
     ["Dégât des eaux : on stoppe la fuite, on sécurise et on répare. Plombier 24h/24.",
      "Facture et rapport d'intervention détaillés pour votre déclaration à l'assurance."] + COMMON_DESC[1:3],
     "Degat-des-eaux", "Toulouse"),

    (C1, "Robinet", "/reparation-robinet-toulouse/", 2.50, 2.00,
     ["reparation robinet toulouse", "robinet qui fuit toulouse", "mitigeur qui fuit", "changer robinet toulouse",
      "remplacement mitigeur toulouse", "robinet casse", "robinet thermostatique douche fuit", "robinet d'arret fuit",
      "plombier robinet toulouse", "chasse d'eau qui fuit"],
     ["Robinet Qui Fuit ?", "Réparation Robinet Toulouse", "Mitigeur, Robinet, Chasse", "Appelez le 09 70 70 71 29",
      "Toutes Marques", "Grohe, Hansgrohe, Roca", "Devis Écrit Avant Travaux", "Remplacement Rapide",
      "Robinet Thermostatique", "Toulouse et 25 km Autour", "Intervention Rapide", "Plombiers Qualifiés",
      "Robinet d'Arrêt Grippé ?", "Chasse d'Eau Qui Fuit ?", "Paiement CB Accepté"],
     ["Robinet qui goutte, mitigeur cassé, chasse d'eau qui fuit : réparation ou remplacement.",
      "Joint, cartouche ou robinet complet : le plombier vous conseille et vous remet un devis."] + COMMON_DESC[1:3],
     "Robinet", "Toulouse"),
]

# Campagne communes : un groupe par commune principale + un groupe « autres communes »
MAIN_COMMUNES = ["Blagnac", "Colomiers", "Tournefeuille", "Balma", "L'Union", "Muret", "Cugnaux", "Ramonville-Saint-Agne",
                 "Saint-Orens-de-Gameville", "Plaisance-du-Touch", "Castanet-Tolosan", "Portet-sur-Garonne", "Villeneuve-Tolosane",
                 "Saint-Jean", "Aucamville", "Labège", "Fenouillet", "Launaguet", "Castelginest", "Cornebarrieu", "Pibrac"]


def kw_name(n):
    """Nom de commune tel que tapé dans Google (minuscules, sans apostrophe ni tiret)."""
    import unicodedata
    n = unicodedata.normalize("NFD", n.lower())
    n = "".join(ch for ch in n if unicodedata.category(ch) != "Mn")
    return n.replace("'", " ").replace("-", " ")


def short(n, limit):
    """Nom court pour les titres (ex. « Ramonville » pour Ramonville-Saint-Agne)."""
    alias = {"Ramonville-Saint-Agne": "Ramonville", "Saint-Orens-de-Gameville": "Saint-Orens", "Plaisance-du-Touch": "Plaisance-du-Touch",
             "Villeneuve-Tolosane": "Villeneuve-Tolosane", "Portet-sur-Garonne": "Portet", "Castanet-Tolosan": "Castanet"}
    n2 = alias.get(n, n)
    return n2 if len(n2) <= limit else n2.split("-")[0]


def commune_group(name):
    cp = next(c[1] for c in COMMUNES if c[0] == name)
    k = kw_name(name)
    s = short(name, 19)
    kws = ["plombier %s" % k, "plombier urgence %s" % k, "plombier a %s" % k, "plombier %s %s" % (k, cp), "plomberie %s" % k,
           "depannage plomberie %s" % k, "fuite d'eau %s" % k, "debouchage %s" % k, "wc bouche %s" % k, "chauffe eau %s" % k,
           "recherche de fuite %s" % k]
    def fit(limit, *options):
        return next(o for o in options if len(o) <= limit)
    heads = ["Plombier %s" % s, fit(30, "Plombier Urgence %s" % s, "Urgence Plombier %s" % s, "SOS Plombier %s" % s, "Urgence %s" % s),
             fit(30, "Plombier à %s 24h/24" % s, "Plombier %s 24h/24" % s, "%s 24h/24" % s),
             "Appelez le 09 70 70 71 29", "Devis Écrit Avant Travaux", "Intervention Rapide", "Fuite, Bouchon, Chauffe-eau",
             "Nuit, Week-end et Fériés", "Plombiers Qualifiés", "Facture pour l'Assurance", "SOS Plombier 24h/24 7j/7",
             fit(30, "Dépannage Plomberie %s" % s, "Dépannage %s" % s, "Plomberie %s" % s), "Toutes Marques", "Paiement CB Accepté",
             fit(30, "Plombier %s (%s)" % (s, cp), "Plombier %s" % cp)]
    descs = [fit(90, "Plombier à %s (%s) disponible 24h/24 : fuite d'eau, débouchage, chauffe-eau." % (s, cp),
                 "Plombier à %s (%s) 24h/24 : fuite d'eau, débouchage, chauffe-eau." % (s, cp),
                 "Plombier à %s 24h/24 : fuite d'eau, débouchage, chauffe-eau." % s),
             fit(90, "Un plombier se déplace à %s rapidement, de jour comme de nuit. Appelez !" % s,
                 "Plombier à %s rapidement, de jour comme de nuit. Appelez maintenant !" % s,
                 "Plombier à %s jour et nuit. Appelez maintenant !" % s),
             COMMON_DESC[1], COMMON_DESC[3]]
    return (C2, "Plombier %s" % name, "/", 4.00, 3.20, kws, heads, descs, "Plombier", short(name, 15).replace(" ", "-"))


def autres_group():
    others = [c for c in COMMUNES if c[0] not in MAIN_COMMUNES]
    kws = []
    for c in others:
        k = kw_name(c[0])
        kws += ["plombier %s" % k, "plombier urgence %s" % k]
    heads = ["Plombier Près de Chez Vous", "Plombier Urgence 24h/24", "Toulouse et 25 km Autour", "Appelez le 09 70 70 71 29",
             "Devis Écrit Avant Travaux", "Intervention Rapide", "Fuite, Bouchon, Chauffe-eau", "Nuit, Week-end et Fériés",
             "Plombiers Qualifiés", "Facture pour l'Assurance", "SOS Plombier Haute-Garonne", "Plombier dans Votre Commune",
             "Toutes Marques", "Paiement CB Accepté", "Dépannage Plomberie 7j/7"]
    descs = ["Plombier d'urgence dans votre commune, à 25 km autour de Toulouse, 24h/24 et 7j/7.",
             "Fuite d'eau, WC bouché, chauffe-eau en panne : un plombier se déplace rapidement.",
             COMMON_DESC[1], COMMON_DESC[3]]
    return (C2, "Plombier Autres communes", "/zones-intervention/", 3.50, 2.80, kws, heads, descs, "Plombier", "Haute-Garonne")


NEGATIVES = [
    # Emploi / formation
    "emploi", "offre d'emploi", "recrutement", "recrute", "embauche", "salaire", "salaires", "cdi", "cdd", "interim", "interimaire",
    "alternance", "apprenti", "apprentissage", "stage", "stagiaire", "formation", "cap plombier", "bac pro", "devenir plombier",
    "ecole", "cours", "metier", "fiche metier", "candidature", "cv", "pole emploi", "france travail", "indeed", "auto entrepreneur",
    # Bricolage / do it yourself
    "tuto", "tutoriel", "comment", "video", "youtube", "soi meme", "moi meme", "diy", "astuce", "astuces", "bicarbonate", "vinaigre",
    "schema", "notice", "mode d'emploi", "pdf", "norme", "dtu",
    # Achat de matériel / magasins
    "leroy merlin", "castorama", "brico depot", "bricomarche", "mr bricolage", "manomano", "amazon", "cedeo", "point p", "brossette",
    "outil", "outils", "outillage", "piece detachee", "pieces detachees", "acheter", "achat", "vente", "occasion", "location",
    "pvc prix", "tube per", "pince", "cle a molette", "furet manuel", "ventouse", "destop", "deboucheur",
    # Hors sujet / autres métiers
    "mario", "jeu", "jeux", "film", "dessin", "coloriage", "definition", "wikipedia", "synonyme", "humour", "blague",
    "electricien", "serrurier", "climatisation", "pompe a chaleur", "piscine", "vidange fosse septique", "fosse septique",
    "ramonage", "chaudiere gaz entretien", "panneau solaire",
    # Gratuit / plaintes
    "arnaque", "plainte", "litige", "avis negatif", "escroquerie",
    # Autres villes (hors zone)
    "paris", "lyon", "marseille", "bordeaux", "montpellier", "nice", "nantes", "lille", "strasbourg", "albi", "montauban",
    "castres", "carcassonne", "pamiers", "foix", "auch", "tarbes", "pau", "agen", "rodez", "cahors", "saint gaudens", "revel",
]

SITELINKS = [
    ("Fuite d'eau", "/fuite-d-eau-toulouse/", "Fuite stoppée rapidement", "Réparation 24h/24"),
    ("Recherche de fuite", "/recherche-de-fuite-toulouse/", "Détection sans casse", "Rapport pour l'assurance"),
    ("Débouchage canalisation", "/debouchage-canalisation-toulouse/", "Évier, douche, baignoire", "Furet et hydrocurage"),
    ("WC bouché", "/debouchage-wc-toulouse/", "Débouchage de toilettes", "Sanibroyeur toutes marques"),
    ("Chauffe-eau en panne", "/depannage-chauffe-eau-toulouse/", "Plus d'eau chaude ?", "Toutes marques"),
    ("Dégât des eaux", "/degat-des-eaux-toulouse/", "Intervention d'urgence", "Facture pour l'assurance"),
    ("Devis gratuit en ligne", "/#contact", "Réponse rapide", "Sans engagement"),
    ("Zones d'intervention", "/zones-intervention/", "Toulouse et 25 km autour", "Tous les quartiers"),
]
CALLOUTS = ["Disponible 24h/24 7j/7", "Devis Avant Travaux", "Intervention Rapide", "Nuit, Week-end, Fériés", "Toutes Marques",
            "Paiement CB Accepté", "Facture pour l'Assurance", "Plombiers Qualifiés", "Détection Sans Casse", "Toulouse + 25 km"]
SNIPPET_SERVICES = ["Fuite d'eau", "Recherche de fuite", "Débouchage", "WC bouché", "Chauffe-eau", "Dégât des eaux", "Robinetterie"]


def check(label, items, limit):
    for t in items:
        if len(t) > limit:
            raise SystemExit("Trop long (%d > %d) – %s : %r" % (len(t), limit, label, t))


def main():
    os.makedirs(OUT, exist_ok=True)
    groups = AD_GROUPS + [commune_group(n) for n in MAIN_COMMUNES] + [autres_group()]

    for g in groups:
        camp, name, url, bex, bph, kws, heads, descs, p1, p2 = g
        check(name + " titres", heads, 30)
        check(name + " descriptions", descs, 90)
        check(name + " chemins", [p1, p2], 15)
        assert len(heads) == 15, (name, len(heads))
        assert len(descs) == 4, (name, len(descs))
        assert len(set(h.lower() for h in heads)) == 15, ("titres en double", name)
    check("liens annexes", [s[0] for s in SITELINKS], 25)
    check("liens annexes desc", [d for s in SITELINKS for d in s[2:]], 35)
    check("accroches", CALLOUTS, 25)
    check("extrait", SNIPPET_SERVICES, 25)

    def w(name, header, rows):
        with open(os.path.join(OUT, name), "w", encoding="utf-8-sig", newline="") as f:
            wr = csv.writer(f)
            wr.writerow(header)
            wr.writerows(rows)

    # 1. Campagnes
    w("1-campagnes.csv", ["Campaign", "Campaign Type", "Networks", "Budget", "Budget type", "Bid Strategy Type", "Languages", "Location", "Campaign Status"],
      [[C1, "Search", "Google search", "50.00", "Daily", "Manual CPC", "fr", "Toulouse (rayon 25 km)", "Paused"],
       [C2, "Search", "Google search", "20.00", "Daily", "Manual CPC", "fr", "Toulouse (rayon 25 km)", "Paused"]])

    # 2. Mots-clés (exact + expression) avec enchères
    rows = []
    n_kw = 0
    for camp, name, url, bex, bph, kws, *_ in groups:
        for k in kws:
            rows.append([camp, name, k, "Exact", "%.2f" % bex, BASE + url])
            n_kw += 1
            if bph:
                rows.append([camp, name, k, "Phrase", "%.2f" % bph, BASE + url])
                n_kw += 1
    w("2-mots-cles.csv", ["Campaign", "Ad Group", "Keyword", "Criterion Type", "Max CPC", "Final URL"], rows)

    # 3. Groupes d'annonces
    w("3-groupes-annonces.csv", ["Campaign", "Ad Group", "Max CPC", "Ad Group Status"],
      [[g[0], g[1], "%.2f" % g[3], "Enabled"] for g in groups])

    # 4. Annonces responsives (RSA)
    head = ["Campaign", "Ad Group", "Ad type"] + ["Headline %d" % i for i in range(1, 16)] + ["Headline 1 position"] + \
           ["Description %d" % i for i in range(1, 5)] + ["Path 1", "Path 2", "Final URL"]
    rows = []
    for camp, name, url, bex, bph, kws, heads, descs, p1, p2 in groups:
        rows.append([camp, name, "Responsive search ad"] + heads + ["1"] + descs + [p1, p2, BASE + url])
    w("4-annonces-rsa.csv", head, rows)

    # 5. Mots-clés négatifs (niveau campagne, en expression)
    rows = [[c, n, "Campaign Negative Phrase"] for c in (C1, C2) for n in NEGATIVES]
    w("5-mots-cles-negatifs.csv", ["Campaign", "Keyword", "Criterion Type"], rows)

    # 6. Composants (extensions)
    rows = [["Sitelink", c, s[0], s[2], s[3], BASE + s[1]] for c in (C1, C2) for s in SITELINKS]
    rows += [["Callout", c, t, "", "", ""] for c in (C1, C2) for t in CALLOUTS]
    rows += [["Structured snippet (Services)", c, "; ".join(SNIPPET_SERVICES), "", "", ""] for c in (C1, C2)]
    rows += [["Call", c, SITE["phone_display"], "Pays : France", "Rapports d'appels : activés", "Conversion : appel >= 60 s"] for c in (C1, C2)]
    w("6-composants-extensions.csv", ["Type", "Campaign", "Texte", "Ligne 1", "Ligne 2", "URL / Option"], rows)

    write_xlsx(groups, n_kw)
    write_single_import(groups)
    write_copy_page(groups)
    print("%d groupes d'annonces, %d mots-clés, %d négatifs : OK (limites de caractères vérifiées)" % (len(groups), n_kw, len(NEGATIVES)))


def write_copy_page(groups):
    """Page HTML « copier-coller » : un bouton Copier sur chaque bloc."""
    import html as H
    esc = H.escape
    n = [0]

    def uid():
        n[0] += 1
        return "b%d" % n[0]

    def block(label, text, rows=None, mono=True):
        i = uid()
        lines = text.count("\n") + 1
        r = rows or min(max(lines, 1), 12)
        return ('<div class="blk"><div class="blk-head"><span class="lbl">%s</span>'
                '<button type="button" class="copy" data-target="%s">Copier</button></div>'
                '<textarea id="%s" class="%s" rows="%d" readonly spellcheck="false">%s</textarea></div>'
                % (esc(label), i, i, "mono" if mono else "", r, esc(text)))

    def field(label, text, limit=None):
        i = uid()
        cnt = ('<span class="cnt%s">%d/%d</span>' % (" over" if len(text) > limit else "", len(text), limit)) if limit else ""
        return ('<li class="fld"><span class="fl">%s</span><span class="fv" id="%s">%s</span>%s'
                '<button type="button" class="copy sm" data-target="%s">Copier</button></li>' % (esc(label), i, esc(text), cnt, i))

    # Fichier Editor complet en texte tabulé (Importer > Coller du texte)
    import io
    buf = io.StringIO()
    with open(os.path.join(OUT, "CREER-LA-CAMPAGNE-import-google-ads-editor.csv"), encoding="utf-8-sig") as f:
        for r in csv.reader(f):
            buf.write("\t".join(r) + "\n")
    tsv = buf.getvalue().rstrip("\n")

    camp_cards = []
    for camp, budget in ((C1, "50"), (C2, "20")):
        gs = [g for g in groups if g[0] == camp]
        settings = "".join([
            field("Nom de la campagne", camp),
            field("Budget quotidien (€)", budget),
            field("Stratégie d'enchères", "CPC manuel"),
            field("Zone", "Toulouse, France – rayon 25 km"),
            field("Langue", "Français"),
        ])
        ag_html = []
        for g in gs:
            _, name, url, bex, bph, kws, heads, descs, p1, p2 = g
            kw_exact = ["[%s]" % k for k in kws]
            kw_phrase = ['"%s"' % k for k in kws] if bph else []
            kw_lines = kw_exact + kw_phrase
            heads_html = "".join(field("Titre %d%s" % (i, " · épingler en 1" if i == 1 else ""), h, 30) for i, h in enumerate(heads, 1))
            desc_html = "".join(field("Description %d" % i, d, 90) for i, d in enumerate(descs, 1))
            bids = "Enchère exacte %.2f € · expression %.2f €" % (bex, bph) if bph else "Enchère %.2f € (exact uniquement)" % bex
            ag_html.append(
                '<details class="ag"><summary><span class="agn">%s</span><span class="agm">%d mots-clés · %s</span></summary>'
                '<div class="ag-body"><ul class="flds">%s%s%s%s%s</ul>%s'
                '<h4>Annonce responsive : 15 titres</h4><ul class="flds">%s</ul>%s'
                '<h4>4 descriptions</h4><ul class="flds">%s</ul></div></details>'
                % (esc(name), len(kw_lines), esc(bids),
                   field("Nom du groupe", name), field("Enchère par défaut (€)", "%.2f" % bex), field("URL finale", BASE + url),
                   field("Chemin 1", p1, 15), field("Chemin 2", p2, 15),
                   block("Mots-clés EXACTS [ ] – %d – enchère %.2f €" % (len(kw_exact), bex), "\n".join(kw_exact)) +
                   (block('Mots-clés EXPRESSION " " – %d – enchère %.2f €' % (len(kw_phrase), bph), "\n".join(kw_phrase)) if kw_phrase else ""),
                   heads_html, block("Les 15 titres d'un coup", "\n".join(heads), rows=6, mono=False),
                   desc_html))
        camp_cards.append(
            '<section class="camp"><h3>%s</h3><ul class="flds">%s</ul>%s<h4>Groupes d\'annonces (%d)</h4>%s</section>'
            % (esc(camp), settings,
               block("Mots-clés négatifs de la campagne (Mots clés > Mots clés à exclure)", "\n".join('"%s"' % x for x in NEGATIVES), rows=8),
               len(gs), "".join(ag_html)))

    sitelinks = "".join(
        '<div class="sl"><ul class="flds">%s%s%s%s</ul></div>' % (field("Texte du lien", t, 25), field("Ligne 1", d1, 35), field("Ligne 2", d2, 35), field("URL finale", BASE + u))
        for t, u, d1, d2 in SITELINKS)

    page = """<title>Campagne Plombier Toulouse</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
/* Mise en page : une colonne de lecture, des blocs « à copier » en police mono, bouton Copier toujours à droite */
:root {
  --bg: #f6f7f6; --panel: #ffffff; --ink: #172723; --muted: #5b6b66; --line: #dfe5e2;
  --accent: #1f5fe0; --accent-ink: #ffffff; --ok: #157a4a; --warn: #b4321f; --field: #f1f4f2;
  --sans: "IBM Plex Sans", system-ui, -apple-system, "Segoe UI", sans-serif;
  --mono: "IBM Plex Mono", ui-monospace, "SFMono-Regular", Menlo, monospace;
}
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
  --bg: #0f1715; --panel: #16211e; --ink: #e5ece9; --muted: #9db0aa; --line: #2a3a35;
  --accent: #6d9cff; --accent-ink: #0b1220; --ok: #4fc58a; --warn: #ff8a73; --field: #1c2a26; color-scheme: dark } }
:root[data-theme="dark"] {
  --bg: #0f1715; --panel: #16211e; --ink: #e5ece9; --muted: #9db0aa; --line: #2a3a35;
  --accent: #6d9cff; --accent-ink: #0b1220; --ok: #4fc58a; --warn: #ff8a73; --field: #1c2a26; color-scheme: dark }
body { background: var(--bg); color: var(--ink); font-family: var(--sans); font-size: 15px; line-height: 1.55; }
.wrap { max-width: 960px; margin: 0 auto; padding-block: 28px 80px;
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }
h1 { font-size: clamp(1.6rem, 4vw, 2.2rem); line-height: 1.1; margin: 0 0 6px; text-wrap: balance; font-weight: 700; }
h2 { font-size: 1.25rem; margin: 40px 0 12px; text-wrap: balance; }
h3 { font-size: 1.1rem; margin: 0 0 12px; }
h4 { font-size: .8rem; text-transform: uppercase; letter-spacing: .08em; color: var(--muted); margin: 22px 0 8px; font-weight: 600; }
p { margin: 0 0 10px; max-width: 68ch; }
.sub { color: var(--muted); margin-bottom: 22px; }
.steps { display: grid; gap: 12px; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); margin: 18px 0 8px; }
.step { background: var(--panel); border: 1px solid var(--line); border-radius: 12px; padding: 16px; min-width: 0; }
.step b { display: block; margin-bottom: 4px; }
.tag { display: inline-block; font-size: .72rem; font-weight: 600; letter-spacing: .06em; text-transform: uppercase; color: var(--ok); margin-bottom: 6px; }
.camp { background: var(--panel); border: 1px solid var(--line); border-radius: 14px; padding: 18px; margin-top: 18px; min-width: 0; }
.blk { margin: 12px 0; min-width: 0; }
.blk-head { display: flex; align-items: center; justify-content: space-between; gap: 10px; margin-bottom: 6px; }
.lbl { font-weight: 600; font-size: .9rem; min-width: 0; }
textarea { width: 100%; box-sizing: border-box; background: var(--field); color: var(--ink); border: 1px solid var(--line); border-radius: 10px;
  padding: 10px 12px; font: 14px/1.5 var(--sans); resize: vertical; white-space: pre; overflow: auto; }
textarea.mono { font-family: var(--mono); font-size: 13px; }
.copy { flex-shrink: 0; background: var(--accent); color: var(--accent-ink); border: 0; border-radius: 8px; padding: 8px 14px;
  font: 600 .85rem var(--sans); cursor: pointer; min-width: 84px; }
.copy.sm { padding: 5px 10px; min-width: 70px; font-size: .78rem; }
.copy:hover { filter: brightness(1.08); }
.copy:focus-visible, summary:focus-visible { outline: 3px solid var(--accent); outline-offset: 2px; }
.copy.done { background: var(--ok); }
.flds { list-style: none; margin: 0; padding: 0; display: flex; flex-direction: column; gap: 6px; }
.fld { display: grid; grid-template-columns: 170px minmax(0, 1fr) auto auto; align-items: center; gap: 10px;
  background: var(--field); border-radius: 8px; padding: 7px 8px 7px 12px; }
.fl { color: var(--muted); font-size: .82rem; }
.fv { font-weight: 500; overflow-wrap: anywhere; min-width: 0; }
.cnt { font: 500 .75rem var(--mono); color: var(--muted); font-variant-numeric: tabular-nums; }
.cnt.over { color: var(--warn); }
details.ag { border: 1px solid var(--line); border-radius: 10px; margin: 8px 0; background: var(--panel); }
details.ag > summary { cursor: pointer; padding: 12px 14px; display: flex; flex-wrap: wrap; gap: 4px 12px; align-items: baseline; list-style: none; }
details.ag > summary::-webkit-details-marker { display: none; }
details.ag > summary::before { content: "▸"; color: var(--accent); }
details.ag[open] > summary::before { content: "▾"; }
.agn { font-weight: 600; }
.agm { color: var(--muted); font-size: .85rem; }
.ag-body { padding: 0 14px 14px; }
.sl { margin-bottom: 10px; }
.note { border-left: 3px solid var(--accent); padding: 8px 12px; background: var(--panel); border-radius: 0 8px 8px 0; margin: 12px 0; }
@media (max-width: 640px) {
  .fld { grid-template-columns: minmax(0, 1fr) auto; }
  .fl { grid-column: 1 / -1; }
  .cnt { justify-self: start; }
}
@media (prefers-reduced-motion: reduce) { * { transition: none !important; } }
</style>
<div class="wrap">
  <h1>Campagne Plombier Toulouse</h1>
  <p class="sub">Google Ads Search · CPC manuel · Toulouse + 25 km · @@ng@@ groupes d'annonces · @@nk@@ mots-clés</p>

  <h2>Méthode 1 : tout créer en un seul coller (Google Ads Editor)</h2>
  <div class="steps">
    <div class="step"><span class="tag">Étape 1</span><b>Copier le bloc ci-dessous</b>Il contient les 2 campagnes, les groupes, les mots-clés avec enchères, les annonces et les négatifs.</div>
    <div class="step"><span class="tag">Étape 2</span><b>Coller dans Editor</b>Google Ads Editor &gt; Compte &gt; <b style="display:inline">Importer &gt; Coller du texte</b> &gt; coller &gt; Traiter &gt; Conserver.</div>
    <div class="step"><span class="tag">Étape 3</span><b>Régler et publier</b>Zone Toulouse + 25 km (option « Présence »), ajustements mobile +20 %, puis Publier. Les campagnes arrivent en pause.</div>
  </div>
  @@tsv@@

  <h2>Méthode 2 : dans l'interface web Google Ads, champ par champ</h2>
  <p>Ouvrez un groupe ci-dessous : chaque valeur a son bouton Copier, dans l'ordre où Google Ads la demande. Les mots-clés se collent tous d'un coup dans le champ « Mots clés » : les crochets [ ] donnent l'exact, les guillemets « " " » l'expression.</p>
  <div class="note"><b>Types de correspondance</b> : <code>[plombier toulouse]</code> = <b>exact</b>, <code>"plombier toulouse"</code> = <b>expression</b>. Collez-les tels quels avec les crochets et les guillemets : Google Ads reconnaît le type tout seul. Les négatifs sont en expression <code>"emploi"</code>. Collez d'abord le bloc exact (enchère par défaut du groupe), puis le bloc expression, et réglez ces mots-clés à l'enchère « expression » indiquée (sélectionner &gt; Modifier &gt; CPC max).</div>
  @@camps@@

  <h2>Composants (extensions) : à ajouter aux 2 campagnes</h2>
  <section class="camp">
    <h3>Liens annexes</h3>@@sitelinks@@
    @@callouts@@
    @@snippets@@
    <ul class="flds">@@call@@</ul>
  </section>
</div>
<script>
(function () {
  function flash(btn, ok) {
    var t = btn.textContent;
    btn.textContent = ok ? "Copié ✓" : "Sélectionné, faites Ctrl+C";
    btn.classList.toggle("done", ok);
    setTimeout(function () { btn.textContent = t; btn.classList.remove("done"); }, 1600);
  }
  function selectEl(el) {
    if (el.select) { el.focus(); el.select(); return; }
    var r = document.createRange(); r.selectNodeContents(el);
    var s = window.getSelection(); s.removeAllRanges(); s.addRange(r);
  }
  document.addEventListener("click", function (e) {
    var btn = e.target.closest && e.target.closest(".copy");
    if (!btn) return;
    var el = document.getElementById(btn.getAttribute("data-target"));
    if (!el) return;
    var text = el.value !== undefined ? el.value : el.textContent;
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(function () { flash(btn, true); }, function () { selectEl(el); flash(btn, false); });
    } else { selectEl(el); flash(btn, false); }
  });
})();
</script>
"""
    for k, v in {
        "ng": len(groups), "nk": sum(len(g[5]) * (2 if g[4] else 1) for g in groups),
        "tsv": block("Texte d'import complet pour Google Ads Editor (%d lignes)" % (tsv.count("\n") + 1), tsv, rows=8),
        "camps": "".join(camp_cards),
        "sitelinks": sitelinks,
        "callouts": block("Accroches (une par ligne)", "\n".join(CALLOUTS), mono=False),
        "snippets": block("Extrait de site : en-tête « Services » (une valeur par ligne)", "\n".join(SNIPPET_SERVICES), mono=False),
        "call": field("Extension d'appel : numéro", SITE["phone_display"]),
    }.items():
        page = page.replace("@@%s@@" % k, str(v))
    with open(os.path.join(OUT, "copier-coller.html"), "w", encoding="utf-8") as f:
        f.write(page)


def write_single_import(groups):
    """Un seul fichier qui crée toute la campagne dans Google Ads Editor
    (Compte > Importer > Depuis un fichier) : campagnes, groupes, mots-clés,
    annonces responsives et mots-clés négatifs."""
    cols = ["Campaign", "Campaign Type", "Networks", "Budget", "Budget type", "Bid Strategy Type", "Languages", "Campaign Status",
            "Ad Group", "Max CPC", "Ad Group Status", "Keyword", "Criterion Type", "Status", "Ad type"] + \
           ["Headline %d" % i for i in range(1, 16)] + ["Headline 1 position"] + ["Description %d" % i for i in range(1, 5)] + \
           ["Path 1", "Path 2", "Final URL"]
    idx = {c: i for i, c in enumerate(cols)}

    def row(**kw):
        r = [""] * len(cols)
        for k, v in kw.items():
            r[idx[k.replace("_", " ")]] = v
        return r

    rows = []
    for camp, budget in ((C1, "50.00"), (C2, "20.00")):
        rows.append(row(Campaign=camp, Campaign_Type="Search", Networks="Google search", Budget=budget, Budget_type="Daily",
                        Bid_Strategy_Type="Manual CPC", Languages="fr", Campaign_Status="Paused"))
    for g in groups:
        rows.append(row(Campaign=g[0], Ad_Group=g[1], Max_CPC="%.2f" % g[3], Ad_Group_Status="Enabled"))
    for camp, name, url, bex, bph, kws, *_ in groups:
        for k in kws:
            rows.append(row(Campaign=camp, Ad_Group=name, Keyword=k, Criterion_Type="Exact", Max_CPC="%.2f" % bex, Status="Enabled", Final_URL=BASE + url))
            if bph:
                rows.append(row(Campaign=camp, Ad_Group=name, Keyword=k, Criterion_Type="Phrase", Max_CPC="%.2f" % bph, Status="Enabled", Final_URL=BASE + url))
    for camp, name, url, bex, bph, kws, heads, descs, p1, p2 in groups:
        r = row(Campaign=camp, Ad_Group=name, Ad_type="Responsive search ad", Status="Enabled", Path_1=p1, Path_2=p2, Final_URL=BASE + url)
        for i, h in enumerate(heads, 1):
            r[idx["Headline %d" % i]] = h
        r[idx["Headline 1 position"]] = "1"
        for i, d in enumerate(descs, 1):
            r[idx["Description %d" % i]] = d
        rows.append(r)
    for camp in (C1, C2):
        for n in NEGATIVES:
            rows.append(row(Campaign=camp, Keyword=n, Criterion_Type="Campaign Negative Phrase"))
    with open(os.path.join(OUT, "CREER-LA-CAMPAGNE-import-google-ads-editor.csv"), "w", encoding="utf-8-sig", newline="") as f:
        wr = csv.writer(f)
        wr.writerow(cols)
        wr.writerows(rows)


def write_xlsx(groups, n_kw):
    """Classeur Excel lisible : un onglet par élément de la campagne."""
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Font, PatternFill
    from openpyxl.utils import get_column_letter

    head_fill = PatternFill("solid", fgColor="1A2E2A")
    head_font = Font(bold=True, color="FFFFFF")
    blue = PatternFill("solid", fgColor="EFF6FF")
    wb = Workbook()

    def sheet(title, header, rows, widths=None, first=False):
        ws = wb.active if first else wb.create_sheet()
        ws.title = title
        ws.append(header)
        for r in rows:
            ws.append(r)
        for c in ws[1]:
            c.fill, c.font = head_fill, head_font
            c.alignment = Alignment(vertical="center", wrap_text=True)
        ws.freeze_panes = "A2"
        ws.auto_filter.ref = ws.dimensions
        for i, wdt in enumerate(widths or [], 1):
            ws.column_dimensions[get_column_letter(i)].width = wdt
        return ws

    # Résumé
    ws = sheet("Résumé", ["Élément", "Valeur"], [], [38, 90], first=True)
    budgets = {C1: 50, C2: 20}
    rows = [
        ("Compte", "Artisans France Plomberie – " + SITE["base_url"]),
        ("Stratégie d'enchères", "CPC manuel (sans requête large)"),
        ("Réseaux", "Réseau de Recherche Google uniquement (décocher Partenaires et Display)"),
        ("Zone", "Toulouse + rayon de 25 km – option « Présence » uniquement"),
        ("Langue", "Français"),
        ("Calendrier", "24h/24, 7j/7"),
        ("Ajustements appareils", "Mobile +20 %, Ordinateur –20 %, Tablette –30 %"),
        ("Ajustements horaires", "19h–8h +15 %, samedi et dimanche +10 %"),
        ("Campagne 1", "%s – budget %d €/jour – %d groupes" % (C1, budgets[C1], sum(1 for g in groups if g[0] == C1))),
        ("Campagne 2", "%s – budget %d €/jour – %d groupes" % (C2, budgets[C2], sum(1 for g in groups if g[0] == C2))),
        ("Mots-clés", "%d (exact + expression)" % n_kw),
        ("Mots-clés négatifs", "%d par campagne" % len(NEGATIVES)),
        ("Conversions à suivre", "Appel depuis l'annonce ≥ 60 s · Clic sur le numéro du site · Formulaire de devis envoyé"),
        ("Téléphone (extension d'appel)", SITE["phone_display"]),
        ("Important", "Les enchères sont des points de départ : à vérifier dans le Planificateur de mots clés puis à ajuster après 7 à 14 jours."),
    ]
    for r in rows:
        ws.append(r)
    for row in ws.iter_rows(min_row=2):
        row[0].font = Font(bold=True)
        row[1].alignment = Alignment(wrap_text=True, vertical="top")

    # Groupes d'annonces
    sheet("Groupes d'annonces", ["Campagne", "Groupe d'annonces", "Enchère exacte (€)", "Enchère expression (€)", "Nb mots-clés", "Page de destination"],
          [[g[0], g[1], g[3], g[4] or "–", len(g[5]), BASE + g[2]] for g in groups], [36, 34, 18, 20, 13, 62])

    # Mots-clés
    rows = []
    for camp, name, url, bex, bph, kws, *_ in groups:
        for k in kws:
            rows.append([camp, name, k, "Exact", "[%s]" % k, bex, BASE + url])
            if bph:
                rows.append([camp, name, k, "Expression", '"%s"' % k, bph, BASE + url])
    ws = sheet("Mots-clés", ["Campagne", "Groupe d'annonces", "Mot-clé", "Correspondance", "Format Google Ads", "CPC max (€)", "URL finale"], rows, [34, 30, 44, 15, 46, 12, 60])
    for c in ws["F"][1:]:
        c.number_format = '0.00 "€"'

    # Annonces : une ligne par élément avec nombre de caractères
    rows = []
    for camp, name, url, bex, bph, kws, heads, descs, p1, p2 in groups:
        for i, h in enumerate(heads, 1):
            rows.append([camp, name, "Titre %d%s" % (i, " (épinglé position 1)" if i == 1 else ""), h, len(h), 30])
        for i, d in enumerate(descs, 1):
            rows.append([camp, name, "Description %d" % i, d, len(d), 90])
        rows.append([camp, name, "Chemin 1", p1, len(p1), 15])
        rows.append([camp, name, "Chemin 2", p2, len(p2), 15])
        rows.append([camp, name, "URL finale", BASE + url, "", ""])
    ws = sheet("Annonces RSA", ["Campagne", "Groupe d'annonces", "Élément", "Texte", "Caractères", "Limite"], rows, [34, 30, 26, 92, 11, 8])
    for row in ws.iter_rows(min_row=2):
        if str(row[2].value).startswith("Description"):
            for c in row:
                c.fill = blue

    # Négatifs
    sheet("Mots-clés négatifs", ["Campagne", "Mot-clé négatif", "Correspondance", "Format Google Ads"],
          [[c, n, "Expression", '"%s"' % n] for c in (C1, C2) for n in NEGATIVES], [36, 34, 16, 36])

    # Extensions
    rows = [["Lien annexe", s[0], s[2], s[3], BASE + s[1]] for s in SITELINKS]
    rows += [["Accroche", t, "", "", ""] for t in CALLOUTS]
    rows += [["Extrait de site (Services)", v, "", "", ""] for v in SNIPPET_SERVICES]
    rows += [["Appel", SITE["phone_display"], "Rapports d'appels activés", "Conversion : appel ≥ 60 s", ""]]
    sheet("Extensions", ["Type", "Texte", "Description 1", "Description 2", "URL"], rows, [26, 30, 30, 30, 62])

    # Format d'import Google Ads Editor (copier-coller)
    head = ["Campaign", "Ad Group", "Ad type"] + ["Headline %d" % i for i in range(1, 16)] + \
           ["Description %d" % i for i in range(1, 5)] + ["Path 1", "Path 2", "Final URL"]
    sheet("Import Editor - RSA", head, [[g[0], g[1], "Responsive search ad"] + g[6] + g[7] + [g[8], g[9], BASE + g[2]] for g in groups])

    wb.save(os.path.join(OUT, "campagne-google-ads-plombier-toulouse.xlsx"))


if __name__ == "__main__":
    main()
