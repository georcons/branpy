SYSTEM_PROMPT_ALGEBRA = r"""I am a teacher, and have some high-level olympiad math problems. I want to categorize the domain of these math problems. Here is a list of all possible 82 domains:

1. Mathematics -> Algebra -> Abstract Algebra -> Field Theory
2. Mathematics -> Algebra -> Abstract Algebra -> Function Theory -> Other
3. Mathematics -> Algebra -> Abstract Algebra -> Functional Equations -> Other
4. Mathematics -> Algebra -> Abstract Algebra -> Group Theory
5. Mathematics -> Algebra -> Abstract Algebra -> Other
6. Mathematics -> Algebra -> Abstract Algebra -> Ring Theory
7. Mathematics -> Algebra -> Algebra -> Algebraic Expressions
8. Mathematics -> Algebra -> Algebra -> Equations and Inequalities
9. Mathematics -> Algebra -> Algebra -> Polynomial Operations
10. Mathematics -> Algebra -> Algebra -> Sequences and Series
11. Mathematics -> Algebra -> Algebraic Expressions -> Other
12. Mathematics -> Algebra -> Differential Equations -> Ordinary Differential Equations (ODEs)
13. Mathematics -> Algebra -> Equations and Inequalities -> Other
14. Mathematics -> Algebra -> Exponents and Powers -> Other
15. Mathematics -> Algebra -> Functional Equations -> Other
16. Mathematics -> Algebra -> Functions and Sequences -> Other
17. Mathematics -> Algebra -> Intermediate Algebra -> Complex Numbers
18. Mathematics -> Algebra -> Intermediate Algebra -> Cubic Functions -> Other
19. Mathematics -> Algebra -> Intermediate Algebra -> Decimal Operations -> Other
20. Mathematics -> Algebra -> Intermediate Algebra -> Exponential Functions
21. Mathematics -> Algebra -> Intermediate Algebra -> Expressions and Inequalities -> Other
22. Mathematics -> Algebra -> Intermediate Algebra -> Factorials -> Other
23. Mathematics -> Algebra -> Intermediate Algebra -> Fraction Series -> Other
24. Mathematics -> Algebra -> Intermediate Algebra -> Functional Analysis
25. Mathematics -> Algebra -> Intermediate Algebra -> Inequalities
26. Mathematics -> Algebra -> Intermediate Algebra -> Logarithmic Functions
27. Mathematics -> Algebra -> Intermediate Algebra -> Modular Arithmetic -> Other
28. Mathematics -> Algebra -> Intermediate Algebra -> Other
29. Mathematics -> Algebra -> Intermediate Algebra -> Permutations and Combinations -> Other
30. Mathematics -> Algebra -> Intermediate Algebra -> Quadratic Functions
31. Mathematics -> Algebra -> Intermediate Algebra -> Radical Equations -> Other
32. Mathematics -> Algebra -> Intermediate Algebra -> Radical Expressions -> Other
33. Mathematics -> Algebra -> Intermediate Algebra -> Rational Functions -> Other
34. Mathematics -> Algebra -> Intermediate Algebra -> Recursive Sequences -> Other
35. Mathematics -> Algebra -> Intermediate Algebra -> Sequences -> Other
36. Mathematics -> Algebra -> Intermediate Algebra -> Systems of Equations -> Other
37. Mathematics -> Algebra -> Linear Algebra -> Determinants
38. Mathematics -> Algebra -> Linear Algebra -> Linear Equations -> Other
39. Mathematics -> Algebra -> Linear Algebra -> Linear Transformations
40. Mathematics -> Algebra -> Linear Algebra -> Matrices
41. Mathematics -> Algebra -> Linear Algebra -> Other
42. Mathematics -> Algebra -> Linear Algebra -> Vectors
43. Mathematics -> Algebra -> Number Theory -> Other
44. Mathematics -> Algebra -> Numbers -> Other
45. Mathematics -> Algebra -> Other
46. Mathematics -> Algebra -> Polynomials -> Other
47. Mathematics -> Algebra -> Prealgebra -> Absolute Values -> Other
48. Mathematics -> Algebra -> Prealgebra -> Arithmetic -> Other
49. Mathematics -> Algebra -> Prealgebra -> Arithmetic Sequences -> Other
50. Mathematics -> Algebra -> Prealgebra -> Averages -> Other
51. Mathematics -> Algebra -> Prealgebra -> Decimals
52. Mathematics -> Algebra -> Prealgebra -> Equations -> Other
53. Mathematics -> Algebra -> Prealgebra -> Exponents -> Other
54. Mathematics -> Algebra -> Prealgebra -> Factorials -> Other
55. Mathematics -> Algebra -> Prealgebra -> Fractions
56. Mathematics -> Algebra -> Prealgebra -> Integers
57. Mathematics -> Algebra -> Prealgebra -> Other
58. Mathematics -> Algebra -> Prealgebra -> Percentages -> Other
59. Mathematics -> Algebra -> Prealgebra -> Ratios -> Other
60. Mathematics -> Algebra -> Prealgebra -> Ratios and Proportions -> Other
61. Mathematics -> Algebra -> Prealgebra -> Sequences -> Other
62. Mathematics -> Algebra -> Prealgebra -> Simple Equations
63. Mathematics -> Algebra -> Sequences -> Other
64. Mathematics -> Algebra -> Sequences and Series -> Other
65. Mathematics -> Algebra -> Sequences and series -> Other
66. Mathematics -> Applied Mathematics -> Math Word Problems
67. Mathematics -> Applied Mathematics -> Math Word Problems -> Other
68. Mathematics -> Calculus -> Differential Calculus -> Applications of Derivatives
69. Mathematics -> Calculus -> Differential Calculus -> Derivatives
70. Mathematics -> Calculus -> Differential Calculus -> Other
71. Mathematics -> Calculus -> Differential Calculus -> Series -> Other
72. Mathematics -> Calculus -> Integral Calculus -> Applications of Integrals
73. Mathematics -> Calculus -> Integral Calculus -> Series -> Other
74. Mathematics -> Calculus -> Integral Calculus -> Techniques of Integration -> Multi-variable
75. Mathematics -> Calculus -> Integral Calculus -> Techniques of Integration -> Other
76. Mathematics -> Calculus -> Integral Calculus -> Techniques of Integration -> Single-variable
77. Mathematics -> Calculus -> Series -> Other
78. Mathematics -> Calculus -> Series and Sequences -> Other
79. Mathematics -> Calculus -> Techniques of Integration -> Other
80. Mathematics -> Precalculus -> Functions
81. Mathematics -> Precalculus -> Limits
82. Mathematics -> Precalculus -> Trigonometric Functions

PROBLEM: Trodgor the dragon is burning down a village consisting of 90 cottages. At time $t=0$ an angry peasant arises from each cottage, and every 8 minutes (480 seconds) thereafter another angry peasant spontaneously generates from each non-burned cottage. It takes Trodgor 5 seconds to either burn a peasant or to burn a cottage, but Trodgor cannot begin burning cottages until all the peasants around him have been burned. How many seconds does it take Trodgor to burn down the entire village?
DOMAIN: Mathematics -> Applied Mathematics -> Math Word Problems

PROBLEM: Consider pairs $(f,g)$ of functions from the set of nonnegative integers to itself such that
[*]$f(0) \geq f(1) \geq f(2) \geq \dots \geq f(300) \geq 0$
[*]$f(0)+f(1)+f(2)+\dots+f(300) \leq 300$
[*]for any 20 nonnegative integers $n_1, n_2, \dots, n_{20}$, not necessarily distinct, we have $$g(n_1+n_2+\dots+n_{20}) \leq f(n_1)+f(n_2)+\dots+f(n_{20}).$$
Determine the maximum possible value of $g(0)+g(1)+\dots+g(6000)$ over all such pairs of functions.
DOMAIN: Mathematics -> Algebra -> Intermediate Algebra -> Inequalities

PROBLEM: Does there exist positive reals $a_0, a_1,\ldots ,a_{19}$, such that the polynomial $P(x)=x^{20}+a_{19}x^{19}+\ldots +a_1x+a_0$ does not have any real roots, yet all polynomials formed from swapping any two coefficients $a_i,a_j$ has at least one real root?
DOMAIN: Mathematics -> Algebra -> Algebra -> Polynomial Operations

PROBLEM: Find the maximum possible number of three term arithmetic progressions in a monotone sequence of $n$ distinct reals.
DOMAIN: Mathematics -> Algebra -> Algebra -> Sequences and Series

PROBLEM: Find the largest real number $\lambda$ with the following property: for any positive real numbers $p,q,r,s$ there exists a complex number $z=a+bi$($a,b\in \mathbb{R})$  such that $$ |b|\ge \lambda |a| \quad \text{and} \quad (pz^3+2qz^2+2rz+s) \cdot (qz^3+2pz^2+2sz+r) =0.$$
DOMAIN: Mathematics -> Algebra -> Intermediate Algebra -> Complex Numbers

PROBLEM: Find the greatest constant $\lambda$ such that for any doubly stochastic matrix of order 100, we can pick $150$ entries such that if the other $9850$ entries were replaced by $0$, the sum of entries in each row and each column is at least $\lambda$.

Note: A doubly stochastic matrix of order $n$ is a $n\times n$ matrix, all entries are nonnegative reals, and the sum of entries in each row and column is equal to 1.
DOMAIN: Mathematics -> Algebra -> Linear Algebra -> Matrices

PROBLEM: Consider functions $f : [0, 1] \rightarrow \mathbb{R}$ which satisfy
  (i) for all in ,    (ii) ,    (iii) whenever , , and are all in .
Find, with proof, the smallest constant $c$ such that
$f(x) \le cx$
for every function $f$ satisfying (i)-(iii) and every $x$ in $[0, 1]$ .
DOMAIN: Mathematics -> Calculus -> Differential Calculus -> Applications of Derivatives

PROBLEM: As shown in the figure, a circle of radius 1 has two equal circles whose diameters cover a chosen diameter of the larger circle. In each of these smaller circles we similarly draw three equal circles, then four in each of those, and so on. Compute the area of the region enclosed by a positive even number of circles.
DOMAIN: Mathematics -> Calculus -> Integral Calculus -> Applications of Integrals

PROBLEM: Find all functions $f: \mathbb{Z}^+\rightarrow \mathbb{Z}^+$ such that for all positive integers $m,n$ with $m\ge n$, $$f(m\varphi(n^3)) = f(m)\cdot \varphi(n^3).$$ Here $\varphi(n)$ denotes the number of positive integers coprime to $n$ and not exceeding $n$.
DOMAIN: Mathematics -> Precalculus -> Functions

PROBLEM: Let $ n(\ge2) $ be a positive integer. Find the minimum $ m $, so that there exists $x_{ij}(1\le i ,j\le n)$ satisfying:
(1)For every $1\le i ,j\le n, x_{ij}=max\{x_{i1},x_{i2},...,x_{ij}\} $ or $ x_{ij}=max\{x_{1j},x_{2j},...,x_{ij}\}.$
(2)For every $1\le i \le n$, there are at most $m$ indices $k$ with $x_{ik}=max\{x_{i1},x_{i2},...,x_{ik}\}.$
(3)For every $1\le j \le n$, there are at most $m$ indices $k$ with $x_{kj}=max\{x_{1j},x_{2j},...,x_{kj}\}.$
DOMAIN: Mathematics -> Algebra -> Other"""

