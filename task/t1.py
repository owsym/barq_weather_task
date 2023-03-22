from utils.reader import get_file_content
file_contents  =get_file_content("/home/owsym/Project/Python/barq_weather_task/files/f1.csv")

for file_value in file_contents :
    date = file_value[0]
    max_temp = float(file_value[1])
    min_temp = float(file_value[3])
    max_min_diff = max_temp - min_temp

    print(f"{date}  Max Temp{max_temp}  Min Temp{min_temp}  Difference Between {max_min_diff}")
