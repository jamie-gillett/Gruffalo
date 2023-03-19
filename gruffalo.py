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
print()
# FIRST ANIMAL ENCOUNTERS
for animal in animals:
    print(f'{"A mouse took a stroll" if animal.name=="Fox" else "On went the mouse"} through the deep dark wood.')
    print(f'A{"n" if animal.name=="Owl" else ""} {animal.name.lower()} saw the mouse and the mouse looked good.')
    print('\u201CWhere are you going to, little brown mouse?')
    print(f'Come {"for" if animal.name=="Snake" else "and have"} {animal.meal} in my {animal.home} house.\u201D')
    print()
    print(f"\u201CIt's {animal.compliment} of you, {animal.name}, but no --")
    print(f"I'm {'having' if animal.name=='Snake' else 'going to have'} {animal.meal} with a gruffalo.\u201D")
    print("\u201CA gruffalo? What's a gruffalo?\u201D")
    print("\u201CA gruffalo! Why, didn't you know?")
    print() # page break
    print(f'\u201C{"His" if animal.name=="Snake" else "He has"} {animal.descriptions[0]}, {"his" if animal.name=="Snake" else "and"} {animal.descriptions[1]}{";" if animal.name=="Snake" else ","}')
    print(f'{"He has" if animal.name=="Snake" else "And"} {animal.descriptions[2]}.\u201D')
    print('\u201CWhere are you meeting him?\u201D')
    print(f'\u201CHere, by {"these" if animal.name=="Fox" else "this"} {animal.meeting},')
    print(f'And his favourite food is {animal.fave_food.lower()}.\u201D')
    print() # page break
    print("\u201C{}! {}!{}".format(animal.fave_food, animal.exclamation, '\u201D Fox said.' if animal.name=="Fox" else "")) # my poor f-string :/
    print('{}Goodbye, little mouse,\u201D and away {} {}.'.format("\u201C" if animal.name=="Fox" else "", "he" if animal.name=="Fox" else animal.name, animal.motion))
    print(f'\u201CSilly old {animal.name}! Doesn\'t he know,')
    print('There\'s no such thing as a gruffal{}'.format('...' if animal.name=="Snake" else 'o?\u201D'))
    print() # page break
print('...Oh!\u201D')
print()
