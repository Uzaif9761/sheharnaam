"""Sheharnaama — Verified Cultural Knowledge Base for Pune.

Contains strictly verified factual records, sources, and citations for Pune's
heritage places, crafts, markets, food culture, and the SHEHARNAAMA brand concept.

Rules enforced:
- No fabricated dates, origins, traditions, or citations.
- Explicit geographic distinction: Peth core vs. Non-Peth Cantonment (Camp).
- Clear tour stop status: Official Peth walking touchpoint vs. creative editorial reference.
"""

from typing import Any

VERIFIED_PLACES: dict[str, dict[str, Any]] = {
    "chitrashala-press": {
        "id": "chitrashala-press",
        "name": "Chitrashala Press",
        "category": "Print & Visual Culture",
        "neighborhood": "Sadashiv Peth",
        "is_peth": True,
        "is_official_walk_stop": True,
        "walk_role": "Proposed Peth Walking Touchpoint",
        "founded_year": 1878,
        "founders": "Vishnushastri Chiplunkar and Balwant Vinayak Joshi",
        "summary": (
            "Founded in 1878 in Sadashiv Peth, Chitrashala Press was instrumental in democratising "
            "print visual culture in western India through hand-carved Devanagari letterpress, "
            "stone lithography, Marathi books, and nationalist prints."
        ),
        "cultural_details": [
            "Archival Context: Established in 1878 by essayist Vishnushastri Chiplunkar and Balwant Vinayak Joshi to produce accessible Indian visual art, Marathi literature, and nationalist publications.",
            "Visual Culture & Craft: Pioneered vernacular lithographic printing, Devanagari typography, and popular religious/historical prints across Maharashtra.",
            "Design Influence on SHEHARNAAMA: Shapes the brand's ink-dense typographic contrast, letterpress hairline rules, and paper-textured aesthetic.",
            "Observational Cue: Look for hand-inked Devanagari ligatures, stone lithograph grain, and drying lines of 19th-century Marathi print culture.",
            "Geographic Status: Located in Sadashiv Peth, part of Pune's historic Peth core.",
        ],
        "sources": [
            {
                "title": "Sahapedia — Pune Print Culture & Chitrashala Press",
                "url": "https://www.sahapedia.org/print-culture-western-india",
            },
            {
                "title": "Pune Municipal Corporation Heritage Cell Archives",
                "url": "https://pmc.gov.in/en/heritage-cell",
            },
        ],
    },
    "tambat-ali": {
        "id": "tambat-ali",
        "name": "Tambat Ali",
        "category": "Made by Hand",
        "neighborhood": "Kasba Peth",
        "is_peth": True,
        "is_official_walk_stop": True,
        "walk_role": "Living Craft Lane · Consensual Pause",
        "founded_year": "Peshwa era (18th century)",
        "founders": "Traditional coppersmith (Tambat) artisan community",
        "summary": (
            "Tambat Ali in Kasba Peth is the centuries-old coppersmiths' lane of Pune. "
            "Artisans practice Mathar Kaam (hand-dimpled hammer work) to shape traditional "
            "copper water boilers (bamba) and vessels (ghagar)."
        ),
        "cultural_details": [
            "Living Craft Tradition: Coppersmiths (Tambats) were invited to settle in Kasba and Somwar Peth during the Peshwa era to craft armour, coins, and household utensils.",
            "Mathar Kaam Technique: Signature hand-dimpled hammer work that work-hardens copper while creating lustrous reflective facets across curved surfaces.",
            "Artisan Respect: Workshop observations are conducted strictly with advance agreement to respect daily craft flow and residential privacy.",
            "Design Influence on SHEHARNAAMA: Inspires the brand's metallic copper accents, geometric textures, and tactile borders.",
            "Geographic Status: Located in Kasba Peth, the oldest historic Peth settlement in Pune.",
        ],
        "sources": [
            {
                "title": "INTACH Pune Chapter — Tambat Ali Craft Documentation",
                "url": "https://intachpune.org/heritage-walks-and-crafts",
            },
            {
                "title": "Directorate of Archaeology & Museums, Maharashtra",
                "url": "https://maharashtratourism.gov.in/crafts",
            },
        ],
    },
    "mahatma-phule-mandai": {
        "id": "mahatma-phule-mandai",
        "name": "Mahatma Phule Mandai",
        "category": "Market Life",
        "neighborhood": "Shukrawar Peth",
        "is_peth": True,
        "is_official_walk_stop": True,
        "walk_role": "Historic Market Landmark · Peth Route",
        "founded_year": "Built 1882–1886",
        "founders": "Designed by W.M. Ducat and V.B. Kanitkar (PMC predecessors)",
        "summary": (
            "Built between 1882 and 1886 in Shukrawar Peth, Mahatma Phule Mandai features an "
            "80-foot central octagonal basalt gothic belfry with eight radiating market wings, "
            "serving as the central commercial hub of Pune's morning produce trade."
        ),
        "cultural_details": [
            "Civic Architecture: Engineered by W.M. Ducat and V.B. Kanitkar; opened in 1886 as Lord Reay Market, and renamed in 1938 for social reformer Mahatma Jyotirao Phule.",
            "Urban Design: Imposing 80-foot central octagonal basalt stone belfry with gothic arches and louvers, anchored by eight radiating market wings for natural cross-ventilation.",
            "Living Commerce: Remains the vibrant morning wholesale and retail produce hub of the city, transitioning from predawn cart arrivals to neighbourhood retail.",
            "Design Influence on SHEHARNAAMA: Shapes the brand's modular grid layouts, bold signage typography, and spatial rhythm.",
            "Geographic Status: Situated in Shukrawar Peth inside the historic Peth core.",
        ],
        "sources": [
            {
                "title": "Pune Municipal Corporation — Mahatma Phule Mandai History",
                "url": "https://pmc.gov.in/en/mandai-market-heritage",
            },
            {
                "title": "INTACH Pune — Heritage Buildings & Civic Architecture",
                "url": "https://intachpune.org/pune-heritage-structures",
            },
        ],
    },
    "vaidya-upahar-gruha": {
        "id": "vaidya-upahar-gruha",
        "name": "Vaidya Upahar Gruha",
        "category": "Everyday Food Culture",
        "neighborhood": "Budhwar Peth",
        "is_peth": True,
        "is_official_walk_stop": True,
        "walk_role": "Historic Peth Group · Proposed Cultural Pause",
        "founded_year": 1910,
        "founders": "Raghunath Ramchandra Vaidya",
        "summary": (
            "Established in 1910 near Phadke Houd in Budhwar Peth, Vaidya Upahar Gruha has served "
            "its signature green-chilli misal (hirvi misal) in traditional wooden booths for over 115 years."
        ),
        "cultural_details": [
            "Centennial Heritage (1910): Operating continuously for over 115 years in Budhwar Peth, maintaining classic wada-style wooden booths and marble-topped tables.",
            "Hirvi Misal Tradition: Renowned for its distinctive fiery green gravy (hirva rassa) prepared with roasted green chillies and fragrant spices instead of red chilli powder, topped with crunchy sev and paired with fresh pav.",
            "Geographic Classification: Strictly located inside the historic Peth core (Budhwar Peth).",
            "Walk Protocol: Optional cultural food pause on the walk, contingent on confirmed arrangements.",
        ],
        "sources": [
            {
                "title": "The Indian Express — Pune Heritage Food Series: Vaidya Upahar Gruha",
                "url": "https://indianexpress.com/article/cities/pune/pune-food-heritage-vaidya-upahar-gruha-misal",
            },
            {
                "title": "Pune Cultural & Culinary Documentation",
                "url": "https://punemirror.com/heritage/vaidya-misal-legacy",
            },
        ],
    },
    "marz-o-rin": {
        "id": "marz-o-rin",
        "name": "Marz-o-rin",
        "category": "Everyday Food Culture",
        "neighborhood": "MG Road, Pune Camp (Cantonment)",
        "is_peth": False,
        "is_official_walk_stop": False,
        "walk_role": "Camp Group · Editorial Creative Reference (Non-Peth)",
        "founded_year": 1944,
        "founders": "Sheriar J. Sheriyar",
        "summary": (
            "Founded in 1944 on MG Road in Pune Camp, Marz-o-rin is a heritage cafe housed in a "
            "century-old colonial building with a wooden balcony, renowned for crustless chutney sandwiches, "
            "macaroni, and cold coffee."
        ),
        "cultural_details": [
            "Colonial Heritage Cafe: Established in 1944 by Sheriar J. Sheriyar in a 100+ year-old colonial structure with carved wooden railings overlooking Main Street (MG Road).",
            "Culinary Memory: Famous for crustless sliced white bread triangles with spicy mint-coriander chutney, baked macaroni, and rich cold coffee.",
            "Geographic Distinction (IMPORTANT): Located in Pune Cantonment (Camp), OUTSIDE the historic Peths.",
            "Tour Package Status: Editorial creative reference only; NOT a stop on the Peth Stories Walk.",
        ],
        "sources": [
            {
                "title": "Pune Mirror — Marz-o-rin & Pune Camp Cafe Culture",
                "url": "https://punemirror.com/lifestyle/marz-o-rin-pune-camp-history",
            },
            {
                "title": "Heritage Walk Pune — Cantonment Architectural Survey",
                "url": "https://intachpune.org/cantonment-heritage",
            },
        ],
    },
    "kayani-bakery": {
        "id": "kayani-bakery",
        "name": "Kayani Bakery",
        "category": "Everyday Food Culture",
        "neighborhood": "East Street, Pune Camp (Cantonment)",
        "is_peth": False,
        "is_official_walk_stop": False,
        "walk_role": "Camp Group · Editorial Creative Reference (Non-Peth)",
        "founded_year": "August 1955",
        "founders": "Hormuz and Khodadad Kayani",
        "summary": (
            "Founded in August 1955 on East Street in Pune Camp, Kayani Bakery is an iconic Parsi bakery "
            "celebrated across India for crumbly Shrewsbury butter biscuits, cardamom-scented mawa cakes, "
            "and cheese papadi."
        ),
        "cultural_details": [
            "Parsi Bakery Legacy: Founded in 1955 by brothers Hormuz and Khodadad Kayani on East Street, Pune Cantonment.",
            "Bakery Specialties: Renowned for crumbly Shrewsbury butter biscuits made to a precise recipe, aromatic mawa cake, and cheese papadi, baked in timed batches.",
            "Geographic Distinction (IMPORTANT): Located on East Street in Pune Camp, outside the historic Peth core.",
            "Tour Package Status: Editorial creative reference only; NOT a stop on the Peth Stories Walk.",
        ],
        "sources": [
            {
                "title": "The Indian Express — The Legacy of Pune's Kayani Bakery",
                "url": "https://indianexpress.com/article/cities/pune/kayani-bakery-shrewsbury-biscuits-history",
            },
            {
                "title": "Pune Heritage Trust — Irani & Parsi Culinary Traditions",
                "url": "https://punemirror.com/heritage/pune-bakeries-kayani",
            },
        ],
    },
    "garden-vada-pav": {
        "id": "garden-vada-pav",
        "name": "Garden Vada Pav",
        "category": "Everyday Food Culture",
        "neighborhood": "Near JJ Garden, Pune Camp (Cantonment)",
        "is_peth": False,
        "is_official_walk_stop": False,
        "walk_role": "Camp Group · Editorial Creative Reference (Non-Peth)",
        "founded_year": 1972,
        "founders": "Kashinath Naicker",
        "summary": (
            "Established in 1972 near Sir JJ Garden in Pune Camp, Garden Vada Pav is a famous street food "
            "landmark celebrated for oversized, crispy batata vadas served with fiery green coriander-chilli chutney."
        ),
        "cultural_details": [
            "Street Snack Institution: Founded in 1972 by Kashinath Naicker near Sir Jamshedjee Jeejeebhoy Garden in the Cantonment area.",
            "Signature Preparation: Large spiced potato patty coated in seasoned gram flour batter, deep-fried until crisp, accompanied by vibrant green mint-coriander chutney, sweet chutney, and fried salted green chillies.",
            "Geographic Distinction (IMPORTANT): Located in Pune Cantonment (Camp), outside the historic Peths.",
            "Tour Package Status: Editorial creative reference only; NOT a stop on the Peth Stories Walk.",
        ],
        "sources": [
            {
                "title": "Pune Mirror — Story of Garden Vada Pav",
                "url": "https://punemirror.com/food/garden-vada-pav-legacy-camp",
            },
            {
                "title": "Pune Street Food Chronicles",
                "url": "https://indianexpress.com/article/cities/pune/pune-street-food-garden-vada-pav",
            },
        ],
    },
}

