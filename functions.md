# Functions

## Was ist eine Funktion?

Eine Funktion ist ein benannter Codeblock, der eine bestimmte Aufgabe ausführt.

Funktionen helfen dabei, Code besser zu strukturieren, wiederzuverwenden und übersichtlicher zu machen.

## Warum Funktionen wichtig sind

Wenn derselbe Code mehrfach gebraucht wird, ist es sinnvoll, ihn in eine Funktion auszulagern.

Dadurch wird der Code:

- besser lesbar
- leichter wartbar
- einfacher wiederverwendbar

## Eine einfache Funktion

```python
def greet():
    print("Hallo!")
```

Diese Funktion heißt greet und gibt beim Aufruf einen Text aus.

```python
greet()
```

## Funktionen mit Parametern

Funktionen können Werte entgegennehmen, damit sie flexibler eingesetzt werden können.

```python
def greet_person(name):
    print(f"Hallo, {name}!")
```

Beim Aufruf kann dann ein konkreter Wert übergeben werden:

```python
greet_person("Daniel")
```

## Funktionen mit Rückgabewert

Mit `return` kann eine Funktion ein Ergebnis zurückgeben.

```python
def add(a, b):
    return a + b
```

Diese Funktion addiert zwei Werte und gibt das Ergebnis zurück.

```python
result = add(3, 4)
print(result)
```

Der Rückgabewert kann danach weiterverwendet, gespeichert oder in anderen Funktionen benutzt werden.

Das ist der wichtige Unterschied zu `print()`:  
`print()` zeigt etwas nur in der Konsole an, während `return` einen Wert aus der Funktion zurückgibt.

## Unterschied zwischen `print()` und `return`

`print()` zeigt einen Wert nur an.  
`return` gibt einen Wert zurück, damit er später weiterverarbeitet werden kann.

```python
def mit_print():
    print("Hallo")

def mit_return():
    return "Hallo"
```

Wenn eine Funktion etwas nur mit `print()` ausgibt, kann dieses Ergebnis nicht so einfach weiterverwendet werden.  
Mit `return` kann der Wert dagegen gespeichert oder an anderer Stelle im Programm benutzt werden.

## Mehrere Rückgaben

Eine Funktion kann je nach Bedingung unterschiedliche Werte zurückgeben.

```python
def is_adult(age):
    if age >= 18:
        return True
    else:
        return False
```

So kann eine Funktion je nach Eingabe unterschiedlich reagieren.

## Leeres `return`

Mit `return` ohne Wert kann eine Funktion sofort beendet werden.

```python
def check_number(number):
    if type(number) != int:
        return
    return number * 2
```

Das kann nützlich sein, wenn eine Funktion bei ungültigen Eingaben direkt abgebrochen werden soll.

## Docstrings

Docstrings sind kurze Beschreibungen, die direkt unter einer Funktionsdefinition stehen.

```python
def square(num):
    """Gibt das Quadrat einer Zahl zurück."""
    return num * num
```

Sie helfen dabei, schneller zu verstehen, was eine Funktion macht.

## Warum ich Funktionen als wichtig empfinde

Durch Funktionen lerne ich, Programme nicht nur Zeile für Zeile zu schreiben, sondern in sinnvolle einzelne Aufgaben aufzuteilen.

Gerade bei größeren Aufgaben wird schnell klar, dass man nicht alles einfach untereinander schreiben sollte. Funktionen machen den Code sauberer und logischer.

## Aktueller Stand

Ich arbeite aktuell daran, Funktionen mit Parametern, Rückgabewerten und einfachen Entscheidungswegen sicher zu verstehen und in kleinen Übungen anzuwenden.

Besonders wichtig war für mich dabei, den Unterschied zwischen `print()` und `return` besser zu verstehen.

Funktionen sind für mich eine wichtige Grundlage für späteren, besser strukturierten Code.
