# Automatisierte Validierung von automatisiert generierten Simulationsbasierten Digitalen Zwillingen für Diskrete Materialflusssysteme

## 1. Einleitung (6-8 Seiten)

1.1 Ausgangssituation

- Bedeutung und Herausforderungen von Digital Twins in der Materialflussplanung
- Problemstellung der manuellen Validierung bei automatisch generierten Modellen

1.2 Problemstellung

- Herausforderungen bei der V&V von automatisch generierten Digital Twins
- Notwendigkeit von Use-Case-unabhängigen Validierungsmethoden
- **Grundlegende Begriffsklärung: Verifikation und Validierung** (→ ausführliche Diskussion in 2.2)
- **Die Verschmelzung von Verifikation und Validierung bei automatisch generierten Modellen**

1.3 Zielsetzung der Arbeit

- Forschungsfragen:
  - Wie kann ein automatisiertes V&V-Verfahren für automatisch generierte Digital Twins entwickelt werden?
  - Inwiefern kann das Object-Centric Event Log als Grundlage für die automatisierte Validierung dienen?
  - **Welche Rolle spielt die Verifikation im Kontext automatisch generierter Digital Twins und inwiefern verschmilzt sie mit der Validierung?** (→ Diskussion in 2.2, 3.1 und 7.2)
- Hypothesen
- **Vorläufige Positionierung zur V&V-Problematik** (→ wird in 2.2 theoretisch fundiert und in 7.2 reflektiert)

1.4 Aufbau der Arbeit/Methodisches Vorgehen

- **Verweis auf methodische Herangehensweise zur empirischen Überprüfung der V&V-Konzepte** (→ Kapitel 4 und 6)

## 2. Theoretische Grundlagen (10-12 Seiten)

2.1 Digital Twin: Definition und Konzepte

- Arten von Digitalen Zwillingen
- Data Driven Digital Twins (→ Bezug zu 3.2: Automatische Modellgenerierung)
- Automatisch generierte Digital Twins

2.2 Verifikation und Validierung im Kontext simulationsbasierter Digital Twins

- **Definitionen und Unterschiede aus klassischer Simulationsliteratur**
- **Historische Entwicklung der V&V-Konzepte** (→ Bezug zu 1.2: Einführende Begriffsklärung)
- **Besonderheiten bei automatisch generierten Modellen** (→ Bezug zu 3.1 und 7.2)
- **Theoretische Argumentation zur Verschmelzung von Verifikation und Validierung**
- **V&V als kontinuierlicher Prozess** (→ Bezug zu 4.5: Online-Validierung)

2.3 Process Mining und Event Logs

- Object-Centric Event Logs als Datengrundlage (→ Bezug zu 4.2: Datenbasierte Validierungsstrategie)
- Standardformate und ihre Bedeutung für die automatisierte Validierung
- **Process Mining als Brücke zwischen Prozessdaten und Modellvalidierung** (→ Bezug zu 4.3)

2.4 Materialflussplanung und -simulation

- Grundlegende Konzepte
- Prozesse und Ressourcen
- Produktionsplanung und Steuerung
- **Relevante KPIs und Metriken** (→ Bezug zu 4.4: Metriken zur Modellbewertung)

## 3. Stand der Forschung (8-10 Seiten)

3.1 Bestehende Ansätze zur Validierung und Verifikation von Digital Twins

- Manuelle vs. automatisierte Ansätze
- **Kritische Diskussion bestehender V&V-Definitionen und Methoden** (→ Rückbezug zu 2.2)
- Herausforderungen bei der Validierung automatisch generierter Modelle

3.2 Automatische Modellgenerierung für Digital Twins

- Vorteile der automatischen Generierung:
  - Kontinuierliche Aktualität und Online-Validierung (→ Bezug zu 4.5)
  - Bewältigung hoher Komplexitätsgrade
  - Standardisierung und Transparenz
  - Skalierbarkeit
  - Vermeidung von Bias in manuellen Validierungen
  - Kosteneinsparungen
- **Herausforderungen bei automatischer Modellgenerierung** (→ Bezug zu Problemstellung in 1.2)

