### GoF - Design Patterns 
This repository provides a collection of examples for GoF design patterns. While the patterns can be applied in every 
object oriented language, here they are implemented in python. 

I hope somebody finds this repo useful. For me, it was a great practice to implement them.

### Usage
While this repository is more like a reading resource, you can execute every example with 
```
python3 -m unittest <path-of-pattern>/test_client.py
```
You can execute all examples with 
```
./run_all_tests.sh
```

### Structure
- Like in the book the patterns are categorized as creational, structural or behavioral. 
- The files are named according to the corresponding pattern-"participant" in the book.
- The class names correspond to the respective example.
- The application of each pattern is implemented in a test class `test_client.py`. 

### Additional notes
The patterns were collected and described by Erich Gamma, Richard Helm, 
Ralph Johnson and John Vlissides - the Gang of Four - in their iconic book [Design Patterns: Elements of Object-Oriented Software](). 
If you don't have the book, get it. 
