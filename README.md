# 쉬운 말 (easy-korean)

영어와 컴퓨터 용어를 몰라도 바로 알아듣게, Claude가 **쉬운 한국어**로 답하게 만드는 스킬이에요.

AI 답은 영어 용어가 많고 문장이 길어서, 영어를 모르면 답을 봐도 뭘 해야 할지 모를 때가 많아요. 이 스킬은 Claude가 **할 일을 먼저 말하고, 영어를 우리말로 풀고, 물을 건 선택지로 하나씩 묻게** 바꿔 줘요.

## 무엇이 바뀌나

**전**
> 해당 파일은 GitHub repository의 Releases 탭에서 다운로드 가능합니다.

**후**
> 파일은 깃허브 보관함의 「Releases」(내놓은 판) 탭에서 내려받아요.
> 1. 「Releases」를 누르세요. (오른쪽에 있어요)
> 2. 받을 파일을 누르면 내려받아져요.

더 많은 예시는 [`examples/before-after.md`](examples/before-after.md)에 있어요.

## 담긴 규칙 12가지

1. 결론·할 일을 첫 줄에
2. 영어·전문 용어는 우리말로 (괄호로 뜻)
3. 짧은 문장, 한 문장에 한 가지
4. 따라 하는 순서는 번호로
5. 물을 것은 선택지로 하나씩
6. 질문에는 되묻지 말고 먼저 답하기
7. 읽을 것 먼저, 질문은 마지막
8. 숫자는 감이 오게 (비교 붙이기)
9. 겁주지 않고, 위험은 꼭 알리기
10. 코드·명령어는 통째로
11. 틀렸으면 짧게 인정하고 고친 것 주기
12. 끝은 다음 할 일 하나

## 까는 법 (설치)

### Claude Code (검은 명령 창)에서
```
/plugin marketplace add rlawhddja1231-hash/easy-korean
/plugin install easy-korean@easy-korean
```

### 그냥 복사해서 쓰기
`skills/easy-korean` 폴더를 통째로 자기 `~/.claude/skills/` 안에 넣으면 돼요.

## 끄고 싶을 때

그 대화에서 "쉬운 말 꺼 줘" 또는 "전문가처럼 말해"라고 하면 돼요.

## 들어 있는 것

- `skills/easy-korean/SKILL.md` — 규칙 본체
- `skills/easy-korean/references/terms.md` — 영어 용어를 쉬운 말로 바꾸는 표
- `scripts/check.py` — 답을 재서 고칠 곳을 짚어 주는 도구
- `examples/before-after.md` — 바뀌기 전과 후 예시

## 라이선스

MIT. 마음대로 가져다 쓰고 고쳐도 돼요.
