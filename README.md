# NarrativeNugget - Youtube Video Summary generator
 a simple python program that accepts youtube video link and generates its summary using BARD-API, working in terminal
This script is designed to extract transcripts from a YouTube video and then generate summaries for the extracted text using the Bard API. The summaries are generated in chunks to accommodate longer videos. 

## Prerequisites

Before using the script, make sure you have the following libraries installed:

- `bardapi`: You can install it using `pip install bardapi`.
- `youtube_transcript_api`: You can install it using `pip install youtube_transcript_api`.

## Usage

1. Run the script using a Python interpreter.
2. Enter the YouTube video link when prompted. The link can contain `?v=` to extract the video ID.

The script will then perform the following steps:

1. Extract the transcript from the provided YouTube video using `YouTubeTranscriptApi`.
2. Break down the transcript into smaller chunks (default: 2500 characters).
3. Generate summaries for each chunk of text using the Bard API.
4. Print out the generated summaries.

## Important Notes

- You need a valid API token for the Bard API to use this script. Make sure to replace `token = 'YOUR_BARD_API_TOKEN'` with your actual API token.
- The generated summaries are based on the Bard API's responses and might vary in quality depending on the input text.
- Ensure you have a stable internet connection while running the script since it relies on fetching data from YouTube and the Bard API.
- For the installation of bard-api, prior to running the program, please follow the link above to the repo of bard-api and follow the methods mentioned there for proper installation
- Also please update the token key for authentication of bard-api, by following the steps mentioned in the original repo

## Disclaimer

This script was created for educational and experimental purposes. The quality of the summaries heavily depends on the capabilities of the Bard API and the accuracy of the YouTube transcript. It is recommended to review and refine the summaries manually if they are intended for serious use.

## Credits
The bard-api used in the making of this project was made by @dsdanielpark (link to repo: https://github.com/DSDanielPark/BARD_API).

## Current Status of the project
- As of now the code isn't fully optimized. It takes a chunk of characters at a time and generates it's summary thereby intro and outro of bard is redundant.
- This project will work successfully for only the youtube videos that have captions enabled(auto-generated will work)
- The current version offers best support of youtube videos in english language.

## License

This script is provided under the [MIT License](LICENSE).