SYSTEM_PROMPT_GEOMETRY = r"""I am a teacher, and have some high-level olympiad math problems. I want to categorize the domain of these math problems. Here is a list of all possible 20 domains:

1. Mathematics -> Geometry -> Differential Geometry -> Curvature
2. Mathematics -> Geometry -> Plane Geometry -> Angles
3. Mathematics -> Geometry -> Plane Geometry -> Area
4. Mathematics -> Geometry -> Plane Geometry -> Areas -> Other
5. Mathematics -> Geometry -> Plane Geometry -> Circles
6. Mathematics -> Geometry -> Plane Geometry -> Circular and Triangular Relationships -> Other
7. Mathematics -> Geometry -> Plane Geometry -> Conic Sections -> Other
8. Mathematics -> Geometry -> Plane Geometry -> Coordinates -> Other
9. Mathematics -> Geometry -> Plane Geometry -> Curves -> Other
10. Mathematics -> Geometry -> Plane Geometry -> Distance -> Other
11. Mathematics -> Geometry -> Plane Geometry -> Distance Problems -> Other
12. Mathematics -> Geometry -> Plane Geometry -> Lines -> Other
13. Mathematics -> Geometry -> Plane Geometry -> Other
14. Mathematics -> Geometry -> Plane Geometry -> Polygons
15. Mathematics -> Geometry -> Plane Geometry -> Triangles -> Other
16. Mathematics -> Geometry -> Plane Geometry -> Triangulations
17. Mathematics -> Geometry -> Solid Geometry -> 3D Shapes
18. Mathematics -> Geometry -> Solid Geometry -> Other
19. Mathematics -> Geometry -> Solid Geometry -> Surface Area
20. Mathematics -> Geometry -> Solid Geometry -> Volume

PROBLEM: In an acute scalene triangle $ABC$, points $D,E,F$ lie on sides $BC, CA, AB$, respectively, such that $AD \perp BC, BE \perp CA, CF \perp AB$. Altitudes $AD, BE, CF$ meet at orthocenter $H$. Points $P$ and $Q$ lie on segment $EF$ such that $AP \perp EF$ and $HQ \perp EF$. Lines $DP$ and $QH$ intersect at point $R$. Compute $HQ/HR$.
DOMAIN: Mathematics -> Geometry -> Plane Geometry -> Triangulations

PROBLEM: There are $2022$ equally spaced points on a circular track $\gamma$ of circumference $2022$. The points are labeled $A_1, A_2, \ldots, A_{2022}$ in some order, each label used once. Initially, Bunbun the Bunny begins at $A_1$. She hops along $\gamma$ from $A_1$ to $A_2$, then from $A_2$ to $A_3$, until she reaches $A_{2022}$, after which she hops back to $A_1$. When hopping from $P$ to $Q$, she always hops along the shorter of the two arcs $\widehat{PQ}$ of $\gamma$; if $\overline{PQ}$ is a diameter of $\gamma$, she moves along either semicircle. Determine the maximal possible sum of the lengths of the $2022$ arcs which Bunbun traveled, over all possible labellings of the $2022$ points.
DOMAIN: Mathematics -> Geometry -> Plane Geometry -> Polygons

PROBLEM: For a pair $ A \equal{} (x_1, y_1)$ and $ B \equal{} (x_2, y_2)$ of points on the coordinate plane, let $ d(A,B) \equal{} |x_1 \minus{} x_2| \plus{} |y_1 \minus{} y_2|$. We call a pair $ (A,B)$ of (unordered) points [i]harmonic[/i] if $ 1 < d(A,B) \leq 2$. Determine the maximum number of harmonic pairs among 100 points in the plane.
DOMAIN: Mathematics -> Geometry -> Plane Geometry -> Other

PROBLEM: Draw a $2004 \times 2004$ array of points. What is the largest integer $n$ for which it is possible to draw a convex $n$-gon whose vertices are chosen from the points in the array?       
DOMAIN: Mathematics -> Geometry -> Plane Geometry -> Polygons

PROBLEM: Find out the maximum value of the numbers of edges of a solid regular octahedron that we can see from a point out of the regular octahedron.(We define we can see an edge $AB$ of the regular octahedron from point $P$ outside if and only if the intersection of non degenerate triangle $PAB$ and the solid regular octahedron is exactly edge $AB$.
DOMAIN: Mathematics -> Geometry -> Solid Geometry -> 3D Shapes

PROBLEM: Let $A,B,C,D$ denote four points in space such that at most one of the distances $AB,AC,AD,BC,BD,CD$ is greater than $1$ . Determine the maximum value of the sum of the six distances.    
DOMAIN: Mathematics -> Geometry -> Solid Geometry -> 3D Shapes

PROBLEM: $P$ , $A$ , $B$ , $C$ , and $D$ are five distinct points in space such that $\angle APB = \angle BPC = \angle CPD = \angle DPA = \theta$ , where $\theta$ is a given acute angle. Determine the greatest and least values of $\angle APC + \angle BPD$ .
DOMAIN: Mathematics -> Geometry -> Solid Geometry -> 3D Shapes

PROBLEM: Determine the greatest positive integer $ n$ such that in three-dimensional space, there exist n points $ P_{1},P_{2},\cdots,P_{n},$ among $ n$ points no three points are collinear, and for arbitary $ 1\leq i < j < k\leq n$, $ P_{i}P_{j}P_{k}$ isn't obtuse triangle.
DOMAIN: Mathematics -> Geometry -> Solid Geometry -> 3D Shapes

PROBLEM: Can an arc of a parabola inside a circle of radius 1 have a length greater than 4?
DOMAIN: Mathematics -> Geometry -> Differential Geometry -> Curvature

PROBLEM: Let $P_1,P_2,\dots,P_n$ be $n$ distinct points over a line in the plane ($n\geq2$). Consider all the circumferences with diameters $P_iP_j$ ($1\leq{i,j}\leq{n}$) and they are painted with $k$ given colors. Lets call this configuration a ($n,k$)-cloud. For each positive integer $k$, find all the positive integers $n$ such that every possible ($n,k$)-cloud has two mutually exterior tangent circumferences of the same color.
DOMAIN: Mathematics -> Geometry -> Differential Geometry -> Curvature"""

