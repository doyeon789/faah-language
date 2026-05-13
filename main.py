import sys

def run_file(path: str):
    
    try:
        source = open(path, encoding='utf-8').read()
    except FileNotFoundError:
        print(f"[ERRPR] Can't find files: {path}" )

    # Lexing <- 문법 패턴 관리

    # Parshing <- 코드가져오기

    # Interpreting <- 인터프린팅




if __name__ == '__main__':
    args = sys.args[1:]

    # -- <= 콘솔 명령어 나중에 만들기 위해서
    # -- 제외한 파일 불러오기
    files= [a for a in args if not a.startswith('--')]

    run_file(files)