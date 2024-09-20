import os

# Function to extract text from a .vtt file
def extract_text_from_vtt(vtt_file):
    lines = []
    with open(vtt_file, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            # Skip the lines that are either empty, timestamps, or metadata
            if line and not line.startswith('WEBVTT') and not '-->' in line:
                lines.append(line)
    return ' '.join(lines)

def main():
    # Get the current directory
    directory = os.path.dirname(os.path.abspath(__file__))
    
    # Get all .vtt files in the directory
    vtt_files = [f for f in os.listdir(directory) if f.endswith('.vtt')]
    
    # Sort files alphabetically or by any other specific logic if needed
    vtt_files.sort()
    
    # Extract text from each .vtt file and concatenate them as paragraphs
    paragraphs = []
    for vtt_file in vtt_files:
        text = extract_text_from_vtt(os.path.join(directory, vtt_file))
        if text:  # Only add non-empty text
            paragraphs.append(text)
    
    # Join paragraphs with a newline separating each one
    output_text = '\n\n'.join(paragraphs)
    
    # Write the output to a text file
    output_file = os.path.join(directory, 'output.txt')
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(output_text)

if __name__ == "__main__":
    main()