import os
from datetime import datetime

class Logger:
    def __init__(self, log_file="logs/backup.log"):
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        self.log_file = log_file

    def log(self, level, message):
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{time}] [{level}] {message}\n"
        with open(self.log_file, "a") as f:
            f.write(log_entry)
