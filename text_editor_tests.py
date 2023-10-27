from app.text_editor.text_editor import TextEditor


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
