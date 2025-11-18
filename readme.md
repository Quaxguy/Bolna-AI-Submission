# OpenAI Status Tracker

A lightweight and efficient Python-based monitoring tool that tracks real-time service updates from the **OpenAI Status Page** using its official **Atom feed** (`history.atom`).  
Built for scalability, reliability, and low overhead—ideal for monitoring multiple services or integrating into larger observability systems.

---

## 🌟 Features

### ⚡ Efficient Polling
- Uses the lightweight Atom feed instead of scraping the main status page.
- Minimizes network usage and CPU overhead.

### 🔔 Real-Time Event Detection
- Tracks the unique ID of the most recent update.
- Instantly identifies new incidents, outages, or degradations.

### 📝 Structured Logging
Outputs standardized, timestamped updates:

```
[YYYY-MM-DD HH:MM:SS] Product: [Affected Service(s)]
[YYYY-MM-DD HH:MM:SS] Status: [Incident Title/Latest Update]
```

### 🕘 Historical Context
- Displays the 5 most recent past incidents upon startup.

### 💓 Heartbeat Signal
- Prints `[All good!]` every 60 seconds when no new updates appear.

---

## 📦 Requirements

- Python **3.x**

Dependencies:
- `requests`
- `feedparser`

---

## 🛠️ Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

Run the tracker:

```bash
python status_tracker.py
```

---

## 📟 Example Output

### On Startup

```
Starting OpenAI Status Tracker...
Monitoring feed: https://status.openai.com/history.atom
Checking for updates every 60 seconds...

--- Displaying 5 Most Recent Historical Updates ---
[2025-11-13 00:33:54] Product: Conversations (Operational)
[2025-11-13 00:33:54] Status: Enterprise users seeing "Access Denied" error

[2025-11-14 02:14:02] Product: Image Generation (Operational)
[2025-11-14 02:14:02] Status: Image generation failing for Android users

... (2 more entries) ...

[2025-11-15 08:53:03] Product: Batch (Operational)
[2025-11-15 08:53:03] Status: Subset of Batch API jobs stuck in finalizing state

--- Tracker initialized. Monitoring for new updates. ---
[2025-11-18 09:45:00] All good!
[2025-11-18 09:46:00] All good!
```

### New Incident Example

```
--- New Status Update Detected ---
[2025-11-18 10:05:15] Product: Chat Completions
[2025-11-18 10:05:15] Status: Degradation of gpt-4o performance observed

--------------------------------------------------
```

---

## 🛑 Stopping the Tracker

Press:

```
Ctrl + C
```

---

## 📁 Project Structure

```
/
├── status_tracker.py
└── requirements.txt
```

---