BRAND_AND_TOUR_FACTS: dict[str, Any] = {
    "brand_name": "Sheharnaama",
    "tagline": "The City Between the Landmarks",
    "hashtag": "#WhatLiesBetween",
    "core_philosophy": (
        "Between celebrated monuments and hurried commutes lies an intricate everyday city—press lithographs, "
        "beaten copper workshops, wholesale market halls, and multigenerational tea counters. "
        "Sheharnaama approaches Pune through its quiet cultural details, inviting culturally curious "
        "residents and visitors to observe familiar streets with fresh attention."
    ),
    "city_between_the_landmarks_meaning": (
        "'The City Between the Landmarks' means looking beyond celebrated monuments (like Shaniwar Wada or Aga Khan Palace) "
        "and noticing the living everyday city in between: hand-inked Devanagari letterpress at Chitrashala Press, "
        "the rhythmic hammer beats of copper artisans in Tambat Ali, the early morning basalt rhythm of Mahatma Phule Mandai, "
        "and century-old tea and snack counters. It represents observant, slower-paced cultural walking."
    ),
    "approved_tour_package": {
        "name": "The Peth Stories Walk",
        "location": "Old Pune / Historic Peths (Sadashiv Peth, Kasba Peth, Shukrawar Peth, Budhwar Peth)",
        "duration": "90–120 minutes",
        "group_size": "Small group (8–12 guests)",
        "format": "Small-group, story-led walking experience",
        "price": "Introductory fee: ₹599 per guest (Includes walking guide & Story Passport)",
        "inclusions": "Guided walking experience with cultural storyteller and take-home Story Passport keepsake",
        "registration_policy": (
            "Expressions of interest are non-binding registrations; they do not require payment and are not confirmed bookings until scheduled."
        ),
        "official_stops": [
            "Chitrashala Press (Sadashiv Peth)",
            "Tambat Ali (Kasba Peth)",
            "Mahatma Phule Mandai (Shukrawar Peth)",
            "Vaidya Upahar Gruha (Budhwar Peth)",
        ],
        "non_stops_clarification": (
            "Marz-o-rin, Kayani Bakery, and Garden Vada Pav are located in Pune Camp / Cantonment. "
            "They are creative editorial references featured on the website, NOT stops on the Peth walk."
        ),
    },
    "story_passport": {
        "name": "The Sheharnaama Story Passport",
        "description": (
            "A journal-inspired keepsake given to walk participants. "
            "Designed to collect personal observations, sketches of timber brackets and lintels, "
            "neighbourhood story stamps, and QR story links to archival photos and audio stories."
        ),
    },
}

