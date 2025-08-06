import math

numbers = set("1234567890.pe")
precedence = {
    "(": 1000,
    "!": 4,
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

    # pre-processing to make all operators 1 character only
    for old, new in replacements.items():
        input_string = input_string.replace(old, new)

    i = 0
    while i < len(input_string):
        char = input_string[i]
        is_unary_minus = char == "-" and (
            i == 0
            or input_string[i - 1] in operators
            and input_string[i - 1] not in (")", "!")
        )

        # handle unary minus
        if is_unary_minus:
            j = i + 1
            start_number_index = j
            while j < len(input_string) and input_string[j] in numbers:
                j += 1
            num_str = input_string[start_number_index:j]
            if num_str == "e":
                operand_list.append(-math.e)
            elif num_str == "p":
                operand_list.append(-math.pi)
            else:
                operand_list.append(float("-" + num_str))
            i = j
            continue

        # handle operands, including e, pi and floats
        if char == "e":
            operand_list.append(math.e)
            i += 1
        elif char == "p":
            operand_list.append(math.pi)
            i += 1
        elif char in numbers:
            start_number_index = i
            while i < len(input_string) and input_string[i] in numbers:
                i += 1
            operand_list.append(float(input_string[start_number_index:i]))

        # handle opening brackets
        elif char == "(":
            operator_list.append(char)
            i += 1

        # handle closing brackets
        elif char == ")":
            while operator_list and not operator_list[-1] == "(":
                operator = operator_list.pop()
                if operator in unary_operators:
                    if len(operand_list) < 1:
                        raise ValueError(
                            f"not enough operands for unary operator {operator}"
                        )
                    value = operand_list.pop()
                    operand_list.append(operators[operator](value))
                else:
                    if len(operand_list) < 2:
                        raise ValueError(
                            f"not enough operands for binaryoperator {operator}"
                        )
                    value2 = operand_list.pop()
                    value1 = operand_list.pop()
                    operand_list.append(operators[operator](value1, value2))
            if not operator_list or operator_list.pop() != "(":
                raise ValueError("Mismatched parentheses")
            i += 1

        # handle other operands according to precedence (if lower than on stack, do math, if higher, add onto stack until needed)
        elif char in operators:
            while (
                operator_list
                and operator_list[-1] != "("
                and precedence.get(char, 0) <= precedence.get(operator_list[-1], 0)
            ):
                operator = operator_list.pop()
                if operator in unary_operators:
                    if len(operand_list) < 1:
                        raise ValueError(
                            f"not enough operands for unary operator {operator}"
                        )
                    value = operand_list.pop()
                    operand_list.append(operators[operator](value))
                else:
                    if len(operand_list) < 2:
                        raise ValueError(
                            f"not enough operands for binary operator {operator}"
                        )
                    value2 = operand_list.pop()
                    value1 = operand_list.pop()
                    operand_list.append(operators[operator](value1, value2))
            operator_list.append(char)
            i += 1

        else:
            raise ValueError("Not a valid token: {char}")

    # input_string empty, time to do remaining calculations
    while operator_list:
        if operator_list[-1] == "(":
            raise ValueError("Mismatched parentheses")

        operator = operator_list.pop()
        if operator in unary_operators:
            if len(operand_list) < 1:
                raise ValueError(f"not enough operands for unary operator {operator}")
            value = operand_list.pop()
            operand_list.append(operators[operator](value))
        else:
            if len(operand_list) < 2:
                raise ValueError(f"not enough operands for binary operator {operator}")
            value2 = operand_list.pop()
            value1 = operand_list.pop()
            operand_list.append(operators[operator](value1, value2))
    if len(operand_list) != 1:
        raise ValueError("Invalid expression format")
    return operand_list[0]


if __name__ == "__main__":
    input_string = input("Give an expression to evaluate:")
    print(f"Result = {expression_evaluation(input_string)}")
