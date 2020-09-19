import io

filename = input("Enter the filename: ");
with open(filename) as f:
    content = f.read().splitlines()

    output = "\n".join(" ".join(two_lines) \
                       for two_lines in zip(content[::2], content[1::2])) + (
                 content[-1] if len(content) % 2 != 0 else '')


with open(r'C:\Users\johani1\PycharmProjects\solr-query-config\prod_acl_output.log', "w") as out:
    out.write(output)