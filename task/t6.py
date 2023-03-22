from utils.reader import get_file_content
from datetime import datetime

file_contents = get_file_content(
    "/home/owsym/Project/Python/barq_weather_task/files/f2.csv")

for file_value in file_contents:
    date = file_value[1]
    datetime = datetime.strptime(date, "%Y-%m-%d")
    weekday = datetime.strftime("%A")
    event = file_value[-2]

    if event == "Thunderstorm":
        print(f"This {weekday} , Event IS > {event}")
