### Bridge

#### Intent
"Decouple an abstraction from its implementation so that the two can vary independently." (GoF)

#### Also Known As
Handle/Body

#### Motivation
In this example the abstraction is a document. There are various document types, each represented as a
subclass (Letter, Article, WikiPage) of the Document class. The Document class uses the implementor class
Renderer for rendering. The Renderer class has various subclasses (Web, Paper, Audio) as well. Each can
be used for rendering the document into the target format of the corresponding renderer implementation.
By applying the bridge pattern, any document can be combined with any renderer. Like in a cartesian product.
The abstraction interface and the implementor interface act as a bridge between concrete abstractions and
concrete implementors.
