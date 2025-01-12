import random


def randomize_alignment():
    alignments = [
        "Lawful Good",
        "Neutral Good",
        "Chaotic Good",
        "Lawful Neutral",
        "True Neutral",
        "Chaotic Neutral",
        "Lawful Evil",
        "Neutral Evil",
        "Chaotic Evil",
    ]
    return random.choice(alignments)


def randomize_race():
    races = [
        "Dragonborn",
        "Drow (Lolth-Sworn)",
        "Drow (Seldarine)",
        "Dwarf (Gold)",
        "Dwarf (Shield)",
        "Dwarf (Duergar)",
        "Elf (High)",
        "Elf (Wood)",
        "Githyanki",
        "Gnome (Rock)",
        "Gnome (Deep)",
        "Gnome (Forest)",
        "Half-Elf (High)",
        "Half-Elf (Wood)",
        "Half-Elf (Drow)",
        "Half-Orc",
        "Halfling (Lightfoot)",
        "Halfling (Strongheart)",
        "Human",
        "Tiefling (Asmodeus)",
        "Tiefling (Mephistopheles)",
        "Tiefling (Zariel)",
    ]
    return random.choice(races)


def randomize_class():
    classes = [
        "Barbarian",
        "Bard",
        "Cleric",
        "Druid",
        "Fighter",
        "Monk",
        "Paladin",
        "Ranger",
        "Rogue",
        "Sorcerer",
        "Warlock",
        "Wizard",
    ]
    return random.choice(classes)


if __name__ == "__main__":
    alignment = randomize_alignment()
    race = randomize_race()
    char_class = randomize_class()
    print(f"Your character's alignment is: {alignment}")
    print(f"Your character's race is: {race}")
    print(f"Your character's class is: {char_class}")
