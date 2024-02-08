import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def define_tree():
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(20)
    return root

def find_max_value(root):
    # Перевірка, чи дерево порожнє
    if root is None:
        return None
    
    # Йдемо праворуч вузлів, доки не знайдемо найбільше значення
    while root.right is not None:
        root = root.right
    
    # Повертаємо найбільше значення
    return root.value

def find_min_value(root):
    # Перевірка, чи дерево порожнє
    if root is None:
        return None
    
    # Йдемо ліворуч вузлів, доки не знайдемо найменше значення
    while root.left is not None:
        root = root.left
    
    # Повертаємо найменше значення
    return root.value

def tree_sum(root):
    # Перевірка, чи дерево порожнє
    if root is None:
        return 0
    
    # Рекурсивно обчислюємо суму лівого та правого піддерев
    left_sum = tree_sum(root.left)
    right_sum = tree_sum(root.right)
    
    # Повертаємо суму значень в поточному вузлі та суми лівого та правого піддерев
    return root.value + left_sum + right_sum

def plot_tree(ax, node, x, y, dx):
    if node is not None:
        ax.text(x, y, str(node.value), style='italic')
        if node.left is not None:
            ax.add_artist(FancyArrowPatch((x - 0.02, y - 0.05), (x - dx, y - 0.15), mutation_scale=20, arrowstyle='->', linestyle='solid', color='gray'))
            plot_tree(ax, node.left, x - dx, y - 0.2, dx / 2)
        if node.right is not None:
            ax.add_artist(FancyArrowPatch((x + 0.02, y - 0.05), (x + dx, y - 0.15), mutation_scale=20, arrowstyle='->', linestyle='solid', color='gray'))
            plot_tree(ax, node.right, x + dx, y - 0.2, dx / 2)

def visualize_tree(root):
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    plot_tree(ax, root, 0.5, 1, 0.4)
    plt.show()