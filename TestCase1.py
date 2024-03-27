"""Test Case to add new art to the museum"""
from Art import Art
from Catalog import Catalog
from Art import ArtType
from Art import ExhibitionLocation
art1 = Art("Starry Night", ArtType.A, "Vincent van Gogh", "1889", "Iconic masterpiece", ExhibitionLocation.EH)
catalog = Catalog()
catalog.add_art(art1)