SYSTEM_PROMPT_NUMBER_THEORY = r"""I am a teacher, and have some high-level olympiad math problems. I want to categorize the domain of these math problems. Here is a list of all possible 22 domains:

1. Mathematics -> Number Theory -> Base Representations -> Other
2. Mathematics -> Number Theory -> Binary Representation -> Other
3. Mathematics -> Number Theory -> Congruences
4. Mathematics -> Number Theory -> Digit Sums -> Other
5. Mathematics -> Number Theory -> Digits and Sums -> Other
6. Mathematics -> Number Theory -> Diophantine Equations -> Other
7. Mathematics -> Number Theory -> Divisibility -> Other
8. Mathematics -> Number Theory -> Divisor Function -> Other
9. Mathematics -> Number Theory -> Divisor Functions -> Other
10. Mathematics -> Number Theory -> Divisors -> Other
11. Mathematics -> Number Theory -> Exponential Equations -> Other
12. Mathematics -> Number Theory -> Exponentiation -> Other
13. Mathematics -> Number Theory -> Factorization
14. Mathematics -> Number Theory -> Greatest Common Divisors (GCD)
15. Mathematics -> Number Theory -> Integer Solutions -> Other
16. Mathematics -> Number Theory -> Least Common Multiples (LCM)
17. Mathematics -> Number Theory -> Modular Arithmetic -> Other
18. Mathematics -> Number Theory -> Other
19. Mathematics -> Number Theory -> Prime Numbers
20. Mathematics -> Number Theory -> Quadratic Fields -> Other
21. Mathematics -> Number Theory -> Rational Approximations -> Other
22. Mathematics -> Number Theory -> Sequences -> Other

PROBLEM: Find all positive integers $a,n\ge1$ such that for all primes $p$ dividing $a^n-1$, there exists a positive integer $m<n$ such that $p\mid a^m-1$.
DOMAIN: Mathematics -> Number Theory -> Prime Numbers

PROBLEM: Let $n=p_1^{a_1}p_2^{a_2}\cdots p_t^{a_t}$ be the prime factorisation of $n$. Define $\omega(n)=t$ and $\Omega(n)=a_1+a_2+\ldots+a_t$. Prove or disprove:
For any fixed positive integer $k$ and positive reals $\alpha,\beta$, there exists a positive integer $n>1$ such that
i) $\frac{\omega(n+k)}{\omega(n)}>\alpha$
ii) $\frac{\Omega(n+k)}{\Omega(n)}<\beta$.
DOMAIN: Mathematics -> Number Theory -> Prime Numbers

PROBLEM: Find all positive integers $a,b,c$ and prime $p$ satisfying that
\[ 2^a p^b=(p+2)^c+1.\]
DOMAIN: Mathematics -> Number Theory -> Prime Numbers

PROBLEM: Let $n$ be a positive integer. Find, with proof, the least positive integer $d_{n}$ which cannot be expressed in the form \[\sum_{i=1}^{n}(-1)^{a_{i}}2^{b_{i}},\] where $a_{i}$ and $b_{i}$ are nonnegative integers for each $i.$
DOMAIN: Mathematics -> Number Theory -> Factorization

PROBLEM: Given distinct positive integer $ a_1,a_2,…,a_{2020} $. For $ n \ge 2021 $, $a_n$ is the smallest number different from $a_1,a_2,…,a_{n-1}$ which doesn't divide $a_{n-2020}...a_{n-2}a_{n-1}$. Proof that every number large enough appears in the sequence.
DOMAIN: Mathematics -> Number Theory -> Factorization

PROBLEM: Let $D_n$ be the set of divisors of $n$. Find all natural $n$ such that it is possible to split $D_n$ into two disjoint sets $A$ and $G$, both containing at least three elements each, such that the elements in $A$ form an arithmetic progression while the elements in $G$ form a geometric progression.
DOMAIN: Mathematics -> Number Theory -> Factorization

PROBLEM: Find all nonnegative integer solutions $(x,y,z,w)$ of the equation\[2^x\cdot3^y-5^z\cdot7^w=1.\]
DOMAIN: Mathematics -> Number Theory -> Congruences

PROBLEM: Determine whether or not there exist positive integers $ a$ and $ b$ such that $ a$ does not divide $ b^n \minus{} n$ for all positive integers $ n$.
DOMAIN: Mathematics -> Number Theory -> Congruences

PROBLEM: Find all positive integers $a$ such that there exists a set $X$ of $6$ integers satisfying the following conditions: for every $k=1,2,\ldots ,36$ there exist $x,y\in X$ such that $ax+y-k$ is divisible by $37$.
DOMAIN: Mathematics -> Number Theory -> Congruences

PROBLEM: Find in explicit form all ordered pairs of positive integers $(m, n)$ such that $mn-1$ divides $m^2 + n^2$.
DOMAIN: Mathematics -> Number Theory -> Divisibility -> Other"""

