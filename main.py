import os

def save_info(filename, info):
    with open(filename, 'a') as file:
        file.write(info + "\n")

def load_info(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return file.readlines()
    return []

# 정보 저장 예제
save_info('info_repository.txt', '이것은 첫 번째 정보입니다.')
save_info('info_repository.txt', '이것은 두 번째 정보입니다.')

# 정보 불러오기 예제
all_info = load_info('info_repository.txt')
for line in all_info:
    print(line.strip())
