from TreeNode import define_tree, find_max_value, find_min_value, tree_sum,visualize_tree

# Створення дерева
root = define_tree()

# Знаходження найбільшого значення
max_value = find_max_value(root)
print("Task 01: Найбільше значення в дереві:", max_value)

# Знаходження найменшого значення
min_value = find_min_value(root)
print("Task 02: Найменше значення в дереві:", min_value)

# Обчислення суми значень у дереві
total_sum = tree_sum(root)
print("Task 03: Сума всіх значень у дереві:", total_sum)

# Базова візуалізація дерева
visualize_tree(root)