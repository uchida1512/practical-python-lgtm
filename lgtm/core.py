# core.py が今回作成するツールのエントリポイント
import click
from lgtm.drawer import save_with_message
from lgtm.image_source import get_image


# Click パッケージで作成するコマンドラインツールは、
# デコレータ click.command() を付けた関数を呼び出すと実行できる。
# また、デコレータ click.option() で、オプションで渡すものを指定し
# デコレータ click.argument() で、位置引数で渡すものを指定する。
@click.command()
@click.option('--message', '-m', default='LGTM', show_default=True, help='画像に乗せる文字列')
@click.argument('keyword')
def cli(keyword, message):
    """LGTM 画像作成ツール"""
    lgtm(keyword, message)
    # 動作確認用
    click.echo('ok!')


def lgtm(keyword, massage):
    # get_image() 関数を利用して画像を取得し、
    # 取得した画像と引数で受け取ったメッセージの文字列を save_with_message() 関数に渡す。
    with get_image(keyword) as fp:
        save_with_message(fp, massage)
    pass


# a@DESKTOP-M8KF2FB MINGW64 ~/PycharmProjects/pythonProject/practical-python-lgtm (main)
# $ python main.py --help
# Usage: main.py [OPTIONS] KEYWORD
#
#   LGTM 画像作成ツール
#
# Options:
#   -m, --message TEXT  画像に乗せる文字列  [default: LGTM]
#   --help              Show this message and exit.

# a@DESKTOP-M8KF2FB MINGW64 ~/PycharmProjects/pythonProject/practical-python-lgtm (main)
# $ python main.py book
# ok!
