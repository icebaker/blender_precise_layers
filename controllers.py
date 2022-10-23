import importlib
import math
import dataclasses
import bpy  # pylint: disable=E0401

if __name__.startswith("blender_precise_layers"):
    from . import logic
else:
    import logic  # pylint: disable=E0401

    importlib.reload(logic)


@dataclasses.dataclass
class State:
    vertical_axis: str
    mm: logic.Xyz
    cm: logic.Xyz
    layers: logic.Xyz


class Controller:
    CLOSE_PRECISION = 0.00000001

    def __init__(self):
        self.blender_object_id = None
        self.blender_object = None

        self.state = State(
            vertical_axis=None,
            mm=logic.Xyz(x=None, y=None, z=None),
            cm=logic.Xyz(x=None, y=None, z=None),
            layers=logic.Xyz(x=None, y=None, z=None),
        )

        self.locked = False

    def model_updated(self, _model, _context, attribute, _axis=None):
        if self.locked or self.blender_object is None:
            return

        x_multiplier = bpy.context.scene.model.nozzle_diameter
        y_multiplier = bpy.context.scene.model.nozzle_diameter
        z_multiplier = bpy.context.scene.model.nozzle_diameter

        match bpy.context.scene.model.vertical_axis:
            case "X":
                x_multiplier = bpy.context.scene.model.layer_height
            case "Y":
                y_multiplier = bpy.context.scene.model.layer_height
            case "Z":
                z_multiplier = bpy.context.scene.model.layer_height

        match attribute:
            case "layers_x":
                self.blender_object.dimensions.x = (
                    bpy.context.scene.model.layers_x * x_multiplier)
            case "layers_y":
                self.blender_object.dimensions.y = (
                    bpy.context.scene.model.layers_y * y_multiplier)
            case "layers_z":
                self.blender_object.dimensions.z = (
                    bpy.context.scene.model.layers_z * z_multiplier)
            case "mm_x":
                self.blender_object.dimensions.x = bpy.context.scene.model.mm_x
            case "mm_y":
                self.blender_object.dimensions.y = bpy.context.scene.model.mm_y
            case "mm_z":
                self.blender_object.dimensions.z = bpy.context.scene.model.mm_z
            case "cm_x":
                self.blender_object.dimensions.x = (
                    bpy.context.scene.model.cm_x * 10.0
                )
            case "cm_y":
                self.blender_object.dimensions.y = (
                    bpy.context.scene.model.cm_y * 10.0
                )
            case "cm_z":
                self.blender_object.dimensions.z = (
                    bpy.context.scene.model.cm_z * 10.0
                )
            case "vertical_axis":
                if (
                    bpy.context.scene.model.vertical_axis is not None
                    and bpy.context.scene.model.vertical_axis != "Z"
                ):
                    self.blender_object["vertical_axis"] = (
                        bpy.context.scene.model.vertical_axis)
                else:
                    del self.blender_object["vertical_axis"]

    def update_model(self):
        self.locked = True

        if not math.isclose(
            bpy.context.scene.model.mm_x, self.state.mm.x,
            abs_tol=self.CLOSE_PRECISION
        ):
            bpy.context.scene.model.mm_x = self.state.mm.x

        if not math.isclose(
            bpy.context.scene.model.mm_y, self.state.mm.y,
            abs_tol=self.CLOSE_PRECISION
        ):
            bpy.context.scene.model.mm_y = self.state.mm.y

        if not math.isclose(
            bpy.context.scene.model.mm_z, self.state.mm.z,
            abs_tol=self.CLOSE_PRECISION
        ):
            bpy.context.scene.model.mm_z = self.state.mm.z

        if not math.isclose(
            bpy.context.scene.model.cm_x, self.state.cm.x,
            abs_tol=self.CLOSE_PRECISION
        ):
            bpy.context.scene.model.cm_x = self.state.cm.x

        if not math.isclose(
            bpy.context.scene.model.cm_y, self.state.cm.y,
            abs_tol=self.CLOSE_PRECISION
        ):
            bpy.context.scene.model.cm_y = self.state.cm.y

        if not math.isclose(
            bpy.context.scene.model.cm_z, self.state.cm.z,
            abs_tol=self.CLOSE_PRECISION
        ):
            bpy.context.scene.model.cm_z = self.state.cm.z

        if not math.isclose(
            bpy.context.scene.model.layers_x, self.state.layers.x,
            abs_tol=self.CLOSE_PRECISION
        ):
            bpy.context.scene.model.layers_x = self.state.layers.x

        if not math.isclose(
            bpy.context.scene.model.layers_y, self.state.layers.y,
            abs_tol=self.CLOSE_PRECISION
        ):
            bpy.context.scene.model.layers_y = self.state.layers.y

        if not math.isclose(
            bpy.context.scene.model.layers_z, self.state.layers.z,
            abs_tol=self.CLOSE_PRECISION
        ):
            bpy.context.scene.model.layers_z = self.state.layers.z

        if (
            not self.state.vertical_axis
            == bpy.context.scene.model.vertical_axis
        ):
            bpy.context.scene.model.vertical_axis = self.state.vertical_axis

        self.locked = False

    def calculate_from_blender_object(self):
        self.state.mm.x = self.blender_object.dimensions.x
        self.state.mm.y = self.blender_object.dimensions.y
        self.state.mm.z = self.blender_object.dimensions.z

        self.state.cm.x = self.state.mm.x / 10.0
        self.state.cm.y = self.state.mm.y / 10.0
        self.state.cm.z = self.state.mm.z / 10.0

        if "vertical_axis" in self.blender_object:
            self.state.vertical_axis = self.blender_object["vertical_axis"]
        else:
            self.state.vertical_axis = "Z"

        x_divider = bpy.context.scene.model.nozzle_diameter
        y_divider = bpy.context.scene.model.nozzle_diameter
        z_divider = bpy.context.scene.model.nozzle_diameter

        match self.state.vertical_axis:
            case "X":
                x_divider = bpy.context.scene.model.layer_height
            case "Y":
                y_divider = bpy.context.scene.model.layer_height
            case "Z":
                z_divider = bpy.context.scene.model.layer_height

        self.state.layers.x = self.state.mm.x / x_divider
        self.state.layers.y = self.state.mm.y / y_divider
        self.state.layers.z = self.state.mm.z / z_divider

        self.update_model()

    def update_blender_object(self, blender_object):
        if blender_object is None:
            self.blender_object = None
            self.blender_object_id = None
            return

        self.blender_object = blender_object
        self.blender_object_id = blender_object.id_data.name

        self.calculate_from_blender_object()
