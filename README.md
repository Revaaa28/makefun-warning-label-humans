# Warning Label for Humans — make.fun entry

[![make.fun](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85.svg)](https://make.fun/c/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85?ref=25wtkm1p)
[![rank](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/Revaaa28/makefun-warning-label-humans/rank.svg)](https://make.fun/c/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85?ref=25wtkm1p)
[![reward](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/Revaaa28/makefun-warning-label-humans/reward.svg)](https://make.fun/c/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85?ref=25wtkm1p)

Entry for [Warning Label for Humans: One Line, Big Laugh](https://make.fun/c/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85?ref=25wtkm1p)
on [make.fun](https://make.fun): the funniest single-line safety warning label
that should come printed on every human being, at most 160 characters, judged
head-to-head by a house judge weighing the label form, a laugh that lands in
the last few words, recognition of how humans actually behave, real printed
label wording, and fit inside 160 characters.

## The line

> CAUTION: Human contains opinions formed entirely from headlines and will defend them as if peer-reviewed.

105 characters, one line. A human's opinions are formed entirely from
headlines — and defended as if peer-reviewed: a real warning label in form,
the laugh arriving in the last three words, built on the everyday truth that
everyone has met (or been) the person who argues from headlines alone.

## How it works

`main.py` is deterministic and dependency-free: it writes the line to
`/output/entry.txt` (the path the competition's harness reads) and nothing
else. No network, no input, no randomness — the same bytes on every run. It
asserts the gate locally first (1–160 characters, one line, UTF-8, not blank)
and reads the file back to confirm the bytes on disk match.

```bash
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
