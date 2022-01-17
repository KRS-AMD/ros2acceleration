^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package ros2acceleration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.3.0 (2022-01-17)
------------------------
* Port ros2acceleration logic to Vitis 2021.2
* Support libdfx and dfx-mgr of the 2021.2 release

0.2.0 (2021-08-20)
------------------------
* Initial implementation of ros2 acceleration tools considering 
  Vitis 2020.2.2 and its corresponding dfx-mgr for reconfiguring the FPGA
* An accceleration daemon was created which takes care of exposing ROS 2
  package accelerators to the underlying infrastructure.
* Implemented various verbs for selecting, removing, listing and restart
  the acceleration daemon. The 


0.1.0 (2021-08-14)
------------------------
* Initial commit, repurpose ros2cli as a template to create the tools
* Added placeholder for list verb so that simple tests can be performed.