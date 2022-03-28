#!/usr/bin/env python3
from urllib import response
import rclpy
from rclpy.node import Node

from example_interfaces.srv import AddTwoInts


def main(args=None):
    rclpy.init(args=args)
    node = Node("add_two_ints_no_oop")
    # creating a client from the node.
    client = node.create_client(AddTwoInts, "add_two_ints")

    # while the client is waiting for the service we print out a warrning message
    while not client.wait_for_service(1.0):
        node.get_logger().warn("waiting for server add two ints")

    # creating a request from the AddTwoints
    request = AddTwoInts.Request()
    request.a = 3
    request.b = 4

    # creating the future
    future = client.call_async(request)

    # we spin the node while the future is not succesfull
    rclpy.spin_until_future_complete(node, future)

    # if there are no erros we get the response from the future's result
    # and log out the request and the response
    try:
        response = future.result()
        node.get_logger().info(str(request.a) + " + " +
                               str(request.b) + " = " + str(response.sum))
    # if we have an exception we print out an error message
    except Exception as e:
        node.get_logger().error("Service call failed %r" % (e,))
    rclpy.shutdown()


if __name__ == "__main__":
    main()
