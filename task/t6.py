from utils.reader import get_file_content
from datetime import datetime
from utils.inedx_mapping import MapperIndex

file_contents = get_file_content(
    "/home/owsym/Project/Python/barq_weather_task/files/f2.csv"
)

for content in file_contents:
    date = content[MapperIndex.DATE_FILE2]
    datetime = datetime.strptime(date, "%Y-%m-%d")
    weekday = datetime.strftime("%A")
    event = content[MapperIndex.EVENT]

    if event == "Thunderstorm":
        print(f"This {weekday} , Event IS > {event}")
