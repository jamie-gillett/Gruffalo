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
    sound: str
    location: str
    expletive: str
    reaction: str

animals = [
    Animal("Fox", "lunch", "underground", "terribly kind", ["terrible tusks", "terrible claws", "terrible teeth in his terrible jaws"], "rocks", "Roasted fox", "I'm off", "sped", "feet", "path", "help", None),
    Animal("Owl", "tea", "treetop", "frightfully nice", ["knobbly knees", "turned-out toes", "a poisonous wart at the end of his nose"], "stream", "Owl ice cream", "Toowhit toowhoo", "flew", "a hoot", "trees", "dear", "Astounding"),
    Animal("Snake", "a feast", "logpile", "wonderfully good", ["eyes are orange", "tongue is black", "purple prickles all over his back"], "lake", "Scrambled snake", "It's time I hid", "slid", "a hiss", "leaves", "crumbs", "Amazing")
]

# ------ STORY TIME ------ #
print()
# MOUSE ENCOUNTERS ANIMALS
for animal in animals:
    print(f'{"A mouse took a stroll" if animal.name=="Fox" else "On went the mouse"} through the deep dark wood.')
    print(f'{"An" if animal.name=="Owl" else "A"} {animal.name.lower()} saw the mouse and the mouse looked good.')
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

# MOUSE ENCOUNTERS THE GRUFFALO
for animal in animals:
    if animal.name == "Fox":
        print("But who is this creature with", end=" ")
    else:
        print(f"{'He has' if animal.name=='Owl' else 'His'} {animal.descriptions[0]}{' and' if animal.name=='Owl' else ', his'}", end= " ")
    print(f"{animal.descriptions[1]}{';' if animal.name=='Snake' else ''}")
    print(f"{'He has' if animal.name=='Snake' else 'And'} {animal.descriptions[2]}{'?' if animal.name=='Fox' else '.'}")
formless_chunk = """
\u201COh help! Oh no!
It's a gruffalo!\u201D

\u201CMy favourite food!\u201D the Guffalo said.
\u201CYou'll taste good on a slice of bread!\u201D
\u201CGood?\u201D said the mouse. \u201CDon't call me good!
I'm the scariest creature in this wood.
Just walk behind me and soon you'll see,
Everyone is afraid of me.\u201D

\u201CAll right,\u201D said the Gruffalo, bursting with laughter.
\u201CYou go ahead and I'll follow after.\u201D"""
print(formless_chunk)

# ANIMALS ECOUNTER THE GRUFFALO
for animal in reversed(animals):
    print(f"They walked {'and walked' if animal.name=='Snake' else 'some more'} till the Guffalo said,")
    print(f"\u201CI hear {animal.sound} {'on' if animal.name=='Fox' else 'in'} the {animal.location} ahead.\u201D")
    print()
    print(f"\u201CIt's {animal.name},\u201D said the mouse. \u201CWhy, {animal.name}, hello!\u201D")
    print(f"{animal.name} took one look at the Gruffalo.")
    print(f"\u201COh {animal.expletive}!\u201D he said, \u201CGoodbye, little mouse,\u201D")
    print(f"And off he {'ran' if animal.name=='Fox' else animal.motion} to his {animal.home} house.")
    print()
    if animal.name=='Fox':
        continue
    print("\u201CYou see?\u201D said the mouse. \u201CI told you so.\u201D")
    print(f"\u201C{animal.reaction}!\u201D said the Gruffalo.")

# FINALE
another_formless_chunk="""\u201CWell, Gruffalo,\u201D said the mouse. \u201CYou see?
Everyone is afraid of me!
But now my tummy's beginning to rumble.
My favourite food is -- gruffalo crumble!\u201D

\u201CGruffalo crumble!\u201D the Gruffalo said,
And quick as the wind he turned and fled.

All was quite in the deep dark wood.
The mouse found a nut and the nut was good.
"""
print(another_formless_chunk)