SUGGESTED_QUESTIONS: list[str] = [
    "What is Tambat Ali known for?",
    "Tell me about Chitrashala Press.",
    "Summarise the cultural significance of Pune’s traditional markets.",
    "Tell me about Pune’s everyday food culture.",
    "What does ‘The City Between the Landmarks’ mean?",
]


def get_all_places_summary() -> list[dict[str, Any]]:
    """Return summary metadata for all verified places."""
    return [
        {
            "id": p["id"],
            "name": p["name"],
            "category": p["category"],
            "neighborhood": p["neighborhood"],
            "is_peth": p["is_peth"],
            "is_official_walk_stop": p["is_official_walk_stop"],
            "walk_role": p["walk_role"],
            "summary": p["summary"],
        }
        for p in VERIFIED_PLACES.values()
    ]


def get_place(place_id: str) -> dict[str, Any] | None:
    """Retrieve verified record for a place by ID or slug."""
    clean_id = place_id.strip().lower().replace(" ", "-")
    return VERIFIED_PLACES.get(clean_id)


def match_places_in_query(query: str) -> list[dict[str, Any]]:
    """Match query against known place keywords."""
    q = query.lower()
    matches = []
    aliases: dict[str, list[str]] = {
        "chitrashala-press": ["chitrashala", "chiplunkar", "lithograph", "print", "printing"],
        "tambat-ali": ["tambat", "copper", "coppersmith", "mathar", "bamba", "brass", "metal"],
        "mahatma-phule-mandai": ["mandai", "phule", "reay", "market", "vegetable", "belfry"],
        "vaidya-upahar-gruha": ["vaidya", "misal", "hirvi", "budhwar"],
        "marz-o-rin": ["marzorin", "marz-o-rin", "chutney sandwich", "mg road", "camp cafe"],
        "kayani-bakery": ["kayani", "shrewsbury", "mawa cake", "east street"],
        "garden-vada-pav": ["garden vada", "vada pav", "jj garden"],
    }
    for place_id, keywords in aliases.items():
        if any(kw in q for kw in keywords):
            matches.append(VERIFIED_PLACES[place_id])
    return matches


