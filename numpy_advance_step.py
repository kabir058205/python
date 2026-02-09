# advanced_numpy.py
# Advanced NumPy concepts for Senior Data Analysts / Interview prep
# Run once: python3 advanced_numpy.py

from random import choices
import numpy as np
import time

def main():
    print("=== ADVANCED NUMPY: ONE-SHOT EXECUTION ===")

    # -------------------------------------------------
    # STEP 1: Advanced Indexing (Fancy Indexing)
    # -------------------------------------------------
    print("\n=== STEP 1: FANCY INDEXING ===")
    arr = np.array([10, 20, 30, 40, 50])
    idx = [0, 2, 4]
    print(arr[idx])

    # -------------------------------------------------
    # STEP 2: Masked Arrays
    # -------------------------------------------------
    print("\n=== STEP 2: MASKED ARRAYS ===")
    data = np.array([100, -1, 200, -1, 300])
    masked = np.ma.masked_where(data == -1, data)
    print(masked)
    print("Mean without masked values:", masked.mean())

    # -------------------------------------------------
    # STEP 3: Broadcasting (2D vs 1D)
    # -------------------------------------------------
    print("\n=== STEP 3: ADVANCED BROADCASTING ===")
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    vector = np.array([10, 20, 30])
    print(matrix + vector)

    # -------------------------------------------------
    # STEP 4: Stack & Split
    # -------------------------------------------------
    print("\n=== STEP 4: STACK & SPLIT ===")
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    stacked = np.vstack((a, b))
    print(stacked)
    print(np.hsplit(stacked, 3))

    # -------------------------------------------------
    # STEP 5: Vectorization vs Loop (Performance)
    # -------------------------------------------------
    print("\n=== STEP 5: VECTORIZATION PERFORMANCE ===")
    size = 1_000_000
    arr = np.random.rand(size)

    start = time.time()
    result_loop = [x * 2 for x in arr]
    print("Loop time:", round(time.time() - start, 4))

    start = time.time()
    result_np = arr * 2
    print("NumPy time:", round(time.time() - start, 4))

    # -------------------------------------------------
    # STEP 6: Memory Views vs Copies
    # -------------------------------------------------
    print("\n=== STEP 6: VIEW VS COPY ===")
    base = np.array([1, 2, 3, 4])
    view = base.view()
    copy = base.copy()

    view[0] = 999
    print("Base after view change:", base)

    copy[1] = 888
    print("Base after copy change:", base)

    # -------------------------------------------------
    # STEP 7: Structured Arrays (Like Table)
    # -------------------------------------------------
    print("\n=== STEP 7: STRUCTURED ARRAYS ===")
    dtype = [("name", "U10"), ("salary", "i4")]
    employees = np.array([("Kabir", 90000), ("Amit", 70000)], dtype=dtype)
    print(employees)
    print(employees[employees['salary'] > 80000])

    # -------------------------------------------------
    # STEP 8: np.select (Multiple Conditions)
    # -------------------------------------------------
    print("\n=== STEP 8: NP.SELECT ===")
    salary = np.array([60000, 72000, 90000, 50000])
    conditions = [
    salary < 70000,
    (salary >= 70000) & (salary < 85000),
    salary >= 85000
    ]
    choices = ["Low", "Medium", "High"]
    result = np.select(conditions, choices, default="Unknown")
    print(result)


    # -------------------------------------------------
    # STEP 9: Linear Algebra
    # -------------------------------------------------
    print("\n=== STEP 9: LINEAR ALGEBRA ===")
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    print("Dot product:\n", np.dot(A, B))
    print("Determinant:", np.linalg.det(A))
    print("Inverse:\n", np.linalg.inv(A))

    # -------------------------------------------------
    # STEP 10: Cumulative Operations
    # -------------------------------------------------
    print("\n=== STEP 10: CUMULATIVE OPS ===")
    arr = np.array([1, 2, 3, 4])
    print("Cumsum:", np.cumsum(arr))
    print("Cumprod:", np.cumprod(arr))

    # -------------------------------------------------
    # STEP 11: Sliding Window (Moving Average)
    # -------------------------------------------------
    print("\n=== STEP 11: MOVING AVERAGE ===")
    data = np.array([10, 20, 30, 40, 50])
    window = 3
    moving_avg = np.convolve(data, np.ones(window)/window, mode='valid')
    print(moving_avg)

    # -------------------------------------------------
    # STEP 12: Histogram (Distribution Analysis)
    # -------------------------------------------------
    print("\n=== STEP 12: HISTOGRAM ===")
    values = np.random.normal(50000, 10000, 1000)
    hist, bins = np.histogram(values, bins=5)
    print("Histogram:", hist)
    print("Bins:", bins)

    # -------------------------------------------------
    # STEP 13: Random Seed (Reproducibility)
    # -------------------------------------------------
    print("\n=== STEP 13: RANDOM SEED ===")
    np.random.seed(42)
    print(np.random.rand(3))

    # -------------------------------------------------
    # STEP 14: np.einsum (Advanced Operations)
    # -------------------------------------------------
    print("\n=== STEP 14: EINSUM ===")
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    print("Dot via einsum:", np.einsum('i,i->', a, b))

    # -------------------------------------------------
    # STEP 15: Memory Size
    # -------------------------------------------------
    print("\n=== STEP 15: MEMORY SIZE ===")
    print("Array bytes:", a.nbytes)

    print("\n=== ADVANCED NUMPY COMPLETED ===")


if __name__ == "__main__":
    main()
