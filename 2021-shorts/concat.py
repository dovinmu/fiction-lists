import os

output = ''

fname_match = '2021-shorts'
for fname in sorted(list(os.listdir('.'))):
	if fname[-3:] == '.md' and fname_match in fname:
		publication = fname.replace(fname_match, '').replace('.md', '').replace('-', ' ')
		output += f"\n## {publication} \n"
		with open(fname) as f:
			output += f.read()

with open(fname_match+'.md', 'w') as f:
	f.write(output)