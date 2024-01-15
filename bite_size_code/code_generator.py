#!/usr/bin/python3

class CodeGenerator:
    def __init__(self, class_name):
        self.class_name = class_name

    def generate(self):
        code = f'class {self.class_name}:\n'
        code += '    def __init__(self):\n'
        code += '        pass\n\n'
        code += '    def some_method(self):\n'
        code += '        pass\n'
        return code

def get_user_input():
    class_name = input("Enter the class name: ")
    return class_name

def main():
    class_name = get_user_input()
    code_generator = CodeGenerator(class_name)
    generated_code = code_generator.generate()

    print("\nGenerated code:")
    print(generated_code)

if __name__ == "__main__":
    main()

