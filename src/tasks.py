def map_main_task(label):
    hir = (label + " -> END").split(" -> ")
    if (hir[1] == "Applied Mathematics"):
        if (hir[2] == "Math Word Problems"): 
            return "Algebra"
        elif (hir[2] == "Statistics"):
            if (hir[3] == "Probability"):
                return "Combinatorics"
            else:
                return "Combinatorics"
        else:
            return "Combinatorics"

    elif (hir[1] == "Algebra"):
        if (hir[2] == "Prealgebra"):
            return "Algebra"
        elif (hir[2] == "Algebra"):
            if (hir[3] == "Equations and Inequalities"): 
                return "Algebra"
            elif (hir[3] == "Algebraic Expressions"): 
                return "Algebra"
            elif (hir[3] == "Polynomial Operations"):
                return "Algebra"
            else:
                return "Algebra"
        elif (hir[2] == "Intermediate Algebra"):
            if (hir[3] == "Quadratic Functions"):
                return "Algebra"
            elif (hir[3] == "Exponential Functions"):
                return "Algebra"
            elif (hir[3] == "Logarithmic Functions"):
                return "Algebra"
            elif (hir[3] == "Complex Numbers"):
                return "Algebra"
            elif (hir[3] == "Inequalities"):
                return "Algebra"
            else:
                return "Algebra"

        elif (hir[2] == "Linear Algebra"):
                return "Algebra"

        elif (hir[2] == "Abstract Algebra"):
            return "Algebra"
        
        else:
            return "Algebra"

    elif (hir[1] == "Discrete Mathematics"):
        if (hir[2] == "Graph Theory"):
            return "Combinatorics"
        elif (hir[2] == "Logic"):
            return "Combinatorics"
        elif (hir[2] == "Algorithms"):
            return "Combinatorics"
        else:
            return "Combinatorics"
        
    elif (hir[1] == "Geometry"):
        if (hir[2] == "Plane Geometry"):
            return "Geometry"
        elif (hir[2] == "Solid Geometry"):
            return "Geometry"
        else:
            return "Geometry"
        
    elif (hir[1] == "Number Theory"):
        if (hir[2] == "Prime Numbers"):
            return "Number Theory"
        elif (hir[2] == "Factorization"):
            return "Number Theory"
        elif (hir[2] == "Congruences"):
            return "Number Theory"
        else:
            return "Number Theory"
        
    elif (hir[1] == "Precalculus"):
        return "Algebra"

    elif (hir[1] == "Calculus"):
        if (hir[2] == "Differential Calculus"):
            return "Algebra"
        elif (hir[2] == "Integral Calculus"):
            return "Algebra"
        else:
            return "Algebra"
        
    elif (hir[1] == "Differential Equations"):
        return "Algebra"

    else:
        return "Others"

    return "Others"

def map_reduced_to_main(label):
    blocks = label.split(" -> ")
    if len(blocks) < 2:
        return "Others"
    else:
        return blocks[1]

def map_reduced_task(label):
    hir = (label + " -> END").split(" -> ")
    if (hir[1] == "Applied Mathematics"):
        if (hir[2] == "Math Word Problems"): 
            return "Mathematics -> Algebra -> Math Word Problems"
        elif (hir[2] == "Statistics"):
            if (hir[3] == "Probability"):
                return "Mathematics -> Combinatorics -> Probability"
            else:
                return "Mathematics -> Combinatorics -> Statistics"
        else:
            return "Mathematics -> Combinatorics -> Others"

    elif (hir[1] == "Algebra"):
        if (hir[2] == "Prealgebra"):
            return "Mathematics -> Algebra -> Expressions"
        elif (hir[2] == "Algebra"):
            if (hir[3] == "Equations and Inequalities"): 
                return "Mathematics -> Algebra -> Expressions"
            elif (hir[3] == "Algebraic Expressions"): 
                return "Mathematics -> Algebra -> Expressions"
            elif (hir[3] == "Polynomial Operations"):
                return "Mathematics -> Algebra -> Polynomials"
            else:
                return "Mathematics -> Algebra -> Sequences and Series"
        elif (hir[2] == "Intermediate Algebra"):
            if (hir[3] == "Quadratic Functions"):
                return "Mathematics -> Algebra -> Expressions"
            elif (hir[3] == "Exponential Functions"):
                return "Mathematics -> Algebra -> Expressions"
            elif (hir[3] == "Logarithmic Functions"):
                return "Mathematics -> Algebra -> Expressions"
            elif (hir[3] == "Complex Numbers"):
                return "Mathematics -> Algebra -> Complex Numbers"
            elif (hir[3] == "Inequalities"):
                return "Mathematics -> Algebra -> Expressions"
            else:
                return "Mathematics -> Algebra -> Others"

        elif (hir[2] == "Linear Algebra"):
                return "Mathematics -> Algebra -> Linear Algebra"

        elif (hir[2] == "Abstract Algebra"):
            return "Mathematics -> Algebra -> Others"
        
        else:
            return "Mathematics -> Algebra -> Others"

    elif (hir[1] == "Discrete Mathematics"):
        if (hir[2] == "Graph Theory"):
            return "Mathematics -> Combinatorics -> Graph Theory"
        elif (hir[2] == "Logic"):
            return "Mathematics -> Combinatorics -> Logic"
        elif (hir[2] == "Algorithms"):
            return "Mathematics -> Combinatorics -> Algorithms"
        else:
            return "Mathematics -> Combinatorics -> Others"
        
    elif (hir[1] == "Geometry"):
        if (hir[2] == "Plane Geometry"):
            return "Mathematics -> Geometry -> Plane Geometry"
        elif (hir[2] == "Solid Geometry"):
            return "Mathematics -> Geometry -> Stereometry"
        else:
            return "Mathematics -> Geometry -> Others"
        
    elif (hir[1] == "Number Theory"):
        if (hir[2] == "Prime Numbers"):
            return "Mathematics -> Number Theory -> Prime Numbers"
        elif (hir[2] == "Factorization"):
            return "Mathematics -> Number Theory -> Factorization"
        elif (hir[2] == "Congruences"):
            return "Mathematics -> Number Theory -> Congruences"
        else:
            return "Mathematics -> Number Theory -> Others"
        
    elif (hir[1] == "Precalculus"):
        return "Mathematics -> Algebra -> Other Calculus"

    elif (hir[1] == "Calculus"):
        if (hir[2] == "Differential Calculus"):
            return "Mathematics -> Algebra -> Differential Calculus"
        elif (hir[2] == "Integral Calculus"):
            return "Mathematics -> Algebra -> Integral Calculus"
        else:
            return "Mathematics -> Algebra -> Other Calculus"
        
    elif (hir[1] == "Differential Equations"):
        return "Mathematics -> Algebra -> Other Calculus"

    else:
        return "Mathematics -> Others"

    return "Mathematics -> Others"