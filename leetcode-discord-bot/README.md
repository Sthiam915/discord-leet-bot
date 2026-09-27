# LeetCode Discord Bot

This project is a Discord bot designed to help users track their LeetCode daily challenges. It allows users to mark challenges as done, track their progress, and analyze their performance over time.

## Features

- Mark LeetCode daily challenges as done and record the time taken.
- Track daily completions for the month.
- Announce the number of days missed in the past 5 days.
- Calculate and announce average completion times for each member enrolled in the server.

## Project Structure

```
leetcode-discord-bot
├── src
│   ├── __init__.py
│   ├── bot.py
│   ├── commands
│   │   ├── __init__.py
│   │   ├── daily.py
│   │   └── stats.py
│   ├── models
│   │   ├── __init__.py
│   │   └── user_progress.py
│   ├── services
│   │   ├── __init__.py
│   │   ├── leaderboard.py
│   │   └── reminders.py
│   └── utils
│       ├── __init__.py
│       └── date_utils.py
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
├── main.py
└── database
    └── sqlite.db
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd leetcode-discord-bot
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Configuration

- Create a `.env` file in the root directory based on the `.env.example` file and fill in the necessary environment variables.

## Usage

1. Run the bot:
   ```
   python main.py
   ```
2. Use the commands to interact with the bot:
   - Mark a daily challenge as done.
   - Check your progress and statistics.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.