# JSON

JSON steht für *JavaScript Object Notation* und ist ein beliebtes textbasiertes Austauschformat. Schauen wir uns zunächst an, wie wir JSON in Python lesen und schreiben können.

Zuerst müssen wir das Modul `json` importieren. Dieses Modul ist Teil der Standardbibliothek, braucht also nicht zu installiert werden.

```python3
import json
```

## Umwandlung eines Python-Dict in ein json

Zunächst benötigen wir ein Python-Wörterbuch, das wir dann in einen json-String umwandeln können. Dann rufen wir die Funktion `json.dumps()` auf. 

```python3
import json

d = {}

d["first_name"] = "Marcel"
d["last_name"] = "Neidinger"
d["mail"] = "mneiding@cisco.com"

string_representation = json.dumps(d)
print(string_representation)
```

`json.dumps()` nimmt ein Python Dict und gibt es in eine Zeichenkette aus.

## Umwandlung eines json-Strings in ein Python Dict

Wir können auch den umgekehrten Weg gehen und einen (korrekt formatierten) json-String in ein Python Dict umwandeln. 

```python3
import json

json_str = """
{"first_name": "Marcel", "last_name": "Neidinger", "mail": "mneiding@cisco.com"}
"""

d = json.loads(json_str)

print(str(d))
```

> :computer: Schreiben Sie ein Skript, das das json-Modul importiert und ein Wörterbuch als String speichert. Das Wörterbuch soll den Vornamen (dictionary key: `first_name`), Nachnamen (dictionary key: `last_name`) und Alter (dictionary key: `age`) einer Person enthalten. Der Vor- und Nachname sollte zufällig aus einer Namensliste gezogen werden, während das Alter eine zufällige Ganzzahl im Bereich von 18 bis 99 sein sollte.
> 
> Die Liste der Vor- und Nachnamen findest du im folgenden Code-Beispiel
> 
> ```python3
> #ToDo: imports
>
> first_names = ["Nadja", "Nick", "Lucy", "Howie", "Sandy", "AJ", "Vanessa", "Brian", "Jessica", "Kevin"]
> last_names = ["Smith", "Johnson", "Brown", "Miller", "Garcia", "Acors", "Alday"]
> 
> # ToDo: Create dictionary
> 
> # ToDo: populate dictionary with information
> 
> # ToDo: Get a json representation of the dictionary using the json module
> string_representation = ?
> 
> print(string_representation)
> ```

<details>
  <summary>Lösung</summary>
  
  ```python3
  import random 
  import json

  first_names = ["Nadja", "Nick", "Lucy", "Howie", "Sandy", "AJ", "Vanessa", "Brian", "Jessica", "Kevin"]
  last_names = ["Smith", "Johnson", "Brown", "Miller", "Garcia", "Acors", "Alday"]

  d = {}

  d["first_name"] = random.choice(first_names)
  d["last_name"] = random.choice(last_names)
  d["age"] = random.randint(18, 99)

  string_representation = json.dumps(d)

  print(string_representation)
  ```
</details>

Damit haben wir zwei Module der Standardbibliothek behandelt.

<div align="right">
   
   [Zurück](standard_library.md) - [Weiter](/sessions/rest_fundamentals/Readme.md)
</div>