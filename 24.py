# Below is a minimal example to parse and simulate the gates.
# Provide your puzzle input lines in input_lines and run.
import sys
import itertools
import re
import graphviz

def parse_input(lines):
    # parse wire initial values and gate definitions
    # return wires_init, gates
    wires = {}
    gates = []

    # Parse lines
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if ':' in line:
            # Wire initialization "x00: 1"
            wire, val = line.split(':')
            wires[wire.strip()] = int(val.strip())
        else:
            # Gate "a AND b -> c" or "x XOR y -> z", etc.
            m = re.match(r'(.*?) (AND|OR|XOR) (.*?) -> (.*)', line)
            if m:
                inp1, op, inp2, out = m.groups()
                gates.append((inp1.strip(), op.strip(), inp2.strip(), out.strip()))
    return wires, gates

def simulate(wires_init, gates):
    # run boolean logic simulation
    # return final wire values
    wires = wires_init.copy()
    updated = True
    while updated:
        updated = False
        for inp1, op, inp2, out in gates:
            if out in wires:
                continue
            if inp1 in wires and inp2 in wires:
                if op == 'AND':
                    wires[out] = wires[inp1] & wires[inp2]
                elif op == 'OR':
                    wires[out] = wires[inp1] | wires[inp2]
                elif op == 'XOR':
                    wires[out] = wires[inp1] ^ wires[inp2]
                updated = True
    return wires

def simulate_gates(wires, gates):
    updated = True
    while updated:
        updated = False
        for inp1, op, inp2, out in gates:
            if out in wires:
                continue
            if inp1 in wires and inp2 in wires:
                if op == 'AND':
                    wires[out] = wires[inp1] & wires[inp2]
                elif op == 'OR':
                    wires[out] = wires[inp1] | wires[inp2]
                elif op == 'XOR':
                    wires[out] = wires[inp1] ^ wires[inp2]
                updated = True
    return wires

def find_wrong_bits(lines, expected_decimal):
    wires, gates = parse_input(lines)
    wires = simulate_gates(wires, gates)
    z_wires = sorted([w for w in wires if w.startswith('z')], key=lambda w: int(w[1:]))
    bit_str = ''.join(str(wires[w]) for w in reversed(z_wires))
    actual_decimal = int(bit_str, 2) if bit_str else 0
    if actual_decimal == expected_decimal:
        print("All bits match.")
        return
    # Compare bits
    exp_bin = bin(expected_decimal)[2:].zfill(len(z_wires))
    act_bin = bin(actual_decimal)[2:].zfill(len(z_wires))
    differences = []
    # Compare from least significant bit up
    for i, (eb, ab) in enumerate(zip(reversed(exp_bin), reversed(act_bin))):
        if eb != ab:
            differences.append(f"z{str(i).zfill(2)} (expected {eb}, got {ab})")
    print(f"Wrong bits: {differences}")

def find_swaps(lines, max_bit_count):
    wires_init, gates = parse_input(lines)
    # gather all gate output wires
    output_wires = [g[3] for g in gates]  # (inp1, op, inp2, out)
    unique_outs = list(set(output_wires))
    # generate combinations of 8 distinct wires in pairs of two
    for combo in itertools.combinations(unique_outs, 8):
        # split combo into four pairs in all possible ways
        # for each pairing, swap in gates, check correctness
        # if correct, return sorted list joined by commas
        ...
    return None

def assign_wire_indices(input_lines):
    import re

    # Data structures
    # wire_to_indices: wire -> set of possible bit indices
    # gates: list of (inp1, op, inp2, out)
    # errors: list of errors found
    wire_to_indices = {}
    gates = []
    errors = []

    def parse_wire(w):
        # if matches [xy](digits) or z(digits), extract digits
        m = re.match(r'([xyz])(\d+)', w)
        if m:
            return int(m.group(2))
        return None

    # Parse lines
    for line in input_lines:
        line = line.strip()
        if not line or ':' in line:
            # ignoring initialization or empty lines here
            continue
        m = re.match(r'(.*?) (AND|OR|XOR) (.*?) -> (.*)', line)
        if m:
            inp1, op, inp2, out = m.groups()
            gates.append((inp1.strip(), op.strip(), inp2.strip(), out.strip()))

    # Initialize known indices from wire names that start with x## or y##
    for gate in gates:
        for w in gate[:3]:  # inp1, inp2
            i = parse_wire(w)
            if i is not None and w not in wire_to_indices:
                wire_to_indices[w] = {i}

    # Iteratively assign indices
    changed = True
    while changed:
        changed = False
        for inp1, _, inp2, out in gates:
            s1 = wire_to_indices.get(inp1, set())
            s2 = wire_to_indices.get(inp2, set())
            # If both inputs have exactly one index and match, assign out
            if len(s1) == 1 and s1 == s2:
                if out not in wire_to_indices:
                    wire_to_indices[out] = set(s1)
                    changed = True
                else:
                    # If out differs, it's an error
                    if wire_to_indices[out] != s1:
                        errors.append(f"Wire {out} conflict: {wire_to_indices[out]} vs {s1}")
            # If inputs mismatch (one wire has multiple or different indices), note that
            elif s1 and s2 and s1 != s2:
                errors.append(f"Input conflict: {inp1}={s1}, {inp2}={s2}")

    # Check if any z## wire got a different index
    for w, idxs in wire_to_indices.items():
        if w.startswith('z'):
            wire_idx = parse_wire(w)
            if wire_idx is not None and (len(idxs) == 1) and wire_idx not in idxs:
                errors.append(f"Wire {w} has index {list(idxs)} but name suggests {wire_idx}")
    
    return wire_to_indices, errors
