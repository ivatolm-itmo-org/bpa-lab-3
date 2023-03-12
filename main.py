def bin_to_hex(x):
    return hex(int(x, 2))

def bin_to_dec(x):
    return int(x, 2)

def from_twos_complement(x):
    if x[0] == '1':
        x = int(x, 2)
        x = '-' + bin(2**7 - x)[2:]
    return x

# Parsing command from cli
while True:
    try:
        cmd = input()

        # Converting command from hex to decimal integer.
        # Otherwise we cannot work with the number
        cmd_int = int(cmd, 16)

        break
    except Exception as e:
        print(e)

# Converting command to binary for analysis.
cmd_bin_str = bin(cmd_int)

# Removing binary notation from string
cmd_bin = cmd_bin_str[2:]

# Extending command to 16 bits if it has less
if len(cmd_bin) < 16:
    cmd_bin = '0' * (16 - len(cmd_bin)) + cmd_bin

# Extracting data from the cmd
code  = cmd_bin[0 : 4]
flag  = cmd_bin[4]
mode  = cmd_bin[4 + 1 : 8]
shift = cmd_bin[8 + 1 : 16]

# Printing parsed information for the user
print("Parsed command:", bin_to_hex(code))

# Printing information about addressing
if flag == '0':
    # Direct absolute addressing.
    # For direct absolute addressing there is no mode
    #   and shift, so combining mode and shift for address
    address = bin_to_hex(mode + shift)
    print(f"Direct absolute addressing. Address: {address}")

else:
    if mode == '110':
        # Direct relative addressing.
        # Converting shift from two's complement
        shift_hex = bin_to_hex(from_twos_complement(shift))
        shift_dec = bin_to_dec(from_twos_complement(shift))
        print(f"Direct relative addressing. Shift: (IP+({shift_hex}))=(IP+({shift_dec}))")

    elif mode == '000':
        # Indirect relative addressing.
        # For indirect relative addressing shift is an address
        #   of the cell with shift
        address = bin_to_hex(from_twos_complement(shift))
        print(f"Indirect relative addressing. Shift: (IP+[{address}])")

    elif mode == '010':
        # Indirect (relative) autoincremental addressing.
        # For indirect autoincremental addressing shift is an address
        #   of the cell with shift. Also there is increment after fetch
        address = bin_to_hex(from_twos_complement(shift))
        print(f"Indirect (relative) autoincremental addressing. Shift: (IP+[{address}])+")

    elif mode == '011':
        # Indirect (relative) autodecremental addressing.
        # For indirect autodecremental addressing shift is an address
        #   of the cell with shift. Also there is decrement at the start
        address = bin_to_hex(from_twos_complement(shift))
        print(f"Indirect (relative) autodecremental addressing. Shift: -(IP+[{address}])")

    elif mode == '111':
        # Direct with operand loading.
        # Shift contains value to load into the command directly
        value = bin_to_hex(from_twos_complement(shift))
        print(f"Direct with operand loading. Value: {value}")
