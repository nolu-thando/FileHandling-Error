#functions

def modify_content (content):
    return content.upper()

def read_and_write_file(input_filename, output_filename):
    try:
        with open (input_filename, 'r') as inflile:
            content = infile.read()

            modified = modify_content (content)