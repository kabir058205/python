# numpy_basics.py

# One-shot execution: STEP 1 .. STEP 19

# Data Analyst focused NumPy examples

import numpy as np

def main():
    print("=== NUMPY BASICS: ONE-SHOT EXECUTION ===")


# -------------------------------------------------
# STEP 1: Create NumPy Arrays
# -------------------------------------------------
print("\n=== STEP 1: CREATE ARRAYS ===")
arr_1d = np.array([10, 20, 30, 40, 50])
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_1d)
print(arr_2d)

# -------------------------------------------------
# STEP 2: Array Properties
# -------------------------------------------------
print("\n=== STEP 2: ARRAY PROPERTIES ===")
print("Shape:", arr_2d.shape)
print("Dimensions:", arr_2d.ndim)
print("Data type:", arr_2d.dtype)

# -------------------------------------------------
# STEP 3: Zeros, Ones, Full
# -------------------------------------------------
print("\n=== STEP 3: ZEROS / ONES / FULL ===")
print(np.zeros(5))
print(np.ones(5))
print(np.full(5, 7))

# -------------------------------------------------
# STEP 4: arange vs linspace
# -------------------------------------------------
print("\n=== STEP 4: ARANGE vs LINSPACE ===")
print(np.arange(0, 10, 2))
print(np.linspace(0, 10, 5))

# -------------------------------------------------
# STEP 5: Indexing & Slicing
# -------------------------------------------------
print("\n=== STEP 5: INDEXING & SLICING ===")
print(arr_1d[0])
print(arr_1d[1:4])

# -------------------------------------------------
# STEP 6: Boolean Filtering (Use case: salary)
# -------------------------------------------------
print("\n=== STEP 6: BOOLEAN FILTERING ===")
salaries = np.array([50000, 70000, 90000, 60000, 80000])
print(salaries[salaries > 70000])

# -------------------------------------------------
# STEP 7: Vectorized Operations
# -------------------------------------------------
print("\n=== STEP 7: VECTORIZED OPS ===")
print(salaries * 1.1)

# -------------------------------------------------
# STEP 8: Mathematical Functions
# -------------------------------------------------
print("\n=== STEP 8: MATH FUNCTIONS ===")
print("Mean:", np.mean(salaries))
print("Std:", np.std(salaries))

# -------------------------------------------------
# STEP 9: Min, Max, Sum
# -------------------------------------------------
print("\n=== STEP 9: MIN / MAX / SUM ===")
print(np.min(salaries), np.max(salaries), np.sum(salaries))

# -------------------------------------------------
# STEP 10: Axis Operations
# -------------------------------------------------
print("\n=== STEP 10: AXIS OPERATIONS ===")
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("Column sum:", np.sum(matrix, axis=0))
print("Row sum:", np.sum(matrix, axis=1))

# -------------------------------------------------
# STEP 11: Reshape
# -------------------------------------------------
print("\n=== STEP 11: RESHAPE ===")
reshaped = np.arange(1, 7).reshape(2, 3)
print(reshaped)

# -------------------------------------------------
# STEP 12: Flatten
# -------------------------------------------------
print("\n=== STEP 12: FLATTEN ===")
print(reshaped.flatten())

# -------------------------------------------------
# STEP 13: Sorting
# -------------------------------------------------
print("\n=== STEP 13: SORTING ===")
print(np.sort(salaries))

# -------------------------------------------------
# STEP 14: Unique & Counts
# -------------------------------------------------
print("\n=== STEP 14: UNIQUE & COUNTS ===")
countries = np.array(["IN", "SE", "IN", "US", "SE"])
print(np.unique(countries, return_counts=True))

# -------------------------------------------------
# STEP 15: Handling NaN
# -------------------------------------------------
print("\n=== STEP 15: NaN HANDLING ===")
data = np.array([10, 20, np.nan, 40])
print("Nan mean:", np.nanmean(data))

# -------------------------------------------------
# STEP 16: Where Condition
# -------------------------------------------------
print("\n=== STEP 16: WHERE CONDITION ===")
print(np.where(salaries >= 80000, "High", "Low"))

# -------------------------------------------------
# STEP 17: Random Numbers
# -------------------------------------------------
print("\n=== STEP 17: RANDOM ===")
print(np.random.randint(1, 100, 5))

# -------------------------------------------------
# STEP 18: Broadcasting
# -------------------------------------------------
print("\n=== STEP 18: BROADCASTING ===")
print(salaries + 5000)

# -------------------------------------------------
# STEP 19: NumPy vs Python List (Performance Idea)
# -------------------------------------------------
print("\n=== STEP 19: NUMPY VS LIST (CONCEPT) ===")
python_list = [1, 2, 3, 4, 5]
print("List x2:", [x * 2 for x in python_list])
print("NumPy x2:", np.array(python_list) * 2)

print("\n=== NUMPY BASICS COMPLETED ===")


if __name__ == "__main__":
    main()
