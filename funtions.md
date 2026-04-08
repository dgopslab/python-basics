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
def greet(name):
    print(f"Hallo, {name}!")
```

Beim Aufruf kann dann ein konkreter Wert übergeben werden:

```python
greet("Daniel")
```

## Funktionen mit Rückgabewert

Mit return kann eine Funktion ein Ergebnis zurückgeben.

```python
def add(a, b):
    return a + b
```

Diese Funktion addiert zwei Werte und gibt das Ergebnis zurück.

```python
result = add(3, 4)
print(result)
```

## Warum ich Funktionen als wichtig empfinde

Durch Funktionen lerne ich, Programme nicht nur Zeile für Zeile zu schreiben, sondern in sinnvolle einzelne Aufgaben aufzuteilen.

Gerade bei größeren Aufgaben wird schnell klar, dass man nicht alles einfach untereinander schreiben sollte. Funktionen machen den Code sauberer und logischer.

## Aktueller Stand

Ich arbeite aktuell daran, Funktionen mit Parametern und Rückgabewerten sicher zu verstehen und in kleinen Übungen anzuwenden.

Sie sind für mich eine wichtige Grundlage für späteren, besser strukturierten Code.
