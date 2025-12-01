EXAMPLES.txt — Human Framework v0.2

This document provides examples showing how to write programs in Human Framework v0.1.


------------------------------------------------------------
SECTION 1 — Basic Element
------------------------------------------------------------

create
name button-login
color red
size medium
position center

Meaning: a blue button named “button-login” centered on screen.


------------------------------------------------------------
SECTION 2 — Simple Interaction
------------------------------------------------------------

create
name light
color white

when click action color yellow

Meaning: clicking the element turns it yellow.


------------------------------------------------------------
SECTION 3 — Passing Event (hover-like)
------------------------------------------------------------

create
name menu-item
color grey

when passing action color white

Meaning: pointer passing over the element changes its color.


------------------------------------------------------------
SECTION 4 — Enter Event
------------------------------------------------------------

create
name welcome-area
color dark

when enter action color light

Meaning: entering this area changes its color.


------------------------------------------------------------
SECTION 5 — Press Event (continuous input)
------------------------------------------------------------

create
name security-button
color red

when press action size large

Meaning: pressing enlarges the element.


------------------------------------------------------------
SECTION 6 — Multiple Events
------------------------------------------------------------

create
name interactive-box
color grey
size medium

when passing action color lightgrey
when click action color green
when press action size large

Meaning: the element reacts differently to each input.


------------------------------------------------------------
SECTION 7 — Mini UI Example
------------------------------------------------------------

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

when passing action color darkgrey
when click action color red

Meaning: a card with a title that changes color based on interaction.
