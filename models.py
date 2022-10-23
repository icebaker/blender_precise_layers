import dataclasses
import bpy  # pylint: disable=E0401


def model_updated(model, context, attribute, axis=None):
    bpy.context.scene.controller.model_updated(model, context, attribute, axis)


@dataclasses.dataclass
class Model(bpy.types.PropertyGroup):  # pylint: disable=R0902
    print_precision: bpy.props.FloatProperty(
        default=0.1,
        precision=2, step=1,
        update=lambda self, context: model_updated(
            self, context, 'print_precision'))

    nozzle_diameter: bpy.props.FloatProperty(
        default=0.4,
        precision=2, step=1,
        update=lambda self, context: model_updated(
            self, context, 'nozzle_diameter'))

    layer_height: bpy.props.FloatProperty(
        default=0.20,
        precision=2, step=1,
        update=lambda self, context: model_updated(
            self, context, 'layer_height'))

    vertical_axis: bpy.props.EnumProperty(
        name='',
        description='Vertical Axis',
        items=[('X', 'X', 'X'), ('Y', 'Y', 'Y'), ('Z', 'Z', 'Z')],
        update=lambda self, context: model_updated(
            self, context, 'vertical_axis'))

    layers_x: bpy.props.FloatProperty(
        default=0.20,
        precision=2, step=1,
        update=lambda self, context: model_updated(
            self, context, 'layers_x', 'x'))

    layers_y: bpy.props.FloatProperty(
        default=0.20,
        precision=2, step=1,
        update=lambda self, context: model_updated(
            self, context, 'layers_y', 'y'))

    layers_z: bpy.props.FloatProperty(
        default=0.20,
        precision=2, step=1,
        update=lambda self, context: model_updated(
            self, context, 'layers_z', 'z'))

    mm_x: bpy.props.FloatProperty(
        precision=2, step=1,
        update=lambda self, context: model_updated(self, context, 'mm_x', 'x'))

    mm_y: bpy.props.FloatProperty(
        precision=2, step=1,
        update=lambda self, context: model_updated(self, context, 'mm_y', 'y'))

    mm_z: bpy.props.FloatProperty(
        precision=2, step=1,
        update=lambda self, context: model_updated(self, context, 'mm_z', 'z'))

    cm_x: bpy.props.FloatProperty(
        precision=4, step=1,
        update=lambda self, context: model_updated(self, context, 'cm_x', 'x'))

    cm_y: bpy.props.FloatProperty(
        precision=4, step=1,
        update=lambda self, context: model_updated(self, context, 'cm_y', 'y'))

    cm_z: bpy.props.FloatProperty(
        precision=4, step=1,
        update=lambda self, context: model_updated(self, context, 'cm_z'))
