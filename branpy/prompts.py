SYSTEM_PROMPT_COMPLETE_BRANCH_BRANCHES = """Mathematics -> Algebra -> Abstract Algebra -> Field Theory
Mathematics -> Algebra -> Abstract Algebra -> Function Theory -> Other
Mathematics -> Algebra -> Abstract Algebra -> Functional Equations -> Other
Mathematics -> Algebra -> Abstract Algebra -> Group Theory
Mathematics -> Algebra -> Abstract Algebra -> Other
Mathematics -> Algebra -> Abstract Algebra -> Ring Theory
Mathematics -> Algebra -> Algebra -> Algebraic Expressions
Mathematics -> Algebra -> Algebra -> Equations and Inequalities
Mathematics -> Algebra -> Algebra -> Polynomial Operations
Mathematics -> Algebra -> Algebra -> Sequences and Series
Mathematics -> Algebra -> Algebraic Expressions -> Other
Mathematics -> Algebra -> Differential Equations -> Ordinary Differential Equations (ODEs)
Mathematics -> Algebra -> Equations and Inequalities -> Other
Mathematics -> Algebra -> Exponents and Powers -> Other
Mathematics -> Algebra -> Functional Equations -> Other
Mathematics -> Algebra -> Functions and Sequences -> Other
Mathematics -> Algebra -> Intermediate Algebra -> Complex Numbers
Mathematics -> Algebra -> Intermediate Algebra -> Cubic Functions -> Other
Mathematics -> Algebra -> Intermediate Algebra -> Decimal Operations -> Other
Mathematics -> Algebra -> Intermediate Algebra -> Exponential Functions
Mathematics -> Algebra -> Intermediate Algebra -> Expressions and Inequalities -> Other
Mathematics -> Algebra -> Intermediate Algebra -> Factorials -> Other
Mathematics -> Algebra -> Intermediate Algebra -> Fraction Series -> Other
Mathematics -> Algebra -> Intermediate Algebra -> Functional Analysis
Mathematics -> Algebra -> Intermediate Algebra -> Inequalities
Mathematics -> Algebra -> Intermediate Algebra -> Logarithmic Functions
Mathematics -> Algebra -> Intermediate Algebra -> Modular Arithmetic -> Other
Mathematics -> Algebra -> Intermediate Algebra -> Other
Mathematics -> Algebra -> Intermediate Algebra -> Permutations and Combinations -> Other
Mathematics -> Algebra -> Intermediate Algebra -> Quadratic Functions
Mathematics -> Algebra -> Intermediate Algebra -> Radical Equations -> Other
Mathematics -> Algebra -> Intermediate Algebra -> Radical Expressions -> Other
Mathematics -> Algebra -> Intermediate Algebra -> Rational Functions -> Other
Mathematics -> Algebra -> Intermediate Algebra -> Recursive Sequences -> Other
Mathematics -> Algebra -> Intermediate Algebra -> Sequences -> Other
Mathematics -> Algebra -> Intermediate Algebra -> Systems of Equations -> Other
Mathematics -> Algebra -> Linear Algebra -> Determinants
Mathematics -> Algebra -> Linear Algebra -> Linear Equations -> Other
Mathematics -> Algebra -> Linear Algebra -> Linear Transformations
Mathematics -> Algebra -> Linear Algebra -> Matrices
Mathematics -> Algebra -> Linear Algebra -> Other
Mathematics -> Algebra -> Linear Algebra -> Vectors
Mathematics -> Algebra -> Number Theory -> Other
Mathematics -> Algebra -> Numbers -> Other
Mathematics -> Algebra -> Other
Mathematics -> Algebra -> Polynomials -> Other
Mathematics -> Algebra -> Prealgebra -> Absolute Values -> Other
Mathematics -> Algebra -> Prealgebra -> Arithmetic -> Other
Mathematics -> Algebra -> Prealgebra -> Arithmetic Sequences -> Other
Mathematics -> Algebra -> Prealgebra -> Averages -> Other
Mathematics -> Algebra -> Prealgebra -> Decimals
Mathematics -> Algebra -> Prealgebra -> Equations -> Other
Mathematics -> Algebra -> Prealgebra -> Exponents -> Other
Mathematics -> Algebra -> Prealgebra -> Factorials -> Other
Mathematics -> Algebra -> Prealgebra -> Fractions
Mathematics -> Algebra -> Prealgebra -> Integers
Mathematics -> Algebra -> Prealgebra -> Other
Mathematics -> Algebra -> Prealgebra -> Percentages -> Other
Mathematics -> Algebra -> Prealgebra -> Ratios -> Other
Mathematics -> Algebra -> Prealgebra -> Ratios and Proportions -> Other
Mathematics -> Algebra -> Prealgebra -> Sequences -> Other
Mathematics -> Algebra -> Prealgebra -> Simple Equations
Mathematics -> Algebra -> Sequences -> Other
Mathematics -> Algebra -> Sequences and Series -> Other
Mathematics -> Algebra -> Sequences and series -> Other
Mathematics -> Applied Mathematics -> Math Word Problems
Mathematics -> Applied Mathematics -> Other
Mathematics -> Applied Mathematics -> Probability -> Other
Mathematics -> Applied Mathematics -> Statistics -> Mathematical Statistics
Mathematics -> Applied Mathematics -> Statistics -> Other
Mathematics -> Applied Mathematics -> Statistics -> Probability -> Counting Methods -> Combinations
Mathematics -> Applied Mathematics -> Statistics -> Probability -> Counting Methods -> Other
Mathematics -> Applied Mathematics -> Statistics -> Probability -> Counting Methods -> Permutations
Mathematics -> Applied Mathematics -> Statistics -> Probability -> Other
Mathematics -> Applied Mathematics -> Math Word Problems -> Other
Mathematics -> Calculus -> Differential Calculus -> Applications of Derivatives
Mathematics -> Calculus -> Differential Calculus -> Derivatives
Mathematics -> Calculus -> Differential Calculus -> Other
Mathematics -> Calculus -> Differential Calculus -> Series -> Other
Mathematics -> Calculus -> Integral Calculus -> Applications of Integrals
Mathematics -> Calculus -> Integral Calculus -> Series -> Other
Mathematics -> Calculus -> Integral Calculus -> Techniques of Integration -> Multi-variable
Mathematics -> Calculus -> Integral Calculus -> Techniques of Integration -> Other
Mathematics -> Calculus -> Integral Calculus -> Techniques of Integration -> Single-variable
Mathematics -> Calculus -> Series -> Other
Mathematics -> Calculus -> Series and Sequences -> Other
Mathematics -> Calculus -> Techniques of Integration -> Other
Mathematics -> Discrete Mathematics -> Algorithms
Mathematics -> Discrete Mathematics -> Combinatorics
Mathematics -> Discrete Mathematics -> Game Theory
Mathematics -> Discrete Mathematics -> Graph Theory
Mathematics -> Discrete Mathematics -> Logic
Mathematics -> Discrete Mathematics -> Set Theory
Mathematics -> Geometry -> Differential Geometry -> Curvature
Mathematics -> Geometry -> Plane Geometry -> Angles
Mathematics -> Geometry -> Plane Geometry -> Area
Mathematics -> Geometry -> Plane Geometry -> Areas -> Other
Mathematics -> Geometry -> Plane Geometry -> Circles
Mathematics -> Geometry -> Plane Geometry -> Circular and Triangular Relationships -> Other
Mathematics -> Geometry -> Plane Geometry -> Conic Sections -> Other
Mathematics -> Geometry -> Plane Geometry -> Coordinates -> Other
Mathematics -> Geometry -> Plane Geometry -> Curves -> Other
Mathematics -> Geometry -> Plane Geometry -> Distance -> Other
Mathematics -> Geometry -> Plane Geometry -> Distance Problems -> Other
Mathematics -> Geometry -> Plane Geometry -> Lines -> Other
Mathematics -> Geometry -> Plane Geometry -> Other
Mathematics -> Geometry -> Plane Geometry -> Polygons
Mathematics -> Geometry -> Plane Geometry -> Triangles -> Other
Mathematics -> Geometry -> Plane Geometry -> Triangulations
Mathematics -> Geometry -> Solid Geometry -> 3D Shapes
Mathematics -> Geometry -> Solid Geometry -> Other
Mathematics -> Geometry -> Solid Geometry -> Surface Area
Mathematics -> Geometry -> Solid Geometry -> Volume
Mathematics -> Number Theory -> Base Representations -> Other
Mathematics -> Number Theory -> Binary Representation -> Other
Mathematics -> Number Theory -> Congruences
Mathematics -> Number Theory -> Digit Sums -> Other
Mathematics -> Number Theory -> Digits and Sums -> Other
Mathematics -> Number Theory -> Diophantine Equations -> Other
Mathematics -> Number Theory -> Divisibility -> Other
Mathematics -> Number Theory -> Divisor Function -> Other
Mathematics -> Number Theory -> Divisor Functions -> Other
Mathematics -> Number Theory -> Divisors -> Other
Mathematics -> Number Theory -> Exponential Equations -> Other
Mathematics -> Number Theory -> Exponentiation -> Other
Mathematics -> Number Theory -> Factorization
Mathematics -> Number Theory -> Greatest Common Divisors (GCD)
Mathematics -> Number Theory -> Integer Solutions -> Other
Mathematics -> Number Theory -> Least Common Multiples (LCM)
Mathematics -> Number Theory -> Modular Arithmetic -> Other
Mathematics -> Number Theory -> Other
Mathematics -> Number Theory -> Prime Numbers
Mathematics -> Number Theory -> Quadratic Fields -> Other
Mathematics -> Number Theory -> Rational Approximations -> Other
Mathematics -> Number Theory -> Sequences -> Other
Mathematics -> Other
Mathematics -> Precalculus -> Functions
Mathematics -> Precalculus -> Limits
Mathematics -> Precalculus -> Trigonometric Functions"""

