import os
import random
import shutil

# Function to generate random positions for A, B, and C elements
def generate_random_positions():
    positions = []
    for _ in range(3):
        random_positions = random.sample(range(1, 10), 3)
        positions.append(random_positions)
    return positions

# Function to update POSCAR file with random positions for A, B, and C elements
def update_POSCAR(file_path, positions):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for i, pos in enumerate(positions):
        for j, p in enumerate(pos):
            lines[j+7+i*3] = lines[j+7+i*3][:30] + f' {p}\n'

    with open(file_path, 'w') as file:
        file.writelines(lines)

# Main program
for i in range(1, 1001):
    result_dir = f'result{i}'
    os.makedirs(result_dir, exist_ok=True)

    if i == 1:
        shutil.copy('POSCAR', f'{result_dir}/POSCAR')
    else:
        new_positions = generate_random_positions()
        update_POSCAR(f'{result_dir}/POSCAR', new_positions)

    shutil.copy('INCAR', f'{result_dir}/INCAR')
    shutil.copy('KPOINT', f'{result_dir}/KPOINT')
    shutil.copy('POTCAR', f'{result_dir}/POTCAR')

    os.chdir(result_dir)
    os.system('vasp') # Run VASP code

    if i > 1:
        previous_dir = f'result{i-1}'
        if not filecmp.cmp('POSCAR', f'{previous_dir}/POSCAR'):
            shutil.copy('POSCAR', f'{result_dir}/POSCAR')
            os.system('vasp')

    os.chdir('..')