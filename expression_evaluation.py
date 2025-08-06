numbers = set("1234567890.")
precedence = {
    "^": 3,
    "v": 2,
    "%": 2,
    "/": 2,
    "*": 2,
    "+": 1,
    "-": 1,
    "(": 0,
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
}


def expression_evaluation(input_string):
    operand_list = []
    operator_list = []
    input_string = input_string.replace(" ", "")
    input_string = input_string.replace("**", "^")
    input_string = input_string.replace("//", "v")
    previous_character = ""
    for i in range(len(input_string)):
        if input_string[i] in numbers:
            if previous_character in numbers:
                operand_list[-1] += input_string[i]
            else:
                operand_list.append(input_string[i])
        elif input_string[i] == ")":
            operator = operator_list.pop()
            while not operator == "(":
                if len(operand_list) < 2:
                    raise ValueError(f"not enough operands for operator {operator}")
                value1 = int(operand_list.pop())
                value2 = int(operand_list.pop())
                operand_list.append(operators[operator](value2, value1))
                operator = operator_list.pop()
        elif input_string[i] in operators:
            if operator_list:
                if (
                    precedence[input_string[i]] > precedence[operator_list[-1]]
                    or input_string[i] == "("
                ):
                    operator_list.append(input_string[i])
                else:
                    operator = operator_list.pop()
                    value1 = int(operand_list.pop())
                    value2 = int(operand_list.pop())
                    operand_list.append(operators[operator](value2, value1))
                    operator_list.append(input_string[i])
            else:
                operator_list.append(input_string[i])
        else:
            raise ValueError("Not a valid expression")
        previous_character = input_string[i]
        print(operator_list)
        print(operand_list)
    while operator_list:
        operator = operator_list.pop()
        if len(operand_list) < 2:
            raise ValueError(f"not enough operands for operator {operator}")
        value1 = int(operand_list.pop())
        value2 = int(operand_list.pop())
        operand_list.append(operators[operator](value2, value1))
        print(operator_list)
        print(operand_list)
    return operand_list[0]


if __name__ == "__main__":
    input_string = input("Give an expression to evaluate:")
    print(f"Result = {expression_evaluation(input_string)}")
