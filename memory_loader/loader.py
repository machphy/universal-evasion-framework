def run_in_memory(payload_file):
    """
    Read and execute Python code from payload_file in memory.
    """
    with open(payload_file, 'r') as f:
        code = f.read()
    exec(code)

if __name__ == "__main__":
    run_in_memory("payload_generator/payload.py")
