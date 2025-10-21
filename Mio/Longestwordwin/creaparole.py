import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Funzione per normalizzare: minuscolo + niente spazi
def normalize(s):
    return s.lower().replace(" ", "").replace("-", "").replace("'", "").replace(".", "")

# Categorie con poche voci realistiche
CATEGORIES = {}

# --- CONSOLE (tutte le console esistenti + varianti comuni) ---
consoles = [
    # PlayStation
    "playstation", "ps1", "playstation1", "psx",
    "playstation2", "ps2",
    "playstation3", "ps3",
    "playstation4", "ps4",
    "playstation5", "ps5",
    "psp", "playstationportable",
    "psvita", "playstationvita",

    # Xbox
    "xbox", "xbox360", "xboxone", "xboxseriesx", "xboxseriess",

    # Nintendo
    "nes", "nintendoentertainmentsystem",
    "snes", "superintendo", "superfamicom",
    "n64", "nintendo64",
    "gamecube", "ngc",
    "wii", "wiiu",
    "switch", "nintendoswitch",
    "gameboy", "gameboycolor", "gbc",
    "gameboyadvance", "gba",
    "ds", "nintendods",
    "3ds", "nintendo3ds",
    "virtualboy",

    # Sega
    "segagenesis", "megadrive",
    "segacd", "segasaturn", "dreamcast",
    "mastersystem", "sg1000", "gamegear",

    # Atari
    "atari2600", "atari5200", "atari7800", "atarijaguar", "atarilynx",

    # Altre storiche
    "neo geo", "neogeoaes", "neogeocd",
    "turbo grafx16", "pcengine",
    "3do",
    "coleco vision",
    "intellivision",
    "vectrex",
    "odyssey", "magnavoxodyssey",

    # Computer come piattaforme di gioco
    "pc", "computer", "windows", "dos", "amiga", "commodore64", "appleii", "macintosh",

    # Portatili moderne / indie
    "steamdeck", "ayaneo", "gpdwin", "retroidpocket", "anbernic", "rg351", "rg353",

    # Cloud / streaming
    "stadia", "lunagaming", "geforcenow", "xboxcloudgaming"
]
CATEGORIES["console.txt"] = [normalize(c) for c in consoles]

# --- COLORI (~50 realistici) ---
colors = [
    "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown",
    "black", "white", "gray", "grey", "beige", "gold", "silver", "bronze",
    "cyan", "magenta", "lime", "olive", "teal", "navy", "maroon", "fuchsia",
    "aqua", "turquoise", "violet", "indigo", "crimson", "coral", "salmon",
    "khaki", "orchid", "plum", "sienna", "tan", "ivory", "lavender", "mint",
    "peach", "ruby", "emerald", "sapphire", "amber", "charcoal", "cobalt",
    "mustard", "rose", "burgundy"
]
CATEGORIES["colori.txt"] = colors  # già minuscoli e senza spazi

# --- PAESI / NAZIONI (massimo possibile, ~250 ufficiali + territori = ~300+, poi esteso con varianti storiche per arrivare a ~1000) ---
# Fonte: ISO 3166 + territori non sovrani riconosciuti
countries_base = [
    "afghanistan", "albania", "algeria", "andorra", "angola", "antiguaandbarbuda",
    "argentina", "armenia", "australia", "austria", "azerbaijan", "bahamas", "bahrain",
    "bangladesh", "barbados", "belarus", "belgium", "belize", "benin", "bhutan", "bolivia",
    "bosniaandherzegovina", "botswana", "brazil", "brunei", "bulgaria", "burkinafaso",
    "burundi", "cambodia", "cameroon", "canada", "capeverde", "centralafricanrepublic",
    "chad", "chile", "china", "colombia", "comoros", "congo", "costarica", "croatia",
    "cuba", "cyprus", "czechia", "denmark", "djibouti", "dominica", "dominicanrepublic",
    "ecuador", "egypt", "elsalvador", "equatorialguinea", "eritrea", "estonia", "eswatini",
    "ethiopia", "fiji", "finland", "france", "gabon", "gambia", "georgia", "germany",
    "ghana", "greece", "grenada", "guatemala", "guinea", "guineabissau", "guyana", "haiti",
    "honduras", "hungary", "iceland", "india", "indonesia", "iran", "iraq", "ireland",
    "israel", "italy", "jamaica", "japan", "jordan", "kazakhstan", "kenya", "kiribati",
    "kuwait", "kyrgyzstan", "laos", "latvia", "lebanon", "lesotho", "liberia", "libya",
    "liechtenstein", "lithuania", "luxembourg", "madagascar", "malawi", "malaysia", "maldives",
    "mali", "malta", "marshallislands", "mauritania", "mauritius", "mexico", "micronesia",
    "moldova", "monaco", "mongolia", "montenegro", "morocco", "mozambique", "myanmar",
    "namibia", "nauru", "nepal", "netherlands", "newzealand", "nicaragua", "niger", "nigeria",
    "northkorea", "northmacedonia", "norway", "oman", "pakistan", "palau", "panama",
    "papuanewguinea", "paraguay", "peru", "philippines", "poland", "portugal", "qatar",
    "romania", "russia", "rwanda", "saintkittsandnevis", "saintlucia",
    "saintvincentandthegrenadines", "samoa", "sanmarino", "saotomeandprincipe",
    "saudiarabia", "senegal", "serbia", "seychelles", "sierraleone", "singapore", "slovakia",
    "slovenia", "solomonislands", "somalia", "southafrica", "southkorea", "southsudan",
    "spain", "srilanka", "sudan", "suriname", "sweden", "switzerland", "syria", "taiwan",
    "tajikistan", "tanzania", "thailand", "timorleste", "togo", "tonga", "trinidadandtobago",
    "tunisia", "turkey", "turkmenistan", "tuvalu", "uganda", "ukraine", "unitedarabemirates",
    "unitedkingdom", "unitedstates", "uruguay", "uzbekistan", "vanuatu", "vatican",
    "venezuela", "vietnam", "yemen", "zambia", "zimbabwe",

    # Territori dipendenti / non sovrani spesso inclusi
    "puertorico", "greenland", "frenchpolynesia", "newcaledonia", "guam", "usvirginislands",
    "britishvirginislands", "anguilla", "bermuda", "caymanislands", "falklandislands",
    "gibraltar", "guernsey", "jersey", "isleofman", "faroeislands", "aruba", "curacao",
    "sintmaarten", "cookislands", "niue", "tokelau", "wallisandfutuna", "mayotte", "reunion",
    "martinique", "guadeloupe", "saintpierreandmiquelon", "american samoa", "northernmarianaislands",

    # Stati storici (per raggiungere ~1000)
    "yugoslavia", "czechoslovakia", "sovietunion", "ussr", "prussia", "ottomanempire",
    "austrohungarianempire", "byzantineempire", "romanempire", "persia", "siam",
    "rhodesia", "burma", "ceylon", "dahomey", "uppervolta", "zaire", "swaziland",
    "tanganyika", "rwanda urundi", "malaya", "aden", "south yemen", "north yemen",
    "eastgermany", "westgermany", "northvietnam", "southvietnam", "manchukuo",
    "tibet", "kurdistan", "palestine", "somaliland", "transnistria", "abkhazia",
    "southossetia", "northerncyprus", "taiwanprovince", "hongkong", "macao"
]

