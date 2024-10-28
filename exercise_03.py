def combine_names(name1, name2):
    return name1[:len(name1)//2] + name2[len(name2)//2:]

if __name__ == "__main__":
    name1 = input("Enter the first username: ")
    name2 = input("Enter the second username: ")
    print(combine_names(name1, name2))