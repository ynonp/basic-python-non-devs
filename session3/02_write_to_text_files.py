# 'w' => write and truncate the file (if exists)
# 'a' => append to the end of the file (if exists)
with open('output.txt', 'w', encoding='utf8') as fout:
    fout.write("Hello world\n")

