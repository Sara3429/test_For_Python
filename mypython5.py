import os
import shutil
import random
import filecmp

# change POSCAR file
def modify_POSCAR(/truba/home/modarresi/playground/test/game/POSCAR):
    with open(/truba/home/modarresi/playground/test/game/POSCAR , 'r') as file:
        lines = file.readlines()
        
        #  change in line between 9 - 17
        elements = ['A', 'B', 'C']
        random_lines = list(range(9, 18))
        random.shuffle(random_lines)
        
        for i, line_num in enumerate(random_lines[:3]):
            lines[line_num] = f'{elements[i]}\n'
        
        for i in range(3):
            lines[random_lines[i]] = f'{elements[i]}\n'
        
        with open(file_path, 'w') as file:
            file.writelines(lines)

# path of input file
input_dir = 'input_files'

# make 5 directory
for i in range(1, 6):
    result_dir = f'result{i}'
    os.makedirs(result_dir, exist_ok=True)
    
    # copy input files in result directory
    for file_name in os.listdir(input_dir):
        shutil.copy(os.path.join(input_dir, file_name), result_dir)
    
    # change POSCAR file
    modify_POSCAR(os.path.join(result_dir, 'POSCAR'))
    
    # compare POSCAR file with privious POSCAR Files
    if i > 1:
        for j in range(1, i):
            prev_result_dir = f'result{j}'
            poscar_new = os.path.join(result_dir, 'POSCAR')
            poscar_prev = os.path.join(prev_result_dir, 'POSCAR')
            
            if not filecmp.cmp(poscar_new, poscar_prev):
                shutil.copy(poscar_new, prev_result_dir)
