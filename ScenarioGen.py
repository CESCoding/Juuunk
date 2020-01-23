#! python3
import random
what = {
    1: "Corp extraction",
    2: "Celebrity under threat",
    3: "Hacker causing havoc",
    4: "PC's past catches up with them",
    5: "Valuable item suddenly within reach",
    6: "Media circus comes to town",
    7: "Corp going bust",
    8: "New drug hits the streets",
    9: "Gang war",
    10: "Corrupt cops",
    11: "The mob throws its muscle around",
    12: "An outsider comes to town",
    13: "Nomads on the warpath",
    14: "New hardware hits the streets",
    15: "Crime boss goes legit",
    16: "Cops purge the underworld",
    17: "Megalomaniac out to destroy the world",
    18: "Serial killer",
    19: "Terrorist plot",
}

who = {
    1: "The Mob",
    2: "Military corp",
    3: "Biotech corp",
    4: "The government",
    5: "Unaffiliated local gang",
    6: "Solo",
    7: "Merc outfit",
    8: "Media",
    9: "Fixer",
    10: "Hacker",
    11: "Foreign government",
    12: "Eco-guerrillas",
    13: "Nomad family",
    14: "Police force",
    15: "Rogue Cops",
    16: "Cyber-psycho",
    17: "Underworld Celeb",
    18: "Conspiracy Theorist",
    19: "Rogue government agent",
}

where = {
    1: "Warehouse",
    2: "Corp HQ",
    3: "Government HQ",
    4: "Nightclub",
    5: "Docks",
    6: "Mob HQ",
    7: "Combat zone",
    8: "Dust zone",
    9: "Airport",
    10: "The Net",
    11: "Media HQ",
    12: "Rooftops",
    13: "Subways",
    14: "Police Station",
    15: "Diner/Restaurant",
    16: "Concert hall",
    17: "Hotel",
    18: "Lab",
    19: "Mall",
}

really = {
    1: "Government Cover-up",
    2: "Corp extraction",
    3: "Corp takeover",
    4: "Corrupt cops",
    5: "Smuggling",
    6: "Gang infiltration",
    7: "Blackmail",
    8: "Hacker causing havoc",
    9: "Old enemy",
    10: "Old friend",
    11: "New drug",
    12: "New hardware",
    13: "Solo on the warpath",
    14: "Media creating news/hoax",
    15: "The Mob",
    16: "Biotech corp experiments",
    17: "Cultists",
    18: "All for love",
    19: "It's really what it seems to be",
}

print("What: " + what[random.randint(1, 19)])
print("Who: " + who[random.randint(1, 19)])
print("Where: " + where[random.randint(1, 19)])
print("Really: " + really[random.randint(1, 19)])
