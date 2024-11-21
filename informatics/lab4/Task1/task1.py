import xmltodict
import yaml


def xml_to_yaml(xml_file_path, yaml_file_path):

    xml_file = open(xml_file_path, "r", encoding="utf-8")
    yaml_file = open(yaml_file_path, "w", encoding="utf-8")

    doc = xmltodict.parse(xml_file.read())

    yaml_file.write(yaml.dump(doc, allow_unicode=True))
    yaml_file.close()


if __name__ == '__main__':
    xml_to_yaml('../schedule.xml', 'schedule.yaml')