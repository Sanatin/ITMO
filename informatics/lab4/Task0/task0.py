def xml_to_yaml(xml_file_path, yaml_file_path):

    xml_file = open(xml_file_path, "r", encoding="utf-8")
    yaml_file = open(yaml_file_path, "w", encoding="utf-8")

    deep_level = next_deep_level = 0

    for line in xml_file.readlines():
        line = line.strip()
        if '<?xml' in line or not line:
            pass
        else:
            tag = line[line.find("<") + 1:line.find(">")]

            if '/' in tag:
                next_deep_level -= 1
                deep_level = next_deep_level
                continue

            line = line.replace(f"<{tag}>", f"{tag}: ")

            if '/' in line:
                line = line.replace(f"</{tag}>", "")
            else: next_deep_level += 1

            line = line.strip()

            if len(line) - 1 != line.count(" "):
                print(' ' * deep_level * 2 + line, end="\n", file=yaml_file)

            deep_level = next_deep_level

    xml_file.close()
    yaml_file.close()


if __name__ == '__main__':
    xml_to_yaml('../schedule.xml', 'schedule.yaml')