/* Ride Ready · PostHog web loader
   Single source of truth for site-wide product analytics.
   Update the project key here and every page picks it up. */
!function(t,e){var o,n,p,r;e.__SV||(window.posthog && window.posthog.__loaded)||(window.posthog=e,e._i=[],e.init=function(i,s,a){function g(t,e){var o=e.split(".");2==o.length&&(t=t[o[0]],e=o[1]),t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}}(p=t.createElement("script")).type="text/javascript",p.crossOrigin="anonymous",p.async=!0,p.src=s.api_host.replace(".i.posthog.com","-assets.i.posthog.com")+"/static/array.js",(r=t.getElementsByTagName("script")[0]).parentNode.insertBefore(p,r);var u=e;for(void 0!==a?u=e[a]=[]:a="posthog",u.people=u.people||[],u.toString=function(t){var e="posthog";return"posthog"!==a&&(e+="."+a),t||(e+=" (stub)"),e},u.people.toString=function(){return u.toString(1)+".people (stub)"},o="Mi Ri init Vi Gi Rr Wi Ji Bi capture calculateEventProperties tn register register_once register_for_session unregister unregister_for_session an getFeatureFlag getFeatureFlagPayload getFeatureFlagResult isFeatureEnabled reloadFeatureFlags updateFlags updateEarlyAccessFeatureEnrollment getEarlyAccessFeatures on onFeatureFlags onSurveysLoaded onSessionId getSurveys getActiveMatchingSurveys renderSurvey displaySurvey cancelPendingSurvey canRenderSurvey canRenderSurveyAsync un identify setPersonProperties group resetGroups setPersonPropertiesForFlags resetPersonPropertiesForFlags setGroupPropertiesForFlags resetGroupPropertiesForFlags reset setIdentity clearIdentity get_distinct_id getGroups get_session_id get_session_replay_url alias set_config startSessionRecording stopSessionRecording sessionRecordingStarted captureException addExceptionStep captureLog startExceptionAutocapture stopExceptionAutocapture loadToolbar get_property getSessionProperty nn Xi createPersonProfile setInternalOrTestUser sn Hi cn opt_in_capturing opt_out_capturing has_opted_in_capturing has_opted_out_capturing get_explicit_consent_status is_capturing clear_opt_in_out_capturing Ki debug Lr rn getPageViewId captureTraceFeedback captureTraceMetric Di".split(" "),n=0;n<o.length;n++)g(u,o[n]);e._i.push([i,s,a])},e.__SV=1)}(document,window.posthog||[]);

posthog.init('phc_mHqNedrIYWqnUfVwIJexMqjP5TorbFB9TWCeGbD4d5A', {
    api_host: 'https://t.rideready.app',
    ui_host: 'https://us.posthog.com',
    defaults: '2026-01-30',
    person_profiles: 'identified_only',
    capture_performance: true,
    enable_heatmaps: true,
    session_recording: {
        maskAllInputs: true
    },
    loaded: function (ph) {
        // Respect Global Privacy Control header (CCPA 2026)
        if (navigator.globalPrivacyControl) {
            ph.opt_out_capturing();
            return;
        }

        // Derive page_type from URL so every event is segmentable
        // without editing 2000 HTML files.
        var pageType = (function () {
            var p = window.location.pathname;
            if (p === '/' || p === '/index.html') return 'homepage';
            if (/^\/parks\/[^/]+\/[^/]+-queue-times\/?$/.test(p)) return 'ride-page';
            if (/^\/parks\/[^/]+\/crowd-calendar\/\d{4}-\d{2}-\d{2}\/?$/.test(p)) return 'crowd-calendar-day';
            if (/^\/parks\/[^/]+\/crowd-calendar\/?$/.test(p)) return 'crowd-calendar-park';
            if (/^\/parks\/[^/]+\/strategy\/?$/.test(p)) return 'park-strategy';
            if (/^\/parks\/[^/]+\/?$/.test(p)) return 'park-guide';
            if (/^\/universal-orlando\//.test(p)) return 'park-guide';
            if (/^\/epic-universe\//.test(p) || p.indexOf('/epic-guide') === 0) return 'park-guide';
            if (/^\/compare\//.test(p)) return 'comparison';
            if (/^\/guides\//.test(p)) return 'guide';
            if (/^\/crowds\//.test(p)) return 'crowd-overview';
            if (/^\/queues\//.test(p)) return 'queue-overview';
            if (/^\/reports\//.test(p)) return 'report';
            if (/^\/reviews\//.test(p)) return 'review';
            if (/^\/orlando\//.test(p)) return 'orlando-guide';
            if (/^\/spring\//.test(p) || /^\/mlk\//.test(p)) return 'seasonal-guide';
            if (/^\/methodology\//.test(p)) return 'methodology';
            if (p.indexOf('/app') === 0) return 'app-landing';
            if (p.indexOf('/waitlist') === 0) return 'waitlist';
            if (p.indexOf('/privacy') === 0 || p.indexOf('/terms') === 0 || p.indexOf('/delete-account') === 0) return 'legal';
            return 'other';
        })();

        // Park slug from URL when applicable, e.g. /parks/epic-universe/...
        var parkSlug = (function () {
            var m = window.location.pathname.match(/^\/parks\/([^/]+)/);
            if (m) return m[1];
            if (window.location.pathname.indexOf('/epic-universe') === 0) return 'epic-universe';
            if (window.location.pathname.indexOf('/universal-orlando') === 0) return 'universal-orlando';
            return null;
        })();

        ph.register({
            page_type: pageType,
            park_slug: parkSlug
        });

        // ---- App Store link click (primary KPI) ----
        document.addEventListener('click', function (e) {
            var link = e.target.closest && e.target.closest('a[href*="apps.apple.com"], a[href*="play.google.com"]');
            if (!link) return;
            var href = link.getAttribute('href') || '';
            var ct = null;
            try { ct = new URL(link.href).searchParams.get('ct'); } catch (_) {}

            ph.capture('app_store_link_clicked', {
                href: href,
                store: href.indexOf('apps.apple.com') >= 0 ? 'apple' : 'google',
                ct_param: ct,
                cta_location: link.dataset.ref || link.dataset.ctaLocation || null,
                link_text: (link.innerText || '').trim().slice(0, 80),
                page_path: window.location.pathname,
                page_type: pageType,
                park_slug: parkSlug,
                distinct_id_at_click: ph.get_distinct_id()
            });
        }, { capture: true });

        // ---- Scroll depth (25/50/75/90) ----
        var fired = {};
        var onScroll = function () {
            var doc = document.documentElement;
            var scrollable = (doc.scrollHeight - window.innerHeight) || 1;
            var pct = Math.round((window.scrollY / scrollable) * 100);
            [25, 50, 75, 90].forEach(function (t) {
                if (pct >= t && !fired[t]) {
                    fired[t] = true;
                    ph.capture('page_scrolled', {
                        depth_percent: t,
                        page_path: window.location.pathname,
                        page_type: pageType,
                        park_slug: parkSlug
                    });
                }
            });
        };
        window.addEventListener('scroll', onScroll, { passive: true });
    }
});
