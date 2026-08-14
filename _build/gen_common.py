# -*- coding: utf-8 -*-
"""Κοινά δομικά στοιχεία για τον ιστότοπο της Μαριλένας Τζαννετάτου."""
import json, pathlib, re
import html as _html

BASE = pathlib.Path(
    "/Users/apostolospollalis/Library/CloudStorage/GoogleDrive-apostolos@clinicbrain.gr/"
    "Shared drives/BRAIN GROUP/CLINICBRAIN/CLIENTS FORM/"
    "2026-08-14 · Μαριλένα Τζαννετάτου - Ψυχολόγος MSc · Ψυχολόγος"
)
WEB = BASE / "website"

# ------------------------------------------------------------------ ταυτότητα
SITE_URL   = "https://www.mtzannetatou.gr"
BRAND      = "Μαριλένα Τζαννετάτου — Ψυχολόγος MSc"
BRAND_SHORT = "Μαριλένα Τζαννετάτου"
NAME       = "Μαριλένα Τζαννετάτου"
NAME_FULL  = "Μαριλένα Τζαννετάτου, MSc"
SPECIALTY  = "Ψυχολόγος"
TITLE_LINE = "Ψυχολόγος MSc"
LICENSE    = "588049"
STREET     = "Στρατηγού Ρογκάκου 29"
CITY       = "Μαρούσι"
CITY_GEN   = "Μαρουσίου"
REGION     = "Αττική"
ZIP        = "15125"
ZIP_PRETTY = "151 25"
PHONE      = "6944813712"
PHONE_P    = "6944 813712"
EMAIL      = "mtzannetatou@gmail.com"
FACEBOOK   = "https://www.facebook.com/ekpaidefsigoneon"
GBP        = "https://share.google/fI01mm5aHw2yGOM5q"
MAPS       = GBP
SESSION    = "50"          # λεπτά ανά συνεδρία
LAT, LON   = "38.0506", "23.8079"    # Μαρούσι — να επιβεβαιωθεί το ακριβές στίγμα

# Περιοχές για τοπικό SEO
AREAS = ["Μαρούσι", "Χαλάνδρι", "Κηφισιά", "Ν. Ερυθραία", "Βριλήσσια", "Πεύκη",
         "Μελίσσια", "Ψυχικό", "Φιλοθέη", "Αγία Παρασκευή", "Νέο Ηράκλειο",
         "Βόρεια Προάστια"]

# Ονόματα στατικών αρχείων με αποτύπωμα περιεχομένου (συμπληρώνονται στο build).
ASSETS = {"css": "site.css", "js": "site.js"}

# ------------------------------------------------------------------ πλοήγηση
NAV = [
    ("Αρχική",                    "index.html"),
    ("Βιογραφικό",                "viografiko.html"),
    ("Θεραπευτικές Προσεγγίσεις", "proseggiseis.html"),
    ("Υπηρεσίες",                 "ypiresies.html"),
    ("Επικοινωνία",               "epikoinonia.html"),
]

