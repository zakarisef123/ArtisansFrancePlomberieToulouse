# -*- coding: utf-8 -*-
"""Génère les pages locales (service × ville), les pages quartiers de Toulouse,
la page des zones d'intervention, les pages légales, sitemap.xml et llms.txt.

Usage : python3 tools/build.py   (depuis la racine du dépôt)
"""
import datetime
import hashlib
import html
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from site_data import SITE, SERVICES, COMMUNES, SECTEURS, PRINCIPALES, QUARTIERS, HABITAT  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = SITE["base_url"]
TEL = SITE["phone_e164"]
TEL_D = SITE["phone_display"]
TODAY = datetime.date.today().isoformat()

SERVICE = {s["slug"]: s for s in SERVICES}

PHONE_SVG = '<path d="M13.832 16.568a1 1 0 0 0 1.213-.303l.355-.465A2 2 0 0 1 17 15h3a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2A18 18 0 0 1 2 4a2 2 0 0 1 2-2h3a2 2 0 0 1 2 2v3a2 2 0 0 1-.8 1.6l-.468.351a1 1 0 0 0-.292 1.233 14 14 0 0 0 6.392 6.384"></path>'
SHIELD_SVG = '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"></path><path d="m9 12 2 2 4-4"></path>'
CHEVRON_DOWN = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m6 9 6 6 6-6"></path></svg>'


def svg(path, size=20, fill="none"):
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 24 24" fill="%s" '
            'stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>'
            % (size, size, fill, path))


def pick(options, key):
    """Choix déterministe d'une variante de texte selon la page."""
    return options[int(hashlib.md5(key.encode()).hexdigest(), 16) % len(options)]


def url(slug):
    return "%s/%s/" % (BASE, slug) if slug else BASE + "/"


def service_href(slug):
    return "/" if slug == "plombier" else "/%s-toulouse/" % slug


# Contexte de texte : les pages services sont centrées sur Toulouse
CTX = {"ville": "Toulouse", "a_ville": "à Toulouse", "de_ville": "de Toulouse", "cp": "31000", "ville_slug": "toulouse",
       "delai_phrase": "À Toulouse et en proche banlieue, nos plombiers interviennent en général en 30 minutes environ ; dans les communes plus éloignées (jusqu'à 25 km), comptez 30 à 45 minutes."}


def communes_par_secteur():
    out = []
    for key, label in SECTEURS:
        out.append((key, label, sorted([c for c in COMMUNES if c[3] == key], key=lambda c: c[2])))
    return out


def fmt(text, ctx):
    return text.format(**ctx)


# ---------------------------------------------------------------------------
# Gabarit commun
# ---------------------------------------------------------------------------
def head(title, desc, canonical, og_image, jsonld, robots="index, follow, max-image-preview:large"):
    blocks = "\n".join('    <script type="application/ld+json">\n%s\n    </script>' % json.dumps(j, ensure_ascii=False, indent=1) for j in jsonld)
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- Google Tag Manager -->
    <script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
    new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
    'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
    }})(window,document,'script','dataLayer','{SITE["gtm"]}');</script>
    <!-- End Google Tag Manager -->
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag() {{ dataLayer.push(arguments); }}
        gtag('consent', 'default', {{
            ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied',
            analytics_storage: 'denied', functionality_storage: 'granted', security_storage: 'granted',
            wait_for_update: 500
        }});
    </script>
    <script async src="https://www.googletagmanager.com/gtag/js?id={SITE["gtag"]}"></script>
    <script>
        gtag('js', new Date());
        gtag('config', '{SITE["gtag"]}');
    </script>
    <title>{html.escape(title, quote=False)}</title>
    <meta name="description" content="{html.escape(desc)}">
    <meta name="robots" content="{robots}">
    <link rel="canonical" href="{canonical}">
    <link rel="icon" type="image/png" sizes="32x32" href="/images/favicon-32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/images/favicon-16.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/images/apple-touch-icon.png">
    <meta name="theme-color" content="#1a2e2a">
    <meta name="geo.region" content="FR-31">
    <meta property="og:type" content="website">
    <meta property="og:locale" content="fr_FR">
    <meta property="og:site_name" content="{SITE["name"]}">
    <meta property="og:title" content="{html.escape(title)}">
    <meta property="og:description" content="{html.escape(desc)}">
    <meta property="og:url" content="{canonical}">
    <meta property="og:image" content="{og_image}">
    <meta name="twitter:card" content="summary_large_image">
    <link rel="stylesheet" href="/assets/style.css">
{blocks}
</head>
<body>
    <noscript><iframe src="https://www.googletagmanager.com/ns.html?id={SITE["gtm"]}" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
    <a href="#main" class="sr-only">Aller au contenu</a>