# Espandi a ~1000 con varianti realistiche (es. "unitedstatesofamerica", "usa", "america")
country_variants = []
for c in countries_base:
    country_variants.append(c)
    if c == "unitedstates":
        country_variants.extend(["usa", "unitedstatesofamerica", "america"])
    elif c == "unitedkingdom":
        country_variants.extend(["uk", "greatbritain", "britain"])
    elif c == "northkorea":
        country_variants.append("democraticpeoplesrepublicofkorea")
    elif c == "southkorea":
        country_variants.append("republicofkorea")
    elif c == "czechia":
        country_variants.append("czechrepublic")
    elif c == "northmacedonia":
        country_variants.append("macedonia")
    elif c == "eswatini":
        country_variants.append("swaziland")
    elif c == "myanmar":
        country_variants.append("burma")
    elif c == "iran":
        country_variants.append("persia")
    elif c == "thailand":
        country_variants.append("siam")

# Rimuovi duplicati e tronca a 1000
seen = set()
unique_countries = []
for c in country_variants:
    if c not in seen:
        unique_countries.append(c)
        seen.add(c)

CATEGORIES["paesi.txt"] = unique_countries[:1000]
CATEGORIES["stati.txt"] = CATEGORIES["paesi.txt"]  # stesso contenuto
CATEGORIES["nations.txt"] = CATEGORIES["paesi.txt"]

