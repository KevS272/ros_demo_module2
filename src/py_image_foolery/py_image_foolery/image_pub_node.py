import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from sensor_msgs.msg import Image
import cv2
import numpy as np

class ImagePublisher(Node):

    def __init__(self):
        super().__init__('image_publisher')
        self.subscription = self.create_subscription(
            String, 'demo_topic', self.callback, 10)
        self.publisher_ = self.create_publisher(Image, 'image_topic', 10)
        self.i = 0

    def callback(self, msg):
        print("executing callback")
        number = int(msg.data.split()[-1])
        image = self.generate_image(number)
        self.publish_image(image)

    def generate_image(self, number):
        if number % 5 == 0:
            color = (0, 255, 0)  # Green
        elif number % 2 == 0:
            color = (255, 0, 0)  # Red
        else:
            color = (0, 0, 255)  # Blue

        image = np.zeros((400, 400, 3), dtype=np.uint8)
        image[:] = color
        return image

    def publish_image(self, image):
        img_msg = Image()
        img_msg.height = image.shape[0]
        img_msg.width = image.shape[1]
        img_msg.encoding = "bgr8"
        img_msg.step = 3 * image.shape[1]
        img_msg.data = image.tobytes()
        self.publisher_.publish(img_msg)

def main(args=None):
    print("Starting image publisher node")
    rclpy.init(args=args)
    image_publisher = ImagePublisher()
    rclpy.spin(image_publisher)
    image_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
