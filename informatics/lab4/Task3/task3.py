def xml_to_yaml(xml_file_path, yaml_file_path):

    xml_file = open(xml_file_path, "r", encoding="utf-8")
    yaml_file = open(yaml_file_path, "w", encoding="utf-8")

    yaml_file.write(dict_to_yaml(xml_to_dict(xml_file.read())))

    xml_file.close()
    yaml_file.close()


def xml_to_dict(element):
    element = element.strip()
    if element.startswith("<?xml"):
        element = element[element.find("?>") + 2:].strip()

    if not element:
        return ""

    if "<" not in element or ">" not in element:
        return element.strip()

    result = {}
    while "<" in element and ">" in element:

        tag = element[element.find("<") + 1: element.find(">")]

        inner_content = element[element.find(">") + 1: element.find(f"</{tag}>")]
        parsed_content = xml_to_dict(inner_content)

        # Если тэг уже был
        if tag in result:
            # Если это еще не список, то делаем списком
            if not isinstance(result[tag], list):
                result[tag] = [result[tag]]
            result[tag].append(parsed_content)
        else:
            result[tag] = parsed_content

        end_tag = element.find(f"</{tag}>") + len(f"</{tag}>")
        element = element[end_tag:]

    return result


def dict_to_yaml(data, deep_level=0):
    yaml = ""

    if isinstance(data, dict):
        for key, value in data.items():
            # Если значение — строка, выводим в одной строке
            if isinstance(value, str):
                yaml += f"{' ' * deep_level * 2}{key}: {value}\n"
            else:
                yaml += f"{' ' * deep_level * 2}{key}:\n"
                yaml += dict_to_yaml(value, deep_level + 1)
    elif isinstance(data, list):
        for item in data:
            yaml += f"{' ' * deep_level * 2}- {dict_to_yaml(item, deep_level + 1).lstrip()}"
    else:
        yaml += f"{' ' * deep_level * 2}{data}\n"

    return yaml


if __name__ == '__main__':
    xml_to_yaml('../schedule.xml', 'schedule.yaml')