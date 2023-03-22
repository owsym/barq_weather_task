def get_file_content(file_contents ):
    file_values = []

    with open(file_contents ) as read_content:
        content = read_content.read()
        for value in content.split("\n")[1:-1]:
            file_values.append(value.split(","))

    return file_values