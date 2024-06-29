"""Module to generate html files"""

# pylint: disable=line-too-long

import os

from block_markdown import markdown_to_html


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    """Recursive function to generate htmls files from markdown files"""
    dir_list = os.listdir(dir_path_content)
    for file in dir_list:
        file_path = os.path.join(dir_path_content, file)
        if not os.path.isfile(file_path):
            new_dir = os.path.join(dest_dir_path, file)
            print(f"***** Creating --> {new_dir} directory *****")
            os.mkdir(new_dir)
            generate_pages_recursive(
                file_path, template_path, os.path.join(dest_dir_path, file)
            )
        if os.path.isfile(file_path):
            generate_page(
                os.path.join(dir_path_content, file),
                template_path,
                os.path.join(dest_dir_path, "index.html"),
            )


def generate_page(from_path, template_path, dest_path):
    """Function to generate an html file from a markdown file"""
    print(
        f"***** Generating page from {from_path} --> {dest_path} using {template_path} *****"
    )
    with open(from_path, "r", encoding="utf-8") as f:
        md = f.read()
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()
    html = markdown_to_html(md).to_html()
    title = extract_title(md)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(template)


def extract_title(markdown):
    """Function to get the title from the H1 in the markdown file"""
    md_list = markdown.split("\n", 1)
    if md_list[0].startswith("# "):
        title = md_list[0][2:]
        return title
    raise ValueError("Markdown document must begin with an H1 heading")