"""


HEADER = f"""
    <header class="site-header">
        <div class="container">
            <a href="/" class="brand" aria-label="Artisans France Plomberie, accueil">
                <span class="brand-mark" aria-hidden="true"><img src="/images/logo.png" alt="" width="163" height="240"></span>
                <span class="brand-text">
                    <span class="brand-name">Artisans <em>France</em> Plomberie</span>
                    <span class="brand-tagline">Plombier Urgence Toulouse · Haute-Garonne</span>
                </span>
            </a>
            <nav class="main-nav" aria-label="Navigation principale">
                <a href="/">Accueil</a>
                <a href="/#services">Services</a>
                <a href="/zones-intervention/">Zones</a>
                <a href="#contact">Devis gratuit</a>
            </nav>
            <div class="header-cta">
                <span class="assur-badge">{svg(SHIELD_SVG, 16)} Agréé Assurances</span>
                <a href="tel:{TEL}" class="call-btn">{svg(PHONE_SVG, 16)}<span>{TEL_D}</span></a>
            </div>
            <button type="button" class="burger" aria-label="Ouvrir le menu" aria-controls="mobile-menu" aria-expanded="false">
                {svg('<path d="M4 6h16"></path><path d="M4 12h16"></path><path d="M4 18h16"></path>', 24)}
            </button>
        </div>
    </header>
    <div id="mobile-menu" class="mobile-menu" role="dialog" aria-label="Menu de navigation">
        <div class="mobile-menu-head">
            <span class="brand-name">Artisans <em style="color:#2563EB;font-style:normal;">France</em> Plomberie</span>
            <button type="button" class="burger" aria-label="Fermer le menu">{svg('<path d="M18 6 6 18"></path><path d="m6 6 12 12"></path>', 22)}</button>
        </div>
        <div class="mobile-menu-body">
            <a href="tel:{TEL}" class="mobile-call-card">
                <span class="mobile-call-icon">{svg(PHONE_SVG, 22)}</span>
                <span><span>Urgence 24h/7j</span><strong>{TEL_D}</strong></span>
            </a>
            <nav class="mobile-nav" aria-label="Navigation mobile">
                <a href="/">Accueil</a>
                <a href="/#services">Services</a>
                <a href="/zones-intervention/">Zones d'intervention</a>
                <a href="#contact">Devis gratuit</a>
            </nav>
            <div class="mobile-menu-foot">{svg(SHIELD_SVG, 14)}<span>Agréé toutes assurances</span></div>
        </div>
    </div>
"""


def footer():
    serv = "\n".join('                        <li><a href="/%s-toulouse/">%s à Toulouse</a></li>' % (s["slug"], s["label"]) for s in SERVICES if s["slug"] != "plombier")
    zones = "\n".join('                        <li><a href="/zones-intervention/#%s">%s</a></li>' % (k, l.split(" :")[0]) for k, l in SECTEURS)
    return f"""
    <footer class="site-footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-col">
                    <div class="footer-brand">
                        <span class="brand-mark" aria-hidden="true"><img src="/images/logo.png" alt="" width="163" height="240" loading="lazy"></span>
                        <span>Artisans <em>France Plomberie</em></span>
                    </div>
                    <p>Plombier d'urgence sur toute la Haute-Garonne : dépannage plomberie 24h/24 à Toulouse et dans toute l'agglomération. Intervention rapide, devis avant travaux.</p>
                </div>
                <div class="footer-col">
                    <h4>Nos services</h4>
                    <ul>
{serv}
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Zones d'intervention</h4>
                    <ul>
                        <li><a href="/zones-intervention/#toulouse">Toulouse, tous quartiers</a></li>
{zones}
                    </ul>
                </div>
                <div class="footer-col">
                    <div class="footer-urgence">
                        <h4>Urgence Directe</h4>
                        <a href="tel:{TEL}">{TEL_D}</a>
                        <div class="footer-status"><span class="dot" aria-hidden="true"></span><span>Technicien disponible</span></div>
                    </div>
                </div>
            </div>
            <div class="footer-bottom">
                <p>© <span id="current-year">{datetime.date.today().year}</span> ARTISANS FRANCE PLOMBERIE. TOUS DROITS RÉSERVÉS.</p>
                <nav class="footer-legal-nav">
                    <a href="/mentions-legales/">Mentions légales</a>
                    <a href="/politique-de-confidentialite/">Politique de confidentialité</a>
                    <button type="button" id="cmp-manage" class="cmp-manage-link">Gérer les cookies</button>
                </nav>
            </div>
            <p class="footer-identity">
                <strong>ARTISANS FRANCE</strong> · Camille Marie DESNOS, entrepreneur individuel ·
                SIREN 102 567 039 · SIRET 102 567 039 00015 · Siège : 47 rue Vivienne, 75002 Paris
            </p>
        </div>
    </footer>
    <div id="sticky-cta" class="sticky-cta">
        <a href="tel:{TEL}">
            <span class="icon-box" aria-hidden="true">{svg(PHONE_SVG, 22, "currentColor")}</span>
            <span class="txt"><span>Dépannage 24/7</span><strong>{TEL_D}</strong></span>
            <span class="chevron" aria-hidden="true">{svg('<path d="m9 18 6-6-6-6"></path>', 18)}</span>
        </a>
    </div>
    <a href="tel:{TEL}" class="floating-phone" aria-label="Appeler le plombier d'urgence au {TEL_D}">{svg(PHONE_SVG, 24, "currentColor")}</a>
    <div id="cmp-banner" class="cmp-banner" role="dialog" aria-label="Gestion du consentement aux cookies" aria-live="polite">
        <h2>Cookies &amp; confidentialité</h2>
        <p>Nous utilisons des cookies pour mesurer l'audience et améliorer votre expérience. Vous pouvez accepter, refuser ou personnaliser vos choix. En savoir plus dans notre <a href="/politique-de-confidentialite/">politique de confidentialité</a>.</p>
        <div id="cmp-prefs" class="cmp-prefs">
            <div class="cmp-pref-row">
                <div class="txt"><strong>Strictement nécessaires</strong><span>Indispensables au fonctionnement du site.</span></div>
                <label class="cmp-switch" aria-label="Cookies strictement nécessaires (toujours actifs)"><input type="checkbox" checked disabled><span class="track"></span></label>
            </div>
            <div class="cmp-pref-row">
                <div class="txt"><strong>Mesure d'audience</strong><span>Statistiques de visite anonymisées.</span></div>
                <label class="cmp-switch" aria-label="Cookies de mesure d'audience"><input type="checkbox" id="cmp-analytics"><span class="track"></span></label>
            </div>
            <div class="cmp-pref-row">
                <div class="txt"><strong>Publicité</strong><span>Publicité et mesure marketing (Google Ads).</span></div>
                <label class="cmp-switch" aria-label="Cookies publicitaires"><input type="checkbox" id="cmp-ads"><span class="track"></span></label>
            </div>
        </div>
        <div class="cmp-actions">
            <button type="button" class="cmp-btn cmp-accept" id="cmp-accept">Tout accepter</button>
            <button type="button" class="cmp-btn cmp-refuse" id="cmp-refuse">Tout refuser</button>
            <button type="button" class="cmp-btn cmp-custom-toggle" id="cmp-customize">Personnaliser mes choix</button>
            <button type="button" class="cmp-btn cmp-save" id="cmp-save" style="display:none;">Enregistrer mes choix</button>
        </div>
    </div>
    <script src="/assets/main.js" defer></script>
