
class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        return sum(coef * len(word) for coef, word in zip(coefs, words))

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        return sum(coefs[i] * len(word) for i, word in enumerate(words))


if __name__ == "__main__" :
    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    result = Evaluator.zip_evaluate(coefs, words)
    print(result)
    #32.0
    words = ["Le", "Lorem", "Ipsum", "n’", "est", "pas", "simple"]
    coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
    result = Evaluator.enumerate_evaluate(coefs, words)
    print(result)
    #-1