def find_expected_and_current(lines):
    # Parse wires and gates
    wires_init, gates = parse_input(lines)

    # Gather bits for x and y
    def gather_bits(prefix):
        # collect (<index>, <value>)
        bits = []
        for w, val in wires_init.items():
            if w.startswith(prefix):
                i = int(w[len(prefix):])
                bits.append((i, val))
        # sort by bit index; build binary string (least significant bit first)
        bits.sort(key=lambda x: x[0])
        bin_str = ''.join(str(b[1]) for b in bits[::-1]) or '0'
        return int(bin_str, 2)

    x_val = gather_bits('x')
    y_val = gather_bits('y')
    expected = x_val + y_val

    # Simulate to get current z-value
    def simulate_gates(wires, gate_list):
        updated = True
        while updated:
            updated = False
            for inp1, op, inp2, out in gate_list:
                if out in wires:
                    continue
                if inp1 in wires and inp2 in wires:
                    if op == 'AND':
                        wires[out] = wires[inp1] & wires[inp2]
                    elif op == 'OR':
                        wires[out] = wires[inp1] | wires[inp2]
                    elif op == 'XOR':
                        wires[out] = wires[inp1] ^ wires[inp2]
                    updated = True
        return wires

    # Copy wires so we don't mutate the original
    final_wires = simulate_gates(dict(wires_init), gates)

    # Gather z bits
    z_bits = []
    for w, val in final_wires.items():
        if w.startswith('z'):
            i = int(w[1:])
            z_bits.append((i, val))
    z_bits.sort(key=lambda x: x[0])
    bin_str = ''.join(str(b[1]) for b in z_bits[::-1]) or '0'
    current = int(bin_str, 2)

    
    return expected, current

def parse_gates(gate_lines):
    """
    Parses gate definitions into a list of tuples: (inp1, op, inp2, out)
    """
    gates = []
    for line in gate_lines:
        line = line.strip()
        if not line or ':' in line:
            continue
        m = re.match(r'(.*?) (AND|OR|XOR) (.*?) -> (.*)', line)
        if m:
            inp1, op, inp2, out = m.groups()
            gates.append((inp1.strip(), op.strip(), inp2.strip(), out.strip()))
    return gates

def create_graph(gates, output_path='gates_graph.gv'):
    """
    Creates a graph of the gates and wires using Graphviz.
    Each gate is represented as a node, connected to its input and output wires.
    """
    dot = graphviz.Digraph(comment='Gates and Wires', format='png')
    
    for inp1, op, inp2, out in gates:
        gate_label = op
        gate_node = f'gate_{inp1}_{op}_{inp2}'
        dot.node(gate_node, gate_label, shape='circle')
        
        # Connect input wires to gate
        dot.edge(inp1, gate_node)
        dot.edge(inp2, gate_node)
        
        # Connect gate to output wire
        dot.edge(gate_node, out)
    
    dot.render(output_path, view=True)

def main():
    import sys
    orig, rules = sys.stdin.read().split('\n\n')
    orig = orig.splitlines()
    rules = rules.splitlines()
    wire_indices, errors = assign_wire_indices(orig+rules)
    expected, current = find_expected_and_current(orig+rules)
    for i, (exp, cur )in enumerate(zip(bin(expected), bin(current))):
        if exp != cur:
            print(f"Bit mismatch {i}: expected {exp}, got {cur}")
            for w, idxs in wire_indices.items():
                if i in idxs:
                    print(f"  Wire {w} has index {i}")
    # Example gate definitions (replace with your actual gate lines)
    
    gates = parse_gates(rules)
    create_graph(gates, output_path='gates_graph')

if __name__ == "__main__":
    main()