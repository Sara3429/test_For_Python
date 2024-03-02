import os
import random
import shutil
# change POSCAR1 file
file_path = "/truba/home/modarresi/playground/test/game/POSCAR1"
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def write_file(file_path, lines):
    with open(file_path, 'w') as file:
        file.writelines(lines)

def process_POSCAR(poscar_lines):
    random.shuffle(poscar_lines[8:17])
    poscar_lines[8:11] = sorted(poscar_lines[8:11])
    poscar_lines[11:14] = sorted(poscar_lines[11:14])
    poscar_lines[14:17] = sorted(poscar_lines[14:17])
    return poscar_lines

def main():
    root_dir = '/truba/home/modarresi/playground/test/game'
    result_dir = '/truba/home/modarresi/playground/test/game/result'

    if not os.path.exists(result_dir + '1'):
        os.makedirs(result_dir + '1')

    if not os.path.exists(result_dir + '2'):
        os.makedirs(result_dir + '2')

    for i in range(1, 6):
        poscar1_lines = read_file(os.path.join(root_dir, 'POSCAR1'))
        poscar_lines = process_POSCAR(poscar1_lines)

        result_dir_i = result_dir + str(i)
        if not os.path.exists(result_dir_i):
            os.makedirs(result_dir_i)

        poscar_path = os.path.join(result_dir_i, 'POSCAR')
        write_file(poscar_path, poscar_lines)

        for file_name in ['INCAR', 'KPOINT', 'POTCAR', 'WALk']:
            shutil.copy(os.path.join(root_dir, file_name), result_dir_i)

        if i > 1:
            previous_poscar_path = os.path.join(result_dir + str(i-1), 'POSCAR')
            previous_poscar_lines = read_file(previous_poscar_path)
            if poscar_lines != previous_poscar_lines:
                shutil.copy(poscar_path, result_dir_i)
            else:
                while poscar_lines == previous_poscar_lines:
                    random.shuffle(poscar1_lines[8:17])
                    poscar_lines = process_POSCAR(poscar1_lines)
                    write_file(poscar_path, poscar_lines)
                    previous_poscar_lines = read_file(previous_poscar_path)

if __name__ == '__main__':
    main()
    
print("Process completed successfully.")     
