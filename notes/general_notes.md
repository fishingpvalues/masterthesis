# Automatisierte Verifikation, Generierung und Validierung von simulierten, digitalen Zwillingen  

*für diskrete Materialflusssysteme: Ein datengetriebenes Framework und Case Study*

---

## Story

- **Verifikation und Validierung (V&V) von digitalen Zwillingen:**  
  - Erster Schritt: Festlegung von Referenzwerten, die verglichen werden können (siehe *SIMULATION-BASED DIGITAL TWINS: AN ACCREDITATION METHOD*).
  - Normalerweise sind diese Werte use-case-spezifisch und müssen im physischen System sowie im digitalen Zwilling übereinstimmen.

- **Automatisch generierte digitale Zwillinge:**  
  - Häufig Einsatz von Process Mining und dem object-centric Eventlog-Format.
  - Manuelle V&V macht wenig Sinn, da sie den Expertenaufwand wieder erhöht.

- **Zielsetzung:**  
  - Entwicklung eines V&V-Verfahrens, das unabhängig vom Use-Case automatisiert eingesetzt werden kann.  
  - **Kernidee:** Das object-centric Eventlog dient als Grundlage für V&V.

---

## Vorgehen

1. **Sortierung:**  
   - Eventlog zeitlich aufsteigend sortieren.

2. **Datensplit:**  
   - Train-, Validation- und Testset bestimmen und mit dem Label "1" versehen.

3. **Auftragserzeugung:**  
   - Aufträge aus den Daten generieren (Order Generator bauen).

4. **Simulationsdaten:**  
   - Für Trainings-, Validierungs- und Testzeitraum (mit denselben Auftragsdaten) Eventlogs durch Simulation erzeugen und mit dem Label "0" versehen.

5. **Modelltraining:**  
   - Classifier trainieren und validieren, ggf. Hyperparameter anpassen.

6. **Fehler-Simulation:**  
   - Falls das Modell bereits sehr gut performt, testweise realistische Fehler in die originalen Eventlogs des Validierungs- und Testsets einbauen.

7. **V&V-System:**  
   - Das V&V-System sollte die Abweichungen erkennen.

8. **Endgültiger Test:**  
   - Framework final an Schmausdaten testen.
