import urllib as url

def open_and_check():
    file = open("quotes.txt")
    contents = file.read()
    # print(contents)
    file.close()
    check_profanity(contents)

def check_profanity(text_to_check):
    connection = url.urlopen("http://www.wdylike.appspot.com/?q=shot" + text_to_check)
    result = connection.read()
    print result
    connection.close()


open_and_check()