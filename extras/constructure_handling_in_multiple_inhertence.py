class A:
    def __init__(self, A_attribute: int) -> None:
        print(f"A_attribute: {A_attribute}")


class B:
    def __init__(self, B_attribute: int) -> None:
        print(f"B_attribute: {B_attribute}")


class C(A, B):

    def __init__(self, A_attribute: int, B_attribute: int) -> None:
        super().__init__(A_attribute=A_attribute)
        A.__init__(self, A_attribute)
        B.__init__(self, B_attribute)


a: A = A(5)
b: B = B(15)
c: C = C(10, 20)