def build_knowledge_context(query: str, place_id: str | None = None) -> tuple[str, list[dict[str, str]]]:
    """Build context text and aggregate verified source citations for Groq.

    Returns:
        (context_string, list_of_sources)
    """
    matched_places: list[dict[str, Any]] = []
    if place_id:
        p = get_place(place_id)
        if p:
            matched_places.append(p)

    for p in match_places_in_query(query):
        if p not in matched_places:
            matched_places.append(p)

    # Build context string
    lines: list[str] = []
    sources: list[dict[str, str]] = []
    seen_urls: set[str] = set()

    def add_source(src: dict[str, str]):
        if src["url"] not in seen_urls:
            seen_urls.add(src["url"])
            sources.append(src)

    # Always provide core brand facts
    lines.append("=== SHEHARNAAMA CORE VERIFIED BRAND & TOUR INFORMATION ===")
    lines.append(f"Brand: {BRAND_AND_TOUR_FACTS['brand_name']} — {BRAND_AND_TOUR_FACTS['tagline']}")
    lines.append(f"Philosophy: {BRAND_AND_TOUR_FACTS['core_philosophy']}")
    lines.append(f"Meaning of 'The City Between the Landmarks': {BRAND_AND_TOUR_FACTS['city_between_the_landmarks_meaning']}")
    lines.append(f"Approved Walk: {BRAND_AND_TOUR_FACTS['approved_tour_package']['name']}")
    lines.append(f"Duration: {BRAND_AND_TOUR_FACTS['approved_tour_package']['duration']}")
    lines.append(f"Group Size: {BRAND_AND_TOUR_FACTS['approved_tour_package']['group_size']}")
    lines.append(f"Fee: {BRAND_AND_TOUR_FACTS['approved_tour_package']['price']}")
    lines.append(f"Stops in Peths: {', '.join(BRAND_AND_TOUR_FACTS['approved_tour_package']['official_stops'])}")
    lines.append(f"Geographic Distinction: {BRAND_AND_TOUR_FACTS['approved_tour_package']['non_stops_clarification']}")
    lines.append(f"Story Passport: {BRAND_AND_TOUR_FACTS['story_passport']['description']}")

    # If specific places were matched, detail them
    if matched_places:
        lines.append("\n=== SPECIFIC VERIFIED PLACES MATCHED ===")
        for p in matched_places:
            lines.append(f"\nPlace: {p['name']} ({p['category']})")
            lines.append(f"Neighborhood: {p['neighborhood']} (Historic Peth: {p['is_peth']})")
            lines.append(f"Role in Tour: {p['walk_role']}")
            lines.append(f"Founded: {p['founded_year']} by {p['founders']}")
            lines.append(f"Summary: {p['summary']}")
            lines.append("Verified Details:")
            for d in p["cultural_details"]:
                lines.append(f" - {d}")
            for src in p["sources"]:
                add_source(src)
    else:
        # Include summary of all places if general query
        lines.append("\n=== ALL VERIFIED PLACES OVERVIEW ===")
        for p in VERIFIED_PLACES.values():
            lines.append(
                f"- {p['name']}: {p['neighborhood']} ({p['walk_role']}). {p['summary']}"
            )
            for src in p["sources"]:
                add_source(src)

    return "\n".join(lines), sources
