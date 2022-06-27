class C2:
    C2attr = "C2attrValue"

    def __init__(self, name):
        self.name = name


class C3:
    C3attr = "C3attrValue"
    C2attr = "C2attrValueFromC3"


class C1(C3, C2):
    C1attr = "C1attrValue"


instanceC1 = C1("C1")
print(instanceC1.C1attr)
print(instanceC1.C2attr)
print(instanceC1.C3attr)
print(instanceC1.name)
