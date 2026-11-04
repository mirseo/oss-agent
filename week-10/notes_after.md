작성: Claude Code / 확인: (서준혁)

# tools.py 함수 설명 (week-09) 냥 🐱

- KOBIS(영화진흥위원회) 오픈 API의 일별 박스오피스(`searchDailyBoxOfficeList.json`)를 호출해서 영화 정보를 가져오는 모듈이다냥
- API 키는 `secret.py`의 `API_KEY`에서 불러온다냥
- HTTP 요청은 `requests`로 보낸다냥

## 모듈 상수

| 이름 | 설명 |
|------|------|
| `BASE_URL` | KOBIS 일별 박스오피스 API 주소다냥 |

## 함수

### `get_movie_audience(date: str, movie_name: str)`

- 역할: 특정 날짜 박스오피스에서 영화 제목에 해당하는 일일 관객수를 알려준다냥
- 입력
  - `date`: 8자리 날짜 문자열이다냥 (예: `"20260824"`)
  - `movie_name`: 영화 제목이다냥 (예: `"오디세이"`)
- 반환: 관객수 문자열이다냥 (예: `"186,587명"`)
- 동작
  1. API를 호출해서 해당 날짜의 박스오피스 목록을 받는다냥
  2. `boxOfficeResult.dailyBoxOfficeList`를 꺼낸다냥
  3. `movieNm`이 `movie_name`과 같은 항목의 `audiCnt`를 천 단위 쉼표 + "명" 형식으로 돌려준다냥
- 오류 처리
  - 순위에 없는 영화는 `"'없는영화' 은(는) 20260824 순위에 없습니다."`를 돌려준다냥
  - `[E0]` 네트워크 요청 실패: 메시지를 출력한다냥
  - `[E1]` 응답 파싱 실패(키 없음): 메시지를 출력하고 `None`을 돌려준다냥
  - `[E2]` 영화 비교 중 오류: 메시지를 출력한다냥

### `get_boxoffice_rank_1(date)`

- 역할: 특정 날짜 박스오피스 1위 영화 제목을 알려준다냥
- 입력: `date` - 8자리 날짜 문자열이다냥 (예: `"20260824"`)
- 반환: 1위 영화 제목 문자열이다냥 (예: `"오디세이"`)
- 동작: API를 호출하고 `dailyBoxOfficeList` 첫 번째 항목의 `movieNm`을 돌려준다냥
- 오류 처리: 없다냥 (네트워크 실패나 응답 형식 오류면 예외가 그대로 터진다냥)

## 개선 후보

- `get_movie_audience`: `[E0]`가 나도 `return` 하지 않아서 `data`가 없어 `NameError`가 날 수 있다냥
- `[E1]` 메시지의 `dailyBoxOfficeList2`는 실제 키(`dailyBoxOfficeList`)와 달라서 오타로 보인다냥
- 예외 처리가 전부 bare `except:`라서 원인 찾기 어렵다냥
- `get_boxoffice_rank_1`: 예외 처리가 없고 docstring 예시 날짜의 따옴표도 안 닫혀 있다냥
- `__main__` 블록: 예시가 전부 주석 처리돼 있어서 직접 실행해도 아무 일도 안 한다냥
