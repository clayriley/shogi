# -*- coding: utf-8 -*-
"""
classes for shogi pieces

@author: clayriley
"""

from abc import ABCMeta
from abc import abstractmethod


class Piece(object, metaclass=ABCMeta):

    name = 'piece'
    sign = '?'
    moveset = {}
    promotion = None

    @abstractmethod
    def __init__(self, color):
        self.captured = type(self)
        self.color = color
        self.moves = getMoves(type(self).moveset, color)
        
    def promote(self):
        return self.promotion(self.color)
    
    def __repr__(self):
        color = 'gote' if self.color else 'sente'
        return '{} ({})'.format(self.name, color)
    
    def __str__(self):
        orientation = ['/','\\'] if self.color else ['\\','/']
        return self.sign.join(orientation)


class King(Piece):

    name = 'king general'
    sign = '王'
    moveset = {(0, 1): 1, (1, 1): 1, (1, 0): 1, (1, -1): 1,
               (0, -1): 1, (-1, -1): 1, (-1, 0): 1, (-1, 1): 1}

    def __init__(self, color):
        super(King, self).__init__(color)
        if not color:
            self.name = 'jeweled general'
            self.sign = '玉'


class Gold(Piece):

    name = 'gold general'
    sign = '金'
    moveset = {(0, 1): 1, (1, 1): 1, (1, 0): 1, (0, -1): 1, (-1, 0): 1, (-1, 1): 1}
    
    def __init__(self, color):
        super(Gold, self).__init__(color)


class Silver(Piece):

    name = 'silver general'
    sign = '銀'
    moveset = {(0, 1): 1, (1, 1): 1, (1, -1): 1, (-1, -1): 1, (-1, 1): 1}
    promotion = PromotedSilver

    def __init__(self, color):
        super(Silver, self).__init__(color)


class PromotedSilver(Gold):

    name = 'promoted silver'
    sign = '全'

    def __init__(self, color):
        super(PromotedSilver, self).__init__(color)
        self.captured = Silver


class Bishop(Piece):

    name = 'bishop'
    sign = '角'
    moveset = {(1, 1): 8, (1, -1): 8, (-1, -1): 8, (-1, 1): 8}
    promotion = Horse

    def __init__(self, color):
        super(Bishop, self).__init__(color)


class Horse(Piece):

    name = 'dragon horse'
    sign = '馬'
    moveset = {(0, 1): 1, (1, 1): 8, (1, 0): 1, (1, -1): 8,
               (0, -1): 1, (-1, -1):8, (-1, 0): 1, (-1, 1): 8}

    def __init__(self, color):
        super(Horse, self).__init__(color)
        self.captured = Bishop


class Rook(Piece):

    name = 'flying chariot'
    sign = '飛'
    moveset = {(0, 1): 8, (1, 0): 8, (0, -1): 8, (-1, 0): 8}
    promotion = Dragon

    def __init__(self, color):
        super(Rook, self).__init__(color)


class Dragon(Piece):

    name = 'dragon king'
    sign = '竜'
    moveset = {(0, 1): 8, (1, 1): 1, (1, 0): 8, (1, -1): 1,
               (0, -1): 8, (-1, -1): 1, (-1, 0): 8, (-1, 1): 1}

    def __init__(self, color):
        super(Dragon, self).__init__(color)
        self.captured = Rook


class Lance(Piece):

    name = 'lance'
    sign = '香'
    moveset = {(0, 1): 8}
    promotion = PerfumedGeneral

    def __init__(self, color):
        super(Lance, self).__init__(color)


class PerfumedGeneral(Gold):

    name = 'perfumed general'
    sign = '杏'

    def __init__(self, color):
        super(PerfumedGeneral, self).__init__(color)
        self.captured = Lance


class Knight(Piece):

    name = 'laurel horse'
    sign = '桂'
    moveset = {(1, 2): 1, (-1, 2): 1}
    promotion = LaurelGeneral

    def __init__(self, color):
        super(Knight, self).__init__(color)


class LaurelGeneral(Gold):

    name = 'laurel general'
    sign = '圭'

    def __init__(self, color):
        super(LaurelGeneral, self).__init__(color)
        self.captured = Knight


class Pawn(Piece):

    name = 'pawn'
    sign = '歩'
    moveset = {(0, 1): 1}
    promotion = Tokin

    def __init__(self, color):
        super(Pawn, self).__init__(color)


class Tokin(Gold):

    name = 'tokin'
    sign = 'と'

    def __init__(self, color):
        super(Tokin, self).__init__(color)
        self.captured = Pawn


def getMoves(moveset, color):
    out = moveset
    if color:
        out = {}
        for cardinals in moveset:
            out[(-cardinals[0], -cardinals[1])] = moveset[cardinals]
    return out
