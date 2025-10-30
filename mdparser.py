from frontmatter import Frontmatter


d = Frontmatter.read._file("제육볶음.md")


print(f"{d['attributes']}")
