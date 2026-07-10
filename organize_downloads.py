import os
import shutil

folder_path = 'C:\\Users\\dkmkelley\\Downloads'

file_types = {
    '3D Print Files': ['.stl', '.3mf', '.blend', '.blend1'],
    'Archives': ['.zip', '.tar', '.gz', '.7z'],
    'Disk Images': ['.img', '.iso'],
    'Documents': ['.pdf', '.doc', '.docx', 'xlsx', '.txt', 'md',],
    'Executables': ['.exe', '.bat', '.sh'],
    'Images': ['.jpg', '.png', '.gif', '.jpeg', '.bmp', '.tif', '.tiff', '.webp'],
    'Videos': ['.mp4', '.mkv', '.mov'],
    'Music': ['.mp3', '.wav']
}
    
    
def organize_folder():
    for root, _, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_ext = os.path.splitext(filename)[1].lower()
            for folder, extensions in file_types.items():
                if file_ext in extensions:
                    new_folder_path = os.path.join(folder_path, folder)

                    if os.path.commonpath([file_path, new_folder_path]) == new_folder_path:
                        break

                    if not os.path.exists(new_folder_path):
                        os.makedirs(new_folder_path)
                    shutil.move(file_path, new_folder_path)
                    print(f'Moved: {filename} -> {folder}')
                    break

organize_folder()
os.system('pause')