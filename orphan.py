import re
import glob

def remove_orphans(line) -> str:
    # Begin of line or space, any letter, soft space
    orphans_pattern = r"(^|[ ~])([a-zA-Z],?) "
    result = line
    for i in range(2):
        # need to run twice, in case of sentence like "a b c dasdf" 
        # it will be fixed to "a~b c~dasdf", and second run will clean the rest
        result = re.sub(orphans_pattern, r"\g<1>\g<2>~", result)

    return result


if __name__ == "__main__":
    files_to_correct = glob.glob("*.tex")
    for f in files_to_correct:
        lines=[]
        with open(f,"r") as doc:
            lines=doc.readlines()
        with open(f,"w") as doc:
            for line in lines:
                doc.write(remove_orphans(line))
                
