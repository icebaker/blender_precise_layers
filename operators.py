import importlib

import bpy  # pylint: disable=E0401

if __name__.startswith('blender_precise_layers'):
    from . import logic
else:
    import logic  # pylint: disable=E0401

    importlib.reload(logic)


class CubifyOperator(bpy.types.Operator):
    '''Resize the object to a cube composed of precise layers.'''
    bl_idname = 'object.cubify_operator'
    bl_label = 'Cubify Operator'

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        mm = logic.Logic.cubify(
            context.active_object.dimensions,
            logic.PrinterSettings(
                nozzle_diameter=context.scene.model.nozzle_diameter,
                layer_height=context.scene.model.layer_height))

        context.active_object.dimensions = (mm, mm, mm)

        return {'FINISHED'}


class FakeOperator(bpy.types.Operator):
    '''Active current object'''
    bl_idname = 'object.fake_operator'
    bl_label = 'Fake Object Operator'

    @classmethod
    def poll(cls, _context):
        return False

    def execute(self, _context):
        return {'FINISHED'}


registrable = (
    CubifyOperator,
    FakeOperator)