</body>
</html>
"""


def contact_form(page_id, ville, service_name):
    options = "".join('<option value="%s"%s>%s</option>' % (html.escape(s["label"]), " selected" if s["name"] == service_name else "", s["label"]) for s in SERVICES)
    return f"""
        <section id="contact" class="contact-section">
            <div class="container">
                <div class="contact-head section-head">
                    <span class="section-eyebrow">Devis gratuit &amp; sans engagement</span>
                    <h2>Demandez votre <span class="accent">devis gratuit</span></h2>
                    <p>Décrivez votre problème en quelques mots, un plombier vous rappelle rapidement. Pour une urgence immédiate, appelez le <strong>{TEL_D}</strong>.</p>
                </div>
                <div class="contact-wrap">
                    <aside class="contact-aside">
                        <div class="contact-phone-card">
                            <span class="label">Urgence immédiate</span>
                            <a href="tel:{TEL}">{TEL_D}</a>
                            <div class="hours"><span class="dot" aria-hidden="true"></span><span>Plombier disponible 24h/24, 7j/7</span></div>
                        </div>
                    </aside>
                    <form class="form-card" action="{SITE["email_form"]}" method="POST">
                        <input type="hidden" name="_subject" value="Demande de devis - {html.escape(service_name)} {html.escape(ville)}">
                        <input type="hidden" name="_captcha" value="false">
                        <input type="hidden" name="_template" value="table">
                        <input type="hidden" name="page" value="{page_id}">
                        <p class="form-honeypot" aria-hidden="true"><label>Ne remplissez pas ce champ si vous etes humain <input type="text" tabindex="-1" autocomplete="off" name="_honeypot"></label></p>
                        <div class="form-row two">
                            <div class="form-field"><label for="prenom">Prénom <span class="req">*</span></label><input type="text" id="prenom" name="prenom" autocomplete="given-name" required></div>
                            <div class="form-field"><label for="nom">Nom <span class="req">*</span></label><input type="text" id="nom" name="nom" autocomplete="family-name" required></div>
                        </div>
                        <div class="form-row two">
                            <div class="form-field"><label for="telephone">Téléphone <span class="req">*</span></label><input type="tel" id="telephone" name="telephone" autocomplete="tel" placeholder="06 00 00 00 00" required></div>
                            <div class="form-field"><label for="ville">Ville</label><input type="text" id="ville" name="ville" autocomplete="address-level2" value="{html.escape(ville)}"></div>
                        </div>
                        <div class="form-row">
                            <div class="form-field"><label for="intervention">Type d'intervention <span class="req">*</span></label>
                                <select id="intervention" name="intervention" required>{options}<option value="Autre">Autre, je ne sais pas</option></select>
                            </div>
                        </div>
                        <div class="form-row">
                            <div class="form-field"><label for="message">Décrivez votre problème <span class="req">*</span></label><textarea id="message" name="message" placeholder="Type de fuite ou de panne, pièce concernée, urgence..." required></textarea></div>
                        </div>
                        <div class="form-consent">
                            <input type="checkbox" id="consent" name="consent" required>
                            <label for="consent">J'accepte que mes informations soient utilisées pour être recontacté au sujet de ma demande, conformément à la <a href="/politique-de-confidentialite/">politique de confidentialité</a>.</label>
                        </div>
                        <button type="submit" class="form-submit">{svg(PHONE_SVG)} Envoyer ma demande de devis</button>
                        <p class="form-note">Réponse rapide. Pour une urgence, appelez directement le {TEL_D}.</p>
                    </form>
                </div>
            </div>
        </section>
