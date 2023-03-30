from utils.reader import get_file_content
from utils.inedx_mapping import MapperIndex

file_path = "/home/owsym/Project/Python/barq_weather_task/files/f1.csv"
file_content = get_file_content(file_path)


for content in file_content:
    date = content[MapperIndex.DATE]
    max_temperature = float(content[MapperIndex.MAX_TEMPERATURE])
    min_temperature = float(content[MapperIndex.MIN_TEMPERATURE])
    max_min_difference = max_temperature - min_temperature

    print(
        f"{date}  Max Temp{max_temperature}  Min Temp{min_temperature}  Difference Between {max_min_difference}"
    )
