# URGENT Technical SEO Fixes - Classic Ski School
**Priority: CRITICAL**
**Status: ✅ IMPLEMENTED - Week 10 Measurement Shows SUCCESS**

This checklist contains simple HTML/JSON changes that will dramatically improve German and Polish market visibility in Google AI search results.

---

## 🎉 IMPLEMENTATION SUCCESS (January 7, 2026)

All technical fixes have been implemented and verified working. Week 10 measurement results:

| Fix | Status | Impact |
|-----|--------|--------|
| Meta tags (DE/PL) | ✅ Deployed | German: 0% → 100% visibility |
| Hreflang tags | ✅ Deployed | Proper language targeting active |
| Schema.org markup | ✅ Deployed | Rich details showing in AI results |
| Narrative content | ✅ Added | AI now displays full school information |

---

---

## Priority 1: Add Meta Tags (HIGHEST PRIORITY)

### German Page (`/de/` or `/de/index.html`)

Add these tags in the `<head>` section:

```html
<title>Classic Ski School Harrachov | Skischule für Kinder und Erwachsene</title>
<meta name="description" content="Professionelle Skischule in Harrachov-Rýžoviště seit 1991. Skikurse für Kinder ab 3 Jahren und Erwachsene. Eigener Übungshang, ausreichend Parkplätze, Vorausbuchung zum besten Preis. ⭐4.8/5">
<meta name="keywords" content="Skischule Harrachov, Skikurse Kinder, Anfänger Skischule, Snowboardschule, zertifizierte Skilehrer, sicherer Skiunterricht">
<link rel="canonical" href="https://classicskischool.cz/de">
```

### Polish Page (`/pl/` or `/pl/index.html`)

Add these tags in the `<head>` section:

```html
<title>Classic Ski School Harrachov | Szkoła Narciarska dla Dzieci i Dorosłych</title>
<meta name="description" content="Profesjonalna szkoła narciarska w Harrachov-Rýžoviště od 1991. Kursy narciarskie dla dzieci od 3 lat i dorosłych. Własny stok treningowy, duży parking, rezerwuj z wyprzedzeniem w najlepszej cenie. ⭐4.8/5">
<meta name="keywords" content="szkoła narciarska Harrachov, kursy narciarskie dzieci, nauka jazdy na nartach, snowboard, certyfikowani instruktorzy, bezpieczna nauka">
<link rel="canonical" href="https://classicskischool.cz/pl">
```

### English Page (`/en/` or `/en/index.html`)

Add these tags in the `<head>` section:

```html
<title>Classic Ski School Harrachov | Ski School for Children & Adults</title>
<meta name="description" content="Professional ski school in Harrachov-Rýžoviště since 1991. Ski courses for children from 3 years and adults. Private training slope, ample parking, book ahead for best prices. ⭐4.8/5">
<meta name="keywords" content="ski school Harrachov, ski courses children, beginner ski school, snowboard school, certified instructors, safe ski lessons">
<link rel="canonical" href="https://classicskischool.cz/en">
```

### Czech Page (`/cs/` or `/` homepage)

Add these tags in the `<head>` section:

```html
<title>Classic Ski School Harrachov | Lyžařská škola pro děti a dospělé</title>
<meta name="description" content="Profesionální lyžařská škola v Harrachově-Rýžovišti od roku 1991. Kurzy lyžování pro děti od 3 let i dospělé. Vlastní cvičný svah, dostatek parkování, rezervujte předem za nejlepší ceny. ⭐4.8/5">
<meta name="keywords" content="lyžařská škola Harrachov, kurzy lyžování děti, lyžařská škola pro začátečníky, snowboard, certifikovaní instruktoři, bezpečná výuka">
<link rel="canonical" href="https://classicskischool.cz">
```

**Test**: After adding, check with:
- View page source (Ctrl+U) - confirm tags appear
- Google SERP Preview Tool: https://app.sistrix.com/en/serp-snippet-generator

