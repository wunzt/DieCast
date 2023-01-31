import PySimpleGUI as ui


def min_roll(quantity):
    """Returns the minimum die roll for any die type."""
    return quantity


def max_roll(die, quantity):
    """Returns the maximum die roll for the given die type."""
    return die * quantity


def avg_roll(die, quantity):
    """Returns the average die roll for the given die type."""
    return (min_roll(quantity) + max_roll(die, quantity)) / 2


ui.theme("LightBrown11")

home_layout = [
    [ui.Text("DieCast")],
    [ui.Text("Please enter the quantity of each type of die you wish to roll below.")],
    [ui.Text("d4", tooltip="A 'd4' is a 4-sided die."), ui.VSep(), ui.In(default_text="0", key="d4")],
    [ui.Text("d6", tooltip="A 'd6' is a 6-sided die."), ui.VSep(), ui.In(default_text="0", key="d6")],
    [ui.Text("d8", tooltip="A 'd8' is a 8-sided die."), ui.VSep(), ui.In(default_text="0", key="d8")],
    [ui.Text("d10", tooltip="A 'd10' is a 10-sided die."), ui.VSep(), ui.In(default_text="0", key="d10")],
    [ui.Text("d12", tooltip="A 'd12' is a 12-sided die."), ui.VSep(), ui.In(default_text="0", key="d12")],
    [ui.Text("d20", tooltip="A 'd20' is a 20-sided die."), ui.VSep(), ui.In(default_text="0", key="d20")],
    [ui.Text("d100", tooltip="A 'd100', sometimes called a percentile die, is a 100-sided die."),
     ui.VSep(), ui.In(default_text="0", key="d100")],
    [ui.Button("Roll", tooltip="Click here to generate pseudo-random results."), ui.Button("Clear")]
    ]

window = ui.Window("DieCast", home_layout, element_justification="c")

def results_window():
    results_layout = [
        [ui.Text("DieCast")],
        [ui.Text("Results")],
        [ui.Text(str(val))],
        [ui.Button("Roll Again", tooltip="Click here to generate a new set of pseudo-random results."),
         ui.Button("New Roll", tooltip="Click here to go back and enter a new roll.")]
    ]

    results_window = ui.Window("DieCast Results", results_layout, element_justification="c")

    while True:
        event, values = results_window.read()
        if event == ui.WINDOW_CLOSED:
            break
        if event == "New Roll":
            results_window.close()
            window.write_event_value("Clear", "Clear")
        if event == "Roll Again":
            results_window.close()
            window.write_event_value("Roll", "Roll")

    results_window.close()


while True:
    event, values = window.read()
    if event == ui.WINDOW_CLOSED:
        break

    if event == "Clear":
        if ui.Window("Are you sure?", [[ui.Text("Clear input fields?")],
                                       [ui.Yes(), ui.No()]]).read(close=True)[0] == "Yes":
            window["d4"]("0")
            window["d6"]("0")
            window["d8"]("0")
            window["d10"]("0")
            window["d12"]("0")
            window["d20"]("0")
            window["d100"]("0")
        else:
            pass

    if event == "Roll":
        die_types = ["d4", "d6", "d8", "d10", "d12", "d20", "d100"]
        die_quantities = [values["d4"], values["d6"], values["d8"], values["d10"], values["d12"],
                          values["d20"], values["d100"]]

        # raise error to user to correct input if not a number
        for val in die_quantities:
            try:
                int_test = int(val)
            except ValueError:
                print("Please enter a whole number.")

        # this is a placeholder for sending the data to the microservice
        i = 0
        for val in die_quantities:
            die = int(die_types[i][1:])
            quant = int(val)
            if int(val) != 0:
                print("You rolled " + val + " " + die_types[i] + ". Lowest possible roll is " +
                      min_roll(val) + ". Highest possible roll is " + str(max_roll(die, quant)) +
                      ". Average roll is " + str(avg_roll(die, quant)) + ".")
            i += 1

        results_window()
