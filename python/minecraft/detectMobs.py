import os

import cv2
import numpy as np
import onnxruntime as ort
import pygetwindow as gw
import pyautogui
import time

base_dir = os.path.dirname(os.path.realpath(__file__))
model_path = os.path.join(base_dir, "yoloFiles/best.onnx")


class DetectMobs:
    """Detect Mobs(Zombie, Skeleton) location with image regognition"""

    def __init__(
        self,
        img_path=None,
        capture_path="yoloFiles/capture.png",
        txt_path="yoloFiles/labels/capture.txt",
        input_img_size=640,
        is_save_result=False,
        vertical_split_num=5,
        horizontal_split_num=3,
        confidence=0.6,
    ):
        self.img_path = img_path
        self.capture_path = os.path.join(base_dir, capture_path)
        self.txt_path = os.path.join(base_dir, txt_path)
        self.input_img_size = input_img_size
        self.is_save_result = is_save_result
        self.vertical_split_num = vertical_split_num
        self.horizontal_split_num = horizontal_split_num
        self.confidence = confidence

        # load onnx model
        self.ort_session = ort.InferenceSession(model_path)

    def capture_img(self):
        window_title = "Minecraft Education"
        window = gw.getWindowsWithTitle(window_title)[0]
        window_location = (window.left, window.top, window.width, window.height)
        window_image = pyautogui.screenshot(region=window_location)
        window_image = cv2.cvtColor(np.array(window_image), cv2.COLOR_BGR2RGB)

        return window_image

    def preprocess_image(self):
        """to load and preprocess images"""
        if self.img_path is None:
            img = self.capture_img()
        else:
            img = cv2.imread(self.img_path)
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # if we need to save result of img
        if self.is_save_result is True:
            cv2.imwrite(self.capture_path, img)
        img_resized = cv2.resize(img_rgb, (self.input_img_size, self.input_img_size))
        img_normalized = img_resized / 255.0  # standarzation to 0-1
        img_transposed = np.transpose(img_normalized, (2, 0, 1))  # HWC->CHW

        return np.expand_dims(img_transposed, axis=0).astype(np.float32)

    def draw_result(self, bboxes):
        """
        draw result(bbox, splitline, center) on input image

        Args:
            bboxes (list): coordinations of bboxes
        """
        img = cv2.imread(self.capture_path)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h, w, _ = img_rgb.shape

        for bbox in bboxes:
            x_center, y_center, width, height = bbox
            # Rescale the bbox to original image size
            x_center = x_center * w / self.input_img_size
            y_center = y_center * h / self.input_img_size
            width = width * w / self.input_img_size
            height = height * h / self.input_img_size

            x_min = int(x_center - width / 2.0)
            y_min = int(y_center - height / 2.0)
            x_max = int(x_center + width / 2.0)
            y_max = int(y_center + height / 2.0)

            # draw red color bbox
            cv2.rectangle(img_rgb, (x_min, y_min), (x_max, y_max), (255, 0, 0), 2)
            # draw center point
            cv2.circle(
                img_rgb,
                center=(int(x_center), int(y_center)),
                radius=5,
                color=(0, 0, 255),
                thickness=-1,
            )

        # draw spliting lines
        for i in range(self.horizontal_split_num):
            line_h = int(i * h / self.horizontal_split_num)
            cv2.line(
                img_rgb,
                pt1=(0, line_h),
                pt2=(w, line_h),
                color=(0, 255, 0),
                thickness=3,
            )
        for i in range(self.vertical_split_num):
            line_w = int(i * w / self.vertical_split_num)
            cv2.line(
                img_rgb,
                pt1=(line_w, 0),
                pt2=(line_w, h),
                color=(0, 255, 0),
                thickness=3,
            )

        # save image which is result of anotation
        cv2.imwrite(self.capture_path, cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR))

    def show_result_img(self):
        img = cv2.imread(self.capture_path)
        cv2.imshow("result_img", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def write_result_to_text(self, bboxes, classes):
        with open(self.txt_path, encoding="UTF-8", mode="w") as f:
            results = self.calc_location(bboxes, classes)
            for result in results:
                f.write(str(result))
                f.write("\n")

    def calc_location(self, bboxes, classes):
        """calculate location on spliting image

        Args:
            bboxes (list): coordinations of mobs
            classes (list): classification of mobs

        Returns:
            ndarray : locations
        """
        results = np.full(self.horizontal_split_num * self.vertical_split_num, -1)

        for i, bbox in enumerate(bboxes):
            x_center, y_center, _, _ = bbox
            x_position = int(x_center / self.input_img_size * self.vertical_split_num)
            y_position = int(y_center / self.input_img_size * self.horizontal_split_num)
            index = y_position * self.vertical_split_num + x_position
            if results[index] != -1:
                if results[index] != classes[i]:
                    results[index] = 9
            else:
                results[index] = classes[i]

        return results

    def detect(self):
        """this is main process in this class"""
        img_tensor = self.preprocess_image()
        outputs = self.ort_session.run(None, {"images": img_tensor})

        # choose mobs coordination in image
        detections = outputs[0]

        bboxes = [list(det[:4]) for det in detections[0] if det[4] > self.confidence]
        classes = [
            np.argmax(det[5:]) for det in detections[0] if det[4] > self.confidence
        ]

        # save results
        if self.is_save_result is True:
            self.draw_result(bboxes)
        self.write_result_to_text(bboxes, classes)

    def main(self):
        # while True:
        self.detect()

        if self.is_save_result:
            self.show_result_img()


if __name__ == "__main__":
    detect = DetectMobs(
        img_path=os.path.join(base_dir, "yoloFiles/input.png"),
        capture_path="yoloFiles/capture.png",
        txt_path="yoloFiles/labels/capture.txt",
        input_img_size=640,
        is_save_result=False,
        vertical_split_num=6,
        horizontal_split_num=1,
        confidence=0.6,
    )
    start_time = time.perf_counter()
    detect.main()
    end_time = time.perf_counter()

    print(f"Execution time: {end_time - start_time} seconds")
