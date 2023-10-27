from app.model.stack import Stack

"""
    general use case = undo operations
    Performance:
        N = length of item list
        Space = O(2 * N) = O(N)
        write:
            Time = O(1)
        undo:
            Time= O(1)
        redo:
            Time= O(1)
        display:
            Time= O(1)
"""


class TextEditor:
    undo_stack = None
    redo_stack = None
    document = None

    def __init__(self, document):
        self.undo_stack = Stack()
        self.redo_stack = Stack()
        self.document = document

    def write(self, text):
        self.undo_stack.push(text)
        self.document += text
        self.display()

    def undo(self):
        self.redo_stack.push(self.undo_stack.peek())
        last_word = self.undo_stack.pop()
        self.document = self.document[: -len(last_word)]
        self.display()

    def redo(self):
        self.document += self.redo_stack.pop()
        self.display()

    def display(self):
        print(self.document)


def main():
    print("Praise typing his body of knowldge")
    text_processor = TextEditor("")
    print("My blank slate")
    text_processor.display()
    text_processor.write("I")
    text_processor.write(" ")
    text_processor.write("k")
    text_processor.write("m")
    text_processor.undo()
    text_processor.write("n")
    text_processor.write("o")
    text_processor.write("w")
    print("Try undo and redo")
    text_processor.undo()
    text_processor.redo()
    text_processor.write(" that")
    text_processor.undo()


if __name__ == "__main__":
    main()
