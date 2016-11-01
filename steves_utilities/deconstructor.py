def chunkify(input_list, chunk_size):

    input_list = list(input_list)
    chunks = []
    while input_list:
        this_chunk = set()
        for i in range(chunk_size):
            try:
                this_chunk.add(input_list.pop())
            except IndexError:
                break
        chunks.append(this_chunk)
    return chunks