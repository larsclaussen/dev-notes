

## ipython


```shell
ipython profile create <profile name>
```

Usually gets created as `~/.ipython/profile_<profile name>/ipython_config.py`

### Enabling rich

Add the following to `~/.ipython/profile_rich_profile/ipython_config.py`

```python
## lines of code to run at IPython startup.
c.InteractiveShellApp.exec_lines = [
        'from rich import pretty, inspect',
        'from rich import traceback',
        'pretty.install()',
        '_ = traceback.install()',
]
```

### Starting with a specific profile

Make ipython an fish alias

```shell
ipython is a function with definition
# Defined in ~/.config/fish/functions/ipython.fish @ line 1
function ipython
    command ipython --profile=rich_profile $argv;
end
```


## Resources

### subclassing

Blog post by [Hynek Schlawack](https://hynek.me/articles/python-subclassing-redux/).

### type hints


Blog post by [Adam Johnson](https://adamj.eu/tech/2021/05/29/python-type-hints-how-to-use-overload/)  on how to use the **overload decorator**.