import asyncio


class CustomStatus:
    def __init__(self):
        self.value = "Resume"
        self.condition = asyncio.Condition()
        self.re_sleep_event = asyncio.Event()

    async def set_value(self, new_value):
        async with self.condition:
            self.value = new_value
            self.condition.notify_all()
            print("notify")

    def get_value(self):
        return self.value

    async def wait_for_value(self, target_value):
        async with self.condition:
            print("self.value",self.value)
            print("target_value",target_value)
            await self.condition.wait_for(lambda: self.value == target_value)
        print(f"Value reached {target_value}")

    def trigger_reset(self):
        self.re_sleep_event.set()  # 触发事件

    async def wait_for_re_sleep(self, interval):
        print("wait_for_re_sleep start")
        await asyncio.wait_for(self.re_sleep_event.wait(), timeout=interval)
        print("wait_for_re_sleep end")

    def clear(self):
        self.re_sleep_event.clear()