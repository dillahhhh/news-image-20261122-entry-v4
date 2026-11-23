# stories.py — 36 stories, all dated Sunday 22 November 2026.
# Written fresh for the v4 entry from web research done in this session.
# Every story carries: region, headline, body, source, confidence.
# Region bodies are kept to one newspaper line each.

LEADS = [
    {
        "kicker": "WAR IN UKRAINE  ·  LEAD",
        "headline": "186 DRONES IN ONE NIGHT — 161 SHOT DOWN",
        "body": ("Russia launched 186 Shahed, Gerbera and decoy drones at Ukraine "
                 "overnight, 72 of them jet-powered. Air defences shot down or "
                 "jammed 161, but hits were recorded at 18 sites. In Dymer, "
                 "north of Kyiv, a drone smashed into a five-storey block at "
                 "about 05:00, collapsing the stairwell. Three people were "
                 "killed and a boy was pulled alive from the rubble."),
        "source": "Ukraine Air Force · Reuters · AFP",
        "confidence": "CONFIRMED",
    },
    {
        "kicker": "CLIMATE  ·  COP31, ANTALYA",
        "headline": "COP31 ENDS WITH NO DEAL",
        "body": ("Climate talks in Antalya collapsed on Sunday after the EU and "
                 "more than 130 countries rejected a final text with no mention "
                 "of fossil fuels. The 10-page draft dropped a $120bn adaptation "
                 "target and set only a 35% electrification goal for 2035. "
                 "President Murat Kurum closed the session without consensus, "
                 "leaving the Antalya Pact unadopted."),
        "source": "Reuters · AP",
        "confidence": "CONFIRMED",
    },
    {
        "kicker": "MIDDLE EAST  ·  CLAIM",
        "headline": "IRAN CLAIMS IT HIT TWO U.S. PATRIOT RADARS",
        "body": ("Iran's Revolutionary Guard said it struck two U.S. Patriot radar "
                 "sites at Al-Riffa and Awali bases in Bahrain overnight, in "
                 "retaliation for alleged U.S. drone violations of Iranian "
                 "airspace. Bahrain said a civilian industrial facility was hit "
                 "and two people were hurt — and a U.S. official said no American "
                 "personnel or facilities were damaged."),
        "source": "IRGC · Reuters · AP",
        "confidence": "CLAIM",
    },
]

