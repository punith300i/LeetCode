class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.rstrip("/").replace("//", "/")
        stack_dir = []

        for item in [p for p in path.split("/") if p]:
            if item == "..":
                try:
                    stack_dir.pop()
                except IndexError:
                    continue
            elif item == ".":
                continue
            else:
                stack_dir.append(item)
        return "/" + "/".join(stack_dir).rstrip("/")