import pyperclip

def main():
    problem_name = get_problem_name()
    file_path = f"neetcode 150/{problem_name}.py"
    with open(file_path, "w") as file:
        file.write(f"")
    print(f"Created file: {file_path}")

    with open("neetcode 150/ReadMe.md", "r") as readme:
        lines = readme.readlines()

    lines[3] = f"## {len(lines) - 6} / 150\n"
    lines.append(f"| {len(lines) - 6} | {problem_name} |\n")

    with open("neetcode 150/ReadMe.md", "w") as readme:
        readme.writelines(lines)

    print(f"Updated ReadMe.md")

def get_problem_name():
    return pyperclip.paste().strip().lower().split('?')[0].split('/')[-1]

if __name__ == "__main__":
    main()