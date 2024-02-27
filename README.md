# 프로그래머스 과제관 
> [Skill_Check_Assignments](https://programmers.co.kr/skill_check_assignments)<br>

## [ML/DL]
- 채용공고 추천 (2021.04.16)
  - [[블로그](https://velog.io/@joniekwon/프로그래머스-과제관-채용-공고-추천-EDA-및-전처리)] [[전체코드](https://github.com/joniekwon/programmers_skill_check_assignments/blob/main/%EC%B1%84%EC%9A%A9%EA%B3%B5%EA%B3%A0%EC%B6%94%EC%B2%9C/20220422%20%EC%B1%84%EC%9A%A9%EA%B3%B5%EA%B3%A0%EC%B6%94%EC%B2%9C_EDA%20%26%20%EB%AA%A8%EB%8D%B8.ipynb)]
- 미술작품 분류 (2022.02.13) 
  - [[제출코드](https://github.com/joniekwon/programers-assignments/blob/main/artpaintings_classification/artpaintings_classification_fastai.ipynb)]
  - LB 88.57142857142857

## [Practica_competency_task]New_type(BE)
- Flask를 이용한 API 구현
  - 고객이름을 이용한 예약 조회
    - 쿼리가 "all"일 경우 모든 예약 정보를 체크인 날짜 기준 오름차순 정렬 후 결과 반환
      ```
      search_results = sorted(search_results, key=lambda x: x["check_in"])
    - 고객 이름 대소문자 구분, 포함된 알파벳이 있는 결과 모두 반환
      ```
      for i, resv in enumerate(reservation):
          if customer_name in resv["customer_name"]:
            search_results.append(reservation[i])
    - 잘못 된 요청 시 에러처리
      ```
      try:
        ...
      except Exception:
        return jsonify({"error":"Invalid data format"}), 400
