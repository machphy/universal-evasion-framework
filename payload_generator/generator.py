import random
import string
import os

def randomize_string(length=16):
    """Generate a random alphanumeric string of given length."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_payload(template, output_file):
    """
    Generate a mutated payload by replacing $$RAND$$ in the template
    with a newly randomized string and write to output_file.
    """
    mutated = template.replace("$$RAND$$", randomize_string())
    full_path = os.path.join(os.path.dirname(__file__), output_file)

    with open(full_path, 'w') as f:
        f.write(mutated)
    print(f"[+] Payload generated and saved to {full_path}")

if __name__ == "__main__":
    template = "print('Payload execution: $$RAND$$')"
    generate_payload(template, "payload.py")
