# Zusammenfassung - Part 1

Eine kleine Zusammenfassung von allem, was wir im ersten Teil unserer dreiteiligen Serie behandelt haben.

## Variablen
[Zum Bereich](variables.md)
* Variablen haben einen Namen und werden mit dem `=` Operater zugewießen. Example: `a = 10`
* Variablen haben Datentypen, die festlegen, welche Art von Werten sie enthalten.
* Datentype:
  * `string` for text
  * `int` for whole numbers
  * `boolean` for boolean(true/false)
  * `float` for floating point numbers
  * `None` for nothing

```python3
an_integer = 10
an_float = 50.0
text = "This is a text"
an_boolean = True
an_nothing = None
```

* Sie können Variablen zwischen verschiedener Datentypen konvertieren.

```python3
a = 10
a_as_text = str(a)
```
* Die Umrechnungsfunktionen sind
  * `str()` to convert to string
  * `bool()` to convert to boolean
  * `int()` to convert to integer
  * `float()` to convert to floating point number

## Schleifen
[Zum Bereich](loops.md)
* Wir können `for` Schleifen verwenden, um einen Vorgang mehrmals auszuführen

```python3
for a in range(0, 10):
  print("Iteration #" + str(a))
```
* Der angegebene Bereich schließt den Anfangspunkt ein und **schließt** die letzte Zahl aus.

## Bedingungen 
[Zum Bereich](loops.md)
* Wir können `if` Klauseln verwenden, um Bedingungen festzulegen
* Eine `if` Klausel enthält eine oder mehrere Bedingungen, die, wenn sie erfüllt sind, ausgeführt werden.
* Wir können zusätzliche Bedingungen haben (mit `elif`) nd eine Auffanglösung, die ausgeführt wird, wenn keine der Bedingungen erfüllt ist (mit `else`)

```python3
age = 10
if age == 12:
  print("Age is 12")
elif age == 15:
  print("Age is 15")
else:
  print("Age is something else")
```

| **Operator**  | **Description**                                   |
|---------------|---------------------------------------------------|
| `a == b`      | True if a is equal to b                           |
| `a > b`       | True if a is strictly greater than b              |
| `a >= b`      | True if a is greater or equal than b              |
| `a < b`       | True if a is strictly less than b                 |
| `a <= b`      | True if a is less of equal than b                 |
| `a % b == 0`  | True if a can be divided by b without a remainder |

## Funktionen
[Zum Bereich](functions.md)
* Funktionen ermöglichen die Kapselung von Code zur späteren Wiederverwendung

```python3
def my_function_name():
 print("Hello!")
```
 
 * Funktionen können ein oder mehrere Argumente haben
 
 ```python 3
 def my_function_name(argument_one, argument_two):
  print("Argument 1 is: " + str(argument_one))
  print("Argument 2 is: " + str(argument_two))  
```

* Funktionen können Informationen zurückgeben

```python3
def my_function(name):
 return "Hi my name is " + str(name)
```
