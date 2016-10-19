# coding: utf-8
"""Python script to automatically grade based on pull requests."""

import csv
import sys
import grader
from reader import fetch, get_students


SURVEY_DATA_PATH = sys.argv[1]
OUTPUT_PATH = sys.argv[2]


if __name__ == '__main__':
    students = get_students(SURVEY_DATA_PATH)
    with open(OUTPUT_PATH, 'w') as csvfile:
        resultwriter = csv.writer(csvfile)
        # this matches the grading spreadsheet template provided by CMS
        resultwriter.writerow(["NetID", "Grade", "Add Comments"])
        submitted_net_ids = []
        for net_id in students:
            print('-------')
            website, response = fetch(net_id)
            print (website)

            if response is None:
                print("WARNING: no valid website for the assign.")
                '''web = score = 0
                #comment = 'Website available : {website}/50, Return right time : {score}/50'.format(website=web, score=score)
                #resultwriter.writerow([net_id, 0, comment])'''
                continue

            score, comment = grader.grade(response)

            resultwriter.writerow([net_id, score, comment])
            print (score, comment)
            submitted_net_ids.append(net_id)

        print('-------')
        print("Number of submissions:", len(submitted_net_ids))
