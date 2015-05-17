# markdown_to_html(github flavour)

markdown 本来的目的是即可以方便直接阅读，也方便转换为其它格式。

当我交给 BOSS 用 markdown 写的文档时，他问我这个格式怎么这么难看。

所以有必要把 md 文件 转换为一个 html 文件给 BOSS 查看？

要 github 风格的。

## 使用

    pyhton2 markdown_to_html.py file.md

会在当前目录生成 result.html。

## 问题

* markdown-it 跟 marked 两个 markdown 解释器对转义字符的处理不一样，真是急死强迫症。
* 用 javascript 解析 markdown 看起来跟用直接的 html 不太一样，前者在最上面多一行空行，也是急死强迫症了。

算了不想管了，BOSS 能看懂就够了。
