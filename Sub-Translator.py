from googletrans import Translator
import re

translator = Translator()


# def isNum(input_string):
#     if input_string:
#         if input_string[0].isdigit() and input_string[-1].isdigit():
#             return True
#     return False

def isNum(input_string):
    if input_string:
        return input_string[0].isdigit() and input_string[-1].isdigit()

sub_source = "source.srt"
output_file_path = "output.txt"

with open(sub_source, "r") as src:
    text_to_translate = src.read()

lines = text_to_translate.split("\n")

new_lines = []
i = 0
while i < len(lines):
    if isNum(lines[i]):
        new_lines.append(lines[i])

    elif (
        (i + 1 < len(lines))
        and isNum(lines[i]) == False
        and isNum(lines[i + 1]) == False
    ):
        new_lines.append(lines[i] + " " + lines[i + 1])
        i += 1

    elif (
        (i + 2 < len(lines))
        and isNum(lines[i]) == False
        and isNum(lines[i + 1]) == False
        and isNum(lines[i + 2]) == False
    ):
        new_lines.append(lines[i] + " " + lines[i + 1] + " " + lines[i + 2])
        i += 2

    else:
        new_lines.append(lines[i])

    i += 1

lines = new_lines

for i in range(len(lines)):
    if isNum(lines[i]):
        pass

    else:
        myText = str(lines[i]) + "(td)"
        translated_text = translator.translate(myText, dest="ckb", src="en").text
        lines[i] = translated_text


def remove_td(string_list):
    return [s.replace("(td)", "\n") for s in string_list]


def remove_TD(string_list):
    return [s.replace("(TD)", "\n") for s in string_list]


lines = remove_td(lines)
lines = remove_TD(lines)

modified_subtitles = "\n".join(lines)


with open(output_file_path, "w", encoding="utf-8") as output_file:
    output_file.write(modified_subtitles)