SYSTEM_PROMPT_COMBINATORICS = r"""I am a teacher, and have some high-level olympiad math problems. I want to categorize the domain of these math problems. Here is a list of all possible 14 domains:

1. Mathematics -> Applied Mathematics -> Other
2. Mathematics -> Applied Mathematics -> Probability -> Other
3. Mathematics -> Applied Mathematics -> Statistics -> Mathematical Statistics
4. Mathematics -> Applied Mathematics -> Statistics -> Other
5. Mathematics -> Applied Mathematics -> Statistics -> Probability -> Counting Methods -> Combinations
6. Mathematics -> Applied Mathematics -> Statistics -> Probability -> Counting Methods -> Other
7. Mathematics -> Applied Mathematics -> Statistics -> Probability -> Counting Methods -> Permutations
8. Mathematics -> Applied Mathematics -> Statistics -> Probability -> Other
9. Mathematics -> Discrete Mathematics -> Algorithms
10. Mathematics -> Discrete Mathematics -> Combinatorics
11. Mathematics -> Discrete Mathematics -> Game Theory
12. Mathematics -> Discrete Mathematics -> Graph Theory
13. Mathematics -> Discrete Mathematics -> Logic
14. Mathematics -> Discrete Mathematics -> Set Theory

PROBLEM: A tournament is a directed graph for which every (unordered) pair of vertices has a single directed edge from one vertex to the other.  Let us define a proper directed-edge-coloring to be an assignment of a color to every (directed) edge, so that for every pair of directed edges $\overrightarrow{uv}$ and $\overrightarrow{vw}$, those two edges are in different colors.  Note that it is permissible for $\overrightarrow{uv}$ and $\overrightarrow{uw}$ to be the same color.  The directed-edge-chromatic-number of a tournament is defined to be the minimum total number of colors that can be used in order to create a proper directed-edge-coloring.  For each $n$, determine the minimum directed-edge-chromatic-number over all tournaments on $n$ vertices.
DOMAIN: Mathematics -> Discrete Mathematics -> Graph Theory

PROBLEM: A table tennis club hosts a series of doubles matches following several rules:
(i)  each player belongs to two pairs at most;
(ii) every two distinct pairs play one game against each other at most;
(iii) players in the same pair do not play against each other when they pair with others respectively.
Every player plays a certain number of games in this series. All these distinct numbers make up a set called the “[i]set of games[/i]”. Consider a set $A=\{a_1,a_2,\ldots ,a_k\}$ of positive integers such that every element in $A$ is divisible by $6$. Determine the minimum number of players needed to participate in this series so that a schedule for which the corresponding [i]set of games [/i] is equal to set $A$ exists.
DOMAIN: Mathematics -> Discrete Mathematics -> Graph Theory

PROBLEM: Given positive integers $n$ and $k$, $n > k^2 >4.$ In a $n \times n$ grid, a $k$[i]-group[/i] is a set of $k$ unit squares lying in different rows and different columns. Determine the maximal possible $N$, such that one can choose $N$ unit squares in the grid and color them, with the following condition holds: in any $k$[i]-group[/i] from the colored $N$ unit squares, there are two squares with the same color, and there are also two squares with different colors.
DOMAIN: Mathematics -> Applied Mathematics -> Statistics -> Probability -> Counting Methods -> Combinations

PROBLEM: Three distinct vertices are chosen at random from the vertices of a given regular polygon of $(2n+1)$ sides. If all such choices are equally likely, what is the probability that the center of the given polygon lies in the interior of the triangle determined by the three chosen random points?
DOMAIN: Mathematics -> Applied Mathematics -> Statistics -> Probability -> Counting Methods -> Combinations

PROBLEM: A physicist encounters $2015$ atoms called usamons. Each usamon either has one electron or zero electrons, and the physicist can't tell the difference.  The physicist's only tool is a diode. The physicist may connect the diode from any usamon $A$ to any other usamon $B$. (This connection is directed.) When she does so, if usamon $A$ has an electron and usamon $B$ does not, then the electron jumps from $A$ to $B$. In any other case, nothing happens. In addition, the physicist cannot tell whether an electron jumps during any given step.  The physicist's goal is to isolate two usamons that she is  sure are currently in the same state. Is there any series of diode usage that makes this possible?
DOMAIN: Mathematics -> Discrete Mathematics -> Algorithms

PROBLEM: Find all functions $f\colon \mathbb{Z}^2 \to [0, 1]$ such that for any integers $x$ and $y$,
\[f(x, y) = \frac{f(x - 1, y) + f(x, y - 1)}{2}.\]
DOMAIN: Mathematics -> Discrete Mathematics -> Algorithms

PROBLEM: This question forms a three question multiple choice test. After each question, there are 4 choices, each preceded by a letter. Please write down your answer as the ordered triple (letter of the answer of Question \#1, letter of the answer of Question \#2, letter of the answer of Question \#3). If you find that all such ordered triples are logically impossible, then write 'no answer' as your answer. If you find more than one possible set of answers, then provide all ordered triples as your answer. When we refer to 'the correct answer to Question $X$ ' it is the actual answer, not the letter, to which we refer. When we refer to 'the letter of the correct answer to question $X$ ' it is the letter contained in parentheses that precedes the answer to which we refer. You are given the following condition: No two correct answers to questions on the test may have the same letter. Question 1. If a fourth question were added to this test, and if the letter of its correct answer were $(\mathrm{C})$, then: (A) This test would have no logically possible set of answers. (B) This test would have one logically possible set of answers. (C) This test would have more than one logically possible set of answers. (D) This test would have more than one logically possible set of answers. Question 2. If the answer to Question 2 were 'Letter (D)' and if Question 1 were not on this multiple-choice test (still keeping Questions 2 and 3 on the test), then the letter of the answer to Question 3 would be: (A) Letter (B) (B) Letter (C) (C) Letter $(\mathrm{D})$ (D) Letter $(\mathrm{A})$ Question 3. Let $P_{1}=1$. Let $P_{2}=3$. For all $i>2$, define $P_{i}=P_{i-1} P_{i-2}-P_{i-2}$. Which is a factor of $P_{2002}$ ? (A) 3 (B) 4 (C) 7 (D) 9
DOMAIN: Mathematics -> Discrete Mathematics -> Logic

PROBLEM: For any real number $\alpha$, define $$\operatorname{sign}(\alpha)= \begin{cases}+1 & \text { if } \alpha>0 \\ 0 & \text { if } \alpha=0 \\ -1 & \text { if } \alpha<0\end{cases}$$ How many triples $(x, y, z) \in \mathbb{R}^{3}$ satisfy the following system of equations $$\begin{aligned} & x=2018-2019 \cdot \operatorname{sign}(y+z) \\ & y=2018-2019 \cdot \operatorname{sign}(z+x) \\ & z=2018-2019 \cdot \operatorname{sign}(x+y) \end{aligned}$$
DOMAIN: Mathematics -> Discrete Mathematics -> Logic

PROBLEM: Let $X_{1}, \cdots, X_{n}$ be $n$ independent and identically distributed observations from the exponential distribution with density function $f(x)=\frac{1}{\beta} e^{-x / \beta}, x \geq 0$. b) Can you find an unbiased estimator $T$ that attains the lower bound in part a)? If yes, please construct one. If no, please show why such an estimator does not exist.
DOMAIN: Mathematics -> Applied Mathematics -> Statistics -> Mathematical Statistics

PROBLEM: Let $f:X\rightarrow X$, where $X=\{1,2,\ldots ,100\}$, be a function satisfying:
1) $f(x)\neq x$ for all $x=1,2,\ldots,100$;
2) for any subset $A$ of $X$ such that $|A|=40$, we have $A\cap f(A)\neq\emptyset$.
Find the minimum $k$ such that for any such function $f$, there exist a subset $B$ of $X$, where $|B|=k$, such that $B\cup f(B)=X$.
DOMAIN: Mathematics -> Discrete Mathematics -> Combinatorics"""


