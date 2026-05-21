import time

# Log file to monitor
LOG_FILE = "system.log"

# Alert file
ALERT_FILE = "alerts.txt"

# Keywords to detect
KEYWORDS = ["ERROR", "FAILED", "WARNING", "CRITICAL"]

print("LogWatch-Sentinel Started...")
print(f"Monitoring: {LOG_FILE}\n")


def check_keywords(line):
    for word in KEYWORDS:
        if word in line:
            return word
    return None


# Open log file
with open(LOG_FILE, "r") as file:
    # Move to end of file
    file.seek(0, 2)

    while True:
        line = file.readline()

        if not line:
            time.sleep(1)
            continue

        detected = check_keywords(line)

        if detected:
            alert_message = f"[ALERT] {detected} detected -> {line}"

            print(alert_message)

            with open(ALERT_FILE, "a") as alert:
                alert.write(alert_message)