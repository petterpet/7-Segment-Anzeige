## 7-Segment-Anzeige

Die in diesem Repository enthaltenen Dateien ermöglichen das Ansteuern von zwei 7-Segment-Anzeigen mithilfe von Schieberegistern des Types 74HC595.

Entweder kann eine einzelne Zahl angezeigt werden oder ein Countdown von maximal 99 abwärts.

Die Ansteuerung erfolgt über einen Raspberry Pi mit Python und es gibt drei Möglichkeiten:
  * Benutzereingabe im Python-Fenster
  * Parameter beim Start über die Shell
  * Mitteilung des Wertes über MQTT
