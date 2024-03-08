# Create python package (Created on 2024-03-08)

## Make a built distribution package to [github](https://github.com/)

1. Create a repo at https://github.com/yes4me/hello_world_python
2. run the following command

```commandline
cd my_package
pip install wheel
python setup.py bdist_wheel
copy ./dist/*.whl .
git init
git add *.whl
git commit -m "first commit"
git remote add origin https://github.com/yes4me/hello_world_python.git
git push
```

## Install package

1. Create run_hello_world.py

    ```commandline
    from hello_module import say_hello
    
    say_hello()
    ```

2. Create requirements.txt, with either:
 
   `git+https://github.com/yes4me/hello_world_python.git`

   `git+https://github.com/yes4me/hello_world_python.git@[branch_name]`

3. Either:
    * cmd: `pip install .\hello_world-1.0-py3-none-any.whl`
    * cmd: `pip install pip install https://github.com/yes4me/hello_world_python/raw/main/dist/hello_world-1.0-py3-none-any.whl`
4. cmd: `python run_hello_world.py`

## Uninstall package

* cmd: `pip uninstall -y hello-world`

## References

* [Uploading the package to a testing location](https://test.pypi.org/)

PS: You cannot do `pip uninstall -r requirements.txt -y`. This is because pip installs packages from Git repositories in
editable mode (-e), and there isn't a straightforward way to uninstall packages installed in editable mode.
