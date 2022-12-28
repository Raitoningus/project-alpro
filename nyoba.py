import urllib.request


class Muhammadiyah:
    def __init__(self, url):
        self.url = url

    def urlweb(self):
        response = urllib.request.urlopen(self.url)
        self.data = response.read()


muhammadiyah = Muhammadiyah("https://www.muhammadiyah.or.id/")
muhammadiyah.urlweb()
print(muhammadiyah.data)
