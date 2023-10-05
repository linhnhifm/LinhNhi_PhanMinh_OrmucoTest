"""
Question A: 
Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the x-axis and returns whether they overlap. 
As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8). 
"""

import unittest

# Helper functions
def is_input_tuple(line1, line2):
    return isinstance(line1, tuple) and isinstance(line2, tuple)

def is_valid_line(x1, x2):
    return x1 <= x2

# Main function to check if lines overlap
"""
Please note the following: 
1. A line (x1, x2) is only valid if the left endpoint x1 is less than or equal to the right endpoint x2. 
For example, (1,5) is a valid line because x1 = 1 is less than x2 = 5.
On the other hand, (5,1) is not a valid line because x1 = 5 is greater than x1 = 1.

2. Adjacent lines that share a same endpoint are considered overlapping lines. 
For example, (1,5) and (5,6) are overlapping lines because they both touch 5.

3. Lines with the same left and right endpoints are considered overlapping lines.
For example, (1,5) and (1,5) are two lines with the same left and right endpoints. They are considered overlapping lines.

4. A line (x1, x2) where x1 = x2 is also considered a line.
For example, (1,1) is a line. 

5. Lines can have negative endpoints. 
For example, (-5, -1) is a valid line.
"""
def do_lines_overlap(line1, line2):
    if not is_input_tuple(line1, line2):
        return "One or more invalid inputs. Input needs to be a tuple."
    
    if not is_valid_line(line1[0], line1[1]) or not is_valid_line(line2[0], line2[1]):
        return "One or more invalid lines. Left endpoint should be less than or equal to the right endpoint."

    x1, x2 = line1
    x3, x4 = line2

    if max(x1, x3) <= min(x2, x4):
        return True
    return False

# Test cases
class TestLineSegmentOverlap(unittest.TestCase):
    def test_valid_line_segment(self):
        self.assertTrue(is_valid_line(1, 5))
        self.assertTrue(is_valid_line(-2, -1))
        self.assertTrue(is_valid_line(0, 0)) 

    def test_invalid_line_segment(self):
         self.assertFalse(is_valid_line(5, 1)) 

    def test_valid_input(self): 
        self.assertTrue(is_input_tuple((1, 5), (5, 1)))
    
    def test_invalid_input(self):
        self.assertFalse(is_input_tuple("abc", "def"))
        self.assertFalse(is_input_tuple(None, (5, 1)))
        self.assertFalse(is_input_tuple((1, 5), 5))
        self.assertFalse(is_input_tuple((1, 5), [5, 1]))

    def test_lines_overlap(self): 
        self.assertTrue(do_lines_overlap((1, 5), (2, 6)))
        self.assertTrue(do_lines_overlap((3, 6), (4, 5)))
        self.assertTrue(do_lines_overlap((-2, 2), (-1, 1)))
        self.assertTrue(do_lines_overlap((1, 5), (1, 5)))
        self.assertTrue(do_lines_overlap((0, 0), (0, 0))) 

    def test_lines_no_overlap(self):
        self.assertFalse(do_lines_overlap((1, 5), (6, 8)))
        self.assertFalse(do_lines_overlap((-3, -2), (-1, 4)))
        self.assertFalse(do_lines_overlap((3, 4), (1, 2)))
        self.assertFalse(do_lines_overlap((0, 0), (2, 2)))

if __name__ == '__main__':
    unittest.main()