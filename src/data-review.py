from util import Box, read_csv
import matplotlib.pyplot as plt

def draw_side_length_histogram(boxes):
    lengths_and_widths = [box.length for box in boxes] + [box.width for box in boxes]
    bins = range(0, max(lengths_and_widths) + 15, 15)
    plt.hist(lengths_and_widths, bins=bins, color='purple', alpha=0.7)
    plt.title('Distribution of Box Side Lengths')
    plt.xlabel('Side Length')
    plt.ylabel('Frequency')
    plt.xticks(bins)
    plt.show()


def draw_width_length_ratio_histogram(boxes):
    ratios = [box.width / box.length for box in boxes if box.length != 0]
    bins = [i * 0.1 for i in range(int(max(ratios) * 10) + 2)]
    plt.hist(ratios, bins=bins, color='blue', alpha=0.7)
    plt.title('Distribution of Width/Length Ratios')
    plt.xlabel('Width/Length Ratio')
    plt.ylabel('Frequency')
    plt.xticks(bins)
    plt.show()


def draw_square_distribution_histogram(boxes):
    squares = [box.length * box.width for box in boxes]
    bins = range(0, max(squares) + 100, 100)
    plt.hist(squares, bins=bins, color='green', alpha=0.7)
    plt.title('Distribution of Box Areas')
    plt.xlabel('Area')
    plt.ylabel('Frequency')
    plt.xticks(bins)
    plt.show()

def main():
    boxes = read_csv("data/1.csv")
    draw_side_length_histogram(boxes)
    draw_width_length_ratio_histogram(boxes)
    # draw_square_distribution_histogram(boxes)
    

if __name__ == "__main__":
    main()