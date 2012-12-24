from setuptools import setup, find_packages


setup(
    name='ioschedd',
    version='0.1.1',
    description='Daemon to control per-device IO Scheduler \
            options in the Linux kernel',
    author='Jeremy Hanmer',
    author_email='jeremy@dreamhost.com',
    url='http://github.com/fzylogic/ioschedd',
    license='Apache2',
    install_requires=[
        'pyudev>=0.16'
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'ioschedd=ioschedd.service:main'
        ]
    },
)
