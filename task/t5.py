from utils.reader import get_file_content

file_content = get_file_content(
    "/home/owsym/Project/Python/barq_weather_task/files/f2.csv"
)

for files_data in file_content:
    date = files_data[1]
    events = files_data[-2]

    if events in ["Rain", "Snow", "Rain-Snow"]:
        print(f"On This {date} , Event IS > {events}")
