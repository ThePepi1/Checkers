class DictionarySerializer:
    def __init__(self,path):
        self.dictionary = {}
        self.path = path
    def load_from_file(self):
        try:
            with open(self.path, 'r') as file:
                self.dictionary = eval(file.read())
                print("Dictionary loaded successfully!")
        except FileNotFoundError:
            print("File not found!")
        except Exception as e:
            print(f"Error occurred while loading dictionary: {e}")

    def save_to_file(self):
        try:
            with open(self.path, 'w') as file:
                file.write(str(self.dictionary))
                print("Dictionary saved successfully!")
        except Exception as e:
            print(f"Error occurred while saving dictionary: {e}")
    def add(self, key, value):
        self.dictionary[key] = value
    def return_move(self, key):
        return self.dictionary[key]
    