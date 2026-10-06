from asyncio import run, sleep, as_completed, gather

async def fetch(i: int, delay: float) -> int:
    await sleep(delay)
    if (i == 2):
        raise ValueError('bad request for 2')
    return i

# asyncio.as_completed returns an iterator that yields awaitables in the order they complete (fastest first), not in the order you passed them.
async def complete_order() -> None:
    print('== as_completed (finish order) ==')
    coros = [fetch(1, 0.8), fetch(2, 0.1), fetch(3, 0.5)]
    for coro in as_completed(coros):
        try:
            res = await coro
            print(f'done -> {res}')
        except ValueError as e:
            print(f'failed -> {e}')

# asyncio.as_completed returns an iterator that yields awaitables in the order they complete (fastest first), not in the order you passed them.

async def gather_with_errors() -> None:
    print("\n== gather (raises on first error) ==")
    try:
        await gather(fetch(1, 0.9), fetch(2, 0.7), fetch(4, 0.2))
    except ValueError as e:
        print(f'gather error -> {e}')
    print("\n== gather(return_exceptions=True) ==") 
    results = await gather(fetch(1, 0.9), fetch(2, 0.7), fetch(4, 0.2), return_exceptions=True)
    for r in results:
        print(f' {type(r).__name__}: {r}')

async def main() -> None:
   await complete_order()
   await gather_with_errors()

if __name__ == '__main__':
    run(main())