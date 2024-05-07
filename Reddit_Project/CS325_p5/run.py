# main.py

import os
from bs4 import BeautifulSoup
import Module_2.redditscrape as redditscrape
import Module_3.extractcomments as extractcomments
import Module_4.analysis as analysis

def read_urls_from_file(file_path):
    """Reads URLs from a file and returns a list."""
    with open(file_path, 'r') as file:
        urls = [line.strip() for line in file.readlines()]
    return urls

def main():
    # Get the current working directory
    current_directory = os.getcwd()

    # Create 'Data/raw' directory if it doesn't exist
    raw_dir = os.path.join(current_directory, 'Data', 'raw')
    if not os.path.exists(raw_dir):
        os.makedirs(raw_dir)

    # Counter for the output files
    output_counter = 1

    # Specify the file path containing the URLs
    urls_file_path = "D:\Reddit_Scrapper_Project\Reddit_Project\urls.txt"  # Replace with the actual path
    

    # Read URLs from the external file
    urls = read_urls_from_file(urls_file_path)

    for url in urls:
        url = url.strip()
        reddit_html = redditscrape.download_and_save_reddit_html(url)

        if reddit_html is not None:
            # Save the 'output.txt' file in the 'Data/raw' directory
            output_file_path = os.path.join(raw_dir, f'output{output_counter}.txt')

            with open(output_file_path, 'w', encoding='utf-8') as file:
                file.write(reddit_html)

            print(f"Reddit HTML content downloaded and saved to '{output_file_path}'")

            # Extract comments from the output file
            comments_file_path = extractcomments.extract_comments(output_file_path)

            if comments_file_path is not None:
                # Perform sentiment analysis on the extracted comments
                analysis.perform_sentiment_analysis(comments_file_path)
                output_counter += 1
            else:
                print("An error occurred during comment extraction. Skipping sentiment analysis.")

if __name__ == "__main__":
    main()
