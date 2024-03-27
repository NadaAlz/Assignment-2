class Catalog:
    """Class to represent a catalog of artworks"""

    def __init__(self):
        # Initialze catalog object with an empty catalog list
        # The attribute is protected using "_"
        self._catalog = []  # Aggregation: Catalog contains a list of Artwork objects.

    # Function to add the art object to the catalog list
    def add_art(self, art):
        self._catalog.append(art)
        print(art.get_art_title(), "is successfully added to the museum")

    # Function to display each art object that is in the catalog
    def display_catalog(self):
        for art in self._catalog:
            print("Art Title:", art.get_art_title())
            print("Art Type:", art.get_art_type())
            print("Artist:", art.get_artist())
            print("Date of Creation:", art.get_date_oc())
            print("Historical Significance:", art.get_histSign())
            print("Exhibition Location:", art.get_exhLoc())
            print("")