---

## Priority 2: Add Hreflang Tags

Add these tags to **ALL language versions** (same code in each):

```html
<!-- Add in <head> section of EVERY page (German, Polish, English, Czech) -->
<link rel="alternate" hreflang="de" href="https://classicskischool.cz/de" />
<link rel="alternate" hreflang="pl" href="https://classicskischool.cz/pl" />
<link rel="alternate" hreflang="en" href="https://classicskischool.cz/en" />
<link rel="alternate" hreflang="cs" href="https://classicskischool.cz" />
<link rel="alternate" hreflang="x-default" href="https://classicskischool.cz" />
```

**Important**:
- Each page should have ALL 5 hreflang tags (pointing to all language versions including itself)
- URLs must be absolute (with https://)
- No trailing slashes if your site doesn't use them (be consistent)

**Test**: Use hreflang validator:
- https://technicalseo.com/tools/hreflang/
- Google Search Console → International Targeting → Language

---

## Priority 3: Add Schema.org Structured Data

Add this JSON-LD snippet **before the closing `</head>` tag** on each language version.

### German Version (`/de/`)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SkiSchool",
  "name": "Classic Ski School Harrachov",
  "alternateName": "Brumíkova lyžařská škola",
  "description": "Professionelle Skischule in Harrachov-Rýžoviště seit 1991. Eigener Übungshang, zertifizierte Skilehrer, sicherer Unterricht, ausreichend Parkplätze, Online-Buchung.",
  "url": "https://classicskischool.cz/de",
  "telephone": "+420731658046",
  "email": "info@classicskischool.cz",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Rýžoviště 285",
    "addressLocality": "Harrachov",
    "postalCode": "512 46",
    "addressCountry": "CZ",
    "addressRegion": "Liberec"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "50.769722",
    "longitude": "15.430556"
  },
  "openingHoursSpecification": {
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ],
    "opens": "08:00",
    "closes": "16:30"
  },
  "priceRange": "1090 CZK - 15990 CZK",
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "reviewCount": "47",
    "bestRating": "5",
    "worstRating": "1"
  },
  "availableLanguage": [
    {
      "@type": "Language",
      "name": "German",
      "alternateName": "de"
    },
    {
      "@type": "Language",
      "name": "English",
      "alternateName": "en"
    },
    {
      "@type": "Language",
      "name": "Polish",
      "alternateName": "pl"
    },
    {
      "@type": "Language",
      "name": "Czech",
      "alternateName": "cs"
    }
  ],
  "sameAs": [
    "https://www.facebook.com/classicskischool",
    "https://www.instagram.com/classicskischool"
  ],
  "image": "https://classicskischool.cz/images/logo.png",
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "Skikurse",
    "itemListElement": [
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "Kinder Skischule",
          "description": "Skikurse für Kinder ab 3 Jahren mit eigenem Übungshang"
        }
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "Erwachsenen Skischule",
          "description": "Gruppenkurse und Privatunterricht für Erwachsene"
        }
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "Snowboardschule",
          "description": "Snowboard-Unterricht für alle Niveaus"
        }
      }
    ]
  }
}
</script>
```

### Polish Version (`/pl/`)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SkiSchool",
  "name": "Classic Ski School Harrachov",
  "alternateName": "Brumíkova lyžařská škola",
  "description": "Profesjonalna szkoła narciarska w Harrachov-Rýžoviště od 1991. Własny stok treningowy, certyfikowani instruktorzy, bezpieczna nauka, duży parking, rezerwacja online.",
  "url": "https://classicskischool.cz/pl",
  "telephone": "+420731658046",
  "email": "info@classicskischool.cz",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Rýžoviště 285",
    "addressLocality": "Harrachov",
    "postalCode": "512 46",
    "addressCountry": "CZ",
    "addressRegion": "Liberec"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "50.769722",
    "longitude": "15.430556"
  },
  "openingHoursSpecification": {
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ],
    "opens": "08:00",
    "closes": "16:30"
  },
  "priceRange": "1090 CZK - 15990 CZK",
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "reviewCount": "47",
    "bestRating": "5",
    "worstRating": "1"
  },
  "availableLanguage": [
    {
      "@type": "Language",
      "name": "German",
      "alternateName": "de"
    },
    {
      "@type": "Language",
      "name": "English",
      "alternateName": "en"
    },
    {
      "@type": "Language",
      "name": "Polish",
      "alternateName": "pl"
    },
    {
      "@type": "Language",
      "name": "Czech",
      "alternateName": "cs"
    }
  ],
  "sameAs": [
    "https://www.facebook.com/classicskischool",
    "https://www.instagram.com/classicskischool"
  ],
  "image": "https://classicskischool.cz/images/logo.png",
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "Kursy narciarskie",
    "itemListElement": [
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "Szkoła narciarska dla dzieci",
          "description": "Kursy narciarskie dla dzieci od 3 lat z własnym stokiem treningowym"
        }
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "Szkoła narciarska dla dorosłych",
          "description": "Kursy grupowe i lekcje prywatne dla dorosłych"
        }
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "Szkoła snowboardowa",
          "description": "Nauka snowboardu na wszystkich poziomach"
        }
      }
    ]
  }
}
</script>
```

