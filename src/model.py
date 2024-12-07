# noinspection PyUnresolvedReferences
class Model:
    from ultralytics import YOLO
    def __init__(self):
        print("Initializing Model")

    @staticmethod
    def train(yolo_model=YOLO("yolo11n.yaml"), dataset=r"/assets/datasets", cfg=100):
        results = yolo_model.train(
            data=dataset,
            epochs=cfg,
            imgsz=640,
            device='mps'
        )
        return results

    @staticmethod #at least for now!
    def predict(self):
        print("Predicting...")
        #ON TO DO!