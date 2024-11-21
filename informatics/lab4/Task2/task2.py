import re


def xml_to_yaml(xml_file_path, yaml_file_path):

    xml_file = open(xml_file_path, "r", encoding="utf-8")
    yaml_file = open(yaml_file_path, "w", encoding="utf-8")

    deep_level = next_deep_level = 0

    for line in xml_file.readlines():
        line = line.strip()

        if re.search(r'<\?xml.*\?>', line) or not line:
            pass
        else:
            tag = re.findall(r'<([^<>]+)>', line)[0]

            if '/' in tag:
                next_deep_level -= 1
                deep_level = next_deep_level
                continue

            line = re.sub(r'<([^/<>]+)>', r'\1: ', line)

            if '/' in line:
                line = re.sub(r'<(/[^<>]+)>', r'', line)
            else: next_deep_level += 1

            line = re.sub(r'^\s+|\s+$', '', line)

            if len(line) - 1 != line.count(" "):
                print(' ' * deep_level * 2 + line, end="\n", file=yaml_file)

            deep_level = next_deep_level

    xml_file.close()
    yaml_file.close()


if __name__ == '__main__':
    xml_to_yaml('../schedule.xml', 'schedule.yaml')