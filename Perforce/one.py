"""
inputs:
hr_hand: 0-12
min_hand: 0-60
return: angel between two hands
"""


def find_angel(hr_hand, min_hand):
    if hr_hand == 12:
        hr_hand = 0
    if min_hand == 60:
        min_hand = 0
    hr_hand = hr_hand * 5
    return abs(hr_hand - min_hand) * 6


if __name__ == '__main__':
    print(f"{find_angel(12, 20)}")
    print(f"{find_angel(7, 10)}")
