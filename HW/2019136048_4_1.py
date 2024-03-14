from ArrayStack import ArrayStack

def ReadFile(file_path):
    try:
        with open(file_path, 'r') as file:
            source_code = file.read()
    except FileNotFoundError:
        print(f"파일 '{file_path}'를 찾을 수 없습니다.")
        return

    stack = ArrayStack(100)

    line_number = 1
    char_index = 0

    for char in source_code:
        char_index += 1

        if char == '\n':
            line_number += 1
            char_index = 0

        if char in "{[(":
            stack.push((char, line_number, char_index))

        elif char in "}])":
            if stack.isEmpty():
                print(f"조건2 위반 - '{char}' (라인 {line_number}, 문자 {char_index})")
                return  
            left, left_line, left_char = stack.pop()
            if (char == "}" and left != "{") or \
               (char == "]" and left != "[") or \
               (char == ")" and left != "("):
                print(f"조건3 위반 - '{char}' (라인 {line_number}, 문자 {char_index})")
                return  

    if not stack.isEmpty():
        left, left_line, left_char = stack.pop()
        print(f"조건1 위반 - '{left}' (라인 {left_line}, 문자 {left_char})")
        return  

    print("괄호가 일치합니다.")

file_path = "Check.py"
ReadFile(file_path)