"""


def provider():
    return {"@type": ["Plumber", "EmergencyService"], "@id": BASE + "/#business", "name": SITE["name"],
            "url": BASE + "/", "telephone": TEL, "image": BASE + "/images/plombier-agree-toulouse.jpg",
            "logo": BASE + "/images/logo.png", "priceRange": "€€",
            "address": {"@type": "PostalAddress", "addressLocality": "Toulouse", "postalCode": "31000", "addressRegion": "Haute-Garonne", "addressCountry": "FR"},
            "openingHoursSpecification": {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "00:00", "closes": "23:59"}}


def breadcrumb_ld(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(items)]}


def breadcrumb_html(items):
    lis = []
    for i, (n, u) in enumerate(items):
        if i == len(items) - 1:
            lis.append('<li aria-current="page">%s</li>' % html.escape(n))
        else:
            lis.append('<li><a href="%s">%s</a></li>' % (u.replace(BASE, "") or "/", html.escape(n)))
    return '<nav class="breadcrumb" aria-label="Fil d\'Ariane"><ol>%s</ol></nav>' % "".join(lis)


def faq_ld(faq):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}


def faq_html(faq, title):
    items = "".join(f"""
                    <details class="faq-item">
                        <summary><span>{q}</span>{CHEVRON_DOWN}</summary>
                        <p>{a}</p>
                    </details>""" for q, a in faq)
    return f"""
                <div class="faq-block">
                    <h2 style="font-size:clamp(1.4rem, 3vw, 1.9rem);font-weight:900;text-transform:uppercase;letter-spacing:-.02em;margin-bottom:1.5rem;">{title}</h2>{items}
                </div>"""


def hero(h1, lead, crumbs, points):
    pts = "".join("<li>%s</li>" % p for p in points)
    return f"""
        <section id="accueil" class="hero hero-sub">
            <div class="container hero-inner">
                {breadcrumb_html(crumbs)}
                <div class="hero-badge"><span class="pulse-dot" aria-hidden="true"></span><span>SOS PLOMBIER DISPONIBLE <b>24H/24 7J/7</b></span></div>
                <h1>{h1}</h1>
                <p class="lead">{lead}</p>
                <div class="hero-actions">
                    <a href="tel:{TEL}" class="hero-call">{svg(PHONE_SVG, 26, "currentColor")}<span>{TEL_D}</span></a>
                    <a href="#contact" class="trust-chip" style="text-decoration:none;">{svg(SHIELD_SVG, 20)}<span>Devis gratuit en ligne</span></a>
                </div>
                <ul class="hero-points">{pts}</ul>
            </div>
        </section>
