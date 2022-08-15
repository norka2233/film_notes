import csv
import unittest

from main import Note, create_csv, read_file

note_charlie = Note('Charlie and the Chocolate Fabric', 'super interesting', 5)
note_marley = Note('Marley and me', 'super sad', 4.8)
file = 'film_notes.csv'

class TestFilmNotes(unittest.TestCase):


    def setUp(self):
        create_csv()
        read_file(file)

    def test_add_note_correct_input(self):
        self.assertEqual(note_charlie.add_note(file), f"Added '{note_charlie.film_name}' to the file 'film_notes.csv'")
        self.assertEqual(note_marley.add_note(file), f"Added '{note_marley.film_name}' to the file 'film_notes.csv'")

    def test_remove_note(self):
        film_name = 'Charlie and the Chocolate Fabric'
        self.assertEqual(note_charlie.remove_note(film_name), f"Film {film_name} was removed from list")

    # def test_remove_note_incorrect_input(self):
    #     film_name = 5
    #     self.assertEqual(note.remove_note(film_name), TypeError)