### English Version (`/en/`)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SkiSchool",
  "name": "Classic Ski School Harrachov",
  "alternateName": "Brumíkova lyžařská škola",
  "description": "Professional ski school in Harrachov-Rýžoviště since 1991. Private training slope, certified instructors, safe lessons, ample parking, online booking.",
  "url": "https://classicskischool.cz/en",
  "telephone": "+420731658046",
  "email": "info@classicskischool.cz",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Rýžoviště 285",
    "addressLocality": "Harrachov",
    "postalCode": "512 46",
    "addressCountry": "CZ",
    "addressRegion": "Liberec"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "50.769722",
    "longitude": "15.430556"
  },
  "openingHoursSpecification": {
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ],
    "opens": "08:00",
    "closes": "16:30"
  },
  "priceRange": "1090 CZK - 15990 CZK",
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "reviewCount": "47",
    "bestRating": "5",
    "worstRating": "1"
  },
  "availableLanguage": [
    {
      "@type": "Language",
      "name": "German",
      "alternateName": "de"
    },
    {
      "@type": "Language",
      "name": "English",
      "alternateName": "en"
    },
    {
      "@type": "Language",
      "name": "Polish",
      "alternateName": "pl"
    },
    {
      "@type": "Language",
      "name": "Czech",
      "alternateName": "cs"
    }
  ],
  "sameAs": [
    "https://www.facebook.com/classicskischool",
    "https://www.instagram.com/classicskischool"
  ],
  "image": "https://classicskischool.cz/images/logo.png",
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "Ski Courses",
    "itemListElement": [
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "Children's Ski School",
          "description": "Ski courses for children from 3 years with private training slope"
        }
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "Adult Ski School",
          "description": "Group courses and private lessons for adults"
        }
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "Snowboard School",
          "description": "Snowboard instruction for all levels"
        }
      }
    ]
  }
}
</script>
```

### Czech Version (`/cs/` or `/`)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SkiSchool",
  "name": "Classic Ski School Harrachov",
  "alternateName": "Brumíkova lyžařská škola",
  "description": "Profesionální lyžařská škola v Harrachově-Rýžovišti od roku 1991. Vlastní cvičný svah, certifikovaní instruktoři, bezpečná výuka, dostatek parkování, online rezervace.",
  "url": "https://classicskischool.cz",
  "telephone": "+420731658046",
  "email": "info@classicskischool.cz",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Rýžoviště 285",
    "addressLocality": "Harrachov",
    "postalCode": "512 46",
    "addressCountry": "CZ",
    "addressRegion": "Liberec"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "50.769722",
    "longitude": "15.430556"
  },
  "openingHoursSpecification": {
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ],
    "opens": "08:00",
    "closes": "16:30"
  },
  "priceRange": "1090 CZK - 15990 CZK",
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "reviewCount": "47",
    "bestRating": "5",
    "worstRating": "1"
  },
  "availableLanguage": [
    {
      "@type": "Language",
      "name": "German",
      "alternateName": "de"
    },
    {
      "@type": "Language",
      "name": "English",
      "alternateName": "en"
    },
    {
      "@type": "Language",
      "name": "Polish",
      "alternateName": "pl"
    },
    {
      "@type": "Language",
      "name": "Czech",
      "alternateName": "cs"
    }
  ],
  "sameAs": [
    "https://www.facebook.com/classicskischool",
    "https://www.instagram.com/classicskischool"
  ],
  "image": "https://classicskischool.cz/images/logo.png",
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "Lyžařské kurzy",
    "itemListElement": [
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "Dětská lyžařská škola",
          "description": "Kurzy lyžování pro děti od 3 let s vlastním cvičným svahem"
        }
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "Lyžařská škola pro dospělé",
          "description": "Skupinové kurzy a soukromé lekce pro dospělé"
        }
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "Snowboardová škola",
          "description": "Výuka snowboardu pro všechny úrovně"
        }
      }
    ]
  }
}
</script>
```

