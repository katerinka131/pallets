import csv

class Box:
    def __init__(self, width: int, length: int, SKU: int):
        self.SKU = SKU
        self.width = width
        self.length = length


def read_csv(file_path: str) -> list[Box]:
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        next(reader)
        # TODO: here we ignore cases where we have more than 1 box of same SKU, but it is quite rare so skip for now
        return [Box(int(row[2]), int(row[3]), int(row[0])) for row in reader]
    

def grab_best_box(boxes, cell_width, cell_length):
    best_box_idx = -1
    best_box_area = -1
    for i in range(len(boxes)):
        box = boxes[i]
        if (box.width <= cell_width and box.length <= cell_length) or (box.width <= cell_length and box.length <= cell_width):
            area = box.width * box.length
            if area > best_box_area:
                best_box_area = area
                best_box_idx = i
    if best_box_idx == -1:
        raise Exception("No box fits in cell")
    return boxes.pop(best_box_idx)


def run_one(file_idx, width, lenght, amount):
    boxes = read_csv(f"data/{file_idx}.csv")
    best_boxes = []
    for _ in range(amount):
        best_boxes.append(grab_best_box(boxes, lenght, width))
    total_area = sum([box.width * box.length for box in best_boxes])
    return (total_area, best_boxes)


def run_one_ansambled(file_idx):
    # width, length, amount
    cell_sizes = [
        (100, 100, 96),
        (100, 200, 48),
        (200, 200, 24),
        (200, 300, 16),
        (240, 200, 20),
        (400, 300, 8),
        (400, 400, 6),
        (600, 400, 4),
        (600, 800, 2),
        (1200, 800, 1),
    ]
    best_area = -1
    best_boxes = []
    best_size = None
    for size in cell_sizes:
        try:
            cur_area, cur_boxes = run_one(file_idx, size[0], size[1], size[2])
            if cur_area > best_area:
                best_area = cur_area
                best_boxes = cur_boxes
                best_size = size
        except Exception as e:
            pass
    return best_area, best_boxes, best_size
