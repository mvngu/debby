################################################################################
## MIT License
##
## Copyright (C) 2024 Aaron Nguyen <amvngu [AT] gmail [DOT] com>
## Copyright (C) 2023 Duck McSouls <quacksouls [AT] gmail [DOT] com>
##
## Permission is hereby granted, free of charge, to any person obtaining a copy
## of this software and associated documentation files (the "Software"), to deal
## in the Software without restriction, including without limitation the rights
## to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
## copies of the Software, and to permit persons to whom the Software is
## furnished to do so, subject to the following conditions:
##
## The above copyright notice and this permission notice shall be included in
## all copies or substantial portions of the Software.
##
## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
## IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
## FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
## AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
## LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
## OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
## SOFTWARE.
################################################################################

from random import choice, randint

# Some basic mathematics problems.

def is_unique(ell: list) -> bool:
    """
    Whether a list has unique elements.

    @param ell A list.
    @returns True if all elements in the list are unique; false otherwise.
    """
    return len(ell) == len(set(ell))

def is_valid_sub_operands(a: int, b: int) -> bool:
    """
    Whether two numbers are valid subtraction operands.  Two numbers a and b are
    valid subtraction operands if a > b.

    @param a The first operand for subtraction.
    @param b The second operand for subtraction.
    """
    return a > b

def random_add_problems() -> list:
    """
    Generate random addition problems with unknown summands.

    @returns A list of 3-tuples of the form: x + y = z.
    """
    # Simple problems
    simple_low = 10
    simple_high = 99
    simple_n = 5
    simple_a = random_operands(simple_low, simple_high, simple_n)
    simple_b = random_operands(simple_low, simple_high, simple_n)

    # # Intermediate problems
    # inter_low = 100
    # inter_high = 999
    # inter_n = 2
    # inter_a = random_operands(inter_low, inter_high, inter_n)
    # inter_b = random_operands(inter_low, inter_high, inter_n)

    # # Advanced problem
    # adv_low = 1000
    # adv_high = 9999
    # adv_n = 1
    # adv_a = random_operands(adv_low, adv_high, adv_n)
    # adv_b = random_operands(adv_low, adv_high, adv_n)

    a = simple_a # + inter_a + adv_a
    b = simple_b # + inter_b + adv_b
    c = [x + y for x, y in zip(a, b)]
    for i in range(len(a)):
        if choice([True, False]):
            a[i] = "X"
        else:
            b[i] = "X"

    return list(zip(a, b, c))

def random_div_problems() -> list:
    """
    Generate random division problems.

    @returns A list of 2-tuples.  Each tuple contains the operand and result for
        a division problem.
    """
    # Simple problems.
    easy_low = 2
    easy_high = 12
    how_many = 6
    easy_multiple = [1, 1]
    easy_opa = []
    while not is_unique(easy_multiple):
        easy_opa = unique_operands(easy_low, easy_high, how_many)
        opb = unique_operands(easy_low, easy_high, how_many)
        easy_multiple = [a * b for a, b in zip(easy_opa, opb)]

    # Advanced problems.
    adv_low = 13
    adv_high = 40
    adv_multiple = [1, 1]
    adv_opa = []
    while not is_unique(adv_multiple):
        adv_opa = unique_operands(easy_low, easy_high, how_many)
        opb = unique_operands(adv_low, adv_high, how_many)
        adv_multiple = [a * b for a, b in zip(adv_opa, opb)]

    # All division problems.
    multiple = easy_multiple + adv_multiple
    divisor = easy_opa + adv_opa
    return list(zip(multiple, divisor))

def random_mult_problems() -> list:
    """
    Generate random multiplication problems.

    @returns A list of 2-tuples.  Each tuple contains the operands for a
        multiplication problem.
    """
    # Simple problems involving the times table from 2 to 12.
    simple_low = 2
    simple_high = 12
    simple_n = 3
    simple_a = random_operands(simple_low, simple_high, simple_n)
    simple_b = random_operands(simple_low, simple_high, simple_n)

    # Intermediate problems involving the multiplication of two 2-digit numbers.
    inter_low = 13
    inter_high = 99
    inter_n = 3
    inter_a = random_operands(inter_low, inter_high, inter_n)
    inter_b = random_operands(inter_low, inter_high, inter_n)

    # Advanced problems involving the multiplication of a 3-digit number by a
    # 2-digit number.
    adv_low = 100
    adv_high = 999
    adv_n = 3
    adv_a = random_operands(adv_low, adv_high, adv_n)
    adv_b = random_operands(inter_low, inter_high, adv_n)

    # Difficult problems involving the multiplication of two 3-digit numbers.
    diff_low = 100
    diff_high = 999
    diff_n = 1
    diff_a = random_operands(diff_low, diff_high, diff_n)
    diff_b = random_operands(diff_low, diff_high, diff_n)

    a = simple_a + inter_a + adv_a + diff_a
    b = simple_b + inter_b + adv_b + diff_b
    return list(zip(a, b))

