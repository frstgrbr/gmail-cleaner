Gmail Cleaner

This Python project uses the Gmail API to automate the cleanup of a Gmail inbox by deleting emails based on specific criteria, such as date or sender. It uses OAuth 2.0 for secure authentication and allows for periodic execution to keep the inbox clean. The script runs in a loop and exits automatically when no more emails match the deletion criteria, ensuring efficient and continuous inbox management.

____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

This script deletes duplicate or unwanted emails from your Gmail inbox. It accomplishes this by iterating through your entire inbox using native Gmail search queries and deleting emails matching those search query parameters. Some parameters include dates and date windows, sender addresses, and domains.

Gmail Cleaner Output
![Gmail Cleaner Output](https://github.com/user-attachments/assets/51834049-7522-4a8d-b721-5891690df06c)

By setting up a Google Developers Console and enabling the Gmail API, I generated OAuth 2.0 credentials and downloaded the JSON file containing the client ID and client secret.

Using this, we're able to monitor script activity and latency of the API in the Google Developers Console.

Gmail Cleaner Activity Timeline
![Gmail Cleaner Activity Timeline](https://github.com/user-attachments/assets/b5aff99f-6f89-4210-b953-5694aab2caa6)

Gmail Cleaner Latency Timeline
![Gmail Cleaner Latency Timeline](https://github.com/user-attachments/assets/eea753f4-16ee-4285-abaf-7bc3471dca9d)
