# Schleifen und Kontrollstrukturen

Das Schreiben von Operationen, Zeile für Zeile ist in Ordnung, aber was ist, wenn wir dieselbe Operation mehrmals ausführen wollen? Nehmen wir an, wir wollen den Satz "Hallo aus Python" fünfmal ausgeben. Wir könnten es so machen:

```python3
print("Hello from python")
print("Hello from python")
print("Hello from python")
print("Hello from python")
print("Hello from python")
```

Effektiv ist dies nicht.

Um dieses hier effektiver und einfacher zu sein, haben Python und alle anderen Programmiersprachen das Konzept der *Schleifen*. Schauen wir uns zunächst die *for-Schleifen* an.

## For Schleifen

Eine `for Schleife` ermöglicht es uns, eine oder mehrere Anweisungen, öfter auszuführen. Um das Beispiel von oben zu nehmen:
```python3
for a in range(0, 5):
    print("Hello from python")
```

Hier gibt es einige Dinge zu beachten:
* wir verwenden das Schlüsselwort `for` um anzugeben, dass es sich um eine *for loop* handelt.
* wir verwenden die `range(start, end)` Funktion, um die Anzahl der Durchläufe für die diese Schleife festzulegen. 
* es wird nur der eingerückte Teil (die Print Anweisung) ausgeführt

> :computer: Verwenden Sie eine for-Schleife, um den Text "Guten Morgen!" 10x auszugeben.

<details>
  <summary>Lösung</summary>
  
  ```python3 
  for a in range(0, 10):
    print("Good morning!")
  ```
</details>

In der oben angegebenen for-Schleife haben wir eine Variable `a`. Dies muss nicht a sein. Wir können diese Variable auch im eingerückten Teil des Textes verwenden. Lassen wir unser Skript den Wert der Variablen ausdrucken.

```python3
for a in range(0, 10):
    print("This is the " + str(a) + ". iteration")
```

> Achtung, es muss der richtige Bereich angegeben werden!

<details>
  <summary>Lösung</summary>
  
  ```python3
  for a in range(1, 6):
    print("This is the " + str(a) + ". iteration")
  ```
</details>

> :computer: Verwenden wir dieses neue Wissen, um alle IP-Adressen in einem Teilnetz auszudrucken.
> 
> Bei einem Class C Netzwerk `192.168.0.0/24` mit einer Netzmaske `255.255.255.0` alle verfügbaren Adressen ausgeben (einschließlich der Netzwerk- und Broadcast-Adresse)

<details>
  <summary>Lösung</summary>
  
  ```python3
  for host_part in range(0, 256):
    ip_address = "192.168.0." + str(host_part)
    print(ip_address)
  ```
</details>

Wir können auch eine for-Schleife innerhalb einer anderen for-Schleife haben. Der Vorgang nennt sich *nesting*.

```python3
for x in range(0, 10):
    for y in range(0, 10):
        print("Looking at pixel (" + str(x) + "," + str(y) + ")")
```

> :computer: Wir können verschachtelte for-Schleifen verwenden, um Multiplikationstabellen auszugeben. Ändere den folgenden Code
> 
> ```python3
>  for num in range(1, 11):
>       print("Multiplication table for " + str(num))
>       # Use another for loop for the `multiplier` variable 
>       # Insert here
>           res = num ∗ multiplier
>           print(str(num) + ” x ” + str(multiplier) + ” = ” + str(res))
> ```

<details>
  <summary>Lösung</summary>
  ```python3 
  for num in range(1, 11):
        print("Multiplication table for " + str(num))
        for multiplier in range(1, 11):
           res = num ∗ multiplier
           print(str(num) + ” x ” + str(multiplier) + ” = ” + str(res))
  ```
</details>

## Kontroll Strukturen

*If-Klauseln* können verwendet werden, um den Programmablauf in Abhängigkeit von einem Variablenwert zu ändern. Die Anweisungen, die ausgeführt werden, wenn ein *Vergleich* oder eine *Bedingung* erfüllt ist, werden auch als *Verzweigung* bezeichnet. Sie sind wiederum durch Einrückung gekennzeichnet.

```python3
a = 10
if a == 10:
    # This is the branch
    print("a has the value of " + str(a))
```

In diesem Beispiel verwenden wir `if` um zu verdeutlichen, dass es sich jetzt um eine *if-clause* handelt. 

Die Bedingung wird dann danach angegeben. Beachten Sie, dass wir `==` für den Vergleich verwenden.

Wir können eine Reihe von Vergleichsoperatoren verwenden wie:
* `a == b` to check if `a` ist gleich `b`
* `a >= b` to check if `a` ist größer oder gleich `b` 
* `a <= b` to check if `a` ist kleiner oder gleich `b`
* `a%b == 0` to check if `a` kann geteilt werden durch `b` ohne einen Restbetrag

Wir können mehr als eine Bedingung haben. Um diese zusätzlichen Verzweigungen zu deklarieren, verwenden wir das Schlüsselwort `elif`. Zusätzlich können wir das Schlüsselwort `else` verwenden, um eine Verzweigung anzugeben, die ausgeführt wird, wenn keine der oben genannten Bedingungen erfüllt wurde.

```python3
a = 5
if a == 10:
    print("a is 10")
elif a == 5:
    print("a is 5")
else:
    print("a is neither 5 nor 10")
```
Beachten Sie, dass Python nicht mehr weiter prüft, wenn die erste Bedingung erfüllt ist! 

> :computer: Der **FizzBuzz**-Test ist eine berühmte Frage in Vorstellungsgesprächen für Programmieranfänger. Die Frage ist einfach:
> 
> Schreibe ein Programm, das die Zahlen von 1 bis (einschließlich) 20 ausgibt:
> 
> * für das Vielfache von drei wird **Fizz** anstelle der Zahl gedruckt
> * für das Vielfache von fünf wird **Buzz** anstelle der Zahl gedruckt
> * für das Vielfache von fünf und drei wird **FizzBuzz** anstelle der Zahl ausgegeben
> * In allen anderen Fällen geben Sie die Nummer aus.
> 
> Drei Tipps: 
> 
> 1) Um zu prüfen, ob eine Zahl ein Vielfaches einer anderen Zahl ist, können Sie diese Bedingung verwenden:
> 
> ```python3
> a = 10
> if a%5 == 0:
>   print("This number is a multiple of 5")
> ```
>
> 2) Mehrere Bedingungen lassen sich mit dem Schlüsselwort `and` verketten.
> 
> ```python3
> age = 17
> if age > 10 and age < 18:
>   print("The person is a teenager")
> ```
> 
> 3) Erinnern Sie sich an for-Schleifen? Sie könnten sich in dieser Übung als nützlich erweisen.

<details>
  <summary>Lösung</summary>
  
  ```python
  
  for num in range(1, 21):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(str(num))
  ```
</details>

<div align="right">
   
   [Zurück](variables.md) - [Weiter](functions.md)
</div>
