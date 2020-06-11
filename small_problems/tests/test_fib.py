from small_problems import fib
import pytest

@pytest.fixture
def runner_naive_fib():
    return fib.naive_fib

@pytest.fixture
def runner_memo_fib():
    return fib.memo_fib

@pytest.fixture
def runner_cache_fib():
    return fib.cache_fib

@pytest.fixture
def runner_iter_fib():
    return fib.iter_fib

@pytest.fixture
def runner_gen_fib():
    return fib.gen_fib

def test_fib_naive(runner_naive_fib):
    fib_tests_easy(runner_naive_fib)

def test_fib_memo(runner_memo_fib):
    fib_tests_easy(runner_memo_fib)
    fib_tests_hard(runner_memo_fib)

def test_fib_lru_cache(runner_cache_fib):
    fib_tests_easy(runner_cache_fib)
    fib_tests_hard(runner_cache_fib)

def test_fib_iter(runner_iter_fib):
    fib_tests_easy(runner_iter_fib)
    fib_tests_hard(runner_iter_fib)

def test_fib_gen(runner_gen_fib):
    for i, v in enumerate(runner_gen_fib(100)):
        if i == 0: assert v == 0
        if i == 1: assert v == 1
        if i == 2: assert v == 1
        if i == 14: assert v == 377
        if i == 100: assert v == 354224848179261915075


def fib_tests_easy(fn):
    assert fn(0) == 0
    assert fn(1) == 1
    assert fn(2) == 1
    assert fn(14) == 377


def fib_tests_hard(fn):
    assert fn(100) == 354224848179261915075
