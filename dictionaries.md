# Dictionaries

Ein Dictionary ist eine Datenstruktur in Python, mit der man einem Schlüssel (`key`) einen Wert (`value`) zuordnen kann.

Es funktioniert ähnlich wie ein Wörterbuch: Ein Begriff verweist auf eine bestimmte Bedeutung. In Python verweist ein Schlüssel auf einen bestimmten Wert.

## Warum Dictionaries nützlich sind

Dictionaries sind hilfreich, wenn Daten nicht nur als einzelne Werte gespeichert werden sollen, sondern als Zuordnungen.

Beispiele:

- ein Name zu einer Punktzahl
- ein Land zu seiner Hauptstadt
- ein Hund zu einer Eigenschaft

## Dictionary erstellen

```python
hunde = {
    "Jack": "empfindlicher Magen",
    "Barra": "aktiv",
    "Luna": "ruhig"
}
```

## Auf Werte zugreifen

Über den Schlüssel kann der passende Wert abgerufen werden:
```python
print(hunde["Jack"])
```

Ausgabe:
```python
empfindlicher Magen
```

## Leeres Dictionary erstellen

```python
leeres_dictionary = {}
```

## Neue Einträge hinzufügen
```python
hunde["Buddy"] = "verspielt"
```
## Werte ändern
```python
hunde["Barra"] = "sehr aktiv"
```

# Durch ein Dictionary iterieren

## Alle Schlüssel ausgeben
```python
for key in hunde:
    print(key)
```

## Alle Werte ausgeben
```python
for key in hunde:
    print(hunde[key])
```

## Was ich bisher damit verstanden habe
- Dictionaries speichern Daten als ```key```-```value```-Paare
- über einen Schlüssel kann man gezielt einen Wert abrufen
- man kann neue Einträge hinzufügen und bestehende ändern
- man kann über die Schlüssel iterieren und damit auch auf die Werte zugreifen

## Aktueller Stand
Ich habe die Grundlagen von Dictionaries kennengelernt und mit einer kleinen Silent-Auction-Übung angewendet.
