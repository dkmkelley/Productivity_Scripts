import os
import shutil

folder_path = 'C:\\Users\\dkmkelley\\Downloads'

file_types = {
    'Images': ['.jpg', '.png', '.gif', '.jpeg', '.bmp', '.tif', '.tiff', '.webp'],
    'Documents': ['.pdf', '.doc', '.docx', 'xlsx', '.txt', 'md',],
    'Videos': ['.mp4', '.mkv', '.mov'],
    'Music': ['.mp3', '.wav'],
    'Archives': ['.zip', '.tar', '.gz', '.7z'],
    'Executables': ['.exe', '.bat', '.sh'],
    '3D Print Files': ['.stl', '.3mf', '.blend', '.blend1'],
    'Disk Images': ['.img', '.iso']
}

def organize_folder():
    for filename in os.listdir(folder_path):
        file_ext = os.path.splitext(filename)[1].lower()
        for folder, extensions in file_types.items():
            if file_ext in extensions:
                new_folder_path = os.path.join(folder_path, folder)
                if not os.path.exists(new_folder_path):
                    os.makedirs(new_folder_path)
                shutil.move(os.path.join(folder_path, filename), new_folder_path)
                print(f'Moved: {filename} -> {folder}')
                break

organize_folder()
os.system('pause')