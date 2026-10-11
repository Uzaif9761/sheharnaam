"""Generates high-fidelity place SVGs for the 7 Pune cultural references.
Each SVG uses the SHEHARNAAMA brand palette (terracotta, cream, charcoal, indigo, warm-white, copper).
"""
import pathlib

OUT_DIR = pathlib.Path("assets/img")

SVGS = {}

# 1. Chitrashala Press (Sadashiv Peth) - Print & Visual Culture
SVGS["place-chitrashala.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 400" role="img" aria-label="Illustration of Chitrashala Press with lithographic roller, Devanagari letterpress types, paper sheets and ink brayer">
  <defs>
    <linearGradient id="cs_bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#F5EAD9"/>
      <stop offset="100%" stop-color="#E8D9C0"/>
    </linearGradient>
    <filter id="cs_grain">
      <feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="2" stitchTiles="stitch"/>
      <feColorMatrix type="matrix" values="0 0 0 0 0.2  0 0 0 0 0.19  0 0 0 0 0.18  0 0 0 0.05 0"/>
    </filter>
  </defs>
  <rect width="640" height="400" fill="url(#cs_bg)"/>

  <!-- Archival drying lines and hung proof sheets -->
  <line x1="40" y1="45" x2="600" y2="45" stroke="#4A4744" stroke-width="2" stroke-dasharray="8 6"/>
  <!-- Proof sheet 1 -->
  <rect x="80" y="45" width="90" height="120" fill="#F9F6F0" stroke="#33312F" stroke-width="2" transform="rotate(-3 80 45)"/>
  <rect x="92" y="62" width="66" height="40" fill="#AD6046" opacity="0.85" transform="rotate(-3 80 45)"/>
  <line x1="92" y1="112" x2="158" y2="112" stroke="#33312F" stroke-width="2" transform="rotate(-3 80 45)"/>
  <line x1="92" y1="124" x2="148" y2="124" stroke="#667B82" stroke-width="2" transform="rotate(-3 80 45)"/>
  <circle cx="125" cy="46" r="4" fill="#8C4B36"/>

  <!-- Proof sheet 2 (Center) -->
  <rect x="230" y="45" width="105" height="135" fill="#F9F6F0" stroke="#33312F" stroke-width="2" transform="rotate(2 230 45)"/>
  <rect x="242" y="65" width="80" height="55" fill="#33312F" transform="rotate(2 230 45)"/>
  <text x="256" y="103" font-family="'Playfair Display', Georgia, serif" font-size="28" fill="#F2E6D5" transform="rotate(2 230 45)">चित्र</text>
  <line x1="244" y1="130" x2="320" y2="130" stroke="#AD6046" stroke-width="2" transform="rotate(2 230 45)"/>
  <line x1="244" y1="142" x2="305" y2="142" stroke="#4A4744" stroke-width="2" transform="rotate(2 230 45)"/>
  <circle cx="282" cy="46" r="4" fill="#8C4B36"/>

  <!-- Proof sheet 3 -->
  <rect x="400" y="45" width="95" height="125" fill="#F9F6F0" stroke="#33312F" stroke-width="2" transform="rotate(-1 400 45)"/>
  <rect x="412" y="64" width="70" height="46" fill="#667B82" opacity="0.9" transform="rotate(-1 400 45)"/>
  <circle cx="447" cy="87" r="14" fill="#F2E6D5" transform="rotate(-1 400 45)"/>
  <line x1="412" y1="120" x2="480" y2="120" stroke="#33312F" stroke-width="2" transform="rotate(-1 400 45)"/>
  <circle cx="447" cy="46" r="4" fill="#8C4B36"/>

  <!-- Heavy print shop worktable -->
  <rect x="50" y="270" width="540" height="24" fill="#8C4B36" stroke="#33312F" stroke-width="3"/>
  <rect x="70" y="294" width="22" height="106" fill="#7A4030" stroke="#33312F" stroke-width="3"/>
  <rect x="548" y="294" width="22" height="106" fill="#7A4030" stroke="#33312F" stroke-width="3"/>
  <line x1="80" y1="360" x2="560" y2="360" stroke="#4A4744" stroke-width="4"/>

  <!-- Lithographic stone / press bed -->
  <rect x="90" y="235" width="240" height="35" rx="3" fill="#667B82" stroke="#33312F" stroke-width="3"/>
  <rect x="100" y="240" width="220" height="25" fill="#4F6169"/>
  <!-- Ink roller (brayer) on table -->
  <rect x="140" y="200" width="120" height="26" rx="13" fill="#33312F" stroke="#AD6046" stroke-width="3"/>
  <path d="M200 200 v-30 h-10 v-25 h20 v25 h-10" fill="#C87A54" stroke="#33312F" stroke-width="2"/>

  <!-- Letterpress type-case drawer with wooden blocks -->
  <rect x="360" y="195" width="210" height="75" fill="#E3D3BD" stroke="#33312F" stroke-width="3"/>
  <!-- Grid of types -->
  <g stroke="#AD6046" stroke-width="1.5">
    <line x1="395" y1="195" x2="395" y2="270"/>
    <line x1="430" y1="195" x2="430" y2="270"/>
    <line x1="465" y1="195" x2="465" y2="270"/>
    <line x1="500" y1="195" x2="500" y2="270"/>
    <line x1="535" y1="195" x2="535" y2="270"/>
    <line x1="360" y1="220" x2="570" y2="220"/>
    <line x1="360" y1="245" x2="570" y2="245"/>
  </g>
  <!-- Lead / wooden type characters reversed -->
  <text x="372" y="214" font-family="'Playfair Display', serif" font-weight="700" font-size="16" fill="#33312F">अ</text>
  <text x="407" y="214" font-family="'Playfair Display', serif" font-weight="700" font-size="16" fill="#AD6046">शा</text>
  <text x="442" y="214" font-family="'Playfair Display', serif" font-weight="700" font-size="16" fill="#33312F">ला</text>
  <text x="477" y="214" font-family="'Playfair Display', serif" font-weight="700" font-size="16" fill="#667B82">पु</text>
  <text x="512" y="214" font-family="'Playfair Display', serif" font-weight="700" font-size="16" fill="#33312F">णे</text>
  <text x="546" y="214" font-family="'Playfair Display', serif" font-weight="700" font-size="16" fill="#AD6046">१८</text>
  <text x="372" y="239" font-family="'Playfair Display', serif" font-weight="700" font-size="15" fill="#AD6046">क</text>
  <text x="407" y="239" font-family="'Playfair Display', serif" font-weight="700" font-size="15" fill="#33312F">म</text>
  <text x="442" y="239" font-family="'Playfair Display', serif" font-weight="700" font-size="15" fill="#667B82">र</text>
  <text x="477" y="239" font-family="'Playfair Display', serif" font-weight="700" font-size="15" fill="#33312F">थ</text>
  <text x="512" y="239" font-family="'Playfair Display', serif" font-weight="700" font-size="15" fill="#AD6046">प</text>
  <text x="547" y="239" font-family="'Playfair Display', serif" font-weight="700" font-size="15" fill="#33312F">त्र</text>

  <!-- Editorial press stamp label -->
  <g transform="translate(480, 290)">
    <rect x="0" y="0" width="115" height="42" fill="#F9F6F0" stroke="#AD6046" stroke-width="2" stroke-dasharray="4 2"/>
    <text x="58" y="18" font-family="'Montserrat', sans-serif" font-size="9" font-weight="700" fill="#AD6046" text-anchor="middle" letter-spacing="1.5">CHITRASHALA</text>
    <text x="58" y="32" font-family="'Montserrat', sans-serif" font-size="8" fill="#33312F" text-anchor="middle">ESTD. 1878</text>
  </g>

  <rect width="640" height="400" filter="url(#cs_grain)"/>
</svg>'''

# 2. Tambat Ali (Kasba Peth) - Made by Hand (Coppersmithing)
SVGS["place-tambat.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 400" role="img" aria-label="Illustration of Tambat Ali workshop with hand-beaten copper bamba boiler, anvil, wooden mallet and glowing copper texture">
  <defs>
    <linearGradient id="ta_bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#F2E6D5"/>
      <stop offset="100%" stop-color="#E2D0B6"/>
    </linearGradient>
    <linearGradient id="ta_copper" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#8C4B36"/>
      <stop offset="35%" stop-color="#C87A54"/>
      <stop offset="70%" stop-color="#D98A62"/>
      <stop offset="100%" stop-color="#7A4030"/>
    </linearGradient>
    <linearGradient id="ta_brass" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#B8863A"/>
      <stop offset="50%" stop-color="#E3C36A"/>
      <stop offset="100%" stop-color="#9C6F2A"/>
    </linearGradient>
    <filter id="ta_grain">
      <feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="2" stitchTiles="stitch"/>
      <feColorMatrix type="matrix" values="0 0 0 0 0.2  0 0 0 0 0.19  0 0 0 0 0.18  0 0 0 0.05 0"/>
    </filter>
  </defs>
  <rect width="640" height="400" fill="url(#ta_bg)"/>

  <!-- Workshop backdrop: wooden timber posts and brickwork -->
  <rect x="30" y="20" width="24" height="380" fill="#7A4030" stroke="#33312F" stroke-width="2"/>
  <rect x="586" y="20" width="24" height="380" fill="#7A4030" stroke="#33312F" stroke-width="2"/>
  <line x1="30" y1="60" x2="610" y2="60" stroke="#33312F" stroke-width="5"/>
  <line x1="30" y1="75" x2="610" y2="75" stroke="#8C4B36" stroke-width="2"/>

  <!-- Hanging copper and brass tools / vessels in background -->
  <path d="M120 75 v45" stroke="#33312F" stroke-width="2"/>
  <circle cx="120" cy="135" r="18" fill="url(#ta_brass)" stroke="#33312F" stroke-width="2"/>
  <path d="M190 75 v60" stroke="#33312F" stroke-width="2"/>
  <ellipse cx="190" cy="150" rx="15" ry="20" fill="url(#ta_copper)" stroke="#33312F" stroke-width="2"/>

  <!-- Workshop stone floor -->
  <rect x="0" y="320" width="640" height="80" fill="#4A4744"/>
  <line x1="0" y1="320" x2="640" y2="320" stroke="#33312F" stroke-width="4"/>

  <!-- Tree trunk base anvil block (Kunda) -->
  <path d="M110 350 L125 210 L235 210 L250 350 Z" fill="#5E3E2F" stroke="#33312F" stroke-width="3"/>
  <!-- Cast iron anvil horn -->
  <path d="M100 210 L150 185 L225 185 L245 210 Z" fill="#33312F"/>
  <path d="M90 200 L115 192 L115 210 Z" fill="#667B82"/>

  <!-- Traditional Copper Bamba (Water Boiler with center flue) -->
  <g id="bamba">
    <!-- Base rim -->
    <ellipse cx="370" cy="320" rx="85" ry="22" fill="#7A4030" stroke="#33312F" stroke-width="3"/>
    <!-- Main cylindrical copper body -->
    <path d="M285 170 C285 130 455 130 455 170 L455 320 C455 335 285 335 285 320 Z" fill="url(#ta_copper)" stroke="#33312F" stroke-width="3.5"/>
    <!-- Mathar Kaam dimpled hand-beaten facets (pattern of hammer marks) -->
    <g fill="#F5C09B" opacity="0.6">
      <ellipse cx="320" cy="175" rx="5" ry="4"/><ellipse cx="340" cy="173" rx="5" ry="4"/><ellipse cx="360" cy="175" rx="5" ry="4"/><ellipse cx="380" cy="173" rx="5" ry="4"/><ellipse cx="400" cy="175" rx="5" ry="4"/><ellipse cx="420" cy="173" rx="5" ry="4"/>
      <ellipse cx="310" cy="200" rx="6" ry="4.5"/><ellipse cx="330" cy="198" rx="6" ry="4.5"/><ellipse cx="350" cy="200" rx="6" ry="4.5"/><ellipse cx="370" cy="198" rx="6" ry="4.5"/><ellipse cx="390" cy="200" rx="6" ry="4.5"/><ellipse cx="410" cy="198" rx="6" ry="4.5"/><ellipse cx="430" cy="200" rx="6" ry="4.5"/>
      <ellipse cx="315" cy="225" rx="6" ry="4.5"/><ellipse cx="335" cy="223" rx="6" ry="4.5"/><ellipse cx="355" cy="225" rx="6" ry="4.5"/><ellipse cx="375" cy="223" rx="6" ry="4.5"/><ellipse cx="395" cy="225" rx="6" ry="4.5"/><ellipse cx="415" cy="223" rx="6" ry="4.5"/>
      <ellipse cx="310" cy="250" rx="6" ry="4.5"/><ellipse cx="330" cy="248" rx="6" ry="4.5"/><ellipse cx="350" cy="250" rx="6" ry="4.5"/><ellipse cx="370" cy="248" rx="6" ry="4.5"/><ellipse cx="390" cy="250" rx="6" ry="4.5"/><ellipse cx="410" cy="248" rx="6" ry="4.5"/><ellipse cx="430" cy="250" rx="6" ry="4.5"/>
      <ellipse cx="320" cy="275" rx="5" ry="4"/><ellipse cx="340" cy="273" rx="5" ry="4"/><ellipse cx="360" cy="275" rx="5" ry="4"/><ellipse cx="380" cy="273" rx="5" ry="4"/><ellipse cx="400" cy="275" rx="5" ry="4"/><ellipse cx="420" cy="273" rx="5" ry="4"/>
      <ellipse cx="330" cy="298" rx="5" ry="4"/><ellipse cx="350" cy="296" rx="5" ry="4"/><ellipse cx="370" cy="298" rx="5" ry="4"/><ellipse cx="390" cy="296" rx="5" ry="4"/><ellipse cx="410" cy="298" rx="5" ry="4"/>
    </g>
    <!-- Central chimney / flue outlet -->
    <rect x="350" y="85" width="40" height="60" fill="#7A4030" stroke="#33312F" stroke-width="2.5"/>
    <ellipse cx="370" cy="85" rx="20" ry="7" fill="#33312F"/>
    <!-- Brass handles (Kadi) -->
    <path d="M285 220 C265 220 265 250 285 250" fill="none" stroke="url(#ta_brass)" stroke-width="7" stroke-linecap="round"/>
    <path d="M455 220 C475 220 475 250 455 250" fill="none" stroke="url(#ta_brass)" stroke-width="7" stroke-linecap="round"/>
    <!-- Brass water tap spigot -->
    <path d="M370 290 h35 v12 h-35 Z" fill="url(#ta_brass)" stroke="#33312F" stroke-width="1.5"/>
    <circle cx="400" cy="290" r="5" fill="url(#ta_brass)"/>
  </g>

  <!-- Traditional brass water pot (Ghagar) beside it -->
  <ellipse cx="510" cy="335" rx="50" ry="16" fill="#8A5A32"/>
  <circle cx="510" cy="285" r="42" fill="url(#ta_brass)" stroke="#33312F" stroke-width="3"/>
  <path d="M488 245 h44 l-4 -15 h-36 Z" fill="url(#ta_brass)" stroke="#33312F" stroke-width="2"/>

  <!-- Artisan shaping hammer / wooden mallet on anvil -->
  <g transform="rotate(22 210 200)">
    <rect x="180" y="192" width="90" height="10" rx="3" fill="#B8863A" stroke="#33312F" stroke-width="2"/>
    <rect x="160" y="180" width="28" height="34" rx="4" fill="#33312F" stroke="#AD6046" stroke-width="2"/>
  </g>

  <!-- Editorial craft badge -->
  <g transform="translate(60, 80)">
    <rect x="0" y="0" width="125" height="38" fill="#F9F6F0" stroke="#C87A54" stroke-width="2"/>
    <text x="62" y="16" font-family="'Montserrat', sans-serif" font-size="8.5" font-weight="700" fill="#AD6046" text-anchor="middle" letter-spacing="1">TAMBAT ALI</text>
    <text x="62" y="30" font-family="'Montserrat', sans-serif" font-size="7.5" fill="#33312F" text-anchor="middle">MATHAR KAAM CRAFT</text>
  </g>

  <rect width="640" height="400" filter="url(#ta_grain)"/>
</svg>'''

# 3. Mahatma Phule Mandai (Shukrawar Peth) - Market Life
SVGS["place-mandai.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 400" role="img" aria-label="Illustration of Mahatma Phule Mandai historic market with central octagonal basalt gothic tower, timber roof wings and market produce baskets">
  <defs>
    <linearGradient id="mp_bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#EFE3D0"/>
      <stop offset="100%" stop-color="#E2D0B8"/>
    </linearGradient>
    <linearGradient id="mp_basalt" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#4A4744"/>
      <stop offset="50%" stop-color="#605C57"/>
      <stop offset="100%" stop-color="#3A3836"/>
    </linearGradient>
    <filter id="mp_grain">
      <feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="2" stitchTiles="stitch"/>
      <feColorMatrix type="matrix" values="0 0 0 0 0.2  0 0 0 0 0.19  0 0 0 0 0.18  0 0 0 0.05 0"/>
    </filter>
  </defs>
  <rect width="640" height="400" fill="url(#mp_bg)"/>

  <!-- Morning market sky glow -->
  <circle cx="320" cy="140" r="130" fill="#F6D8A8" opacity="0.35"/>

  <!-- Mahatma Phule Mandai central gothic basalt tower (80-ft tower, opened 1886) -->
  <!-- Tower base and central body -->
  <rect x="260" y="110" width="120" height="170" fill="url(#mp_basalt)" stroke="#33312F" stroke-width="3"/>
  <!-- Stone masonry coursing -->
  <g stroke="#33312F" stroke-width="1" opacity="0.5">
    <line x1="260" y1="135" x2="380" y2="135"/><line x1="260" y1="160" x2="380" y2="160"/>
    <line x1="260" y1="185" x2="380" y2="185"/><line x1="260" y1="210" x2="380" y2="210"/>
    <line x1="260" y1="235" x2="380" y2="235"/><line x1="260" y1="260" x2="380" y2="260"/>
  </g>

  <!-- Belfry Gothic Arched Windows in octagonal tower -->
  <path d="M285 180 A12 18 0 0 1 315 180 V210 H285 Z" fill="#33312F"/>
  <path d="M325 180 A12 18 0 0 1 355 180 V210 H325 Z" fill="#33312F"/>
  <!-- Louvers inside gothic arches -->
  <g stroke="#F2E6D5" stroke-width="1.5">
    <line x1="288" y1="188" x2="312" y2="188"/><line x1="288" y1="195" x2="312" y2="195"/><line x1="288" y1="202" x2="312" y2="202"/>
    <line x1="328" y1="188" x2="352" y2="188"/><line x1="328" y1="195" x2="352" y2="195"/><line x1="328" y1="202" x2="352" y2="202"/>
  </g>

  <!-- Clock face on tower -->
  <circle cx="320" cy="140" r="18" fill="#F9F6F0" stroke="#33312F" stroke-width="2.5"/>
  <circle cx="320" cy="140" r="15" fill="none" stroke="#AD6046" stroke-width="1"/>
  <line x1="320" y1="140" x2="320" y2="130" stroke="#33312F" stroke-width="2"/>
  <line x1="320" y1="140" x2="328" y2="140" stroke="#33312F" stroke-width="1.5"/>

  <!-- Steep Gothic Spire / Steeple roof -->
  <path d="M250 110 L320 25 L390 110 Z" fill="#AD6046" stroke="#33312F" stroke-width="3"/>
  <line x1="320" y1="25" x2="320" y2="10" stroke="#33312F" stroke-width="3"/>
  <!-- Weather vane / finial -->
  <path d="M312 10 H328 M320 5 V15 M322 8 L328 10 L322 12 Z" stroke="#C87A54" stroke-width="2" fill="none"/>

  <!-- Radiating Market Wings (Left & Right tiled pitched roofs) -->
  <path d="M40 210 L260 170 V280 L40 280 Z" fill="#8C4B36" stroke="#33312F" stroke-width="3"/>
  <path d="M380 170 L600 210 V280 L380 280 Z" fill="#8C4B36" stroke="#33312F" stroke-width="3"/>
  <!-- Clerestory louvers along market wings -->
  <g fill="#F2E6D5" stroke="#33312F" stroke-width="1.5">
    <rect x="70" y="225" width="25" height="35"/><rect x="115" y="220" width="25" height="35"/>
    <rect x="160" y="215" width="25" height="35"/><rect x="205" y="210" width="25" height="35"/>
    <rect x="410" y="210" width="25" height="35"/><rect x="455" y="215" width="25" height="35"/>
    <rect x="500" y="220" width="25" height="35"/><rect x="545" y="225" width="25" height="35"/>
  </g>

  <!-- Market street level stone platform -->
  <rect x="0" y="280" width="640" height="120" fill="#E8D9C0" stroke="#33312F" stroke-width="3"/>

  <!-- Wholesale market stalls, crates and vegetable baskets (Topli) -->
  <!-- Stacking fruit crates -->
  <rect x="60" y="310" width="70" height="25" fill="#C89B62" stroke="#5E3E2F" stroke-width="2"/>
  <rect x="65" y="290" width="60" height="22" fill="#D8A86C" stroke="#5E3E2F" stroke-width="2"/>
  <!-- Produce basket 1 (Marigold & lemons) -->
  <ellipse cx="200" cy="345" rx="42" ry="18" fill="#AD6046" stroke="#33312F" stroke-width="2"/>
  <circle cx="190" cy="335" r="9" fill="#E3B25C"/><circle cx="210" cy="336" r="8" fill="#AD6046"/><circle cx="200" cy="330" r="8" fill="#E3B25C"/>
  <!-- Produce basket 2 (Fresh greens) -->
  <ellipse cx="320" cy="350" rx="55" ry="22" fill="#8C4B36" stroke="#33312F" stroke-width="2.5"/>
  <path d="M280 345 C300 320 340 320 360 345 Z" fill="#37452C"/>
  <!-- Produce basket 3 (Onions / Spices) -->
  <ellipse cx="440" cy="345" rx="44" ry="19" fill="#AD6046" stroke="#33312F" stroke-width="2"/>
  <circle cx="430" cy="335" r="8" fill="#C87A54"/><circle cx="450" cy="334" r="8" fill="#F2E6D5"/><circle cx="440" cy="328" r="8" fill="#C87A54"/>
  <!-- Crate Right -->
  <rect x="510" y="305" width="75" height="26" fill="#C89B62" stroke="#5E3E2F" stroke-width="2"/>

  <!-- Editorial sign badge -->
  <g transform="translate(60, 60)">
    <rect x="0" y="0" width="135" height="38" fill="#F9F6F0" stroke="#33312F" stroke-width="2"/>
    <text x="67" y="16" font-family="'Montserrat', sans-serif" font-size="8" font-weight="700" fill="#33312F" text-anchor="middle" letter-spacing="1">PHULE MANDAI</text>
    <text x="67" y="30" font-family="'Montserrat', sans-serif" font-size="7.5" fill="#AD6046" text-anchor="middle">OCTAGONAL GOTHIC TOWER</text>
  </g>

  <rect width="640" height="400" filter="url(#mp_grain)"/>
</svg>'''

# 4. Vaidya Upahar Gruha (Budhwar Peth) - Everyday Food Culture (Peth Group)
SVGS["place-vaidya.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 400" role="img" aria-label="Illustration of Vaidya Upahar Gruha historic breakfast counter with bowl of green chilli misal, pav, sprouted beans and vintage wooden booth">
  <defs>
    <linearGradient id="vy_bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#F7EEDF"/>
      <stop offset="100%" stop-color="#EADBCE"/>
    </linearGradient>
    <filter id="vy_grain">
      <feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="2" stitchTiles="stitch"/>
      <feColorMatrix type="matrix" values="0 0 0 0 0.2  0 0 0 0 0.19  0 0 0 0 0.18  0 0 0 0.05 0"/>
    </filter>
  </defs>
  <rect width="640" height="400" fill="url(#vy_bg)"/>

  <!-- Century-old Peth Upahar Gruha wooden booth paneling -->
  <rect x="40" y="20" width="560" height="150" fill="#E3D3BD" stroke="#33312F" stroke-width="3"/>
  <g stroke="#8C4B36" stroke-width="2">
    <line x1="140" y1="20" x2="140" y2="170"/><line x1="240" y1="20" x2="240" y2="170"/>
    <line x1="400" y1="20" x2="400" y2="170"/><line x1="500" y1="20" x2="500" y2="170"/>
    <rect x="60" y="35" width="60" height="115" fill="none"/>
    <rect x="160" y="35" width="60" height="115" fill="none"/>
    <rect x="420" y="35" width="60" height="115" fill="none"/>
    <rect x="520" y="35" width="60" height="115" fill="none"/>
  </g>

  <!-- Vintage Slate menu board on the wall -->
  <rect x="255" y="35" width="130" height="85" fill="#33312F" stroke="#AD6046" stroke-width="2.5"/>
  <text x="320" y="58" font-family="'Playfair Display', serif" font-size="13" font-weight="700" fill="#F2E6D5" text-anchor="middle">वैद्य उपहार गृह</text>
  <text x="320" y="76" font-family="'Montserrat', sans-serif" font-size="8.5" fill="#E3B25C" text-anchor="middle">BUDHWAR PETH · 1910</text>
  <text x="320" y="96" font-family="'Montserrat', sans-serif" font-size="10" font-weight="600" fill="#F9F6F0" text-anchor="middle">हिरवी मिसळ</text>
  <line x1="275" y1="104" x2="365" y2="104" stroke="#667B82" stroke-width="1"/>

  <!-- Dining table surface -->
  <rect x="0" y="170" width="640" height="230" fill="#F2E6D5" stroke="#33312F" stroke-width="3"/>
  <line x1="0" y1="170" x2="640" y2="170" stroke="#7A4030" stroke-width="6"/>

  <!-- Centerpiece: Famous Green-Chilli Misal (Hirvi Misal) Bowl -->
  <!-- Steel plate / katori underliner -->
  <ellipse cx="280" cy="305" rx="125" ry="58" fill="#E8D9C0" stroke="#33312F" stroke-width="3"/>
  <ellipse cx="280" cy="298" rx="115" ry="52" fill="#F9F6F0" stroke="#AD6046" stroke-width="2"/>

  <!-- The Misal Bowl -->
  <ellipse cx="280" cy="285" rx="88" ry="42" fill="#FFFFFF" stroke="#33312F" stroke-width="3"/>
  <!-- Iconic green spiced gravy (Hirva rassa) -->
  <ellipse cx="280" cy="282" rx="80" ry="36" fill="#3D5A2E"/>
  <!-- Sprouted moth beans and potato base -->
  <ellipse cx="280" cy="280" rx="66" ry="28" fill="#4E6E38"/>
  <!-- Golden crisp farsan / sev top layer -->
  <ellipse cx="280" cy="275" rx="55" ry="22" fill="#E3B25C"/>
  <g fill="#D49A38">
    <circle cx="265" cy="273" r="3"/><circle cx="285" cy="270" r="3"/><circle cx="295" cy="274" r="3"/><circle cx="275" cy="278" r="3"/>
  </g>
  <!-- Finely chopped onions, fresh coriander garnish & green chilli slice -->
  <g fill="#F9F6F0">
    <circle cx="260" cy="272" r="2.5"/><circle cx="270" cy="268" r="2.5"/><circle cx="290" cy="271" r="2.5"/><circle cx="300" cy="275" r="2.5"/>
  </g>
  <path d="M282 267 C288 262 292 265 296 268" stroke="#25421A" stroke-width="3" fill="none"/>
  <!-- Lemon wedge on rim -->
  <path d="M205 280 A12 12 0 0 1 222 268 Z" fill="#E3C36A" stroke="#33312F" stroke-width="1.5"/>

  <!-- Traditional ladi pav pair on butter paper -->
  <g transform="translate(420, 240)">
    <polygon points="0,40 160,10 170,85 10,115" fill="#F9F6F0" stroke="#33312F" stroke-width="1.5"/>
    <!-- Two pav buns -->
    <rect x="25" y="35" width="55" height="52" rx="14" fill="#C89B62" stroke="#5E3E2F" stroke-width="2.5"/>
    <rect x="85" y="32" width="55" height="52" rx="14" fill="#C89B62" stroke="#5E3E2F" stroke-width="2.5"/>
    <line x1="80" y1="38" x2="80" y2="84" stroke="#8C4B36" stroke-width="2"/>
  </g>

  <!-- Brass cutting chai glass / water tumbler -->
  <path d="M90 230 L98 320 L135 320 L143 230 Z" fill="#D89B54" stroke="#33312F" stroke-width="2.5"/>
  <ellipse cx="116.5" cy="230" rx="26.5" ry="8" fill="#F2E6D5" stroke="#33312F" stroke-width="2"/>

  <!-- Editorial location badge -->
  <g transform="translate(60, 45)">
    <rect x="0" y="0" width="135" height="38" fill="#F9F6F0" stroke="#37452C" stroke-width="2"/>
    <text x="67" y="16" font-family="'Montserrat', sans-serif" font-size="8" font-weight="700" fill="#37452C" text-anchor="middle" letter-spacing="1">HISTORIC PETH</text>
    <text x="67" y="30" font-family="'Montserrat', sans-serif" font-size="7.5" fill="#33312F" text-anchor="middle">BUDHWAR PETH · MISAL</text>
  </g>

  <rect width="640" height="400" filter="url(#vy_grain)"/>
</svg>'''

# 5. Marz-o-rin (Pune Camp / MG Road) - Everyday Food Culture (Camp Group)
SVGS["place-marzorin.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 400" role="img" aria-label="Illustration of Marz-o-rin heritage cafe on MG Road with colonial wooden balcony, chutney sandwich and tall cold coffee glass">
  <defs>
    <linearGradient id="mr_bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#F2EAE0"/>
      <stop offset="100%" stop-color="#E2D4C3"/>
    </linearGradient>
    <filter id="mr_grain">
      <feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="2" stitchTiles="stitch"/>
      <feColorMatrix type="matrix" values="0 0 0 0 0.2  0 0 0 0 0.19  0 0 0 0 0.18  0 0 0 0.05 0"/>
    </filter>
  </defs>
  <rect width="640" height="400" fill="url(#mr_bg)"/>

  <!-- Colonial heritage building facade (MG Road 100+ year old structure) -->
  <rect x="50" y="20" width="540" height="150" fill="#F9F6F0" stroke="#33312F" stroke-width="3"/>
  <!-- Striped canvas awning -->
  <g stroke="#33312F" stroke-width="2">
    <path d="M40 70 L50 40 H590 L600 70 Z" fill="#AD6046"/>
    <!-- Awning stripes -->
    <polygon points="80,70 90,40 120,40 110,70" fill="#F2E6D5"/>
    <polygon points="150,70 160,40 190,40 180,70" fill="#F2E6D5"/>
    <polygon points="220,70 230,40 260,40 250,70" fill="#F2E6D5"/>
    <polygon points="290,70 300,40 330,40 320,70" fill="#F2E6D5"/>
    <polygon points="360,70 370,40 400,40 390,70" fill="#F2E6D5"/>
    <polygon points="430,70 440,40 470,40 460,70" fill="#F2E6D5"/>
    <polygon points="500,70 510,40 540,40 530,70" fill="#F2E6D5"/>
  </g>

  <!-- Ornate wooden balcony balustrade -->
  <rect x="60" y="100" width="520" height="60" fill="#E8D9C0" stroke="#33312F" stroke-width="2"/>
  <line x1="60" y1="120" x2="580" y2="120" stroke="#8C4B36" stroke-width="3"/>
  <!-- Balcony railing spindles -->
  <g stroke="#33312F" stroke-width="2">
    <line x1="90" y1="100" x2="90" y2="160"/><line x1="130" y1="100" x2="130" y2="160"/>
    <line x1="170" y1="100" x2="170" y2="160"/><line x1="210" y1="100" x2="210" y2="160"/>
    <line x1="250" y1="100" x2="250" y2="160"/><line x1="290" y1="100" x2="290" y2="160"/>
    <line x1="330" y1="100" x2="330" y2="160"/><line x1="370" y1="100" x2="370" y2="160"/>
    <line x1="410" y1="100" x2="410" y2="160"/><line x1="450" y1="100" x2="450" y2="160"/>
    <line x1="490" y1="100" x2="490" y2="160"/><line x1="530" y1="100" x2="530" y2="160"/>
  </g>

  <!-- Cafe tabletop foreground -->
  <rect x="0" y="200" width="640" height="200" fill="#667B82" stroke="#33312F" stroke-width="3"/>
  <rect x="20" y="208" width="600" height="184" fill="#758B92"/>

  <!-- Famous Marz-o-rin Green Chutney Sandwiches (triangular cut white bread) -->
  <g transform="translate(130, 230)">
    <!-- Serving plate -->
    <ellipse cx="110" cy="95" rx="95" ry="42" fill="#F9F6F0" stroke="#33312F" stroke-width="2.5"/>
    <ellipse cx="110" cy="92" rx="85" ry="36" fill="#F2E6D5" stroke="#AD6046" stroke-width="1.5"/>
    <!-- Triangle sandwich 1 -->
    <polygon points="50,105 130,55 125,115" fill="#FFFFFF" stroke="#33312F" stroke-width="2"/>
    <path d="M50 105 L130 55" stroke="#4E7037" stroke-width="4.5"/> <!-- Green chutney layer -->
    <!-- Triangle sandwich 2 -->
    <polygon points="90,115 170,65 165,120" fill="#FFFFFF" stroke="#33312F" stroke-width="2"/>
    <path d="M90 115 L170 65" stroke="#4E7037" stroke-width="4.5"/>
  </g>

  <!-- Tall glass of cold coffee with froth and paper straw -->
  <g transform="translate(410, 210)">
    <!-- Glass shadow -->
    <ellipse cx="45" cy="155" rx="36" ry="12" fill="#4F6169"/>
    <!-- Glass body -->
    <path d="M20 30 L30 150 C30 156 60 156 60 150 L70 30 Z" fill="#7A5636" stroke="#33312F" stroke-width="2.5"/>
    <!-- Froth on top -->
    <ellipse cx="45" cy="30" rx="25" ry="9" fill="#EEDAC0" stroke="#33312F" stroke-width="2"/>
    <!-- Straw -->
    <line x1="45" y1="30" x2="62" y2="-15" stroke="#AD6046" stroke-width="4" stroke-linecap="round"/>
  </g>

  <!-- Non-Peth Camp Geographic Notice Badge -->
  <g transform="translate(60, 20)">
    <rect x="0" y="0" width="165" height="36" fill="#F9F6F0" stroke="#667B82" stroke-width="2"/>
    <text x="82" y="15" font-family="'Montserrat', sans-serif" font-size="8" font-weight="700" fill="#4F6169" text-anchor="middle" letter-spacing="1">PUNE CAMP · MG ROAD</text>
    <text x="82" y="28" font-family="'Montserrat', sans-serif" font-size="7" fill="#AD6046" text-anchor="middle">NON-PETH CREATIVE REF.</text>
  </g>

  <rect width="640" height="400" filter="url(#mr_grain)"/>
</svg>'''

# 6. Kayani Bakery (Pune Camp / East Street) - Everyday Food Culture (Camp Group)
SVGS["place-kayani.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 400" role="img" aria-label="Illustration of Kayani Bakery on East Street with wire trays of fluted Shrewsbury biscuits, mawa cake and bakery counter">
  <defs>
    <linearGradient id="kb_bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#F5EFE6"/>
      <stop offset="100%" stop-color="#E8DCCC"/>
    </linearGradient>
    <filter id="kb_grain">
      <feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="2" stitchTiles="stitch"/>
      <feColorMatrix type="matrix" values="0 0 0 0 0.2  0 0 0 0 0.19  0 0 0 0 0.18  0 0 0 0.05 0"/>
    </filter>
  </defs>
  <rect width="640" height="400" fill="url(#kb_bg)"/>

  <!-- Bakery shopfront panel & clock (East Street 1955) -->
  <rect x="40" y="20" width="560" height="140" fill="#AD6046" stroke="#33312F" stroke-width="3"/>
  <rect x="60" y="35" width="520" height="35" fill="#33312F"/>
  <text x="320" y="58" font-family="'Playfair Display', Georgia, serif" font-size="19" font-weight="700" fill="#F2E6D5" text-anchor="middle" letter-spacing="2">KAYANI BAKERY</text>
  <text x="320" y="95" font-family="'Montserrat', sans-serif" font-size="9" font-weight="600" fill="#F9F6F0" text-anchor="middle" letter-spacing="1.5">EAST STREET · ESTD. 1955</text>

  <!-- Bakery glass display vitrine counter -->
  <rect x="0" y="160" width="640" height="240" fill="#33312F"/>
  <rect x="30" y="175" width="580" height="205" fill="#F9F6F0" stroke="#8C4B36" stroke-width="3"/>

  <!-- Stainless wire cooling tray with famous Shrewsbury Biscuits -->
  <rect x="50" y="200" width="340" height="160" fill="#E8D9C0" stroke="#33312F" stroke-width="2.5"/>
  <!-- Wire grid lines -->
  <g stroke="#B8A48B" stroke-width="1">
    <line x1="50" y1="230" x2="390" y2="230"/><line x1="50" y1="260" x2="390" y2="260"/>
    <line x1="50" y1="290" x2="390" y2="290"/><line x1="50" y1="320" x2="390" y2="320"/>
  </g>

  <!-- Array of round, fluted Shrewsbury butter biscuits with stamped center -->
  <g fill="#E3B25C" stroke="#8C4B36" stroke-width="2">
    <!-- Row 1 -->
    <circle cx="100" cy="235" r="22"/><circle cx="165" cy="235" r="22"/><circle cx="230" cy="235" r="22"/><circle cx="295" cy="235" r="22"/><circle cx="355" cy="235" r="22"/>
    <!-- Row 2 -->
    <circle cx="100" cy="285" r="22"/><circle cx="165" cy="285" r="22"/><circle cx="230" cy="285" r="22"/><circle cx="295" cy="285" r="22"/><circle cx="355" cy="285" r="22"/>
    <!-- Row 3 -->
    <circle cx="100" cy="335" r="20"/><circle cx="165" cy="335" r="20"/><circle cx="230" cy="335" r="20"/><circle cx="295" cy="335" r="20"/><circle cx="355" cy="335" r="20"/>
  </g>
  <!-- Biscuit center indents / butter pricks -->
  <g fill="#A66F28">
    <circle cx="100" cy="235" r="4"/><circle cx="165" cy="235" r="4"/><circle cx="230" cy="235" r="4"/><circle cx="295" cy="235" r="4"/><circle cx="355" cy="235" r="4"/>
    <circle cx="100" cy="285" r="4"/><circle cx="165" cy="285" r="4"/><circle cx="230" cy="285" r="4"/><circle cx="295" cy="285" r="4"/><circle cx="355" cy="285" r="4"/>
  </g>

  <!-- Loaf of Mawa Cake & signature bakery box -->
  <!-- Mawa Cake round loaf -->
  <g transform="translate(420, 200)">
    <ellipse cx="75" cy="65" rx="55" ry="24" fill="#C87A54" stroke="#33312F" stroke-width="2.5"/>
    <path d="M20 65 L20 100 C20 120 130 120 130 100 L130 65 Z" fill="#B0653B" stroke="#33312F" stroke-width="2.5"/>
    <!-- Cardamom and almond slivers on cake -->
    <circle cx="65" cy="60" r="3" fill="#F2E6D5"/><circle cx="85" cy="62" r="3" fill="#F2E6D5"/><circle cx="75" cy="70" r="3" fill="#F2E6D5"/>
    <text x="75" y="145" font-family="'Montserrat', sans-serif" font-size="9" font-weight="600" fill="#33312F" text-anchor="middle">MAWA CAKE</text>
  </g>

  <!-- Non-Peth Camp Geographic Notice Badge -->
  <g transform="translate(60, 20)">
    <rect x="0" y="0" width="165" height="34" fill="#F9F6F0" stroke="#AD6046" stroke-width="2"/>
    <text x="82" y="14" font-family="'Montserrat', sans-serif" font-size="8" font-weight="700" fill="#AD6046" text-anchor="middle" letter-spacing="1">PUNE CAMP · EAST STREET</text>
    <text x="82" y="27" font-family="'Montserrat', sans-serif" font-size="7" fill="#33312F" text-anchor="middle">NON-PETH CREATIVE REF.</text>
  </g>

  <rect width="640" height="400" filter="url(#kb_grain)"/>
</svg>'''

# 7. Garden Vada Pav (Pune Camp / JJ Garden) - Everyday Food Culture (Camp Group)
SVGS["place-garden-vadapav.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 400" role="img" aria-label="Illustration of Garden Vada Pav street food counter near JJ Garden with hot kadhai, golden crisp batata vada, signature green chutney bowl and fried chillies">
  <defs>
    <linearGradient id="gv_bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#F6EFE5"/>
      <stop offset="100%" stop-color="#E8DCCC"/>
    </linearGradient>
    <linearGradient id="gv_oil" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#D89B54"/>
      <stop offset="100%" stop-color="#B87B2E"/>
    </linearGradient>
    <filter id="gv_grain">
      <feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="2" stitchTiles="stitch"/>
      <feColorMatrix type="matrix" values="0 0 0 0 0.2  0 0 0 0 0.19  0 0 0 0 0.18  0 0 0 0.05 0"/>
    </filter>
  </defs>
  <rect width="640" height="400" fill="url(#gv_bg)"/>

  <!-- Street counter background near Cantonment JJ Garden -->
  <rect x="0" y="0" width="640" height="180" fill="#E8D9C0"/>
  <rect x="40" y="20" width="560" height="70" fill="#AD6046" stroke="#33312F" stroke-width="3"/>
  <text x="320" y="52" font-family="'Playfair Display', Georgia, serif" font-size="20" font-weight="700" fill="#F9F6F0" text-anchor="middle">GARDEN VADA PAV</text>
  <text x="320" y="74" font-family="'Montserrat', sans-serif" font-size="9" font-weight="600" fill="#F2E6D5" text-anchor="middle" letter-spacing="1.5">JJ GARDEN, CAMP · ESTD. 1972</text>

  <!-- Heavy steel street frying counter -->
  <rect x="0" y="160" width="640" height="240" fill="#4A4744" stroke="#33312F" stroke-width="3"/>
  <line x1="0" y1="160" x2="640" y2="160" stroke="#7A4030" stroke-width="5"/>

  <!-- Large heavy cast-iron kadhai on left -->
  <g transform="translate(130, 230)">
    <!-- Gas flame base hint -->
    <ellipse cx="90" cy="115" rx="75" ry="15" fill="#33312F"/>
    <!-- Iron Kadhai body -->
    <path d="M10 40 C10 120 170 120 170 40 Z" fill="#33312F" stroke="#1A1918" stroke-width="4"/>
    <!-- Kadhai handles -->
    <circle cx="5" cy="40" r="10" fill="none" stroke="#667B82" stroke-width="3.5"/>
    <circle cx="175" cy="40" r="10" fill="none" stroke="#667B82" stroke-width="3.5"/>
    <!-- Simmering oil -->
    <ellipse cx="90" cy="50" rx="70" ry="24" fill="url(#gv_oil)"/>
    <!-- Vadas frying in oil -->
    <circle cx="65" cy="52" r="15" fill="#E3B25C" stroke="#A86F24" stroke-width="2"/>
    <circle cx="105" cy="48" r="16" fill="#E3B25C" stroke="#A86F24" stroke-width="2"/>
    <circle cx="85" cy="60" r="14" fill="#E3B25C" stroke="#A86F24" stroke-width="2"/>
  </g>

  <!-- Foreground: The iconic large Garden Vada Pav served fresh -->
  <g transform="translate(340, 200)">
    <!-- Stainless steel tray -->
    <ellipse cx="120" cy="120" rx="120" ry="50" fill="#F9F6F0" stroke="#33312F" stroke-width="3"/>
    <ellipse cx="120" cy="116" rx="108" ry="44" fill="#E8D9C0" stroke="#667B82" stroke-width="1.5"/>

    <!-- Soft butter-fluffy Pav bun sliced open -->
    <rect x="50" y="80" width="75" height="55" rx="18" fill="#C89B62" stroke="#5E3E2F" stroke-width="3"/>

    <!-- Oversized golden crispy Batata Vada nestled in pav -->
    <circle cx="88" cy="98" r="30" fill="#E3B25C" stroke="#8C4B36" stroke-width="3"/>
    <!-- Crispy besan droplets (chura) -->
    <circle cx="65" cy="125" r="4" fill="#C87A54"/><circle cx="75" cy="130" r="3" fill="#C87A54"/><circle cx="115" cy="126" r="4" fill="#C87A54"/>

    <!-- Iconic Signature Green Chutney Bowl (coriander, mint, spicy chillies) -->
    <ellipse cx="175" cy="105" rx="42" ry="24" fill="#33312F" stroke="#1A1918" stroke-width="2.5"/>
    <ellipse cx="175" cy="102" rx="36" ry="19" fill="#3D6E2E"/>
    <ellipse cx="175" cy="100" rx="26" ry="13" fill="#4E8A38"/>

    <!-- Fried salted green chillies on the side -->
    <path d="M125 140 C145 130 165 148 185 138" fill="none" stroke="#37452C" stroke-width="4.5" stroke-linecap="round"/>
    <path d="M135 148 C155 138 175 156 195 146" fill="none" stroke="#4A5B3D" stroke-width="4" stroke-linecap="round"/>
  </g>

  <!-- Non-Peth Camp Geographic Notice Badge -->
  <g transform="translate(60, 20)">
    <rect x="0" y="0" width="165" height="34" fill="#F9F6F0" stroke="#AD6046" stroke-width="2"/>
    <text x="82" y="14" font-family="'Montserrat', sans-serif" font-size="8" font-weight="700" fill="#AD6046" text-anchor="middle" letter-spacing="1">PUNE CAMP · JJ GARDEN</text>
    <text x="82" y="27" font-family="'Montserrat', sans-serif" font-size="7" fill="#33312F" text-anchor="middle">NON-PETH CREATIVE REF.</text>
  </g>

  <rect width="640" height="400" filter="url(#gv_grain)"/>
</svg>'''

for filename, content in SVGS.items():
    path = OUT_DIR / filename
    path.write_text(content.strip(), encoding="utf-8")
    print(f"Written: {path}")

print("All 7 place SVGs generated successfully.")
