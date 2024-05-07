# extractcomments.py

import os
from bs4 import BeautifulSoup

def extract_comments(input_file_path):
    try:
        with open(input_file_path, 'r', encoding='utf-8') as file:
            text_content = file.read()

        comments = []

        # Parse the text content as HTML using BeautifulSoup
        soup = BeautifulSoup(text_content, 'html.parser')

        # Find all <div> elements with class "md"
        comment_divs = soup.find_all('div', class_='md')   

        for comment_div in comment_divs:
            # Find the <p> element within each <div>
            comment_text = comment_div.find('p')

            # Check if a <p> element was found
            if comment_text:
                comments.append(comment_text.get_text())

        # Extract the file number from the input file name, e.g., output1.txt, output2.txt, etc.
        file_number = os.path.splitext(os.path.basename(input_file_path))[0].replace("output", "")

        # Create 'Data/processed' directory if it doesn't exist
        processed_dir = 'Data/processed'
        if not os.path.exists(processed_dir):
            os.makedirs(processed_dir)

        # Write the extracted comments to comments.txt
        output_comments_file = os.path.join(processed_dir, f'comments{file_number}.txt')
        with open(output_comments_file, 'w', encoding='utf-8') as file:
            for comment in comments:
                file.write(comment + '\n')

        print(f"Comments extracted and saved to '{output_comments_file}'")

        return output_comments_file  # Return the file path
    except Exception as e:
        print(f"An error occurred during comment extraction: {e}")
        return None  # Return None in case of an error
