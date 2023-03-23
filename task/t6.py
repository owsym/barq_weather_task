from utils.reader import get_file_content
from datetime import datetime

file_content = get_file_content(
    "/home/owsym/Project/Python/barq_weather_task/files/f2.csv"
)

for files_data in file_content:
    date = files_data[1]
    datetime = datetime.strptime(date, "%Y-%m-%d")
    weekday = datetime.strftime("%A")
    event = files_data[-2]

    if event == "Thunderstorm":
        print(f"This {weekday} , Event IS > {event}")
