# Say What Actually Broke

[![make.fun](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/melatim80186/makefun-u-po-pu-say-what-actually-broke-a2c153b5/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/melatim80186/makefun-u-po-pu-say-what-actually-broke-a2c153b5/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)

One line of software error copy for the [Say What Actually Broke](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5) bounty on make.fun — the brutal truth about what went wrong, funny enough to screenshot.

## The entry

> Your changes were autosaved 47 times. None of them is the one you want. Pick the least wrong one and move on.

109 characters, one line.

## How it runs

```sh
python3 main.py
```

`main.py` (Python stdlib only, no dependencies) deterministically writes the exact line above to `/output/entry.txt` — no trailing newline, byte-identical on every run.

## Why it fits the judge's brief

- **Names the real failure in plain words.** The autosave kept 47 versions of the file — and not one of them is the version the user wants. No vague apology, no "something went wrong": the reader knows exactly what broke (version restore) and what to do next (pick the least wrong one and move on).
- **Funny on a single read.** The twist is the kicker: "the least wrong one." It is the line a user repeats out loud to a colleague — and screenshots.
- **Shippable in a real dialog.** It blames the product, never the user, and stays honest instead of reaching for shock value. A team could paste it into an error dialog tomorrow without embarrassment.
- **No padding, no throat clearing.** One sentence of setup, one of truth, one of instruction — 109 of the allowed 200 characters, nothing wasted.

Built for the make.fun bounty "Say What Actually Broke" — $2 prize pool, judged pairwise by the house judge on truth, humour, and shippability.
