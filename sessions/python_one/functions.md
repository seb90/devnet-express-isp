# Functionen
Funktionen werden dann interessant, wenn es Teile im Code gibt, die immer wieder verwendet werden. Es könnte zwar jedes mal der Code kopiert werden, aber im Falle einer Änderung müsste diese an vielen Stellen durchgeführt werden, außerdem kann mit Funktionen viel Code gespart werden und die Übersichtlichkeit erhöht werden.

#### Probleme bei Copy & Paste:
- Änderungen müssen an jeder Stelle gemacht werden, wird ein Teil übersehen führ dies zu Fehler

## Functionen definieren
Eine Funktion beschreibt einen Teil des Codes, der jederzeit aufgerufen werden kann. Python bietet von Haus aus Funktionen, die wir bereits verwendet haben. z.B. `print`.

Erstellen einer ersten Funktion. Das Keyword dafür ist `def` gefolgt von einem Funktionsname, Rundenklammern und darin enthaltenen Übergabeparameter.

```python
def my_function():
    print("Hello")
```

Aufrufen einer Funktion:
```python

def my_function():
    print("Hello")

my_function()
```

> :computer: Aufgabe: Erstelle eine Funktion `say_hello` welche ausgibt `Hello NAME, nice to meet you!`. 
> Ersetze NAME mit deinem Namen.

<details>
  <summary>Lösung</summary>
  
  ```python
def say_hello():
    print("Hello Sebastian, nice to meet you!")

say_hello()
  ```
</details>

## Functions mit Parameter und Rückgaben
Functions können Parameter `arguments` haben. Diese Werte können in der Funktion verwendet werden.
```python
def say_hello(name):
    print("Hello " + str(name) + ", nice to meet you!")

say_hello('Sebastian')
```    

Eine Funktion kann uns auch etwas zurück geben, dafür wird `return` verwendet:
```python
def kb_to_mb(kb):
    mb = kb / 1024
    return mb

print(kb_to_mb(18271))
```

> :computer: Aufgabe: Schreibe eine Funktion `device_status`, welche die Parameter `name` und `status` annimmt. Wenn der Status *inactive* ist soll `Device NAME is offline` ausgegeben werden, ist das Device active soll `Device NAME is online` ausgegeben werden.
> Zusatzaufgabe: wenn keiner der Status nicht übereinstimmt soll eine entsprechende Fehlermeldung ausgegeben werden. 
>
> ```python
> def device_status(???, ???):
>   ???
>   return ???
> 
> print(device_status(???, ???))
> ```

<details>
  <summary>Lösung</summary>
  
  ```python
  
def device_status(name, status):
    if status == 'active':
        return 'Device' + name + ' is online.'
    if status == 'inactive':
        return 'Device' + name + ' is offline.'
    return "Error, device status for device " + name + " doesn't match."


print(device_status('SW1', 'active'))
print(device_status('SW2', 'inactive'))
  ```
</details>

<div align="right">
   
   [Zurück](loops.md) - [Weiter](advanced_data_structures.md)
</div>