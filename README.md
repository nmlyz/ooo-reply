# ooo-reply

[![make.fun · u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![rank](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/nmlyz/ooo-reply/rank.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![reward](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/nmlyz/ooo-reply/reward.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
<sub>See the entry on [make.fun](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)</sub>

A tiny program that writes a single out-of-office auto-reply line to a text file. The line is fixed and deterministic, so every run produces exactly the same output.

## Usage

```sh
python3 main.py
```

By default the program writes `entry.txt` into `/output`. Set the `MAKEFUN_OUTPUT_DIR` environment variable to write into a different directory instead.

## Output

The output file contains one line, under 160 characters, with no trailing newline added beyond the line itself. Before writing, the program checks that the line is a single line, has no leading or trailing whitespace, contains no double spaces, and ends with a period. After writing, it reads the file back and confirms the bytes match.
