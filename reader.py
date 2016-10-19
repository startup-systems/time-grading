import urllib2
import csv


def fetch(net_id):
    """Returns the URL, the response, and the corresponding score."""
    website = 'https://' + net_id + '-time.herokuapp.com'
    try:
        response = urllib2.urlopen(website).read()
    except urllib2.HTTPError:
        response = None
    return website, response


def get_students(filepath):
    net_ids = []
    with open(filepath, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        reader.next()
        for row in reader:
            net_ids.append(row[3])
    return net_ids
