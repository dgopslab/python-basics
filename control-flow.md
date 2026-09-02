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
