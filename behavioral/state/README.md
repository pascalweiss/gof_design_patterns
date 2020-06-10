### Pattern Name
State

#### Intent
"Allow an object to alter its behavior when its internal state changes.
The object will appear to change its class." (GoF)

#### Also Known As
Objects for States

#### Motivation
In this example, the State pattern is applied on a gate. The gate may be used at the entry of a
concert hall or a cinema. To control if a guest is authorised to enter, the guest has to show
the barcode on his ticket to a scanner.
Here the gate is represented as the following finite state machine:

```
(Q, Σ, T, q0, F)
States:         Q = (open, closed)
Actions:        Σ = (entered, valid)
initial state: q0 = closed
Transitions     F = {
    (open, entered) -> closed,
    (open, valid)   -> valid,
    (closed, entered) -> closed,
    (closed, valid)   -> open
}
```