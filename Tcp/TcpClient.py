import asyncio

async def send_messages(writer):
    while True:
        message = await asyncio.to_thread(input, "You: ")
        if message.lower() in {"quit", "exit"}:
            print("Closing connection...")
            writer.close()
            await writer.wait_closed()
            break
        writer.write(message.encode())
        await writer.drain()

async def receive_messages(reader):
    while True:
        data = await reader.readline()
        if not data:
            print("Server closed connection.")
            break
        print(f"Server: {data.decode().strip()}")

async def main():
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)
    print("Connected to the server. Type messages or 'quit' to exit.")

    send_task = asyncio.create_task(send_messages(writer))
    recv_task = asyncio.create_task(receive_messages(reader))

    await asyncio.wait([send_task, recv_task], return_when=asyncio.FIRST_COMPLETED)

if __name__ == "__main__":
    asyncio.run(main())
