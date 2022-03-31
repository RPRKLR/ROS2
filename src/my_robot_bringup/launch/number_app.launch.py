import imp
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    launch_description = LaunchDescription()

    number_publisher_node = Node(
        package="my_py_pkg",
        executable="number_publisher",
        name="my_number_publisher",
        #remappings=[()],
        parameters=[{"number_to_publish": 4}]

    )

    launch_description.add_action(number_publisher_node)
    return launch_description
