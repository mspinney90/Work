# A simple script that records the current date and time to a log file named "Logger.txt" every time it is run.

from datetime import datetime
from pathlib import Path


def record_current_time() -> None:
	log_file = Path(__file__).with_name("Logger.txt")
	current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

	with log_file.open("a", encoding="utf-8") as file:
		file.write(f"{current_time}\n")


if __name__ == "__main__":
	record_current_time()
