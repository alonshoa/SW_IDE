def levenshtein_distance(s1,s2):
    if len(s1) > len(s2):
        s1,s2 = s2,s1

    distances = range(len(s1) + 1)
    for index2,char2 in enumerate(s2):
        newDistances = [index2+1]
        for index1,char1 in enumerate(s1):
            if char1 == char2:
                newDistances.append(distances[index1])
            else:
                newDistances.append(1 + min((distances[index1],
                                             distances[index1+1],
                                             newDistances[-1])))
        distances = newDistances
    return distances[-1]

def compare_code(app):
    input_code = app.code_text.get("1.0", "end-1c")
    output_code = app.output_code_textbox.get("1.0", "end-1c")
    input_code_lines = input_code.split("\n")
    output_code_lines = output_code.split("\n")
    app.output_code_textbox.tag_config("diff", background="red")
    for i in range(len(input_code_lines)):
        if levenshtein_distance(input_code_lines[i], output_code_lines[i]) > 0:
            app.output_code_textbox.tag_add("diff", str(i+1) + ".0", str(i+1) + ".end")
