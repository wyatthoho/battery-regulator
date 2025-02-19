import time
from typing import List

from bs4 import BeautifulSoup
from markdown.extensions.tables import TableExtension
import markdown

HTML_TEMPLATE = '.\\build\\html_template.html'
BS4_PARSER = 'html.parser'
IMG_ALT_MESSAGE = 'Please login Xing\'s SharePoint using your current browser to view this image.'
IMG_HOST_URL = '//10.0.0.23/rd/Thermal&Adv Engineering/CAE/battery-regulator/images'
LOGO_URL = '//10.0.0.23/rd/Thermal&Adv Engineering/CAE/battery-regulator/images/xm-logo.ico'
QUERY = f'.png?{int(time.time())}'


def convert_img_to_label(soup: BeautifulSoup):
    for img_tag in soup.find_all('img'):
        label_tag = soup.new_tag('label')
        img_tag.wrap(label_tag)
        input_tag = soup.new_tag('input', type='checkbox')
        label_tag.insert(0, input_tag)


def replace_img_link(line: str) -> str:
    if 'img alt="" src=' in line:
        return line\
            .replace('alt=""', f'alt="{IMG_ALT_MESSAGE}"')\
            .replace('../images', IMG_HOST_URL)\
            .replace('.png', QUERY)
    return line


def transform_md_to_html(path_md: str) -> str:
    with open(path_md, 'r', encoding='UTF-8') as f:
        contents_md = f.read()
    extensions = [
        TableExtension(use_align_attribute=True),
        'fenced_code'
    ]
    contents_html = markdown.markdown(
        contents_md,
        tab_length=2,
        extensions=extensions
    )
    return contents_html


def main(md_paths: List[str]):
    for path_md in md_paths:
        with open(HTML_TEMPLATE, 'r') as f:
            soup = BeautifulSoup(f, BS4_PARSER)

        body_str = replace_img_link(transform_md_to_html(path_md))
        body_soup = BeautifulSoup(body_str, BS4_PARSER)
        convert_img_to_label(body_soup)
        soup.body.append(body_soup)
        path_html = path_md\
            .replace('.\\markdown\\', '.\\html\\')\
                .replace('.md', '.html')
        
        head = soup.find('head')
        h1 = soup.find('h1')
        title = soup.new_tag('title')
        title.string = ' | '.join(['XING', 'CAE Documents', h1.string])
        link = soup.new_tag('link', rel='icon', type='image/x-icon', href=LOGO_URL)
        head.insert(0, title)
        head.insert(1, link)

        with open(path_html, 'w', encoding='UTF-8') as f:
            f.write(str(soup))
