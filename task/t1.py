from utils.reader import get_file_content

file_content = get_file_content(
    "/home/owsym/Project/Python/barq_weather_task/files/f1.csv"
)

for files_data in file_content:
    date = files_data[0]
    max_temp = float(files_data[1])
    min_temp = float(files_data[3])
    max_min_diff = max_temp - min_temp

    print(
        f"{date}  Max Temp{max_temp}  Min Temp{min_temp}  Difference Between {max_min_diff}"
    )
