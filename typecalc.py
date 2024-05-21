import itertools

# Define the custom type effectiveness chart as a dictionary
type_chart = {
    'normal': {'normal': 1, 'fighting': 1, 'flying': 1, 'poison': 1, 'ground': 1, 'rock': 0.5, 'bug': 1, 'ghost': 0, 'steel': 0.5, 'fire': 1, 'water': 1, 'grass': 1, 'electric': 1, 'psychic': 1, 'ice': 1, 'dragon': 1, 'dark': 1, 'fairy': 1},
    'fighting': {'normal': 2, 'fighting': 1, 'flying': 0.5, 'poison': 0.5, 'ground': 1, 'rock': 2, 'bug': 0.5, 'ghost': 0, 'steel': 2, 'fire': 1, 'water': 1, 'grass': 1, 'electric': 1, 'psychic': 0.5, 'ice': 1, 'dragon': 1, 'dark': 2, 'fairy': 0.5},
    'flying': {'normal': 1, 'fighting': 1, 'flying': 1, 'poison': 1, 'ground': 1, 'rock': 0.5, 'bug': 2, 'ghost': 1, 'steel': 0.5, 'fire': 1, 'water': 1, 'grass': 2, 'electric': 0.5, 'psychic': 1, 'ice': 1, 'dragon': 1, 'dark': 1, 'fairy': 1, 'fight': 2},
    'poison': {'normal': 1, 'fighting': 1, 'flying': 1, 'poison': 0.5, 'ground': 0.5, 'rock': 0.5, 'bug': 1, 'ghost': 0.5, 'steel': 0, 'fire': 1, 'water': 1, 'grass': 2, 'electric': 1, 'psychic': 1, 'ice': 1, 'dragon': 1, 'dark': 1, 'fairy': 2},
    'ground': {'normal': 1, 'fighting': 1, 'flying': 0, 'poison': 2, 'ground': 1, 'rock': 2, 'bug': 0.5, 'ghost': 1, 'steel': 2, 'fire': 2, 'water': 1, 'grass': 0.5, 'electric': 2, 'psychic': 1, 'ice': 1, 'dragon': 1, 'dark': 1, 'fairy': 1},
    'rock': {'normal': 1, 'fighting': 0.5, 'flying': 2, 'poison': 1, 'ground': 0.5, 'rock': 1, 'bug': 2, 'ghost': 1, 'steel': 0.5, 'fire': 2, 'water': 1, 'grass': 1, 'electric': 1, 'psychic': 1, 'ice': 2, 'dragon': 1, 'dark': 1, 'fairy': 1},
    'bug': {'normal': 1, 'fighting': 0.5, 'flying': 0.5, 'poison': 0.5, 'ground': 1, 'rock': 1, 'bug': 1, 'ghost': 0.5, 'steel': 0.5, 'fire': 0.5, 'water': 1, 'grass': 2, 'electric': 1, 'psychic': 2, 'ice': 1, 'dragon': 1, 'dark': 2, 'fairy': 0.5},
    'ghost': {'normal': 0, 'fighting': 1, 'flying': 1, 'poison': 1, 'ground': 1, 'rock': 1, 'bug': 1, 'ghost': 2, 'steel': 1, 'fire': 1, 'water': 1, 'grass': 1, 'electric': 1, 'psychic': 2, 'ice': 1, 'dragon': 1, 'dark': 0.5, 'fairy': 1},
    'steel': {'normal': 1, 'fighting': 1, 'flying': 1, 'poison': 1, 'ground': 1, 'rock': 2, 'bug': 1, 'ghost': 1, 'steel': 0.5, 'fire': 0.5, 'water': 0.5, 'grass': 1, 'electric': 0.5, 'psychic': 1, 'ice': 2, 'dragon': 1, 'dark': 1, 'fairy': 2},
    'fire': {'normal': 1, 'fighting': 1, 'flying': 1, 'poison': 1, 'ground': 1, 'rock': 0.5, 'bug': 2, 'ghost': 1, 'steel': 2, 'fire': 0.5, 'water': 0.5, 'grass': 2, 'electric': 1, 'psychic': 1, 'ice': 2, 'dragon': 0.5, 'dark': 1, 'fairy': 1},
    'water': {'normal': 1, 'fighting': 1, 'flying': 1, 'poison': 1, 'ground': 2, 'rock': 2, 'bug': 1, 'ghost': 1, 'steel': 1, 'fire': 2, 'water': 0.5, 'grass': 0.5, 'electric': 1, 'psychic': 1, 'ice': 1, 'dragon': 0.5, 'dark': 1, 'fairy': 1},
    'grass': {'normal': 1, 'fighting': 1, 'flying': 0.5, 'poison': 0.5, 'ground': 2, 'rock': 2, 'bug': 0.5, 'ghost': 1, 'steel': 0.5, 'fire': 0.5, 'water': 2, 'grass': 0.5, 'electric': 1, 'psychic': 1, 'ice': 1, 'dragon': 0.5, 'dark': 1, 'fairy': 1},
    'electric': {'normal': 1, 'fighting': 1, 'flying': 2, 'poison': 1, 'ground': 0, 'rock': 1, 'bug': 1, 'ghost': 1, 'steel': 1, 'fire': 1, 'water': 2, 'grass': 0.5, 'electric': 0.5, 'psychic': 1, 'ice': 1, 'dragon': 0.5, 'dark': 1, 'fairy': 1},
    'psychic': {'normal': 1, 'fighting': 2, 'flying': 1, 'poison': 2, 'ground': 1, 'rock': 1, 'bug': 1, 'ghost': 1, 'steel': 0.5, 'fire': 1, 'water': 1, 'grass': 1, 'electric': 1, 'psychic': 0.5, 'ice': 1, 'dragon': 1, 'dark': 0, 'fairy': 1},
    'ice': {'normal': 1, 'fighting': 1, 'flying': 2, 'poison': 1, 'ground': 2, 'rock': 1, 'bug': 1, 'ghost': 1, 'steel': 0.5, 'fire': 0.5, 'water': 0.5, 'grass': 2, 'electric': 1, 'psychic': 1, 'ice': 0.5, 'dragon': 2, 'dark': 1, 'fairy': 1},
    'dragon': {'normal': 1, 'fighting': 1, 'flying': 1, 'poison': 1, 'ground': 1, 'rock': 1, 'bug': 1, 'ghost': 1, 'steel': 0.5, 'fire': 1, 'water': 1, 'grass': 1, 'electric': 1, 'psychic': 1, 'ice': 1, 'dragon': 2, 'dark': 1, 'fairy': 0},
    'dark': {'normal': 1, 'fighting': 0.5, 'flying': 1, 'poison': 1, 'ground': 1, 'rock': 1, 'bug': 1, 'ghost': 2, 'steel': 1, 'fire': 1, 'water': 1, 'grass': 1, 'electric': 1, 'psychic': 2, 'ice': 1, 'dragon': 1, 'dark': 0.5, 'fairy': 0.5},
    'fairy': {'normal': 1, 'fighting': 2, 'flying': 1, 'poison': 0.5, 'ground': 1, 'rock': 1, 'bug': 1, 'ghost': 1, 'steel': 0.5, 'fire': 0.5, 'water': 1, 'grass': 1, 'electric': 1, 'psychic': 1, 'ice': 1, 'dragon': 2, 'dark': 2, 'fairy': 1},
}