SERVICES = [
    dict(slug="ypiresies/atomiki-therapeia-enilikon.html",
         nav="Ατομική Θεραπεία Ενηλίκων",
         who="Ενήλικες",
         short="Ατομική Θεραπεία Ενηλίκων",
         teaser="Ατομικές συνεδρίες σε ασφαλές πλαίσιο, για την κατανόηση συναισθημάτων, βιωμάτων και μοτίβων που επηρεάζουν τη ζωή και τις σχέσεις.",
         icon="person"),
    dict(slug="ypiresies/atomiki-therapeia-efivon.html",
         nav="Ατομική Θεραπεία Εφήβων",
         who="Έφηβοι &amp; νεαροί ενήλικες",
         short="Ατομική Θεραπεία Εφήβων",
         teaser="Χώρος έκφρασης και αυτογνωσίας για τον έφηβο, με κατανόηση της αναπτυξιακής φάσης και του οικογενειακού πλαισίου.",
         icon="spark"),
    dict(slug="ypiresies/oikogeneiaki-therapeia.html",
         nav="Οικογενειακή Θεραπεία",
         who="Οικογένειες",
         short="Οικογενειακή Θεραπεία",
         teaser="Δουλειά με τη δυναμική του οικογενειακού συστήματος: ρόλοι, σχέσεις και μοτίβα επικοινωνίας που μπορούν να αλλάξουν.",
         icon="family"),
    dict(slug="ypiresies/therapeia-zevgous.html",
         nav="Θεραπεία Ζεύγους",
         who="Ζευγάρια",
         short="Θεραπεία Ζεύγους",
         teaser="Εστίαση στα μοτίβα σύνδεσης μέσα στη σχέση, στη διαχείριση συγκρούσεων και στη συναισθηματική ασφάλεια των συντρόφων.",
         icon="link"),
    dict(slug="ypiresies/symvouleftiki-goneon.html",
         nav="Συμβουλευτική Γονέων",
         who="Γονείς",
         short="Συμβουλευτική Γονέων",
         teaser="Ενίσχυση της σχέσης γονέα–παιδιού, αποτελεσματική οριοθέτηση και τρόποι επικοινωνίας που καλλιεργούν ασφάλεια.",
         icon="hands"),
    dict(slug="ypiresies/ekpaidefsi-goneon-gordon.html",
         nav="Εργαστήρι Αποτελεσματικού Γονέα",
         who="Ομάδες γονέων &amp; εκπαιδευτικών",
         # αδιάσπαστο κενό: το «Gordon» να μη μένει μόνο του σε δεύτερη γραμμή
         short="Εκπαίδευση Γονέων · Μέθοδος&nbsp;Gordon",
         teaser="Βιωματικές ομάδες γονέων στη μέθοδο Thomas Gordon: ενεργητική ακρόαση, επίλυση συγκρούσεων, αμοιβαίος σεβασμός.",
         icon="group"),
]

ICONS = {
 "person": '<circle cx="12" cy="7.5" r="3.5"/><path d="M4.5 21a7.5 7.5 0 0 1 15 0"/>',
 "spark": '<path d="M12 2.5 13.9 8l5.6 1.9-5.6 1.9L12 17.4 10.1 11.8 4.5 9.9 10.1 8z"/><path d="M18.5 15.5 19.3 18l2.2.8-2.2.8-.8 2.4-.8-2.4-2.2-.8 2.2-.8z"/>',
 "family": '<circle cx="7.5" cy="7" r="2.6"/><circle cx="16.5" cy="7" r="2.6"/><path d="M2.8 20a4.7 4.7 0 0 1 9.4 0"/><path d="M11.8 20a4.7 4.7 0 0 1 9.4 0"/>',
 "link": '<path d="M9.5 14.5 14.5 9.5"/><path d="M11 6.5 12.8 4.7a4 4 0 0 1 5.7 5.7l-1.9 1.8"/><path d="M13 17.5l-1.8 1.8a4 4 0 0 1-5.7-5.7l1.9-1.8"/>',
 "hands": '<path d="M12 21s-7-4.2-7-9.2A3.8 3.8 0 0 1 12 9.4a3.8 3.8 0 0 1 7 2.4c0 5-7 9.2-7 9.2z"/><path d="M12 9.4V3"/>',
 "group": '<circle cx="12" cy="6" r="2.4"/><circle cx="5" cy="10" r="2.2"/><circle cx="19" cy="10" r="2.2"/><path d="M8.2 15.5a4.2 4.2 0 0 1 7.6 0"/><path d="M2 18.5a3.6 3.6 0 0 1 5.2-2.6"/><path d="M22 18.5a3.6 3.6 0 0 0-5.2-2.6"/>',
 "spiral": '<path d="M12 12.6a1.2 1.2 0 1 1 2 -.9c0 1.6-1.6 2.6-3.1 2.6-2.2 0-3.9-1.8-3.9-4 0-2.9 2.4-5.2 5.3-5.2 3.6 0 6.5 3 6.5 6.6 0 4.4-3.6 7.9-8 7.9"/>',
 "leaf": '<path d="M20 4c0 9-5.6 13.5-11.5 13.5A4.5 4.5 0 0 1 4 13c0-5 4.6-9 16-9z"/><path d="M4.5 19.5C7 15 11 11.5 16 9.5"/>',
 "chat": '<path d="M21 12a8 8 0 0 1-8 8H4l2-3.2A8 8 0 1 1 21 12z"/><path d="M9 11h6M9 14.5h3.5"/>',
 "shield": '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/>',
 "grad": '<path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/>',
 "book": '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>',
 "hand-sign": '<path d="M8.5 12V4.8a1.4 1.4 0 0 1 2.8 0V11"/><path d="M11.3 10.4V3.6a1.4 1.4 0 0 1 2.8 0V11"/><path d="M14.1 11V5.8a1.4 1.4 0 0 1 2.8 0V13"/><path d="M8.5 12 6.9 9.6a1.4 1.4 0 0 0-2.4 1.4l3 6.1A5.5 5.5 0 0 0 12.4 21h.6a4 4 0 0 0 4-4v-4"/>',
 "monitor": '<rect x="2.5" y="4" width="19" height="13" rx="2"/><path d="M9 21h6M12 17v4"/>',
 "phone": '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.9.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/>',
 "pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>',
 "clock": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
 "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m2 7 10 6 10-6"/>',
 "chev": '<path d="m6 9 6 6 6-6"/>',
 "calendar": '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/><path d="m9 16 2 2 4-4"/>',
}


