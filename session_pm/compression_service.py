import gzip


class CompressionService:
    def __init__(self) -> None:
        pass

    def compress_data(self, data: bytes) -> bytes:
        return gzip.compress(data)

    def decompress_data(self, data: bytes) -> bytes:
        return gzip.decompress(data)
