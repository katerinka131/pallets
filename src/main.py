from util import run_one_ansambled
import argparse
import matplotlib.pyplot as plt


def gen_layout(file_idx):
    best_area, best_boxes, best_size = run_one_ansambled(file_idx)
    cell_width, cell_length, amount = best_size
    left_bottom_corners = []
    res = []
    for y in range(0, 800, cell_width):
        for x in range(0, 1200, cell_length):
            left_bottom_corners.append((x, y))
    for i in range(amount):
        box = best_boxes[i]
        left_bottom_x, left_bottom_y = left_bottom_corners[i]
        right_top_x = left_bottom_x + cell_length
        right_top_y = left_bottom_y + cell_width
        if left_bottom_x + box.width > right_top_x or left_bottom_y + box.length > right_top_y:
            box_top_x = left_bottom_x + box.length
            box_top_y = left_bottom_y + box.width
            res.append((box.SKU, left_bottom_x, left_bottom_y, box_top_x, box_top_y))
        else:
            box_top_x = left_bottom_x + box.width
            box_top_y = left_bottom_y + box.length
            res.append((box.SKU, left_bottom_x, left_bottom_y, box_top_x, box_top_y))
    print(*res, sep='\n')
    print(f"Occupied area: {best_area}")
    print(f"Occupancy: {best_area / (1200 * 800) * 100}%")
    return res



def visualize_layout(file_idx):
    layout = gen_layout(file_idx)
    fig, ax = plt.subplots()
    for box in layout:
        sku, x1, y1, x2, y2 = box
        rect = plt.Rectangle((x1, y1), x2 - x1, y2 - y1, fill=True, edgecolor='black', facecolor='blue', alpha=0.5)
        ax.add_patch(rect)
        ax.text((x1 + x2) / 2, (y1 + y2) / 2, sku, ha='center', va='center', fontsize=8, color='white')
    ax.set_xlim(0, 1200)
    ax.set_ylim(0, 800)
    ax.set_aspect('equal')
    plt.title('Box Layout')
    plt.xlabel('Width')
    plt.ylabel('Length')
    plt.gca().invert_yaxis()
    plt.show()


def run_all():
    failed = 0
    occupancy = []
    for i in range(1, 437):
        total_area, best_boxes, size = run_one_ansambled(i)
        if total_area == -1:
            failed += 1
        else:
            occupancy.append(total_area / (1200 * 800))
            if total_area > 1200 * 800:
                print(f"Failed on {i}, total area {total_area}")
    print(f"Fail rate {failed / 436 * 100}%")
    print(f"Average occupancy: {sum(occupancy) / len(occupancy) * 100}%")
    plt.hist(occupancy, bins=20, edgecolor='black')
    plt.title('Occupancy Distribution')
    plt.xlabel('Occupancy')
    plt.ylabel('Frequency')
    plt.show()


def main():
    parser = argparse.ArgumentParser(description='Box Layout Generator')
    parser.add_argument('--run_all', action='store_true', help='Run all layouts')
    parser.add_argument('--file_idx', type=int, help='Index of the file to run a single layout')
    parser.add_argument('--visualize', action='store_true', help='Visualize the layout')
    args = parser.parse_args()
    if args.run_all:
        run_all()
    elif args.file_idx is not None:
        if args.visualize:
            visualize_layout(args.file_idx)
        else:
            gen_layout(args.file_idx)
    else:
        print("Please provide either --run_all or --file_idx")


if __name__ == "__main__":
    main()
