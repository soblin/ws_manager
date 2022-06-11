from setuptools import setup

package_name = 'ws_manager'

setup(
    name=package_name,
    version='1.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Mamoru Sobue',
    maintainer_email='hilo.soblin@gmail.com',
    description='ROS2 workspace manager',
    license='MIT',
    entry_points={
        'console_scripts': [
            'ws_manager = ws_manager.ws_manager:main'
        ],
    },
)
