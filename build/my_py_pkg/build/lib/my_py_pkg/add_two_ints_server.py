#!/usr/bin/env python3
from ast import Add
import rclpy
from rclpy.node import Node

from example_interfaces.srv import AddTwoInts


class AddTwoIntsServerNode(Node):
    def __init__(self):
        super().__init__("add_two_ints_server")
        # create service first value is the type of service, the second is the name of the service and the callback function
        self.server_ = self.create_service(
            AddTwoInts, "add_two_ints", self.callback_add_two_int)
        self.get_logger().info("wellcone to the server")

    def callback_add_two_int(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info(str(request.a) + " + " +
                               str(request.b) + " = " + str(response.sum))
        return response


def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntsServerNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
