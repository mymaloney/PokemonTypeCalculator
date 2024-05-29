import itertools

# Define the custom type effectiveness chart as a dictionary
type_chart = {
    'normal': {'normal': 1, 'fighting': 1, 'flying': 1, 'poison': 1, 'ground': 1, 'rock': 0.5, 'bug': 1, 'ghost': 0, 'steel': 0.5, 'fire': 1, 'water': 1, 'grass': 1, 'electric': 1, 'psychic': 1, 'ice': 1, 'dragon': 1, 'dark': 1, 'fairy': 1},
    'fighting': {'normal': 2, 'fighting': 1, 'flying': 0.5, 'poison': 0.5, 'ground': 1, 'rock': 2, 'bug': 0.5, 'ghost': 0, 'steel': 2, 'fire': 1, 'water': 1, 'grass': 1, 'electric': 1, 'psychic': 0.5, 'ice': 1, 'dragon': 1, 'dark': 2, 'fairy': 0.5},
    'flying': {'normal': 1, 'fighting': 2, 'flying': 1, 'poison': 1, 'ground': 1, 'rock': 0.5, 'bug': 2, 'ghost': 1, 'steel': 0.5, 'fire': 1, 'water': 1, 'grass': 2, 'electric': 0.5, 'psychic': 1, 'ice': 1, 'dragon': 1, 'dark': 1, 'fairy': 1},
    'poison': {'normal': 1, 'fighting': 1, 'flying': 1, 'poison': 0.5, 'ground': 0.5, 'rock': 0.5, 'bug': 1, 'ghost': 0.5, 'steel': 0, 'fire': 1, 'water': 1, 'grass': 2, 'electric': 1, 'psychic': 1, 'ice': 1, 'dragon': 1, 'dark': 1, 'fairy': 2},
    'ground': {'normal': 1, 'fighting': 1, 'flying': 0, 'poison': 2, 'ground': 1, 'rock': 2, 'bug': 0.5, 'ghost': 1, 'steel': 2, 'fire': 2, 'water': 1, 'grass': 0.5, 'electric': 2, 'psychic': 1, 'ice': 1, 'dragon': 1, 'dark': 1, 'fairy': 1},
    'rock': {'normal': 1, 'fighting': 0.5, 'flying': 2, 'poison': 1, 'ground': 0.5, 'rock': 1, 'bug': 2, 'ghost': 1, 'steel': 0.5, 'fire': 2, 'water': 1, 'grass': 1, 'electric': 1, 'psychic': 1, 'ice': 2, 'dragon': 1, 'dark': 1, 'fairy': 1},
    'bug': {'normal': 1, 'fighting': 0.5, 'flying': 0.5, 'poison': 0.5, 'ground': 1, 'rock': 1, 'bug': 1, 'ghost': 0.5, 'steel': 0.5, 'fire': 0.5, 'water': 1, 'grass': 2, 'electric': 1, 'psychic': 2, 'ice': 1, 'dragon': 1, 'dark': 2, 'fairy': 0.5},
    'ghost': {'normal': 0, 'fighting': 1, 'flying': 1, 'poison': 1, 'ground': 1, 'rock': 1, 'bug': 1, 'ghost': 2, 'steel': 1, 'fire': 1, 'water': 1, 'grass': 1, 'electric': 1, 'psychic': 2, 'ice': 1, 'dragon': 1, 'dark': 0.5, 'fairy': 1},
    'steel': {'normal': 1, 'fighting': 1, 'flying': 1, 'poison': 1, 'ground': 1, 'steel': 0.5, 'fire': 0.5, 'water': 0.5, 'grass': 1, 'electric': 0.5, 'psychic': 1, 'ice': 2, 'dragon': 1, 'dark': 1, 'fairy': 2},
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

def calculate_weaknesses(defender_types):
    weaknesses = {}
    for attacker in type_chart.keys():
        max_effectiveness = 0  # Start with a low value
        for defender in defender_types:
            effectiveness = type_chart[attacker].get(defender, 1)  # Default to 1 if defender type not found
            if effectiveness > max_effectiveness:
                max_effectiveness = effectiveness
        if max_effectiveness > 1:
            weaknesses[attacker] = max_effectiveness
    return weaknesses

def recommend_types(weaknesses):
    recommendations = {}
    for attacker, eff in weaknesses.items():
        max_coverage = 0
        best_recommendation = []
        for atk_type in types:
            coverage = sum(1 for eff in weaknesses.values() if type_chart[atk_type].get(attacker, 1) == 2)
            if coverage > max_coverage:
                max_coverage = coverage
                best_recommendation = [atk_type]
            elif coverage == max_coverage:
                best_recommendation.append(atk_type)
        recommendations[attacker] = best_recommendation
    return recommendations

def get_defenders():
    defenders = []
    for i in range(1, 7):  # Allow up to 6 defenders
        defender = input(f"Enter defender {i} (or press Enter to finish): ").strip()
        if not defender:
            break
        if '/' in defender:
            defender_types = tuple(defender.lower().split('/'))
        else:
            defender_types = defender.lower()
        defenders.append(defender_types)
    return defenders

# Main function to execute the weakness check and recommendations
def main():
    defenders = get_defenders()
    if not defenders:
        print("No defenders entered.")
        return
    weaknesses = calculate_weaknesses(defenders)
    if not weaknesses:
        print("No weaknesses found in the defending team.")
    else:
        print("Weaknesses in the defending team:")
        for attacker, eff in weaknesses.items():
            print(f"{attacker}: {eff}")

        recommendations = recommend_types(weaknesses)
        print("\nRecommended types to add to your team:")
        for attacker, recs in recommendations.items():
            print(f"To cover against {attacker}, consider adding: {', '.join(recs) if recs else 'No strong recommendations'}")

if __name__ == "__main__":
    main()
