import asyncio
import time

async def greet(name: str, delay: float) -> str:
    print(f"[{time.strftime('%H:%M:%S')}] start {name}")
    await asyncio.sleep(delay)
    print(f"[{time.strftime('%H:%M:%S')}] done {name}")
    return f"hello {name}"

async def sequential() -> None:
    t0 = time.perf_counter()
    await greet('Alice', 1.0)
    await greet('Ben', 1.5)
    await greet('Jack', 2.3)
    print(f'sequential total: {time.perf_counter() - t0:.2f}s\n')

async def concurrent() -> None:
    t0 = time.perf_counter()
    res = await asyncio.gather(
        greet('Alice', 3.0),
        greet('Ben', 1.5),
        greet('Jack', 2.3)
    )
    print(f'concurrent total: {time.perf_counter() - t0:.2f}s\n')
    print(f'result: {res}')
    

async def main() -> None:
    await sequential()
    await concurrent()

if __name__ == '__main__':
    asyncio.run(main())