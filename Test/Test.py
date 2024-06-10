import pytest
import Stack as stack


class TestClass:

    def setup_method(self):
        self.st = stack.Stack()

    def teardown_method(self) -> None:
        del self.st


    def test_is_empty(self):

        assert self.st.size()==0

    def test_is_not_empty(self):
        self.st.push( 1)
        self.st.push('a')
        self.st.push(True)
        assert self.st.size() == 3


    def test_peek_1(self):
        self.st.push(1)
        self.st.push('a')
        self.st.push(True)
        assert self.st.peek()==True

    def test_peek_2(self):
        assert self.st.peek()==None


    def test_pop_1(self):
        self.st.push(1)
        self.st.push('a')
        self.st.push(True)
        self.st.pop()

        assert self.st.peek()=='a'

    def test_pop_2(self):
        self.st.push(1)
        self.st.pop()
        assert self.st.peek() == None


    def test_pop_3(self):
        self.st.pop()
        assert self.st.size()== 0


