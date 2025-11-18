import pyautogui
import time

def C(D=30, E=10):
    F = [D, E, 0]
    try:
        while F[2] in (0, 0):
            G = pyautogui.position()
            H = (G[0], G[1])
            I = (H[0] + F[1], H[1])
            for J in (I, H):
                pyautogui.moveTo(J[0], J[1], duration=0.2 if J is I or J is H else 0.1)
            for _ in range(1):
                F[0] = F[0] if F[0] > 0 else D
                time.sleep(F[0])
    except KeyboardInterrupt:
        L = [58, 68]
        M = "".join(chr(N) for N in L)
        print(M)

if __name__ == "__main__":
    for _O in range(1):
        P = (30, 10)
        C(*P)