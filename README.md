# BG3 Randomizer

A Python script to generate randomized Baldur's Gate 3 character concepts, including class, subclass (with Patch 8 support), race, gender, alignment, background, and a unique name. The script also generates a creative writing prompt for a character backstory, blending the styles of two famous fantasy authors.

## Features
- Supports all classes and subclasses, including 12 new subclasses from Patch 8 (April 2025)
- Randomizes race (with subraces), gender, alignment, background, and name
- Option to generate a Dark Urge character
- Outputs a detailed prompt for writing a character backstory

## Requirements
- Python 3.7+
- [Faker](https://pypi.org/project/Faker/) library

Install dependencies:
```
pip install -r requirements.txt
```

## Usage
Run the script from the command line:
```
python script.py
```
To generate a Dark Urge character:
```
python script.py dark_urge
```

## Customization
- Edit `script.py` to add or modify races, subclasses, or backgrounds.
- Update `new_subclasses.md` for details on Patch 8 subclasses.

## Patch 8 Subclasses
See [new_subclasses.md](new_subclasses.md) for a summary of the new subclasses added in Patch 8.

## License
MIT License