3.3 Machine Learning-basierte Ansätze zur Modellvalidierung

- Klassifikationsverfahren für die Erkennung von Modellabweichungen (→ Bezug zu 4.3)
- Herausforderungen bei der Datenaufbereitung und Feature-Selektion
- **Diskussion bisheriger ML-Ansätze im Kontext der V&V-Problematik** (→ Bezug zu 2.2 und 4.3)

3.4 Forschungslücken und offene Fragen

- **Identifizierung der Forschungslücke zur automatisierten V&V** (→ Bezug zu Forschungsfragen in 1.3)
- **Abgrenzung des eigenen Forschungsansatzes** (→ Überleitung zu Kapitel 4)

## 4. Konzeption eines Frameworks zur automatisierten Validierung (12-15 Seiten)

4.1 Anforderungsanalyse

- Funktionale Anforderungen
- Technische Anforderungen
- Anforderungen an Datenformate
- **Ableitung der Anforderungen aus theoretischen Erkenntnissen** (→ Bezug zu 2.2 und 3.4)

4.2 Datenbasierte Validierungsstrategie

- Object-Centric Event Logs als Validierungsgrundlage (→ Bezug zu 2.3)
- Zeitliche Datenpartitionierung (Training, Validation, Test)
- Feature-Selektion: Identifikation relevanter Merkmale aus Event Logs
- Auftragsrekonstruktion aus Prozessdaten
- **Methodische Umsetzung der theoretischen V&V-Konzepte** (→ Bezug zu 2.2)

4.3 Machine Learning-basierter Validierungsansatz

- Simulationsmodell zur Erzeugung synthetischer Event Logs
- **Klassifikationsbasierte Abweichungserkennung als vereinheitlichten V&V-Ansatz** (→ Bezug zu 2.2 und 3.3)
- Hyperparameter-Optimierung und Modellselektion
- Künstliche Fehlerinjektion zur Validierung des Ansatzes (→ Bezug zu 6.3)

4.4 Metriken und Kennzahlen zur Modellbewertung

- Prozessorientierte Metriken (Durchlaufzeiten, Ressourcenauslastung) (→ Bezug zu 2.4)
- Zeitbezogene Metriken (Start- und Endzeitpunkte, Bearbeitungsdauern)
- Auftragsbezogene Metriken (Vollständigkeit, Reihenfolgetreue)
- **Ableitung der Metriken aus V&V-Theorie** (→ Bezug zu 2.2)

4.5 Online-Validierung und kontinuierliches Monitoring

- Früherkennung von Modellabweichungen
- Handlungsempfehlungen bei Modelldrift
- **V&V als kontinuierlicher Prozess in der Praxis** (→ Bezug zu 2.2)

## 5. Implementierung des Frameworks (8-12 Seiten)

5.1 Architektur und Systemaufbau

- Komponenten und ihre Interaktionen
- Datenfluss und Schnittstellen
- UML-Diagramm des Gesamtsystems
- **Technische Umsetzung der konzeptionellen Anforderungen** (→ Bezug zu 4.1)

5.2 Event Log Verarbeitung

- Datenaufbereitung und -transformation
- Feature Engineering für Auftragsrekonstruktion (→ Bezug zu 4.2)
- Techniken zur Datenpartitionierung
- **Implementierung der Process-Mining-Konzepte** (→ Bezug zu 2.3)

5.3 Simulationsintegration

- Einbindung des Digital Twin Modells
- Generierung synthetischer Event Logs
- Automatisierte Validierungsexperimente
- **Praktische Umsetzung der V&V-Verschmelzung** (→ Bezug zu 2.2 und 4.3)

5.4 Machine Learning Pipeline

- Auswahl und Implementierung von Klassifikationsalgorithmen (→ Bezug zu 4.3)
- Training, Validierung und Modellevaluation
- Fehlerinjektion und Anomalieerkennung (→ Bezug zu 4.3 und 6.3)
- **Technische Realisierung des ML-basierten V&V-Ansatzes** (→ Bezug zu 3.3)

## 6. Fallstudie: Validierung in der Praxis (10-12 Seiten)

6.1 Anwendungsszenario und Datenbasis

