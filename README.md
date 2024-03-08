# Create python package (Created on 2024-03-08)

## Create the package using setuptools to github

1. Create a repo at https://github.com/yes4me/hello_world_python
2. run the following command

```commandline
cd my_package
git init
git add .
git commit -m "first commit"
git remote add origin https://github.com/yes4me/hello_world_python.git
git push
```

PS: when installing packages from GitHub using pip, pip automatically treats github.com as a trusted host.

## Install package

1. create run_hello_world.py

    ```commandline
    from hello_module import say_hello
    
    say_hello()
    ```

2. Either:
    * cmd: `pip install git+https://github.com/yes4me/hello_world_python.git`
    * cmd: `pip install -r requirements.txt`
3. cmd: `python run_hello_world.py`

## Uninstall package

* cmd: `pip uninstall -y hello-world`
