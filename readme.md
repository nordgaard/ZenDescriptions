Setup:

1) In the GetDescriptionsByID.py, update the credentials with your email and API key

2) Create custom personal view you want to get the descriptions from, be sure to include columns, IDs, Subject, Requested Date, Update Date and any other columns you will find useful

3) Export as CSV

4) Unzip document and import csv file into GoogleSheets

5) Copy the ticket IDS column and past into ids.tsv (you can delete the header row)

ids.tsv should look like this:

12345
12346
12347
12387
21452
...

6) in the GetDescriptionsByID.py file, update the Descriptions_DATE.csv and save

7) in Terminal, navigate to this folder and run "python GetDescriptionsByID.py"

8) In google sheets add newly created Descriptions_DATE.csv file to a new tab

9) In your main sheets document, add a column "description" and run =VLOOKUP(COL_ID,SecondSheetes_ID,2,FALSE)
