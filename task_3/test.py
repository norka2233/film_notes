import csv
import unittest

from main import Note, create_csv, read_file

file = 'film_notes.csv'


class TestFilmNotes(unittest.TestCase):
    def setUp(self):
        create_csv()
        read_file('film_notes.csv')

    def test_add_note_correct_input(self):
        note = Note('Charlie and the Chocolate Fabric', 'super interesting', 5)
        self.assertEqual(note.add_note(file), "Added 'Charlie and the Chocolate Fabric' to the file 'film_notes.csv'")

    def test_add_note_not_correct_input(self):
        note = Note(2, 2, 5)
        self.assertEqual(note.add_note(file), TypeError)
