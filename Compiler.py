def compiler(text: str) -> str:
    current_byte = 0
    compiled_commands = []

    i = 0
    while i < len(text):
        char = text[i]
        target_byte = ord(char)

        repeat_count = 1
        while i + repeat_count < len(text) and text[i + repeat_count] == char:
            repeat_count += 1

        diff_forward = (target_byte - current_byte) % 256
        diff_backward = (current_byte - target_byte) % 256


        if diff_forward <= diff_backward:
            steps = diff_forward
            if steps > 0:
                compiled_commands.append(f"Mi{'a' * steps}w")
        else:
            steps = diff_backward
            if steps > 0:
                compiled_commands.append(f"My{'a' * steps}w")


        compiled_commands.append(f"Me{'a' * repeat_count}w")
        current_byte = target_byte
        i += repeat_count

    return " ".join(compiled_commands)


