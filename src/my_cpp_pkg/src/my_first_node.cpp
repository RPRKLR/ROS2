#include "rclcpp/rclcpp.hpp"

//creating the MyNode class
class MyNode : public rclcpp::Node
{
public:
//creating the constructor, whrere we create the node, and then initialize the counter
    MyNode() : rclcpp::Node("cpp_test"), counter_(0)
    {
        // logger write into the terminal
        RCLCPP_INFO(this->get_logger(), "Hello cpp node");
        //creating the wall timer, the duration is one second the we bind the referened timer callback function, to the itself
        timer_ = this->create_wall_timer(std::chrono::seconds(1), std::bind(&MyNode::timer_callback, this));
    }

private:
//creating the timer, with shared pointer
    rclcpp::TimerBase::SharedPtr timer_;
    //add one to the counter and then push it to the log
    void timer_callback()
    {
        counter_++;
        RCLCPP_INFO(this->get_logger(), "Hello %d", counter_);
    }
    int counter_;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    // make a shared MyNode pointer
    auto node = std::make_shared<MyNode>();

    // spinnign the node
    rclcpp::spin(node);

    rclcpp::shutdown();
    return 0;
}