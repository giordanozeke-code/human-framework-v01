# Human Framework v0.1 — Technical Specification

Human Framework v0.1 is a high-level declarative language based on natural syntax, without parentheses or symbols. It is designed to describe interfaces and logic using human-readable keywords.

##  Core Keywords

- **create** — defines a new element
- **name** — assigns a readable identifier
- **color** — sets the element’s visual color
- **size** — sets the element’s size
- **position** — defines spatial placement
- **when** — opens an event block
- **action** — describes what happens in response to an event

## Element Construction Rules

After `create`, all following keywords belong to the same element
until another `create` or a `when` statement appears.
The order of internal keywords is free.

##  Supported Events

- **click** — triggered when the user presses and releases input
- **press** — triggered continuously while input is held
- **passing** — triggered when the pointer moves over an element
- **enter** — triggered when the user enters a logical area or panel

## SECTION X — Import Rules

Additional language rules and features will be defined in the following sections.
