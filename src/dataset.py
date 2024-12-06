class Colors: cyan = '\033[96m'


green = '\033[92m'
warn = '\033[93m'
fail = '\033[91m'
end = '\033[0m'
bold = '\033[1m'
underline = '\033[4m'


class Manager: def


main(self) -> None: self.disableWarnings()
self.importALL()
m = YOLO("yolo11n.pt")
print(m)


def __init__(self): self.dependencies = None


def importALL(self, *JSON: str) -> bool: import importlib, json


self.dependencies = (json.load(open("assets/data.json")))["dependencies"] \ if json.load(
    open("assets/data.json")) else[JSON] if self.dependencies: try: for dependency in self.dependencies: if
self.dependencies[str(dependency)]: importlib.import_module(str(dependency), self.dependencies[str(dependency)])
print(f"{Colors.cyan}correctly imported {dependency}") else: importlib.import_module(str(dependency))
print(f"{Colors.cyan}correctly imported {dependency}") except Exception as e: print(
    f"{Colors.fail}{Colors.underline}Error importing dependency: {e}")
return False
print(f"{Colors.green}{Colors.underline}correctly imported all dependencies")
del self.dependencies
return True @ staticmethod


def enablePrint(): sys.stdout = sys.__stdout__ @ staticmethod


def disablePrint(): sys.stdout = open(os.devnull, 'w') @ staticmethod


def disableWarnings(): import warnings


warnings.filterwarnings('ignore')
manager = Manager()
manager.main()