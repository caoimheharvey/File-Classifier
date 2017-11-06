import os, hashlib
def findDupes(startDir):
    seen = {}
    stack = [startDir]
    dupes = []

    while len(stack):
        current = stack.pop()
        if os.path.isdir(current):
            for path in os.listdir(current):
                full = os.path.join(current, path)
                stack.append(full)
        else:
            hashed = hashing(current)
            if hashed in seen:
                existing = seen[hashed]
                dupes.append((existing, current))
            else:
                seen[hashed] = current
    print(dupes)
    return dupes

def hashing(path):
    hasher = hashlib.md5()

    with open(path, 'rb') as file:
        hasher.update(file.read())
        return hasher.hexdigest()

findDupes("./")
