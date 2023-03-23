def get_file_content(file_content):
    files_data = []

    with open(file_content) as read_content:
        content = read_content.read()
        for data in content.split("\n")[1:-1]:
            files_data.append(data.split(","))

    return files_data
