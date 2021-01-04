# Single Responsibility Principle (SRP)
class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n ' .join(self.entries)


class Persistence:
    @staticmethod
    def save_to_file(j, filename):
        f = open(filename, 'w')
        f.write(str(j))
        f.close()


journal = Journal()
journal.add_entry('The first day.')
journal.add_entry('The second day.')

print(f'Journal entries :\n{journal}')

file = r'/Users/jahednaghipoor/Desktop/Codes/Python codes/Design Pattern /SOLID/SRP.txt'
Persistence.save_to_file(journal, file)

with open(file) as fh:
    print(fh.read())
