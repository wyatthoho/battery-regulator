from pathlib import Path

import buildhtml


MD_DIR = 'markdown'
MD_PATTERN = '*.md'


def main() -> None:
    md_paths = Path(MD_DIR).glob(MD_PATTERN)
    for path in md_paths:
        buildhtml.main(path)


if __name__ == '__main__':
    main()