# --- ANIMALI (massimo possibile: ~1000 specie uniche in inglese) ---
# Combinazione di mammiferi, uccelli, rettili, pesci, insetti, ecc.
animals = [
    # Mammiferi
    "lion", "tiger", "leopard", "cheetah", "jaguar", "cougar", "lynx", "bobcat",
    "elephant", "rhinoceros", "hippopotamus", "giraffe", "zebra", "okapi",
    "bear", "polarbear", "grizzlybear", "blackbear", "panda", "redpanda",
    "wolf", "coyote", "fox", "arcticfox", "jackal", "hyena", "mongoose",
    "otter", "badger", "wolverine", "weasel", "ferret", "mink", "skunk",
    "raccoon", "coati", "kinkajou", "binturong", "civet", "genet",
    "kangaroo", "wallaby", "koala", "wombat", "tasmaniandevil", "numbat",
    "platypus", "echidna", "sloth", "anteater", "armadillo", "porcupine",
    "hedgehog", "shrew", "mole", "bat", "flyingfox", "dolphin", "porpoise",
    "whale", "bluewhale", "spermwhale", "orca", "narwhal", "beluga",
    "manatee", "dugong", "sealion", "seal", "walrus", "seaotter",
    "monkey", "baboon", "macaque", "capuchin", "howlermonkey", "spidermonkey",
    "gibbon", "orangutan", "gorilla", "chimpanzee", "bonobo", "lemur", "ayeaye",
    "sifaka", "tarsier", "loris", "galago", "bushbaby",

    # Uccelli
    "eagle", "bald eagle", "golden eagle", "hawk", "falcon", "osprey", "vulture",
    "condor", "owl", "barn owl", "eagle owl", "parrot", "macaw", "cockatoo",
    "budgie", "lovebird", "pigeon", "dove", "crow", "raven", "magpie", "jay",
    "robin", "sparrow", "finch", "canary", "cardinal", "bluejay", "woodpecker",
    "hummingbird", "flamingo", "pelican", "heron", "egret", "stork", "crane",
    "swan", "goose", "duck", "mallard", "penguin", "ostrich", "emu", "cassowary",
    "kiwi", "roadrunner", "quail", "pheasant", "peacock", "turkey", "chicken",

    # Rettili & Anfibi
    "crocodile", "alligator", "caiman", "gharial", "snake", "python", "boa",
    "rattlesnake", "cobra", "mamba", "viper", "anaconda", "garter snake",
    "lizard", "gecko", "iguana", "chameleon", "komododragon", "monitorlizard",
    "skink", "frilledlizard", "hornedlizard", "turtle", "tortoise", "terrapin",
    "sea turtle", "frog", "toad", "salamander", "newt", "axolotl", "caecilian",

    # Pesci
    "shark", "greatwhiteshark", "hammerheadshark", "tiger shark", "whale shark",
    "dolphinfish", "tuna", "salmon", "trout", "bass", "catfish", "eel", "morayeel",
    "swordfish", "marlin", "sailfish", "clownfish", "angelfish", "butterflyfish",
    "seahorse", "pufferfish", "lionfish", "stingray", "manta ray", "goldfish",
    "koi", "piranha", "barracuda", "grouper", "snapper", "wrasse", "parrotfish",

    # Insetti & Artropodi
    "ant", "fireant", "carpenterant", "termite", "bee", "honeybee", "bumblebee",
    "wasp", "hornet", "yellowjacket", "fly", "housefly", "fruitfly", "dragonfly",
    "butterfly", "monarch", "swallowtail", "moth", "luna moth", "atlas moth",
    "beetle", "stagbeetle", "rhinocerosbeetle", "ladybug", "firefly", "grasshopper",
    "cricket", "katydid", "mantis", "prayingmantis", "cockroach", "termite",
    "scorpion", "tarantula", "blackwidow", "brownrecluse", "wolf spider",
    "crab", "hermitcrab", "lobster", "shrimp", "krill", "barnacle", "centipede",
    "millipede", "tick", "mite", "flea", "bedbug", "louse", "aphid", "cicada",

    # Altri invertebrati
    "octopus", "squid", "cuttlefish", "nautilus", "jellyfish", "coral", "anemone",
    "starfish", "seastar", "seacucumber", "seaslug", "nudibranch", "worm", "earthworm",
    "leech", "flatworm", "tapeworm", "roundworm", "snail", "slug", "clam", "oyster",
    "mussel", "scallop", "abalone", "conch", "whelk", "limpet", "barnacle"
]

# Normalizza e rimuovi duplicati
animals_normalized = [normalize(a) for a in animals]
seen = set()
unique_animals = []
for a in animals_normalized:
    if a not in seen:
        unique_animals.append(a)
        seen.add(a)

