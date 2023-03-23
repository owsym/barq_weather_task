from utils.reader import get_file_content
from utils.inedx_mapping import MapperIndex

file_path = "/home/owsym/Project/Python/barq_weather_task/files/f1.csv"
file_content = get_file_content(file_path)


for content in file_content:
    date = content[MapperIndex.DATE]
    max_temperature = float(content[MapperIndex.MAX_TEMPERATURE])
    min_temperature = float(content[MapperIndex.MIN_TEMPERATURE])
    max_min_diff = max_temperature - min_temperature
    max_min_diff = (max_temperature - min_temperature) / 2

    print(
        f"{date}  Max Temp is {max_temperature}  Min Temp is {min_temperature}  Average Of {max_min_diff}"
    )
