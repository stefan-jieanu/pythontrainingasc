def read_in_chunks(filename, chunk_size):
    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk: # Am ajuns la sfarsitul fisierului
                break
            yield chunk.decode('utf-8')

# Create a test file
with open('big_file.txt', 'w') as f:
    for i in range(1, 10000):
        f.write(f'This is line {i}\n')

# Reading the file chunk by chunk
file_chunks = read_in_chunks('big_file.txt', 1024)
print(next(file_chunks))
print(next(file_chunks))