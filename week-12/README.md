# boxoffice — KOBIS 박스오피스 조회 스킬

## 하는 일
영화진흥위회(KOBIS) 일별 박스오피스를 조회한다. 특정 날자의 박스오피스 1위 영화나 그 영화의 관객 수를 물을 떄 사용한다.

## 들어 있는 파일
- .claude/skills/boxoffice/SKILL.md
- .claude/skills/boxoffice/scripts/boxoffice.py
- .claude/skills/boxoffice/LICENSE

## 필요한 것
1. 가상 환경
2. requests (파이썬 베이스 패키지)

## 설치
boxoffice 폴더를 프로젝트의 .claude/skills/ 아래에 두고, week-12 폴더에서 claude code를 실행하고, 이후 "20261114 박스오피스 1위 알려줘"와 같이 질의하면 스킬이 자동으로 실행된다.

## 바깥으로 요청하는 곳
영화진흥위원회(KOBIS)의 오픈 API(일별 박스오피스)를 호출한다.
"https://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
이 경로로 API 키와 데이터를 전달하고 전송한다.

## 키
키를 사용하는 방법은 secret.py에서 매개변수 상수로 API_KEY에 담아서 KOBIS API키를 저장하세요

## 권한
allowed-tools는 없고, 실행 시마다 python3 .claude/skills/boxoffice/... 등 직접 파일 경로를 수행하고 bash의 명령 허용 여부를 질의한다.

## 라이선스
MIT 라이선스
파일 위치 : .claude/skills/boxoffice/LICENSE