types = list(type_chart.keys())

def calculate_effectiveness(attacker_types, defender_types):
    effectiveness = 1.0
    for atk in attacker_types:
        for defn in defender_types:
            effectiveness *= type_chart[atk][defn]
    return effectiveness

def check_coverage(attackers):
    coverage = {}
    all_combinations = list(itertools.product(types, repeat=2))
    for defender in all_combinations:
        max_effectiveness = 0  # Start with a low value
        for attacker in attackers:
            if isinstance(attacker, tuple):  # Dual type attacker
                attk_types = attacker
            else:
                attk_types = (attacker,)
            effectiveness = calculate_effectiveness(attk_types, defender)
            if effectiveness > max_effectiveness:
                max_effectiveness = effectiveness
        if max_effectiveness < 1:
            coverage[defender] = max_effectiveness
    return coverage

def get_attackers():
    attackers = []
    for i in range(1, 7):  # Allow up to 6 attackers
        attacker = input(f"Enter attacker {i} (or press Enter to finish): ").strip()
        if not attacker:
            break
        if '/' in attacker:
            attacker_types = tuple(attacker.lower().split('/'))
        else:
            attacker_types = attacker.lower()
        attackers.append(attacker_types)
    return attackers

# Main function to execute the coverage check
def main():
    attackers = get_attackers()
    if not attackers:
        print("No attackers entered.")
        return
    coverage = check_coverage(attackers)
    print("Defenders not fully covered:")
    for defender, eff in coverage.items():
        print(f"{defender}: {eff}")

if __name__ == "__main__":
    main()
