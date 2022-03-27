#!/usr/bin/env python3
from threading import Timer
import rclpy
from rclpy.node import Node
#example interface for the string value
from example_interfaces.msg import String

class RobotNewsStationNode(Node):

    def __init__(self):
        #creating the node with the name 
        super().__init__("robot_news_station")

        self.robot_name = "C3PO"

        #creating a publisher whoch will send string vale, the name of the publisher and then the queue size
        self.publishers_ = self.create_publisher(String, "robot_news", 10)

        # creating timer which will run the function in every 0.5 seconds and then log to the terminal
        self.timer_ = self.create_timer(0.5, self.publish_news)
        self.get_logger().info("Robot station has been started")

    #creating the publish funciton 
    def publish_news(self):
        msg = String()
        msg.data = "Hi this is " + str(self.robot_name) + " From the robot news station"
        self.publishers_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = RobotNewsStationNode()   
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()