"""


def aside(img, alt, place):
    return f"""
                    <aside class="prose-aside">
                        <img src="/images/{img}.jpg" srcset="/images/{img}.jpg 1x, /images/{img}-hd.jpg 2x" alt="{html.escape(alt)}" width="600" height="600" loading="lazy">
                        <div class="aside-card">
                            <span class="label">Urgence plomberie {html.escape(place)}</span>
                            <a class="tel" href="tel:{TEL}">{TEL_D}</a>
                            <ul>
                                <li>Disponible 24h/24, 7j/7</li>
                                <li>Devis écrit avant travaux</li>
                                <li>Toutes marques, tous équipements</li>
                                <li>Facture détaillée pour l'assurance</li>
                            </ul>
                        </div>
                    </aside>"""


def tags(links):
    return '<div class="zone-tags">%s</div>' % "".join('<a class="zone-tag" href="%s">%s</a>' % (h, html.escape(t)) for h, t in links)


def write(slug, content):
    d = os.path.join(ROOT, slug)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
        f.write(content)


# ---------------------------------------------------------------------------
# Page service (Toulouse + communes à 25 km)
# ---------------------------------------------------------------------------
def strip_tags(t):
    import re
    return re.sub(r"<[^>]+>", "", t)


def communes_text(service_name):
    """Paragraphes par secteur citant toutes les communes desservies."""
    out = []
    for key, label, cs in communes_par_secteur():
        names = ", ".join("%s (%s)" % (c[0], c[1]) for c in cs)
        out.append("<p><strong>%s</strong> : %s.</p>" % (label, names))
    return "\n".join(out)


def build_service(s):
    ctx = CTX
    slug = "%s-toulouse" % s["slug"]
    canonical = url(slug)
    title = fmt(s["title"], ctx)
    desc = fmt(s["desc"], ctx)
    h1 = fmt(s["h1"], ctx)
    crumbs = [("Accueil", BASE + "/"), (s["label"] + " à Toulouse", canonical)]
    principales = ", ".join(PRINCIPALES[:-1]) + " et " + PRINCIPALES[-1]

    intro = fmt(s["intro"][0], ctx)
    sections_html = ""
    for h2, paras in s["sections"]:
        sections_html += "<h2>%s</h2>\n" % fmt(h2, ctx)
        for p in paras:
            p = fmt(p, ctx)
            sections_html += (p if p.startswith("<") else "<p>%s</p>" % p) + "\n"

    quartiers = ", ".join(q[1] for q in QUARTIERS)
    zone_html = f"""
                    <h2>{s["label"]} à Toulouse et <span class="accent">25 km autour</span></h2>
                    <p>Nos plombiers interviennent pour {s["label"].lower()} dans <strong>tous les quartiers de Toulouse</strong> (31000, 31100, 31200, 31300, 31400, 31500) : {quartiers}.</p>
                    <p>Nous couvrons aussi toutes les communes situées dans un rayon d'environ 25 km autour de Toulouse, dont {principales} :</p>
                    {communes_text(s["name"])}
                    <p>{ctx["delai_phrase"]}</p>"""

    other_services = [(service_href(o["slug"]), (o["label"] + " à Toulouse") if o["slug"] != "plombier" else "Plombier urgence Toulouse") for o in SERVICES if o["slug"] != s["slug"]]

    faq = [(fmt(q, ctx), fmt(a, ctx)) for q, a in s["faq"]]
    faq.append(("Intervenez-vous autour de Toulouse pour %s ?" % s["label"].lower(),
                "Oui, nous intervenons dans toutes les communes à environ 25 km autour de Toulouse : %s, mais aussi %s et toutes les communes listées sur notre page zones d'intervention." % (principales, ", ".join(c[0] for c in COMMUNES if c[0] not in PRINCIPALES and c[2] <= 13)[:400])))
    faq.append(("Êtes-vous un plombier agréé par les assurances ?", "Nous travaillons avec toutes les compagnies d'assurance habitation. Nos factures et rapports d'intervention détaillés sont acceptés pour vos déclarations de sinistre dégât des eaux."))

    service_ld = {"@context": "https://schema.org", "@type": "Service", "name": strip_tags(h1), "serviceType": s["label"],
                  "url": canonical, "description": desc, "provider": provider(),
                  "areaServed": [{"@type": "City", "name": "Toulouse"}] + [{"@type": "City", "name": c[0], "address": {"@type": "PostalAddress", "postalCode": c[1], "addressLocality": c[0], "addressCountry": "FR"}} for c in COMMUNES],
                  "availableChannel": {"@type": "ServiceChannel", "servicePhone": {"@type": "ContactPoint", "telephone": TEL, "contactType": "Dépannage d'urgence", "availableLanguage": "French", "hoursAvailable": "Mo-Su 00:00-23:59"}}}

    body = hero(h1, fmt(s["lead"], ctx), crumbs, ["Intervention 24h/24", "Toulouse + 25 km", "Devis avant travaux", "Facture pour l'assurance"])
    body += f"""
        <section class="prose-section">
            <div class="container prose-grid">
                <article class="prose">
                    <p>{intro}</p>
                    {"".join("<p>%s</p>" % fmt(p, ctx) for p in s["intro"][1:])}
                    <p>{HABITAT["centre"]}</p>
                    {sections_html}
                    <div class="info-box"><strong>Prix transparent :</strong> le plombier vous remet un devis écrit sur place, avant toute intervention. Pour un dépannage à domicile de plus de 150 € TTC, ce devis est obligatoire. TVA à 10 % possible pour un logement achevé depuis plus de 2 ans.</div>
                    {zone_html}
                    {faq_html(faq, "Questions fréquentes : " + s["label"].lower() + " à Toulouse")}
                </article>
                {aside(s["img"], fmt(s["img_alt"], ctx), "Toulouse")}
            </div>
        </section>
        <section class="cta-band">
            <div class="container">
                <div class="cta-band-left">
                    <span class="cta-icon" aria-hidden="true">{svg(PHONE_SVG, 34)}</span>
                    <div>
                        <h2 style="font-size:inherit;">{s["name"]} à Toulouse ou autour ? Appelez maintenant</h2>
                        <p>Plombier disponible 24h/24 · Devis avant travaux · Toulouse et 25 km autour</p>
                    </div>
                </div>
                <a href="tel:{TEL}" class="cta-band-btn"><span>{TEL_D}</span></a>
            </div>
        </section>
{contact_form(slug, "", s["name"])}
        <section class="links-section">
            <div class="container">
                <h2>Nos autres services de plomberie</h2>
                {tags(other_services + [("/zones-intervention/", "Toutes nos zones d'intervention")])}
            </div>
        </section>
