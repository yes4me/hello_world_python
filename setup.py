from setuptools import setup

"""
| Command          | Information                                     |
|------------------|-------------------------------------------------|
| name             | hello-world                                     |
| version          | 1.0                                             |
| py_modules       | ['hello_world']                                 |
| install_requires | []                                              |
| entry_points     | hello_world.exe is created in the /venv/Scripts |
"""

setup(
    name='hello-world',
    version='1.0',
    py_modules=['hello_module'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'say_hello = hello_module: say_hello'  # Function reference
        ]
    },
)
