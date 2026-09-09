def interpreter(code: str) -> str:
    byte = 0
    output = []

    commands = code.strip().split()

    for command in commands:
        if not (command.startswith('M') and command.endswith('w') and len(command) >= 3):
            return "Error"

        com_type = command[1]
        n = command.count('a')

        if com_type == 'e':
            output.append(chr(byte) * n)
        elif com_type == 'i':
            byte = (byte + n) % 256
        elif com_type == 'y':
            byte = (byte - n) % 256
        else:
            return "Error"


    return "".join(output)


