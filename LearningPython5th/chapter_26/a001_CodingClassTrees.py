class C2:
    C2attr = "C2attrValue"

    def setName(self, name: str) -> None:
        self.name = name


class C3:
    C3attr = "C3attrValue"


class C1(C2, C3):
    C1attr = "C1attrValue"


instanceC1 = C1()
instanceC2 = C2()
print(instanceC1.C2attr)
print(instanceC1.C3attr)
print(instanceC1.C1attr)
instanceC1.setName("C1")
print(instanceC1.name)
C2.setName(instanceC1, "C11")

print(C1.__bases__)
