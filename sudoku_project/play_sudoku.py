# main.py
from generate_sudoku import generate_sudoku
from solve_sudoku import solve_sudoku_backtracking
from print_board import print_board
import copy

def play_sudoku():
    puzzle, solution = generate_sudoku()
    board = copy.deepcopy(puzzle)

    while True:
        print_board(board)
    
        while True:
            try: 
                row = int(input("행 번호 (0~8):  |(종료하려면 -1 입력)"))
            except:
                print("잘못된 입력입니다. 숫자를 입력하세요.")
                continue
            if row == -1:
                print("게임을 종료합니다.")
                return
            elif row < 0 or row > 8:
                print("잘못된 행 번호입니다.")
                continue
            break

        while True:
            try:
                col = int(input("열 번호 (0~8):  |(종료하려면 -1 입력)"))
            except:
                print("잘못된 입력입니다. 숫자를 입력하세요.")
                continue
            if col == -1:
                print("게임을 종료합니다.")
                return
            elif col < 0 or col > 8:
                print("잘못된 열 번호입니다.")
                continue
            break
        
        while True:
            try:
                num = int(input("넣을 숫자 (1~9):  |(종료하려면 -1 입력)"))
            except:
                print("잘못된 입력입니다. 숫자를 입력하세요.")
                continue
            if num == -1:
                print("게임을 종료합니다.")
                return
            elif num < 0 or col > 8:
                print("잘못된 입력값입니다.")
                continue
            break


        if puzzle[row][col] != 0:
            print("이 칸은 수정할 수 없습니다.")
            continue

        if solution[row][col] != num:
            print("틀렸습니다!")
        else:
            board[row][col] = num
            print("정답!")

        if board == solution:
            print("축하합니다! 스도쿠를 완성했습니다.")
            break


if __name__ == '__main__':
    play_sudoku()

