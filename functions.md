# Functions

## Was ist eine Funktion?

Eine Funktion ist ein benannter Codeblock, der eine bestimmte Aufgabe ausführt.

Funktionen helfen dabei, Code besser zu strukturieren, wiederzuverwenden und übersichtlicher zu machen.

## Warum Funktionen wichtig sind

Wenn derselbe Code mehrfach gebraucht wird, kann es sinnvoll sein, ihn in eine Funktion auszulagern.

Dadurch wird der Code:

* besser lesbar
* leichter wartbar
* einfacher wiederverwendbar

## Eine einfache Funktion

```python
def greet():
    print("Hallo!")
```

Diese Funktion heißt `greet` und gibt beim Aufruf einen Text aus.

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

Der Rückgabewert kann danach weiterverwendet, gespeichert oder an andere Funktionen übergeben werden.

## Unterschied zwischen `print()` und `return`

`print()` zeigt einen Wert in der Konsole an.

`return` gibt einen Wert aus einer Funktion zurück, damit dieser anschließend weiterverarbeitet werden kann.

```python
def mit_print():
    print("Hallo")

def mit_return():
    return "Hallo"
```

Wenn eine Funktion einen Wert nur mit `print()` ausgibt, steht dieser Wert nicht automatisch als Rückgabewert der Funktion zur weiteren Verarbeitung zur Verfügung.

Mit `return` kann der Wert dagegen gespeichert oder an anderer Stelle im Programm verwendet werden.

## Unterschiedliche Rückgabewerte

Eine Funktion kann je nach Bedingung unterschiedliche Werte zurückgeben.

```python
def is_adult(age):
    if age >= 18:
        return True
    else:
        return False
```

So kann eine Funktion abhängig von der Eingabe unterschiedlich reagieren.

## Leeres `return`

Mit `return` ohne Wert kann eine Funktion vorzeitig beendet werden.

```python
def check_number(number):
    if type(number) != int:
        return

    return number * 2
```

Das kann zum Beispiel genutzt werden, wenn eine Funktion unter einer bestimmten Bedingung nicht weiter ausgeführt werden soll.

## Docstrings

Docstrings sind Beschreibungen, die direkt unter einer Funktionsdefinition stehen können.

```python
def square(num):
    """Gibt das Quadrat einer Zahl zurück."""
    return num * num
```

Sie helfen dabei, schneller zu verstehen, welche Aufgabe eine Funktion hat.

## Warum ich Funktionen wichtig finde

Durch Funktionen habe ich begonnen, Programme nicht nur Zeile für Zeile zu schreiben, sondern größere Aufgaben in kleinere Teilaufgaben aufzuteilen.

Gerade bei umfangreicheren Programmen hilft diese Struktur dabei, den Code besser nachvollziehen zu können.

## Einordnung

Funktionen mit Parametern und Rückgabewerten waren ein wichtiger Schritt dabei, Programme stärker in einzelne Aufgaben zu strukturieren.

Diese Grundlagen nutze ich inzwischen auch in weiteren Übungen und Projekten.

