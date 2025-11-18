import requests
import feedparser
import time
import datetime
import re
import sys

# The official Atom feed for the OpenAI status page.
FEED_URL = "https://status.openai.com/history.atom"


POLL_INTERVAL_SECONDS = 60

def parse_entry(entry):
    """
    Parses a single entry from the Atom feed and prints it
    in the required format.
    """
    try:
        
        # The Atom feed uses <updated> for entries
        ts_struct = entry.updated_parsed
        ts_dt = datetime.datetime.fromtimestamp(time.mktime(ts_struct))
        ts_str = ts_dt.strftime('%Y-%m-%d %H:%M:%S')

        status_message = entry.title.strip()

        summary_html = entry.summary

        product = "N/A"

        
        # Look for <b> or <strong> tags around "Affected components"
        # and then capture the content of the <ul> list that follows.
        product_match = re.search(
            r'<[b|strong]>Affected components?</[b|strong]>\s*<ul>(.*?)</ul>',
            summary_html,
            re.IGNORECASE | re.DOTALL
        )

        if product_match:
            
            components_html = product_match.group(1)
            # Remove all HTML tags (like <li>)
            product = re.sub(r'<[^>]+>', '', components_html).strip()
            # Clean up newlines and replace with a comma
            product = re.sub(r'\s*\n\s*', ', ', product)
        elif "all systems operational" in status_message.lower():
            product = "All Systems"

        print(f"[{ts_str}] Product: {product}")
        print(f"[{ts_str}] Status: {status_message}\n")

    except Exception as e:
        print(f"Error parsing entry: {e}", file=sys.stderr)

def track_status():
    print("Starting Open AI status Tracker....")
    print(f"Monitoring feed: {FEED_URL}")
    print(f"Checking for updates every {POLL_INTERVAL_SECONDS} seconds....\n")

    last_seen_id = None
    first_run = True

    while True:
        try:
            
            response = requests.get(FEED_URL, timeout=10)
            response.raise_for_status()  

            feed = feedparser.parse(response.content)

            if feed.bozo:
                print(f"Warning: Feed may be malformed. {feed.bozo_exception}", file=sys.stderr)

            if not feed.entries:
                print("Feed contains no entries. Retrying...", file=sys.stderr)
                time.sleep(POLL_INTERVAL_SECONDS)
                continue

            
            latest_entry = feed.entries[0]
            latest_id = latest_entry.id

            if first_run:
                # On the first run, store the latest ID and print 5 historical updates
                last_seen_id = latest_id
                first_run = False

                print("--- Displaying 5 Most Recent Historical Updates ---")

                # Get the 5 latest entries (they are newest-to-oldest)
                historical_entries = feed.entries[:5]

                # Reverse them to print in chronological (oldest-to-newest) order
                historical_entries.reverse()

                for entry in historical_entries:
                    parse_entry(entry)

                print("--- Tracker initialized. Monitoring for new updates. ---")

            elif latest_id != last_seen_id:
                print("\n--- New Status Update Detected ---")

                #new entry
                new_entries = []
                for entry in feed.entries:
                    if entry.id == last_seen_id:
                        break
                    new_entries.append(entry)

                new_entries.reverse()

                for entry in new_entries:
                    parse_entry(entry)

                # Update the last seen ID to the newest one
                last_seen_id = latest_id
                print("--------------------------------------------------")

            else:
                ts_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                print(f"[{ts_str}] All good!")

        except requests.exceptions.RequestException as e:
            print(f"\nNetwork error: {e}", file=sys.stderr)
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}", file=sys.stderr)

        time.sleep(POLL_INTERVAL_SECONDS)

if __name__ == "__main__":
    try:
        track_status()
    except KeyboardInterrupt:
        print("\nTracker stopped by user.")
        sys.exit(0)