#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):

    def __init__(self):
        super().__init__("py_test_")
        self.counter_ = 0
        self.get_logger().info("Hello from the Class ROS2")
        self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        self.counter_ += 1
        self.get_logger().info("Hello " + str(self.counter_))


def main(args=None):
    #fist most important part
    rclpy.init(args=args)
    #creating a node
    node = MyNode() 
    #basicly infinite while loop   
    rclpy.spin(node)
    #shut down the program
    rclpy.shutdown()

if __name__ == "__main__":
    main()