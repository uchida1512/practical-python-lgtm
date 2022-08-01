# core.py が今回作成するツールのエントリポイント
import click


# Click パッケージで作成するコマンドラインツールは、
# デコレータclick.command() を付けた関数を呼び出すと実行できる
@click.command()
def cli():
    """LGTM 画像作成ツール"""
    lgtm()
    # 動作確認用
    click.echo('lgtm')


def lgtm():
    # ここにロジック(処理)を追加していく
    pass