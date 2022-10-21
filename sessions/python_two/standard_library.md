# Python Bibliotheken - Library
Python hat bereits viele Module an Bord, wenn jedoch komplexere Anwendungen geschrieben werden, kommt man schnell an den Punkt wo weitere Funktionen benötigt werden. Diese lassen sich importieren.

## Modul importieren und verwenden
Um ein Modul zu importieren wird der Befehl `import` verwendet. Üblicherweiße werden alle Imports ganz oben im Code ausgeführt.

```python
import random
```

Mit dem Modul random, kann zum Beispiel eine Zufallszahl erstellt werden. Anschließend wird im Code das Modul aufzurufen, nach einem Punkt, wird die gewünschte Funktion aus dem Modul geladen. Hier ist die jeweilige Dokumentation hilfreich.
```python
import random
a = random.random()  # zufällige Kommazahl
b = random.randint(0, 10)  # zufällige int Zahl zwischen Wert 1 und Wert 2.

print(a)
print(b)
```

Es kann auch nur eine Funktion aus einem Modul geladen werden:
```python
from random import randint
b = randint(0, 10)
print(b)
```

Ebenso kann ein Modul unter einem anderen Namen geladen werden:
````python
import random as r
b = r.randint(0, 10)
print(b)
````

<div align="right">
   
   [Zurück](/sessions/python_one/Readme.md) - [Weiter](json.md)
</div>


