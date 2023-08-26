import os

class DirectAccessFile:

    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, "rb+")
        self.record_size = os.path.getsize(filename) // len(self.file.read(1))

    def read_record(self, record_number):
        physical_address = record_number * self.record_size
        self.file.seek(physical_address)
        record = self.file.read(self.record_size)
        return record

    def write_record(self, record_number, record):
        physical_address = record_number * self.record_size
        self.file.seek(physical_address)
        self.file.write(record)

    def delete_record(self, record_number):
        physical_address = record_number * self.record_size
        self.file.seek(physical_address)
        self.file.write(b"\x00" * self.record_size)

    def close(self):
        self.file.close()



file = DirectAccessFile("my_file.dat")

    # Create a record
record = {"name": "John Doe", "age": 30}

    # Write the record to the file
file.write_record(1, record)

    # Read the record from the file
read_record = file.read_record(1)
print(read_record)

    # Delete the record from the file
file.delete_record(1)

    # Close the file
file.close()
