import random
class tag:
    def __init__(self, name: str, command: str, context: str, argsdict: dict):
        self.name = name
        command = command.strip()
        self.choose(command, name, context=context)
        self.context = context
        self.argsdict = {}
        self.functions = {}
        self.argsdict = argsdict

    def randchoice(self):
        def calculate(args: str, argsdict: dict):
            result = random.choice(args.split())
            result = result.replace("_", " ")
            return result
        return calculate

    def string(self):
        def calculate(args: str, argsdict: dict):
            args = args.replace(" ", "_")
            return args
        return calculate

    def setrange(self):
        def calculate(args: str, argsdict: dict):
            args = args.split()
            result = ""
            for i in range(int(args[0]), int(args[1])+1):
                if i != int(args[1]):
                    result += str(i) + " "
                else:
                    result += str(i)
            return result
        return calculate

    def plus(self):
        def calculate(args: str, argsdict:dict):
            args = args.split()
            result = 0
            for arg in args:
                if args[0] == "-":
                    result -= float(arg)
                else:
                    result += float(arg)
            try:
                if result.is_integer():
                    result = int(result)
            except:
                pass
            return result
        return calculate

    def minus(self):
        def calculate(args: str, argsdict:dict):
            args = args.split()
            result = float(args[0]) - float(args[1])
            try:
                if result.is_integer():
                    result = int(result)
            except:
                pass
            return result
        return calculate

    def divide(self):
        def calculate(args: str, argsdict:dict):
            args = args.split()
            result = args[0]
            for arg in args:
                result /= float(arg)
            try:
                if result.is_integer():
                    result = int(result)
            except:
                pass
            return result
        return calculate

    def multiply(self):
        def calculate(args: str, argsdict:dict):
            args = args.split()
            result = 1
            for arg in args:
                result *= float(arg)
            try:
                if result.is_integer():
                    result = int(result)
            except:
                pass
            return result
        return calculate

    def equalplus(self):
        def calculate(args: str, argsdict: dict):
            args = args.split()
            name = args[0]
            value = argsdict.get("%s" % name)
            result = float(value) + float(arg)
            try:
                if result.is_integer():
                    result = int(result)
            except:
                pass
            self.argsdict.update({name: str(result)})
            return result
        return calculate


    def equalminus(self):
        def calculate(args: str, argsdict: dict):
            args = args.split()
            name = args[0]
            value = argsdict.get("%s" % name)
            result = float(value)
            result = value - float(args[1])
            try:
                if result.is_integer():
                    result = int(result)
            except:
                pass
            self.argsdict.update({name: str(result)})
            return result
        return calculate

    def equalmultiply(self):
        def calculate(args: str, argsdict: dict):
            args = args.split()
            name = args[0]
            value = argsdict.get("%s" % name)
            result = 1
            result = float(value) * float(args[1])
            try:
                if result.is_integer():
                    result = int(result)
            except:
                pass
            self.argsdict.update({name: str(result)})
            return result
        return calculate

    def equaldivide(self):
        def calculate(args: str, argsdict:dict):
            args = args.split()
            name = args[0]
            value = argsdict.get("%s" % name)
            result = float(value) / float(args[1])
            try:
                if result.is_integer():
                    result = int(result)
            except:
                pass
            self.argsdict.update({name: str(result)})
            return result
        return calculate


    def selfReturn(self):
        def showContext(args: str, argsdict:dict):
            context = self.context
            result = run(context, args, argsdict)
            return result
        return showContext

    def ifCheck(self):
        def ifChecksemi(args: str, argsdict: dict):
            firstArg = args[0:args.find("equal")].strip()
            if firstArg.find("(") != -1 and firstArg.find(")") == -1:
                firstArg + ")"
            firstArg = run(firstArg, "", argsdict)
            secondArg = args[args.find("equal") + 5:args.find("do")].strip()
            secondArg = run(secondArg, "", argsdict)
            thirdArg = args[args.find("do") + 2:args.find("else")].strip()
            fourthArg = args[args.find("else") + 4:].strip()
            if firstArg == secondArg:
                thirdArg = run(thirdArg, "", argsdict)
                return thirdArg
            else:
                fourthArg = run(fourthArg, "", argsdict)
                return fourthArg
        return ifChecksemi

    def setVariable(self):
        def semi(args: str, argsdict:dict):
            if len(args.split()) > 2:
                line = args.strip()
                args = args.split()
                name = args[0]
                value = line.replace(name + " ", "", 1)
                self.argsdict.update({name:str(value)})
                return ""
            elif len(args.split()) == 2:
                args = args.split()
                name = args[0]
                value = args[1]
                self.argsdict.update({name:str(value)})
                return ""
            else:
                return ""
        return semi

    def callVariable(self):
        return self.argsdict

    def useVariable(self):
        def useVar(args: str, argsdict: dict):
            line = args
            for key in argsdict.keys():
                line = line.replace(key, argsdict[key])
            return line
        return useVar

    def nocommand(self, context: str):
        def message(args, argsdict):
            return context
        return message
    
    def nothing(self):
        def semi(context: str):
            return context
        return semi

    def choose(self, command: str, initargs=(), name="", context=""):
        if command == "+" or command == "plus" or command == "add":
            self.func = self.plus()
        elif command == "-" or command == "minus":
            self.func = self.minus()
        elif command == "*" or command == "multiply":
            self.func = self.multiply()
        elif command == "/" or command == "divide":
            self.func = self.divide()
        elif command == "return":
            self.func = self.selfReturn()
        elif command == "declare" or command == "equal":
            self.func = self.setVariable()
        elif command == "use":
            self.func = self.useVariable()
        elif command == "if":
            self.func = self.ifCheck()
        elif command == "+=":
            self.func = self.equalplus()
        elif command == "-=":
            self.func = self.equalminus()
        elif command == "*=":
            self.func = self.equalmultiply()
        elif command == "/=":
            self.func = self.equaldivide()
        elif command == "randchoice":
            self.func = self.randchoice()
        elif command == "range":
            self.func = self.setrange()
        elif command == "string" or command == "str":
            self.func = self.string()
        else:
            self.func = self.nocommand(context)

    def run(self, args: str, argsdict: dict):
        args = args.strip()
        args = args.replace("(", "", 1)
        args = args[::-1].replace(")", "", 1)[::-1]
        args = args.strip()
        if len(args.split()) > 1:
            args = args.replace(args.split()[0], "", 1)
        return self.func(args, argsdict)
        


