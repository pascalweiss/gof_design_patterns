### Adapter

#### Intent
"Convert the interface of a class into another interface clients expect. Adapter lets
classes work together that couldn't otherwise because of incompatible interfaces." (GoF)

#### Also Known As
Wrapper

#### Motivation
The user has to apply the function target_invoker put can't change it. It requires an argument of type
InvokerTarget. But the target that the user actually wants use is of type UserTarget. The problem is, that
UserTarget is not compatible with target_invoker.
