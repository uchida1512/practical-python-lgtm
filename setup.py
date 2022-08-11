# Python プログラムをコマンドとして実行するには、setup.py を用意して
# インストールする必要がある。
# なお、お手本のコードは「https://github.com/rhoboro/lgtm」にあり。
from setuptools import find_packages, setup


setup(
    name='lgtm',
    version='1.0.0',
    packages=find_packages(exclude=('test',)),
    install_requires=[
        'Click~=7.0',
        'Pillow~=6.2.1',
        'requests~=2.22.0',
    ],
    # entry_points では、console_scripts キーを使って、スクリプトインタフェースの
    # 登録を行っている。
    # console_scripts キーにスクリプトインタフェースを登録すると、そのインタフェースを
    # 呼び出すためのスクリプトがインストール中に自動で作成される。
    entry_points={
        'console_scripts': [
            'lgtm=lgtm.core:cli'
        ]
    }
)

# a@DESKTOP-M8KF2FB MINGW64 ~/PycharmProjects/pythonProject/practical-python-lgtm (main)
# $ pip list
# Package    Version
# ---------- ---------
# certifi    2022.6.15
# chardet    3.0.4
# Click      7.0
# idna       2.8
# Pillow     6.2.1
# pip        22.2.1
# requests   2.22.0
# setuptools 63.3.0
# urllib3    1.25.11


# lgtm コマンドを登録
# a@DESKTOP-M8KF2FB MINGW64 ~/PycharmProjects/pythonProject/practical-python-lgtm (main)
# $ pip install -e .
# Obtaining file:///C:/Users/a/PycharmProjects/pythonProject/practical-python-lgtm
#   Preparing metadata (setup.py) ... done
# （中略）
# Installing collected packages: lgtm
#   Running setup.py develop for lgtm
# Successfully installed lgtm-1.0.0


# a@DESKTOP-M8KF2FB MINGW64 ~/PycharmProjects/pythonProject/practical-python-lgtm (main)
# $ pip list
# Package    Version   Editable project location
# ---------- --------- --------------------------------------------------------------
# certifi    2022.6.15
# chardet    3.0.4
# Click      7.0
# idna       2.8
# lgtm       1.0.0     c:\users\a\pycharmprojects\pythonproject\practical-python-lgtm
# Pillow     6.2.1
# pip        22.2.1
# requests   2.22.0
# setuptools 63.3.0
# urllib3    1.25.11


# a@DESKTOP-M8KF2FB MINGW64 ~/PycharmProjects/pythonProject/practical-python-lgtm (main)
# $ lgtm
# Usage: lgtm [OPTIONS] KEYWORD
# Try "lgtm --help" for help.
#
# Error: Missing argument "KEYWORD".


# a@DESKTOP-M8KF2FB MINGW64 ~/PycharmProjects/pythonProject/practical-python-lgtm (main)
# $ lgtm book
# ok!