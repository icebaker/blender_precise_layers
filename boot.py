import importlib
import bpy  # pylint: disable=E0401
from bpy.app.handlers import persistent  # pylint: disable=E0401


if __name__.startswith('blender_precise_layers'):
    from . import operators
    from . import controllers
    from . import models
    from . import views
else:
    import operators  # pylint: disable=E0401
    import controllers  # pylint: disable=E0401
    import models  # pylint: disable=E0401
    import views  # pylint: disable=E0401


def model_updated(model, context, attribute, axis=None):
    bpy.context.scene.controller.model_updated(model, context, attribute, axis)


@persistent
def depsgraph_updated(scene):
    scene.controller.update_blender_object(
        bpy.context.view_layer.objects.active
    )


def register():
    importlib.reload(operators)
    importlib.reload(controllers)
    importlib.reload(models)
    importlib.reload(views)

    for operator in operators.registrable:
        bpy.utils.register_class(operator)

    bpy.utils.register_class(models.Model)
    bpy.types.Scene.model = bpy.props.PointerProperty(type=models.Model)

    bpy.types.Scene.controller = controllers.Controller()

    for view in views.registrable:
        bpy.utils.register_class(view)

    bpy.app.handlers.depsgraph_update_post.append(depsgraph_updated)


def unregister():
    for handler in bpy.app.handlers.depsgraph_update_post:
        bpy.app.handlers.depsgraph_update_post.remove(handler)

    del bpy.types.Scene.controller

    bpy.utils.unregister_class(models.Model)

    for view in views.registrable:
        bpy.utils.unregister_class(view)

    for operator in operators.registrable:
        bpy.utils.unregister_class(operator)


def boot():
    if hasattr(bpy.types.Scene, 'controller'):
        unregister()
    register()
