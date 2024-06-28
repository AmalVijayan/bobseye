from linter import AILinter

if __name__ == '__main__':
    unclean_code =  """
                    def c(a, b):
                        x = []
                        for i in range(len(a)):
                            x.append(a[i] + b[i])
                        return x
                    """
    
    clean_code = """
                 def add_elementwise(list1, list2):
                    if len(list1) != len(list2):
                        raise ValueError("Both lists must have the same length.")

                    return [x + y for x, y in zip(list1, list2)]
                 """

    inputs = [
        {"snippet" : unclean_code},
        {"snippet" : clean_code},
        ]
    
    linter = AILinter('gpt-4')
    linter.lint_code_snippets(inputs)
    linter.write_results_to_file('lint-results.txt')



    