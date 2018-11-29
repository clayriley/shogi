# -*- coding: utf-8 -*-
"""
@author: clayriley
"""

import pieces

sente = True
gote = not sente


class Game(object):
    pass


class Player(object):

    def __init__(self, color):
        self.color = color
        self.hand = {pieces.Rook: 0,
                     pieces.Bishop: 0,
                     pieces.Gold: 0,
                     pieces.Silver: 0,
                     pieces.Knight: 0,
                     pieces.Lance: 0,
                     pieces.Pawn: 0}


class Board(object):

    files = {0: 9, 1: 8, 2: 7, 3: 6, 4: 5, 5: 4, 6: 3, 7: 2, 8: 1}
    ranks = {0: '一', 1: '二', 2: '三', 3: '四', 4: '五',
             5: '六', 6: '七', 7: '八', 8: '九'}
    camps = {gote: [0, 1, 2], sente: [8, 7, 6]}
    empty = '    '

    def __init__(self):
        self.sente = Player(sente)
        self.gote = Player(gote)
        self.piece_map = self.initialize_map()

    def initialize_map(self):
        board = [[None][:]*len(Board.files) for rank in range(len(Board.ranks))]
        for color in [gote, sente]:
            rear, mid, forward = Board.camps[color]
            for f in Board.files:
                board[forward][f] = pieces.Pawn(color)
                if f in [0, 8]:
                    board[rear][f] = pieces.Lance(color)
                elif f in [1, 7]:
                    board[rear][f] = pieces.Knight(color)
                elif f in [2, 6]:
                    board[rear][f] = pieces.Silver(color)
                elif f in [3, 5]:
                    board[rear][f] = pieces.Gold(color)
                elif f == 4:
                    board[rear][f] = pieces.King(color)
            if color:
                board[mid][1] = pieces.Rook(color)
                board[mid][7] = pieces.Bishop(color)
            else:
                board[mid][1] = pieces.Bishop(color)
                board[mid][7] = pieces.Rook(color)
        return board

    def getPieceAt(self, file, rank):
        return self.piece_map[rank][file]

    def __str__(self):
        # represent gote's pieces in hand
        board = '[ '
        for piece, count in self.gote.hand.items():
            if count > 0:
                for i in range(count):
                    if i == 0:
                        board += str(piece)
                    else:
                        board += '/'
                board += ' '
        board += ' ]\n\n '

        for f in sorted(Board.files):
            board += '____{}___ '.format(Board.files[f])
        for r in range(len(Board.ranks)):
            board += '\n#{}|'.format('#' * 9 * len(Board.files))
            board += '\n#{}|\n'.format(
                '  {}  #'.format(Board.empty) * len(Board.files))
            for f in range(len(Board.files)):
                p = self.getPieceAt(f, r)
                board += '#  {!s}  '.format(Board.empty if p is None else p)
            board += '#|{}'.format(Board.ranks[r])
            board += '\n#{}|'.format('        #' * len(Board.files))
        board += '\n#{}|\n\n[ '.format('#' * 9 * len(Board.files))

        # represent sente's pieces in hand
        for piece, count in self.sente.hand.items():
            if count > 0:
                for i in range(count):
                    if i == 0:
                        board += str(piece)
                    else:
                        board += '\\'
                board += ' '
        board += ' ]'
        return board


def main():
    b=Board()
    print b

if __name__ == '__main__':
    main()
