def remove_char_at_index(s: str, index: int) -> str:
    return s[:index] + s[index + 1:]

# clearing output file and fmtScript file
file = open("main.rs", "w")
file.write("")
file.close()


# opening script and output file
file = open("rustscript.txt", "r")
outputfile = open("main.rs", "a")

# current active variables
active_variables = []

# import statment occurence
import_occurence = True

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
    elif words[0] == "from" and import_occurence:
        outputfile.write(f"use {words[1]}::{words[3]};\n")
    elif words[0] != "from" and import_occurence:
        import_occurence = False
        outputfile.write("fn main() {\n")
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
        if words[0] in active_variables:
            outputfile.write(f"    {' '.join(str(text) for text in words)};\n")
        else:
            outputfile.write(f"    let mut {' '.join(str(text) for text in words)};\n")
            active_variables.append(words[0])

outputfile.write("}\n")

# closing all opened files
outputfile.close()
file.close()