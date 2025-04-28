import re
import time
from pathlib import Path

import markdown
from bs4 import BeautifulSoup
from markdown.extensions.tables import TableExtension


ENCODING = 'UTF-8'
PARSER = 'html.parser'
IMG_ALT_TEXT = 'Please login intranet.'
HTML_TEMPLATE_PATH = 'build/html_template.html'
IMG_SERVER_URL = '//10.0.0.23/rd/Thermal&Adv Engineering/CAE/battery-regulator/images/'
FAVICON_PATH = '//10.0.0.23/rd/Thermal&Adv Engineering/CAE/battery-regulator/images/xm-logo.ico'
IMAGE_DIR = '../images/'
IMAGE_EXT = '.png'
OUTPUT_DIR = 'html'
OUTPUT_EXT = '.html'


def extract_latex_expressions(text: str) -> list[str]:
    pattern = r'\$\$(.+?)\$\$|\$(.+?)\$'
    matches = re.finditer(pattern, text, flags=re.DOTALL)
    return [(m.group(1) or m.group(2)).strip() for m in matches]


def markdown_to_html(text: str) -> str:
    return markdown.markdown(
        text,
        tab_length=2,
        extensions=[TableExtension(use_align_attribute=True), 'fenced_code']
    )


def update_image_links(html: str) -> str:
    if 'img alt="" src=' in html:
        timestamp = f'.png?{int(time.time())}'
        return (
            html.replace('alt=""', f'alt="{IMG_ALT_TEXT}"')
                .replace(IMAGE_DIR, IMG_SERVER_URL)
                .replace(IMAGE_EXT, timestamp)
        )
    return html


def wrap_images_with_labels(soup: BeautifulSoup) -> None:
    for img in soup.find_all('img'):
        label = soup.new_tag('label')
        img.wrap(label)
        checkbox = soup.new_tag('input', type='checkbox')
        label.insert(0, checkbox)


def set_html_title(soup: BeautifulSoup) -> None:
    head = soup.find('head')
    title_text = soup.find('h1').string if soup.find('h1') else 'Document'
    title_tag = soup.new_tag('title')
    title_tag.string = f'XING | CAE Documents | {title_text}'
    favicon_tag = soup.new_tag('link', rel='icon', type='image/x-icon', href=FAVICON_PATH)
    head.insert(0, title_tag)
    head.insert(1, favicon_tag)


def replace_latex_in_html(html: str, expressions: list[str]) -> str:
    pattern = r'\$\$(.+?)\$\$|\$(.+?)\$'
    matches = list(re.finditer(pattern, html, flags=re.DOTALL))

    if len(matches) != len(expressions):
        raise ValueError(f"Found {len(matches)} math placeholders but {len(expressions)} expressions.")

    for match, expr in zip(reversed(matches), reversed(expressions)):
        start, end = match.span()
        delimiter_start = '\\[' if match.group(1) else '\\('
        delimiter_end = '\\]' if match.group(1) else '\\)'
        html = html[:start] + f"{delimiter_start}{expr}{delimiter_end}" + html[end:]

    return html


def main(path: Path) -> None:
    text_md = path.read_text(encoding=ENCODING)

    expressions = extract_latex_expressions(text_md)
    body_html = markdown_to_html(text_md)
    body_html = update_image_links(body_html)
    body_soup = BeautifulSoup(body_html, PARSER)
    wrap_images_with_labels(body_soup)

    template_soup = BeautifulSoup(Path(HTML_TEMPLATE_PATH).read_text(encoding=ENCODING), PARSER)
    template_soup.body.append(body_soup)
    set_html_title(template_soup)

    final_html = replace_latex_in_html(str(template_soup), expressions)

    output_path = Path(OUTPUT_DIR).joinpath(path.stem).with_suffix(OUTPUT_EXT)
    output_path.write_text(final_html, encoding=ENCODING)

