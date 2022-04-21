# Built ins
import json

class DataStack():
    def __init__(self) -> None:
        self.stack = []

    def pushData(self, data) -> None:
        self.stack.append(data)

    def popData(self, data) -> dict:
        popped_data = self.stack.pop()
        return popped_data

    def writeToFile(self, filename) -> None:
        try:
            l = len(self.stack)
            with open(filename, "w") as f:
                json.dump(self.stack, f)
            self.stack = []
            status = 0
        except Exception as e:
            print(e)
            l = 0
            status = 1
        
        finally:
            return f"{l} records written to {filename}...", status
        