def icon(name, cls="w-6 h-6", sw="1.7"):
    # τα width/height μένουν ως ασφαλές fallback, ώστε το εικονίδιο να μη
    # «σκάει» στα 300×150 αν λείψει ποτέ ο κανόνας μεγέθους από το CSS
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" '
            'fill="none" stroke="currentColor" stroke-width="%s" stroke-linecap="round" '
            'stroke-linejoin="round" class="%s" aria-hidden="true">%s</svg>' % (sw, cls, ICONS[name]))


def rel(depth):
    return "../" * depth


def plain(s):
    """Καθαρό κείμενο για JSON-LD: οι HTML οντότητες (&amp;, &nbsp;) δεν έχουν
    θέση σε structured data — η Google τις διαβάζει κυριολεκτικά."""
    return _html.unescape(s).replace("\u00a0", " ").strip()


# ------------------------------------------------------------------ JSON-LD
def practice_ld():
    """Το γραφείο ως ProfessionalService — όχι MedicalClinic: η ψυχολόγος δεν
    είναι ιατρός και δεν παρέχει ιατρικές πράξεις."""
    return {
        "@type": ["ProfessionalService", "LocalBusiness"],
        "@id": SITE_URL + "/#grafeio",
        "name": BRAND,
        "alternateName": "Ψυχολόγος Μαρούσι – Μαριλένα Τζαννετάτου",
        "url": SITE_URL + "/",
        "image": SITE_URL + "/assets/img/og-image.jpg",
        "logo": SITE_URL + "/assets/img/logo.png",
        "description": ("Ψυχολόγος στο Μαρούσι. Ατομική θεραπεία ενηλίκων και εφήβων, οικογενειακή "
                        "θεραπεία, θεραπεία ζεύγους, συμβουλευτική και εκπαίδευση γονέων. "
                        "Συνεδρίες διά ζώσης και διαδικτυακά, καθώς και στην Ελληνική Νοηματική Γλώσσα."),
        "priceRange": "€€",
        "currenciesAccepted": "EUR",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": STREET,
            "addressLocality": CITY,
            "addressRegion": REGION,
            "postalCode": ZIP,
            "addressCountry": "GR",
        },
        "geo": {"@type": "GeoCoordinates", "latitude": LAT, "longitude": LON},
        "hasMap": MAPS,
        "telephone": "+30" + PHONE,
        "email": EMAIL,
        "sameAs": [FACEBOOK, GBP],
        "areaServed": [{"@type": "City", "name": a} for a in AREAS[:-1]],
        "availableLanguage": [
            {"@type": "Language", "name": "Ελληνικά"},
            {"@type": "Language", "name": "Ελληνική Νοηματική Γλώσσα"},
        ],
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "Υπηρεσίες ψυχοθεραπείας και συμβουλευτικής",
            "itemListElement": [
                {"@type": "Offer", "itemOffered": {"@type": "Service",
                 "name": plain(s["short"]), "url": SITE_URL + "/" + s["slug"]}}
                for s in SERVICES
            ],
        },
        "founder": {"@id": SITE_URL + "/viografiko.html#psychologos"},
        "employee": {"@id": SITE_URL + "/viografiko.html#psychologos"},
        "openingHoursSpecification": [
            {"@type": "OpeningHoursSpecification",
             "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
             "opens": "09:00", "closes": "21:00"},
        ],
    }


