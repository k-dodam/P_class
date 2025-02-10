'''
값이 학생들이 좋아하는 과목 리스트인 딕셔너리 생성 (2가지)

"어떤 과목을 좋아하는 학생을 찾을까요?" > 과목 입력받기
"(학생 이름)이 (과목 이름)과목을 좋아합니다." 출력
'''

subject = {
    "민지" : ["국어", "영어"],
    "보민" : ["수학", "사회"],
    "승아" : ["과학", "체육"],
    "연우" : ["국어", "영어", "수학", "사회", "과학", "체육"]
}
found = False # 과목 발견 여부 저장
subject_input = input("어떤 과목을 좋아하는 학생을 찾을까요? : ")
for i,j in subject.items():
    if subject_input in j:
        print(f"{i} 학생이 {subject_input} 과목을 좋아합니다.")
        found = True

if not found :
    print(f"{subject_input} 과목은 존재하지 않는 과목입니다.")