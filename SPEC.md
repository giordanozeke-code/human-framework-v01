# Human Framework v0.2 — Technical Specification

Human Framework v0.2 is a high-level declarative language based on natural syntax, without parentheses or symbols. It is designed to describe interfaces and logic using human-readable keywords.

##  Core Keywords

- **create** — defines a new element
- **name** — assigns a readable identifier
- **color** — sets the element’s visual color
- **size** — sets the element’s size
- **position** — defines spatial placement
- **when** — opens an event block
- **action** — attaches a concrete action to an event. Actions trigger backend logic (e.g. print output, apply color, etc.).

Note: the keyword `action` has no functional role in v0.1; it is a purely visual-semantic indicator used to make event lines more readable. It does       not change interpretation, execution, or behavior.

Note: when (global) — allows defining events not bound to a specific element. Global events run at program start or when the environment triggers         them.


## Action 

- **color Value** - Sets the color property of the active element. Errors if no active element exists.
- **print Value** - Outputs Value during program execution. Can be used globally (e.g., When run action print hello)


## Element Construction Rules

After `create`, all following keywords belong to the same element
until another `create` or a `when` statement appears.
The order of internal keywords is free.

A when placed outside an element is considered global and is assigned to the special _global element.

##  Supported Events

- **click** — triggered when the user presses and releases input
- **press** — triggered continuously while input is held
- **passing** — triggered when the pointer moves over an element
- **enter** — triggered when the user enters a logical area or panel
- **run** - global event executed at program start.


## SECTION X — Import Rules

Additional language rules and features will be defined in the following sections.
