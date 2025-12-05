import psutil

memory = psutil.virtual_memory()

def convert_bytes(size):
    # Convert bytes to GB
    gb = size / (1024 ** 3)
    return gb

total_gb = convert_bytes(memory.total)
available_gb = convert_bytes(memory.available)
used_gb = convert_bytes(memory.used)

print(f"Total RAM: {total_gb: .3f} GB")
print(f"Available RAM:{available_gb: .3f} GB")
print(f"Used RAM: {used_gb: 3f} GB")
print(f"RAM Usage: {memory.percent}%")



"""
Total RAM:  7.703 GB
Available RAM: 1.043 GB
Used RAM:  6.659821 GB
RAM Usage: 86.5%

"""
