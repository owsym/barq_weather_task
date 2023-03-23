def get_file_content(file_path):
    files_contents = []

    with open(file_path) as file_reader:
        content = file_reader.read()

        for line_value in content.split("\n")[1:-1]:
            colum_value = line_value.split(",")
            files_contents.append(colum_value)

    return files_contents