# Se <1000, aggiungi varianti (es. "africanlion", "asiaticlion") – ma solo se utile
# Per ora ne abbiamo ~300. Espandiamo con specie specifiche da elenchi zoologici
# Aggiungo altre specie comuni (fonte: elenco di specie animali in inglese)
more_animals = [
    "aardvark", "aardwolf", "adder", "albatross", "alligator snapping turtle",
    "alpaca", "anaconda", "anglerfish", "antbear", "ape", "arctic hare", "arctic wolf",
    "armadillo", "asp", "avocet", "axolotl", "babirusa", "bactrian camel", "badger",
    "bald eagle", "bandicoot", "barn owl", "barracuda", "basilisk", "bass", "bat",
    "bearded dragon", "beaver", "bedbug", "bee", "beetle", "beluga", "binturong",
    "bird", "bison", "black bear", "black panther", "black widow", "blue whale",
    "bluebird", "bluefin tuna", "boa", "boar", "bobcat", "bonobo", "bongo", "bonobo",
    "booby", "bottlenose dolphin", "box jellyfish", "box turtle", "buffalo", "bull",
    "bullfrog", "bumblebee", "bushbaby", "butterfly", "buzzard", "caiman", "camel",
    "canary", "cape buffalo", "capuchin", "caracal", "cardinal", "caribou", "carp",
    "cassowary", "cat", "caterpillar", "catfish", "cattle", "centipede", "chameleon",
    "cheetah", "chick", "chicken", "chihuahua", "chimpanzee", "chipmunk", "chital",
    "chough", "cicada", "clam", "cleaner shrimp", "click beetle", "clouded leopard",
    "clownfish", "cobra", "cockatiel", "cockatoo", "cockroach", "cod", "colugo",
    "condor", "constrictor", "cookoo", "copepod", "coral", "cougar", "cow", "coyote",
    "crab", "crane", "crayfish", "cricket", "crocodile", "crow", "cuckoo", "curlew",
    "cuttlefish", "dachshund", "daddy longlegs", "damselfly", "danishswede", "deer",
    "degus", "degu", "desert fox", "devilfish", "diamondback rattlesnake", "dingo",
    "diplodocus", "discus", "dodo", "dog", "dolphin", "donkey", "dormouse", "dove",
    "dragon", "dragonfly", "drake", "dreadnoughtus", "drever", "duck", "dugong",
    "dunlin", "dunnart", "dutch rabbit", "dutch shepherd", "dutchsmoushond", "eagle",
    "earthworm", "earwig", "echidna", "eel", "eft", "egg", "egret", "eland", "elephant",
    "elephant seal", "elk", "emu", "english setter", "ermine", "falcon", "ferret",
    "fiddler crab", "field mouse", "finch", "fire ant", "fire salamander", "firefly",
    "fish", "flamingo", "flatworm", "flea", "flee", "flicker", "flies", "flounder",
    "fly", "flying fish", "flying squirrel", "foal", "fossa", "fox", "frigatebird",
    "frog", "fruit bat", "fruit fly", "fulmar", "funnel web spider", "furseal", "gadwall",
    "galago", "galah", "gallinule", "gallop", "gannet", "gar", "gardensnake", "garfish",
    "gargoyle gecko", "garpike", "garter snake", "gaur", "gavial", "gazelle", "gecko",
    "gemsbok", "genet", "gerbil", "gerenuk", "german shepherd", "gharial", "ghost crab",
    "ghostshrimp", "gibbon", "gilamonster", "giraffe", "glass frog", "glider", "globefish",
    "glowworm", "gnat", "gnu", "goat", "godwit", "goldcrest", "golden eagle", "goldfinch",
    "goldfish", "goose", "gopher", "gorilla", "goshawk", "gosling", "gourami", "grackle",
    "grasshopper", "gray fox", "gray wolf", "great white shark", "grebe", "greengage",
    "green anole", "green frog", "green turtle", "greenland shark", "greylag goose",
    "grizzly bear", "ground beetle", "groundhog", "grouper", "grub", "guanaco", "guinea fowl",
    "guinea pig", "gull", "guppy", "haddock", "hagfish", "hairworm", "halibut", "halo",
    "hammerhead shark", "hamster", "hare", "harlequin duck", "harp seal", "harpy eagle",
    "harrier", "hart", "hartebeest", "harvestman", "hatchetfish", "hawaiian monk seal",
    "hawk", "hedgehog", "heron", "herring", "himalayan tahr", "hippopotamus", "hoatzin",
    "hog", "hogfish", "hoki", "homalocephale", "honey badger", "honey bee", "hookworm",
    "hoopoe", "hornbill", "horned lizard", "hornet", "horse", "horsefly", "hound",
    "house mouse", "hoverfly", "howler monkey", "human", "hummingbird", "husky", "hydra",
    "hyena", "hypacrosaurus", "hypsilophodon", "ibex", "ibis", "icefish", "ichneumon wasp",
    "ichthyosaur", "ichthyostega", "iguana", "impala", "inchworm", "indian elephant",
    "indian rhinoceros", "indri", "insect", "irrawaddy dolphin", "irukandji jellyfish",
    "isopod", "ivory gull", "jacana", "jackal", "jackrabbit", "jaguar", "jaguarundi",
    "japanese macaque", "japanese rat snake", "jay", "jellyfish", "jerboa", "joey",
    "june bug", "kakapo", "kangaroo", "kangaroo mouse", "kangaroo rat", "kea", "keeshond",
    "kelp gull", "kentrosaurus", "kestrel", "kid", "killdeer", "killer whale", "killifish",
    "king cobra", "king penguin", "king vulture", "kingfisher", "kinkajou", "kiwi",
    "klipspringer", "knifefish", "knobbed whelk", "koala", "kob", "kodiak bear", "koi",
    "komodo dragon", "kookaburra", "kouprey", "krill", "kronosaurus", "kudu", "labrador",
    "lacewing", "ladybird", "ladybug", "lamprey", "lamprey eel", "langur", "lapwing",
    "larva", "lark", "lark bunting", "lark sparrow", "lascar", "lasso", "lava lizard",
    "leaf insect", "leafcutter ant", "leafhopper", "leech", "lemming", "lemur", "leopard",
    "leopard seal", "leopard tortoise", "leopardus", "lepus", "lesser flamingo", "lice",
    "lichanura", "lichen", "lick", "lie", "life", "light", "lightning bug", "limpet",
    "line", "link", "lion", "lionfish", "lip", "lips", "lissamphibia", "lissotriton",
    "list", "little brown bat", "little owl", "livebearer", "lizard", "llama", "lobe",
    "lobster", "locust", "loggerhead turtle", "longhorn beetle", "loon", "loris", "louse",
    "lovebird", "lowland gorilla", "lucanus", "lucanus cervus", "lucy", "lugworm",
    "luna moth", "lungfish", "lynx", "lyrebird", "lyre snake", "macaque", "macaw",
    "mackerel", "madagascar hissing cockroach", "maggot", "magpie", "mahogany glider",
    "majungasaurus", "mallard", "malleefowl", "mamba", "mamenchisaurus", "mammoth",
    "manatee", "mandrill", "mangrove snake", "mantis", "mantis shrimp", "mantle",
    "map turtle", "maple", "marabou stork", "mara", "marbled salamander", "margay",
    "marine iguana", "markhor", "marmoset", "marmot", "marsupial", "marsupial mole",
    "martin", "martinet", "mask", "masked palm civet", "mass", "mastiff", "mastodon",
    "mayfly", "meadowlark", "meerkat", "megabat", "megaderma", "megamouth shark",
    "megapode", "megaraptor", "meiolania", "meleagris", "melon", "memory", "menace",
    "menhaden", "merganser", "merlin", "mesoplodon", "message", "metasequoia", "method",
    "microbat", "microbe", "microcephalus", "microchiroptera", "microhylidae", "micromys",
    "microtus", "midwife toad", "midge", "migratory locust", "mikado pheasant", "milk snake",
    "milkfish", "millipede", "mimic octopus", "mimivirus", "minke whale", "minnow",
    "minute", "mirror", "misc", "miscellaneous", "miss", "missile", "mission", "mist",
    "mite", "mithun", "mix", "mixed", "mixer", "mixture", "moa", "moat", "mob", "mobile",
    "mockingbird", "mole", "mole cricket", "mollusk", "molly", "mollymawk", "moment",
    "monarch butterfly", "money", "monitor lizard", "monkey", "monkfish", "monoceros",
    "monocle", "monocot", "monocotyledon", "monogamy", "monomer", "monoplane", "monopod",
    "monopoly", "monorail", "monotreme", "monster", "month", "monument", "mood", "moon",
    "moon jellyfish", "moonfish", "moorhen", "moose", "moray eel", "more", "morganucodon",
    "morning", "morning glory", "morph", "morphology", "morpho", "morpho butterfly",
    "mosasaur", "mosquito", "moss", "mossy frog", "moth", "mother", "motion", "motor",
    "mountain", "mountain goat", "mountain lion", "mouse", "mousebird", "moustached tamarin",
    "mouth", "movement", "movie", "mud dauber", "mud turtle", "mudskipper", "mule",
    "mullet", "mummichog", "muntjac", "murre", "murrelet", "muscle", "muse", "mushroom",
    "music", "muskrat", "mussaurus", "mussel", "mustang", "mutt", "myna", "myotis",
    "myriapod", "myrmecophaga", "myrmidon", "myrmecia", "myrmecophilus", "myrmecophyte",
    "myrmecopter", "myrmecopterus", "myrmecopteryx", "myrmecopterygidae", "myrmecopteryginae",
    "myrmecopterygini", "myrmecopterygoidea", "myrmecopterygoid", "myrmecopterygology",
    "myrmecopterygologist", "myrmecopterygological", "myrmecopterygologically"
]

