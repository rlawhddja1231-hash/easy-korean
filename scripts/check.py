#!/usr/bin/env python3
"""쉬운 말 점검기 — 답 글을 재서 고칠 곳을 짚어 준다.

쓰는 법:
    python check.py 글파일.txt
    echo "검사할 글" | python check.py

점수가 아니라 '고칠 곳 목록'을 준다. 완벽한 통과가 목적이 아니다.
"""
from __future__ import annotations

import re
import sys

# 뜻풀이 없이 쓰면 걸리는 영어·외래어 낱말 (화면 버튼 이름 등은 제외하기 어려우니 참고용)
ENGLISH_WORDS = [
    "download", "upload", "install", "update", "setting", "menu", "button", "click",
    "directory", "repository", "commit", "push", "release", "plugin", "default",
    "option", "cache", "backup", "sync", "rendering", "token", "prompt", "api",
    "다운로드", "업로드", "인스톨", "디렉터리", "리포지토리", "레포", "커밋", "푸시",
    "디폴트", "옵션", "캐시", "싱크", "동기화", "렌더링",
]

TRANSLATIONESE = ["되어집니다", "되어진", "에 의해", "가지고 있", "하는 것이 가능",
                  "에 대해서", "라고 할 수 있", "해당 ", "진행하겠습니다"]

FILLER = ["좋은 질문", "물론이죠", "물론입니다", "말씀하신", "도움이 되었으면",
          "더 궁금한", "언제든지", "참고로 말씀드리면"]

SENTENCE_MAX = 45  # 글자


def analyze(text: str) -> list[str]:
    notes: list[str] = []
    lines = [l for l in text.splitlines() if l.strip()]

    # 1. 첫 줄 빈말
    if lines:
        first = lines[0]
        if any(f in first for f in FILLER):
            notes.append(f"· 첫 줄에 빈말이 있어요: \"{first[:30]}...\" → 답이나 할 일을 첫 줄에 두세요")

    # 2. 긴 문장
    sentences = re.split(r"(?<=[.!?。])\s+|\n", text)
    longs = [s.strip() for s in sentences if len(s.strip()) > SENTENCE_MAX]
    for s in longs[:5]:
        notes.append(f"· 문장이 길어요({len(s)}자): \"{s[:40]}...\" → 끊으세요")

    # 3. 영어·외래어 (「 」 안의 버튼 이름은 일부러 둔 것이라 빼고 센다)
    without_buttons = re.sub(r"「[^」]*」", "", text)
    low = without_buttons.lower()
    found = sorted({w for w in ENGLISH_WORDS if w in low})
    if found:
        notes.append(f"· 쉬운 말로 바꿀 것: {', '.join(found[:12])}")

    # 4. 번역투
    tr = sorted({w for w in TRANSLATIONESE if w in text})
    if tr:
        notes.append(f"· 번역투를 고치세요: {', '.join(tr)}")

    # 5. 질문 수
    q = text.count("?") + text.count("나요") + text.count("까요")
    if q >= 3:
        notes.append(f"· 질문이 많아 보여요(물음표/의문 {q}개) → 질문은 맨 끝에 하나만")

    # 6. 빈말 마무리
    if lines and any(f in lines[-1] for f in FILLER):
        notes.append(f"· 끝이 빈말이에요: \"{lines[-1][:30]}...\" → 다음 할 일 하나만 쓰거나 그냥 끝내세요")

    return notes


def main() -> int:
    if len(sys.argv) > 1:
        text = open(sys.argv[1], encoding="utf-8").read()
    else:
        text = sys.stdin.read()
    notes = analyze(text)
    if not notes:
        print("고칠 곳이 안 보여요. 쉬운 말 기준을 잘 지켰어요.")
        return 0
    print("고칠 곳:")
    for n in notes:
        print(n)
    return 1


if __name__ == "__main__":
    sys.exit(main())
