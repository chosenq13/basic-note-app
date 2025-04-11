import os
import json
import datetime

class Note:
    def __init__(self,note_text,date):
        self.note_text = note_text
        self.date = date

    def __str__(self):
        return (f"{self.note_text} - {self.date}")

    def to_dict(self):
        return {
            "note_text": self.note_text,
            "date": self.date.strftime("%Y-%m-%d %H:%M:%S")
        }

    @staticmethod
    def from_dict(data):
        return Note(
            note_text=data["note_text"],
            date=datetime.datetime.strptime(data["date"], "%Y-%m-%d %H:%M:%S")
        )


class NotesApp:
    def __init__(self):
        self.notes = []

    def add_note(self,note):
        self.notes.append(note)

    def list_notes(self):
        for i,_note in enumerate(self.notes):
            print("----------")
            print(f"{i}- {_note}")
            print("----------")

    def load_from_file(self, filename):
        if os.path.exists(filename):
            with open(filename, "r") as f:
                self.notes = [Note.from_dict(item) for item in json.load(f)]

    def save_to_file(self,filename):
        with open(filename,"w") as f:
            json.dump([note.to_dict() for note in self.notes], f, ensure_ascii=False, indent=4)

    def delete_note(self,note):
        try:
            self.notes.pop(note)
            self.save_to_file("notes.json")
            print("Deleted note")
        except IndexError:
            print("Invalid note")








my_app = NotesApp()

def run():
    my_app.load_from_file("notes.json")
    print("--Notes app loaded--\n"
          "Welcome to the Notes app!\n"
          "Please select your action!\n"
          "1- Create a Note\n"
          "2- List Notes\n"
          "3- Search Notes\n"
          "4- Delete Notes\n"
          "5- Quit App\n")

    user_input = input("> ")

    if user_input == "1":
        note_text = input("Note text: ")
        new_note = Note(note_text,datetime.datetime.now())
        my_app.add_note(new_note)
        my_app.save_to_file("notes.json")

    elif user_input == "2":
        my_app.list_notes()

    elif user_input == "3":
        user_input = input("Search Keys: ")
        for search_note in my_app.notes:
            if user_input.lower() in search_note.note_text.lower():
                print(search_note.note_text)

    elif user_input == "4":
        my_app.list_notes()
        delete_input = input("Which Note: ")
        my_app.delete_note(int(delete_input))

    elif user_input == "5":
        exit()
    else:
        print("Invalid input")



while True:
    run()

