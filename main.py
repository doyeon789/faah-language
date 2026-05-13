import sys

def run_file(path: str):
    pass


if __name__ == '__main__':
    args = sys.args[1:]

    # -- <= 콘솔 명령어 나중에 만들기 위해서
    # -- 제외한 파일 불러오기
    files= [a for a in args if not a.startswith('--')]

    run_file(files)