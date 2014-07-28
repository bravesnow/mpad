import misaka as md
from misaka import Markdown,HtmlRenderer,SmartyPants
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

class BleepRenderer(HtmlRenderer,SmartyPants):
    def block_code(self, text, lang):
        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % text.strip()
        lexer = get_lexer_by_name(lang,encoding='utf-8',stripall=True)
        formatter = HtmlFormatter(linenos=True,encoding='utf-8',noclasses="True")
        return highlight(text, lexer, formatter)

def mdtohtml(text):
    renderer = BleepRenderer()
    mark = Markdown(renderer,extensions=
                    md.EXT_FENCED_CODE|md.EXT_NO_INTRA_EMPHASIS)
    return mark.render(text)

