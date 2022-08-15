import csv
import unittest

from main import Note, create_csv, read_file

note_charlie = Note('Charlie and the Chocolate Fabric', 'super interesting', 5)
note_marley = Note('Marley and Me', 'super sad', 4.8)
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

    def test_print_note(self):
        film_name = "Marley and me"
        note_marley.add_note(file)
        # with open('film_notes.csv', 'r') as f:
        #     reader = csv.reader(f)
        #     [print(i) for i in reader]
        self.assertEqual(note_marley.print_note(film_name), None)

    def test_get_lowest_rate(self):
        result = ['Harry Potter and Half-Blood Prince']
        self.assertEqual(note_charlie.get_lowest_rate(), result)

    def test_get_highest_rate(self):
        result = ["Harry Potter and Philosopher's Stone",
                  'Harry Potter and Goblet of Fire',
                  'Harry Potter and Deathly Hallows Pt.2']
        self.assertEqual(note_charlie.get_highest_rate(), result)

    def test_get_average_rate(self):
        self.assertEqual(Note.get_average_rate(self), None)


