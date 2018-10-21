class tag:
    def __init__(self, name: str, command: str, context: str, argsdict: dict):
        self.name = name
        print("커맨드", command)
        command = command.strip()
        self.choose(command, name, context=context)
        self.context = context
        self.argsdict = {}
        self.functions = {}
        self.argsdict = argsdict

    def plus(self):
        def calculate(args: str, argsdict:dict):
            print(args)
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
            result = 0
            for arg in args:
                result -= float(arg)
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
            print("이퀄플러스", args)
            args = args.split()
            name = args[0]
            print(argsdict)
            print(self.argsdict)
            value = argsdict.get("%s" % name)
            print(value)
            result = float(value)
            for arg in args[1:]:
                result += float(arg)
            try:
                if result.is_integer():
                    result = int(result)
            except:
                pass
            print("name is", name)
            print(result)
            print(self.argsdict.get("%s" % name))
            self.argsdict.update({name:str(result)})
            print(self.argsdict.get("%s" % name))
            return result
        return calculate


    def equalminus(self):
        def calculate(args: str, argsdict: dict):
            args = args.split()
            parser = self.useVariable()
            value = int(parser(args[0], argsdict))
            result = float(value) - float(args[1])
            try:
                if result.is_integer():
                    result = int(result)
            except:
                pass
            return result
        return calculate

    def equalmultiply(self):
        def calculate(args: str, argsdict: dict):
            parser = self.useVariable()
            value = int(parser(args[0], argsdict))
            result = 1
            result *= float(value)
            for arg in args[1:]:
                result *= float(arg)
            try:
                if result.is_integer():
                    result = int(result)
            except:
                pass
            return result
        return calculate

    def equaldivide(self):
        def calculate(args: str, argsdict:dict):
            parser = self.useVariable()
            value = int(parser(args[0], argsdict))
            result = float(value)
            for arg in args[1:]:
                result /= float(arg)
            try:
                if result.is_integer():
                    result = int(result)
            except:
                pass
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
            print(firstArg)
            if firstArg.find("(") != -1:
                firstArg += ")"
            print(firstArg + "퍼스트아그")
            firstArg = run(firstArg, "", argsdict)
            secondArg = args[args.find("equal") + 5:args.find("do")].strip()
            if len(secondArg.split()) < 1:
                command = secondArg[1:-1].split()[0]
            else:
                command = ""
            secondArg = run(secondArg, "", argsdict)
            thirdArg = args[args.find("do") + 2:args.find("else")].strip()
            fourthArg = args[args.find("else") + 4:].strip()
            print("포스아그", fourthArg)
            print("포스아그", fourthArg)
            if firstArg == secondArg:
                thirdArg = run(thirdArg, "", argsdict)
                return thirdArg
            else:
                fourthArg = run(fourthArg, "", argsdict)
                return fourthArg
        return ifChecksemi

    def setVariable(self):
        def semi(args: str, argsdict:dict):
            print("dd")
            print(args)
            if len(args.split()) > 2:
                print("more 2")
                print("line", args)
                line = args.strip()
                args = args.split()
                name = args[0]
                value = line.replace(name + " ", "", 1)
                print(value)
                self.argsdict.update({name:str(value)})
                print(argsdict)
                return ""
            elif len(args.split()) == 2:
                print("2")
                args = args.split()
                name = args[0]
                value = args[1]
                self.argsdict.update({name:str(value)})
                print(argsdict)
                return ""
            else:
                return ""
        return semi

    def callVariable(self):
        return self.argsdict

    def useVariable(self):
        def useVar(args: str, argsdict: dict):
            print(argsdict)
            print(args)
            line = args
            for key in argsdict.keys():
                line = line.replace(key, argsdict[key])
            print(line)
            print("유즈바!")
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
            print("셋")
            self.func = self.setVariable()
        elif command == "use":
            print("유즈")
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
        else:
            self.func = self.nocommand(context)

    def run(self, args: str, argsdict: dict):
        print("런", args)
        args = args.strip()
        args = args.replace("(", "", 1)
        args = args.replace(")", "", 1)
        args = args.strip()
        print(args)
        if len(args.split()) > 1:
            args = args.replace(args.split()[0], "", 1)
        print(args)
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
    print(rawline)
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
                print("현재 "+ rawline)
                semiTag = rawline[:depthList.index(1, depthList.index(1) + 1) + 1]
                print("현재 " + semiTag)
                if rawline.find("(if") == 0 or rawline.find("(declare") == 0:
                    print("디클레어")
                    mode = semiTag[1:-1].split()[0]
                    print("모드", mode)
                    Tag = tag(Name, mode, semiTag, argsdict)
                    argsdict.update(Tag.argsdict)
                    result = Tag.run(semiTag, argsdict)
                    argsdict.update(Tag.argsdict)
                    rawline = rawline.replace(semiTag, result, 1)
                    return run(rawline, args, argsdict)
                print(checkDepth(semiTag))
                print(max(checkDepth(semiTag)))
                startnumsemi = checkDepth(semiTag).index(
                        max(checkDepth(semiTag)))
                print(startnumsemi)
                endnumsemi = checkDepth(semiTag).index(
                        max(checkDepth(semiTag)), startnumsemi+1)
                print("스타트넘", startnumsemi)
                print("엔드넘", endnumsemi)
                print("세미태그", semiTag)
                useTag = semiTag[startnumsemi:endnumsemi+1]
                print("유즈태그", useTag)
                mode = useTag[1:-1].split()[0]
                print("모드", mode)
                Tag = tag(Name, mode, useTag, argsdict)
                print(argsdict)
                result = Tag.run(useTag, argsdict)
                argsdict.update(Tag.argsdict)
                print("결과", result)
                Temptag = semiTag.replace(useTag, str(result), 1)
                rawline = rawline.replace(semiTag, Temptag, 1)
                print(argsdict)
                return run(rawline, args, argsdict)
        else:
            return rawline