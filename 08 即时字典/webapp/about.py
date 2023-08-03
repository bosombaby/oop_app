import justpy as jp


class About:
    path = "/about"

    def server(self):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(classes="mt-48 w-1/2 mx-auto text-center", a=wp)
        jp.Div(text="This is About Page", classes="text-2xl font-bold", a=div)
        jp.Div(
            text="Once upon a time, there was a young man named Jack who lived in a small town. "
            "Jack was a kind and hardworking person, but he had never been in love before. "
            "One day, he met a beautiful young woman named Lily, who had just moved to town. "
            "Jack was immediately smitten with her and they began to spend time together.",
            classes="text-xl",
            a=div,
        )

        return wp


if __name__ == "__main__":
    jp.Route(About.path, About.server)
    jp.justpy(port=8081)
