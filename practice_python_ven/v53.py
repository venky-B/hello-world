import textwrap

if __name__ == "__main__":
    ss = input()
    size  =int(input())
    wrapper = textwrap.TextWrapper(width=size)
    abc = wrapper.wrap(text = ss)
    for i in abc:
        print(i)