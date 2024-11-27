gunzip -c ~/Code/MCB185/data/dictionary.gz | grep  -v "[^zirconia]" | grep "r" | grep -E ".{4,}"

# would like to discuss; was struggling with and looked back at previous code, understood, but have questions why iterations I tried did not work