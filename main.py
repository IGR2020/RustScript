def remove_char_at_index(s: str, index: int) -> str:
    return s[:index] + s[index + 1:]

# clearing output file and fmtScript file
file = open("main.rs", "w")
file.write("")
file.close()


# opening script and output file
file = open("rustscript.txt", "r")
outputfile = open("main.rs", "a")
outputfile.write("fn main() {\n")

# reading lines
for line in file.readlines():

    # spearating words and keywords
    words = []
    current_word = ""
    is_string = False
    for i, text in enumerate(line):
        if text == '"':
            is_string = not is_string
        if text in ["(", " ", ")", ";"] and not is_string:
            words.append(current_word)
            current_word = ""
        else:
            current_word += text
    
    # compiling key words and arguments
    if words[0] == "#":
        pass
    elif words[0] == "print":
        variables = []
        variable_names = []
        for i, text in enumerate(words[1]):
            if text == "}" and words[1][i - 2] == "{":
                variables.append(i - 1)
                variable_names.append(words[1][i - 1])
        for var in variables:
            words[1] = remove_char_at_index(words[1], var)
        if len(variables) > 0:
            outputfile.write(f"    println!({words[1]}, {', '.join(str(var) for var in variable_names)});\n")
        else:
            outputfile.write(f"    println!({words[1]});\n")
    else:
        outputfile.write(f"    let {' '.join(str(text) for text in words)};\n")

outputfile.write("}")

# closing all opened files
outputfile.close()
file.close()