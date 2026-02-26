from launch import LaunchDescription
from launch_ros.actions import Node,SetParameter

from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration

from launch_ros.substitutions import FindPackageShare
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

	# _declare = DeclareLaunchArgument() # make new lunch file argument
	# _start = Node() # start up new node

	bringup_dir = FindPackageShare(package='nav2_bringup').find('nav2_bringup')

	config_dir = os.path.join(FindPackageShare(package='orion_vi_bringup').find('orion_vi_bringup_pkg'),'config')
	config_file = os.path.join(config_dir, 'bringup.config.yaml')

	

	nav2_bringup_launch = IncludeLaunchDescription(
	PythonLaunchDescriptionSource(

		os.path.join(bringup_dir,'launch','bringup_launch.py')),

		launch_arguments={
			'params_file': config_file
		}.items()
	)

	ld = LaunchDescription()
	ld.add_action(nav2_bringup_launch)

	return ld