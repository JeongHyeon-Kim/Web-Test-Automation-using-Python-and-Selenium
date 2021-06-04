if __name__ == "__main__": # import로 부를 시엔 실행되지 않음
# AttributeError: module 'class_exercise' has no attribute 'Calculator'
    class Calculator:
            def input_num(self, first, second): # 안넣어주면 에러 발생
            self.first = first
            self.second = second
        def sum(self):
            result = self.first + self.second
            return result
        def mul(self):
            result = self.first * self.second
            return result
        def sub(self):
            result = self.first - self.second
            return result
        def div(self):
            result = self.first / self.second
            return result
