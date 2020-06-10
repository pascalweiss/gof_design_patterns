### Prototype

#### Intent
Specify the kinds of objects to create using a prototypical instance, and create new objects
by copying the prototype.

#### Motivation
Suppose we are building a graph editor and we want to implement the new feature "duplicate shape".
When the user applies "duplicate shape", the editor will take the currently selected shape
and duplicate it by creating a new shape of the same type with the same properties.
