#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2


class CameraPublisherNode(Node):
    def __init__(self):
        super().__init__('camera_publisher')
        self.publisher_ = self.create_publisher(Image, 'camera_image', 10)
        self.timer_ = self.create_timer(1.0 / 30.0, self.publish_frame)
        self.bridge_ = CvBridge()
        self.cap_ = cv2.VideoCapture(0)  # Use 0 for the default camera

    def publish_frame(self):
        ret, frame = self.cap_.read()
        if ret:
            msg = self.bridge_.cv2_to_imgmsg(frame, encoding='bgr8')
            self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = CameraPublisherNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
