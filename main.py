import os
from typing import Final

FileName = str
Data = str

_CSV_FILE_NAME = "test.csv"
_CSV_FILE_DIR = "."

def does_file_exists(file: FileName) -> bool:
	return os.path.exists(file)

def create_csv(csv_to_create: FileName) -> None:
	csv_fields: Final = "ID,NAME,EMAIL,PASSWORD"

	fd = open(csv_to_create, "w")

	fd.write(csv_fields + '\n')

	fd.close()
	fd = None


def write_csv_file(csv_file: FileName, data_to_write: Data) -> None:
	if(not does_file_exists(csv_file)):
		create_csv(csv_file)
	
	fd = open(csv_file, "+a")

	fd.write(data_to_write + '\n')

	fd.close()
	fd = None

def main() -> int:
	write_csv_file(f"{_CSV_FILE_DIR}/{_CSV_FILE_NAME}", "0,John,johndoe@gmail.com,1234abc")
	return 0

if(__name__ == "__main__"):
	main()
