import csv



def create_csv():

    with open("film_notes.csv", "w") as file:
        fieldnames = ["film_name", "note", "rate"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({"film_name": "Harry Potter and Philosopher's Stone", "note": "watch again, perfect", "rate": 5})
        writer.writerow({"film_name": "Harry Potter and Chamber of Secrets", "note": "watch again, scary", "rate": 4.5})
        writer.writerow({"film_name": "Harry Potter and Prisoner of Azkaban", "note": "okay", "rate": 3.5})
        writer.writerow({"film_name": "Harry Potter and Goblet of Fire", "note": "amazing, definitely watch again", "rate": 5})
        writer.writerow({"film_name": "Harry Potter and Order of the Phoenix", "note": "normal, book much better", "rate": 3})
        writer.writerow({"film_name": "Harry Potter and Half-Blood Prince", "note": "dislike the movie", "rate": 2.5})
        writer.writerow({"film_name": "Harry Potter and Deathly Hallows Pt.1", "note": "definitely like", "rate": 4.5})
        writer.writerow({"film_name": "Harry Potter and Deathly Hallows Pt.2", "note": "perfect", "rate": 5})


create_csv()


def read_file(file):
    with open(file, 'r') as f:
        reader = csv.reader(f)
            


class Note:

    def __init__(self, film_name, note, rating):
        self.film_name = film_name
        self.note = note
        self.rating = rating

    def add_note(self, file):
        with open(file, 'a', encoding='UTF8', newline='') as f:
            input_data = [self.film_name, self.note, self.rating]
            writer = csv.writer(f)
            writer.writerow([i for i in input_data])
            return print(f"Added '{self.film_name}' to the file '{file}'")

    def remove_note(self, film_name):
        lines = []
        with open('film_notes.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] != film_name:
                    lines.append(row)

        with open('film_notes.csv', 'w') as f:
            writer = csv.writer(f)
            [writer.writerow(row) for row in lines]
            print(f"Film {film_name} was removed from list")

    def print_note(self, film_name):
        notes = []
        with open('film_notes.csv', 'r') as file:
            reader = csv.reader(file)
            [notes.append(row[1])  for row in reader if row[0] == film_name]
            return print(f"The notes of the film '{film_name}' is: {notes}")

    def get_rate(self, func):
        with open('film_notes.csv', 'r', newline='') as file:
            dict_reader = list(csv.DictReader(file))
            top_rate = func(dict_reader, key=lambda x: x['rate']).get('rate')
            top_films = [film['film_name'] for film in dict_reader if film['rate'] == top_rate]
            print(f"The {func.__name__} rate is <{top_rate}>  of the film(s) {top_films}")
            return top_films

    def get_lowest_rate(self):
        return self.get_rate(min)

    def get_highest_rate(self):
        return self.get_rate(max)

    def get_average_rate(self):
        with open('film_notes.csv', 'r', newline='') as file:
            dict_reader = csv.DictReader(file)
            rates = []
            integer_rate_list = []
            for i in dict_reader:
                rates.append(i['rate'])
            [integer_rate_list.append(float(x)) for x in rates]
            return print(f"Average film rate is {sum(integer_rate_list) / len(integer_rate_list)}")



note_1 = Note('Spywoman', 'funny', 5)
note_2 = Note('Spychildren', 'perfect', 4.5)
note_3 = Note('Alice in Wonderland', 'nice', 4)

note_1.add_note('film_notes.csv')
note_2.add_note('film_notes.csv')
note_3.add_note('film_notes.csv')

note_1.print_note('Spywoman')

note_1.remove_note('Spychildren')

note_1.get_highest_rate()

note_1.get_lowest_rate()

note_1.get_average_rate()

