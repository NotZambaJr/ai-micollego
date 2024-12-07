# noinspection PyUnres\olvedReferences
class Dataset:
    def __init__(self):
        print("successfully imported class Dataset")

    @staticmethod
    def getDataset(api_key, workspace, project, v=1, yolo='yolov11'):
        rf = Roboflow(api_key=str(api_key))
        project = rf.workspace(str(workspace)).project(str(project))
        version = project.version(v)
        dataset = version.download(str(yolo))
        return dataset

    # noinspection PyUnresolvedReferences
    @staticmethod
    def _getImageSize(img) -> int:
        width = cv2.imread(img).shape[1]
        return width

    # noinspection PyUnresolvedReferences
    @staticmethod
    def generateDataset():
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print(f"failed to open camera")
        dir = 'datasets'
        os.makedirs(dir, exist_ok=True)
        img = 0
        while img < 20:
            ret, frame = cap.read()
            if not ret:
                print(f"failed to grab frame")
                break
            cv2.imshow("current input", frame)
            key = cv2.waitKey(1) & 0xFF
            if key%256 == 27:
                print(f"manually exited from: {dir}/{img}")
                break
            elif key%256 == ord('s'):
                name = os.path.join(dir, f"opencv_frame_{img}.png")
                cv2.imwrite(name, frame)
                print(f"frame saved to {name}")
                img += 1
        print("images fetched correctly")

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
        except OSError:
            print("Error occurred while deleting files.")
        return