"""
    og = "%s/images/%s.jpg" % (BASE, s["img"])
    return slug, head(title, desc, canonical, og, [service_ld, breadcrumb_ld(crumbs), faq_ld(faq)]) + HEADER + '    <main id="main">' + body + "    </main>" + footer()


# ---------------------------------------------------------------------------
# Page zones d'intervention (toutes les communes à 25 km, par secteur)
# ---------------------------------------------------------------------------
def build_zones():
    slug = "zones-intervention"
    canonical = url(slug)
    title = "Plombier Toulouse et 25 km autour – Zones d'intervention 24h/24"
    desc = "Plombier d'urgence 24h/24 à Toulouse (tous quartiers) et dans %d communes à 25 km : Blagnac, Colomiers, Tournefeuille, Balma, Muret, Cugnaux... Appelez le %s." % (len(COMMUNES), TEL_D)
    crumbs = [("Accueil", BASE + "/"), ("Zones d'intervention", canonical)]
    serv_links = "".join('<li><a href="%s">%s</a></li>' % (service_href(s["slug"]), (s["label"] + " à Toulouse") if s["slug"] != "plombier" else "Plombier urgence Toulouse") for s in SERVICES)
    services_inline = ", ".join('<a href="%s">%s</a>' % (service_href(s["slug"]), s["name"].lower()) for s in SERVICES if s["slug"] != "plombier")

    sections = f"""
                    <h2 id="toulouse">Plombier à <span class="accent">Toulouse</span>, tous quartiers</h2>
                    <p>{HABITAT["centre"]} Nous intervenons dans les six secteurs postaux de Toulouse (31000, 31100, 31200, 31300, 31400 et 31500), en général en 30 minutes environ.</p>
                    <ul class="zones-columns">{"".join("<li>%s <small>(%s)</small></li>" % (q[1], q[2]) for q in QUARTIERS)}</ul>"""
    for key, label, cs in communes_par_secteur():
        names = ", ".join(c[0] for c in cs[:4])
        sections += f"""
                    <h2 id="{key}">{label}</h2>
                    <p>Plombier d'urgence à {names} et dans tout le secteur {key} de Toulouse : {services_inline}. Intervention 24h/24, devis écrit avant travaux.</p>
                    <ul class="zones-columns">{"".join("<li><strong>%s</strong> <small>(%s) · ~%d km</small></li>" % (c[0], c[1], c[2]) for c in cs)}</ul>"""

    faq = [
        ("Jusqu'où intervenez-vous autour de Toulouse ?", "Nous intervenons à Toulouse et dans toutes les communes situées dans un rayon d'environ 25 km : de Saint-Jory et Bouloc au nord jusqu'à Muret et Labarthe-sur-Lèze au sud, de Léguevin et Fonsorbes à l'ouest jusqu'à Ayguesvives et Gragnague à l'est."),
        ("Quel est le délai d'intervention en banlieue toulousaine ?", CTX["delai_phrase"]),
        ("Les tarifs sont-ils différents selon la commune ?", "Le plombier établit toujours un devis écrit sur place, avant toute intervention. Vous connaissez le prix exact et décidez librement."),
        ("Intervenez-vous la nuit et le week-end dans toute la zone ?", "Oui, notre service fonctionne 24h/24 et 7j/7, jours fériés compris, à Toulouse comme dans toutes les communes desservies."),
    ]
    place_ld = {"@context": "https://schema.org", "@type": "Service", "name": "Plombier d'urgence à Toulouse et 25 km autour", "serviceType": "Plombier d'urgence",
                "url": canonical, "provider": provider(),
                "areaServed": [{"@type": "City", "name": "Toulouse"}] + [{"@type": "City", "name": c[0], "address": {"@type": "PostalAddress", "postalCode": c[1], "addressLocality": c[0], "addressCountry": "FR"}} for c in COMMUNES]}
    body = hero('Plombier Toulouse <span class="accent">et 25 km autour</span>', "Nos plombiers interviennent 24h/24 dans tous les quartiers de Toulouse et dans %d communes de la Haute-Garonne, dans un rayon d'environ 25 km." % len(COMMUNES), crumbs,
                ["%d communes desservies" % len(COMMUNES), "%d quartiers de Toulouse" % len(QUARTIERS), "24h/24, 7j/7", "Devis avant travaux"])
    body += f"""
        <section class="prose-section">
            <div class="container prose-grid">
                <article class="prose">
                    <p>Fuite d'eau, canalisation ou WC bouché, chauffe-eau en panne, dégât des eaux : Artisans France Plomberie se déplace en urgence à <strong>Toulouse et dans toute son agglomération</strong>. Retrouvez ci-dessous l'ensemble des quartiers et communes où nous intervenons.</p>
                    {sections}
                    <h2>Nos services</h2>
                    <ul>{serv_links}</ul>
                    {faq_html(faq, "Questions fréquentes : zones d'intervention")}
                </article>
                {aside("plombier-intervention-30-min-toulouse", "Plombier en intervention à Toulouse et dans l'agglomération", "Toulouse")}
            </div>
        </section>
{contact_form(slug, "", "Plombier")}
"""
    return slug, head(title, desc, canonical, BASE + "/images/plombier-agree-toulouse.jpg", [place_ld, breadcrumb_ld(crumbs), faq_ld(faq)]) + HEADER + '    <main id="main">' + body + "    </main>" + footer()


# ---------------------------------------------------------------------------
# Pages légales et 404
# ---------------------------------------------------------------------------
def simple_page(slug, title, desc, h1, inner, robots="index, follow"):
    canonical = url(slug) if slug else BASE + "/404"
    body = f"""
        <div class="container">
            <article class="legal-page">
                <h1>{h1}</h1>
                {inner}
                <a class="legal-back" href="/">← Retour à l'accueil</a>
            </article>
        </div>
