# noinspection PyUnres\olvedReferences
from manager import Events
import time
class Dataset:
    def __init__(self):
        print("successfully imported class Dataset")
        self.img = 0
        self.processStarted = False
        with open("assets/data.json", 'r') as f:
            self.limit = json.load(f).get("vars", {})

    @staticmethod
    def getDataset(api_key, workspace, project, v=1, yolo='yolov11'):
        Events.isUpdating.set()
        rf = Roboflow(api_key=str(api_key))
        project = rf.workspace(str(workspace)).project(str(project))
        version = project.version(v)
        dataset = version.download(str(yolo))
        if Events.isUpdating.is_set():
            Events.isUpdating.clear()
        return dataset

    # noinspection PyUnresolvedReferences
    @staticmethod
    def _getImageSize(img) -> int:
        width = cv2.imread(img).shape[1]
        return width

    # noinspection PyUnresolvedReferences
    def generateDataset(self, success, frame: any) -> None:
        Events.alredyFetched.set()
        _dir = 'local'
        os.makedirs(_dir, exist_ok=True)
        print(self.img)
        while self.img < int(self.limit["limit"]):
            name = os.path.join(_dir, f"opencv_frame_{self.img}.png")
            cv2.imwrite(name, frame)
            print(f"frame saved to {name}")
            self.img += 1
            time.sleep(2)

        else:
            print(f"images alredy fetched: {self.img}")
            time.sleep(5)
        return

    #noinspection PyUnresolvedReferences
    async def updateDataset(self, interval="86400") -> [bool, any]:
        await self.delete('datasets/base')
        self.getDataset(
            self.getParams()['api_key'],
            self.getParams()['workspace'],
            self.getParams()['project'],
            self.getParams()['v'],
            self.getParams()['yolo']
            )
        print("successfully updated dataset")
        return True, time.sleep(interval)

    #noinspection PyUnresolvedReferences
    @staticmethod
    def getParams(*JSON):
        import json
        try:
            if JSON:
                with open(JSON, 'r') as f:
                    params = json.load(f).get("roboflow", {})
            else:
                with open("assets/data.json", 'r') as f:
                    params = json.load(f).get("roboflow", {})
            print("correctly fetched parameters")
        except Exception as e:
            print(f"Error importing Params: {e}")
        return params

    #noinspection PyUnresolvedReferences
    @staticmethod
    async def delete(directory_path) -> None:
        try:
            files = os.listdir(directory_path)
            for file in files:
                file_path = os.path.join(directory_path, file)
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    Events.alredyFetched.clear()
        except OSError:
            print("Error occurred while deleting files.")
        return
