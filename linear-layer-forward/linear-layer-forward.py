def linear_layer_forward(X: list, W: list, b: list) -> list:
    ans = []

    for i in range(len(X)):
        row = []

        for k in range(len(W[0])):
            total = 0

            for j in range(len(W)):
                total += X[i][j] * W[j][k]

            total += b[k]
            row.append(total)

        ans.append(row)

    return ans