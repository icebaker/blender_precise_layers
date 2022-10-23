# 3D Printer Precise Layers

A [Blender 3D](https://www.blender.org) Addon that helps you create accurate models for 3D Printing.

## Setup

Ensure that Blender is properly configured for 3D Printing units. You can follow the great [_Blender for 3D Printing_](https://daler.github.io/blender-for-3d-printing/interface/transforms.html#units) guide to achieve this.

## Development

```sh
pip install -r requirements-dev.txt

pycodestyle *.py

pylint *.py

pytest
```

Read Blender's [Tips and Tricks](https://docs.blender.org/api/current/info_tips_and_tricks.html) and [Gotchas](https://docs.blender.org/api/current/info_gotcha.html).

Developing inside Blender:

```python
init_path = "/home/icebaker/blender_precise_layers/__init__.py"

exec(
    compile(open(init_path).read(), init_path, 'exec'),
    {"init_path": init_path}
)
```

Rerun the script every time you change the code: It will reload all your updated code inside Blender.
