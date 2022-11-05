from utils import check_dim, currently_satisfied_constraints
import numpy as np


def test_checkdim():
    assert check_dim(constraints=[1, 2], board_extract=np.array([
        1, 0, 0, 1, 1, 0, 0]))
    assert check_dim(constraints=[1, 2], board_extract=np.array([
        0, 1, 0, 0, 1, 1, 0, 0]))


def test_currently_satisfied_constraints():
    assert currently_satisfied_constraints(
        np.array([1, 1, 1, 0, 1])) == ([3, 1], True)
    assert currently_satisfied_constraints(
        np.array([1, 1, 1, 0, 0])) == ([3], False)
    assert currently_satisfied_constraints(
        np.array([0, 0, 0, 0, 1])) == ([1], True)
    assert currently_satisfied_constraints(
        np.array([0, 0, 0, 0, 0])) == ([], False)


def run():
    test_checkdim()
    test_currently_satisfied_constraints()