def __sub_problems() -> list:
    """
    Generate random subtraction problems.

    @returns A list of 2-tuples.  Each tuple contains the operands for a
        subtraction problem.
    """
    # Simple problems
    simple_low = 10
    simple_high = 99
    simple_n = 5
    simple_a = random_operands(simple_low, simple_high, simple_n)
    simple_b = random_operands(simple_low, simple_high, simple_n)

    # # Intermediate problems
    # inter_low = 100
    # inter_high = 999
    # inter_n = 2
    # inter_a = random_operands(inter_low, inter_high, inter_n)
    # inter_b = random_operands(inter_low, inter_high, inter_n)

    # # Advanced problem
    # adv_low = 1000
    # adv_high = 9999
    # adv_n = 1
    # adv_a = random_operands(adv_low, adv_high, adv_n)
    # adv_b = random_operands(adv_low, adv_high, adv_n)

    a = simple_a # + inter_a + adv_a
    b = simple_b # + inter_b + adv_b
    return list(zip(a, b))

def random_sub_problems() -> list:
    """
    Generate random subtraction problems with unknowns.

    @returns A list of 3-tuples of the form: x - y = z.
    """
    problem = []
    good_problems = False
    while not good_problems:
        problem = __sub_problems()
        valid = [is_valid_sub_operands(x, y) for x, y in problem]
        good_problems = all(valid)

    a = []
    b = []
    c = []
    for x, y in problem:
        if choice([True, False]):
            a.append("X")
            b.append(y)
        else:
            a.append(x)
            b.append("X")
        c.append(x - y)

    return list(zip(a, b, c))

def random_operands(low: int, high: int, how_many: int) -> list:
    """
    Generate random operands for a mathematics problem.

    @param low Minimum value for operand.
    @param high Maximum value for operand.
    @param how_many How many operands to generate.
    @returns A list of random operands.
    """
    return [randint(low, high) for _ in range(how_many)]

def unique_operands(low: int, high: int, how_many: int) -> list:
    """
    Generate random, unique operands for a mathematics problem.

    @param low Minimum value for operand.
    @param high Maximum value for operand.
    @param how_many How many operands to generate.
    @returns A list of random, unique operands.
    """
    op = random_operands(low, high, how_many)
    while not is_unique(op):
        op = random_operands(low, high, how_many)
    return op

def unique_problems(n: int, kind: str) -> list:
    """
    Generate unique, random mathematics problems.

    @param n Generate this many problems.
    @param kind The type of mathematics problem.  Currently supporting these:
        * "+" -- An addition problem.
        * "-" -- A subtraction problem.
        * "x" -- A multiplication problem.
        * "/" -- A division problem.
    @returns A list of 2-tuples.  Each tuple contains the operands for a
        mathematics problem.
    """
    if n < 1:
        raise ValueError("Must generate at least 1 problem")

    problem = []
    match kind:
        case "x":
            while len(set(problem)) < n:
                problem = random_mult_problems()
        case "/":
            while len(set(problem)) < n:
                problem = random_div_problems()
        case "+":
            while len(set(problem)) < n:
                problem = random_add_problems()
        case "-":
            while len(set(problem)) < n:
                problem = random_sub_problems()
        case _:
            raise ValueError("Invalid problem type")

    return problem

################################################################################
# Start here
################################################################################

def main():
    """
    Generate various mathematics problems.
    """
    how_many_add = 5
    how_many_sub = 5
    how_many_mult = 10
    how_many_div = 10
    print("Addition")
    for x, y, z in unique_problems(how_many_add, "+"):
        print("%s + %s = %d" % (str(x), str(y), z))
    print("\nSubtraction")
    for x, y, z in unique_problems(how_many_sub, "-"):
        print("%s - %s = %d" % (str(x), str(y), z))
    print("\nMultiplication")
    for x, y in unique_problems(how_many_mult, "x"):
        print(x, y)
    print("\nDivision")
    for x, y in unique_problems(how_many_div, "/"):
        print(x, y)

if __name__ == "__main__":
    main()
