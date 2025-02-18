import os

import buildhtml


def get_md_paths(src_path: str = '.\\markdown') -> list:
    md_paths = [
        os.path.join(src_path, path)
        for path in os.listdir(src_path) if path.endswith('.md')
    ]
    return md_paths


def main() -> None:
    md_paths = get_md_paths()
    buildhtml.main(md_paths)


if __name__ == '__main__':
    main()
