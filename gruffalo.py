from dataclasses import dataclass

# ------ SET UP ------ #
@dataclass
class Animal:
    name: str
    meal: str
    home: str
    compliment: str
    descriptions: list[str]
    # meeting: str
    # fave_food: str
    # exclamation: str
    # motion: str

animals = [
    Animal("Fox", "lunch", "underground", "terribly kind", ["terrible tusks", "terrible claws", "terrible teeth in his terrible jaws"]),
    Animal("Owl", "tea", "treetop", "frightfully nice", ["knobbly knees", "turned-out toes", "a poisonous wart at the end of his nose"]),
    Animal("Snake", "a feast", "logpile", "wonderfully good", ["eyes are orange", "tongue is black", "purple prickles all over his back"])
]

# ------ STORY TIME ------ #
print() # First encounters
for animal in animals:
    print(f'{"A mouse took a stroll" if animal.name=="Fox" else "On went the mouse"} through the deep dark wood.')
    print(f'A{"n" if animal.name=="Owl" else ""} {animal.name.lower()} saw the mouse and the mouse looked good.')
    print('"Where are you going to, little brown mouse?')
    print(f'Come {"for" if animal.name=="Snake" else "and have"} {animal.meal} in my {animal.home} house."')
    print(f"\"It's {animal.compliment} of you, {animal.name}, but no --")
    print(f"I'm {'having' if animal.name=='Snake' else 'going to have'} {animal.meal} with a gruffalo.\"")
    print("\"A gruffalo? What's a gruffalo?\"")
    print("\"A gruffalo! Why, didn't you know?")
    # if not animal.name == "Snake":
    #     print(f'"He has {animal.descriptions[0]}, and {animal.descriptions[1]},')
    #     print(f'And {animal.descriptions[2]}."')
    # else:
    #     print(f'"His {animal.descriptions[0]}, his {animal.descriptions[1]};')
    #     print(f'He has {animal.descriptions[2]}."')
    print(f'"{"He has" if not animal.name=="Snake" else "His"} {animal.descriptions[0]}, {"and" if not animal.name=="Snake" else "his"} {animal.descriptions[1]}{"," if not animal.name=="Snake" else ";"}')
    print(f'{"And" if not animal.name=="Snake" else "He has"} {animal.descriptions[2]}."')
    print()