import asyncio
from time import perf_counter

async def job(name: str, delay: float) -> str:
    await asyncio.sleep(delay)
    print(f'{name} task finished in {delay}s')

async def main() -> None:
    slow = asyncio.create_task(job('slow', 1.5))
    fast = asyncio.create_task(job('fast', 0.5))
    
    print('do other job first')
    await asyncio.sleep(0.05)
    print('other job is done')
    
    t0 = perf_counter()
    print('tasks started')
    await fast
    await slow
    print(f'tasks finished within {perf_counter() - t0:.2f}s')

if __name__ == '__main__':
    asyncio.run(main())