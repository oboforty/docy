from eme.entities import loadConfig
from eme.website import WebsiteApp


class ExampleWebsite(WebsiteApp):


    def __init__(self):
        # eme/examples/simple_website is the working directory.
        conf = loadConfig('webapp/config.ini')

        super().__init__(conf)


if __name__ == "__main__":
    app = ExampleWebsite()
    app.start()

# Uncomment this for wsgi, so that app.start is only called if the devs run the local version:
# app = ExampleWebsite()
# if __name__ == "__main__":
#     app.start()

