import justpy as jp

from webapp.home import Home
from webapp.about import About
from webapp.dictionary import Dictionary

if __name__ == "__main__":
    jp.Route(Home.path, Home.server)
    jp.Route(About.path, About.server)
    jp.Route(Dictionary.path, Dictionary.server)
    jp.justpy(port=8081)
