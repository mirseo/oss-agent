# tools.py 함수 설명 (week-09)

KOBIS(영화진흥위원회) 오픈 API의 **일별 박스오피스**(`searchDailyBoxOfficeList.json`)를 호출해 영화 정보를 가져오는 모듈입니다.
API 키는 `secret.py`의 `API_KEY`에서 불러오고, `requests`로 HTTP 요청을 보냅니다.

## 모듈 상수

| 이름 | 설명 |
|------|------|
| `BASE_URL` | KOBIS 일별 박스오피스 API 주소 |

## 함수 (총 2개)

### `get_movie_audience(date: str, movie_name: str)`

특정 날짜의 박스오피스에서 **영화 제목에 해당하는 일일 관객수**를 알려줍니다.

- **입력**
  - `date`: 8자리 날짜 문자열 (예: `"20260824"`)
  - `movie_name`: 영화 제목 (예: `"오디세이"`)
- **반환**: 관객수 문자열 (예: `"186,587명"`)
- **동작**
  1. API를 호출해 해당 날짜의 박스오피스 목록을 받아옴
  2. `boxOfficeResult.dailyBoxOfficeList`를 꺼냄
  3. 목록에서 `movieNm`이 `movie_name`과 같은 영화를 찾아 `audiCnt`를 천 단위 쉼표 + "명" 형식으로 반환
- **오류 처리**
  - 순위에 없는 영화: `"'없는영화' 은(는) 20260824 순위에 없습니다."` 반환
  - `[E0]` 네트워크 요청 실패 → 메시지 출력
  - `[E1]` 응답 파싱 실패(키 없음) → 메시지 출력 후 `None` 반환
  - `[E2]` 영화 비교 중 오류 → 메시지 출력

### `get_boxoffice_rank_1(date)`

특정 날짜의 **박스오피스 1위 영화 제목**을 알려줍니다.

- **입력**: `date` - 8자리 날짜 문자열 (예: `"20260824"`)
- **반환**: 1위 영화 제목 문자열 (예: `"오디세이"`)
- **동작**: API 호출 후 `dailyBoxOfficeList`의 첫 번째 항목의 `movieNm`을 반환
- **오류 처리**: 없음 (네트워크 실패나 응답 형식 오류 시 예외가 그대로 발생)

## 참고할 점 (개선 후보)

- `get_movie_audience`에서 `[E0]` 네트워크 오류가 나도 `return` 하지 않아, 다음 단계에서 `data`가 정의되지 않아 `NameError`가 날 수 있음
- `[E1]` 메시지의 `dailyBoxOfficeList2`는 실제 키(`dailyBoxOfficeList`)와 달라 오타로 보임
- 예외 처리가 모두 bare `except:`라 원인 파악이 어려움
- `get_boxoffice_rank_1`에는 예외 처리가 없고, docstring의 예시 날짜 따옴표가 닫혀 있지 않음
- `__main__` 블록은 모든 예시가 주석 처리되어 있어 직접 실행해도 아무 일도 하지 않음