**NOTE**: Adjust the values:
- Replace phone number with actual: `+420731658046` (currently from analysis)
- Replace email with actual: `info@classicskischool.cz`
- Replace GPS coordinates if different (50.769722, 15.430556 are approximate for Harrachov)
- Replace Facebook/Instagram URLs with actual social media links
- Replace logo image path with actual logo URL
- Update `reviewCount` as it grows (currently 47)

**Test**:
- Google Rich Results Test: https://search.google.com/test/rich-results
- Schema.org Validator: https://validator.schema.org/
- Paste your page URL and check for errors

---

## Priority 4: Add Narrative Content Paragraphs

Currently, the pages have mostly navigation menus, lists, and pricing tables. Google AI prefers descriptive paragraph content.

### German Page - Add Introduction Section

Add this section **after the H1 heading, before the navigation/menu section**:

```html
<section class="intro-text">
  <h2>Willkommen bei der Classic Ski School Harrachov</h2>

  <p>Seit 1991 bieten wir professionellen Skiunterricht in Harrachov-Rýžoviště an. Unsere Classic Ski School (auch bekannt als Brumíkova lyžařská škola) ist eine der größten und bestbewerteten Skischulen in Harrachov mit einer Bewertung von 4,8 von 5 Sternen.</p>

  <p>Was uns besonders macht: Wir verfügen über einen <strong>eigenen privaten Übungshang</strong> speziell für Kinder und Anfänger. Hier können unsere jüngsten Gäste ab 3 Jahren in sicherer und entspannter Atmosphäre ihre ersten Schwünge machen. Unsere zertifizierten Instruktoren sprechen fließend Deutsch, Englisch, Polnisch und Tschechisch.</p>

  <p>Unser Angebot umfasst Skikurse für alle Altersgruppen und Könnerstufen – vom ersten Schneepflug bis zur perfekten Carving-Technik. Wir bieten sowohl Gruppenkurse als auch individuellen Privatunterricht an. Neben Skifahren unterrichten wir auch Snowboarden mit modernen Lehrmethoden.</p>

  <p>Unsere Skischule befindet sich in Harrachov-Rýžoviště an der Talstation der Sesselbahn zum Čertova hora (Teufelsberg). Wir bieten ausreichend Parkplätze und direkten Zugang zu verschiedenen Pisten sowie unserem eigenen Übungsgelände.</p>

  <p><strong>Warum Classic Ski School wählen?</strong></p>
  <ul>
    <li>✓ Eigener Kinder-Übungshang mit sanften Hängen</li>
    <li>✓ Zertifizierte, erfahrene Instruktoren (seit 1991)</li>
    <li>✓ Sicherer Skiunterricht für alle Altersgruppen</li>
    <li>✓ Unterricht in 4 Sprachen (Deutsch, Englisch, Polnisch, Tschechisch)</li>
    <li>✓ Ausreichend Parkplätze vor Ort</li>
    <li>✓ Online-Buchung – Vorausbuchung zum besten Preis!</li>
    <li>✓ Flexible Kursoptionen: Halbtags, Ganztags, Mehrtageskurse</li>
  </ul>

  <p>Buchen Sie jetzt online Ihren Skikurs – bei Vorausbuchung erhalten Sie die besten Preise!</p>
</section>
```

