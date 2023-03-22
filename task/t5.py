from utils.reader import get_file_content
file_contents  =get_file_content("/home/owsym/Project/Python/barq_weather_task/files/f2.csv")

for file_value in file_contents :
    date = file_value[1]
    events = file_value[-2]

    if events in ["Rain", "Snow", "Rain-Snow"]:
        print(f"On This {date} , Event IS > {events}")