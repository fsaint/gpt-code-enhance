from pygptcalls import gptcall
import file_ops

if __name__ == '__main__':
    print("Hello")
    prompt = "update all python files in the directory sample_project. Add documentation and type annotations in every method."
    gptcall(file_ops, prompt)
