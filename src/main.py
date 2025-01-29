 # Current data and time
import datetime


current_time = datetime.datetime.now()
file_path = "../docs/version.md"

with open(file_path, "w") as file:
    file.write(f" # Version information\n\n")
    file.write(f"{current_time}")
