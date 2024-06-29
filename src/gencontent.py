"""Module to generate html files"""

# pylint: disable=line-too-long


from block_markdown import markdown_to_html


def generate_page(from_path, template_path, dest_path):
    """Function to generate an html file from a markdown file"""
    print(
        f"***** Generating page from {from_path} to {dest_path} using {template_path} *****"
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