SYSTEM_PROMPT_COMPLETE = r"""I am a teacher, and have some high-level olympiad math problems. I want to categorize the domain of these math problems. Here is a list of all possible 138 domains:

1. Mathematics -> Algebra -> Abstract Algebra -> Field Theory
2. Mathematics -> Algebra -> Abstract Algebra -> Function Theory -> Other
3. Mathematics -> Algebra -> Abstract Algebra -> Functional Equations -> Other
4. Mathematics -> Algebra -> Abstract Algebra -> Group Theory
5. Mathematics -> Algebra -> Abstract Algebra -> Other
6. Mathematics -> Algebra -> Abstract Algebra -> Ring Theory
7. Mathematics -> Algebra -> Algebra -> Algebraic Expressions
8. Mathematics -> Algebra -> Algebra -> Equations and Inequalities
9. Mathematics -> Algebra -> Algebra -> Polynomial Operations
10. Mathematics -> Algebra -> Algebra -> Sequences and Series
11. Mathematics -> Algebra -> Algebraic Expressions -> Other
12. Mathematics -> Algebra -> Differential Equations -> Ordinary Differential Equations (ODEs)
13. Mathematics -> Algebra -> Equations and Inequalities -> Other
14. Mathematics -> Algebra -> Exponents and Powers -> Other
15. Mathematics -> Algebra -> Functional Equations -> Other
16. Mathematics -> Algebra -> Functions and Sequences -> Other
17. Mathematics -> Algebra -> Intermediate Algebra -> Complex Numbers
18. Mathematics -> Algebra -> Intermediate Algebra -> Cubic Functions -> Other
19. Mathematics -> Algebra -> Intermediate Algebra -> Decimal Operations -> Other
20. Mathematics -> Algebra -> Intermediate Algebra -> Exponential Functions
21. Mathematics -> Algebra -> Intermediate Algebra -> Expressions and Inequalities -> Other
22. Mathematics -> Algebra -> Intermediate Algebra -> Factorials -> Other
23. Mathematics -> Algebra -> Intermediate Algebra -> Fraction Series -> Other
24. Mathematics -> Algebra -> Intermediate Algebra -> Functional Analysis
25. Mathematics -> Algebra -> Intermediate Algebra -> Inequalities
26. Mathematics -> Algebra -> Intermediate Algebra -> Logarithmic Functions
27. Mathematics -> Algebra -> Intermediate Algebra -> Modular Arithmetic -> Other
28. Mathematics -> Algebra -> Intermediate Algebra -> Other
29. Mathematics -> Algebra -> Intermediate Algebra -> Permutations and Combinations -> Other
30. Mathematics -> Algebra -> Intermediate Algebra -> Quadratic Functions
31. Mathematics -> Algebra -> Intermediate Algebra -> Radical Equations -> Other
32. Mathematics -> Algebra -> Intermediate Algebra -> Radical Expressions -> Other
33. Mathematics -> Algebra -> Intermediate Algebra -> Rational Functions -> Other
34. Mathematics -> Algebra -> Intermediate Algebra -> Recursive Sequences -> Other
35. Mathematics -> Algebra -> Intermediate Algebra -> Sequences -> Other
36. Mathematics -> Algebra -> Intermediate Algebra -> Systems of Equations -> Other
37. Mathematics -> Algebra -> Linear Algebra -> Determinants
38. Mathematics -> Algebra -> Linear Algebra -> Linear Equations -> Other
39. Mathematics -> Algebra -> Linear Algebra -> Linear Transformations
40. Mathematics -> Algebra -> Linear Algebra -> Matrices
41. Mathematics -> Algebra -> Linear Algebra -> Other
42. Mathematics -> Algebra -> Linear Algebra -> Vectors
43. Mathematics -> Algebra -> Number Theory -> Other
44. Mathematics -> Algebra -> Numbers -> Other
45. Mathematics -> Algebra -> Other
46. Mathematics -> Algebra -> Polynomials -> Other
47. Mathematics -> Algebra -> Prealgebra -> Absolute Values -> Other
48. Mathematics -> Algebra -> Prealgebra -> Arithmetic -> Other
49. Mathematics -> Algebra -> Prealgebra -> Arithmetic Sequences -> Other
50. Mathematics -> Algebra -> Prealgebra -> Averages -> Other
51. Mathematics -> Algebra -> Prealgebra -> Decimals
52. Mathematics -> Algebra -> Prealgebra -> Equations -> Other
53. Mathematics -> Algebra -> Prealgebra -> Exponents -> Other
54. Mathematics -> Algebra -> Prealgebra -> Factorials -> Other
55. Mathematics -> Algebra -> Prealgebra -> Fractions
56. Mathematics -> Algebra -> Prealgebra -> Integers
57. Mathematics -> Algebra -> Prealgebra -> Other
58. Mathematics -> Algebra -> Prealgebra -> Percentages -> Other
59. Mathematics -> Algebra -> Prealgebra -> Ratios -> Other
60. Mathematics -> Algebra -> Prealgebra -> Ratios and Proportions -> Other
61. Mathematics -> Algebra -> Prealgebra -> Sequences -> Other
62. Mathematics -> Algebra -> Prealgebra -> Simple Equations
63. Mathematics -> Algebra -> Sequences -> Other
64. Mathematics -> Algebra -> Sequences and Series -> Other
65. Mathematics -> Algebra -> Sequences and series -> Other
66. Mathematics -> Applied Mathematics -> Math Word Problems
67. Mathematics -> Applied Mathematics -> Math Word Problems -> Other
68. Mathematics -> Calculus -> Differential Calculus -> Applications of Derivatives
69. Mathematics -> Calculus -> Differential Calculus -> Derivatives
70. Mathematics -> Calculus -> Differential Calculus -> Other
71. Mathematics -> Calculus -> Differential Calculus -> Series -> Other
72. Mathematics -> Calculus -> Integral Calculus -> Applications of Integrals
73. Mathematics -> Calculus -> Integral Calculus -> Series -> Other
74. Mathematics -> Calculus -> Integral Calculus -> Techniques of Integration -> Multi-variable
75. Mathematics -> Calculus -> Integral Calculus -> Techniques of Integration -> Other
76. Mathematics -> Calculus -> Integral Calculus -> Techniques of Integration -> Single-variable
77. Mathematics -> Calculus -> Series -> Other
78. Mathematics -> Calculus -> Series and Sequences -> Other
79. Mathematics -> Calculus -> Techniques of Integration -> Other
80. Mathematics -> Precalculus -> Functions
81. Mathematics -> Precalculus -> Limits
82. Mathematics -> Precalculus -> Trigonometric Functions
83. Mathematics -> Geometry -> Differential Geometry -> Curvature
84. Mathematics -> Geometry -> Plane Geometry -> Angles
85. Mathematics -> Geometry -> Plane Geometry -> Area
86. Mathematics -> Geometry -> Plane Geometry -> Areas -> Other
87. Mathematics -> Geometry -> Plane Geometry -> Circles
88. Mathematics -> Geometry -> Plane Geometry -> Circular and Triangular Relationships -> Other
89. Mathematics -> Geometry -> Plane Geometry -> Conic Sections -> Other
90. Mathematics -> Geometry -> Plane Geometry -> Coordinates -> Other
91. Mathematics -> Geometry -> Plane Geometry -> Curves -> Other
92. Mathematics -> Geometry -> Plane Geometry -> Distance -> Other
93. Mathematics -> Geometry -> Plane Geometry -> Distance Problems -> Other
94. Mathematics -> Geometry -> Plane Geometry -> Lines -> Other
95. Mathematics -> Geometry -> Plane Geometry -> Other
96. Mathematics -> Geometry -> Plane Geometry -> Polygons
97. Mathematics -> Geometry -> Plane Geometry -> Triangles -> Other
98. Mathematics -> Geometry -> Plane Geometry -> Triangulations
99. Mathematics -> Geometry -> Solid Geometry -> 3D Shapes
100. Mathematics -> Geometry -> Solid Geometry -> Other
101. Mathematics -> Geometry -> Solid Geometry -> Surface Area
102. Mathematics -> Geometry -> Solid Geometry -> Volume
103. Mathematics -> Applied Mathematics -> Other
104. Mathematics -> Applied Mathematics -> Probability -> Other
105. Mathematics -> Applied Mathematics -> Statistics -> Mathematical Statistics
106. Mathematics -> Applied Mathematics -> Statistics -> Other
107. Mathematics -> Applied Mathematics -> Statistics -> Probability -> Counting Methods -> Combinations
108. Mathematics -> Applied Mathematics -> Statistics -> Probability -> Counting Methods -> Other
109. Mathematics -> Applied Mathematics -> Statistics -> Probability -> Counting Methods -> Permutations
110. Mathematics -> Applied Mathematics -> Statistics -> Probability -> Other
111. Mathematics -> Discrete Mathematics -> Algorithms
112. Mathematics -> Discrete Mathematics -> Combinatorics
113. Mathematics -> Discrete Mathematics -> Game Theory
114. Mathematics -> Discrete Mathematics -> Graph Theory
115. Mathematics -> Discrete Mathematics -> Logic
116. Mathematics -> Discrete Mathematics -> Set Theory
117. Mathematics -> Number Theory -> Base Representations -> Other
118. Mathematics -> Number Theory -> Binary Representation -> Other
119. Mathematics -> Number Theory -> Congruences
120. Mathematics -> Number Theory -> Digit Sums -> Other
121. Mathematics -> Number Theory -> Digits and Sums -> Other
122. Mathematics -> Number Theory -> Diophantine Equations -> Other
123. Mathematics -> Number Theory -> Divisibility -> Other
124. Mathematics -> Number Theory -> Divisor Function -> Other
125. Mathematics -> Number Theory -> Divisor Functions -> Other
126. Mathematics -> Number Theory -> Divisors -> Other
127. Mathematics -> Number Theory -> Exponential Equations -> Other
128. Mathematics -> Number Theory -> Exponentiation -> Other
129. Mathematics -> Number Theory -> Factorization
130. Mathematics -> Number Theory -> Greatest Common Divisors (GCD)
131. Mathematics -> Number Theory -> Integer Solutions -> Other
132. Mathematics -> Number Theory -> Least Common Multiples (LCM)
133. Mathematics -> Number Theory -> Modular Arithmetic -> Other
134. Mathematics -> Number Theory -> Other
135. Mathematics -> Number Theory -> Prime Numbers
136. Mathematics -> Number Theory -> Quadratic Fields -> Other
137. Mathematics -> Number Theory -> Rational Approximations -> Other
138. Mathematics -> Number Theory -> Sequences -> Other

PROBLEM: Given positive integers $n$ and $k$, $n > k^2 >4.$ In a $n \times n$ grid, a $k$[i]-group[/i] is a set of $k$ unit squares lying in different rows and different columns. Determine the maximal possible $N$, such that one can choose $N$ unit squares in the grid and color them, with the following condition holds: in any $k$[i]-group[/i] from the colored $N$ unit squares, there are two squares with the same color, and there are also two squares with different colors.
DOMAIN: Mathematics -> Applied Mathematics -> Statistics -> Probability -> Counting Methods -> Combinations

PROBLEM: A tournament is a directed graph for which every (unordered) pair of vertices has a single directed edge from one vertex to the other.  Let us define a proper directed-edge-coloring to be an assignment of a color to every (directed) edge, so that for every pair of directed edges $\overrightarrow{uv}$ and $\overrightarrow{vw}$, those two edges are in different colors.  Note that it is permissible for $\overrightarrow{uv}$ and $\overrightarrow{uw}$ to be the same color.  The directed-edge-chromatic-number of a tournament is defined to be the minimum total number of colors that can be used in order to create a proper directed-edge-coloring.  For each $n$, determine the minimum directed-edge-chromatic-number over all tournaments on $n$ vertices.
DOMAIN: Mathematics -> Discrete Mathematics -> Graph Theory

PROBLEM: Let $f:X\rightarrow X$, where $X=\{1,2,\ldots ,100\}$, be a function satisfying:
1) $f(x)\neq x$ for all $x=1,2,\ldots,100$;
2) for any subset $A$ of $X$ such that $|A|=40$, we have $A\cap f(A)\neq\emptyset$.
Find the minimum $k$ such that for any such function $f$, there exist a subset $B$ of $X$, where $|B|=k$, such that $B\cup f(B)=X$.
DOMAIN: Mathematics -> Discrete Mathematics -> Combinatorics

PROBLEM: Trodgor the dragon is burning down a village consisting of 90 cottages. At time $t=0$ an angry peasant arises from each cottage, and every 8 minutes (480 seconds) thereafter another angry peasant spontaneously generates from each non-burned cottage. It takes Trodgor 5 seconds to either burn a peasant or to burn a cottage, but Trodgor cannot begin burning cottages until all the peasants around him have been burned. How many seconds does it take Trodgor to burn down the entire village?
DOMAIN: Mathematics -> Applied Mathematics -> Math Word Problems

PROBLEM: Consider pairs $(f,g)$ of functions from the set of nonnegative integers to itself such that
[*]$f(0) \geq f(1) \geq f(2) \geq \dots \geq f(300) \geq 0$
[*]$f(0)+f(1)+f(2)+\dots+f(300) \leq 300$
[*]for any 20 nonnegative integers $n_1, n_2, \dots, n_{20}$, not necessarily distinct, we have $$g(n_1+n_2+\dots+n_{20}) \leq f(n_1)+f(n_2)+\dots+f(n_{20}).$$
Determine the maximum possible value of $g(0)+g(1)+\dots+g(6000)$ over all such pairs of functions.
DOMAIN: Mathematics -> Algebra -> Intermediate Algebra -> Inequalities

PROBLEM: Does there exist positive reals $a_0, a_1,\ldots ,a_{19}$, such that the polynomial $P(x)=x^{20}+a_{19}x^{19}+\ldots +a_1x+a_0$ does not have any real roots, yet all polynomials formed from swapping any two coefficients $a_i,a_j$ has at least one real root?
DOMAIN: Mathematics -> Algebra -> Algebra -> Polynomial Operations

PROBLEM: Find all positive integers $a,n\ge1$ such that for all primes $p$ dividing $a^n-1$, there exists a positive integer $m<n$ such that $p\mid a^m-1$.
DOMAIN: Mathematics -> Number Theory -> Prime Numbers

PROBLEM: Let $n$ be a positive integer. Find, with proof, the least positive integer $d_{n}$ which cannot be expressed in the form \[\sum_{i=1}^{n}(-1)^{a_{i}}2^{b_{i}},\]
where $a_{i}$ and $b_{i}$ are nonnegative integers for each $i.$
DOMAIN: Mathematics -> Number Theory -> Factorization

PROBLEM: Find all nonnegative integer solutions $(x,y,z,w)$ of the equation\[2^x\cdot3^y-5^z\cdot7^w=1.\]
DOMAIN: Mathematics -> Number Theory -> Congruences

PROBLEM: In an acute scalene triangle $ABC$, points $D,E,F$ lie on sides $BC, CA, AB$, respectively, such that $AD \perp BC, BE \perp CA, CF \perp AB$. Altitudes $AD, BE, CF$ meet at orthocenter $H$. Points $P$ and $Q$ lie on segment $EF$ such that $AP \perp EF$ and $HQ \perp EF$. Lines $DP$ and $QH$ intersect at point $R$. Compute $HQ/HR$.
DOMAIN: Mathematics -> Geometry -> Plane Geometry -> Triangulations

PROBLEM: Find out the maximum value of the numbers of edges of a solid regular octahedron that we can see from a point out of the regular octahedron.(We define we can see an edge $AB$ of the regular octahedron from point $P$ outside if and only if the intersection of non degenerate triangle $PAB$ and the solid regular octahedron is exactly edge $AB$.
DOMAIN: Mathematics -> Geometry -> Solid Geometry -> 3D Shapes"""

def FILTER_SYSTEM_PROMPT(filter):
    if filter == "Algebra": return SYSTEM_PROMPT_ALGEBRA
    if filter == "Geometry": return SYSTEM_PROMPT_GEOMETRY
    if filter == "Number Theory": return SYSTEM_PROMPT_NUMBER_THEORY
    if filter == "Combinatorics": return SYSTEM_PROMPT_COMBINATORICS
    return SYSTEM_PROMPT_COMPLETE

def GENERATE_USER_PROMPT(statement):
    return "Give me the domain of the following problem: " + statement + ". Prompt only the domain without any other words."
