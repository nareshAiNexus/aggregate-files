import os
from pathlib import Path

def aggregate(input_dir, output_path):
    # Input directory containing Python files
    dir_names = [item for item in os.listdir(input_dir)]
    
    os.chdir(input_dir)
    for i in range(len(dir_names)):

        current_dir = Path.cwd() / dir_names[i]  # Renamed from input_dir to current_dir

        # List all Python files in the directory
        files = list(current_dir.glob("*.py"))

        # Extract file names without extensions
        file_names = [file.stem for file in files]

        # Initialize content for the Markdown file
        content = ""

        # Process each Python file
        for j, file in enumerate(files):
            with file.open("r", encoding="utf-8") as f:
                content += f"## {file_names[j]} \n"
                content += "\n```python\n"
                content += f.read()
                content += "\n```\n"

        # Write the aggregated content to a Markdown file
        output_file = output_path + "\\" + dir_names[i] + ".md"
        with open(output_file, "w", encoding="utf-8") as md:
            md.write(content)


input_dir = input("Location were all the python files locates: ")
output_path = input("Location to save all the md files : ")
aggregate(input_dir, output_path)
