"""
Course:      CST8002 - Programming Language Research Project
Section:     010
Professor:   Stanley Pieda
Author:      Muhammed Burak Tatar (041181274)
File:        model/shrub_cover_record.py

Description:
    Record (entity) class for one row of the Vuntut National Park
    shrub cover dataset. Each field uses a dataset column name.

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


class ShrubCoverRecord:
    """Represents one record (one row) of the shrub cover dataset.

    Every field of this class matches one column of the dataset:
    Identification, Transect number, Species code, Species,
    Start (meters), End (meters), Maximum height (meters), Cover (meters).
    """

    def __init__(self, identification, transect_number, species_code,
                 species, start_meters, end_meters, maximum_height_meters,
                 cover_meters):
        """Create a new ShrubCoverRecord with the values of one CSV row.

        Args:
            identification (int): value of the "Identification" column.
            transect_number (str): value of the "Transect number" column.
            species_code (str): value of the "Species code" column.
            species (str): value of the "Species" column.
            start_meters (float): value of the "Start (meters)" column.
            end_meters (float): value of the "End (meters)" column.
            maximum_height_meters (float): value of the
                "Maximum height (meters)" column.
            cover_meters (float): value of the "Cover (meters)" column.
        """
        # Each instance variable stores one column of the record.
        self.identification = identification
        self.transect_number = transect_number
        self.species_code = species_code
        self.species = species
        self.start_meters = start_meters
        self.end_meters = end_meters
        self.maximum_height_meters = maximum_height_meters
        self.cover_meters = cover_meters

    def __str__(self):
        """Return the record as one formatted line of text for the screen.

        Returns:
            str: the record fields lined up in columns.
        """
        # The numbers after ":" set the column width, so the rows line up.
        return (f"{self.identification:<6}"
                f"{self.transect_number:<10}"
                f"{self.species_code:<10}"
                f"{self.species:<20}"
                f"{self.start_meters:<10.2f}"
                f"{self.end_meters:<10.2f}"
                f"{self.maximum_height_meters:<12.2f}"
                f"{self.cover_meters:<10.2f}")
