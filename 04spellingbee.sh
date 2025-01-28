gunzip -c ~/Code/MCB185/data/dictionary.gz | grep  -v "[^zirconia]" | grep "r" | grep -E ".{4,}"
# can't I combine the last grep with one of the first two greps?

# why doesn't this work:
 # grep  -v "[^zirconia]{,3}" | grep "r" | grep -E ".{4,}"
 # grep  -v "[^zirconia]" | grep "r" | grep -E ".{4,}"