SYSTEM_PROMPT_COMPLETE_BRANCH_EXAMPLES = """
Here are a few references to the domain.

PROBLEM: A fair coin is flipped eight times in a row. Let $p$ be the probability that there is exactly one pair of consecutive flips that are both heads and exactly one pair of consecutive flips that are both tails. If $p=\\frac{a}{b}$, where $a, b$ are relatively prime positive integers, compute $100a+b$.
DOMAIN: Mathematics -> Applied Mathematics -> Statistics -> Probability -> Counting Methods -> Combinations

PROBLEM: Determine all functions $f:(0,\\infty)\\to\\mathbb{R}$ satisfying $$\\left(x+\\frac{1}{x}\\right)f(y)=f(xy)+f\\left(\\frac{y}{x}\\right)$$ for all $x,y>0$.
DOMAIN: Mathematics -> Algebra -> Abstract Algebra -> Other

PROBLEM: Let $n$ be a positive integer. A child builds a wall along a line with $n$ identical cubes. He lays the first cube on the line and at each subsequent step, he lays the next cube either on the ground or on the top of another cube, so that it has a common face with the previous one. How many such distinct walls exist?
DOMAIN: Mathematics -> Discrete Mathematics -> Combinatorics

PROBLEM: Call an integer $n>1$ radical if $2^{n}-1$ is prime. What is the 20th smallest radical number? If $A$ is your answer, and $S$ is the correct answer, you will get $\\max \\left(25\\left(1-\\frac{|A-S|}{S}\\right), 0\\right)$ points, rounded to the nearest integer.
DOMAIN: Mathematics -> Number Theory -> Prime Numbers

PROBLEM: If \\( 50\\% \\) of \\( N \\) is 16, what is \\( 75\\% \\) of \\( N \\)?
DOMAIN: Mathematics -> Algebra -> Prealgebra -> Fractions

PROBLEM: Determine the remainder when $$\\sum_{i=0}^{2015}\\left\\lfloor\\frac{2^{i}}{25}\\right\\rfloor$$ is divided by 100, where $\\lfloor x\\rfloor$ denotes the largest integer not greater than $x$.
DOMAIN: Mathematics -> Number Theory -> Congruences

PROBLEM: Determine all real numbers $a > 0$ for which there exists a nonnegative continuous function $f(x)$ defined on $[0,a]$ with the property that the region \\[ R = \\{ (x,y) ; 0 \\le x \\le a, 0 \\le y \\le f(x) \\} \\] has perimeter $k$ units and area $k$ square units for some real number $k$.
DOMAIN: Mathematics -> Geometry -> Plane Geometry -> Area

PROBLEM: Find the smallest positive integer $n$ such that there exists a complex number $z$, with positive real and imaginary part, satisfying $z^{n}=(\\bar{z})^{n}$.
DOMAIN: Mathematics -> Algebra -> Intermediate Algebra -> Complex Numbers

PROBLEM: Find all differentiable functions \\(f:(0, \\infty) \\rightarrow \\mathbb{R}\\) such that \\(f(b)-f(a)=(b-a) f^{\\prime}(\\sqrt{a b}) \\quad \\text { for all } \\quad a, b>0\\).
DOMAIN: Mathematics -> Calculus -> Differential Calculus -> Derivatives

PROBLEM: For how many integers $a(1 \\leq a \\leq 200)$ is the number $a^{a}$ a square?
DOMAIN: Mathematics -> Number Theory -> Factorization

PROBLEM: In a group of 50 children, each of the children in the group have all of their siblings in the group. Each child with no older siblings announces how many siblings they have; however, each child with an older sibling is too embarrassed, and says they have 0 siblings. If the average of the numbers everyone says is $\\frac{12}{25}$, compute the number of different sets of siblings represented in the group.
DOMAIN: Mathematics -> Algebra -> Algebra -> Equations and Inequalities

PROBLEM: A permutation of a finite set is a one-to-one function from the set to itself; for instance, one permutation of $\\{1,2,3,4\\}$ is the function $\\pi$ defined such that $\\pi(1)=1, \\pi(2)=3$, $\\pi(3)=4$, and $\\pi(4)=2$. How many permutations $\\pi$ of the set $\\{1,2, \\ldots, 10\\}$ have the property that $\\pi(i) \\neq i$ for each $i=1,2, \\ldots, 10$, but $\\pi(\\pi(i))=i$ for each $i$?
DOMAIN: Mathematics -> Discrete Mathematics -> Combinatorics

PROBLEM: A sphere is centered at a point with integer coordinates and passes through the three points $(2,0,0)$, $(0,4,0),(0,0,6)$, but not the origin $(0,0,0)$. If $r$ is the smallest possible radius of the sphere, compute $r^{2}$.
DOMAIN: Mathematics -> Geometry -> Solid Geometry -> 3D Shapes

PROBLEM: Snacks are purchased for 17 soccer players. Juice boxes come in packs of 3 and cost $2.00 per pack. Apples come in bags of 5 and cost $4.00 per bag. What is the minimum amount of money that Danny spends to ensure every player gets a juice box and an apple?
DOMAIN: Mathematics -> Applied Mathematics -> Math Word Problems
"""

def GENERATE_USER_PROMPT(statement):
    return "Give me the domain of the following problem: " + statement + ". Prompt only the domain without any other words."

def FILTER_SYSTEM_PROMPT(filter):
    problems, count = _fetch_problems(filter)
    
    output = "I am a teacher, and have some high-level olympiad math problems. I want to categorize the domain of these math problems. Here is a list of all possible " + str(count) + " domains:\n"

    output += problems

    output += SYSTEM_PROMPT_COMPLETE_BRANCH_EXAMPLES

    return output


def _fetch_problems(filter):
    lines = SYSTEM_PROMPT_COMPLETE_BRANCH_BRANCHES.split('\n')
    newlines = []

    if filter == "none":
        newlines = lines
    
    else:
        for line in lines:
            if line.startswith(filter):
                newlines.append(line)
    
    output = ""
    index = 1

    for line in newlines:
        output += str(index) + ". " + line + "\n"
        index += 1

    length = len(newlines)

    return output, length 