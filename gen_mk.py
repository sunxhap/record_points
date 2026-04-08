# simple_generate.py
import os

content = """site_name: 爬虫逆向文章库
site_url: https://sunxhap.github.io/record_points/
docs_dir: docs

theme:
  name: material
  language: zh
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.expand
    - navigation.top
    - search.suggest
    - content.code.copy

plugins:
  - search:
      lang: zh
  - awesome-pages  # 自动生成所有导航

markdown_extensions:
  - admonition
  - pymdownx.superfences
  - tables
  - toc:
      permalink: true

extra_css:
  - extra.css
"""

with open('mkdocs.yml', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ 已生成极简配置（自动识别所有文件）")