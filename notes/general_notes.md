Automatisierte Validierung von automatisiert generierten Simulationsbasierten Digitalen Zwillingen für Diskrete Materialflusssysteme

Story:
 V\&V von digitalen Zwillingen benötigt als ersten Schritt Referenzwert, die Vergleichen werden können (siehe SIMULATION-BASED DIGITAL TWINS: AN ACCREDITATION METHOD)
 Normalerweise sind diese Werte Use-case spezifisch festzulegen und müssen im phyischen System und im digitalen Zwilling übereinstimmen
 Bei Automatische generierten Zwillingen wird häufig auf Process Mining und das (object centric) Eventlog Format gesetzt
 Gerade bei der automatischen erstellung macht ein manuelles V\&V wenig Sinn, da es wieder manuellen Expertenaufwand erhöht
 Hier soll also ein V\&V Verfahren entwickelt werden das Use-case unabhängig automatisiert eingesetzt werden kann
 Kernidee: das object-centric Event log dient als Grundlage für V\&V

- V+V nach der Modellerstellung
- ist bei AUtomatischen generierten DT Verifikation und Validierung nicht dasselbe?
Was ist hierbei Verifikation? Fällt das weg?

Vorgehen:
 Eventlog zeitlich aufsteigen sortieren
 Train,validation und test set bestimmen und mit 1 labeln
 Aufträge aus den Daten generieren Order darf nicht die gesamten Prozessschritte beinhalten Features requested auslesen automatisch => Wie bei Schmaus? Was ist relevantes Features und was sind unwichtige Prozessdaten? TransformationModell soll Feautures entrhalten nur ORders = Aufträge mit sinnvollen Features: Finde sinnvolle Aufträge
Wahrtscheinlich passen die Zeiten aber die exakten Zeitpunkte was mit denen?

SOLL: Simulation kann Eventlog 1:1 wiedergeben
Feinplanungssimulation durchaus interessant: TimeModel genauer gestalten

welcher purpose? Design planning or control? Wann welcher purpose wie will ich VVUQ machen?
Wie abstrahieren wir von den Eventlogs? Kriterien anhand des Eventlogs zur Evailierung festrlegen welche Metriken? Was giobt das Foirmat her?
 Für Training, Validation und Test Zeitraum (mit selben Auftragsdaten) Eventlogs mit der Simulation erzeugen und mit 0 Labeln
 Classifier trainieren () und validieren gegenfalls Hyperparameter anpasssen. Ist der Classifier genau genug? Was will man mit dieser Genauigkeit erreichen?
 Wenn Model schon jetzt perfekt, testweise realistische Fehler in original Eventlogs von Validierung und Testset einbauen
 Das V\&V System sollte nun die Abweichung erkennen
 Framework auf Schmausdaten final testen
