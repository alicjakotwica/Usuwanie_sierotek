# Script to remove orphan letters at the end of line

The script can remove orphans by inserting hard space (~) after single letter words.

By default, the script searches for all files with `.tex` extension inside the directory it has been run, and applies fixes automatically.
Because of this simplicity, it is strongly advised to run it on project under version control to manage inserted changes. 

The script does not need additional packages to run. 

# Example of work
Before:

"Sierotki to taki jednoliterowe wyrazy, które pozostały na końcu zdania takie jak: a, i, w, itp."

After:

"Sierotki to taki jednoliterowe wyrazy, które pozostały na końcu zdania takie jak: a,~i,~w,~itp."

This will assure that TeX will not break line after a single letter leaving it at the 