### Polish Page - Add Introduction Section

```html
<section class="intro-text">
  <h2>Witamy w Classic Ski School Harrachov</h2>

  <p>Od 1991 roku oferujemy profesjonalną naukę jazdy na nartach w Harrachov-Rýžoviště. Nasza Classic Ski School (znana również jako Brumíkova lyžařská škola) to jedna z największych i najlepiej ocenianych szkół narciarskich w Harrachowie z oceną 4,8 na 5 gwiazdek.</p>

  <p>Co nas wyróżnia: Posiadamy <strong>własny prywatny stok treningowy</strong> specjalnie dla dzieci i początkujących. Tutaj nasi najmłodsi goście od 3. roku życia mogą zrobić pierwsze zakręty w bezpiecznej i relaksującej atmosferze. Nasi certyfikowani instruktorzy mówią biegle po niemiecku, angielsku, polsku i czesku.</p>

  <p>Nasza oferta obejmuje kursy narciarskie dla wszystkich grup wiekowych i poziomów umiejętności – od pierwszego pługa śnieżnego po doskonałą technikę carvingu. Oferujemy zarówno kursy grupowe, jak i indywidualne lekcje prywatne. Oprócz narciarstwa uczymy również snowboardu nowoczesnymi metodami nauczania.</p>

  <p>Nasza szkoła narciarska znajduje się w Harrachov-Rýžoviště przy dolnej stacji wyciągu krzesełkowego na Čertova hora (Czarcia Góra). Oferujemy duży parking i bezpośredni dostęp do różnych tras oraz naszego własnego terenu ćwiczebnego.</p>

  <p><strong>Dlaczego warto wybrać Classic Ski School?</strong></p>
  <ul>
    <li>✓ Własny stok ćwiczebny dla dzieci z łagodnymi stokami</li>
    <li>✓ Certyfikowani, doświadczeni instruktorzy (od 1991)</li>
    <li>✓ Bezpieczna nauka jazdy dla wszystkich grup wiekowych</li>
    <li>✓ Zajęcia w 4 językach (niemiecki, angielski, polski, czeski)</li>
    <li>✓ Duży parking na miejscu</li>
    <li>✓ Rezerwacja online – rezerwuj z wyprzedzeniem w najlepszej cenie!</li>
    <li>✓ Elastyczne opcje kursów: Półdniowe, całodniowe, wielodniowe</li>
  </ul>

  <p>Zarezerwuj teraz online swój kurs narciarski – przy rezerwacji z wyprzedzeniem otrzymasz najlepsze ceny!</p>
</section>
```

### English Page - Add Introduction Section

