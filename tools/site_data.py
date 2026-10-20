# -*- coding: utf-8 -*-
"""Données du site : entreprise, services, communes et quartiers.

Toutes les pages locales (service × ville) sont générées à partir de ce fichier
par tools/build.py. Pour ajouter une commune ou un service, il suffit de
compléter les listes ci-dessous puis de relancer : python3 tools/build.py
"""

SITE = {
    "base_url": "https://plomberietoulouse.artisansfrance.com",
    "name": "Artisans France Plomberie",
    "phone_display": "09 70 70 71 29",
    "phone_e164": "+33970707129",
    "email_form": "https://formsubmit.co/zakari.sefta1@gmail.com",
    "gtm": "GTM-PZ6QSD93",
    "gtag": "GT-T944WWWS",
    "ads_conversion": "AW-18317420737/2JlZCOOYyfkcEMHRtp5E",
    "lat": "43.6047",
    "lng": "1.4442",
}

# ---------------------------------------------------------------------------
# SERVICES
# Chaque texte peut contenir {ville}, {a_ville} (« à Blagnac »), {cp}, {de_ville}
# ---------------------------------------------------------------------------
SERVICES = [
    {
        "slug": "plombier",
        "name": "Plombier",
        "label": "Plombier d'urgence",
        "h1": "Plombier {a_ville} <span class=\"accent\">24h/24</span>",
        "title": "Plombier {ville} ({cp}) – Urgence 24h/24, devis gratuit",
        "desc": "Plombier {a_ville} ({cp}) disponible 24h/24 et 7j/7 : fuite d'eau, canalisation bouchée, chauffe-eau. Devis avant travaux. Appelez le 09 70 70 71 29.",
        "img": "plombier-agree-toulouse",
        "img_alt": "Plombier d'urgence Artisans France Plomberie intervenant {a_ville}",
        "lead": "Fuite d'eau, WC ou évier bouché, chauffe-eau en panne : un plombier qualifié se déplace {a_ville} jour et nuit, week-end et jours fériés compris. Devis clair avant toute intervention.",
        "intro": [
            "Vous cherchez un <strong>plombier {a_ville}</strong> capable d'intervenir vite et proprement ? Artisans France Plomberie assure le dépannage plomberie {a_ville} ({cp}) et dans les communes voisines, 24 heures sur 24. Un plombier vous répond au téléphone, évalue la situation et se déplace avec le matériel adapté.",
            "Une urgence plomberie n'attend pas. Notre équipe de <strong>plombiers {a_ville}</strong> intervient pour toutes les pannes du quotidien : fuite, engorgement, eau chaude coupée, robinet cassé. Le diagnostic et le devis sont faits sur place, avant le moindre travail.",
            "Besoin d'un <strong>plombier en urgence {a_ville}</strong> ? Nous intervenons en journée comme la nuit, le dimanche et les jours fériés, avec un principe simple : vous connaissez le prix avant que le travail commence, et rien n'est fait sans votre accord.",
        ],
        "sections": [
            ("Nos interventions de plomberie {a_ville}", [
                "<ul><li><strong>Fuite d'eau</strong> sur canalisation, raccord, flexible ou sous un évier</li><li><strong>Recherche de fuite non destructive</strong> (caméra thermique, gaz traceur, test de pression)</li><li><strong>Débouchage</strong> de canalisation, évier, douche, baignoire et WC</li><li><strong>Dépannage de chauffe-eau</strong> électrique, thermodynamique ou au gaz</li><li><strong>Dégât des eaux</strong> : mise en sécurité et rapport pour l'assurance</li><li><strong>Robinetterie</strong> : réparation ou remplacement de robinet, mitigeur, chasse d'eau</li></ul>",
            ]),
            ("Comment se passe votre dépannage", [
                "Vous appelez le <strong>09 70 70 71 29</strong> : un plombier vous pose quelques questions pour comprendre la panne et vous donne les premiers gestes à faire (couper l'eau, couper le chauffe-eau, éponger). Il se déplace ensuite {a_ville} avec l'outillage nécessaire.",
                "Sur place, il établit le diagnostic, vous explique la réparation et vous remet un <strong>devis écrit</strong>. L'intervention ne commence qu'après votre accord. À la fin, vous recevez une facture détaillée, utile en cas de déclaration à votre assurance.",
            ]),
        ],
        "faq": [
            ("Combien de temps faut-il à un plombier pour arriver {a_ville} ?", "Le délai dépend de l'heure et de la circulation. {delai_phrase} Le délai estimé vous est annoncé dès votre appel."),
            ("Intervenez-vous la nuit et le dimanche {a_ville} ?", "Oui. Notre service de plomberie fonctionne 24h/24 et 7j/7, y compris les nuits, week-ends et jours fériés, {a_ville} comme dans toute l'agglomération toulousaine."),
            ("Combien coûte un plombier {a_ville} ?", "Chaque panne est différente. Le plombier établit un devis écrit sur place, avant toute intervention : vous connaissez le prix exact et vous restez libre d'accepter ou non. Pour les dépannages à domicile de plus de 150 € TTC, le devis écrit est d'ailleurs obligatoire."),
            ("Quels moyens de paiement acceptez-vous ?", "Vous pouvez régler par carte bancaire, espèces ou chèque. Une facture détaillée vous est systématiquement remise."),
        ],
    },
    {
        "slug": "fuite-d-eau",
        "name": "Fuite d'eau",
        "label": "Réparation de fuite d'eau",
        "h1": "Fuite d'eau {a_ville} : <span class=\"accent\">plombier en urgence</span>",
        "title": "Fuite d'eau {ville} ({cp}) – Plombier urgence 24h/24",
        "desc": "Fuite d'eau {a_ville} ? Plombier en urgence 24h/24 : on stoppe la fuite et on répare (canalisation, flexible, raccord). Devis avant travaux.",
        "img": "fuite-eau-toulouse",
        "img_alt": "Réparation d'une fuite d'eau par un plombier {a_ville}",
        "lead": "Tuyau qui goutte, flexible qui a lâché, eau qui coule sous l'évier ou au plafond : on stoppe la fuite et on répare, {a_ville} et alentours, 24h/24.",
        "intro": [
            "Une <strong>fuite d'eau {a_ville}</strong> peut vite causer des dégâts importants : parquet gondolé, plafond taché, voisin du dessous inondé. Nos plombiers interviennent en urgence pour stopper l'écoulement, trouver l'origine et réparer durablement.",
            "Flexible percé, joint usé, raccord desserré ou canalisation fissurée : quelle que soit l'origine de votre <strong>fuite d'eau {a_ville}</strong>, un plombier se déplace rapidement avec les pièces courantes pour réparer dès le premier passage dans la plupart des cas.",
            "Vous constatez de l'eau qui coule ou une flaque inexpliquée ? Coupez l'eau et appelez-nous : la <strong>réparation de fuite d'eau {a_ville}</strong> fait partie de nos interventions les plus fréquentes, de jour comme de nuit.",
        ],
        "sections": [
            ("Les fuites que nous réparons", [
                "<ul><li>Fuite sous l'évier ou le lavabo (siphon, flexible, raccord)</li><li>Fuite de chasse d'eau ou de mécanisme de WC</li><li>Fuite sur canalisation cuivre, PER, multicouche ou PVC</li><li>Fuite au niveau du compteur ou du robinet d'arrêt</li><li>Fuite de chauffe-eau (groupe de sécurité, raccords)</li><li>Fuite de robinet ou de mitigeur</li></ul>",
            ]),
            ("Les bons gestes en attendant le plombier", [
                "<ol><li><strong>Coupez l'arrivée d'eau</strong> générale (robinet près du compteur) ou le robinet d'arrêt de l'appareil concerné.</li><li>Si l'eau approche des prises ou du tableau électrique, <strong>coupez l'électricité</strong> de la zone.</li><li>Épongez et protégez vos meubles, prévenez le voisin du dessous si vous êtes en immeuble.</li><li>Prenez des <strong>photos</strong> : elles serviront pour votre assurance.</li></ol>",
            ]),
            ("Facture élevée sans fuite visible ?", [
                "Une consommation anormale sur votre facture ou un compteur qui tourne alors que tout est fermé signale souvent une fuite cachée. Dans ce cas, nous réalisons une <a href=\"/recherche-de-fuite-{ville_slug}/\">recherche de fuite non destructive {a_ville}</a> pour localiser l'origine sans casser.",
            ]),
        ],
        "faq": [
            ("Que faire en cas de fuite d'eau {a_ville} la nuit ?", "Coupez immédiatement l'arrivée d'eau générale puis appelez le 09 70 70 71 29. Un plombier est joignable 24h/24 et se déplace {a_ville} pour stopper la fuite, même la nuit ou le week-end."),
            ("Le plombier peut-il réparer la fuite dès le premier passage ?", "Dans la grande majorité des cas, oui : nos plombiers ont dans leur véhicule les pièces courantes (joints, flexibles, raccords, robinets d'arrêt). Si une pièce spécifique est nécessaire, la fuite est d'abord neutralisée puis la réparation définitive est planifiée."),
            ("Qui paie la réparation d'une fuite d'eau en appartement ?", "Si la fuite provient d'une installation privative (après votre robinet d'arrêt), la réparation est généralement à la charge de l'occupant ou du propriétaire. Une fuite sur une colonne commune relève de la copropriété. Notre facture détaillée vous aide à faire valoir vos droits auprès de votre assurance."),
            ("Combien coûte la réparation d'une fuite d'eau {a_ville} ?", "Le prix dépend de l'origine de la fuite et de son accessibilité. Le plombier vous remet un devis écrit sur place avant toute réparation : vous décidez en connaissance de cause."),
        ],
    },
    {
        "slug": "recherche-de-fuite",
        "name": "Recherche de fuite",
        "label": "Recherche de fuite non destructive",
        "h1": "Recherche de fuite {a_ville} <span class=\"accent\">sans casse</span>",
        "title": "Recherche de fuite {ville} ({cp}) – Détection non destructive",
        "desc": "Recherche de fuite non destructive {a_ville} : caméra thermique, gaz traceur. Fuite localisée sans casse, rapport pour l'assurance.",
        "img": "recherche-de-fuite-toulouse",
        "img_alt": "Recherche de fuite non destructive par caméra thermique {a_ville}",
        "lead": "Fuite cachée dans un mur, sous une dalle ou un carrelage ? Nous la localisons sans casser grâce à la détection non destructive, et vous remettons un rapport pour l'assurance.",
        "intro": [
            "Une tache d'humidité qui s'étend, un compteur qui tourne alors que tout est fermé, une facture d'eau qui explose : ce sont les signes d'une fuite cachée. Notre service de <strong>recherche de fuite {a_ville}</strong> localise précisément l'origine, sans démolir vos murs ni votre carrelage.",
            "La <strong>recherche de fuite non destructive {a_ville}</strong> permet de trouver une fuite encastrée ou enterrée en limitant les travaux au strict minimum. Le plombier n'ouvre qu'à l'endroit exact de la fuite, ce qui réduit fortement le coût total de la réparation.",
            "Fuite sous dalle, dans une cloison, sur un réseau de chauffage au sol ou dans le jardin : nos techniciens réalisent la <strong>détection de fuite {a_ville}</strong> avec des appareils professionnels, puis vous remettent un rapport détaillé utile pour votre assurance.",
        ],
        "sections": [
            ("Nos méthodes de détection", [
                "<ul><li><strong>Caméra thermique</strong> : repère les écarts de température liés à une fuite d'eau chaude ou de chauffage</li><li><strong>Gaz traceur</strong> : un gaz inoffensif est injecté dans le réseau et détecté à sa sortie</li><li><strong>Test de pression</strong> : isole le tronçon de canalisation qui perd de l'eau</li><li><strong>Écoute électro-acoustique</strong> : capte le bruit de l'eau qui s'échappe sous pression</li><li><strong>Inspection caméra</strong> des canalisations d'évacuation</li><li><strong>Humidimètre</strong> : cartographie l'humidité dans les murs et les sols</li></ul>",
            ]),
            ("Un rapport pour votre assurance", [
                "En cas de dégât des eaux, la plupart des contrats d'assurance habitation prévoient la prise en charge de la recherche de fuite (garantie « recherche de fuite »). Nous vous remettons un <strong>rapport de recherche de fuite</strong> avec photos et localisation, à joindre à votre déclaration de sinistre. Vérifiez les conditions de votre contrat auprès de votre assureur.",
            ]),
        ],
        "faq": [
            ("Comment savoir si j'ai une fuite d'eau cachée {a_ville} ?", "Fermez tous les robinets et relevez votre compteur d'eau, puis relevez-le à nouveau une à deux heures plus tard sans utiliser d'eau. S'il a tourné, il y a une fuite. Autres signes : tache d'humidité, moisissures, peinture qui cloque, bruit d'écoulement continu."),
            ("La recherche de fuite non destructive abîme-t-elle mon logement ?", "Non, c'est tout l'intérêt de la méthode : la fuite est localisée sans casser. Seule l'ouverture nécessaire à la réparation est réalisée, à l'endroit exact de la fuite."),
            ("Mon assurance rembourse-t-elle la recherche de fuite ?", "Beaucoup de contrats multirisques habitation prennent en charge la recherche de fuite lorsqu'elle est liée à un dégât des eaux. Nous vous fournissons un rapport détaillé pour faciliter votre déclaration. Les conditions exactes dépendent de votre contrat."),
            ("Intervenez-vous pour une fuite sur plancher chauffant {a_ville} ?", "Oui. La caméra thermique et le gaz traceur sont particulièrement adaptés pour localiser une fuite sur un plancher chauffant ou un réseau de chauffage encastré."),
        ],
    },
    {
        "slug": "debouchage-canalisation",
        "name": "Débouchage canalisation",
        "label": "Débouchage de canalisation",
        "h1": "Débouchage canalisation {a_ville} <span class=\"accent\">24h/24</span>",
        "title": "Débouchage canalisation {ville} ({cp}) – Plombier 24h/24",
        "desc": "Canalisation bouchée {a_ville} ? Débouchage d'évier, douche, colonne par furet ou hydrocurage, 24h/24. Devis avant travaux.",
        "img": "canalisation-bouchee-toulouse",
        "img_alt": "Débouchage de canalisation par un plombier {a_ville}",
        "lead": "Évier qui ne se vide plus, douche qui stagne, mauvaises odeurs, refoulements : nous débouchons vos canalisations {a_ville} rapidement et proprement.",
        "intro": [
            "Une <strong>canalisation bouchée {a_ville}</strong> se manifeste par une eau qui s'évacue lentement, des gargouillis ou des remontées d'odeurs. Quand les produits du commerce ne suffisent plus, nos plombiers interviennent avec du matériel professionnel pour un débouchage efficace.",
            "Graisses dans l'évier, cheveux dans la douche, calcaire ou racines dans les canalisations extérieures : le <strong>débouchage de canalisation {a_ville}</strong> demande la bonne technique selon la cause. Nous intervenons 24h/24, y compris le week-end.",
            "Refoulement dans la douche, évier bouché la veille d'un repas, colonne d'immeuble engorgée : notre service de <strong>débouchage {a_ville}</strong> traite tous les bouchons, de l'évier à la canalisation principale.",
        ],
        "sections": [
            ("Nos techniques de débouchage", [
                "<ul><li><strong>Ventouse et pompe manuelle</strong> pour les bouchons légers</li><li><strong>Furet électrique</strong> pour les bouchons tenaces dans les canalisations intérieures</li><li><strong>Hydrocurage haute pression</strong> pour nettoyer les parois et éliminer graisses et dépôts</li><li><strong>Inspection caméra</strong> pour localiser un bouchon récurrent ou une canalisation cassée</li></ul>",
            ]),
            ("Évitez les produits chimiques agressifs", [
                "Les déboucheurs à base de soude ou d'acide peuvent abîmer les joints et les canalisations anciennes, et sont dangereux en cas de projection. Si un premier essai à la ventouse ne donne rien, il vaut mieux faire appel à un plombier.",
                "Pour un WC bouché, consultez notre page dédiée au <a href=\"/debouchage-wc-{ville_slug}/\">débouchage de WC {a_ville}</a>.",
            ]),
        ],
        "faq": [
            ("Pourquoi ma canalisation se bouche-t-elle souvent ?", "Les bouchons répétés viennent souvent d'un dépôt de graisse ou de calcaire sur les parois, d'une pente insuffisante ou d'une canalisation abîmée. Un hydrocurage et une inspection caméra permettent d'en trouver la cause et de régler le problème durablement."),
            ("Pouvez-vous déboucher une canalisation la nuit {a_ville} ?", "Oui, notre service de débouchage fonctionne 24h/24 et 7j/7 {a_ville} et dans les communes alentour, y compris les jours fériés."),
            ("Combien coûte un débouchage de canalisation {a_ville} ?", "Le prix dépend de la technique nécessaire (furet, hydrocurage, caméra) et de l'accessibilité. Un devis écrit vous est remis sur place, avant toute intervention."),
            ("Le débouchage est-il à la charge du locataire ?", "L'entretien courant des canalisations, dont le débouchage d'un évier ou d'un lavabo, est en principe à la charge du locataire. Un bouchon sur une colonne commune relève du propriétaire ou de la copropriété."),
        ],
    },
    {
        "slug": "debouchage-wc",
        "name": "WC bouché",
        "label": "Débouchage de WC",
        "h1": "WC bouché {a_ville} ? <span class=\"accent\">Débouchage rapide</span>",
        "title": "WC bouché {ville} ({cp}) – Débouchage toilettes 24h/24",
        "desc": "WC bouché {a_ville} ? Débouchage de toilettes et sanibroyeur 24h/24, intervention propre et rapide. Devis avant travaux.",
        "img": "wc-bouche-toulouse",
        "img_alt": "Débouchage de WC bouché par un plombier {a_ville}",
        "lead": "Toilettes qui débordent ou ne se vident plus, sanibroyeur en panne : un plombier débouche vos WC {a_ville}, proprement et sans délai.",
        "intro": [
            "Des <strong>WC bouchés {a_ville}</strong>, c'est une urgence du quotidien, surtout quand il n'y a qu'un seul cabinet de toilette dans le logement. Nos plombiers interviennent rapidement avec le matériel adapté pour un débouchage propre.",
            "Lingettes, papier en excès, objet tombé dans la cuvette ou canalisation entartrée : le <strong>débouchage de WC {a_ville}</strong> est l'une de nos interventions les plus courantes, de jour comme de nuit.",
            "Votre cuvette déborde ou se vide au ralenti ? Ne tirez plus la chasse et appelez-nous : un plombier se déplace pour le <strong>débouchage de vos toilettes {a_ville}</strong>, avec un devis remis avant l'intervention.",
        ],
        "sections": [
            ("Ce que nous traitons", [
                "<ul><li>WC bouché par du papier, des lingettes ou un objet</li><li>Évacuation de WC lente ou qui gargouille</li><li>Sanibroyeur bloqué ou en panne</li><li>Canalisation de WC entartrée</li><li>Fuite de chasse d'eau ou de mécanisme</li></ul>",
            ]),
            ("Les bons réflexes", [
                "Ne tirez pas la chasse plusieurs fois : la cuvette risque de déborder. Essayez une ventouse adaptée aux WC, puis appelez un plombier si rien ne bouge. Évitez la soude caustique, dangereuse et inefficace sur les bouchons de lingettes.",
                "Si plusieurs évacuations sont bouchées en même temps (WC, douche, évier), le problème se situe probablement plus loin sur la canalisation : voir notre service de <a href=\"/debouchage-canalisation-{ville_slug}/\">débouchage de canalisation {a_ville}</a>.",
            ]),
        ],
        "faq": [
            ("Mon WC est bouché et je n'ai pas d'autres toilettes, intervenez-vous rapidement {a_ville} ?", "Oui, c'est une urgence que nous traitons en priorité. Un plombier se déplace 24h/24 {a_ville} pour déboucher vos toilettes."),
            ("Peut-on jeter des lingettes dans les WC ?", "Non, même celles dites « biodégradables » : elles ne se désagrègent pas assez vite et sont l'une des premières causes de WC bouchés et de pannes de sanibroyeur."),
            ("Réparez-vous les sanibroyeurs ?", "Oui, nous débouchons et dépannons les sanibroyeurs et broyeurs de toutes marques, et pouvons les remplacer si nécessaire."),
            ("Combien coûte le débouchage d'un WC {a_ville} ?", "Le tarif dépend de la cause et de la technique utilisée. Le plombier établit un devis écrit sur place avant de commencer."),
        ],
    },
    {
        "slug": "depannage-chauffe-eau",
        "name": "Chauffe-eau",
        "label": "Dépannage de chauffe-eau",
        "h1": "Dépannage chauffe-eau {a_ville} : <span class=\"accent\">eau chaude rétablie</span>",
        "title": "Dépannage chauffe-eau {ville} ({cp}) – Plombier 24h/24",
        "desc": "Chauffe-eau en panne {a_ville} ? Dépannage et remplacement de ballon d'eau chaude toutes marques, 24h/24. Devis avant travaux.",
        "img": "chauffe-eau-panne-toulouse",
        "img_alt": "Dépannage d'un chauffe-eau en panne {a_ville}",
        "lead": "Plus d'eau chaude, ballon qui fuit, disjoncteur qui saute : nous dépannons ou remplaçons votre chauffe-eau {a_ville}, toutes marques.",
        "intro": [
            "Plus d'eau chaude du jour au lendemain ? Le <strong>dépannage de chauffe-eau {a_ville}</strong> est une de nos spécialités. Nos plombiers interviennent sur tous les modèles : ballon électrique, chauffe-eau thermodynamique, chauffe-eau au gaz et chauffe-bain.",
            "Résistance grillée, thermostat défaillant, groupe de sécurité qui fuit ou cuve percée : nous diagnostiquons la panne de votre <strong>ballon d'eau chaude {a_ville}</strong> et vous proposons la solution la plus économique, réparation ou remplacement.",
            "Un <strong>chauffe-eau en panne {a_ville}</strong>, c'est tout le foyer privé de douche. Nos plombiers se déplacent rapidement avec les pièces les plus courantes pour rétablir l'eau chaude dès que possible.",
        ],
        "sections": [
            ("Pannes de chauffe-eau les plus fréquentes", [
                "<ul><li><strong>Plus d'eau chaude</strong> : résistance, thermostat, contacteur jour/nuit ou disjoncteur</li><li><strong>Eau tiède ou insuffisante</strong> : entartrage, résistance fatiguée, mauvais réglage</li><li><strong>Fuite</strong> au groupe de sécurité, aux raccords ou à la cuve</li><li><strong>Disjoncteur qui saute</strong> : défaut d'isolement de la résistance</li><li><strong>Bruits ou eau colorée</strong> : calcaire, anode usée</li></ul>",
            ]),
            ("Réparer ou remplacer ?", [
                "Un chauffe-eau électrique a une durée de vie moyenne de 10 à 15 ans selon la dureté de l'eau et l'entretien. Si la cuve fuit, le remplacement est inévitable. Sinon, une résistance, un thermostat ou un groupe de sécurité se remplacent facilement. Le plombier vous conseille honnêtement et vous remet un devis pour chaque option.",
                "Nous intervenons sur toutes les marques : Atlantic, Thermor, Ariston, Chaffoteaux, De Dietrich, Saunier Duval, ELM Leblanc, Chappée…",
            ]),
        ],
        "faq": [
            ("Pourquoi je n'ai plus d'eau chaude ?", "Vérifiez d'abord le disjoncteur du chauffe-eau sur le tableau électrique et le contacteur heures creuses. Si tout est en place, la panne vient souvent de la résistance ou du thermostat. Un plombier peut les tester et les remplacer sur place."),
            ("Mon chauffe-eau fuit, que faire ?", "Coupez l'alimentation électrique du chauffe-eau au tableau, puis fermez l'arrivée d'eau froide (robinet du groupe de sécurité). Appelez ensuite un plombier : une fuite au groupe de sécurité se répare facilement, une fuite de cuve impose un remplacement."),
            ("Remplacez-vous un chauffe-eau dans la journée {a_ville} ?", "Lorsque le modèle est disponible, le remplacement peut souvent être réalisé rapidement. Le plombier vous indique les délais et le prix exact sur devis."),
            ("Quelles marques de chauffe-eau dépannez-vous ?", "Toutes les marques du marché : Atlantic, Thermor, Ariston, Chaffoteaux, De Dietrich, Saunier Duval, ELM Leblanc, Chappée et bien d'autres."),
        ],
    },
    {
        "slug": "degat-des-eaux",
        "name": "Dégât des eaux",
        "label": "Intervention dégât des eaux",
        "h1": "Dégât des eaux {a_ville} : <span class=\"accent\">intervention d'urgence</span>",
        "title": "Dégât des eaux {ville} ({cp}) – Plombier urgence 24h/24",
        "desc": "Dégât des eaux {a_ville} : plombier en urgence 24h/24 pour stopper la fuite et sécuriser. Rapport pour l'assurance, devis avant travaux.",
        "img": "degat-des-eaux-toulouse",
        "img_alt": "Intervention d'urgence sur un dégât des eaux {a_ville}",
        "lead": "Rupture de tuyau, plafond qui goutte, appartement inondé : on stoppe la fuite, on sécurise et on vous remet les documents utiles pour l'assurance.",
        "intro": [
            "Un <strong>dégât des eaux {a_ville}</strong> demande une réaction immédiate pour limiter les dommages. Nos plombiers interviennent en urgence pour stopper la fuite, identifier son origine et réaliser la réparation.",
            "Rupture de flexible, canalisation éclatée, débordement de machine à laver ou fuite chez le voisin du dessus : en cas de <strong>dégât des eaux {a_ville}</strong>, appelez-nous à toute heure. Nous intervenons aussi bien en maison qu'en appartement.",
            "Face à un <strong>dégât des eaux {a_ville}</strong>, chaque minute compte. Notre plombier stoppe l'écoulement, sécurise l'installation et vous remet une facture et un rapport d'intervention détaillés pour votre déclaration de sinistre.",
        ],
        "sections": [
            ("Les premiers gestes", [
                "<ol><li><strong>Coupez l'eau</strong> au robinet général (près du compteur).</li><li><strong>Coupez l'électricité</strong> si l'eau atteint des prises, des luminaires ou le tableau.</li><li>Mettez à l'abri meubles, objets de valeur et papiers.</li><li><strong>Photographiez</strong> les dégâts et conservez les objets endommagés.</li><li>Prévenez votre voisin, votre syndic ou votre propriétaire.</li></ol>",
            ]),
            ("Déclarer le sinistre à votre assurance", [
                "En règle générale, un dégât des eaux doit être déclaré à votre assureur dans les <strong>5 jours ouvrés</strong> suivant sa découverte. Entre voisins, le <strong>constat amiable dégât des eaux</strong> facilite la gestion du dossier. Notre facture et notre rapport d'intervention décrivent l'origine de la fuite et les travaux réalisés.",
                "Si l'origine de la fuite n'est pas visible, nous réalisons une <a href=\"/recherche-de-fuite-{ville_slug}/\">recherche de fuite non destructive {a_ville}</a>.",
            ]),
        ],
        "faq": [
            ("Que faire en premier en cas de dégât des eaux {a_ville} ?", "Coupez l'arrivée d'eau générale, coupez l'électricité si nécessaire, puis appelez un plombier au 09 70 70 71 29 pour stopper la fuite. Prenez ensuite des photos pour votre assurance."),
            ("Quel est le délai pour déclarer un dégât des eaux ?", "Le délai habituel est de 5 jours ouvrés à compter de la découverte du sinistre. Consultez votre contrat pour connaître les conditions précises."),
            ("Fournissez-vous un rapport pour l'assurance ?", "Oui. Vous recevez une facture détaillée et, si nécessaire, un rapport d'intervention ou de recherche de fuite décrivant l'origine du sinistre et les réparations effectuées."),
            ("La fuite vient de chez mon voisin, pouvez-vous intervenir ?", "Nous pouvons intervenir à la demande de l'occupant du logement d'où provient la fuite, ou du syndic pour les parties communes. Prévenez rapidement votre voisin et remplissez ensemble un constat amiable."),
        ],
    },
    {
        "slug": "reparation-robinet",
        "name": "Robinet",
        "label": "Réparation de robinetterie",
        "h1": "Réparation robinet {a_ville} : <span class=\"accent\">fuite ou casse</span>",
        "title": "Réparation robinet {ville} ({cp}) – Fuite, mitigeur, plombier",
        "desc": "Robinet qui fuit ou cassé {a_ville} ? Réparation et remplacement de robinet, mitigeur, chasse d'eau, 24h/24. Devis avant travaux.",
        "img": "plombier-intervention-30-min-toulouse",
        "img_alt": "Réparation de robinet et mitigeur par un plombier {a_ville}",
        "lead": "Robinet qui goutte, mitigeur bloqué, robinet d'arrêt grippé : nous réparons ou remplaçons votre robinetterie {a_ville}, toutes marques.",
        "intro": [
            "Un robinet qui goutte peut gaspiller plusieurs milliers de litres d'eau par an. Nos plombiers assurent la <strong>réparation de robinet {a_ville}</strong> : changement de joint, de cartouche ou de clapet, ou remplacement complet si nécessaire.",
            "Mitigeur qui fuit, robinet thermostatique de douche défaillant, robinet d'arrêt qui ne ferme plus : la <strong>réparation de robinetterie {a_ville}</strong> est rapide quand on dispose des bonnes pièces. Nos plombiers interviennent sur toutes les marques.",
            "Robinet cassé, fuite au pied du mitigeur ou sous l'évier : un plombier se déplace {a_ville} pour <strong>réparer ou remplacer votre robinet</strong>, avec un devis remis avant de commencer.",
        ],
        "sections": [
            ("Nos interventions de robinetterie", [
                "<ul><li>Remplacement de joint, cartouche céramique ou clapet</li><li>Réparation et remplacement de mitigeur de cuisine ou de salle de bain</li><li>Robinet thermostatique de douche ou de baignoire</li><li>Robinet d'arrêt et vanne générale grippés</li><li>Mécanisme et robinet flotteur de chasse d'eau</li><li>Robinet extérieur et robinet de machine à laver</li></ul>",
            ]),
            ("Réparer ou changer le robinet ?", [
                "Sur un robinet récent, changer la cartouche ou le joint suffit souvent. Sur un modèle ancien ou entartré, le remplacement est parfois plus économique à moyen terme. Le plombier vous présente les deux options sur devis. Nous intervenons sur toutes les marques, dont Grohe, Hansgrohe, Jacob Delafon et Roca.",
            ]),
        ],
        "faq": [
            ("Mon robinet goutte, est-ce urgent ?", "Pas toujours, mais une fuite permanente fait grimper la facture d'eau. Si le robinet ne ferme plus du tout ou fuit sous l'évier, coupez le robinet d'arrêt et appelez un plombier."),
            ("Fournissez-vous le robinet ?", "Oui, nous pouvons fournir un robinet ou un mitigeur adapté, ou poser celui que vous avez déjà acheté."),
            ("Intervenez-vous sur les robinets thermostatiques {a_ville} ?", "Oui, nous réparons et remplaçons les mitigeurs thermostatiques de douche et de baignoire de toutes marques."),
            ("Combien coûte la réparation d'un robinet {a_ville} ?", "Le prix dépend de la panne et de la pièce à changer. Le plombier vous remet un devis écrit sur place avant toute intervention."),
        ],
    },
]

