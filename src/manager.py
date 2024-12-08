# noinspection PyUnresolvedReferences
import json, importlib, sys, builtins, threading
from pathlib import Path

class Manager:

    def __init__(self):
        self.init = None
        self.global_shared_namespace = {}

    def verbose(self):
        import sys
        if "-v" or "verbose" in list(sys.argv):
            self.enablePrint()
        else:
            self.disablePrint()

    @staticmethod
    def enablePrint():
        sys.stdout = sys.__stdout__

    @staticmethod
    def disablePrint():
        sys.stdout = open(os.devnull, 'w')

    @staticmethod
    def disableWarnings():
        import warnings
        warnings.filterwarnings('ignore')

class Events:
    isUpdating = threading.Event()
    alredyFetched = threading.Event()

def run_once(f):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args, **kwargs)
    wrapper.has_run = False
    return wrapper

@run_once
def importALL(*JSON, base_dir=None, make_global_in=None):
    # Load dependencies from JSON file
    if JSON:
        with open(JSON, 'r') as f:
            dependencies = json.load(f).get("dependencies", {})
    else:
        with open("assets/data.json", 'r') as f:
            dependencies = json.load(f).get("dependencies", {})

    global_imports = {}

    # Add base_dir to sys.path if specified
    if base_dir:
        base_dir_path = Path(base_dir).resolve()
        if str(base_dir_path) not in sys.path:
            sys.path.append(str(base_dir_path))

    # Process each dependency
    for module, submodules in dependencies.items():
        try:
            if module.endswith('.py'):  # Import local files
                module_path = Path(module).resolve()
                module_name = module_path.stem
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                imported_module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(imported_module)
                global_imports[module_name] = imported_module
                print(f"Successfully imported: {module}")
            else:  # Import standard or installed packages
                imported_module = importlib.import_module(module)
                global_imports[module] = imported_module
                print(f"Successfully imported: {module}")

                # Import specific submodules/functions if defined
                for submodule in submodules:
                    try:
                        global_imports[submodule] = getattr(imported_module, submodule)
                        print(f"Successfully imported: {submodule} from {module}")
                    except AttributeError:
                        print(f"Submodule {submodule} not found in {module}")
        except ImportError as e:
            print(f"Failed to import {module}: {e}")
        except FileNotFoundError as e:
            print(f"File {module} not found: {e}")

    # Update the builtins namespace for global access
    for name, module in global_imports.items():
        setattr(builtins, name, module)

    print("Successfully imported all modules globally.")
    return global_imports


def init():
    global global_imports, yolo_model
    manager = Manager()
    manager.disableWarnings()
    manager.enablePrint()
    manager.verbose()
    importALL(make_global_in="/src")

init()
def main():
    import model
    yolo_model = model.Model()
    yolo_model.predict()
main()










