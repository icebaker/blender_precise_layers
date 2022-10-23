import sys
import importlib


bl_info = {
    "name": "3D Printer Precise Layers",
    "author": "icebaker",
    "version": (0, 0, 3),
    "blender": (2, 80, 0),
    "location": "View3D > Toolbox",
    "description": "Calculate Precise Layers for 3D Printing",
    "warning": "",
    "doc_url": "",
    "category": "Mesh",
}


if "pytest" not in sys.modules:
    if __name__.startswith("blender_precise_layers"):
        from . import boot

        importlib.reload(boot)

        register = boot.register
        unregister = boot.unregister
    else:
        import os

        init_dir = os.path.dirname(init_path)  # pylint: disable=E0602
        if init_dir not in sys.path:
            sys.path.append(init_dir)

        import boot  # pylint: disable=E0401

        importlib.reload(boot)

        boot.boot()
