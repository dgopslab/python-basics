## `basics.md`

# Basics

## Was ist Python?

Python ist eine gut lesbare Programmiersprache, die sich für viele unterschiedliche Aufgaben einsetzen lässt.

Sie wird unter anderem verwendet für:

* Skripte und Automatisierung
* Webentwicklung
* Datenverarbeitung
* kleine Tools und Programme
* Testing und weitere technische Anwendungen

## Warum ich Python lerne

Python hilft mir dabei, Programmierlogik zu verstehen und grundlegende Konzepte praktisch anzuwenden.

Dabei geht es mir vor allem darum, Programme Schritt für Schritt nachzuvollziehen und die Grundlagen später in eigenen kleinen Projekten einsetzen zu können.

## Erste Grundlagen

### Variablen

Variablen speichern Werte, damit diese im Programm weiterverarbeitet werden können.

Beispiel:

```python
name = "Daniel"
age = 40
```

## Datentypen

Zu den grundlegenden Datentypen, mit denen ich bisher gearbeitet habe, gehören:

* `str` für Text
* `int` für ganze Zahlen
* `float` für Kommazahlen
* `bool` für Wahrheitswerte wie `True` oder `False`

## Ausgabe mit `print()`

Mit `print()` können Inhalte in der Konsole ausgegeben werden.

```python
print("Hello World!")
```

## Eingabe mit `input()`

Mit `input()` können Benutzereingaben abgefragt werden.

```python
name = input("Wie heißt du? ")
print(name)
```

## Strings

Strings sind Zeichenketten. Mit ihnen lassen sich zum Beispiel Namen, Begriffe oder ganze Sätze speichern und verarbeiten.

```python
vorname = "Daniel"
print(vorname)
```

## Was ich aus den ersten Grundlagen mitnehme

Die Basics helfen mir vor allem dabei, zu verstehen:

* wie Werte gespeichert werden
* wie Programme Informationen verarbeiten
* wie Ein- und Ausgaben funktionieren
* wie erste kleine Programme aufgebaut sind

## Einordnung

Diese Notizen stammen aus einer frühen Phase meines Python-Lernwegs und dokumentieren grundlegende Konzepte, auf denen meine späteren Übungen und Projekte aufbauen.

---

## `control-flow.md`

# Control Flow

## Was bedeutet Control Flow?

Control Flow beschreibt, in welcher Reihenfolge ein Programm ausgeführt wird und unter welchen Bedingungen bestimmte Teile des Codes laufen.

Damit kann ein Programm auf Eingaben reagieren, Entscheidungen treffen und Abläufe wiederholen.

## Bedingungen mit `if`, `elif` und `else`

Mit `if` kann geprüft werden, ob eine Bedingung erfüllt ist.

```python
age = 18

if age >= 18:
    print("Du bist volljährig.")
```

Mit `elif` können weitere Bedingungen ergänzt werden. Mit `else` kann ein Fall behandelt werden, wenn die vorherigen Bedingungen nicht erfüllt sind.

```python
score = 75

if score >= 90:
    print("Sehr gut")
elif score >= 70:
    print("Gut")
else:
    print("Weiter üben")
```

## Vergleichsoperatoren

Bedingungen arbeiten häufig mit Vergleichsoperatoren, zum Beispiel:

* `==` gleich
* `!=` ungleich
* `>` größer als
* `<` kleiner als
* `>=` größer oder gleich
* `<=` kleiner oder gleich

## Schleifen

Schleifen werden verwendet, wenn ein bestimmter Ablauf mehrfach ausgeführt werden soll.

### `for`-Schleife

Eine `for`-Schleife wird häufig verwendet, um nacheinander über mehrere Werte oder Elemente zu laufen.

```python
for number in range(5):
    print(number)
```

### `while`-Schleife

Eine `while`-Schleife läuft so lange, wie eine Bedingung erfüllt ist.

```python
count = 1

while count <= 3:
    print(count)
    count += 1
```

## Warum diese Grundlagen wichtig sind

Mit Bedingungen und Schleifen lassen sich Programme flexibel aufbauen.

Sie helfen dabei:

* Entscheidungen im Code abzubilden
* Eingaben auszuwerten
* wiederkehrende Abläufe umzusetzen
* Programme sinnvoll zu strukturieren

## Einordnung

Bedingungen und Schleifen gehören zu den Grundlagen, die ich anschließend in verschiedenen Übungen und kleinen Konsolenprogrammen praktisch eingesetzt habe.

---

## `functions.md`

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

---

## `exercises.md`

# Exercises

## Ziel dieser Datei

Hier sammle ich kleine Python-Übungen und erste Programme, mit denen ich grundlegende Konzepte praktisch angewendet habe.

Dazu gehören vor allem:

* Ein- und Ausgabe
* Bedingungen
* Schleifen
* Funktionen
* kleine Logikaufgaben

## Warum Übungen wichtig sind

Gerade am Anfang haben mir Übungen dabei geholfen, die Grundlagen nicht nur theoretisch zu verstehen, sondern auch praktisch anzuwenden.

Dabei ging es für mich vor allem darum:

* Syntax sicherer anzuwenden
* Programmabläufe besser zu verstehen
* Fehler zu erkennen und zu korrigieren
* Schritt für Schritt sicherer im Schreiben von Code zu werden

## Beispiele für frühe Übungen

Typische Übungen aus dieser Lernphase waren zum Beispiel:

* kleine Begrüßungsprogramme
* Abfragen mit `if`, `elif` und `else`
* Schleifen mit `for` und `while`
* einfache Funktionen
* kleine Konsolenprogramme mit Benutzereingaben

## Beispiel aus dieser Lernphase

Ein konkretes Übungsprojekt ist mein [Caesar Cipher](caesar-cipher.md).

Dabei werden mehrere Grundlagen wie Eingaben, Bedingungen, Schleifen und String-Verarbeitung in einem kleinen Konsolenprogramm miteinander kombiniert.

## Einordnung

Diese Datei dokumentiert frühe Python-Übungen aus meinem Lernweg.

Weitere praktische Anwendungen entstehen inzwischen eher in eigenen Projekt-Repositories.
