import os
import shutil

def flatten_directory():
    # Get the current directory (where the script is run)
    current_dir = os.getcwd()
    
    # Create a new "flat" directory
    flat_dir = os.path.join(current_dir, "Flat")
    os.makedirs(flat_dir, exist_ok=True)
    
    # Walk through all subdirectories
    for root, dirs, files in os.walk(current_dir):
        # Skip the current directory and the "flat" directory itself
        if root == current_dir or root == flat_dir:
            continue
        
        # Process all files in the current subdirectory
        for file in files:
            source_path = os.path.join(root, file)
            dest_path = os.path.join(flat_dir, file)
            
            # If a file with the same name already exists, add a number to the filename
            counter = 1
            while os.path.exists(dest_path):
                name, ext = os.path.splitext(file)
                dest_path = os.path.join(flat_dir, f"{name}_{counter}{ext}")
                counter += 1
            
            # Copy the file
            shutil.copy(source_path, dest_path)
            print(f"Copied: {source_path} -> {dest_path}")

    print("Directory flattening complete. All files are now in the 'flat' folder.")

if __name__ == "__main__":
    flatten_directory()