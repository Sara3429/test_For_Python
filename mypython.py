import os
import shutil
import random
import filecmp

# تابع برای تغییر فایل POSCAR
def modify_POSCAR(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
        # تغییرات در خطوط ۹ تا ۱۷
        elements = ['A', 'B', 'C']
        random_lines = list(range(9, 18))
        random.shuffle(random_lines)
        
        for i, line_num in enumerate(random_lines[:3]):
            lines[line_num] = f'{elements[i]}\n'
        
        for i in range(3):
            lines[random_lines[i]] = f'{elements[i]}\n'
        
        with open(file_path, 'w') as file:
            file.writelines(lines)

# مسیر فایل‌های ورودی
input_dir = 'input_files'

# ساخت ۵ پوشه
for i in range(1, 6):
    result_dir = f'result{i}'
    os.makedirs(result_dir, exist_ok=True)
    
    # کپی فایل‌های ورودی به پوشه result
    for file_name in os.listdir(input_dir):
        shutil.copy(os.path.join(input_dir, file_name), result_dir)
    
    # تغییر فایل POSCAR
    modify_POSCAR(os.path.join(result_dir, 'POSCAR'))
    
    # مقایسه فایل POSCAR با فایل‌های قبلی و ذخیره نتایج
    if i > 1:
        for j in range(1, i):
            prev_result_dir = f'result{j}'
            poscar_new = os.path.join(result_dir, 'POSCAR')
            poscar_prev = os.path.join(prev_result_dir, 'POSCAR')
            
            if not filecmp.cmp(poscar_new, poscar_prev):
                shutil.copy(poscar_new, prev_result_dir)