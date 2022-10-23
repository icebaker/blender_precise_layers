import importlib
import bpy  # pylint: disable=E0401

if __name__.startswith('blender_precise_layers'):
    from . import operators
else:
    import operators  # pylint: disable=E0401

    importlib.reload(operators)


ID_PREFIX = 'VIEW3D_PT_precise_layers_'
SPACE_TYPE = 'VIEW_3D'
REGION_TYPE = 'UI'
CATEGORY = 'Precise Layers'


class PrinterSettingsView(bpy.types.Panel):
    bl_label = '3D Printer Settings'
    bl_idname = ID_PREFIX + 'printer_settings'
    bl_space_type = SPACE_TYPE
    bl_region_type = REGION_TYPE
    bl_category = CATEGORY

    @classmethod
    def poll(cls, _context):
        return True

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.prop(
            context.scene.model, 'print_precision', text='Print Precision'
        )

        row = layout.row()
        row.prop(
            context.scene.model, 'nozzle_diameter', text='Nozzle Diameter'
        )

        row = layout.row()
        row.prop(context.scene.model, 'layer_height', text='Layer Height')


class ObjectSettingsView(bpy.types.Panel):
    bl_label = 'Object Settings'
    bl_idname = ID_PREFIX + 'object_settings'
    bl_space_type = SPACE_TYPE
    bl_region_type = REGION_TYPE
    bl_category = CATEGORY

    @classmethod
    def poll(cls, context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator(
            operators.FakeOperator.bl_idname, text=context.object.name)

        row = layout.row()
        row.label(text='Vertical Axis:')
        row.prop(context.scene.model, 'vertical_axis')


class OperationsView(bpy.types.Panel):
    bl_label = 'Operations'
    bl_idname = ID_PREFIX + 'operations'
    bl_space_type = SPACE_TYPE
    bl_region_type = REGION_TYPE
    bl_category = CATEGORY

    @classmethod
    def poll(cls, context):
        return context.object is not None

    def draw(self, _context):
        layout = self.layout

        row = layout.row()
        row.operator(operators.CubifyOperator.bl_idname, text='Cubify')


class LayersView(bpy.types.Panel):
    bl_label = 'Layers'
    bl_idname = ID_PREFIX + 'layers'
    bl_space_type = SPACE_TYPE
    bl_region_type = REGION_TYPE
    bl_category = CATEGORY

    @classmethod
    def poll(cls, context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.prop(context.scene.model, 'layers_x', text='X')

        row = layout.row()
        row.prop(context.scene.model, 'layers_y', text='Y')

        row = layout.row()
        row.prop(context.scene.model, 'layers_z', text='Z')


class MillimetersView(bpy.types.Panel):
    bl_label = 'Millimeters'
    bl_idname = ID_PREFIX + 'millimeters'
    bl_space_type = SPACE_TYPE
    bl_region_type = REGION_TYPE
    bl_category = CATEGORY

    @classmethod
    def poll(cls, context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.prop(context.scene.model, 'mm_x', text='X')

        row = layout.row()
        row.prop(context.scene.model, 'mm_y', text='Y')

        row = layout.row()
        row.prop(context.scene.model, 'mm_z', text='Z')


class CentimetersView(bpy.types.Panel):
    bl_label = 'Centimeters'
    bl_idname = ID_PREFIX + 'centimeters'
    bl_space_type = SPACE_TYPE
    bl_region_type = REGION_TYPE
    bl_category = CATEGORY

    @classmethod
    def poll(cls, context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.prop(context.scene.model, 'cm_x', text='X')

        row = layout.row()
        row.prop(context.scene.model, 'cm_y', text='Y')

        row = layout.row()
        row.prop(context.scene.model, 'cm_z', text='Z')


class XView(bpy.types.Panel):
    bl_label = 'X'
    bl_idname = ID_PREFIX + 'x'
    bl_space_type = SPACE_TYPE
    bl_region_type = REGION_TYPE
    bl_category = CATEGORY
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.prop(context.scene.model, 'layers_x', text='Layers')

        row = layout.row()
        row.prop(context.scene.model, 'mm_x', text='Millimeters')

        row = layout.row()
        row.prop(context.scene.model, 'cm_x', text='Centimeters')


class YView(bpy.types.Panel):
    bl_label = 'Y'
    bl_idname = ID_PREFIX + 'y'
    bl_space_type = SPACE_TYPE
    bl_region_type = REGION_TYPE
    bl_category = CATEGORY
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.prop(context.scene.model, 'layers_y', text='Layers')

        row = layout.row()
        row.prop(context.scene.model, 'mm_y', text='Millimeters')

        row = layout.row()
        row.prop(context.scene.model, 'cm_y', text='Centimeters')


class ZView(bpy.types.Panel):
    bl_label = 'Z'
    bl_idname = ID_PREFIX + 'z'
    bl_space_type = SPACE_TYPE
    bl_region_type = REGION_TYPE
    bl_category = CATEGORY
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.prop(context.scene.model, 'layers_z', text='Layers')

        row = layout.row()
        row.prop(context.scene.model, 'mm_z', text='Millimeters')

        row = layout.row()
        row.prop(context.scene.model, 'cm_z', text='Centimeters')


registrable = (
    PrinterSettingsView,
    ObjectSettingsView,
    OperationsView,
    LayersView, MillimetersView, CentimetersView,
    XView, YView, ZView)