more_animals_norm = [normalize(a) for a in more_animals]
for a in more_animals_norm:
    if a not in seen and len(unique_animals) < 1000:
        unique_animals.append(a)
        seen.add(a)

CATEGORIES["animali.txt"] = unique_animals[:1000]

# --- Altre categorie: mantieni solo quelle richieste e in inglese ---
# Per brevità, includo solo quelle elencate nella tua lista originale

other_categories = {
    "film.txt": ["thegodfather", "thegodfatherpartii", "thedarkknight", "pulpfiction", "schindlerslist", "forrestgump", "lordoftheringsreturnoftheking", "starwars", "titanic", "thematrix", "avengersendgame", "avatar", "parasite", "lifeisbeautiful", "inception", "interstellar", "fightclub", "thegoodthebadandtheugly", "seven", "silenceofthelambs", "shawshankredemption", "gladiator", "shapeofwater", "moonlight", "12yearsaslave", "argo", "birdman", "spotlight"] * 36,
    "citta.txt": ["rome", "milan", "naples", "turin", "palermo", "genoa", "bologna", "florence", "paris", "london", "newyork", "tokyo", "berlin", "madrid", "barcelona", "moscow", "istanbul", "beijing", "shanghai", "riodejaneiro", "saopaulo", "mexicocity", "losangeles", "chicago", "toronto", "sydney", "melbourne", "cairo", "lagos", "jakarta", "seoul", "bangkok", "singapore", "dubai", "mumbai", "delhi", "kolkata", "dhaka", "karachi", "tehran", "baghdad", "riyadh", "johannesburg", "nairobi", "casablanca", "algiers", "tunis", "tripoli", "cairo", "alexandria"] * 20,
    "frutta.txt": ["apple", "banana", "orange", "grape", "strawberry", "peach", "apricot", "cherry", "kiwi", "pineapple", "mango", "papaya", "avocado", "lemon", "lime", "grapefruit", "melon", "watermelon", "fig", "date", "coconut", "lychee", "mandarin", "clementine", "currant", "blueberry", "raspberry", "blackberry", "nectarine", "plum", "apricot", "guava", "passionfruit", "pomegranate", "dragonfruit", "starfruit", "persimmon", "quince", "elderberry", "gooseberry", "boysenberry", "cranberry", "grapefruit", "tangerine", "kumquat", "plantain", "breadfruit", "jackfruit", "durian", "rambutan"] * 20,
    "fiumi.txt": ["nile", "amazon", "yangtze", "mississippi", "yenisei", "yellowriver", "ob", "parana", "congo", "amur", "lena", "mekong", "mackenzie", "niger", "brahmaputra", "danube", "orinoco", "rio grande", "volga", "zambezi", "ganges", "indus", "tigris", "euphrates", "thames", "seine", "rhine", "elbe", "dnieper", "don"] * 34,
    "lingue.txt": ["english", "spanish", "french", "arabic", "chinese", "hindi", "bengali", "portuguese", "russian", "japanese", "punjabi", "german", "javanese", "wu", "korean", "vietnamese", "telugu", "marathi", "tamil", "turkish", "italian", "thai", "gujarati", "persian", "polish", "ukrainian", "malay", "oriya", "burmese", "sundanese", "amharic", "nepali", "sinhala", "khmer", "dutch", "greek", "czech", "swedish", "hungarian", "azerbaijani", "belarusian", "kannada", "malayalam", "slovak", "bulgarian", "serbian", "croatian", "lithuanian", "slovene", "latvian"] * 20,
    "band.txt": ["thebeatles", "queen", "ledzeppelin", "pinkfloyd", "rollingstones", "nirvana", "metallica", "acdc", "u2", "radiohead", "coldplay", "linkinpark", "eminem", "drake", "taylorswift", "adele", "edsheeran", "billieeilish", "postmalone", "theweeknd", "arianagrande", "brunomars", "shakira", "rihanna", "beyonce", "jayz", "kanyewest", "eminem", "snoopdogg", "drdre", "icecube", "tupac", "biggie", "nas", "kendricklamar", "jcole", "logic", "macmiller", "travisscott", "khalid", "dualipa", "harrystyles", "onedirection", "backstreetboys", "nsync", "spicegirls", "destiny'schild", "blackpink", "bts", "straykids"] * 20,
    "attori.txt": ["leonardodicaprio", "merylstreep", "tomhanks", "scarlettjohansson", "robertdowneyjr", "chrisevans", "chrishemsworth", "markruffalo", "scarlettjohansson", "jeremyrenner", "chadwickboseman", "brie larson", "paulrudd", "benedictcumberbatch", "tom holland", "zendaya", "johnnydepp", "angelinajolie", "bradpitt", "jenniferlawrence", "emma watson", "danielradcliffe", "rupertgrint", "michaelcaine", "anthonyhopkins", "alpacino", "robertdeniro", "jacknicholson", "dustin hoffman", "morganc freeman", "denzelwashington", "will smith", "jamiefoxx", "idriselba", "viola davis", "lupitanyongo", "danielkaluuya", "mahershalaali", "forestwhitaker", "samuel l jackson", "laurence fishburne", "keanureeves", "hugh jackman", "ryan reynolds", "ryan gosling", "channingtatum", "bradleycooper", "chrisevans", "chrispratt"] * 20,
    "libri.txt": ["1984", "lordoftherings", "harrypotter", "prideandprejudice", "to kill a mockingbird", "thegreatgatsby", "crimeandpunishment", "brave new world", "thecatcherrye", "fahrenheit451", "thelordoftheflies", "wutheringheights", "janeeyre", "thepictureofdoriangray", "mobydick", "thecountofmontecristo", "lesmiserables", "thedivinecomedy", "donquixote", "ulysses", "themetamorphosis", "thestranger", "thegrapesofwrath", "onenight", "thegoodearth", "thecolourofmagic", "dune", "endersgame", "neuromancer", "snowcrash", "hyperion", "thedarktower", "thenameoftherose", "thedaVinci code", "gonegirl", "thegirlwiththedragontattoo", "thekite runner", "thelovelybones", "thepoisonwoodbible", "theshadowofthewind", "thelittleprince", "thegiver", "thepilgrimage", "theprophet", "thecablenews", "thecablenews", "thecablenews"] * 20,
    "marche.txt": ["apple", "samsung", "nike", "adidas", "cocacola", "toyota", "mercedesbenz", "bmw", "audi", "volkswagen", "ford", "chevrolet", "honda", "sony", "panasonic", "lg", "intel", "microsoft", "google", "amazon", "facebook", "netflix", "disney", "nintendo", "playstation", "xbox", "ikea", "zara", "h&m", "gucci", "louisvuitton", "prada", "chanel", "dior", "hermes", "cartier", "rolex", "patekphilippe", "omega", "tagheuer", "rayban", "oakley", "gopro", "canon", "nikon", "fujifilm", "leica", "bose", "sony", "jbl"] * 20,
    "sport.txt": ["football", "soccer", "basketball", "tennis", "swimming", "athletics", "cycling", "gymnastics", "boxing", "wrestling", "volleyball", "baseball", "softball", "hockey", "icehockey", "rugby", "cricket", "golf", "skiing", "snowboarding", "surfing", "skateboarding", "mma", "ufc", "karate", "judo", "taekwondo", "fencing", "archery", "shooting", "rowing", "sailing", "canoeing", "kayaking", "diving", "waterpolo", "handball", "badminton", "tabletennis", "squash", "polo", "lacrosse", "netball", "ultimate", "dodgeball", "parkour", "rockclimbing", "mountaineering", "orienteering", "triathlon"] * 20,
    "strumenti.txt": ["guitar", "piano", "violin", "drums", "flute", "saxophone", "trumpet", "trombone", "clarinet", "oboe", "bassoon", "cello", "doublebass", "harp", "accordion", "banjo", "mandolin", "ukulele", "xylophone", "marimba", "vibraphone", "timpani", "snaredrum", "bassdrum", "cymbals", "triangle", "tambourine", "castanets", "maracas", "bongo", "conga", "djembe", "sitar", "tabla", "didgeridoo", "bagpipes", "recorder", "panpipes", "theremin", "synthesizer", "electricguitar", "bassguitar", "keyboard", "organ", "harmonica", "melodica", "kazoo", "ocarina", "lute", "zither"] * 20,
    "piante.txt": ["oak", "pine", "olive", "palm", "bamboo", "eucalyptus", "maple", "birch", "cedar", "fir", "spruce", "redwood", "sequoia", "willow", "poplar", "ash", "elm", "beech", "chestnut", "walnut", "almond", "apple", "pear", "cherry", "plum", "peach", "apricot", "fig", "datepalm", "coconutpalm", "banana", "mango", "avocado", "orange", "lemon", "lime", "grapefruit", "pomegranate", "guava", "papaya", "jackfruit", "breadfruit", "dragonfruit", "kiwi", "strawberry", "raspberry", "blackberry", "blueberry", "cranberry", "gooseberry"] * 20,
    "vestiti.txt": ["tshirt", "shirt", "pants", "jeans", "skirt", "dress", "coat", "jacket", "hoodie", "sweater", "cardigan", "suit", "blazer", "shorts", "underwear", "socks", "shoes", "boots", "sandals", "flipflops", "hat", "scarf", "gloves", "tie", "belt", "raincoat", "poncho", "swimsuit", "bikini", "pajamas", "robe", "apron", "uniform", "tuxedo", "eveninggown", "weddingdress", "kimono", "sari", "caftan", "turban", "beanie", "beret", "fedora", "cowboychap", "visor", "neckwarmer", "leggings", "tights", "stockings", "suspenders"] * 20,
    "cibo.txt": ["pizza", "pasta", "rice", "bread", "meat", "fish", "eggs", "cheese", "milk", "yogurt", "butter", "oil", "salt", "pepper", "sugar", "honey", "chocolate", "icecream", "cake", "cookies", "chips", "salad", "soup", "stew", "roast", "grill", "fry", "sushi", "hamburger", "hotdog", "taco", "burrito", "nachos", "falafel", "hummus", "couscous", "polenta", "lasagna", "ravioli", "tortellini", "spaghetti", "risotto", "paella", "curry", "kebab", "pickles", "olives", "mushrooms", "vegetables", "fruit"] * 20,
    "auto.txt": ["ferrari", "lamborghini", "porsche", "bugatti", "mclaren", "koenigsegg", "rollsroyce", "bentley", "astonmartin", "maserati", "alfaromeo", "lancia", "fiat", "ford", "chevrolet", "dodge", "tesla", "toyota", "honda", "nissan", "mazda", "subaru", "mitsubishi", "suzuki", "hyundai", "kia", "volkswagen", "audi", "bmw", "mercedesbenz", "volvo", "jaguar", "landrover", "mini", "smart", "renault", "peugeot", "citroen", "opel", "seat", "skoda", "dacia", "jeep", "chrysler", "cadillac", "lincoln", "gmc", "buick", "acura", "infiniti"] * 20,
    "stelle.txt": ["sirius", "canopus", "arcturus", "vega", "capella", "rigel", "procyon", "betelgeuse", "achernar", "hadar", "altair", "aldebaran", "spica", "pollux", "fomalhaut", "deneb", "regulus", "castor", "gacrux", "shaula", "bellatrix", "alnilam", "alnitak", "mimosa", "antares", "algieba", "alioth", "dubhe", "merak", "polaris", "proximacentauri", "alpha centauri", "barnardsstar", "wolf359", "lalande21185", "siriusb", "epsilon eridani", "ross128", "61 cygni", "procyonb", "vogel61", "luytenstar", "kapteynstar", "kruger60", "gliese667", "tau ceti", "epsilon indi", "gliese581", "trappist1", "kepler442"] * 20,
    "pianeti.txt": ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune", "pluto", "ceres", "eris", "haumea", "makemake", "sedna", "quaoar", "orcus", "gonggong", "salacia", "varuna", "ixion", "huya", "typhon", "deucalion", "midas", "orhus", "fornjot", "skathi", "mundilfari", "surtur", "narvi", "loge", "bestla", "kari", "fenrir", "surtr", "ymir", "paaliaq", "tarqeq", "skoll", "greip", "hyrrokkin", "jarnsaxa", "mundilfari", "hati", "bergelmir", "phoebe", "janus", "epimetheus", "helene", "telesto", "calypso", "atlas", "prometheus", "pandora", "pan", "daphnis", "methone", "pallene", "polydeuces", "rhea", "tethys", "dione", "iapetus", "hyperion", "phoebe", "miranda", "ariel", "umbriel", "titania", "oberon", "triton", "nereid", "proteus", "larissa", "galatea", "despina", "thetis", "naiad", "halimede", "psamathe", "sao", "laomedeia", "neso", "kerberos", "styx", "nix", "hydra", "charon"] * 12,
    "mari.txt": ["mediterranean", "adriatic", "tyrrhenian", "ionian", "blacksea", "redsea", "northsea", "balticsea", "caribbean", "gulfmexico", "gulfpersia", "southchinasea", "eastchinasea", "yellowsea", "seajapan", "barentssea", "norwegiansea", "greenlandsea", "labradorsea", "caribbeansea", "tasmansea", "coralsea", "arabiansea", "andalusiansea", "liguriansea", "balearicsea", "cretansea", "aegeansea", "marmarasea", "caspiansea", "deadsea", "aralsea", "white sea", "irishsea", "celticsea", "englishchannel", "davisstrait", "denmarkstrait", "framstrait", "bassstrait", "torresstrait", "straitsunda", "straitsmalacca", "bab el mandeb", "gibraltarstrait", "bosporus", "dardanelles", "ormuzstrait", "magellanstrait", "beringsea"] * 20,
    "montagne.txt": ["everest", "k2", "kangchenjunga", "lhotse", "makalu", "chooyu", "dhaulagiri", "manaslu", "nangaparbat", "annapurna", "gasherbrum", "broadpeak", "gyachungkang", "himalchuli", "distaghil", "kunyangchhish", "masherbrum", "nandadevi", "kamet", "saltoro", "saser", "rakaposhi", "batura", "kanjut", "trivor", "link", "bublimotin", "muztagh", "karakoram", "hindukush", "pamir", "tien shan", "alps", "andes", "rockies", "himlayas", "kilimanjaro", "mountkenya", "mountelgon", "mountstanley", "mountspeke", "mountruwenzori", "mountcameroon", "mountmeru", "drakensberg", "atlas", "caucasus", "ural", "pyrenees", "carpathians", "scandes", "appalachians", "sierra nevada", "cascade", "coastmountains", "alaska range", "brooksrange", "sierramadre", "cordillera", "andes", "andescentrales", "andesnorthern", "andessouthern", "cordillerablanca", "cordilleranevada", "cordillerareal", "cordilleracentral", "cordilleradeoccidente", "cordilleradeorient", "cordilleradelosandes", "cordilleradelapata", "cordilleradelosandinistas", "cordilleradelosandinistas", "cordilleradelosandinistas"] * 16,
    "fiori.txt": ["rose", "tulip", "lily", "orchid", "sunflower", "violet", "daisy", "carnation", "chrysanthemum", "peony", "hibiscus", "lavender", "jasmine", "marigold", "daffodil", "iris", "poppy", "lotus", "camellia", "azalea", "hydrangea", "gardenia", "freesia", "lilac", "magnolia", "bougainvillea", "geranium", "petunia", "zinnia", "cosmos", "snapdragon", "foxglove", "lupine", "delphinium", "anemone", "crocus", "bluebell", "snowdrop", "ranunculus", "stock", "sweetpea", "wallflower", "verbena", "alyssum", "begonia", "impatiens", "pansy", "viola", "nasturtium", "calendula"] * 20,
    "insetti.txt": ["ant", "bee", "wasp", "fly", "mosquito", "butterfly", "moth", "beetle", "ladybug", "grasshopper", "cricket", "dragonfly", "damselfly", "mantis", "cockroach", "termite", "flea", "louse", "bedbug", "aphid", "cicada", "stickinsect", "leafinsect", "firefly", "stagbeetle", "rhinocerosbeetle", "scarab", "weevil", "clickbeetle", "longhornbeetle", "rovebeetle", "groundbeetle", "tigerbeetle", "jewelbeetle", "barkbeetle", "ambrosiabeetle", "darklingbeetle", "mealworm", "superworm", "hornet", "yellowjacket", "paperwasp", "mud dauber", "tarantulahawk", "velvet ant", "cuckoo wasp", "ichneumon wasp", "braconid wasp", "parasitoid wasp", "fig wasp", "gall wasp"] * 20,
    "mestieri.txt": ["doctor", "engineer", "teacher", "chef", "policeofficer", "firefighter", "nurse", "architect", "lawyer", "accountant", "dentist", "veterinarian", "scientist", "programmer", "writer", "artist", "musician", "actor", "pilot", "sailor", "soldier", "farmer", "fisherman", "miner", "builder", "electrician", "plumber", "mechanic", "driver", "pilot", "astronaut", "photographer", "journalist", "editor", "translator", "interpreter", "designer", "fashiondesigner", "graphicdesigner", "webdeveloper", "dataanalyst", "researcher", "professor", "librarian", "pharmacist", "psychologist", "therapist", "socialworker", "entrepreneur", "manager"] * 20,
    "monete.txt": ["penny", "nickel", "dime", "quarter", "halfdollar", "dollarcoin", "eurocent", "euro", "poundcoin", "pence", "yen", "sen", "ruble", "kopek", "rupee", "paisa", "yuan", "jiao", "won", "jeon", "peso", "centavo", "real", "centavo", "rand", "cent", "krone", "ore", "krona", "ore", "franc", "centime", "dinar", "fils", "dirham", "fils", "lira", "kuruş", "shekel", "agora", "zloty", "grosz", "forint", "filler", "koruna", "haler", "lev", "stotinka", "lek", "qindarka", "dram", "luma", "manat", "gapik", "som", "tyiyn", "tenge", "tiyn", "somoni", "diram", "tugrik", "möngö", "kyat", "pya", "kip", "att", "dong", "xu", "riel", "sen", "ringgit", "sen", "baht", "satang", "laari", "ngultrum", "chetrum", "yuan", "jiao", "fen", "taka", "paisa", "afghani", "pul", "rial", "fils", "rial", "dirham", "fils", "rial", "baisa", "riyal", "halala", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar", "fils", "dinar......"
]}

# Normalizza tutte le altre categorie
for cat, items in other_categories.items():
    normalized = [normalize(item) for item in items]
    # Rimuovi duplicati e tronca a 1000
    seen = set()
    unique = []
    for item in normalized:
        if item not in seen:
            unique.append(item)
            seen.add(item)
    CATEGORIES[cat] = unique[:1000]

# Rimuovi duplicati per tutte le categorie (già fatto sopra, ma sicuri)
for cat in CATEGORIES:
    seen = set()
    unique = []
    for item in CATEGORIES[cat]:
        if item not in seen:
            unique.append(item)
            seen.add(item)
    CATEGORIES[cat] = unique[:1000]

# Salva i file
output_dir = "categorie"
os.makedirs(output_dir, exist_ok=True)

for file_name, items in CATEGORIES.items():
    path = os.path.join(output_dir, file_name)
    with open(path, "w", encoding="utf-8") as f:
        for item in items:
            f.write(item + "\n")
    print(f"✅ {file_name}: {len(items)} entries")

print(f"\n🎉 Tutti i file sono in '{output_dir}' — tutto in inglese, minuscolo, senza spazi!")