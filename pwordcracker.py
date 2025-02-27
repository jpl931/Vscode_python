import itertools

def brute_force_crack(password, charset='abcdefghijklmnopqrstuvwxyz):
    for length in range(1, 9):  # Adjust the range for longer passwords
        for attempt in itertools.product(charset, repeat=length):
            attempt = ''.join(attempt)
            if attempt == password:
                return attempt
    return None

password = 'abc'  # Example password
cracked_password = brute_force_crack(password)
print(f'Cracked password: {cracked_password}')