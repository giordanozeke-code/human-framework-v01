# Human Framework — STANDARD-LIB.md

This document lists all official keywords and behaviors included in Human Framework v0.2.
Only these constructs are guaranteed to exist in the language.
Future versions may extend the standard library but will not break the behavior defined here.

SECTION 1 — Element Creation Keywords

**create**
-Creates a new UI element. It begins a new element block.

**name**
-Assigns a readable identifier to the element.
-Names should be unique inside the same logical scope.

**color**
-Sets the visual color of the element.
-Future versions may extend the color set.

**size**
-Sets the general dimension of the element.

**position**
-Defines the placement of the element.

Examples:
-position center
-position inside card top

##SECTION 2 — Events

Human Framework v0.2 supports five event types.

**click**
-Triggered when the user presses and releases on the element.

**press**
-Triggered continuously while the user holds an input (for example a mouse button or key).

**passing**
-Triggered while the pointer stays inside the element’s region.
-Behaves like a hover-style interaction.

**enter**
-Triggered when the user enters a logical area or panel.
-It fires on entry, not continuously.

**run**
-global event executed at program start.
  It can only be defined inside the _global element.

##Section 3 - Action
**color** -applies a color to an element
**print** -outputs a value during execution

##SECTION 4 — Action Syntax

Human Framework v0.2 uses a compact event to action syntax:

-when EVENT action PROPERTY VALUE


SECTION 5 — Properties Supported in v0.2

The following properties are officially supported:

**name**      — logical identifier of the element
**color**     — visual color from the standard color set
**size**      — small, medium, large
**position**  — spatial placement relative to the layout or another element

Any other property name is ignored by the runtime in v0.1 but may become valid in future versions.

SECTION 6 — Reserved Words

The following words are reserved by Human Framework v0.2 and should not be used as names:

-**create**
-**name**
-**color**
-**size**
-**position**
-**when**
-**action**
-**click**
-**press**
-**passing**
-**enter**
-**run**
-**print**

##SECTION 7 — Version Note

This standard library definition applies to Human Framework v0.2.
Later versions may add:
- new properties
- new events
- new element types
- new action forms

All changes will be appended to this document without breaking existing scripts.
