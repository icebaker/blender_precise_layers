from .logic import (Logic, Xyz, Layers, PrinterSettings)


def test_logic():
    assert Logic.layers_for(PrinterSettings(
        nozzle_diameter=0.4, layer_height=0.28,
    )) == Layers(horizontal=7, vertical=10, delta=0.0)

    assert Logic.cubify(
        Xyz(x=7.5, y=3.2, z=5.4),
        PrinterSettings(nozzle_diameter=0.4, layer_height=0.28)
    ) == 8.4

    assert Logic.cubify(
        Xyz(x=10, y=10, z=10),
        PrinterSettings(nozzle_diameter=0.4, layer_height=0.28)
    ) == 11.200000000000001

    assert Logic.mm_to_layers(
        8.4,
        PrinterSettings(nozzle_diameter=0.4, layer_height=0.28)
    ) == Layers(horizontal=21, vertical=30, delta=0.0)

    assert Logic.mm_to_layers(
        11.200000000000001,
        PrinterSettings(nozzle_diameter=0.4, layer_height=0.28)
    ) == Layers(horizontal=28, vertical=40, delta=0.0)
