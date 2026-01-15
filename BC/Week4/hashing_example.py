
import hashlib
inputs = ["Blockchain", "Cryptography2025", "Hello, World!"]

for input_str in inputs:
    print(f"Input: {input_str}")
    # Note: SHA-128 is not a standard; using SHA-256 and SHA-512
    sha256_hash = hashlib.sha256(input_str.encode()).hexdigest()
    sha512_hash = hashlib.sha512(input_str.encode()).hexdigest()
    print(f"SHA-256: {sha256_hash} (Length: {len(sha256_hash)})")
    print(f"SHA-512: {sha512_hash} (Length: {len(sha512_hash)})\n")
