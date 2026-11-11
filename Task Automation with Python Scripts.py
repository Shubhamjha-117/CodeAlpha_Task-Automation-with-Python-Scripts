from pathlib import Path
import shutil

image_types = {
    '.jpg': 'JPG',
    '.jpeg': 'JPEG',
    '.png': 'PNG'
}




source = Path("G:\\MY PICS")

successfully_moved = 0
skipped = 0
failed = 0
if source.exists() and source.is_dir():
    
    for file in source.rglob("*"):
        if file.is_file():
            ext = file.suffix.lower()
            if ext in image_types :
                target_dir = source/image_types[ext]
                target_dir.mkdir(parents = True,exist_ok= True)
                target_file = target_dir/file.name
            
                try:
                    if target_file.exists():
                        print(f"Skipped: {file.name} (already exists)")
                        skipped += 1
                        continue
                    else :
                        print(f"Moving Jpg Files :{file.name} -> {image_types[ext]}")
                        shutil.move(str(file),str(target_file))
                        successfully_moved += 1

                except OSError as e :
                    print(f"Error moving {file.name} : {e}")
                    failed +=1 
    if successfully_moved == 0 and skipped == 0 and failed == 0:
        print("No image files found to move.\n")
else:
    print("Source folder does not exist!")
print("\t\t Summary \n")
print(f"SuccessFully Moved Files : {successfully_moved}\n")
print(f"Skipped Files: {skipped}\n")
print(f"Failed Files: {failed}\n")
