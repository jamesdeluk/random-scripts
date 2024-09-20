import os

def srt_to_text(srt_file):
    """Convert .srt file content to plain text."""
    text = []
    with open(srt_file, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line.isdigit() or '-->' in line or not line:
                continue
            text.append(line)
    return ' '.join(text)

def convert_folder(folder_path, output_file):
    """Convert all .srt files in a folder to plain text paragraphs."""
    with open(output_file, 'w', encoding='utf-8') as output:
        for filename in sorted(os.listdir(folder_path)):
            if filename.endswith('.srt'):
                srt_file_path = os.path.join(folder_path, filename)
                paragraph = srt_to_text(srt_file_path)
                output.write(paragraph + '\n\n')

if __name__ == "__main__":
    folder_path = "subs"  # Replace with the path to your .srt folder
    output_file = "output.txt"  # The output file where the text will be saved
    convert_folder(folder_path, output_file)