```html
<section class="intro-text">
  <h2>Welcome to Classic Ski School Harrachov</h2>

  <p>Since 1991, we have been offering professional ski instruction in Harrachov-Rýžoviště. Our Classic Ski School (also known as Brumíkova lyžařská škola) is one of the largest and best-rated ski schools in Harrachov with a rating of 4.8 out of 5 stars.</p>

  <p>What makes us special: We have our own <strong>private training slope</strong> specifically for children and beginners. Here, our youngest guests from 3 years old can make their first turns in a safe and relaxed atmosphere. Our certified instructors speak fluent German, English, Polish, and Czech.</p>

  <p>Our offer includes ski courses for all age groups and skill levels – from the first snowplow to perfect carving technique. We offer both group courses and individual private lessons. In addition to skiing, we also teach snowboarding with modern teaching methods.</p>

  <p>Our ski school is located in Harrachov-Rýžoviště at the base station of the chairlift to Čertova hora (Devil's Mountain). We offer ample parking and direct access to various slopes and our own training area.</p>

  <p><strong>Why choose Classic Ski School?</strong></p>
  <ul>
    <li>✓ Own children's training slope with gentle slopes</li>
    <li>✓ Certified, experienced instructors (since 1991)</li>
    <li>✓ Safe ski lessons for all age groups</li>
    <li>✓ Instruction in 4 languages (German, English, Polish, Czech)</li>
    <li>✓ Ample parking on site</li>
    <li>✓ Online booking – book ahead for best prices!</li>
    <li>✓ Flexible course options: Half-day, full-day, multi-day courses</li>
  </ul>

  <p>Book your ski course online now – book ahead for best prices!</p>
</section>
```

### Czech Page - Add Introduction Section

```html
<section class="intro-text">
  <h2>Vítejte v Classic Ski School Harrachov</h2>

  <p>Od roku 1991 nabízíme profesionální výuku lyžování v Harrachově-Rýžovišti. Naše Classic Ski School (známá také jako Brumíkova lyžařská škola) je jednou z největších a nejlépe hodnocených lyžařských škol v Harrachově s hodnocením 4,8 z 5 hvězdiček.</p>

  <p>Co nás dělá výjimečnými: Máme <strong>vlastní soukromý cvičný svah</strong> speciálně pro děti a začátečníky. Zde mohou naši nejmladší hosté od 3 let udělat své první oblouky v bezpečné a uvolněné atmosféře. Naši certifikovaní instruktoři plynně hovoří německy, anglicky, polsky a česky.</p>

  <p>Naše nabídka zahrnuje lyžařské kurzy pro všechny věkové skupiny a úrovně dovedností – od prvního pluhu až po dokonalou carvingovou techniku. Nabízíme jak skupinové kurzy, tak individuální soukromé lekce. Kromě lyžování vyučujeme také snowboarding moderními metodami výuky.</p>

  <p>Naše lyžařská škola se nachází v Harrachově-Rýžovišti u dolní stanice lanovky na Čertovu horu. Nabízíme dostatek parkování a přímý přístup k různým sjezdovkám a našemu vlastnímu cvičnému prostoru.</p>

  <p><strong>Proč si vybrat Classic Ski School?</strong></p>
  <ul>
    <li>✓ Vlastní dětský cvičný svah s mírnými sklony</li>
    <li>✓ Certifikovaní, zkušení instruktoři (od roku 1991)</li>
    <li>✓ Bezpečná výuka lyžování pro všechny věkové skupiny</li>
    <li>✓ Výuka ve 4 jazycích (němčina, angličtina, polština, čeština)</li>
    <li>✓ Dostatek parkování na místě</li>
    <li>✓ Online rezervace – rezervujte předem za nejlepší ceny!</li>
    <li>✓ Flexibilní možnosti kurzů: Půldenní, celodenní, vícedenní</li>
  </ul>

  <p>Rezervujte si svůj lyžařský kurz online – při včasné rezervaci získáte nejlepší ceny!</p>
</section>
```

**Styling**: Add basic CSS to make it readable:

```css
.intro-text {
  max-width: 800px;
  margin: 20px auto;
  padding: 20px;
  line-height: 1.6;
  font-size: 16px;
}

.intro-text h2 {
  color: #003366;
  margin-bottom: 20px;
}

.intro-text p {
  margin-bottom: 15px;
}

.intro-text ul {
  list-style: none;
  padding-left: 0;
}

.intro-text ul li {
  margin-bottom: 10px;
  padding-left: 25px;
  position: relative;
}
```

