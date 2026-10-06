from asyncio import run, sleep, CancelledError, wait_for, timeout

async def slow_op(delay: float) -> str:
    try:
        await sleep(delay)
    except CancelledError as e:
        print(f"    cleanup: closing connection...{e}")
        raise
    return "done"

async def with_wait_for() -> None:
    print("== wait_for (older style) ==")
    try:
        await wait_for(slow_op(5.0), timeout=1.0)
    except TimeoutError:
        print("    timed out")

async def with_timeout() -> None:
    print("\n== asyncio.timeout (context manager, 3.11+) ==")
    try:
        async with timeout(1.0):
            await slow_op(5.0)
    except TimeoutError:
        print("    timed out")
        
async def main() -> None:
    await with_wait_for()
    await with_timeout()
    
if __name__ == '__main__':
    run(main())