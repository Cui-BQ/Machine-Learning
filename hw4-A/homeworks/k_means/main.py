if __name__ == "__main__":
    from k_means import calculate_error, lloyd_algorithm  # type: ignore
else:
    from .k_means import lloyd_algorithm, calculate_error

import matplotlib.pyplot as plt
import numpy as np

from utils import load_dataset, problem


@problem.tag("hw4-A", start_line=1)
def main():
    """Main function of k-means problem

    You should:
        a. Run Lloyd's Algorithm for k=10, and report 10 centers returned.
        b. For ks: 2, 4, 8, 16, 32, 64 run Lloyd's Algorithm,
            and report objective function value on both training set and test set.
            (All one plot, 2 lines)

    NOTE: This code takes a while to run. For debugging purposes you might want to change:
        x_train to x_train[:10000]. CHANGE IT BACK before submission.
    """
    (x_train, _), (x_test, _) = load_dataset("mnist")
    #raise NotImplementedError("Your Code Goes Here")

    """
    # Part b
    centers = lloyd_algorithm(x_train, 10)
    for i in range(10):
        plt.imshow(centers[i].reshape(28,28))
        plt.show()
    """

    
    # Part c
    ks = [2, 4, 8, 16, 32, 64]
    train_error = np.zeros(6)
    test_error = np.zeros(6)
    i = 0
    for k in ks:
        print("k = ", k)
        centers = lloyd_algorithm(x_train, k)
        train_error[i] += calculate_error(x_train, centers)
        test_error[i] += calculate_error(x_test, centers)
        i += 1

    plt.figure(1)
    plt.plot(ks, train_error)
    plt.plot(ks, test_error)
    plt.xlabel('K')
    plt.ylabel('Error')
    plt.title('3.c')
    plt.legend(["train_error", "test_error"])
    plt.show()


if __name__ == "__main__":
    main()
