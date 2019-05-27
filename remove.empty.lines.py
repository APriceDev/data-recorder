with open('data/data-1558991081123.txt') as infile, open('data/data.txt', 'w') as outfile:
    for line in infile:
        if not line.strip():
            continue  # skip the empty line
        outfile.write(line)  # non-empty line. Write it to output