REGIONS = [
    {
        "name": "EUROPE",
        "count": 10,
        "color": (180, 35, 24),
        "items": [
            ("SUPERMARKET HIT IN VYSHNEVE",
             "A Shahed hit a Novus supermarket in the evening, killing 3 and wounding 15, incl. 3 children.",
             "Mayor Illya Dikov", "CONFIRMED", "drone"),
            ("ONE KILLED IN BILA TSERKVA",
             "A drone strike set a private home ablaze, killing one person.",
             "SES Ukraine", "CONFIRMED", "fire"),
            ("ODESA GRID \u201cCANNOT DELIVER POWER\u201d",
             "Ukrenergo: damaged lines make it \u201cphysically impossible\u201d to supply the power Odesa needs.",
             "Ukrenergo", "CONFIRMED", "bolt"),
            ("SPARTA II STILL BURNING",
             "The Russian cargo ship hit on Saturday was still smouldering as towing began; 16 crew evacuated.",
             "Finland", "CONFIRMED", "ship"),
            ("GEORGIA MOURNS SIX DEAD",
             "A day of mourning for the six, incl. two children, killed in Wednesday's Ponichala gas blast.",
             "Govt of Georgia", "CONFIRMED", "candle"),
            ("FRANCE PROTESTS FOR SIXTH WEEKEND",
             "Tens of thousands marched over living costs and police protections — the sixth weekend.",
             "AFP", "REPORTED", "march"),
            ("BELGIUM WARNS OF FLIGHT CHAOS",
             "Belgium warned of cancellations as air-traffic controllers prepared to strike.",
             "Reuters", "REPORTED", "plane"),
            ("MOLDOVA: JET DRONE CROSSED TWICE",
             "Moldova said a Russian jet drone crossed its airspace twice on Saturday.",
             "Govt of Moldova", "REPORTED", "drone"),
            ("ZELENSKYY DEFENDS BRIDGE STRIKES",
             "Ukraine's president defended strikes on the Crimean Bridge as attacks on cities went on.",
             "AP", "REPORTED", "bridge"),
        ],
    },
    {
        "name": "MIDDLE EAST & AFRICA",
        "count": 6,
        "color": (194, 65, 12),
        "items": [
            ("IRAN BLACKOUTS BEGIN",
             "Rolling cuts of up to two hours a day began after war damage cut gas output.",
             "Tavanir", "CONFIRMED", "bolt"),
            ("KHARTOUM DRONES KILL FOUR",
             "Drones struck before dawn, killing four and damaging a UN building with staff inside.",
             "UN · AFP", "CONFIRMED", "drone"),
            ("TRUMP DARES IRAN ON HORMUZ",
             "Trump told Fox News Iranian ships testing the blockade would end up \u201cat the bottom of the sea\u201d.",
             "Fox News", "CONFIRMED", "ship"),
            ("IRAN SHOWS DOUBLE LAUNCHER",
             "Iran unveiled an underground system able to fire two liquid-fuelled missiles at once.",
             "IRGC", "REPORTED", "rocket"),
            ("GAZA AID TRUCK HIT, THREE DEAD",
             "An Israeli strike hit a truck witnesses said carried World Central Kitchen aid, killing three.",
             "Witnesses", "REPORTED", "truck"),
        ],
    },
    {
        "name": "ASIA-PACIFIC",
        "count": 5,
        "color": (14, 116, 144),
        "items": [
            ("HONG KONG VOTES",
             "Hong Kong chose its Election Committee: 856 candidates, 723 seats, 98.79% turnout.",
             "Govt of Hong Kong", "CONFIRMED", "vote"),
            ("CIKANDE FIRE: 3 DEAD, 36 MISSING",
             "Rescuers searched the Milkita factory ruins; at least 3 dead, about 36 missing.",
             "Police", "CONFIRMED", "fire"),
            ("SEOUL MOVES TO IMPEACH CHIEF JUSTICE",
             "The ruling party set out grounds to impeach Chief Justice Cho Hee-dae.",
             "JoongAng Daily", "REPORTED", "court"),
            ("JAPAN TOBACCO FACES RECORD LOSS",
             "Japan Tobacco expects a record \u00a5724bn net loss after losing its Russian units.",
             "Jiji Press", "REPORTED", "money"),
            ("GOLDEN HORSE GOES TO ANGELA YUEN",
             "Angela Yuen won best leading actress at Taiwan's Golden Horse Awards for \u201cAfterpiece\u201d.",
             "CNA", "CONFIRMED", "trophy"),
        ],
    },
    {
        "name": "AMERICAS",
        "count": 7,
        "color": (29, 78, 216),
        "items": [
            ("BOLSONARO STABLE IN ICU",
             "The ex-president remained stable and conscious in intensive care, three days after admission.",
             "Hospital", "CONFIRMED", "health"),
            ("FBI PROBES CRIME DATABASE HACK",
             "The FBI is probing a breach of its national crime database — its second hacked system in two months.",
             "CNN · AP", "REPORTED", "hack"),
            ("BRAZIL STORM TOLL RISES TO FIVE",
             "The toll from Friday's supercell rose to five, with 265 injured and about 8,000 homes damaged.",
             "Civil Defense", "CONFIRMED", "storm"),
            ("PERU QUAKE: ONE DEAD, 853 DISPLACED",
             "A new report on Friday's M6.7 Jun\u00edn quake: one dead, 15 injured, 853 displaced.",
             "INDECI", "CONFIRMED", "quake"),
            ("MEASLES KILLS VIRGINIA CHILD",
             "A child under five in Virginia became the 12th American measles death this year.",
             "CDC", "REPORTED", "health"),
            ("TRUMP THREATENS TECH TAX",
             "Trump threatened a \u201ctremendous tax\u201d on U.S. tech firms building AI data centres abroad.",
             "AP", "REPORTED", "money"),
            ("USDA FARM SYSTEM HACKED",
             "Hackers breached the Agriculture Dept's farmer-payment system, leaving loan applications offline.",
             "AP", "REPORTED", "hack"),
        ],
    },
    {
        "name": "WORLD",
        "count": 2,
        "color": (109, 40, 217),
        "items": [
            ("BEPICOLOMBO ENTERS MERCURY ORBIT",
             "BepiColombo entered Mercury orbit — only the second mission ever; ESA says the craft is safe.",
             "ESA", "CONFIRMED", "rocket"),
        ],
    },
]

