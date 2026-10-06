class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split("/")
        stack = []

        for ele in path_list:
            if ele == '..':
                if stack:
                    stack.pop()
            elif ele == '.' or ele == '' :
                continue
            else:
                stack.append(ele)

        return "/" + "/".join(stack)
