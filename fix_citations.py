import os
import re
import glob


def is_in_math_or_command(text, pos):
    """Check if position is inside a math environment or LaTeX command"""
    # Check for math environments
    math_envs = [
        (r"\$\$", r"\$\$"),  # Display math
        (r"\$", r"\$"),  # Inline math
        (r"\\begin\{equation\}", r"\\end\{equation\}"),
        (r"\\begin\{align\}", r"\\end\{align\}"),
        (r"\\begin\{math\}", r"\\end\{math\}"),
    ]

    for start_pattern, end_pattern in math_envs:
        starts = [m.start() for m in re.finditer(start_pattern, text)]
        ends = [m.start() for m in re.finditer(end_pattern, text)]

        for i in range(min(len(starts), len(ends))):
            if starts[i] < pos < ends[i]:
                return True

    # Check if within a LaTeX command
    command_matches = re.finditer(r"\\[a-zA-Z]+(\{[^{}]*\}|\[[^\[\]]*\])*", text)
    for match in command_matches:
        if match.start() < pos < match.end():
            return True

    return False


def replace_citations(text):
    """Replace incorrect citations with correct LaTeX format"""
    result = text

    # Find all instances of "word" (but not `` or '' which are already correct)
    quotes_pattern = r'"([^"]+)"'
    matches = list(re.finditer(quotes_pattern, result))

    # Process matches in reverse to avoid position shifts
    for match in reversed(matches):
        start, end = match.span()
        content = match.group(1)

        # Skip if in math or LaTeX command
        if is_in_math_or_command(result, start):
            continue

        # Check if it's a multi-word citation (sentence) or single word
        if " " in content:
            replacement = f"``{content}'"
        else:
            replacement = f"`{content}'"

        result = result[:start] + replacement + result[end:]

    return result


def process_file(file_path):
    """Process a single LaTeX file"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        modified_content = replace_citations(content)

        if modified_content != content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(modified_content)
            print(f"Fixed citations in: {file_path}")
        else:
            print(f"No changes needed in: {file_path}")

    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")


def main():
    # Define the directory where your LaTeX files are located
    chapters_dir = r"c:\masterthesis\chapters"

    # Get all .tex files
    tex_files = glob.glob(os.path.join(chapters_dir, "*.tex"))

    print(f"Found {len(tex_files)} .tex files to process")

    # Process each file
    for file_path in tex_files:
        process_file(file_path)

    print("Citation fixing completed!")


if __name__ == "__main__":
    main()
