import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    gazebo = IncludeLaunchDescription(
            os.path.join(
                get_package_share_directory("pantilt_description"),
                "launch",
                "gazebo.launch.py"
            )
        )
    
    controller = IncludeLaunchDescription(
            os.path.join(
                get_package_share_directory("pantilt_controller"),
                "launch",
                "slider_controller.launch.py"
            ),
            launch_arguments={"is_sim": "True"}.items()
        )
    
    # moveit = IncludeLaunchDescription(
    #         os.path.join(
    #             get_package_share_directory("pantilt_moveit"),
    #             "launch",
    #             "moveit.launch.py"
    #         ),
    #         launch_arguments={"is_sim": "True"}.items()
    #     )
    
  
    return LaunchDescription([
        gazebo,
        controller,
        #moveit,
    ])