import importlib
import bpy  # pylint: disable=E0401

if __name__.startswith("blender_precise_layers"):
    from . import operators
else:
    import operators  # pylint: disable=E0401

    importlib.reload(operators)


class View(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Precise Layers"
    bl_idname = "OBJECT_PT_printer_layers"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Precise Layers"

    @classmethod
    def poll(cls, context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.label(text="3D Printer Settings:")

        row = layout.row()
        row.prop(
            context.scene.model, "print_precision", text="Print Precision"
        )

        row = layout.row()
        row.prop(
            context.scene.model, "nozzle_diameter", text="Nozzle Diameter"
        )

        row = layout.row()
        row.prop(context.scene.model, "layer_height", text="Layer Height")

        row = layout.separator()
        row = layout.row()
        row.operator(operators.FakeOperator.bl_idname, text=obj.name)

        row = layout.row()
        row.label(text="Vertical Axis:")
        row.prop(context.scene.model, "vertical_axis")

        row = layout.separator()
        row = layout.row()
        row.label(text="Millimeters:")

        row = layout.row()
        row.prop(context.scene.model, "mm_x", text="X")

        row = layout.row()
        row.prop(context.scene.model, "mm_y", text="Y")

        row = layout.row()
        row.prop(context.scene.model, "mm_z", text="Z")

        row = layout.separator()
        row = layout.row()
        row.label(text="Centimeters:")

        row = layout.row()
        row.prop(context.scene.model, "cm_x", text="X")

        row = layout.row()
        row.prop(context.scene.model, "cm_y", text="Y")

        row = layout.row()
        row.prop(context.scene.model, "cm_z", text="Z")

        row = layout.separator()
        row = layout.row()
        row.label(text="Layers:")

        row = layout.row()
        row.prop(context.scene.model, "layers_x", text="X")

        row = layout.row()
        row.prop(context.scene.model, "layers_y", text="Y")

        row = layout.row()
        row.prop(context.scene.model, "layers_z", text="Z")

        row = layout.separator()
        row = layout.row()
        row.operator(operators.CubifyOperator.bl_idname, text="Cubify")
