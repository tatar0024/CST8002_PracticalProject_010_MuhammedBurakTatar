"""
Course:      CST8002 - Programming Language Research Project
Section:     010
Professor:   Stanley Pieda
Author:      Muhammed Burak Tatar (041181274)
File:        main.py

Description:
    Main program (entry point). Loads the first records of the shrub
    cover dataset into a list and shows them on the screen.

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

import os

from persistence.dataset_reader import read_records

AUTHOR_NAME = "Muhammed Burak Tatar"
"""Full name of the author, always shown on the screen."""

NUMBER_OF_RECORDS_TO_LOAD = 10
"""How many records are read from the dataset."""

DATASET_FILE_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data", "vuntut_np_shrub_cover_2016_data.csv")
"""Full path of the dataset file (inside the "data" folder)."""


def print_author_banner():
    """Print a line with the author's full name."""
    print("=" * 88)
    print(f"  Program by: {AUTHOR_NAME}")
    print("=" * 88)


def print_records(records):
    """Print a table heading and then every record in the list.

    Args:
        records (list): the ShrubCoverRecord objects to print.
    """
    print("Vuntut National Park - Shrub Cover 2016 (Parks Canada)")
    print("Contains information licensed under the Open Government "
          "Licence - Canada.")
    print()
    print(f"{'ID':<6}{'Transect':<10}{'Code':<10}{'Species':<20}"
          f"{'Start(m)':<10}{'End(m)':<10}{'MaxHeight':<12}{'Cover(m)':<10}")
    print("-" * 88)

    # Loop over the list and print each record on its own line.
    for record in records:
        print(record)

    print("-" * 88)
    print(f"{len(records)} records loaded.")


def main():
    """Load the records from the dataset and show them on the screen."""
    print_author_banner()

    try:
        shrub_cover_records = read_records(DATASET_FILE_PATH,
                                           NUMBER_OF_RECORDS_TO_LOAD)
        print_records(shrub_cover_records)
    except FileNotFoundError:
        print(f"Error: the dataset file was not found:\n{DATASET_FILE_PATH}")
    except (ValueError, IndexError):
        print("Error: the dataset file has a row that could not be read.")
    except OSError as error:
        print(f"Error: the dataset file could not be opened: {error}")
    finally:
        # The name is printed again at the end, so it is always visible.
        print_author_banner()


if __name__ == "__main__":
    main()
