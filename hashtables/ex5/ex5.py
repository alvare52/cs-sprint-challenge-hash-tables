# Your code here
import pathlib


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    pathsDict = {}
    queriesDict = {}

    # fill in pathsDict with every item in array
    for value in files:
        path = pathlib.PurePath(value).name
        
        # value = "home/david/foo.txt"
        # path = "foo.txt"

        # if key DOESN'T exist yet
        if path not in pathsDict:
            pathsDict[path] = [value]

        # else, key is already present, so just add value to it's value arra
        else:
            # print(f"path dupe {value}")
            pathsDict[path].append(value)
        
    
    # for query in queries:
    #     queriesDict[query] = query

    for query in queries:
        # if "foo" in "/bin/foo"
        if query in pathsDict:
            for value in pathsDict[query]:
                result.append(value)
            # result.append(query)
    
    # print(f"pathsDict = {pathsDict}")
    # print(f"queriesDict = {queriesDict}")

    return result


if __name__ == "__main__":
    # files = [
    #     '/bin/foo',
    #     '/bin/bar',
    #     '/usr/bin/baz'
    # ]
    files = [
    "/usr/local/share/foo.txt",
    "/usr/bin/ls",
    "/home/davidlightman/foo.txt",
    "/bin/su"
    ]
    # queries = [
    #     "foo",
    #     "qux",
    #     "baz"
    # ]
    queries = [
    "ls",
    "foo.txt",
    "nosuchfile.txt"
    ]
    print(finder(files, queries))

# Given a list of full paths to files, and a list of filenames to query,
# report all the full paths that match that filename.

# Example input:

# ```python
# paths = [
#     "/usr/local/share/foo.txt",
#     "/usr/bin/ls",
#     "/home/davidlightman/foo.txt",
#     "/bin/su"
# ]

# queries = [
#     "ls",
#     "foo.txt",
#     "nosuchfile.txt"
# ]
# ```

# Example return value:

# ```
# [ "/usr/local/share/foo.txt", "/usr/bin/ls", "/home/davidlightman/foo.txt" ]
# ```

# because that's where the `foo.txt` and `ls` files are. 

# The file `"nosuchfile.txt"` is ignored because it's not in the `paths`.