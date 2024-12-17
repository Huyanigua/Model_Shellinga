import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib.colors import ListedColormap


# генерируем изначальную сетку в виде одномерного списка
def generate_grid(n):
    all_cells = n*n
    blue = int(all_cells*0.45)
    red = int(all_cells*0.45)
    empty = all_cells - blue - red
    cells = [0]*empty + [1]*red + [2]*blue
    random.shuffle(cells)
    return cells


# алгоритм проверки соседей
def neighbours(cell):
    counter = 0
    if cell-n-1 >= 0 and (cell-n-1)//n == (cell-n)//n:
        if grid[cell-n-1] == grid[cell]:
            counter += 1
    if cell-n >= 0:
        if grid[cell-n] == grid[cell]:
            counter += 1
    if cell-n+1 >= 0 and (cell-n+1)//n == (cell-n)//n:
        if grid[cell-n+1] == grid[cell]:
            counter += 1
    if cell-1 >= 0 and (cell-1)//n == cell//n:
        if grid[cell-1] == grid[cell]:
            counter += 1
    if cell+1 < len(grid) and (cell+1)//n == cell//n:
        if grid[cell+1] == grid[cell]:
            counter += 1
    if cell+n-1 < len(grid) and (cell+n-1)//n == (cell+n)//n:
        if grid[cell+n-1] == grid[cell]:
            counter += 1
    if cell+n < len(grid):
        if grid[cell+n] == grid[cell]:
            counter += 1
    if cell+n+1 < len(grid) and (cell+n+1)//n == (cell+n)//n:
        if grid[cell+n+1] == grid[cell]:
            counter += 1
    if counter < 2:
        return True
    else:
        return False


# составление списка несчастных клеток
def unhappy():
    unhappy_list = []
    for cell in range(len(grid)):
        if grid[cell] == 0:
            continue
        if neighbours(cell):
            unhappy_list.append(cell)
    return unhappy_list


# задаём размеры квадрата
n = int(input("Введите размер квадрата: "))
grid = generate_grid(n)
startgrid = grid.copy()
# генерим список для пустых клеток
empty_cells = []
for i in range(len(grid)):
    if grid[i] == 0:
        empty_cells.append(i)

# цикл для перестановки
unhappy_positions = unhappy()
while unhappy_positions:
    r_unhappy_pos = random.choice(unhappy_positions)
    r_empty_pos = random.choice(empty_cells)
    empty_cells.remove(r_empty_pos)
    empty_cells.append(r_unhappy_pos)
    grid[r_unhappy_pos], grid[r_empty_pos] = grid[r_empty_pos], grid[r_unhappy_pos]
    unhappy_positions = unhappy()


# рисуем две области - до преобразований и после
colors = ['white', 'red', 'blue']
cmap = ListedColormap(colors)
color_indices1 = np.array(startgrid).reshape(n, n)
color_indices2 = np.array(grid).reshape(n, n)
# создаем фигуру и оси
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(color_indices1, cmap=cmap, origin='upper')
axes[1].imshow(color_indices2, cmap=cmap, origin='upper')
axes[0].axis('off')
axes[1].axis('off')
axes[0].set_title('Начальная сетка')
axes[1].set_title('Итоговая сетка')
plt.show()
