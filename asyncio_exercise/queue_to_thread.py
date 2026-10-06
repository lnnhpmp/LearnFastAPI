from asyncio import run, sleep, Queue, create_task, to_thread, gather
import time

async def producer(q: Queue) -> None:
    for i in range(6):
        await sleep(0.2)
        await q.put(i)
        print(f"  produced {i}")
    await q.put(None)

async def consumer(q: Queue, name: str) -> None:
    while True:
        item = await q.get()
        if item is None:
            await q.put(None)              # pass sentinel to next worker
            break
        await sleep(0.5)           # simulate processing
        print(f"  [{name}] consumed {item}")

def blocking_sum(n: int) -> int:
    # A CPU-bound call that would freeze the loop if awaited directly.
    time.sleep(0.3)
    return sum(range(n))

async def offload_example() -> None:
    print("\n== to_thread (blocking work off the event loop) ==")
    a = create_task(to_thread(blocking_sum, 100_000))
    b = create_task(to_thread(blocking_sum, 100_000))
    print("  loop stayed responsive")
    print(f"  sums: {await a}, {await b}")


async def main() -> None:
    q: Queue = Queue()
    producers = [producer(q)]
    consumers = [consumer(q, "w1"), consumer(q, "w2")]
    await gather(*producers, *consumers)
    await offload_example()
    
if __name__ == '__main__':
    run(main())