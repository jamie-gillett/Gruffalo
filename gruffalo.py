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

formless_chunk = """
“Oh help! Oh no!
It's a gruffalo!”

“My favourite food!” the Guffalo said.
“You'll taste good on a slice of bread!”
“Good?” said the mouse. “Don't call me good!
I'm the scariest creature in this wood.
Just walk behind me and soon you'll see,
Everyone is afraid of me.”

“All right,” said the Gruffalo, bursting with laughter.
“You go ahead and I'll follow after.”"""

another_formless_chunk = """“Well, Gruffalo,” said the mouse. “You see?
Everyone is afraid of me!
But now my tummy's beginning to rumble.
My favourite food is -- gruffalo crumble!”

“Gruffalo crumble!” the Gruffalo said,
And quick as the wind he turned and fled.

All was quite in the deep dark wood.
The mouse found a nut and the nut was good.
"""

# ------ STORY TIME ------ #
print()
# MOUSE ENCOUNTERS ANIMALS
for animal in animals:
    print(f'{"A mouse took a stroll" if animal.name=="Fox" else "On went the mouse"} through the deep dark wood.')
    print(f'{"An" if animal.name=="Owl" else "A"} {animal.name.lower()} saw the mouse and the mouse looked good.')
    print('“Where are you going to, little brown mouse?')
    print(f'Come {"for" if animal.name=="Snake" else "and have"} {animal.meal} in my {animal.home} house.”')
    print()
    print(f"“It's {animal.compliment} of you, {animal.name}, but no --")
    print(f"I'm {'having' if animal.name=='Snake' else 'going to have'} {animal.meal} with a gruffalo.”")
    print("“A gruffalo? What's a gruffalo?”")
    print("“A gruffalo! Why, didn't you know?")
    print() # page break
    print(f'“{"His" if animal.name=="Snake" else "He has"} {animal.descriptions[0]}, {"his" if animal.name=="Snake" else "and"} {animal.descriptions[1]}{";" if animal.name=="Snake" else ","}')
    print(f'{"He has" if animal.name=="Snake" else "And"} {animal.descriptions[2]}.”')
    print('“Where are you meeting him?”')
    print(f'“Here, by {"these" if animal.name=="Fox" else "this"} {animal.meeting},')
    print(f'And his favourite food is {animal.fave_food.lower()}.”')
    print() # page break
    print("“{}! {}!{}".format(animal.fave_food, animal.exclamation, '” Fox said.' if animal.name=="Fox" else "")) # my poor f-string :/
    print('{}Goodbye, little mouse,” and away {} {}.'.format("“" if animal.name=="Fox" else "", "he" if animal.name=="Fox" else animal.name, animal.motion))
    print(f'“Silly old {animal.name}! Doesn\'t he know,')
    print('There\'s no such thing as a {}'.format('gruffal...' if animal.name=="Snake" else 'gruffalo?”'))
    print() # page break
print('...Oh!”')
print()

# MOUSE ENCOUNTERS THE GRUFFALO
for animal in animals:
    if animal.name == "Fox":
        print("But who is this creature with", end=" ")
    else:
        print(f"{'He has' if animal.name=='Owl' else 'His'} {animal.descriptions[0]}{' and' if animal.name=='Owl' else ', his'}", end= " ")
    print(f"{animal.descriptions[1]}{';' if animal.name=='Snake' else ''}")
    print(f"{'He has' if animal.name=='Snake' else 'And'} {animal.descriptions[2]}{'?' if animal.name=='Fox' else '.'}")
print(formless_chunk)

# ANIMALS ECOUNTER THE GRUFFALO
for animal in reversed(animals):
    print(f"They walked {'and walked' if animal.name=='Snake' else 'some more'} till the Guffalo said,")
    print(f"“I hear {animal.sound} {'on' if animal.name=='Fox' else 'in'} the {animal.location} ahead.”")
    print()
    print(f"“It's {animal.name},” said the mouse. “Why, {animal.name}, hello!”")
    print(f"{animal.name} took one look at the Gruffalo.")
    print(f"“Oh {animal.expletive}!” he said, “Goodbye, little mouse,”")
    print(f"And off he {'ran' if animal.name=='Fox' else animal.motion} to his {animal.home} house.")
    print()
    if animal.name=='Fox':
        continue
    print("“You see?” said the mouse. “I told you so.”")
    print(f"“{animal.reaction}!” said the Gruffalo.")

# FINALE
print(another_formless_chunk)