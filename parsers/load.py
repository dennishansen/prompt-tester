import json

def run():

    input_file = "parsers/parser.py"
    output_file = "prompts/diff_prompts.json"

    # Read the parser file
    with open(input_file, "r") as f:
        parser = f.read()

    # Read the JSON file
    with open(output_file, 'r') as file:
        diff_prompts = file.read()

    # Parse the JSON content into a Python object
    prompts = json.loads(diff_prompts)

    # Keep asking for a prompt name until the user enters a valid name
    while True:
        diff_prompt_name = input("Enter the name of the diff prompt: ")

        # Check if the name is valid
        if any(prompt["name"] == diff_prompt_name for prompt in prompts):
            break

        print("No prompt found with that name")
        
    # Get the diff prompt object to update
    prompt = next(prompt for prompt in prompts if prompt["name"] == diff_prompt_name)

        # Continue to ask for a parser name until a unique name is given
    while True:
        name = input("Enter a unique name for the diff prompt: ")

        # Check if the name is unique
        if not any(parser["name"] == name for parser in prompt['parsers']):
            break

        print("A diff prompt with that name already exists")

    # Define a new parser object
    new_parser = {
        "id": str(len(prompt["parsers"])),
        "parser": parser
    }

    # Append the new parser object to the "parsers" list of the first prompt
    prompt["parsers"].append(new_parser)

    # Convert the updated Python object back to JSON format
    updated_diff_prompts = json.dumps(prompts, indent=4)

    # Write the updated JSON content back to the file
    with open(output_file, 'w') as file:
        file.write(updated_diff_prompts)

    print("Completed")