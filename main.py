import math
import matplotlib.pyplot as plt
import numpy as np

# L = float(input())
# V = float(input())
# R = float(input())
# I_0 = float(input())


def func_1(x, I, R, V, L):

    return (V - R * I) / L


def rk4_s(x_0, I_0, f_1, f_2, L, V, R, h, v_max):
    I = I_0
    k_1 = np.longdouble(h * f_1(x_0, L, V, R, I_0))
    if abs(k_1) > v_max:
        return v_max, v_max
    l_1 = np.longdouble(h * f_2(x_0, L, V, R, I_0))
    if abs(l_1) > v_max:
        return v_max, v_max
    k_2 = np.longdouble(h * f_1(x_0 + h / 2, I_0 + k_1 / 2, L, V, R))
    if abs(k_2) > v_max:
        return v_max, v_max
    l_2 = np.longdouble(h * f_2(x_0 + h / 2, I_0 + k_1 / 2, L, V, R))
    if abs(l_2) > v_max:
        return v_max, v_max
    k_3 = np.longdouble(h * f_1(x_0 + h / 2, I_0 + k_2 / 2, V, L, R))
    if abs(k_3) > v_max:
        return v_max, v_max
    l_3 = np.longdouble(h * f_2(x_0 + h / 2, I_0 + k_2 / 2, L, V, R))
    if abs(l_3) > v_max:
        return v_max, v_max
    k_4 = np.longdouble(h * f_1(x_0 + h, I_0 + k_3, L, V, R))
    if abs(k_4) > v_max:
        return v_max, v_max
    l_4 = np.longdouble(h * f_2(x_0 + h, I_0 + k_3, L, V, R))
    if abs(l_4) > v_max:
        return v_max, v_max
    I += np.longdouble(1 / 6 * (k_1 + 2 * k_2 + 2 * k_3 + k_4))
    if abs(I) > v_max:
        return v_max, v_max

    return I


def num_sol_3_task(L, V, R, N_max, f_1, f_2, x_0, I_0, x_end, h, e, error_control):
    v_max = 10e30
    c1 = 0
    c2 = 0
    u1_ds = I_0
    s_nor = 0
    n = 1

    C1 = [c1]
    C2 = [c2]
    U1 = [I_0]
    U1_ds = [I_0]
    U1_U1ds = [0]
    H = [h]
    error_arr = [0]
    X = [x_0]

    while x_0 <= x_end - h:
        temp_1, temp_2 = rk4_s(x_0, I_0, f_1, f_2, L, V, R, h, v_max)
        temp1_ds, temp2_ds = rk4_s(x_0, I_0, f_1, f_2, L, V, R, h / 2, v_max)
        temp1_ds, temp2_ds = rk4_s(
            x_0 + h / 2, temp1_ds, temp2_ds, f_1, f_2, L, V, R, h / 2, v_max
        )

        if v_max in [temp_1, temp_2, temp1_ds]:
            break

        s_nor = ((temp_1 - temp1_ds) /15)
        if error_control and abs(s_nor) > e:
            h = h / 2
            c1 += 1
        else:
            I_0 = temp_1

            u1_ds = temp1_ds
            x_0 = x_0 + h
            H.append(h)
            U1_ds.append(u1_ds)
            U1.append(I_0)
            U1_U1ds.append(I_0 - u1_ds)
            X.append(x_0)
            error_arr.append(s_nor / 15)
            if error_control:
                if s_nor < e / 32:
                    h = 2 * h
                    c2 += 1
            C2.append(c2)
            C1.append(c1)
        if error_control:
            if n >= N_max:
                break
        n += 1

    return X, U1, U1_ds, error_arr, H, C1, C2, n-C1


def rk4(x_i, y_i, h, func, v_max, L, V, R):
    y = np.longdouble(y_i)
    k1 = np.longdouble(h * func(x_i, y, L, V, R))
    if abs(k1) > v_max:
        return v_max
    k2 = np.longdouble(h * func(x_i + h / 2, y + k1 / 2, L, V, R))
    if abs(k2) > v_max:
        return v_max
    k3 = np.longdouble(h * func(x_i + h / 2, y + k2 / 2, L, V, R))
    if abs(k3) > v_max:
        return v_max
    k4 = np.longdouble(h * func(x_i + h, y + k3, L, V, R))
    if abs(k4) > v_max:
        return v_max
    y += np.longdouble((1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4))
    return y


def func_num_sln(
    x0, u0, x_max, h, Nmax, max_error, func, error_control, is_test, L, R, V, right_limit
):
    v_max = 10e30
    c1 = 0
    c2 = 0
    x = x0
    v = u0
    v2 = u0
    i = 1
    n=0

    X = [x0]
    T = [u0]
    U = [u0]
    # X2 = []
    V2 = [u0]
    C1 = [c1]
    C2 = [c2]
    H = [h]
    error_arr = [(v2 - v) / 15]
    if is_test:
        c = u0 * math.exp((5 / 2) * x0)

    while x <= x_max - h:
        temp = rk4(x, v, h, func, v_max, L, V, R)
        temp2 = rk4(x, v, h / 2, func, v_max, L, V, R)
        # v_half = temp2
        temp2 = rk4(x + h / 2, temp2, h / 2, func, v_max, L, V, R)
        if temp == v_max or temp2 == v_max:
            break
        if error_control and (abs(temp2 - temp) > max_error):
            h /= 2
            c1 += 1
        else:
            x += h
            v = temp
            v2 = temp2
            X.append(x)
            T.append(v)
            # X2.append(x-h/2)
            # V2.append(v_half)
            # X2.append(x)
            V2.append(v2)
            C1.append(c1)
            H.append(h)
            error_arr.append(((v2 - v) / 15)*16)
            n+=1
            if is_test:
                u = c * math.exp((-3 / 2) * x)
                U.append(u)

            if error_control:
                if abs((v2 - v)/15) < (max_error / 32):
                    h *= 2
                    c2 += 1
            C2.append(c2)

        if error_control:
            if i == Nmax:
                break
        i += 1
        n += 1
        if x + h > x_max:
            while x + h > x_max:
                h /= 2
                c1 += 1
        if x > x_max - right_limit:
            break


    return X, T, V2, error_arr, H, C1, C2, U, n-c1


def test_precise_sln(x0, u0, h, x_max):
    X = [x0]
    U = [u0]
    # h = 0.001
    x = x0
    u = u0
    c = u0 * math.exp((5 / 2) * x0)
    while x < x_max - h:
        x += h
        u = c * math.exp((-5 / 2) * x)
        X.append(x)
        U.append(u)
    return X, U
