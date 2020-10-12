# # 1. 파일 쓰기( r: 읽기 모드, w:쓰기 모드, a:추가 모드)
# f = open('새파일.txt', 'w', encoding = 'utf-8') #현재 폴더에 새파일.txt가 있으면 열고 없으면 만들어서 연다
# f.write('Hello File\n')
# f.write('안녕하세요.')
# f.close()

# # 2.반복문으로 5줄 파일에 작성하기
# f = open('새파일.txt', 'w', encoding = 'utf-8')
# for i in range(1,6):
#     f.write(f'{i}번째 줄입니다.\n')
# f.close

# # 3. 파일에 내용 추가하기
# f = open('새파일.txt', 'w', encoding = 'utf-8')
# for i in range(6, 11):
#     f.write(f'{i}번째 줄입니다.\n')
# f.close

# # 4.파일 한 줄 읽기
# f = open('새파일.txt', 'r', encoding = 'utf-8')
# print(f.readline())
# print(f.readline())
# f.close()

# 5.파일 여러 줄 읽기
#f = open('새파일.txt', 'r', encoding = 'utf-8')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line, end = ' ')
# f.close()

# for line in f.readlines():
#     print(line, end = ' ')
# f.close()

# # 6.파일 전체 내용 읽기
# f = open('새파일.txt', 'r', encoding = 'utf-8')
# print(f.read()) # 파일 전체 내용을 하나의 문자열로 반환한다.
# f.close()

# 7. with문의 사용 (자동으로 파일닫기)
with open('새파일.txt', 'r', encoding = 'utf-8') as f:
    print(f.read())







