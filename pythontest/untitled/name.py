# !/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="feijigame",
    version="1.0",
    packages=find_packages(),

    description="feijigame",
    long_description="feijigame",
    author="zhouzhipeng",
    author_email="542945190@qq.com",

    license="GPL",
    keywords=("feijigame", "game"),
    platforms="Independant",
    url=" ",
    entry_points={
        'console_scripts': [
            'setupdemo = fejitest.playgame:main'
        ]
    }
)







def main():
    pass
if __name__ == '__main__':
    main()
