# encoding: utf-8

# create date: 15/5/17
# project name: markdown_to_html
# script name: main
# author: Tong
# function:

__author__ = 'Tong'


import sys

def markdown_to_html(file_name, out_name='result.html'):
    markdown_js = ''
    with open('markdown-it.js') as f:
        markdown_js = f.read().decode('utf-8')

    markdown_css = ''
    with open('github-markdown.css') as f:
        markdown_css = f.read().decode('utf-8')

    markdown_content = ''
    with open(file_name) as f:
        markdown_content = f.read().decode('utf-8')

    replace_table = [('\\', '\\\\'),
                     ('\r\n', '\\n'), ('\n', '\\n'),
                     ('\"', '\\\"'), ('\'', '\\\'')]
    for i in replace_table:
        markdown_content = markdown_content.replace(i[0], i[1])

    html = '<!DOCTYPE html>' \
           '<html><head>' \
           '<meta http-equiv="Content-Type" ' \
           'content="text/html; charset=utf-8" /> ' \
           '<style>' + '.markdown-body{ min-width: 200px; max-width: 790px; ' \
           'margin: 0 auto; padding: 30px;}' + markdown_css + '</style>' \
           '<script type="text/javascript">' + markdown_js + '</script>' \
           '</head><body>' \
           '<article class="markdown-body"><script type="text/javascript">' \
           'var md = markdownit();var result = ' \
           'md.render(\'' + markdown_content + '\');document.write(result);' \
           '</script></article></body></html>'

    with open(out_name, 'w') as f:
        f.write(html.encode('utf-8'))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'usage: python2 markdown_to_html file_name'

    file_name = sys.argv[1]

    markdown_to_html(file_name)