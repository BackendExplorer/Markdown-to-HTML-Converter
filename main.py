import sys
import os
import markdown

# Markdown を HTML に変換
def markdown_to_html(input_path, output_path):
    with open(input_path, 'r') as infile:
        text = infile.read()
    html = markdown.markdown(
        text,
        extensions=["extra", "codehilite", "sane_lists", "toc"]
    )
    with open(output_path, 'w') as outfile:
        outfile.write(html)


def main(argv):
    # 引数の個数チェック
    if len(argv) != 4:
        sys.stdout.buffer.write(
            b"Wrong usage!\nusage: python3 file-converter.py markdown inputfile outputfile\n"
        )
        sys.exit(1)

    command = argv[1]
    input_path = argv[2]
    output_path = argv[3]

    # コマンドチェック
    if command != 'markdown':
        sys.stdout.buffer.write(b"Command not found...\n")
        sys.exit(1)

    # ファイル存在チェック
    if not os.path.exists(input_path):
        sys.stdout.buffer.write(b"Input file does not exist...\n")
        sys.exit(1)

    # 拡張子チェック
    if not (input_path.endswith('.md') and output_path.endswith('.html')):
        sys.stdout.buffer.write(b"Invalid file type: input should be .md and output should be .html\n")
        sys.exit(1)

    # 変換処理
    markdown_to_html(input_path, output_path)


if __name__ == '__main__':
    main(sys.argv)
