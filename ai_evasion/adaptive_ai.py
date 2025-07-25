import random
import string
import re
import os

def random_string(length=8):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def obfuscate_code(code):
    # Step 1: Add random comments
    lines = code.split('\n')
    lines = [line + f"  # {random_string()}" if line.strip() and not line.strip().startswith('#') else line for line in lines]

    # Step 2: Rename simple variable assignments
    var_map = {}
    def replace_vars(match):
        var_name = match.group(1)
        if var_name not in var_map:
            var_map[var_name] = random_string()
        return var_map[var_name]

    code = '\n'.join(lines)
    code = re.sub(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\s*=', lambda m: replace_vars(m) + ' =', code)

    # Step 3: Insert dummy function
    dummy = f"\ndef {random_string()}():\n    return {random.randint(1,10)} * {random.randint(2,5)}\n"
    return dummy + "\n" + code

def apply_ai_obfuscation(input_path, output_path):
    with open(input_path, 'r') as f:
        original_code = f.read()

    obfuscated_code = obfuscate_code(original_code)

    with open(output_path, 'w') as f:
        f.write(obfuscated_code)

    print(f"[+] AI-obfuscated payload saved to {output_path}")

if __name__ == "__main__":
    # Automatically obfuscate payload.py and save to payload_ai.py
    input_file = os.path.join(os.path.dirname(__file__), '../payload_generator/payload.py')
    output_file = os.path.join(os.path.dirname(__file__), '../payload_generator/payload_ai.py')
    apply_ai_obfuscation(input_file, output_file)
