# file_read_write.py
def modify_content(content):
    
    # Example modification: Convert text to uppercase
    return content.upper()

def read_and_write_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        modified = modify_content(content)

        with open(output_filename, 'w') as outfile:
            outfile.write(modified)

        print(f"Modified content written to '{output_filename}'.")
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError as e:
        print(f"Error reading or writing files: {e}")


