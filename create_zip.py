import zipfile
import os

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            if file == "create_zip.py" or ".git" in root or "KernelSU-Next-chopin.zip" in file or "README.md" in file:
                continue
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, path)
            ziph.write(file_path, arcname)

if __name__ == "__main__":
    zipf = zipfile.ZipFile('KernelSU-Next-chopin.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir('.', zipf)
    zipf.close()
    print("KernelSU-Next-chopin.zip created successfully.")
