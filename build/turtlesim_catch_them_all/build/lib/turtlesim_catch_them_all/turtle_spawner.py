#!/usr/bin/env python3
from functools import partial
import math
import random
import rclpy
from rclpy.node import Node

from turtlesim.srv import Spawn

class TurtleSpawnerNode(Node):
    def __init__(self):
        super().__init__("turtle_spawner")
        self.turtle_name_prefix_ = "turtle"
        self.turtle_counter_ = 0
        self.spawn_turtle_timer_ = self.create_timer(2.0, self.spawn_new_turtle)

    def spawn_new_turtle(self):
        self.turtle_counter_ += 1
        name = self.turtle_name_prefix_ + str(self.turtle_counter_)
        x = random.uniform(0.0, 11.0)
        y = random.uniform(0.0, 11.0)
        theta = random.uniform(0.0, 2*math.pi)
        self.call_spawn_server(name, x, y, theta)

        # creating a function
    
    def call_spawn_server(self, turtle_name, x, y, theta):
        # creating the client
        client = self.create_client(Spawn, "spawn")
        # while the cclient is waiting print warrining message
        while not client.wait_for_service(1.0):
            self.get_logger().warn("waiting for server to call spawn")
        # creating the request
        request = Spawn.Request()
        request.x = x
        request.y = y
        request.theta = theta
        request.name = turtle_name

        # creating the future
        future = client.call_async(request)
        # calling the add done callback function, and with the help of partial we call the function and give two other arguments
        future.add_done_callback(
            partial(self.callback_call_spawn, turtle_name=turtle_name, x=x, y=y, theta = theta))
    #creating the callback function which will give us the response
    def callback_call_spawn(self, future, turtle_name, x, y, theta):
        try:
            response = future.result()
            if response.name != "":
                self.get_logger().info("Turtle " + response.name + " is now alive")
        # if we have an exception we print out an error message
        except Exception as e:
            self.get_logger().error("Service call failed %r" % (e,))


def main(args=None):
    rclpy.init(args=args)
    node = TurtleSpawnerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()