# Variablen und Datentypen
Variablen sind eines der wichtigsten Elemente bei der Programmierung. 
Variablen verhalten sich wie ein Platzhalter bzw. ein Speicher für einen 
Wert. Und bestehen immer aus einem Namen, der einen Wert beinhalten kann.

Erstellen einer Variable und prüfen mit print:
```python
a = 4
b = "Hello"
print(a)
print(b)
```
Damit haben wir erste Variablen initialisiert und ausgegeben! 

## Datentypen
Wir können verschiedene Werte in Variablen abbilden z.B. eine Zahl oder einen Text.
Python kennt vier einfache Basis Datentypen:
* `string` für Texte
* `int` für ganze Zahlen
* `float` für Dezimalzahlen
* `None` für "nichts"

### Strings
Ein String ist ein Text. Texte müssen in Anführungszeichen stehen:
```python
text_1 = "Ich bin ein Text."
text_2 = 'Ich bin auch ein Text.'
```

Strings lassen einfach verbinden, dazu wir das + Zeichen genutzt. Um ein Leerzeichen zwischen den beiden Elemente zu haben wird ein `" "` ein Leerzeichen in Anführungszeichen mit eingebunden:
```python
text_1 = "Ich bin ein Text."
text_2 = 'Ich bin auch ein Text.'
text_3 = text_1 + " " + text_2
print(text_3)
```

> :computer: Aufgabe: ändere das Skript so, dass dein Name ausgegeben wird:
> ```python3
> # Hier muss Code ergänzt werden
> print("Hello " + your_name)
> ```

<details>
  <summary>Lösung</summary>

  ```python
  your_name = "Sebastian"
  print("Hello " + your_name)
  ```
</details>

### Integers
Integers sind ganze Zahlen. Hier wird kein Anführungszeichen benötigt.
```python
a = 10
b = 5
```

Mit Zahlen können wir Rechnen
```python
a = 10
b = a * 5  # b ist 50
c = 10
d = b - c  # d ist 40
```

Wir können auch mit den eigenen Werten rechnen bzw. Werte überschreiben:
```python
a = 5
a = a + 5  # a ist 10
a = a * 2  # a ist 20
a = a - 5  # a ist 15
```

> :computer: Aufgabe: löse die folgende Aufgabe mit Python:
* Erstelle Variable `a` mit dem Wert 10
* Erstelle Variable `b` mit dem Wert 2
* Erstelle Variable `c` mit dem Wert aus der Multiplikation von `a` und `b`
* Füge 10 zur Variable `c` hinzu
* Multipliziere `c` mit sich selbst
* Gib das Ergebnis von `c` aus

<details>
  <summary>Lösung</summary>

  ```python
  a = 10
  b = 2
  c = a * b
  c = c + 10
  c = c * c
  print(c)
  ```
</details>

### Floats
Floats sind die Ergänzung zu Integers. Der Unterschied ist, ein Float muss keine ganze Zahl sein. Als Trennzeichen wird ein `.` verwendet. Hier wird ebenfalls kein Anführungszeichen benötigt.
```python
a = 10.5
b = 5
c = b / 2.5
```

### None
None ist ein weiterer Datentyp der "nichts" repräsentiert.
```python
a = None
```

### Converting between data types
In Python muss oft zwischen verschiedenen Datentypen gewechselt werden. Zum Beispiel beim verwenden von `print`. Wenn wir einen Text und eine Zahl ausgeben wollen, muss die Zahl in einen String umgewandelt werden.
```python
a = 10
b = str(a)  # converts int --> string
c = float(a)  # converts int --> float
```

Mit der type Funktion können wir uns den Datentyp einer Varbiable anzeigen lassen:
```python
a = 10
b = 'Hello World'
print('Var a is a ' + type(a))
print('Var b is a ' + type(b))
```

> :warning: Beim umwandelnt eines `float` in ein `int` wird nicht gerundet, es wird nur die Kommastelle abgeschnitten.

Um eine Zahl zu Runden, gibt es die Funktion `round`. Ohne Paramater wird auf 0-Stellen gerundet, mit Parameter kann angegeben werden auf wie viel Stellen gerundet werden soll:
```python
a = 4.6
b = 4.21354
c = round(a)
d = round(b, 1)
```

Es kann nicht alles umgewandelt werden, einen Text in eine Integer führt entsprechend zu einem `ValueError` Fehler.
```python
text = "I am a text"
number = int(text)
```

<div align="right">
   
   [Zurück](Readme.md) - [Weiter](loops.md)
</div>