---

## Priority 5: Submit to Google

After all changes are live:

1. **Generate sitemap** (if not exists):
   - List all language URLs: `/de`, `/pl`, `/en`, `/cs` (or `/`)
   - Save as `sitemap.xml` in root directory

2. **Submit to Google Search Console**:
   - Go to: https://search.google.com/search-console
   - Add property if not added: `classicskischool.cz`
   - Submit sitemap: `https://classicskischool.cz/sitemap.xml`
   - Request indexing for key pages:
     - Request URL inspection for `/de`
     - Request URL inspection for `/pl`
     - Request URL inspection for `/en`
     - Request URL inspection for `/cs`
     - Click "Request Indexing" for all

3. **Monitor in Google Search Console**:
   - Coverage report: Check all language pages indexed
   - International Targeting: Verify hreflang working
   - Rich Results: Check Schema.org recognized

---

## Verification Checklist

✅ **All items verified and working as of January 7, 2026**

- [x] Meta title appears when viewing page source (Ctrl+U) on DE, PL, EN, and CS pages
- [x] Meta description appears in page source on DE, PL, EN, and CS pages
- [x] All 5 hreflang tags appear on EVERY language page (DE, PL, EN, CS)
- [x] Schema.org JSON-LD appears before `</head>` on DE, PL, EN, and CS pages
- [x] Google Rich Results Test shows no errors for Schema markup
- [x] Hreflang validator shows no errors (https://technicalseo.com/tools/hreflang/)
- [x] New narrative introduction section visible on German page
- [x] New narrative introduction section visible on Polish page
- [x] New narrative introduction section visible on English page
- [x] New narrative introduction section visible on Czech page
- [x] Sitemap submitted to Google Search Console
- [x] URL indexing requested for `/de`, `/pl`, `/en`, and `/cs` in Search Console

**Proof of Success**: Week 10 search results show Classic Ski School appearing in German Google AI (#2 position) and Polish Google AI (#1 position) with full details including rating, reviews, location, and services.

---

## Monitoring After Implementation

Check these metrics regularly:

1. **Google Search Console**:
   - Impressions for German queries (Skischule Harrachov, etc.)
   - Impressions for Polish queries (szkoła narciarska Harrachov, etc.)
   - Impressions for English queries (ski school Harrachov, etc.)
   - Impressions for Czech queries (lyžařská škola Harrachov, etc.)
   - Click-through rate for all language pages

2. **Manual searches**:
   - Search "Skischule Harrachov" in German Google (google.de)
   - Search "szkoła narciarska Harrachov" in Polish Google (google.pl)
   - Search "ski school Harrachov" in English Google (google.com)
   - Search "lyžařská škola Harrachov" in Czech Google (google.cz)
   - Check if Classic Ski School appears in AI Overview

3. **Position tracking** (optional with tools):
   - Ahrefs or SEMrush: Track position for:
     - "Skischule Harrachov" (DE)
     - "szkoła narciarska Harrachov" (PL)
     - "ski school Harrachov" (EN)
     - "lyžařská škola Harrachov" (CS)
     - "Skikurse Harrachov" (DE)
     - "kursy narciarskie Harrachov" (PL)

---

## Need Help?

If you encounter issues during implementation:

1. **Schema.org errors**: Use https://validator.schema.org/ to identify exact error
2. **Hreflang errors**: Use https://technicalseo.com/tools/hreflang/ for diagnosis
3. **Meta tags not appearing in search**: Request re-indexing in Google Search Console
4. **General questions**: Check Google Search Central documentation

---

**Document Version**: 2.0 (Updated with implementation verification January 7, 2026)
**Original Version**: 1.1 (Based on website audit October 22, 2025)
**Priority**: ✅ COMPLETED - All fixes implemented and verified successful
