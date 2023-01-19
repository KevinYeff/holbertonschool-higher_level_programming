#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    hideContent = dir(hidden_4)
    for hideNames in hideContent:
        if hideNames[0:1] != "_":
            print(hideNames)
