from dataclasses import dataclass

# ------ SET UP ------ #
@dataclass
class Animal:
    name: str
    meal: str
    home: str
    compliment: str
    descriptions: list[str]
    meeting: str
    fave_food: str
    exclamation: str
    motion: str

animals = [
    Animal("Fox", "lunch", "underground", "terribly kind", ["terrible tusks", "terrible claws", "terrible teeth in his terrible jaws"], "rocks", "Roasted fox", "I'm off", "sped"),
    Animal("Owl", "tea", "treetop", "frightfully nice", ["knobbly knees", "turned-out toes", "a poisonous wart at the end of his nose"], "stream", "Owl ice cream", "Toowhit toowhoo", "flew"),
    Animal("Snake", "a feast", "logpile", "wonderfully good", ["eyes are orange", "tongue is black", "purple prickles all over his back"], "lake", "Scrambled snake", "It's time I hid", "slid")
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
    print() # page break
    print(f'"{"His" if animal.name=="Snake" else "He has"} {animal.descriptions[0]}, {"his" if animal.name=="Snake" else "and"} {animal.descriptions[1]}{";" if animal.name=="Snake" else ","}')
    print(f'{"He has" if animal.name=="Snake" else "And"} {animal.descriptions[2]}."')
    print('"Where are you meeting him?"')
    print(f'"Here, by {"these" if animal.name=="Fox" else "this"} {animal.meeting},')
    print(f'And his favourite food is {animal.fave_food.lower()}."')
    print() # page break
    if animal.name=="Fox":
        print(f"\"{animal.fave_food}! {animal.exclamation}!\" Fox said.")
        print("\"", end='')
    else:
        print(f"\"{animal.fave_food}! {animal.exclamation}!")
    print(f'Goodbye, little mouse," and away {"he" if animal.name=="Fox" else animal.name} {animal.motion}.')
    print(f'"Silly old {animal.name}! Doesn\'t he know,')
    print(f'There\'s no such thing as a gruffal',end='')
    if animal.name=="Snake":
        print('...')
    else:
        print('o?"')
    print() # page break