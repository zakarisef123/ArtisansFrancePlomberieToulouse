(function () {
    "use strict";

    var menu = document.getElementById("mobile-menu");
    var burgers = document.querySelectorAll(".burger");

    function openMenu() {
        menu.classList.add("is-open");
        document.body.style.overflow = "hidden";
        burgers[0] && burgers[0].setAttribute("aria-expanded", "true");
    }

    function closeMenu() {
        menu.classList.remove("is-open");
        document.body.style.overflow = "";
        burgers[0] && burgers[0].setAttribute("aria-expanded", "false");
    }

    burgers.forEach(function (btn) {
        btn.addEventListener("click", function () {
            if (menu.classList.contains("is-open")) {
                closeMenu();
            } else {
                openMenu();
            }
        });
    });

    menu && menu.querySelectorAll("a").forEach(function (link) {
        link.addEventListener("click", closeMenu);
    });

    var stickyCta = document.getElementById("sticky-cta");
    var hero = document.getElementById("accueil");
    if (stickyCta && hero && "IntersectionObserver" in window) {
        var observer = new IntersectionObserver(
            function (entries) {
                entries.forEach(function (entry) {
                    stickyCta.classList.toggle("is-visible", !entry.isIntersecting);
                });
            },
            { rootMargin: "-80% 0px 0px 0px" }
        );
        observer.observe(hero);
    }

    var yearEl = document.getElementById("current-year");
    if (yearEl) {
        yearEl.textContent = new Date().getFullYear();
    }

    /* ---------- CMP / Google Consent Mode v2 ---------- */
    var CONSENT_KEY = "afs_consent_v1";
    var banner = document.getElementById("cmp-banner");

    function gtagPush() {
        window.dataLayer = window.dataLayer || [];
        window.dataLayer.push(arguments);
    }

    function applyConsent(c) {
        gtagPush("consent", "update", {
            ad_storage: c.ads ? "granted" : "denied",
            ad_user_data: c.ads ? "granted" : "denied",
            ad_personalization: c.ads ? "granted" : "denied",
            analytics_storage: c.analytics ? "granted" : "denied"
        });
    }

    function getStored() {
        try {
            return JSON.parse(localStorage.getItem(CONSENT_KEY));
        } catch (e) {
            return null;
        }
    }

    function openBanner() {
        if (!banner) return;
        banner.classList.add("is-open");
        document.body.classList.add("cmp-active");
    }

    function closeBanner() {
        if (!banner) return;
        banner.classList.remove("is-open");
        document.body.classList.remove("cmp-active");
    }

    function saveConsent(c) {
        try {
            localStorage.setItem(CONSENT_KEY, JSON.stringify(c));
        } catch (e) {}
        applyConsent(c);
        closeBanner();
    }

    if (banner) {
        var stored = getStored();
        if (stored) {
            applyConsent(stored);
        } else {
            openBanner();
        }

        var accept = document.getElementById("cmp-accept");
        var refuse = document.getElementById("cmp-refuse");
        var customize = document.getElementById("cmp-customize");
        var save = document.getElementById("cmp-save");
        var prefs = document.getElementById("cmp-prefs");
        var analyticsIn = document.getElementById("cmp-analytics");
        var adsIn = document.getElementById("cmp-ads");

        accept && accept.addEventListener("click", function () {
            saveConsent({ analytics: true, ads: true });
        });
        refuse && refuse.addEventListener("click", function () {
            saveConsent({ analytics: false, ads: false });
        });
        customize && customize.addEventListener("click", function () {
            if (!prefs) return;
            var open = prefs.classList.toggle("is-open");
            if (save) save.style.display = open ? "block" : "none";
        });
        save && save.addEventListener("click", function () {
            saveConsent({
                analytics: !!(analyticsIn && analyticsIn.checked),
                ads: !!(adsIn && adsIn.checked)
            });
        });

        var manage = document.getElementById("cmp-manage");
        manage && manage.addEventListener("click", function (e) {
            e.preventDefault();
            var s = getStored();
            if (analyticsIn) analyticsIn.checked = s ? !!s.analytics : false;
            if (adsIn) adsIn.checked = s ? !!s.ads : false;
            openBanner();
        });
    }

    /* ---------- Modale de devis par service ---------- */
    var modal = document.getElementById("quote-modal");
    if (modal) {
        var quoteButtons = document.querySelectorAll(".service-quote");
        var closeBtn = document.getElementById("quote-close");
        var serviceLabel = document.getElementById("quote-service-label");
        var serviceInput = document.getElementById("quote-service-input");
        var lastFocused = null;

        function openModal(service) {
            lastFocused = document.activeElement;
            if (serviceLabel) serviceLabel.textContent = service;
            if (serviceInput) serviceInput.value = service;
            modal.classList.add("is-open");
            modal.setAttribute("aria-hidden", "false");
            document.body.style.overflow = "hidden";
            var firstField = document.getElementById("q-prenom");
            if (firstField) firstField.focus();
        }

        function closeModal() {
            modal.classList.remove("is-open");
            modal.setAttribute("aria-hidden", "true");
            document.body.style.overflow = "";
            if (lastFocused && lastFocused.focus) lastFocused.focus();
        }

        quoteButtons.forEach(function (btn) {
            btn.addEventListener("click", function () {
                openModal(btn.getAttribute("data-service") || "Intervention");
            });
        });

        closeBtn && closeBtn.addEventListener("click", closeModal);
        modal.addEventListener("click", function (e) {
            if (e.target === modal) closeModal();
        });
        document.addEventListener("keydown", function (e) {
            if (e.key === "Escape" && modal.classList.contains("is-open")) closeModal();
        });
    }

    /* ---------- Envoi des formulaires (FormSubmit) ---------- */
    document.querySelectorAll('form[action*="formsubmit.co"]').forEach(function (form) {
        form.addEventListener("submit", function (e) {
            e.preventDefault();
            var data = new FormData(form);
            var submitBtn = form.querySelector('button[type="submit"]');
            if (submitBtn) submitBtn.disabled = true;
            var ajaxUrl = form.action.replace("formsubmit.co/", "formsubmit.co/ajax/");
            fetch(ajaxUrl, {
                method: "POST",
                headers: { "Content-Type": "application/x-www-form-urlencoded", "Accept": "application/json" },
                body: new URLSearchParams(data).toString()
            }).then(function (r) {
                if (!r.ok) throw new Error("submit failed");
                form.innerHTML = '<p class="form-success">Merci, votre demande a bien \u00e9t\u00e9 envoy\u00e9e. Nous vous recontactons rapidement. Pour une urgence, appelez directement le 09 70 70 71 29.</p>';
                if (typeof gtag === "function") {
                    gtag('event', 'conversion', {
                        'send_to': 'AW-18317420737/2JlZCOOYyfkcEMHRtp5E',
                        'value': 1.0,
                        'currency': 'EUR'
                    });
                }
            }).catch(function () {
                if (submitBtn) submitBtn.disabled = false;
                alert("Une erreur est survenue lors de l'envoi. Merci d'appeler directement le 09 70 70 71 29.");
            });
        });
    });

    /* ---------- Suivi de conversion Google Ads sur les appels ---------- */
    document.addEventListener("click", function (e) {
        var link = e.target.closest && e.target.closest('a[href^="tel:"]');
        if (!link) return;
        if (typeof gtag === "function") {
            gtag('event', 'conversion', {
                'send_to': 'AW-18317420737/2JlZCOOYyfkcEMHRtp5E',
                'value': 1.0,
                'currency': 'EUR'
            });
        }
    });
})();

