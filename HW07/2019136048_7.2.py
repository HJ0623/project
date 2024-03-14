M = 13                  # 해시 테이블의 크기
table = [None]*M        # 해시 테이블. 모든 항목은 None으로 초기화
def hashFn(key) :     # 해시 함수로는 제산함수 사용
    return key% M

def insert(key) :
    i = hashFn(key)
    count = M
    while count>0 :
        if table[i] == None or table[i] == -1 :
#       
            break               # 삽입 위치 발견
        i = (i + 1) % M         # 다음위치 조사
        count -= 1

    if count > 0 :              # 삽입할 곳이 있으면 삽입
        table[i] = key

# 코드 7.13: 선형조사법의 탐색 연산
def search(key) :
    i = hashFn(key)
    count = M
    while count>0 :
        if table[i] == None :   # 탐색 실패
            return None
        if table[i] == key :    # 탐색 성공
            return table[i]
        i = (i + 1) % M
        count -= 1

    return None                 # 탐색 실패


# 코드 7.14: 선형조사법의 삭제 연산
def delete(key) :
    i = hashFn(key)
    count = M
    while count>0 :
        if table[i] == key :    # 삭제할 레코드 발견
            table[i] = -1
#            table[i] = None
            return
        if table[i] == None :   # 삭제할 레코드 없음
            return
        i = (i + 1) % M
        count -= 1


if __name__ == "__main__":
   
    data = [45, 27, 88, 9, 71, 60, 77, 38, 99]
    
    # 삽입 연산
    for d in data:
        print("삽입 %2d (hash=%2d):" % (d, hashFn(d)), end=' ')
        insert(d)
        print(table)

    # 탐색 연산
    print("\n탐색 연산:")
    search_data = [46, 39, 27, 88]
    for d in search_data:
        result = search(d)
        if result is not None:
            print(f"{d} 찾았습니다: {result}")
        else:
            print(f"{d} 못 찾았습니다")

    # 삭제 연산
    delete_data = [60, 71]
    for d in delete_data:
        print(f"\n삭제 {d}:", end=' ')
        delete(d)
        print(table)