def person_ld():
    return {
        "@type": "Person",
        "@id": SITE_URL + "/viografiko.html#psychologos",
        "name": NAME,
        "jobTitle": "Ψυχολόγος, MSc",
        "url": SITE_URL + "/viografiko.html",
        "image": SITE_URL + "/assets/img/og-image.jpg",
        "worksFor": {"@id": SITE_URL + "/#grafeio"},
        "sameAs": [FACEBOOK],
        "knowsLanguage": ["el", "Ελληνική Νοηματική Γλώσσα"],
        "hasCredential": [
            {"@type": "EducationalOccupationalCredential",
             "credentialCategory": "Άδεια ασκήσεως επαγγέλματος Ψυχολόγου",
             "identifier": LICENSE},
            {"@type": "EducationalOccupationalCredential",
             "credentialCategory": "MSc Παιδοψυχολογία (with Distinction)"},
            {"@type": "EducationalOccupationalCredential",
             "credentialCategory": "Diploma in Counselling — COSCA"},
        ],
        "alumniOf": [
            {"@type": "CollegeOrUniversity", "name": "Université de Strasbourg"},
            {"@type": "CollegeOrUniversity", "name": "University of Central Lancashire"},
        ],
        "knowsAbout": ["Συστημική ψυχοθεραπεία", "Συνθετική ψυχοθεραπεία",
                       "Θεωρία του δεσμού", "Συμβουλευτική γονέων",
                       "Εκπαίδευση γονέων μέθοδος Gordon", "Ειδική αγωγή"],
    }


def website_ld():
    return {
        "@type": "WebSite",
        "@id": SITE_URL + "/#website",
        "url": SITE_URL + "/",
        "name": BRAND,
        "inLanguage": "el-GR",
        "publisher": {"@id": SITE_URL + "/#grafeio"},
    }


def breadcrumb_ld(trail):
    """trail: [(name, href_absolute), ...]"""
    return {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": u}
            for i, (n, u) in enumerate(trail)
        ],
    }


def faq_ld(pairs):
    return {
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}}
            for q, a in pairs
        ],
    }


# ------------------------------------------------------------------ κοινά μπλοκ
def faq_block(pairs):
    out = []
    for q, a in pairs:
        out.append(
            '<div class="cb-faq border-b border-dark-olive/10 py-8">'
            '<button class="w-full flex justify-between items-center text-left focus:outline-none group">'
            '<h3 class="font-serif text-2xl md:text-3xl text-dark-olive group-hover:text-olive-green transition-colors pr-8">'
            + q + '</h3>'
            '<div class="w-12 h-12 rounded-full border border-dark-olive/20 flex items-center justify-center '
            'group-hover:border-olive-green transition-colors shrink-0">'
            + icon("chev", "w-5 h-5 text-dark-olive group-hover:text-olive-green transition-transform duration-500", "2") +
            '</div></button>'
            '<div class="faq-answer"><div class="cb-prose">' + a + '</div></div></div>'
        )
    return "\n".join(out)


def hours_table():
    """Κάθε χρονικό διάστημα μπαίνει σε δικό του span: μένει αδιάσπαστο, αλλά
    τα διαστήματα μεταξύ τους αναδιπλώνονται ελεύθερα σε στενές οθόνες."""
    R = '<span class="cb-hours__r">%s</span>'
    rows = [
        ("Δευτέρα",   R % "09:00 – 21:00"),
        ("Τρίτη",     R % "09:00 – 21:00"),
        ("Τετάρτη",   R % "09:00 – 21:00"),
        ("Πέμπτη",    R % "09:00 – 21:00"),
        ("Παρασκευή", R % "09:00 – 21:00"),
        ("Σάββατο &amp; Κυριακή", '<span class="cb-hours__closed">Κλειστά</span>'),
    ]
    body = "".join("<tr><th>%s</th><td>%s</td></tr>" % (d, h) for d, h in rows)
    return ('<table class="cb-hours"><tbody>%s</tbody></table>'
            '<p class="cb-hours__foot">Οι συνεδρίες είναι κατόπιν ραντεβού, διά ζώσης ή διαδικτυακά.</p>' % body)


