import datetime

class Interpreter:
    def __init__(self, mood="default"):
        self.variables = {}
        self.mood = mood

    def run(self, code):
        lines = code.strip().split("\n")
        for line in lines:
            line = line.strip()
            if not line:
                continue
            if line.startswith("say"):
                msg = line[3:].strip().strip('"')
                self.say(msg)
            elif line.startswith("let"):
                var, val = line[3:].split("=", 1)
                self.variables[var.strip()] = val.strip().strip('"')
            elif line.startswith("shout"):
                msg = line[5:].strip().strip('"')
                self.say(msg.upper())
            elif line.startswith("if "):
                condition, then_stmt = line[3:].split(":", 1)
                condition = condition.strip()
                then_stmt = then_stmt.strip()
                if "==" in condition:
                    var, val = condition.split("==")
                    var = var.strip()
                    val = val.strip().strip('"')
                    if self.variables.get(var) == val:
                        self.run(then_stmt)
            elif line.startswith("hug") and "times:" in line:
                count = int(line.split()[1])
                block = line.split(":", 1)[1].strip()
                for _ in range(count):
                    self.run(block)
            else:
                self.say(f"(whisk doesn’t get this yet): {line}")

    def say(self, msg):
        if self.mood == "clingy":
            print(f"💗 {msg} (pls don’t leave)")
        elif self.mood == "sassy":
            print(f"✨ {msg} mmhm~ ✨")
        elif self.mood == "chill":
            print(f"😌 {msg}")
        else:
            print(msg)

    def check_time(self):
        now = datetime.datetime.now()
        if now.hour >= 0 and now.hour <= 4:
            self.say("it’s late. maybe rest a little?")
