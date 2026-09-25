"""
Course:      CST8002 - Programming Language Research Project
Section:     010
Professor:   Stanley Pieda
Author:      Muhammed Burak Tatar (041181274)
File:        persistence/dataset_reader.py

Description:
    Reads the shrub cover CSV dataset and turns each row into a
    ShrubCoverRecord object.

Dataset:
    Contains information licensed under the Open Government Licence -
    Canada. https://open.canada.ca/en/open-government-licence-canada

References:
    [1] Parks Canada, "Shrub cover-Vuntut," Open Government Portal,
        Oct. 1, 2017. Accessed: Sep. 24, 2026. [Online]. Available:
        https://open.canada.ca/data/en/dataset/ddd98f33-d155-45d5-9b14-a6b4ee186580
    [2] Python Software Foundation, "9. Classes," The Python Tutorial.
        Accessed: Sep. 24, 2026. [Online]. Available:
        https://docs.python.org/3/tutorial/classes.html
    [3] Python Software Foundation, "csv - CSV File Reading and Writing,"
        The Python Standard Library. Accessed: Sep. 24, 2026. [Online].
        Available: https://docs.python.org/3/library/csv.html
    [4] Python Software Foundation, "8. Errors and Exceptions," The Python
        Tutorial. Accessed: Sep. 24, 2026. [Online]. Available:
        https://docs.python.org/3/tutorial/errors.html
    [5] Python Software Foundation, "6. Modules," The Python Tutorial.
        Accessed: Sep. 24, 2026. [Online]. Available:
        https://docs.python.org/3/tutorial/modules.html
    [6] D. Goodger and G. van Rossum, "PEP 257 - Docstring Conventions,"
        Python Enhancement Proposals, May 29, 2001. Accessed: Sep. 24,
        2026. [Online]. Available: https://peps.python.org/pep-0257/
    [7] Government of Canada, "Open Government Licence - Canada,"
        Open Government Portal. Accessed: Sep. 24, 2026. [Online].
        Available: https://open.canada.ca/en/open-government-licence-canada
"""

import csv

from model.shrub_cover_record import ShrubCoverRecord

FILE_ENCODING = "cp1252"
"""Text encoding of the dataset file (Windows-1252, for the French row)."""

NUMBER_OF_HEADER_ROWS = 2
"""Rows to skip: row 1 has English column names, row 2 has French ones."""


def read_records(file_path, number_of_records):
    """Read records from the dataset file and return them in a list.

    Args:
        file_path (str): path of the CSV dataset file.
        number_of_records (int): how many records to read from the file.

    Returns:
        list: a list of ShrubCoverRecord objects.

    Raises:
        FileNotFoundError: if the dataset file does not exist.
        ValueError: if a number in the file cannot be converted.
    """
    shrub_cover_records = []

    # "with" closes the file automatically, even if an error happens.
    with open(file_path, "r", encoding=FILE_ENCODING,
              newline="") as dataset_file:
        csv_reader = csv.reader(dataset_file)

        # Skip the English and the French column name rows.
        for _ in range(NUMBER_OF_HEADER_ROWS):
            next(csv_reader)

        for row in csv_reader:
            # Stop when we have loaded the number of records we want.
            if len(shrub_cover_records) >= number_of_records:
                break

            # Split the row into its columns and convert the numbers.
            record = ShrubCoverRecord(
                identification=int(row[0]),
                transect_number=row[1].strip(),
                species_code=row[2].strip(),
                species=row[3].strip(),
                start_meters=float(row[4]),
                end_meters=float(row[5]),
                maximum_height_meters=float(row[6]),
                cover_meters=float(row[7]))

            shrub_cover_records.append(record)

    return shrub_cover_records
