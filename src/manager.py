from src.dataset import enablePrint


# noinspection PyUnresolvedReferences
class Manager:

    def __init__(self):
        self.init = None

    @staticmethod
    def verbose():
        import sys
        if "-v" or "verbose" in list(sys.argv):
            enablePrint()
        else:
            disablePrint()

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

class Colors:
    cyan = '\033[96m'
    green = '\033[92m'
    warn = '\033[93m'
    fail = '\033[91m'
    end = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'


def importALL(*JSON):
    import json, importlib
    if JSON:
        with open(JSON, 'r') as f:
            dependencies = json.load(f).get("dependencies", {})
    else:
        with open("assets/data.json", 'r') as f:
            dependencies = json.load(f).get("dependencies", {})
    global_imports = {}
    for module, submodules in dependencies.items():
        try:
            imported_module = importlib.import_module(module)
            global_imports[module] = imported_module
            print(f"{Colors.green}correctly imported:{module}{Colors.end}")

            for submodule in submodules:
                try:
                    global_imports[submodule] = getattr(imported_module, submodule)
                    print(f"{Colors.green}correctly imported:{print} {submodule} from: {imported_module}{Colors.end}")
                except AttributeError:
                    print(f"{Colors.fail}Submodule {submodule} not found in {module}")
        except ImportError as e:
            print(f"{Colors.fail}Failed to import {module}: {e}")
    globals().update(global_imports)
    return global_imports, print(f"{Colors.underline}{Colors.cyan}imported modules: {global_imports}")

def main():
    manager = Manager()
    manager.verbose()
    manager.disableWarnings()
    importALL()
main()



