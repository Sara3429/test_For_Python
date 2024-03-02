import os
import random
import shutil
import string
import filecmp

base_dir = '/truba/home/modarresi/playground/test/game'
# change POSCAR1 file
file_path = "/truba/home/modarresi/playground/test/game/POSCAR1"
def read_lines_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def write_lines_to_file(file_path, lines):
    with open(file_path, 'w') as file:
        file.writelines(lines)

def generate_random_letters(num_letters, letters):
    return random.choices(letters, k=num_letters)

def main():
    letters = ['A', 'B', 'C']
    
    for i in range(1, 6):
        result_dir = os.path.join(base_dir, f'result{i}')
        os.makedirs(result_dir, exist_ok=True)
        
        poscar1_lines = read_lines_from_file(os.path.join(base_dir, 'POSCAR1'))
        random_letters = generate_random_letters(9, letters) + generate_random_letters(6, letters) + generate_random_letters(3, letters)
        
        for j in range(9):
            poscar1_lines[j] = random_letters[j] + '\n'
        
        random.shuffle(random_letters)
        for j in range(9):
            poscar1_lines[j+9] = random_letters[j] + '\n'
        
        random.shuffle(random_letters)
        for j in range(9):
            poscar1_lines[j+15] = random_letters[j] + '\n'
        
        write_lines_to_file(os.path.join(result_dir, 'POSCAR'), poscar1_lines)
        
        shutil.copy(os.path.join(base_dir, 'INCAR'), result_dir)
        shutil.copy(os.path.join(base_dir, 'KPOINT'), result_dir)
        shutil.copy(os.path.join(base_dir, 'POTCAR'), result_dir)
        shutil.copy(os.path.join(base_dir, 'WALK'), result_dir)
        
if __name__ == '__main__':
    main()
    
print("Process completed successfully.")    
