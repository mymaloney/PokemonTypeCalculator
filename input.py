import os

def get_types():
    types_input = input("Enter the types separated by commas and spaces (e.g., fire, water, grass, ...): ").strip()
    types = [type_.strip().lower() for type_ in types_input.split(",") if type_.strip()]
    return types

def get_effectiveness(types):
    effectiveness_chart = {type_: {type_: 1 for type_ in types} for type_ in types}
    for type_ in types:
        print(f"\nConfiguring effectiveness for {type_}:")

        super_effective = input(f"Enter types {type_} is super effective against (2), separated by commas: ").strip()
        if super_effective:
            super_effective_types = [t.strip().lower() for t in super_effective.split(",") if t.strip()]
            for t in super_effective_types:
                effectiveness_chart[type_][t] = 2

        not_very_effective = input(f"Enter types {type_} is not very effective against (0.5), separated by commas: ").strip()
        if not_very_effective:
            not_very_effective_types = [t.strip().lower() for t in not_very_effective.split(",") if t.strip()]
            for t in not_very_effective_types:
                effectiveness_chart[type_][t] = 0.5

        ineffective = input(f"Enter types {type_} is ineffective against (0), separated by commas: ").strip()
        if ineffective:
            ineffective_types = [t.strip().lower() for t in ineffective.split(",") if t.strip()]
            for t in ineffective_types:
                effectiveness_chart[type_][t] = 0

    return effectiveness_chart

def format_chart(chart):
    formatted_chart = "type_chart = {\n"
    for type_, effectiveness in chart.items():
        formatted_chart += f"    '{type_}': {{"
        formatted_chart += ", ".join(f"'{k}': {v}" for k, v in effectiveness.items())
        formatted_chart += "},\n"
    formatted_chart += "}\n"
    return formatted_chart

def update_file(file_path, new_chart):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    start_idx = None
    end_idx = None
    for i, line in enumerate(lines):
        if 'type_chart = {' in line:
            start_idx = i
        if start_idx is not None and line.strip() == '}':
            end_idx = i + 1
            break

    if start_idx is None or end_idx is None:
        print(f"Error: Could not find type_chart in {file_path}")
        return

    new_chart_str = format_chart(new_chart)
    updated_lines = lines[:start_idx] + [new_chart_str] + lines[end_idx:]

    with open(file_path, 'w') as file:
        file.writelines(updated_lines)

    print(f"type_chart successfully updated in {file_path}")

def update_type_charts(new_chart):
    update_file('attack.py', new_chart)
    update_file('defend.py', new_chart)

def main():
    types = get_types()
    if not types:
        print("No types entered.")
        return

    type_chart = get_effectiveness(types)
    update_type_charts(type_chart)

if __name__ == "__main__":
    main()
