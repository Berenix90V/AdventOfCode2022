def detect_visible_trees_in_a_direction(tree_array, begin, end):
    tallest_tree = 0
    visible_trees = [False for el in range(0, len(tree_array)) ]
    step = 1 if end > begin else -1
    for x in range(begin, end, step):
        current_tree = tree_array[x]
        if x == begin:
            visible_trees[x] = True
            tallest_tree = current_tree
        else:
            if current_tree > tallest_tree:
                visible_trees[x] = True
                tallest_tree = current_tree
                if current_tree == 9:
                    break
    return visible_trees


def visible_trees_in_array(trees_array):
    visible_trees_from_begin = detect_visible_trees_in_a_direction(trees_array, 0, len(trees_array)-1)
    visible_trees_from_end = detect_visible_trees_in_a_direction(trees_array, len(trees_array)-1, 0)
    return [i or j for i, j in zip(visible_trees_from_begin, visible_trees_from_end)]

def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = [[0 for row in range(rows)] for column in range(cols)]
    for row in range(rows):
        for col in range(cols):
            transposed[col][row] = matrix[row][col]
    return transposed

def count_visible_trees(visible_trees):
    return sum(map(sum, visible_trees))

def day8a(filepath):
    matrix = []
    
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            row=[]
            for digit in line:
                row.append(digit)
            matrix.append(row)

        visible_trees = []
        n_col = len(matrix[0])
        visible_trees = [[False for col in range(n_col)] for row in range(len(matrix))]
    
        for x in range(len(matrix)):
            visible_trees_in_row = visible_trees_in_array(matrix[x])
            visible_trees[x] = [i or j for i, j in zip(visible_trees_in_row, visible_trees[x])]

        t_matrix = transpose(matrix)
        t_visible_trees = transpose(visible_trees)

        for x in range(len(t_matrix)):
            visible_trees_in_col = visible_trees_in_array(t_matrix[x])
            t_visible_trees[x] = [i or j for i, j in zip(visible_trees_in_col, t_visible_trees[x])]
        
        visible_trees = transpose(t_visible_trees)

    return count_visible_trees(visible_trees)


print(day8a("day8_veronica.txt"))