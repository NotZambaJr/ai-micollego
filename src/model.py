# noinspection PyUnresolvedReferences
class Model:
    from manager import run_once

    def __init__(self):
        print("Initializing Model")
        self.frame = None
        self.yolo_model = None
        self.Dataset=dataset.Dataset()
        self.generateData = None


    @staticmethod
    def train(yolo_model=YOLO("yolo11n.yaml"), dataset=r"/assets/datasets", cfg=100):
        results = yolo_model.train(
            data=dataset,
            epochs=cfg,
            imgsz=640,
            device='mps'
        )
        return results

    def predict(self, model="yolo11n.pt", stream="webcam", debug=True) -> None:
        from manager import Events
        if not Events.isUpdating.is_set():
            self.yolo_model=YOLO(model)
            if stream == "webcam":
                cap = cv2.VideoCapture(0)
                cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
                cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            else:
                cap = cv2.VideoCapture(str(stream))
            while cap.isOpened():
                success, self.frame = cap.read()
                if success:
                    results = self.yolo_model(self.frame, verbose=False)
                    annotated_frame = results[0].plot()

                    if Events.alredyFetched.is_set() is False & self.getTarget(self.yolo_model):
                        self.generateData = threading.Thread(
                            target=self.Dataset.generateDataset,
                            args=cap.read()
                        )
                        if self.generateData.is_alive() is False:
                            self.generateData.start()
                        elif Events.alredyFetched.is_set() is True:
                            self.generateData.join()

                    cv2.imshow("YOLO Inference", annotated_frame) if debug else None
                    if cv2.waitKey(1) & 0xFF == ord("q"):
                        break
                else:
                    print("Error reading frame")
                    break
            cap.release()
            cv2.destroyAllWindows()
            return
        else:
            print("Cannot run while fetching data")

    @staticmethod
    def getTarget(model, target="person"):
        if model.names[0] == str(target):
            return True
