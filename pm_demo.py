from session_pm.compression_service import CompressionService

sample_input = input("Message to compress: ")
print(sample_input)

compression_srvc = CompressionService()
compressed_input = compression_srvc.compress_data(sample_input.encode())
print(compressed_input)

decompressed_data = compression_srvc.decompress_data(compressed_input)
print(decompressed_data)
