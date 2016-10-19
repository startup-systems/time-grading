import time
import re


def handle(data_string):
    score = 0
    result = time.time()  # since epoch in seconds
    alt_result = result * 1000  # in milliseconds
    res = float(data_string)
    if abs(res - result) <= 60 or abs(res - alt_result) <= 60 * 1000:
        score = 50
    return score


def grade(response):

    sci_pattern = re.compile(r'\d+\.?\d*[eE][+-]\d+')
    float_pattern = re.compile(r'\d{10,20}\.\d+')
    int_pattern = re.compile(r'\d{10,20}')
    format_pattern = [sci_pattern, float_pattern, int_pattern]
    score = 0
    for data_format in format_pattern:
        m = re.search(data_format, response)
        if m is None:
            continue
        score = handle(m.group())
        print m.group()
        break

    comment = 'Website available : 50/50; Return right time : {score}/50'.format(score=score)
    total = 50 + score
    return total, comment
