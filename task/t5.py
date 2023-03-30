from utils.reader import get_file_content
from utils.inedx_mapping import MapperIndex

file_contents = get_file_content(
    "/home/owsym/Project/Python/barq_weather_task/files/f2.csv"
)

for content in file_contents:
    date = content[MapperIndex.DATE_FILE2]
    events = content[MapperIndex.EVENTS]

    if events in ["Rain", "Snow", "Rain-Snow"]:
        print(f"On This {date} , Event IS > {events}")
