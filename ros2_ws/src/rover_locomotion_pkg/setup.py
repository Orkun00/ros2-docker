from setuptools import find_packages, setup

package_name = 'rover_locomotion_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='orkun.acar@ozu.edu.tr',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # This line allows: ros2 run rover_locomotion_pkg rover_movement_calculation_node
            'rover_movement_calculation_node = rover_locomotion_pkg.rover_movement_calculation_node:main',
        ],
    },
)
