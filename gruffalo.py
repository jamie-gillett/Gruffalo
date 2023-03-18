from dataclasses import dataclass

@dataclass
class Animal:
    name: str
    meal: str
    home: str
    compliment: str
    # descriptions: list[str]
    # meeting: str
    # fave_food: str
    # exclamation: str
    # motion: str

animals = [
    Animal("Fox","lunch","underground","terribly kind"),
    Animal("Owl","tea","treetop","frightfully nice"),
    Animal("Snake","a feast","logpile","wonderfully good")
]

animals = ["Fox", "Owl", "Snake"]
meals = {"Fox": "lunch", "Owl": "tea", "Snake": "a feast"}
homes = {"Fox": "underground", "Owl": "treetop", "Snake": "logpile"}
compliment = {"Fox": "terribly kind", "Owl": "frightfully nice", "Snake": "wonderfully good"}

print()
for i, animal in enumerate(animals):
    print(f'{"A mouse took a stroll" if animal=="Fox" else "On went the mouse"} through the deep dark wood.')
    print(f'A{"n" if animal=="Owl" else ""} {animal.lower()} saw the mouse and the mouse looked good.')
    print('"Where are you going to, little brown mouse?')
    print(f'Come {"for" if animal=="Snake" else "and have"} {meals[animal]} in my {homes[animal]} house."')
    print(f"\"It's {compliment[animal]} of you, {animal}, but no --")
    print(f"I'm {'having' if animal=='Snake' else 'going to have'} {meals[animal]} with a gruffalo.\"")
    print("\"A gruffalo? What's a gruffalo?\"")
    print("\"A gruffalo! Why, didn't you know?")
    print()