import os

def write_list(fname, stories):
    with open(fname, 'w') as f:
        for title, author, href in sorted(list(stories), key=lambda el: el[0]):
            f.write(f"{title} by {author}: {href}\n\n")

if __name__ == "__main__":
    output = ''

    fname_match = '2021-shorts'
    # try:
    os.remove(fname_match+'.md')


    for fname in sorted(list(os.listdir('.'))):
        if fname[-3:] == '.md' and fname_match in fname:
            publication = fname.replace(fname_match, '').replace('.md', '').replace('-', ' ').title()
            output += f"\n## {publication} \n"
            with open(fname) as f:
                output += f.read() + "\n"

    with open(fname_match+'.md', 'w') as f:
        f.write(output)
    print("wrote to", fname_match+'.md')