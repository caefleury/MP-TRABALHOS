""" An example of a test module in pytest"""
from oito_rainhas import *


def test_check_table_column_size():
    """ Table should be false due to row number"""
    table_input = ['00001000', '01000000', '00010000', '00000010',
                   '00100000', '00000001', '00000100', '10000000', '01000000']
    assert check_table(table_input) is False


def test_check_table_row_size():
    """ Table should be false due to bigger rows"""
    table_input = ['000010000', '010000000', '000100000',
                   '000000010', '001000000', '000000001', '000000100', '100000000']
    assert check_table(table_input) is False


def test_check_true_table():
    """ Table should be true """
    table_input = ['00001000', '01000000', '00010000',
                   '00000010', '00100000', '00000001', '00000100', '10000000']
    assert check_table(table_input) is True


def test_vertical_loss_01():
    """ Table should be false due to two queens in same column"""
    table_input = ['10000000', '01000000', '00010000',
                   '00000010', '00100000', '00000001', '00000100', '10000000']
    assert check_vertical(table_input) is False


def test_vertical_loss_02():
    """ Table should be false due to two queens in same column"""
    table_input = ['00001000', '01000000', '00010000',
                   '0000100', '00100000', '00000001', '00000100', '10000000']
    assert check_vertical(table_input) is False


def test_vertical_win():
    """ Table should be true due to two queens in same column"""
    table_input = ['00001000', '01000000', '00010000',
                   '00000010', '00100000', '00000001', '00000100', '10000000']
    assert check_vertical(table_input) is True


def test_diagonal_win():
    """ Table should be true due to two queens not in diagonal range"""
    table_input = ['00001000', '01000000', '00010000',
                   '00000010', '00100000', '00000001', '00000100', '10000000']
    assert check_diagonal(table_input) is True


def test_diagonal_loss_01():
    """ Table should be false due to two queens in diagonal range"""
    table_input = ['00001000', '01000000', '00100000',
                   '00000010', '00100000', '00000001', '00000100', '10000000']
    assert check_diagonal(table_input) is False


def test_diagonal_loss_02():
    """ Table should be false due to two queens in diagonal range"""
    table_input = ['00000001', '01000000', '00010000',
                   '00000010', '00100000', '00000001', '00000100', '10000000']
    assert check_diagonal(table_input) is False


def test_check_game_win():
    """ Table should be false due to two queens in diagonal range"""
    table_input = ['00001000', '01000000', '00010000',
                   '00000010', '00100000', '00000001', '00000100', '10000000']
    assert check_game(table_input) == 1


def test_check_game_loss_01():
    """ Table should be false due to two queens in diagonal range"""
    table_input = ['00000001', '01000000', '00010000',
                   '00000010', '00100000', '00000001', '00000100', '10000000']
    assert check_game(table_input) == 0


def test_check_game_loss_02():
    """ Table should be false due to two queens in diagonal range"""
    table_input = ['000000010', '010000000', '000100000',
                   '000000010', '000100000', '000000001', '000000100', '100000000', '000100000']
    assert check_game(table_input) == -1