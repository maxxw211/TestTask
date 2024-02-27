import ast
from itertools import combinations


def calculate_area(box: tuple) -> int:
    _, box_coordinates = box
    x = abs(box_coordinates[0] - box_coordinates[1])
    y = abs(box_coordinates[3] - box_coordinates[2])
    return x * y


def get_box_combinations(boxes: list, min_area: int, max_area: int) -> list[tuple] | list:
    valid_combinations = []

    for idx in range(1, len(boxes) + 1):
        for combination in combinations(boxes, idx):
            total_area = sum(calculate_area(box) for box in combination)
            if min_area <= total_area < max_area:
                valid_combinations.append(combination)

    return valid_combinations


input_boxes = ast.literal_eval(input("Input a list of boxes:\t"))
input_min_area = int(input("Minimum area:\t"))
input_max_area = int(input("Maximum area:\t"))

result = get_box_combinations(boxes=input_boxes, min_area=input_min_area, max_area=input_max_area)
for valid_combination in result:
    print(f"Valid combination: {[box[0] for box in valid_combination]}")
