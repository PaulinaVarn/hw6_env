def celsius_converter(f_temp:str|float):
    f_temp = float(f_temp)
    f_temp = round((f_temp - 32) / 1.8, 2)
              
def parse_and_clean(line:str):
    new_line = [item.strip() for item in line.strip().split("|")]
    if len(new_line) < 5 or new_line[4] != "ACTIVE":
        return None
    return [item.strip() for item in new_line]


with open("environmental_raw.txt", "r") as infile, open("cleaned_rows.csv", "w") as outfile:
    corrupted_lines = 0
    for line in infile:
        cleaned_row = parse_and_clean(line)
        if cleaned_row == None:
            corrupted_lines +=1
        else:
            temperature = cleaned_row[2]
            if temperature.replace(".", "", 1).isdigit():
                cleaned_row[2] = celsius_converter(temperature)
                outfile.write(",".join(map(str, cleaned_row)) + "\n")
            else:
                corrupted_lines += 1
print(f"How many lines were corrupted: {corrupted_lines}")