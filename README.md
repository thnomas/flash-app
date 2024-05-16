# flash ⚡

A command line flashcard app. 
- flash_app.py reads a 'data.csv' file from the same directory.
- Select *Review* to go through all the cards in your file. Your successful and unsucessful attempts are written to the file and tracked.
- Select *Quiz* to test yourself on a subset of cards.
- You can also manually add cards to your file. 

### Sample file format (🇳🇱):
| front   | back    | created_at | review | successful_review | category | example | pronunciation |
|---------|---------|------------|--------|-------------------|----------|---------|---------------|
| apple   | de appel| 2024-05-21 | 0      | 0                 |          |         |               |
| milk    | de melk | 2024-05-22 | 1      | 1                 |          |         |               |
| juice   | het sap | 2024-05-23 | 1      | 1                 |          |         |               |