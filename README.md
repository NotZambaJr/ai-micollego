# [**AI-MiCollego**](https://github.com/NotZambaJr/ai-micollego.git)
A **FREE algorithm** designed to train and utilize a simple graphical interface for YOLO v11. Please use it responsibly, ensuring compliance with any relevant ethical or legal guidelines.

---

## **Imports**
AI-MiCollego simplifies dependency management by adopting a method similar to the `package.json` format commonly used in web applications. This approach allows for an intuitive and structured way of handling imports.

### **Importing Dependencies**
To import all dependencies defined in a JSON file, use the following command:

```python
manager.importALL(*JSON)
```

This command reads the dependencies from a JSON file and dynamically imports them. 

### **How It Works**
The `importALL` function allows you to define dependencies in a JSON-like structure, offering flexibility and simplicity in managing your project. 

Here’s an example JSON file:

#### Example: Importing External Packages
```json
{
  "dependencies": {
    "numpy": [],
    "pandas": []
  }
}
```
In this example:
- `numpy` and `pandas` are imported as standard modules.

#### Example: Importing Local Files
If you want to import a local file located in the `src` folder (e.g., `example.py`), you can specify it like this:

```json
{
  "dependencies": {
    "./example.py": []
  }
}
```
This will dynamically import the `example.py` file as a module.

---

### **Advanced Import Options**
If you need to import specific functions, classes, or submodules, you can define them explicitly in the JSON file:

#### Example: Importing Specific Functions or Classes
For syntax like:
```python
from your_package import your_function
```
The JSON configuration would look like this:
```json
{
  "dependencies": {
    "your_package": [
      "your_function"
    ]
  }
}
```
This imports only the `your_function` from `your_package`.

---

### **Full Flexibility with JSON Files**
If you want to dynamically load dependencies from a custom JSON file, you can specify the file path as an argument in the `importALL` function:

```python
manager.importALL(*your_json_file)
```

#### Default Behavior
By default, the application looks for a JSON file at:
```
src/assets/data.json
```
If you don’t want to use this file, ensure it is empty or avoid specifying redundant modules in it.



##
##
##
##

## **Dataset**
The `Dataset` class simplifies dataset management by providing tools to download datasets from Roboflow, generate datasets using webcam input, and update datasets asynchronously.

---

## Key Features

1. **Download Datasets**: Fetch datasets from Roboflow with ease.
2. **Generate Datasets**: Capture and save images using your webcam.
3. **Update Datasets**: Automatically update datasets and manage old files.
4. **Parameter Management**: Load and utilize dataset parameters from JSON files.

---

## Methods

#### `getDataset(api_key, workspace, project, v=1, yolo='yolov11')`
**Purpose:** Downloads a dataset from Roboflow.  
**Parameters:**  
- `api_key` (str): Your Roboflow API key.  
- `workspace` (str): Roboflow workspace name.  
- `project` (str): Project name within the workspace.  
- `v` (int): Dataset version (default: `1`).  
- `yolo` (str): Dataset format (default: `'yolov11'`).  
**Usage:**  
```python
dataset = Dataset.getDataset("your_api_key", "workspace", "project", v=2, yolo="yolov5")
```
Before continuing make sure your `Roboflow` credentials are correct:

The JSON configuration would look like this:


```json
{
  "roboflow": {
    "api_key": "your_api_key",
    "workspace" : "your_workspace_name",
    "project": "your_project_name",
    "version": 1.0,
    "yolo": "your_yolo_version"
}
```

 `default for yolo: yolov11`
    

### `generateDataset()`
**Purpose:** Captures images from a webcam and saves them in the `datasets` folder.  
**Workflow:**  
- Press `ESC` to exit.  
- Press `S` to save the current frame.  
**Usage:**  
```python
Dataset.generateDataset()
```

##

### `updateDataset(interval="86400")`
**Purpose:** Updates the dataset by deleting old files and downloading a new version. Runs asynchronously.  
**Parameters:**  
- `interval` (str): Time (in seconds) before the next update (default: `86400`).  
**Usage:**  
```python
import asyncio
asyncio.run(Dataset().updateDataset(interval="3600"))
```

##

### `getParams(*JSON)`
**Purpose:** Loads dataset parameters from a JSON file. Defaults to `assets/data.json`.  
**Usage:**  
```python
params = Dataset.getParams("path/to/config.json")
```

##

### `delete(directory_path)`
**Purpose:** Deletes all files in a specified directory.  
**Usage:**  
```python
await Dataset.delete("datasets/base")
```

---

## Example Usage

```python
from dataset import Dataset
import asyncio

# Initialize Dataset class
d = Dataset()

# Fetch parameters
params = Dataset.getParams("config.json")

# Download a dataset
dataset = Dataset.getDataset(
    api_key=params["api_key"],
    workspace=params["workspace"],
    project=params["project"],
    v=1,
    yolo="yolov11"
)

# Generate a dataset using webcam
Dataset.generateDataset()

# Update the dataset asynchronously
asyncio.run(d.updateDataset("3600"))
```

---

