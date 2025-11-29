tutorial = """# Human Framework — TUTORIAL.md

This tutorial introduces Human Framework v0.1 and explains how to write your first programs using the language.  
It is designed for complete beginners and requires no programming background.

SECTION 1 — What Human Framework Is
Human Framework is a human-readable, declarative language meant to describe UI elements and simple logic using natural words.  
There are no parentheses, no symbols, and no complex structures.  
Everything is expressed through readable keywords.

SECTION 2 — Creating Your First Element
Every interface begins with the keyword:

create
name title
color black
size medium
position top

Meaning: this defines a simple element named "title" that appears at the top of the layout.

SECTION 3 — Reacting to User Input
Human Framework enables interaction through events.  
Every event starts with the keyword "when".

Example:

create
name button-start
color blue
size medium

when click -> color green

Meaning: when the user clicks the element, its color changes to green.

SECTION 4 — Hover-Like Behavior With Passing
"passing" triggers when the pointer moves over an element.

Example:

create
name menu-item
color grey

when passing -> color white

Meaning: when the cursor moves over the element, the element becomes white.

SECTION 5 — Entering Logical Areas
The "enter" event activates when the user enters a logical area or a panel.

Example:

create
name welcome-area
color dark

when enter -> color light

Meaning: entering this area changes its color.

SECTION 6 — Continuous Press
The "press" event repeats while the user holds input.

Example:

create
name hold-button
color red

when press -> size large

Meaning: holding the button enlarges the element.

SECTION 7 — Combining Elements
A simple interface may contain multiple elements and interactions.

Example:

create
name card
color white
size large
position center

create
name card-title
color black
size small
position inside card top

when passing -> color darkgrey
when click -> color red

Meaning: the card shows a title that reacts to hover and click events.

SECTION 8 — What Happens Internally
Behind the scenes, Human Framework builds:
- an object tree
- event bindings
- reactive behaviors

The runtime waits for user input and applies property changes whenever events occur.

SECTION 9 — Writing Clean Scripts
Keep your scripts readable:
- one property per line
- event lines separated from element blocks
- avoid long names
- keep behavior simple and clear

SECTION 10 — Version Note
This tutorial describes Human Framework v0.1.  
Future versions may introduce new properties, events, nesting, and richer interactions."""

path = "/mnt/data/TUTORIAL.txt"
with open(path, "w", encoding="utf-8") as f:
    f.write(tutorial)

path
