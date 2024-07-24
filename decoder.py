def decode(password):
    return ''.join(str((int(char) - 3) % 10) for char in password)
