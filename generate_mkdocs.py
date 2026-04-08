import os
import yaml
import re


def get_markdown_files(docs_dir='docs'):
    """扫描 docs 目录获取所有 markdown 文件"""
    nav_structure = []

    for root, dirs, files in os.walk(docs_dir):
        # 排除隐藏文件夹和 __pycache__
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']

        rel_path = os.path.relpath(root, docs_dir)

        for file in sorted(files):
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                rel_file_path = os.path.relpath(file_path, docs_dir)

                # 获取文件名（不带扩展名）作为标题
                title = os.path.splitext(file)[0]
                # 清理文件名，去掉序号前缀等
                title = re.sub(r'^\d+[\.\-_]\s*', '', title)

                nav_structure.append({
                    'path': rel_file_path.replace('\\', '/'),
                    'title': title,
                    'folder': rel_path if rel_path != '.' else ''
                })

    return nav_structure


def build_nav_tree(files):
    """将文件列表构建为嵌套的导航结构"""
    tree = {}

    for item in files:
        path_parts = item['path'].split('/')
        current_level = tree

        for i, part in enumerate(path_parts[:-1]):
            if part not in current_level:
                current_level[part] = {}
            current_level = current_level[part]

        # 添加文件
        file_name = path_parts[-1]
        current_level[file_name] = {
            '_title': item['title'],
            '_path': item['path']
        }

    return tree


def tree_to_nav_list(tree, docs_dir='docs'):
    """将树结构转换为 MkDocs nav 格式"""
    nav = []

    for key in sorted(tree.keys()):
        value = tree[key]
        # 如果是文件夹（dict 且没有 _path）
        if isinstance(value, dict) and '_path' not in value:
            folder_name = key.replace('-', ' ').replace('_', ' ').title()

            # 查找文件夹内的 index.md 或 README.md
            index_file = None
            children = []

            for sub_key, sub_value in value.items():
                if isinstance(sub_value, dict) and '_path' in sub_value:
                    if sub_key.lower() in ['index.md', 'readme.md']:
                        index_file = sub_value['_path']
                    else:
                        children.append({sub_value['_title']: sub_value['_path']})
                else:
                    # 递归处理子文件夹
                    sub_nav = tree_to_nav_list({sub_key: sub_value}, docs_dir)
                    children.extend(sub_nav)

            if index_file:
                nav.append({folder_name: [index_file] + children})
            elif children:
                nav.append({folder_name: children})
        else:
            # 根目录的文件
            if '_path' in value and value['_path'].lower() not in ['index.md', 'readme.md']:
                nav.append({value['_title']: value['_path']})
            elif '_path' in value:
                # 首页放最前面
                nav.insert(0, {'首页': value['_path']})

    return nav


def generate_mkdocs():
    """生成完整的 mkdocs.yml"""

    # 基础配置
    config = {
        'site_name': '爬虫逆向文章库',
        'site_description': '记录爬虫逆向、Android逆向、VM防护等技术文章',
        'site_author': 'sunxiang',
        'site_url': 'https://sunxiang.github.io/and/',

        'repo_name': 'GitHub',
        'repo_url': 'https://github.com/sunxiang/and',
        'edit_uri': 'edit/main/docs/',

        'copyright': 'Copyright &copy; 2026 sunxiang',
        'docs_dir': 'docs',

        'theme': {
            'name': 'material',
            'language': 'zh',
            'palette': [
                {
                    'media': '(prefers-color-scheme: light)',
                    'scheme': 'default',
                    'primary': 'teal',
                    'accent': 'teal',
                    'toggle': {
                        'icon': 'material/brightness-7',
                        'name': '切换到深色模式'
                    }
                },
                {
                    'media': '(prefers-color-scheme: dark)',
                    'scheme': 'slate',
                    'primary': 'teal',
                    'accent': 'teal',
                    'toggle': {
                        'icon': 'material/brightness-4',
                        'name': '切换到浅色模式'
                    }
                }
            ],
            'features': [
                'navigation.tabs',
                'navigation.sections',
                'navigation.expand',
                'navigation.top',
                'search.suggest',
                'search.highlight',
                'content.code.copy'
            ],
            'icon': {
                'logo': 'material/spider'
            }
        },

        'plugins': [
            {'search': {'lang': ['zh']}},
            'awesome-pages'  # 自动生成剩余导航
        ],

        'markdown_extensions': [
            'admonition',
            'pymdownx.details',
            'pymdownx.superfences',
            {'pymdownx.highlight': {'anchor_linenums': True}},
            'pymdownx.inlinehilite',
            {'pymdownx.tabbed': {'alternate_style': True}},
            'tables',
            {'toc': {'permalink': True}}
        ],

        'extra_css': ['extra.css']
    }

    # 扫描文件生成导航
    if os.path.exists('docs'):
        files = get_markdown_files('docs')
        if files:
            tree = build_nav_tree(files)
            nav = tree_to_nav_list(tree)
            if nav:
                config['nav'] = nav

    # 写入文件
    with open('mkdocs.yml', 'w', encoding='utf-8') as f:
        yaml.dump(config, f, allow_unicode=True, sort_keys=False, default_flow_style=False)

    print("✅ 已生成 mkdocs.yml")
    print("🚀 运行 'mkdocs serve' 预览效果")


if __name__ == '__main__':
    generate_mkdocs()