import csv
import re
import sys
from openai import OpenAI
def get_api_key(file_path):
    try:
        with open(file_path, 'r') as file:
            api_key = file.readline().strip()
        return api_key
    except FileNotFoundError:
        print("API key file not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the API key: {e}")
        return None

api_key_file_path = "D:/api.txt"  
key = get_api_key(api_key_file_path)


client = OpenAI(api_key=key)

def giveQuery(user):
    prompt = f"""
    Follow the steps:
    1. You are generating test cases for a web application.
    2. The test cases should be of only two values in each - name and email id
    3. Give output in a csv format only such as the angled delimiters shown:
    <<<testname, testname@gmail.com>>>
    4. {user}
    5. The name and email ids can be unique from the example I gave
    6. Do not deviate from the output format
    """

    print(prompt)
    return prompt


def query_openai(query):
    try:
        response = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=query,
            max_tokens=2048
        )
        return response.choices[0].text
    except Exception as e:
        return str(e)


def update_test_cases_csv_simple(file_path, input_string):
    try:
        rows = input_string.strip().split("\n")
        with open(file_path, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for row in rows:
                name, email = row.split(", ")
                writer.writerow([name, email])
    except:
        print("Failed")


def parse_and_update(input_text, csv_file_path):
    print(input_text)
    pattern = re.compile(r'<<<(.*?)>>>')
    matches = pattern.findall(input_text)
    with open(csv_file_path, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        if csvfile.tell() == 0:
            writer.writerow(['name', 'email'])
        for match in matches:
            name, email = match.split(',')
            writer.writerow([name.strip(), email.strip()])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        user = ' '.join(sys.argv[1:])
    else:
        print("No argument provided.")
        user = "5 test cases"
    filepath = "test_cases.csv"
    print(user)
    parse_and_update(query_openai(giveQuery(user)), filepath)
