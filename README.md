# [**AI-MiCollego**](https://github.com/NotZambaJr/ai-micollego.git)

AI-MiCollego is a **FREE algorithm** designed to train and use a simple graphical interface for YOLO v11. Please use it responsibly, ensuring compliance with ethical and legal guidelines.

---

## **Imports**

AI-MiCollego simplifies dependency management with a method similar to `package.json` used in web applications. This approach allows for intuitive and structured handling of dependencies.

### **Importing Dependencies**
To import dependencies from a JSON file, use:
```python
manager.importALL(*JSON)
```

#### Example JSON for External Packages
```json
{
  "dependencies": {
    "numpy": [],
    "pandas": []
  }
}
```

#### Example JSON for Local Files
```json
{
  "dependencies": {
    "./example.py": []
  }
}
```

### **Advanced Import Options**
For specific imports like:
```python
from your_package import your_function
```
Use this JSON structure:
```json
{
  "dependencies": {
    "your_package": ["your_function"]
  }
}
```

### Default Behavior
By default, the application looks for dependencies in:
```
src/assets/data.json
```

---

## **Dataset Management**

The `Dataset` class provides tools for:
1. **Downloading Datasets**: Fetch datasets from Roboflow.
2. **Generating Datasets**: Capture images from a webcam.
3. **Updating Datasets**: Automate dataset updates and cleanups.
4. **Parameter Management**: Load configuration from JSON files.

### **Methods**

#### `getDataset(api_key, workspace, project, v=1, yolo='yolov11')`
**Purpose**: Downloads a dataset from Roboflow.  
**Usage**:
```python
dataset = Dataset.getDataset("api_key", "workspace", "project", v=1, yolo="yolov11")
```

#### JSON Example for Roboflow Parameters
```json
{
  "roboflow": {
    "api_key": "your_api_key",
    "workspace": "workspace_name",
    "project": "project_name",
    "version": 1,
    "yolo": "yolov11"
  }
}
```

---

#### `generateDataset()`
**Purpose**: Captures images from a webcam and saves them in the `datasets` folder.  
- Press `ESC` to exit.
- Press `S` to save a frame.  
**Usage**:
```python
Dataset.generateDataset()
```

---

#### `updateDataset(interval="86400")`
**Purpose**: Deletes old files and downloads new datasets asynchronously.  
**Usage**:
```python
import asyncio
asyncio.run(Dataset().updateDataset(interval="3600"))
```

---

#### `getParams(*JSON)`
**Purpose**: Loads configuration parameters from a JSON file. Defaults to `assets/data.json`.  
**Usage**:
```python
params = Dataset.getParams("path/to/config.json")
```

---

#### `delete(directory_path)`
**Purpose**: Deletes all files in a directory.  
**Usage**:
```python
await Dataset.delete("datasets/base")
```

---

### **Example Usage**

```python
from dataset import Dataset
import asyncio

# Initialize Dataset
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

# Generate a dataset using the webcam
Dataset.generateDataset()

# Update datasets asynchronously
asyncio.run(d.updateDataset("3600"))
```

---

## **YOLO Model Interaction**

AI-MiCollego simplifies interactions with YOLO models, making them more intuitive and user-friendly.

### **Prediction**
```python
def predict(
    self, 
    model="yolo11n.pt", 
    stream="webcam", 
    debug=True
) -> None:
```
**Purpose**: Run object detection using YOLO.  
- `model`: Path to the YOLO model (default: `yolo11n.pt`).  
- `stream`: Input source (default: `webcam`; for video: `path/to/video.mp4`).  
- `debug`: Displays a CV2 dialog window with detection results.  

#### Example Workflow
A thread captures images for training when a target is detected:

```python
self.generateData = threading.Thread(
    target=self.Dataset.generateDataset,
    args=cap.read()
)
if not self.generateData.is_alive():
    self.generateData.start()
elif Events.alreadyFetched.is_set():
    self.generateData.join()
```
_Default Limit_: Captures up to 20 images for training.  

#### JSON for Custom Limit
```json
{
  "vars": {
    "limit": your_custom_limit
  }
}
```

---

### **GetTarget**
```python
@staticmethod
def getTarget(model, target="person"):
    return model.names[0] == str(target)
```
**Purpose**: Checks if the model detects the specified target in the frame.  
**Returns**: `True` if the target is detected.

---

## **Dependencies**

Install required dependencies:
```bash
pip install sympy opencv-python roboflow torch ultralytics 
```

---

## **Notes**
- Ensure your `Roboflow` credentials are correct.
- Configure `cv2` for webcam access if needed.
- Adjust image limits via the JSON configuration for training flexibility.

--- 