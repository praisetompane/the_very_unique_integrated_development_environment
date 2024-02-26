from app.linting.brackets_linter import BracketsLinter
from app.text_editor.text_editor import TextEditor


class IDE:
    class _ansi_escape_sequence_color:
        FAIL = "\033[91m"
        OKGREEN = "\033[92m"
        ENDC = "\033[0m"

    _brackets_linter = None
    _text_editor = None
    _colours = None

    def __init__(self, current_document):
        self._brackets_linter = BracketsLinter()
        self._text_editor = TextEditor(current_document)
        self._colours = self._ansi_escape_sequence_color

    def write(self, code):
        self._text_editor.write(code)
        if self._brackets_linter.lint(code):
            print(
                f"{self._colours.OKGREEN}code passed brackets linting{self._colours.ENDC}"
            )
        else:
            print(
                f"{self._colours.FAIL}code failed brackets linting{self._colours.ENDC}"
            )

    def undo(self):
        self._text_editor.undo()

    def redo(self):
        self._text_editor.redo()