- Beschreibung des Produktionssystems (z.B. IoT Factory)
- Verfügbare Eventdaten und ihre Eigenschaften
- Datenvorverarbeitung und -analyse
- **Vorstellung des Testumfelds zur empirischen Überprüfung** (→ Bezug zu 1.4)

6.2 Automatisch generierter Digital Twin

- Modellgenerierungsprozess
- Modelleigenschaften und -parameter
- **Aspekte der automatischen Modellgenerierung in der Praxis** (→ Bezug zu 3.2)

6.3 Validierungsexperimente

- Experimentelles Design
- Durchführung der automatisierten Validierung
- Fehlerinjektion und Modellanpassung
- **Empirische Überprüfung der theoretischen V&V-Konzepte** (→ Bezug zu 2.2 und 4.3)

6.4 Ergebnisse und Interpretation

- Modellgenauigkeit und -zuverlässigkeit
- Erkennungsrate von künstlich injizierten Fehlern
- Analyse der Validierungsmetriken (→ Bezug zu 4.4)
- **Bewertung der Ergebnisse im Kontext der V&V-Theorie** (→ Bezug zu 2.2)

6.5 Vergleich mit manuellen Validierungsmethoden

- Aufwandsanalyse
- Qualitätsvergleich
- Kosten-Nutzen-Betrachtung
- **Empirischer Beleg für die Vorteile der automatisierten V&V** (→ Bezug zu 3.2 und 7.3)

## 7. Diskussion der Ergebnisse (5-7 Seiten)

7.1 Evaluation des entwickelten Frameworks

- Stärken und Schwächen
- Erfüllung der Anforderungen (→ Bezug zu 4.1)
- **Bewertung des Frameworks im Lichte der Forschungsfragen** (→ Bezug zu 1.3)

7.2 Bedeutung der Verifikation bei automatisch generierten Digital Twins

- **Rückbezug zur theoretischen Diskussion über V&V** (→ Bezug zu 1.2, 2.2 und 3.1)
- **Empirische Erkenntnisse zur Verschmelzung von Verifikation und Validierung**
- Abgrenzung zur Validierung
- Integration in den Gesamtprozess
- **Theoretische Weiterentwicklung der V&V-Konzepte** (→ Bezug zu 2.2 und 8.2)

7.3 Limitationen der automatisierten Validierung

- Technische Grenzen
- Methodische Einschränkungen
- Anwendungsbereiche
- **Kritische Reflexion des eigenen Ansatzes** (→ Bezug zu 4.5 und 6.5)

7.4 Implikationen für Forschung und Praxis

- Wissenschaftlicher Beitrag
- Praktische Anwendbarkeit
- **Transfer der Erkenntnisse in andere Domänen** (→ Ausblick zu 8.3)

## 8. Fazit und Ausblick (4-6 Seiten)

8.1 Zusammenfassung der wichtigsten Ergebnisse

- **Beantwortung der Forschungsfragen** (→ Bezug zu 1.3)
- **Validierung der Hypothesen** (→ Bezug zu 1.3)
- **Synthese der empirischen Erkenntnisse** (→ Bezug zu Kapitel 6)

8.2 Methodische und theoretische Erkenntnisse

- **Bedeutung des Object-Centric Event Log Formats** (→ Bezug zu 2.3 und 4.2)
- **Machine Learning für die automatisierte Validierung** (→ Bezug zu 3.3 und 4.3)
- **Weiterentwicklung der V&V-Theorie** (→ Bezug zu 2.2 und 7.2)

8.3 Ausblick

- Zukünftige Forschungsrichtungen
- Potenzial für Weiterentwicklungen
- **Offene Fragen und weiterer Forschungsbedarf** (→ Bezug zu 3.4 und 7.4)

8.4 Handlungsempfehlungen für die Praxis

- Implementierungsstrategien
- Best Practices
- **Praktische Anwendung der theoretischen Erkenntnisse** (→ Bezug zu 7.4)

## 9. Literaturverzeichnis

## 10. Anhang

- Ergänzende Daten und Abbildungen
- Code- und Framework-Dokumentation
- Experimentelle Ergebnisse im Detail
- Glossar (falls erforderlich)
