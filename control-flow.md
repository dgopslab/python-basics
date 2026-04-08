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

Mit elif können weitere Bedingungen ergänzt werden, und mit else kann ein Standardfall abgefangen werden.

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

Bedingungen arbeiten oft mit Vergleichsoperatoren, zum Beispiel:

- == gleich
- != ungleich
- > größer als
- < kleiner als
- >= größer oder gleich
- <= kleiner oder gleich

## Schleifen

Schleifen werden verwendet, wenn ein bestimmter Code mehrfach ausgeführt werden soll.

### for-Schleife

Eine for-Schleife wird oft verwendet, um über eine feste Anzahl oder über Elemente in einer Struktur zu laufen.

```python
for number in range(5):
    print(number)
```

### while-Schleife

Eine while-Schleife läuft so lange, wie eine Bedingung erfüllt ist.

```python
count = 1

while count <= 3:
    print(count)
    count += 1
```

## Warum diese Grundlagen wichtig sind

Mit Bedingungen und Schleifen lassen sich Programme deutlich flexibler aufbauen.

Sie helfen dabei:

- Entscheidungen im Code abzubilden
- Eingaben auszuwerten
- wiederkehrende Abläufe zu automatisieren
- Programme sinnvoll zu strukturieren

## Aktueller Stand

Ich arbeite aktuell daran, Bedingungen und Schleifen sicher zu verstehen und in kleinen Übungen anzuwenden.

Gerade diese Grundlagen sind für mich wichtig, um später auch komplexere Programme und Automatisierungen besser aufbauen zu können.
