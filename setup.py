from setuptools import find_packages
from setuptools import setup

package_name = 'ros2acceleration'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/' + package_name, ['package.xml']),
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
    ],
    install_requires=['ros2cli'],
    zip_safe=True,
    author='Víctor Mayoral Vilches',
    author_email='victorma@xilinx.com',
    maintainer='Víctor Mayoral Vilches',
    maintainer_email='victorma@xilinx.com',
    url='https://github.com/ros-acceleration/ros2acceleration',
    download_url='https://github.com/ros-acceleration/ros2acceleration/releases',
    keywords=[],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
    ],
    description='The acceleration command for ROS 2 command line tools.',
    long_description="""\
The package provides the accceleration command for the ROS 2 command line tools.""",
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'ros2cli.command': [
            'acceleration = ros2acceleration.command.acceleration:AccelerationCommand',
        ],
        'ros2cli.extension_point': [
            'ros2acceleration.verb = ros2acceleration.verb:VerbExtension',
        ],
        'ros2acceleration.verb': [
            'bw = ros2acceleration.verb.bw:BwVerb',
            'delay = ros2acceleration.verb.delay:DelayVerb',
            'echo = ros2acceleration.verb.echo:EchoVerb',
            'find = ros2acceleration.verb.find:FindVerb',
            'hz = ros2acceleration.verb.hz:HzVerb',
            'info = ros2acceleration.verb.info:InfoVerb',
            'list = ros2acceleration.verb.list:ListVerb',
            'pub = ros2acceleration.verb.pub:PubVerb',
            'type = ros2acceleration.verb.type:TypeVerb',
        ],
    }
)