"""
    return head(title, desc, canonical, BASE + "/images/plombier-agree-toulouse.jpg", [], robots) + HEADER + '    <main id="main">' + body + "    </main>" + footer()


MENTIONS = f"""
<h2>Éditeur du site</h2>
<p><strong>ARTISANS FRANCE</strong>, Camille Marie DESNOS, entrepreneur individuel.<br>
SIREN 102 567 039 · SIRET 102 567 039 00015<br>
Siège : 47 rue Vivienne, 75002 Paris<br>
Téléphone : <a href="tel:{TEL}">{TEL_D}</a></p>
<h2>Directeur de la publication</h2>
<p>Camille Marie DESNOS.</p>
<h2>Hébergement</h2>
<p>Netlify, Inc., 512 2nd Street, Suite 200, San Francisco, CA 94107, États-Unis – www.netlify.com</p>
<h2>Propriété intellectuelle</h2>
<p>L'ensemble des contenus de ce site (textes, images, logo) est protégé. Toute reproduction sans autorisation est interdite. Les marques citées appartiennent à leurs propriétaires respectifs et sont mentionnées à titre informatif.</p>
<h2>Prix et devis</h2>
<p>Conformément à l'arrêté du 24 janvier 2017, un devis écrit détaillé est remis avant toute prestation de dépannage, de réparation ou d'entretien à domicile d'un montant supérieur à 150 € TTC.</p>
<h2>Médiation de la consommation</h2>
<p>En cas de litige, le consommateur peut recourir gratuitement à un médiateur de la consommation. Les coordonnées du médiateur sont communiquées sur simple demande.</p>
"""

PRIVACY = f"""
<h2>Responsable du traitement</h2>
<p>ARTISANS FRANCE, Camille Marie DESNOS, entrepreneur individuel, 47 rue Vivienne, 75002 Paris.</p>
<h2>Données collectées</h2>
<p>Via les formulaires de devis : prénom, nom, téléphone, ville, type d'intervention et description de votre demande. Ces données sont utilisées uniquement pour vous recontacter et traiter votre demande (base légale : mesures précontractuelles à votre demande).</p>
<h2>Durée de conservation</h2>
<p>Les données des demandes de devis sont conservées 3 ans à compter du dernier contact, puis supprimées.</p>
<h2>Destinataires et sous-traitants</h2>
<p>Les formulaires sont transmis par le service FormSubmit. Le site est hébergé par Netlify. La mesure d'audience et la publicité utilisent les services Google (Google Analytics, Google Ads, Google Tag Manager), uniquement si vous y consentez.</p>
<h2>Cookies</h2>
<p>Les cookies de mesure d'audience et publicitaires ne sont déposés qu'après votre accord (Google Consent Mode v2). Vous pouvez modifier vos choix à tout moment via le lien « Gérer les cookies » en bas de page.</p>
<h2>Vos droits</h2>
<p>Vous disposez d'un droit d'accès, de rectification, d'effacement, d'opposition et de limitation sur vos données. Pour l'exercer, contactez-nous au {TEL_D}. Vous pouvez également introduire une réclamation auprès de la CNIL (www.cnil.fr).</p>
"""


# ---------------------------------------------------------------------------
def main():
    pages = []  # (slug, priority)
    for s in SERVICES:
        if s["slug"] == "plombier":
            continue  # la page « plombier Toulouse » est la page d'accueil
        slug, content = build_service(s)
        write(slug, content)
        pages.append((slug, "0.9"))
    slug, content = build_zones()
    write(slug, content)
    pages.append((slug, "0.8"))
    write("mentions-legales", simple_page("mentions-legales", "Mentions légales – Artisans France Plomberie", "Mentions légales du site Artisans France Plomberie Toulouse.", "Mentions légales", MENTIONS))
    write("politique-de-confidentialite", simple_page("politique-de-confidentialite", "Politique de confidentialité – Artisans France Plomberie", "Politique de confidentialité et cookies du site Artisans France Plomberie Toulouse.", "Politique de confidentialité", PRIVACY))
    pages += [("mentions-legales", "0.2"), ("politique-de-confidentialite", "0.2")]
    with open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8") as f:
        f.write(simple_page("", "Page introuvable – Artisans France Plomberie", "Page introuvable.", "Page introuvable",
                            '<p>Cette page n\'existe pas ou a été déplacée. Pour une urgence plomberie, appelez directement le <a href="tel:%s">%s</a> ou consultez nos <a href="/zones-intervention/">zones d\'intervention</a>.</p>' % (TEL, TEL_D), "noindex, follow"))

    # sitemap.xml (avec extension images Google)
    imgs = {"": [s["img"] for s in SERVICES] + ["plombier-intervention-30-min-toulouse"], "zones-intervention": ["plombier-intervention-30-min-toulouse"]}
    for s in SERVICES:
        imgs["%s-toulouse" % s["slug"]] = [s["img"]]

    def entry(loc, slug, freq, prio):
        im = "".join("\n    <image:image><image:loc>%s/images/%s.jpg</image:loc></image:image>" % (BASE, i) for i in dict.fromkeys(imgs.get(slug, [])))
        return "  <url>\n    <loc>%s</loc>\n    <lastmod>%s</lastmod>\n    <changefreq>%s</changefreq>\n    <priority>%s</priority>%s\n  </url>" % (loc, TODAY, freq, prio, im)
    urls = [entry(BASE + "/", "", "weekly", "1.0")]
    urls += [entry(url(sl), sl, "monthly" if p < "0.5" else "weekly", p) for sl, p in pages]
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n%s\n</urlset>\n' % "\n".join(urls))

    # llms.txt
    serv_lines = "\n".join("- [%s à Toulouse](%s): %s" % (s["label"], url("%s-toulouse" % s["slug"]), strip_tags(fmt(s["lead"], CTX))) for s in SERVICES if s["slug"] != "plombier")
    secteurs = "\n".join("- %s : %s" % (label, ", ".join("%s (%s)" % (c[0], c[1]) for c in cs)) for key, label, cs in communes_par_secteur())
    llms = f"""# Artisans France Plomberie – Plombier d'urgence à Toulouse et 25 km autour

