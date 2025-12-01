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
- **print** - outputs a value during program execution

Note: when (global) — allows defining events not bound to a specific element. Global events run at program start or when the environment triggers         them.

## Action 

- **color Value** - Sets the color property of the active element. Errors if no active element exists.
- **print Value** - Outputs Value during program execution. Can be used globally (e.g., When run action print hello)

## Element Construction Rules

After `create`, all following keywords belong to the same element
until another `create` or a `when` statement appears.
The order of internal keywords is free.

## Special Element: _global

The parser automatically creates a special element named `_global`.
All `when` statements defined outside any `create` block are attached to `_global`.
Actions inside `_global` are executed at runtime based on global events (e.g., run).

A when placed outside an element is considered global and is assigned to the special _global element.

##  Supported Events

- **click** — triggered when the user presses and releases input
- **press** — triggered continuously while input is held
- **passing** — triggered when the pointer moves over an element
- **enter** — triggered when the user enters a logical area or panel
- **run** - global event executed at program start.
- Note: `run` can only be defined in the `_global` element.It is executed automatically when the program starts, before any element-related events.

## SECTION X — Import Rules

## Error Rules
Human Framework detects the following errors:

• Missing active element — using `color` or other property keywords outside of a `create` block raises an error.
• Unknown keywords — silently ignored for forward compatibility.
• Missing action target — actions referring to non-existent elements raise backend errors.


Additional language rules and features will be defined in the following sections.
