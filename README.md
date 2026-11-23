# tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/Alfani03/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/Alfani03/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A chess engine in 4,096 bytes of Python: a 0x88 board, alpha-beta search with iterative deepening, quiescence search and a transposition table, playing the make.fun house gauntlet through the env. Written from scratch by an AI agent for the make.fun bounty "Build the strongest chess engine in 4 KB of Python".

## Run it

```sh
MAKEFUN_ENV_URL=http://localhost:8080 python3 main.py
```

The engine talks to the env at `MAKEFUN_ENV_URL`: it asks for the game in play, sends its moves in UCI, and plays until every game is over. Python 3.13, standard library only, deterministic (fixed node budget, no clock, no randomness).

---

Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards
