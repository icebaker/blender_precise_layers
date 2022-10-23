import dataclasses


@dataclasses.dataclass
class PrinterSettings:
    nozzle_diameter: float
    layer_height: float
    print_precision: float = 0.1


@dataclasses.dataclass
class Xyz:
    x: float
    y: float
    z: float


@dataclasses.dataclass
class Layers:
    horizontal: int
    vertical: int
    delta: float = None


class Logic:
    @staticmethod
    def cubify(blender_object, printer):
        layers = Logic.layers_for(printer)
        expected = max([blender_object.x, blender_object.y, blender_object.z])

        multiplier = round(
            expected / (layers.horizontal * printer.nozzle_diameter), 0
        )

        return multiplier * layers.horizontal * printer.nozzle_diameter

    @staticmethod
    def mm_to_layers(mm, printer):
        layers = Layers(
            horizontal=round(mm / printer.nozzle_diameter, 0),
            vertical=round(mm / printer.layer_height, 0))

        layers.delta = abs(
            (layers.horizontal * printer.nozzle_diameter)
            - (layers.vertical * printer.layer_height)
        )

        return layers

    @staticmethod
    def layers_for(printer):
        candidates = []

        for horizontal in range(1, 10 + 1):
            for vertical in range(1, 10 + 1):
                layers = Layers(
                    horizontal=horizontal,
                    vertical=vertical,
                    delta=abs(
                        (horizontal * printer.nozzle_diameter)
                        - (vertical * printer.layer_height)))

                candidates.append(layers)

            candidates.sort(key=lambda c: c.delta)

        candidates.sort(key=lambda c: c.vertical)
        candidates.sort(key=lambda c: c.horizontal)
        candidates.sort(key=lambda c: c.delta)

        return candidates[0]
