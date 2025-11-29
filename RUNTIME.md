# Human Framework — RUNTIME.md

The Runtime defines how a program written in the language is interpreted and transformed into executable behavior. This document describes the internal model an implementation must follow.

## 1. Execution Model

Human Framework uses a declarative, event-driven model.

- Elements are created with `create`
- Properties (`name`, `color`, `size`, `position`) populate the internal object tree
- Events (`click`, `press`, `passing`, `enter`) attach reactive behaviors to elements
- `action` describes what happens when an event is triggered

A script is not executed top-down.  
The runtime builds the structure first, then waits for events.

## 2. Object Tree

Every `create` statement generates a node in the internal tree.

Each node contains:
- an identifier
- a set of properties
- event handlers
- optional children (for future versions)

The object tree is the central representation of the UI and its behavior.

## 3. Event Propagation

Human Framework uses a simple and deterministic event model.

- An event targets the element it is attached to
- Events do not bubble unless added in future versions
- Each event directly triggers its associated `action`

Example:

`when click -> color red`

The runtime interprets this as:

“On click of this element, update its color property to red.”

## 4. Rendering Layer

The runtime does not require a specific rendering engine.

An implementation may target:
- HTML / CSS
- Canvas / WebGL
- Native UI systems
- Game engines
- Custom rendering layers

The runtime guarantees consistent event behavior and property updates, regardless of the rendering backend.

## 5. Error Handling

Human Framework uses predictable, human-oriented error rules.

- Unknown keywords → syntax error  
- Unknown properties → ignored for forward compatibility  
- Invalid actions → runtime warning (execution continues)  
- Invalid event names → runtime error (handler is not attached)

Errors should remain understandable and not cryptic compiler traces.

## 6. Determinism

Given the same script, the runtime must always produce:
- the same object tree  
- the same event bindings  
- the same behavior  

Determinism ensures predictability, testing, and cross-implementation compatibility.

## 7. Evolution Note

Future versions may extend:
- nesting of elements
- event bubbling
- dynamic element creation
- extended property types
- richer actions

This document defines the baseline for Human Framework v0.1.
