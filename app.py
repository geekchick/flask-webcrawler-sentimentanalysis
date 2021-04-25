from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def get_links():
    # create empty list called links to hold the urls
    links = []
    # get the request and store into a response variable
    url_response = requests.get('https://xkcd.com/')

    # if the response is 200-400 then proceed:
    if url_response:
        # get the url
        # add url to the links list
        links.append('https://xkcd.com/')
        # get the message body from the response obj
        text = url_response.text
    # else if the response is >= 400 then break
    else:
        return "This is an error"

    # start = 0, end = length of text
    start, end = 0, len(text)

    # while there is something in links
    while True:
        # get each url on the page
        # look for '<a href=' and extract the url by doing a find
        # start_link = text.find('<a href=', start, end) -> this is where the link starts
        start_link = text.find('<a href=', start, end)

        if start_link == -1:
            break
        
        # start_quote = text.find('"', start_link, end) -> get the link from where " starts
        start_quote = text.find('"', start_link)
        # end_quote = text.find('"', start_link + 1) -> get the end position of the link
        end_quote = text.find('"', start_quote + 1)
        # append the link to the links list -> links.append(text[start_quote + 1:end_quote])
        links.append(text[start_quote + 1:end_quote])

        # reset start position
        start = end_quote + 1
        

    return render_template('home.html', links=links)