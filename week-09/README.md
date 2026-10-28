### 서준혁 (학번 20231331, AI 빅데이터학과)

## 1. 무엇을 하는 코드인가
KOBIS(영화진흥위원회) 오픈API로 일별 박스오피스를 조회합니다.
- `get_boxoffice_rank_1(date)`: 해당 날짜 1위 영화 제목을 반환
- `get_movie_audience(date, movie_name)`: 해당 날짜 영화의 관객 수를 반환 (예: `186,587명`)

## 2. 설치 방법
1. KOBIS 오픈API에서 API 키를 발급받습니다.
2. `week-09/secret.py` 파일을 만들고 키를 넣습니다.
   ```python
   API_KEY = "발급받은_키"
   ```
3. 가상환경을 만들고 의존성을 설치합니다.
   ```bash
   python3 -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   ```

## 3. 실행 방법
```bash
python3 main.py
```
