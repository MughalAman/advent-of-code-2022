def get_input_from_file() -> str:
    with open("input.txt", "r") as f:
        return str(f.read())

def calculate_total_calories(elf_with_calories: str) -> int:
    total_calories = 0
    for calorie in elf_with_calories.split("\n"):
        total_calories += int(calorie)
    return total_calories

def list_of_elves_with_total_calories(elves_list) -> list:
    elves_with_total_calories = []

    for elf in elves_list:
        elves_with_total_calories.append(calculate_total_calories(elf))

    return elves_with_total_calories

def get_top_3_elves(elves_with_total_calories: list) -> list:
    return sorted(elves_with_total_calories, reverse=True)[:3]

def get_3_biggest_calories(elves_with_total_calories: list) -> int:
    top_3_elves = get_top_3_elves(elves_with_total_calories)

    return sum(top_3_elves), [elves_with_total_calories.index(elf) for elf in top_3_elves]

def main():
    input = get_input_from_file()
    elves_with_calories = input.split("\n\n")
    elves_with_total_calories = list_of_elves_with_total_calories(elves_with_calories)
    total_calories, elves_index = get_3_biggest_calories(elves_with_total_calories)

    print(f"Total calories: {total_calories} Elves: elve number {elves_index[0] + 1}, elve number {elves_index[1] + 1}, elve number {elves_index[2] + 1}")



if __name__ == "__main__":
    main()