SPORT = [
    ("VERSTAPPEN WINS VEGAS THRILLER",
     "Verstappen beat Norris by 0.639s; 352 overtakes, 35 lead changes.",
     "F1", "CONFIRMED"),
    ("ALCARAZ WINS FIRST ATP FINALS",
     "Alcaraz beat Zverev 6-2, 7-6 to win his first ATP Finals title.",
     "ATP", "CONFIRMED"),
    ("M\u00c1RQUEZ CLINCHES EIGHTH TITLE",
     "M\u00e1rquez sealed his eighth MotoGP crown, equalling Agostini.",
     "MotoGP", "CONFIRMED"),
    ("LIVERPOOL ROUT UNITED 4-0",
     "Liverpool thrashed Man Utd 4-0 at Anfield on Pochettino's debut.",
     "EPL", "CONFIRMED"),
    ("WEMBANYAMA DROPS 50",
     "Wembanyama: 50 pts, 19 reb, 5 blocks, 4 steals in a 114-91 win.",
     "NBA", "CONFIRMED"),
    ("INDIA DECLARE ON 720/9",
     "India declared on 720/9 — the highest Test total ever in NZ.",
     "ESPN", "CONFIRMED"),
]

STATS = [
    ("186", "DRONES LAUNCHED"),
    ("161", "SHOT DOWN"),
    ("35%", "ELECTRIFICATION BY 2035"),
    ("$120BN", "ADAPTATION TARGET DROPPED"),
    ("720/9", "INDIA'S RECORD TOTAL"),
    ("50", "PTS · WEMBANYAMA"),
]

TIMELINE = [
    ("00:00", "Drones strike Khartoum (02:00 local)"),
    ("03:00", "Dymer apartment hit, Kyiv region (05:00 local)"),
    ("05:00", "India declares 720/9 in Wellington (18:00 local)"),
    ("13:20", "Peru toll update issued (08:20 Lima)"),
    ("15:00", "Supermarket hit in Vyshneve (17:00 Kyiv)"),
    ("20:00", "COP31 ends without a deal (23:00 Antalya)"),
]

DATE_CHECK = [
    ("Nvidia SEC probe", "17 Nov"),
    ("Poland missiles land", "20 Nov"),
    ("Peru quake strikes", "20 Nov"),
    ("Georgia blast", "19 Nov"),
    ("Brazil storm hits", "20 Nov"),
    ("Cikande fire starts", "21 Nov"),
    ("Sparta II struck", "21 Nov"),
    ("Oxfam Gaza report", "23 Nov"),
]

MAP_PINS = [
    (1, "Kyiv", 30.5, 50.6),
    (2, "Odesa", 30.7, 46.5),
    (3, "Gulf of Finland", 25.0, 59.5),
    (4, "Tbilisi", 44.8, 41.7),
    (5, "Antalya", 30.7, 36.9),
    (6, "Bahrain", 50.6, 26.2),
    (7, "Khartoum", 32.5, 15.6),
    (8, "Hong Kong", 114.2, 22.3),
    (9, "Cikande", 106.3, -6.2),
    (10, "Wellington", 174.8, -41.3),
    (11, "Bras\u00edlia", -47.9, -15.8),
    (12, "Las Vegas", -115.1, 36.2),
]

TOTAL_STORIES = 36
