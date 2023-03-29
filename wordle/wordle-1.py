#读取文件
def read_words_from_file(file_path):
    with open(file_path) as f:
        return set(f.read().splitlines())

#单词过滤
def filter_words(words, cmd, pos=None):
    if cmd[0] == "+":
        for c in cmd[1:]:
            if pos is not None:
                words = {w for w in words if w[pos] == c}
            else:
                words = {w for w in words if c in w}
    elif cmd[0] == "-":
        for c in cmd[1:]:
            if pos is not None:
                words = {w for w in words if w[pos] != c}
            else:
                words = {w for w in words if c not in w}
    return words

#判断命令格式是否正确
def is_valid_cmd(cmd):
    if len(cmd) < 2 or not cmd[1:].isalpha():
        return False
    if cmd[0] not in "+-":
        return False
    return True

#单词列表
def print_word_list(words, show_list=False):
    print()
    print(len(words))
    print("Total:", len(words))

    if show_list and words:
        print("Word_list:", words)

    # 输出前三个个单词
    words_list = list(words)
    if len(words_list) > 0:
        print("First word:", words_list[0])
    if len(words_list) > 1:
        print("Second word:", words_list[1])
    if len(words_list) > 2:
        print("Third word:", words_list[2])


#无限循环等待输入
def main():
    file_path = "wordle.txt"
    words = read_words_from_file(file_path)
    pos = None

    while True:
        cmd = input("输入(+A/-A): ")
        if not is_valid_cmd(cmd):
            print("输入有误，需要输入+A/-A.")
            continue
        pos_input = input("输入位置(1-5): ")
        if pos_input:
            pos = int(pos_input) - 1
            if pos < 0 or pos > 4:
                print("需要输入数字在1-5之间")
                continue
        else:
            pos = None
        
        words = filter_words(words, cmd, pos)
        if len(words) < 20:
            print_word_list(words, show_list=True)
        else:
            print_word_list(words)
            first_word = next(iter(words))

if __name__ == '__main__':
    main()

