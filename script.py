import random
from faker import Faker

# Initialize Faker
fake = Faker("en_US")


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


def randomize_gender():
    genders = ["Male", "Female"]
    return random.choice(genders)


def randomize_race():
    races_and_subraces = {
        "Dragonborn": [],
        "Drow": ["Lolth-Sworn", "Seldarine"],
        "Dwarf": ["Gold", "Shield", "Duergar"],
        "Elf": ["High", "Wood"],
        "Githyanki": [],
        "Gnome": ["Rock", "Deep", "Forest"],
        "Half-Elf": ["High", "Wood", "Drow"],
        "Half-Orc": [],
        "Halfling": ["Lightfoot", "Strongheart"],
        "Human": [],
        "Tiefling": ["Asmodeus", "Mephistopheles", "Zariel"],
    }

    chosen_race = random.choice(list(races_and_subraces.keys()))
    chosen_subrace = (
        random.choice(races_and_subraces[chosen_race])
        if races_and_subraces[chosen_race]
        else None
    )
    return chosen_race if not chosen_subrace else f"{chosen_race} ({chosen_subrace})"


def randomize_class_and_subclass():
    classes_and_subclasses = {
        "Barbarian": ["Berserker", "Wildheart", "Wild Magic"],
        "Bard": ["College of Lore", "College of Swords", "College of Valor"],
        "Cleric": [
            "Knowledge Domain",
            "Life Domain",
            "Light Domain",
            "Nature Domain",
            "Tempest Domain",
            "Trickery Domain",
            "War Domain",
        ],
        "Druid": ["Circle of the Land", "Circle of the Moon", "Circle of Spores"],
        "Fighter": ["Battle Master", "Champion", "Eldritch Knight"],
        "Monk": ["Way of the Four Elements", "Way of the Open Hand", "Way of Shadow"],
        "Paladin": [
            "Oath of the Ancients",
            "Oath of Devotion",
            "Oath of Vengeance",
            "Oathbreaker",
        ],
        "Ranger": ["Beast Master", "Gloom Stalker", "Hunter"],
        "Rogue": ["Arcane Trickster", "Assassin", "Thief"],
        "Sorcerer": ["Draconic Bloodline", "Storm Sorcery", "Wild Magic"],
        "Warlock": ["The Archfey", "The Fiend", "The Great Old One"],
        "Wizard": [
            "School of Abjuration",
            "School of Conjuration",
            "School of Divination",
            "School of Enchantment",
            "School of Evocation",
            "School of Illusion",
            "School of Necromancy",
            "School of Transmutation",
        ],
    }

    chosen_class = random.choice(list(classes_and_subclasses.keys()))
    chosen_subclass = random.choice(classes_and_subclasses[chosen_class])
    return chosen_class, chosen_subclass


def randomize_name():
    gender = randomize_gender()
    first_name = (
        fake.first_name_male() if gender == "Male" else fake.first_name_female()
    )
    last_name = fake.last_name()
    return f"{first_name} {last_name}", gender


def generate_character(is_dark_urge=False):
    name, gender = randomize_name()
    char_class, subclass = randomize_class_and_subclass()
    return {
        "Name": name,
        "Gender": gender,
        "Alignment": randomize_alignment(),
        "Race": randomize_race(),
        "Class": char_class,
        "Subclass": subclass,
        "Background": "Haunted One" if is_dark_urge else randomize_background(),
    }


if __name__ == "__main__":
    # Set is_dark_urge to True for a Dark Urge playthrough
    character = generate_character(is_dark_urge=True)
    print("Your randomized character:")
    print(character)