def nameParse(rawline):
    rawline = rawline.replace("디피 maketag ", "", 1)
    name = rawline.split()[0]
    return name

def checkDepth(rawline):
    move = 0
    depth = 0
    depthList = []
    for letter in rawline:
        move += 1
        if letter == '(':
            depth += 1
            depthList.append(depth)
        elif letter == ')':
            depthList.append(depth)
            depth -= 1
        else:
            depthList.append(-1)
    return depthList

def declareschecker(rawline, num=0):
    if rawline.find('(declare') != -1:
        rawline = rawline.replace('(declare', "", 1)
        return declareschecker(rawline, num+1)
    else:
        return num

def run(rawline: str, args="", argsdict={}):
    rawline = rawline.strip()
    rawline = rawline.replace("input", args)
    if len(rawline.split()) <= 1:
        return rawline
    else:
        if rawline.find("디피 maketag ") != -1:
            rawline = rawline.replace("디피 maketag ", "", 1)
            Name = nameParse(rawline)
            rawline = rawline.replace(Name + " ", "", 1)
        else:
            Name = ""
        depthList = checkDepth(rawline)
        if len(depthList) == 0:
            return rawline
        if max(depthList) == -1:
            return rawline
        elif max(depthList) != -1:
            if True:
                semiTag = rawline[:depthList.index(1, depthList.index(1) + 1) + 1]
                if rawline.find("(if") == 0 or rawline.find("(declare") == 0:
                    mode = semiTag[1:-1].split()[0]
                    Tag = tag(Name, mode, semiTag, argsdict)
                    argsdict.update(Tag.argsdict)
                    result = Tag.run(semiTag, argsdict)
                    argsdict.update(Tag.argsdict)
                    rawline = rawline.replace(semiTag, result, 1)
                    return run(rawline, args, argsdict)
                startnumsemi = checkDepth(semiTag).index(
                        max(checkDepth(semiTag)))
                endnumsemi = checkDepth(semiTag).index(
                        max(checkDepth(semiTag)), startnumsemi+1)
                useTag = semiTag[startnumsemi:endnumsemi+1]
                mode = useTag[1:-1].split()[0]
                Tag = tag(Name, mode, useTag, argsdict)
                result = Tag.run(useTag, argsdict)
                argsdict.update(Tag.argsdict)
                Temptag = semiTag.replace(useTag, str(result), 1)
                rawline = rawline.replace(semiTag, Temptag, 1)
                return run(rawline, args, argsdict)
        else:
            return rawline
