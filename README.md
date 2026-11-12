# tiny-chess-01

A chess engine in at most 4,096 bytes of Python, written for the
make.fun bounty "Build the strongest chess engine in 4 KB of Python".

`main.py` is the whole engine: a 0x88 board, negamax alpha-beta search
with quiescence (captures, plus all evasions when in check) and MVV
move ordering. It searches to a fixed node budget (150,000 nodes a
move), never a clock, so replays play the same moves. It talks to the
trial env at `MAKEFUN_ENV_URL` (`POST /game`, `POST /move`) and plays
the 8-game house gauntlet.

Notes: en passant captures are not generated (rare, saves bytes);
there is no transposition table and no repetition detection in search
(both cut for size/correctness). Promotions are queen-only.

## Files

- `main.py` — the engine (Python 3.13, standard library only)
- `LICENSE` — MIT

## Run it

Set `MAKEFUN_ENV_URL` to the trial env and run `python3 main.py`.
