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
    """Detect Mobs(Zombie, Skeleton) location with image recognition"""

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

        # Load ONNX model
        self.ort_session = ort.InferenceSession(model_path)

    def capture_img(self):
        window_title = "Minecraft Education"
        window = gw.getWindowsWithTitle(window_title)[0]
        window_location = (window.left, window.top, window.width, window.height)
        window_image = pyautogui.screenshot(region=window_location)
        window_image = cv2.cvtColor(np.array(window_image), cv2.COLOR_BGR2RGB)

        return window_image

    def preprocess_image(self):
        """To load and preprocess images"""
        if self.img_path is None:
            img = self.capture_img()
        else:
            img = cv2.imread(self.img_path)

        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # If we need to save the result of the image
        if self.is_save_result is True:
            cv2.imwrite(self.capture_path, img)
        img_resized = cv2.resize(img_rgb, (self.input_img_size, self.input_img_size))
        img_normalized = img_resized / 255.0  # Standardization to 0-1
        img_transposed = np.transpose(img_normalized, (2, 0, 1))  # HWC->CHW

        return np.expand_dims(img_transposed, axis=0).astype(np.float32)

    def draw_result(self, bboxes, classes):
        """
        Draw detection results (bounding boxes and center points) on the input image.

        Args:
            bboxes (list): List of bounding box coordinates
            classes (list): List of classes corresponding to each detection
        """
        img = cv2.imread(self.capture_path)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h, w, _ = img_rgb.shape

        # Draw bounding boxes and center points on the image
        for bbox in bboxes:
            x_center, y_center, width, height = bbox
            # Scale back to the original image size
            x_center = x_center * w / self.input_img_size
            y_center = y_center * h / self.input_img_size
            width = width * w / self.input_img_size
            height = height * h / self.input_img_size

            x_min = int(x_center - width / 2.0)
            y_min = int(y_center - height / 2.0)
            x_max = int(x_center + width / 2.0)
            y_max = int(y_center + height / 2.0)

            # Draw a red bounding box
            cv2.rectangle(img_rgb, (x_min, y_min), (x_max, y_max), (255, 0, 0), 2)
            # Draw the center point
            cv2.circle(
                img_rgb,
                center=(int(x_center), int(y_center)),
                radius=5,
                color=(0, 0, 255),
                thickness=-1,
            )

        # Save the result image
        cv2.imwrite(self.capture_path, cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR))

    def show_result_img(self):
        img = cv2.imread(self.capture_path)
        cv2.imshow("result_img", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def write_result_to_text(self, bboxes, classes):
        """
        Write detection results (1 or 0) to a text file for each segment.

        Args:
            bboxes (list): List of detected bounding boxes
            classes (list): List of classes corresponding to each detection
        """
        results_diamondhead, results_diamondboot = self.calc_location(bboxes, classes)

        with open(self.txt_path, encoding="UTF-8", mode="w") as f:
            # Write results for diamondhead
            for result in results_diamondhead:
                f.write("1" if result == 1 else "0")
            f.write("\n")

            # Write results for diamondboot
            for result in results_diamondboot:
                f.write("1" if result == 1 else "0")
            f.write("\n")

    def calc_location(self, bboxes, classes):
        """
        Check if diamondhead or diamondboot is detected in each split region.

        Args:
            bboxes (list): List of detected bounding boxes
            classes (list): List of classes corresponding to each detection

        Returns:
            list, list: Lists of detection results for diamondhead and diamondboot in each region
        """
        segment_width = 640 // self.vertical_split_num
        segment_height = 640 // self.horizontal_split_num

        results_diamondhead = [0] * (self.vertical_split_num * self.horizontal_split_num)
        results_diamondboot = [0] * (self.vertical_split_num * self.horizontal_split_num)

        for bbox, cls in zip(bboxes, classes):
            x_center, y_center, _, _ = bbox

            # Calculate the region index based on the center coordinates
            segment_x = int(x_center // segment_width)
            segment_y = int(y_center // segment_height)
            segment_index = segment_y * self.vertical_split_num + segment_x

            # Mark as detected (1) in the corresponding region if diamondhead or diamondboot is found
            if cls == 0:  # diamondhead
                results_diamondhead[segment_index] = 1
            elif cls == 1:  # diamondboot
                results_diamondboot[segment_index] = 1

        return results_diamondhead, results_diamondboot

    def detect(self):
        """Main process to detect objects and write results to a text file."""
        img_tensor = self.preprocess_image()
        outputs = self.ort_session.run(None, {"images": img_tensor})

        # Extract bounding boxes and classes based on confidence threshold
        detections = outputs[0]
        bboxes = [det[:4] for det in detections[0] if det[4] > self.confidence]
        classes = [np.argmax(det[5:]) for det in detections[0] if det[4] > self.confidence]

        if self.is_save_result:
            # Draw the detection result on the image for debugging
            self.draw_result(bboxes, classes)

        # Write detection result to text file
        self.write_result_to_text(bboxes, classes)

    def main(self):
        while True:
            self.detect()
            time.sleep(0.1)  # Add a delay to control how often the screen is captured and detected

            # Show result image for debugging
            #if self.is_save_result:
                #self.show_result_img()


if __name__ == "__main__":
    with open(os.path.join(base_dir, "yoloFiles/detectMobs_config.txt"), "r") as file:
        v = int(file.readline())
        h = int(file.readline())
    detect = DetectMobs(
        capture_path="yoloFiles/capture.png",
        txt_path="yoloFiles/labels/capture.txt",
        input_img_size=640,
        is_save_result=False,
        vertical_split_num=v,
        horizontal_split_num=h,
        confidence=0.6,
    )

    detect.main()