# ---------------------------------------------------------------------------
# COMMUNES desservies dans un rayon d'environ 25 km autour de Toulouse.
# (nom, code postal, distance approximative du centre de Toulouse en km, secteur)
# Aucune page n'est créée par commune : elles sont citées sur l'accueil,
# les pages services et la page « zones d'intervention ».
# ---------------------------------------------------------------------------
SECTEURS = [
    ("nord", "Nord toulousain"),
    ("nord-ouest", "Nord-ouest : Blagnac et l'aéroport"),
    ("ouest", "Ouest : Colomiers, Tournefeuille et la vallée du Touch"),
    ("sud-ouest", "Sud-ouest : Cugnaux, Frouzins, Fonsorbes"),
    ("sud", "Sud : Portet, Muret et la vallée de la Garonne"),
    ("sud-est", "Sud-est : Ramonville, Castanet, Labège et le Sicoval"),
    ("est", "Est : Balma, Quint-Fonsegrives et les coteaux"),
    ("nord-est", "Nord-est : L'Union, Saint-Jean et la vallée de l'Hers"),
]

COMMUNES = [
    # Nord
    ("Aucamville", "31140", 7, "nord"), ("Fonbeauzard", "31140", 9, "nord"), ("Launaguet", "31140", 8, "nord"),
    ("Saint-Alban", "31140", 10, "nord"), ("Fenouillet", "31150", 9, "nord"), ("Castelginest", "31780", 11, "nord"),
    ("Pechbonnieu", "31140", 13, "nord"), ("Montberon", "31140", 15, "nord"), ("Saint-Loup-Cammas", "31140", 15, "nord"),
    ("Bruguières", "31150", 15, "nord"), ("Gratentour", "31150", 15, "nord"), ("Lespinasse", "31150", 13, "nord"),
    ("Gagnac-sur-Garonne", "31150", 13, "nord"), ("Saint-Jory", "31790", 20, "nord"), ("Saint-Sauveur", "31790", 20, "nord"),
    ("Castelnau-d'Estrétefonds", "31620", 23, "nord"), ("Bouloc", "31620", 24, "nord"),
    # Nord-ouest
    ("Blagnac", "31700", 7, "nord-ouest"), ("Beauzelle", "31700", 10, "nord-ouest"), ("Cornebarrieu", "31700", 12, "nord-ouest"),
    ("Mondonville", "31700", 15, "nord-ouest"), ("Daux", "31700", 19, "nord-ouest"), ("Seilh", "31840", 13, "nord-ouest"),
    ("Aussonne", "31840", 14, "nord-ouest"), ("Merville", "31330", 22, "nord-ouest"),
    # Ouest
    ("Colomiers", "31770", 12, "ouest"), ("Tournefeuille", "31170", 10, "ouest"), ("Pibrac", "31820", 17, "ouest"),
    ("Brax", "31490", 18, "ouest"), ("Léguevin", "31490", 22, "ouest"), ("Plaisance-du-Touch", "31830", 17, "ouest"),
    ("La Salvetat-Saint-Gilles", "31880", 17, "ouest"),
    # Sud-ouest
    ("Cugnaux", "31270", 11, "sud-ouest"), ("Villeneuve-Tolosane", "31270", 13, "sud-ouest"), ("Frouzins", "31270", 15, "sud-ouest"),
    ("Seysses", "31600", 20, "sud-ouest"), ("Fonsorbes", "31470", 22, "sud-ouest"),
    # Sud
    ("Portet-sur-Garonne", "31120", 10, "sud"), ("Roques", "31120", 13, "sud"), ("Pinsaguel", "31120", 14, "sud"),
    ("Lacroix-Falgarde", "31120", 14, "sud"), ("Vieille-Toulouse", "31320", 9, "sud"), ("Pins-Justaret", "31860", 18, "sud"),
    ("Villate", "31860", 18, "sud"), ("Labarthe-sur-Lèze", "31860", 20, "sud"), ("Muret", "31600", 20, "sud"),
    ("Eaunes", "31600", 22, "sud"), ("Saubens", "31600", 21, "sud"),
    # Sud-est
    ("Ramonville-Saint-Agne", "31520", 7, "sud-est"), ("Auzeville-Tolosane", "31320", 10, "sud-est"),
    ("Castanet-Tolosan", "31320", 12, "sud-est"), ("Pechabou", "31320", 14, "sud-est"), ("Labège", "31670", 11, "sud-est"),
    ("Escalquens", "31750", 15, "sud-est"), ("Saint-Orens-de-Gameville", "31650", 10, "sud-est"), ("Lauzerville", "31650", 15, "sud-est"),
    ("Deyme", "31450", 18, "sud-est"), ("Belberaud", "31450", 16, "sud-est"), ("Odars", "31450", 17, "sud-est"),
    ("Ayguesvives", "31450", 23, "sud-est"),
    # Est
    ("Balma", "31130", 6, "est"), ("Quint-Fonsegrives", "31130", 10, "est"), ("Pin-Balma", "31130", 10, "est"),
    ("Flourens", "31130", 13, "est"), ("Drémil-Lafage", "31280", 14, "est"), ("Mons", "31280", 13, "est"),
    ("Aigrefeuille", "31280", 16, "est"),
    # Nord-est
    ("L'Union", "31240", 8, "nord-est"), ("Saint-Jean", "31240", 9, "nord-est"), ("Montrabé", "31850", 11, "nord-est"),
    ("Beaupuy", "31850", 13, "nord-est"), ("Mondouzil", "31850", 15, "nord-est"), ("Rouffiac-Tolosan", "31180", 11, "nord-est"),
    ("Castelmaurou", "31180", 15, "nord-est"), ("Saint-Geniès-Bellevue", "31180", 13, "nord-est"),
    ("Lapeyrouse-Fossat", "31180", 18, "nord-est"), ("Gragnague", "31380", 18, "nord-est"),
]

