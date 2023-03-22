with open(r"C:\Users\Sampath Wijekoon\PycharmProjects\Udemy Projects\day_24\Mail Merge Project Start\Input\Letters\starting_letter.txt") as file:
    content = file.read()

with open(r"C:\Users\Sampath Wijekoon\PycharmProjects\Udemy Projects\day_24\Mail Merge Project Start\Input\Names\invited_names.txt") as file:
    names = []
    for line in file:
        repl_line = line.replace("\n", "")
        names.append(repl_line)

for name in names:
    with open(rf"C:\Users\Sampath Wijekoon\PycharmProjects\Udemy Projects\day_24\Mail Merge Project Start\Output\ReadyToSend\letter_to_{name}", "w") as file:
        ready = content.replace('[name]', name)
        file.write(ready)