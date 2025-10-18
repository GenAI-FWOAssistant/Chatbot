# Einführung FWO-Chatbot
Im Rahmen der Gruppenarbeit im Modul Sprachverarbeitung und generative KI entwickeln wir ein LLM-basiertes Agentensystem für die Fachschaft Wirtschaft Olten (FWO), eine studentische Vertretung aller Wirtschaftsstudenten der FHNW School of Business in Olten.

Ziel des Projekts ist es, die erlernten Vorlesungsthemen Prompt Engineering, Retrieval Augmented Generation (RAG) und Safeguarding praktisch anzuwenden.

Wir haben uns für einen FWO Chatbot entschieden, der das Schreiben von Social Media Beiträgen auf Instagram, LinkedIn und WhatsApp erleichtert. Das Erstellen der Beiträge ist zeitaufwendig und wird bisher meist mit ChatGPT gemacht. Dabei fehlt jedoch der Bezug zu internen Dokumenten und früheren Captions. Der Chatbot soll die Social Media Verantwortlichen unterstützen, indem er:
- Instagram Beiträge mit passenden Hashtags schreibt
- LinkedIn Beiträge ohne Hashtags im passenden Stil erstellt
- WhatsApp Nachrichten für kurzfristige Ankündigungen formuliert

Durch den Einsatz von RAG kann der Chatbot auf vergangene Inhalte zugreifen und Beiträge im vertrauten Stil der FWO generieren.

## Abgabe und Präsentation
Deadline: 27.10.2025, 17:00 Uhr
Präsentation am 27.10.2025

## How to use
### Voraussetzungen:
- VS Code oder Pycharm als Applikation
- `requirements.txt` ausführen während der Installation (siehe Schritt 3)
- Eigenen API Key -> Wir empfehlen CEREBRAS

1. ### Virtuelle Umgebung erstellen
```
python -m venv ./.venv
```

2. ### Script aktivieren
#### Windows:
```
.\.venv\Scripts\Activate
```

#### MacOS:
```
source .venv/bin/Activate
```


3. ### Jetzt das Requirement installieren
#### Windows:
```
pip install -r .\requirements.txt
```

#### MacOS:
```
pip install -r ./requirements.txt
```

4. ### .env Datei erstellen
IHR_API_KEY = secretkey