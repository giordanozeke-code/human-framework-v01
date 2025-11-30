# Human Framework — Interpreter v0.1

This folder contains the reference implementation of the Human Framework v0.1 interpreter.
The interpreter is made of two main files:

- human_parser.py  → parses .se source files
- human_backend.py → simple backend used to load elements and simulate events

This version is a minimal demonstration to show how the language works internally.

------------------------------------------------------------
SECTION 1 — Folder Contents
------------------------------------------------------------

human_parser.py  
    Defines the HumanParser class.
    Reads a .se file, processes each line, and builds a list of elements
    with properties (name, color, size, position) and events (when + action).

human_backend.py  
    Defines the HumanBackend class.
    Loads the parsed tree, initializes the internal state, and allows
    event simulation (click, press, passing, enter) applying the action rules.

prova.se (optional)  
    Example source file used for basic testing.

------------------------------------------------------------
SECTION 2 — Running a .se File
------------------------------------------------------------

To run a .se file through the interpreter:

1. Open the terminal inside the interpreter/ folder  
2. Execute:

   python human_backend.py filename.se

Example:

   python human_backend.py prova.se

The backend will print the initial state of all parsed elements.

------------------------------------------------------------
SECTION 3 — Interactive Usage (Python REPL)
------------------------------------------------------------

You can also use the interpreter interactively:

1. Open the terminal inside the interpreter/ folder  
2. Type:  python  
3. At the >>> prompt:

   from human_backend import HumanBackend
   b = HumanBackend()
   b.load("prova.se")

   b.simulate_event("box", "click")
   b.simulate_event("menu", "enter")

   b.print_state()

This will show the event simulation and the final state of each element.

------------------------------------------------------------
SECTION 4 — Project Status
------------------------------------------------------------

This is the first official implementation of the Human Framework v0.1 interpreter.

It currently supports:
- stable parsing of: create, name, color, size, position, when, action
- event handling for: click, press, passing, enter
- a test backend that updates element properties according to action rules

Future versions may add:
- HTML or GUI renderers
- new properties and events
- official development tools
- more advanced runtime features

------------------------------------------------------------
SECTION 5 — License
------------------------------------------------------------

This interpreter follows the same MIT license as the rest of the Human Framework project.
Contributions to improve the parser or backend are welcome through pull requests.
