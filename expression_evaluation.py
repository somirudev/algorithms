import math

numbers = set("1234567890.")
precedence = {
    "(": 1000,
    "w": 4,
    "l": 4,
    "s": 4,
    "c": 4,
    "t": 4,
    "^": 3,
    "v": 2,
    "%": 2,
    "/": 2,
    "*": 2,
    "+": 1,
    "-": 1,
}
operators = {
    "(": None,
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
    "v": lambda x, y: x // y,
    "^": lambda x, y: x**y,
    "%": lambda x, y: x % y,
    "!": lambda x: math.factorial(x),
    "w": lambda x: math.sqrt(x),
    "l": lambda x: math.log(x),
    "s": lambda x: math.sin(x),
    "c": lambda x: math.cos(x),
    "t": lambda x: math.tan(x),
}
unary_operators = set("!wlsct")
replacements = {
    " ": "",
    "**": "^",
    "//": "v",
    "sqrt": "w",
    "log": "l",
    "sin": "s",
    "cos": "c",
    "tan": "t",
    "pi": "p",
}


def expression_evaluation(input_string):
    operand_list = []
    operator_list = []
    for old, new in replacements.items():
        input_string = input_string.replace(old, new)
    previous_character = ""
    for i in range(len(input_string)):
        # handle operands, including e, pi and floats
        if input_string[i] == "e":
            operand_list.append(math.e)
        elif input_string[i] == "p":
            operand_list.append(math.pi)
        elif input_string[i] in numbers:
            if previous_character in numbers:
                operand_list[-1] += input_string[i]
            else:
                operand_list.append(input_string[i])
        # handle closing brackets
        elif input_string[i] == ")":
            operator = operator_list.pop()
            while not operator == "(":
                if operator in unary_operators:
                    if len(operand_list) < 1:
                        raise ValueError(f"not enough operands for operator {operator}")
                    value = float(operand_list.pop())
                    operand_list.append(operators[operator](value))
                else:
                    if len(operand_list) < 2:
                        raise ValueError(f"not enough operands for operator {operator}")
                    value2 = float(operand_list.pop())
                    value1 = float(operand_list.pop())
                    operand_list.append(operators[operator](value1, value2))
                operator = operator_list.pop()
        # handle factorial
        elif input_string[i] == "!":
            operator = input_string[i]
            if len(operand_list) < 1:
                raise ValueError(f"not enough operands for operator {operator}")
            value = int(operand_list.pop())
            operand_list.append(operators[operator](value))
        # handle other operands according to precedence (if lower than on stack, do math, if higher, add onto stack until needed)
        elif input_string[i] in operators:
            if operator_list:
                if (
                    precedence[input_string[i]] > precedence[operator_list[-1]]
                    or operator_list[-1] == "("
                ):
                    operator_list.append(input_string[i])
                else:
                    operator = operator_list.pop()
                    if operator in unary_operators:
                        if len(operand_list) < 1:
                            raise ValueError(
                                f"not enough operands for operator {operator}"
                            )
                        value = float(operand_list.pop())
                        operand_list.append(operators[operator](value))
                    else:
                        if len(operand_list) < 2:
                            raise ValueError(
                                f"not enough operands for operator {operator}"
                            )
                        value2 = float(operand_list.pop())
                        value1 = float(operand_list.pop())
                        operand_list.append(operators[operator](value1, value2))
                    operator_list.append(input_string[i])
            else:
                operator_list.append(input_string[i])

        else:
            raise ValueError("Not a valid expression")

        previous_character = input_string[i]

        print(operator_list)
        print(operand_list)

    # input_string empty, time to do remaining calculations
    while operator_list:
        operator = operator_list.pop()
        if operator in unary_operators:
            if len(operand_list) < 1:
                raise ValueError(f"not enough operands for operator {operator}")
            value = float(operand_list.pop())
            operand_list.append(operators[operator](value))
        else:
            if len(operand_list) < 2:
                raise ValueError(f"not enough operands for operator {operator}")
            value2 = float(operand_list.pop())
            value1 = float(operand_list.pop())
            operand_list.append(operators[operator](value1, value2))
        print(operator_list)
        print(operand_list)
    return operand_list[0]


if __name__ == "__main__":
    input_string = input("Give an expression to evaluate:")
    print(f"Result = {expression_evaluation(input_string)}")
