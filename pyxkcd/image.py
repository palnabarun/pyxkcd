from term_image.image import from_url


def render_from_url(url: str):
    image = from_url(url)
    image.draw()
