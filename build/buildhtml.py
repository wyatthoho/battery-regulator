import time
from pathlib import Path

from bs4 import BeautifulSoup
from markdown.extensions.tables import TableExtension
import markdown


ENCODING = 'UTF-8'
BS4_PARSER = 'html.parser'
IMG_ALT_MESSAGE = 'Please login intranet.'
HTML_TEMPLATE = 'build/html_template.html'
IMG_HOST_URL = '//10.0.0.23/rd/Thermal&Adv Engineering/CAE/battery-regulator/images/'
FAVICON_URL = '//10.0.0.23/rd/Thermal&Adv Engineering/CAE/battery-regulator/images/xm-logo.ico'
TGT_DIR, IMG_EXT = '../images/', '.png'
HTML_DIR, HTML_EXT = 'html', '.html'


def convert_img_to_label(soup: BeautifulSoup):
    for img_tag in soup.find_all('img'):
        label_tag = soup.new_tag('label')
        img_tag.wrap(label_tag)
        input_tag = soup.new_tag('input', type='checkbox')
        label_tag.insert(0, input_tag)


def replace_img_link(line: str) -> str:
    if 'img alt="" src=' in line:
        query = f'.png?{int(time.time())}'
        return line\
            .replace('alt=""', f'alt="{IMG_ALT_MESSAGE}"')\
            .replace(TGT_DIR, IMG_HOST_URL)\
            .replace(IMG_EXT, query)
    return line


def transform_md_to_html(path_md: Path) -> str:
    with path_md.open('r', encoding=ENCODING) as f:
        contents_md = f.read()
    return markdown.markdown(
        contents_md,
        tab_length=2,
        extensions=[TableExtension(use_align_attribute=True), 'fenced_code']
    )


def insert_title(soup: BeautifulSoup):
    head = soup.find('head')
    h1 = soup.find('h1')
    title = soup.new_tag('title')
    title.string = f'XING | CAE Documents | {h1.string}'
    link = soup.new_tag('link', rel='icon', type='image/x-icon', href=FAVICON_URL)
    head.insert(0, title)
    head.insert(1, link)


def main(path_md: Path):
    body_str = replace_img_link(transform_md_to_html(path_md))
    body_soup = BeautifulSoup(body_str, BS4_PARSER)
    convert_img_to_label(body_soup)

    with Path(HTML_TEMPLATE).open('r', encoding=ENCODING) as f:
        soup = BeautifulSoup(f, BS4_PARSER)
    soup.body.append(body_soup)
    insert_title(soup)

    path_html = Path(HTML_DIR).joinpath(path_md.stem).with_suffix(HTML_EXT)
    with path_html.open('w', encoding=ENCODING) as f:
        f.write(str(soup))
