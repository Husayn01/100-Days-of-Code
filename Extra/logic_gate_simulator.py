def logic_gate_simulator(A, B, type_gate):
    """
    Simulates various logic gates based on the given inputs and gate type.
    Returns:
    bool: The result of the logic gate operation.
    str: "Invalid Gate" if the gate type is not recognized.

    """
    if type_gate == "AND":
        return A and B
    elif type_gate == "OR":
        return A or B
    elif type_gate == "NOT":
        return not A
    elif type_gate == "NAND":
        return not (A and B)
    elif type_gate == "NOR":
        return not (A or B)
    elif type_gate == "XOR":
        return A ^ B
    elif type_gate == "NXOR":
        return not (A ^ B)
    else:
        return "Invalid Gate"

print(logic_gate_simulator(True, False, "OR"))

