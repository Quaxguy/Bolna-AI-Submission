BOLNA AI SUBMISSION: OpenAI Status Tracker

🌟 Overview

This is a lightweight Python script designed to efficiently monitor and log service updates from the official OpenAI Status Page. Instead of relying on inefficient web scraping or continuous page refreshes, the script utilizes the status page's official Atom feed (history.atom) to adopt a scalable, event-based tracking approach.

The application automatically detects new incidents, outages, or degradations and prints detailed, timestamped information about the affected product and the latest status event to the console.

✨ Features

Efficient Polling: Monitors the lightweight Atom feed (.atom file) rather than the heavy main HTML page, ensuring high efficiency and low overhead, which is crucial for scaling to many status pages.

Real-time Event Detection: Tracks the unique ID of the latest update. If a new ID is detected, it immediately fetches and processes the new incident details.

Structured Logging: Outputs all relevant updates in a standardized, easy-to-read format:

[YYYY-MM-DD HH:MM:SS] Product: [Affected Service(s)]
[YYYY-MM-DD HH:MM:SS] Status: [Incident Title/Latest Update]


Historical View: On startup, the script displays the 5 most recent historical updates to provide immediate context on past incidents.

Heartbeat Signal: Prints an [All good!] message every 60 seconds when no new updates are found, confirming the tracker is actively running.

⚙️ Prerequisites

You need Python 3.x installed on your system.

🛠️ Setup & Installation

Clone the repository or save the files:
Save the provided status_tracker.py and requirements.txt files into a single directory.

Install dependencies:
The script relies on two common Python libraries: requests (for fetching the feed) and feedparser (for parsing the Atom feed XML).

Open your terminal or command prompt, navigate to the project directory, and run:

pip install -r requirements.txt


(The requirements.txt file contains: requests and feedparser)

🚀 How to Run

Execute the script from your terminal:

python status_tracker.py


Example Console Output (Startup)

The application will first display the historical updates before entering the continuous polling loop.

Starting OpenAI Status Tracker...
Monitoring feed: [https://status.openai.com/history.atom](https://status.openai.com/history.atom)
Checking for updates every 60 seconds...

--- Displaying 5 Most Recent Historical Updates ---
[2025-11-13 00:33:54] Product: Conversations (Operational)
[2025-11-13 00:33:54] Status: Enterprise users seeing "Access Denied" error

[2025-11-14 02:14:02] Product: Image Generation (Operational)
[2025-11-14 02:14:02] Status: Image generation failing for Android users
... (2 more historical entries) ...
[2025-11-15 08:53:03] Product: Batch (Operational)
[2025-11-15 08:53:03] Status: Subset of Batch API jobs stuck in finalizing state

--- Tracker initialized. Monitoring for new updates. ---
[2025-11-18 09:45:00] All good!
[2025-11-18 09:46:00] All good!
... (Waits for new update) ...

--- New Status Update Detected ---
[2025-11-18 10:05:15] Product: Chat Completions
[2025-11-18 10:05:15] Status: Degradation of gpt-4o performance observed

--------------------------------------------------


Stopping the Tracker

To stop the script, press Ctrl+C in the terminal.