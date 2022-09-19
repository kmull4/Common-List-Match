'''
****NOTE****
The original .csv files have been truncated and altered to protect potentially sensitive information, regardless of the fact that it is publicly available.


Posting:
Match two datasets using the Python function ratio. I only need 1 match and
 only if the score is above .85.

I need the public_150k_plus_220703.csv file. There is a category entitled:
    BorrowerName.

This needs to be matched to the Company Name/Company Legal Name included in the
 attached file.


Self notes:
Should be 53 columns total for the public_[redacted] csv file.
Converted company_names from .xls to .csv
'''


import csv
from difflib import SequenceMatcher

debug = True
ratio = 0.85
final_list = []

# compare function using SequenceMatcher
def match(BorrowerName):
    with open('company_names_test.csv', mode='r') as company_name:
        company_name_reader = csv.DictReader(company_name)
        line_count = 0
        for row in company_name_reader:
            if line_count == 0:
                #print(f'Column names are {", ".join(row)}')
                line_count += 1
            myratio1 = SequenceMatcher(None, str(BorrowerName), str({row["Company Name"]})).ratio()
            myratio2 = 0 # for debug so I only need to type once
            return max(myratio1, myratio2)

# open both .csv files
# depending on how to interface with csv,
    # pull the data point from public_150k_plus
    # call comparing functino above
        # if result >= ratio, then add to final list


with open('public_test.csv', mode='r') as public_list:
    public_list_reader = csv.DictReader(public_list)
    line_count = 0
    for row in public_list_reader:
        if line_count == 0:
            print('uncomment for column names. Too messy for testing.\n')
            #print(f'Column names are {", ".join(row)}')
            line_count += 1
        elif line_count % 1000 == 0: # update user
            print('processing... currently on line', line_count, '\n')
        if match({row["BorrowerName"]}) >= ratio:
            final_list.append({row["LoanNumber"]})
        line_count += 1
    print(f'Processed {line_count} lines.')

print(final_list)
