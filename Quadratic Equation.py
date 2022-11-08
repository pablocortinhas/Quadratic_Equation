import os

def clear():
    os.system('cls')


j = 1
while j == 1:
    w = 1
    while w == 1:
        print('-' * 24, 'Quadratic Equation - Pablo Cortinhas', '-' * 24)
        op = int(input('[1] Calculate - [2] Theory - [3] Go out\n'))
        if op == 1:
            w = 2
            clear()

        elif op == 2:
            clear()
            print('-' * 32, 'Quadratic Equation', '-' * 32)
            print('\n  This article is about algebraic equations of degree two and their solutions.\n'
                  'For the formula used to find solutions to such equations, see Quadratic formula.\n'
                  'For functions defined by polynomials of degree two, see Quadratic function.\n'
                  '\n  In algebra, a quadratic equation (from Latin quadratus "square") is any \n'
                  'equation that can be rearranged in standard form as -> ax² + bx + c = 0\n'
                  '\n  Where x represents an unknown, and a, b, and c represent known numbers, where\n'
                  'a ≠ 0. (If a = 0 (and b ≠ 0) then the equation is linear, not quadratic, as \n'
                  'the ax² term becomes zero.) The numbers a, b, and c are the coefficients of \n' 
                  'the equation and may be distinguished by calling them, respectively, the\n' 
                  'quadratic coefficient, the linear coefficient and the constant or free term.\n')
            print('  The values of x that satisfy the equation are called solutions of the equation,\n'
                  'and roots or zeros of the expression on its left-hand side. A quadratic equation\n'
                  'has at most two solutions. If there is only one solution, one says that it is a\n'
                  'double root. If all the coefficients are real numbers, there are either two real\n'
                  'solutions, or a single real double root, or two complex solutions that are complex\n'
                  'conjugates of each other.\n'
                  '\n  A quadratic equation always has two roots, if complex roots are included;\n'
                  'and a double root is counted for two. A quadratic equation can be factored into\n'
                  'an equivalent equation.\nSome formulas seen in the Quadratic Equation:')
            print('\nΔ = b² - 4 . a . c\n')
            print('\nx = -b ± √Δ')
            print('   --------- ')
            print('     2 . a \n')
            print('\nhttps://en.wikipedia.org/wiki/Quadratic_equation\n\n')

            q = 1
            while q == 1:
                z = input('Do you want to return to the menu? [Y] Yes\n')
                z = z.upper()
                if z == 'Y':
                    q = 2
                    w = 1
                else:
                    z != 'Y'
                    q = 1

        elif op == 3:
            exit()

        elif op != 1 or op != 2 or op != 3:
            w = 1
        clear()


    def calc():
        print('\nQuadratic Formula -> Δ = b² - 4 * a * c')
        a = float(input('\nEnter the value of a: '))
        b = float(input('Enter the value of b: '))
        c = float(input('Enter the value of c: '))
        delta = (b ** 2 - 4 * a * c)
        x1 = (-b + delta ** 0.5) / (2 * a)
        x2 = (-b - delta ** 0.5) / (2 * a)

        if delta > 0:
            print(f"\nΔ= {delta} \nx'= %.2f \nx''= %.2f\n" %(x1, x2))

        elif delta < 0:
            print(f'\nΔ= {delta} delta is less than zero.\n')

        elif delta == 0:
            print(f'\nΔ= {delta}\nx = {x1}\n')


    calc()
j = 1