# Communes mises en avant (titres, descriptions, accroches)
PRINCIPALES = ["Blagnac", "Colomiers", "Tournefeuille", "Balma", "L'Union", "Muret", "Cugnaux", "Ramonville-Saint-Agne"]

# Quartiers de Toulouse (pages « plombier-toulouse-<quartier> »)
QUARTIERS = [
    ("capitole", "Capitole", "31000", "centre historique"),
    ("carmes", "Carmes", "31000", "centre historique"),
    ("saint-etienne", "Saint-Étienne", "31000", "centre historique"),
    ("arnaud-bernard", "Arnaud-Bernard", "31000", "centre historique"),
    ("compans-caffarelli", "Compans-Caffarelli", "31000", "centre"),
    ("saint-cyprien", "Saint-Cyprien", "31300", "rive gauche"),
    ("patte-d-oie", "Patte d'Oie", "31300", "rive gauche"),
    ("croix-de-pierre", "Croix-de-Pierre", "31300", "rive gauche"),
    ("purpan", "Purpan", "31300", "ouest"),
    ("saint-martin-du-touch", "Saint-Martin-du-Touch", "31300", "ouest"),
    ("lardenne", "Lardenne", "31100", "ouest"),
    ("mirail", "Mirail", "31100", "sud-ouest"),
    ("bagatelle", "Bagatelle", "31100", "sud-ouest"),
    ("saint-simon", "Saint-Simon", "31100", "sud-ouest"),
    ("minimes", "Les Minimes", "31200", "nord"),
    ("sept-deniers", "Sept Deniers", "31200", "nord"),
    ("borderouge", "Borderouge", "31200", "nord"),
    ("croix-daurade", "Croix-Daurade", "31200", "nord-est"),
    ("lalande", "Lalande", "31200", "nord"),
    ("bonnefoy", "Bonnefoy", "31500", "est"),
    ("jolimont", "Jolimont", "31500", "est"),
    ("cote-pavee", "Côte Pavée", "31500", "est"),
    ("guilhemery", "Guilheméry", "31500", "est"),
    ("busca", "Busca", "31400", "sud-est"),
    ("saint-michel", "Saint-Michel", "31400", "sud"),
    ("saint-agne", "Saint-Agne", "31400", "sud"),
    ("rangueil", "Rangueil", "31400", "sud-est"),
    ("montaudran", "Montaudran", "31400", "sud-est"),
    ("empalot", "Empalot", "31400", "sud"),
    ("pouvourville", "Pouvourville", "31400", "sud-est"),
]

HABITAT = {
    "centre": "Le bâti toulousain mêle immeubles anciens en brique, maisons de ville et résidences récentes. Dans l'ancien, les canalisations en plomb, en fonte ou en cuivre vieillissant sont sources de fuites et de bouchons ; nos plombiers connaissent bien ces installations.",
    "dense": "La commune mêle résidences collectives et maisons individuelles. En immeuble, une fuite peut vite toucher les voisins du dessous ; en maison, les canalisations enterrées et les chauffe-eau en garage ou cellier demandent un diagnostic précis.",
    "pavillonnaire": "L'habitat y est majoritairement pavillonnaire, avec de nombreux lotissements. Nos interventions les plus fréquentes : chauffe-eau en panne, débouchage de canalisations extérieures, fuites sur réseau enterré ou sous dalle.",
    "periurbain": "Entre bourg ancien et lotissements plus récents, les installations sont très variées : anciennes canalisations dans les maisons de bourg, réseaux enterrés et fosses ou regards extérieurs dans les maisons plus récentes.",
}