def contact_card(depth):
    r = rel(depth)
    return f"""<div class="cb-contact-card">
<div class="cb-contact-card__row">{icon('pin', 'w-5 h-5 cb-mint shrink-0')}
<div><span class="cb-contact-card__k">Διεύθυνση</span>
<a href="{MAPS}" target="_blank" rel="noopener noreferrer">{STREET}, {ZIP_PRETTY} {CITY}</a></div></div>
<div class="cb-contact-card__row">{icon('phone', 'w-5 h-5 cb-mint shrink-0')}
<div><span class="cb-contact-card__k">Τηλέφωνο</span>
<a href="tel:+30{PHONE}">{PHONE_P}</a></div></div>
<div class="cb-contact-card__row">{icon('mail', 'w-5 h-5 cb-mint shrink-0')}
<div><span class="cb-contact-card__k">Email</span>
<a href="mailto:{EMAIL}">{EMAIL}</a></div></div>
<div class="cb-contact-card__row">{icon('clock', 'w-5 h-5 cb-mint shrink-0')}
<div><span class="cb-contact-card__k">Ωράριο <span class="cb-open-badge" data-open-status></span></span>
{hours_table()}</div></div>
</div>"""


def access_note():
    """Η προσβασιμότητα στη Νοηματική είναι το βασικό διαφοροποιητικό στοιχείο."""
    return (f'<div class="cb-access">{icon("hand-sign", "cb-access__ic")}'
            f'<div><strong>Στην Ελληνική Νοηματική Γλώσσα</strong>'
            f'<span>Όλες οι υπηρεσίες προσφέρονται και στην ΕΝΓ, χωρίς διερμηνέα.</span></div></div>')


def booking_embed():
    """Θέση ενσωμάτωσης του ηλεκτρονικού ημερολογίου. Μέχρι να μπει, δείχνει
    καθαρό placeholder με το τηλέφωνο ώστε η σελίδα να μη μοιάζει σπασμένη."""
    return f"""<div class="cb-booking">
<!-- ══════════════════════════════════════════════════════════════════════
     CALENDLY · ΣΗΜΕΙΟ ΕΝΣΩΜΑΤΩΣΗΣ

     Αντικαταστήστε ΟΛΟ το <div class="cb-booking__ph"> ... </div> παρακάτω
     με το inline embed του Calendly:

       <div class="calendly-inline-widget"
            data-url="https://calendly.com/USERNAME/50min?hide_gdpr_banner=1&amp;primary_color=2f8a73"
            style="min-width:320px;height:720px"></div>
       <script src="https://assets.calendly.com/assets/external/widget.js" async></script>

     Πριν τη δημοσίευση:
       • Ρυθμίστε στο Calendly διάρκεια συνεδρίας {SESSION} λεπτά.
       • Περάστε το ωράριο: Δευτέρα – Παρασκευή 09:00-21:00.
       • Συνδέστε το ημερολόγιο {EMAIL} για να αποφεύγονται διπλοκρατήσεις.
       • Το Calendly είναι εκτελών την επεξεργασία εκτός ΕΕ — αναφέρεται ήδη
         στην Πολιτική Απορρήτου· μην αφαιρέσετε εκείνη την παράγραφο.
       • Μην ζητάτε δεδομένα ψυχικής υγείας στη φόρμα κράτησης.
     ══════════════════════════════════════════════════════════════════════ -->
<div class="cb-booking__ph">
{icon('calendar', 'cb-booking__ic')}
<p class="cb-booking__t">Ηλεκτρονικό ημερολόγιο ραντεβού</p>
<p class="cb-booking__d">Σε αυτό το σημείο θα ενσωματωθεί το σύστημα online κρατήσεων,
ώστε να επιλέγετε μόνοι σας ημέρα και ώρα για την πρώτη σας συνεδρία.</p>
<p class="cb-booking__d cb-booking__d--em">Μέχρι τότε, κλείστε ραντεβού τηλεφωνικά ή με μήνυμα:</p>
<div class="cb-booking__actions">
<a class="cb-btn" href="tel:+30{PHONE}">{icon('phone','w-4 h-4')}<span>{PHONE_P}</span></a>
<a class="cb-btn cb-btn--ghost" href="mailto:{EMAIL}">{icon('mail','w-4 h-4')}<span>EMAIL</span></a>
</div>
</div>
<p class="cb-booking__note">Η συνεδρία διαρκεί {SESSION} λεπτά. Αν βρίσκεστε σε κρίση ή σκέφτεστε να βλάψετε τον εαυτό σας,
μην περιμένετε ραντεβού: καλέστε τη <a href="tel:1018">1018</a> (Γραμμή Παρέμβασης για την Αυτοκτονία, 24/7)
ή το <a href="tel:112">112</a>.</p>
</div>"""
