from app.linting.brackets_linter import BracketsLinter

import unittest

"""
    general use case: symmetry test
    Performance:
        N = length of _document
        Time = O(N)
        Space = O(N)
"""


class TestBracketsLinter(unittest.TestCase):
    c_linter = BracketsLinter()

    def valid_code(self):
        valid_code = """
                        public void add(int index, int element){
                            if(numberOfElements < _size)
                                array[index] = element;
                            else {
                                resize();
                                array[index] = element;
                            }
                            numberOfElements++;
                        }
                    """
        self.assertEqual(
            c_linter.lint(valid_code), True, "Ensure valid code passes linting"
        )

    def invalid_code(self):
        invalid_code = """
                    public void add[int index, int element){
                        if(numberOfElements < _size)
                            array[index] = element;
                        else {
                            resize();
                            array(index] = element;
                        }
                        numberOfElements++;
                    }
                """
        self.assertEqual(
            c_linter.lint(invalid_code), False, "Ensure invalid code fails linting"
        )


if __name__ == "__main__":
    unittest.main()
