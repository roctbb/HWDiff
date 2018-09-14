import difflib
import requests


def get_text(file):
    with open(file) as f:
        text = f.read()
    return text


def make_comparison(text1, text2):
    main = text1.split('\n')
    result = difflib.ndiff(main, text2.split('\n'))

    same = 0

    for line in result:
        if line[0] == " ":
            same += 1

    return same / len(main)


def download(url):
    return requests.get(url).text


'''
files = ['files/file1.txt', 'files/file2.txt']
'''

files = list(open('tasks.txt').read().split('\n'))

for i in range(len(files)):
    main = download(files[i])

    for j in range(i + 1, len(files)):
        comparison_file = files[j]

        comparison = download(comparison_file)
        result = make_comparison(main, comparison)

        if result > 0.3:
            print("alert on line {} to {}: {} vs {} - {}".format(i + 1, j + 1, files[i], comparison_file, result))

print("DONE")
