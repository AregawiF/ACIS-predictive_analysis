import os

# Define the folder structure
folder_structure = {
    ".vscode": ["settings.json"],
    ".github/workflows": ["unittests.yml"],
    "src": ["__init__.py", "data_processing.py", "pipelines.py", "dashboard.py", "feature_store.py"],
    "notebooks": ["__init__.py", "README.md"],
    "tests": ["__init__.py", "test_data_processing.py", "test_pipelines.py", "test_dashboard.py", "test_feature_store.py"],
    "scripts": ["__init__.py", "database_setup.py", "run_dashboard.py"],
}

# Define files to be created in the root directory
root_files = [".gitignore", "requirements.txt", "README.md"]

def create_folders_and_files():
    # Create folder structure
    for folder, files in folder_structure.items():
        os.makedirs(folder, exist_ok=True)
        for file in files:
            file_path = os.path.join(folder, file)
            if not os.path.exists(file_path):
                with open(file_path, 'w') as f:
                    pass  # Create an empty file
    
    # Create root files
    for file in root_files:
        if not os.path.exists(file):
            with open(file, 'w') as f:
                pass  # Create an empty file
    
    print("Project structure created successfully.")

if __name__ == "__main__":
    create_folders_and_files()