> Artisans France Plomberie est un service de plomberie d'urgence disponible 24h/24 et 7j/7 à Toulouse (tous quartiers) et dans les communes situées à environ 25 km autour (Haute-Garonne, 31) : fuite d'eau, recherche de fuite non destructive, débouchage de canalisation et de WC, dépannage de chauffe-eau, dégât des eaux et réparation de robinetterie. Téléphone : {TEL_D} ({TEL}). Devis écrit remis sur place avant toute intervention.

## Informations clés

- Nom : Artisans France Plomberie (ARTISANS FRANCE, Camille Marie DESNOS, entrepreneur individuel, SIRET 102 567 039 00015)
- Téléphone d'urgence : {TEL_D}, disponible 24h/24, 7j/7, jours fériés compris
- Site : {BASE}/
- Zone : Toulouse (31000 à 31500, tous quartiers) et {len(COMMUNES)} communes dans un rayon d'environ 25 km
- Délai d'intervention : en général 30 minutes environ à Toulouse et en proche banlieue, 30 à 45 minutes en périphérie
- Tarifs : devis écrit gratuit établi sur place avant toute intervention ; paiement par carte bancaire, espèces ou chèque
- Assurance : factures et rapports d'intervention fournis pour les déclarations de sinistre dégât des eaux
- Marques prises en charge : Atlantic, Thermor, Ariston, Chaffoteaux, De Dietrich, Saunier Duval, ELM Leblanc, Chappée, Grohe

## Pages principales

- [Plombier urgence Toulouse (accueil)]({BASE}/): présentation, engagements, FAQ et formulaire de devis
- [Zones d'intervention]({url("zones-intervention")}): tous les quartiers de Toulouse et les communes à 25 km

## Services

{serv_lines}

## Quartiers de Toulouse desservis

{", ".join(q[1] for q in QUARTIERS)}

## Communes desservies (rayon d'environ 25 km)

{secteurs}

## Optional

- [Version complète pour IA (llms-full.txt)]({BASE}/llms-full.txt)
- [Plan du site]({BASE}/sitemap.xml)
- [Mentions légales]({url("mentions-legales")})
"""
    with open(os.path.join(ROOT, "llms.txt"), "w", encoding="utf-8") as f:
        f.write(llms)

    # llms-full.txt : contenu complet des pages services, en texte brut
    full = [llms.replace("## Optional", "## Détail des services\n\n(voir ci-dessous)\n\n## Optional", 1)]
    for s in SERVICES:
        if s["slug"] == "plombier":
            continue
        part = ["", "---", "", "# %s à Toulouse" % s["label"], "", "URL : %s" % url("%s-toulouse" % s["slug"]), "", strip_tags(fmt(s["lead"], CTX)), ""]
        part += [strip_tags(fmt(p, CTX)) for p in s["intro"]]
        for h2, paras in s["sections"]:
            part += ["", "## " + strip_tags(fmt(h2, CTX)), ""]
            for p in paras:
                txt = fmt(p, CTX).replace("</li>", "\n").replace("<li>", "- ")
                part.append(strip_tags(txt).strip())
        part += ["", "## Questions fréquentes", ""]
        for q, a in s["faq"]:
            part += ["### " + fmt(q, CTX), "", fmt(a, CTX), ""]
        full.append("\n".join(part))
    with open(os.path.join(ROOT, "llms-full.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(full))
    print("%d pages générées (+ accueil), sitemap.xml et llms.txt écrits." % len(pages))


if __name__ == "__main__":
    main()
