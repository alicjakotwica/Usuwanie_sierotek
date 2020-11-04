import re
import sys

def remove_orphants(line) -> str:
    return re.sub("(\s[iaezw])\s", "\g<1>~", line)

if __name__ == "__main__":
    for i in range(len(sys.argv)-1):
        lines=[]
        with open(sys.argv[i+1],"r") as doc:
            lines=doc.readlines()
        with open(sys.argv[i+1],"w") as doc:
            for line in lines:
                doc.write(remove_orphants(line))
                
