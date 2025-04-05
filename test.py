from asyncio import run, gather, sleep, create_task
import aiohttp
from loapy import LostArkRest
from loapy.types import armories, characters
import time
import threading

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IktYMk40TkRDSTJ5NTA5NWpjTWk5TllqY2lyZyIsImtpZCI6IktYMk40TkRDSTJ5NTA5NWpjTWk5TllqY2lyZyJ9.eyJpc3MiOiJodHRwczovL2x1ZHkuZ2FtZS5vbnN0b3ZlLmNvbSIsImF1ZCI6Imh0dHBzOi8vbHVkeS5nYW1lLm9uc3RvdmUuY29tL3Jlc291cmNlcyIsImNsaWVudF9pZCI6IjEwMDAwMDAwMDA1NzI4MzEifQ.nKPohnEdb_tJ6JlDGsrWatIMT-nNsoUssE6cHUnNBEFwfkIiMnrqGAK2TQSDvP2It_rEpcEfIWNYbMu8vJSf9u-p4SrY6lxaQov3SZeRH6AdRl2kOjwHsDsiW_sQm8vQtufz5tSX9P3HLGZhxcPWqIDBvqod6ZIzuiORg4Gb_QkYCue2yZbf46xcTS01dlSY0ynew2c6R4Y7kNpwIdedJX1JGULCt0VnkXYg8LbvkLmr1BIhoPDzaIpcUXlE_qyptqvHuwUSc2g_GNtuaySBzqsVPGbuZameELqPnXTVFc7GeQ_PPSyFIBbGOLygx_A_HYxqg5YE5O1VJ46XYJCe0A"
lostark = LostArkRest(token)

com_start_time = time.time()

async def main() -> None:
	print(
		await lostark.fetch_events()
	)

	print(
		await lostark.fetch_character("데런자연", combat_skills=False, colosseums=False, collectibles=False, avatars=False)
	)
	print("0 process time :", time.time() - com_start_time)


async def aiohttp_req_profile(name):
	async with aiohttp.ClientSession() as session:
		async with session.get(
			url=f"https://developer-lostark.game.onstove.com/armories/characters/{name}/profiles",
			headers={
                    "Accept": "application/json",
                    "Authorization": f"Bearer {token}",
					}
			) as response:
			if response.status == 200:
				print(await response.text())
			
def thp():
	run(aiohttp_req_profile("데런자연"))
"""
try:
	p = time.time()
	
	print("데런자연 요청")
	# th0 = threading.Thread(target=thp)
	# th0.setDaemon(True)
	# th0.start()
	run(aiohttp_req_profile("데런자연"))
	print("자연화가 요청")
	run(aiohttp_req_profile("자연화가"))
	print(time.time() - p)
except Exception as e:
	print("에러 발생 :", e)
"""

async def aiohttp_main0():
	async with aiohttp.ClientSession() as session:
		async with session.get('http://python.org') as response:

			print("Status:", response.status)
			print("Content-type:", response.headers['content-type'])

			html = await response.text()
			print("Body:", html[:15], "...")
			print("0 process time :", time.time() - com_start_time)
			

async def aiohttp_main1():
	async with aiohttp.ClientSession() as session:
		async with session.get('http://python.org') as response:

			print("Status:", response.status)
			print("Content-type:", response.headers['content-type'])

			html = await response.text()
			print("Body:", html[:15], "...")
			print("0 process time :", time.time() - com_start_time)
			
			
async def aiohttp_main2():
	async with aiohttp.ClientSession() as session:
		async with session.get('http://python.org') as response:

			print("Status:", response.status)
			print("Content-type:", response.headers['content-type'])

			html = await response.text()
			print("Body:", html[:15], "...")
			print("0 process time :", time.time() - com_start_time)

if False:
	run(aiohttp_main0())
	run(aiohttp_main1())
	run(aiohttp_main2())
"""
async def fetch(session, url):
	print(url, "요청 처리")
	async with session.get(url) as response:
		print(url, "응답 수신")
		return await response.json()  # JSON 응답 처리

async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]  # 여러 요청을 동시에 실행할 태스크 생성
        return await gather(*tasks)  # 모든 태스크 병렬 실행

# 실행할 URL 목록
urls = [
    "https://jsonplaceholder.typicode.com/todos/1",
    "https://jsonplaceholder.typicode.com/todos/2",
    "https://jsonplaceholder.typicode.com/todos/3"
]

# 메인 비동기 실행
async def fetch_main():
    results = await fetch_all(urls)
    for result in results:
        print(result)

run(fetch_main())
"""
"""
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()

async def main():
    urls = [
        "https://jsonplaceholder.typicode.com/todos/1",
        "https://jsonplaceholder.typicode.com/todos/2",
        "https://jsonplaceholder.typicode.com/todos/3",
        "https://jsonplaceholder.typicode.com/todos/4"
    ]
    
    async with aiohttp.ClientSession() as session:
        tasks = [create_task(fetch(session, url)) for url in urls]  # 각각의 요청을 병렬 실행
        results = await gather(*tasks)  # 모든 요청 완료 대기

    for result in results:
        print(result)

run(main())
"""

async def main():
	characters = ["데런자연", "자연화가", "자연격파"]
	"""gather에서 쓰는 *arg 에 대한 테스트
	>>> a = [1, 2, 3]
	>>> *a
	File "<stdin>", line 1
	SyntaxError: can't use starred expression here
	>>> a
	[1, 2, 3]
	>>> *a
	File "<stdin>", line 1
	SyntaxError: can't use starred expression here
	>>> def f(*a):
	...     print(a)
	...
	>>> f(a)
	([1, 2, 3],)
	>>> f(*a)
	(1, 2, 3)
	>>> quit()
	"""
	tasks = [create_task(lostark.fetch_character(char, engravings=False ,combat_skills=False, colosseums=False, collectibles=False, avatars=False)) for char in characters]
	results = await gather(*tasks)
	armor_datas = []

	for i, result in enumerate(results):
		# print(characters[i])
		# print(result)
		d: armories.ArmoryProfile = result["ArmoryProfile"]
		e: armories.ArmoryEquipment = result["ArmoryEquipment"]
		
		armor_datas.append((d, e))

	print(len(armor_datas[0][1]))
	for i in armor_datas[0][1]:
		print(f'이름 : {i["Name"]}, 타입 : {i["Type"]}')

run(main())