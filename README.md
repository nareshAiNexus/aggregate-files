# Aggregate Python Files into Markdown

This Python script, `aggregate.py`, is designed to consolidate Python files from subdirectories into Markdown files. Each Markdown file will contain the content of all Python files within a specific subdirectory, formatted with Markdown syntax for better readability and documentation purposes.

## How This Program Works

### 1. **Input Directory Structure**
The script expects an input directory containing subdirectories. Each subdirectory should include Python files (`.py`) that you want to aggregate into a single Markdown file.

Example input directory structure:
```
input_dir/
    subdir1/
        file1.py
        file2.py
    subdir2/
        file3.py
```

### 2. **Processing Steps**
1. The script takes the input directory path and the output directory path as arguments.
2. It identifies all subdirectories within the input directory.
3. For each subdirectory:
   - It locates all `.py` files.
   - Extracts the file names (without extensions) for labeling.
   - Reads the content of each `.py` file and formats it into Markdown.
4. A Markdown file is created for each subdirectory in the specified output directory. The file name corresponds to the subdirectory name.

### 3. **Output**
The output is a set of Markdown files, each containing:
- Section headers for each Python file.
- The Python file content wrapped in Markdown code blocks for syntax highlighting.

Example output for `subdir1.md`:
```markdown
## file1

```python
# Content of file1.py
```

## file2

```python
# Content of file2.py
```
```

## How to Run the Script

### Prerequisites
- Python 3.x installed.
- Ensure the input directory is structured as described above.
- Ensure the output directory exists.

### Steps
1. Place the script in your desired location.
2. Update the `input_dir` and `output_path` variables in the script to match your directory paths:
   ```python
   input_dir = "D:\\path\\to\\input_directory"
   output_path = "D:\\path\\to\\output_directory"
   ```
3. Run the script:
   ```bash
   python aggregate.py
   ```
4. Check the output directory for the generated Markdown files.

## Benefits of This Script

### 1. **Centralized Documentation**
By consolidating Python files into Markdown format, this script creates an organized and easily navigable document for each subdirectory, making it easier to understand and review code.

### 2. **Improved Collaboration**
Markdown files are Git-friendly and can be viewed directly on platforms like GitHub. This allows teams to easily review and discuss code.

### 3. **Enhanced Readability**
The use of Markdown formatting ensures syntax highlighting and a structured presentation of code, which improves readability and comprehension.

### 4. **Automated Workflow**
This script automates the otherwise manual and time-consuming task of creating documentation for Python files, saving developers time and effort.

### 5. **Cross-Project Applicability**
This script is adaptable to various projects with a similar file structure, making it a reusable tool for different Python projects.

## Example Use Case
Suppose you are working on a coding interview preparation repository with multiple algorithm examples organized by category. This script can:
- Aggregate all algorithm implementations from each category into separate Markdown files.
- Enable easy sharing and viewing of these implementations on GitHub or other platforms.

---

Feel free to use and adapt this script as needed. Contributions and suggestions for improvement are always welcome!

