import os
from pathlib import Path

PORT = int(os.environ.get("PORT", 5000))
WORKERS = int(os.environ.get("WEB_CONCURRENCY", 1))
DEBUG = bool(os.environ.get("DEBUG", False))

if "DOMAIN" in os.environ:  # staging / production
    SERVER_NAME = os.environ["DOMAIN"]
    IMAGES_URL = f"https://{SERVER_NAME}"
    API_SCHEMES = ["https"]
elif "HEROKU_APP_NAME" in os.environ:  # review apps
    SERVER_NAME = os.environ["HEROKU_APP_NAME"] + ".herokuapp.com"
    IMAGES_URL = f"https://{SERVER_NAME}"
    API_SCHEMES = ["https"]
else:  # localhost
    SERVER_NAME = f"localhost:{PORT}"
    IMAGES_URL = "https://memegen-link-v2.herokuapp.com"
    API_SCHEMES = ["http", "https"]

ROOT_DIRECTORY = Path(__file__).parent.parent.resolve()
FONTS_DIRECTORY = ROOT_DIRECTORY / "fonts"
FONT = FONTS_DIRECTORY / "TitilliumWeb-Black.ttf"

SHOW_TEXT_BOXES = False
TEST_IMAGES_DIRECTORY = ROOT_DIRECTORY / "app" / "tests" / "images"
TEST_IMAGES = [
    ("iw", ["tests code", "in production"]),
    ("unknown", ["unknown template"]),
    ("sparta", ["", "this is sparta!"]),
    (
        "ski",
        [
            "if you try to put a bunch more text than can possibly fit on a meme",
            "you're gonna have a bad time",
        ],
    ),
    ("fry", ["a", "b"]),
    ("fry", ["short line", "longer line of text than the short one"]),
    ("fry", ["longer line of text than the short one", "short line"]),
]