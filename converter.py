import csv

def csv_to_yaml(csv_file, yaml_file):
    with open(csv_file, 'r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip header if present
        data = {}
        for row in csvreader:
            intent = row[0]
            example = row[1]
            if intent not in data:
                data[intent] = []
            data[intent].append(example)
    
    with open(yaml_file, 'w', encoding='utf-8') as yamlfile:
        for intent, examples in data.items():
            yamlfile.write(f'nlu:\n')
            yamlfile.write(f'  - intent: {intent}\n')
            yamlfile.write(f'    examples: |\n')
            for example in examples:
                yamlfile.write(f'      - {example}\n')
