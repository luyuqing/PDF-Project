import extract_eko
import extract_stork

output = {"Ekofisk": {}, "Storklakken": {}}
output["Ekofisk"] = extract_eko.output
output["Storklakken"] = extract_stork.output

print(output)
