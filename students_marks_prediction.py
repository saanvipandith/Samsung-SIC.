# ==========================================================
# STUDENT MARKS ANALYSIS SYSTEM
# Samsung SIC Project
# Semester 2 DSA Project using Python, Pandas, NumPy & Matplotlib
# ==========================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==========================================================
# STUDENT DATA
# ==========================================================

students = [
    ["Aarav Sharma", 1, 78, 85, 82],
    ["Diya Patel", 2, 92, 88, 95],
    ["Rohan Verma", 1, 67, 74, 70],
    ["Ananya Gupta", 3, 89, 91, 87],
    ["Vivaan Rao", 2, 76, 80, 79],
    ["Ishita Singh", 1, 95, 98, 97],
    ["Arjun Nair", 4, 81, 77, 84],
    ["Meera Joshi", 2, 88, 90, 92],
    ["Kabir Mehta", 3, 72, 68, 75],
    ["Saanvi Kapoor", 2, 91, 89, 93],
    ["Rahul Reddy", 4, 85, 83, 81],
    ["Priya Menon", 3, 94, 92, 90],
    ["Aditya Kumar", 1, 69, 73, 71],
    ["Sneha Jain", 2, 87, 85, 88],
    ["Karthik Rao", 4, 79, 82, 80]
]

# ==========================================================
# CREATE DATAFRAME
# ==========================================================

df = pd.DataFrame(
    students,
    columns=[
        "Student Name",
        "Semester",
        "Maths",
        "Science",
        "English"
    ]
)

# ==========================================================
# CALCULATE TOTAL & AVERAGE
# ==========================================================

df["Total"] = (
    df["Maths"] +
    df["Science"] +
    df["English"]
)

df["Average"] = round(df["Total"] / 3, 2)

# ==========================================================
# GRADE ASSIGNMENT FUNCTION
# ==========================================================

def assign_grade(avg):

    if avg >= 90:
        return "A+"

    elif avg >= 80:
        return "A"

    elif avg >= 70:
        return "B"

    elif avg >= 60:
        return "C"

    else:
        return "D"

df["Grade"] = df["Average"].apply(assign_grade)

# ==========================================================
# DISPLAY STUDENT RECORDS
# ==========================================================

print("\n")
print("=" * 70)
print("STUDENT RECORDS")
print("=" * 70)

print(df)

# ==========================================================
# NUMPY STATISTICAL ANALYSIS
# ==========================================================

marks_array = np.array(df["Average"])

print("\n")
print("=" * 70)
print("STATISTICAL ANALYSIS")
print("=" * 70)

print("Class Average Marks :", round(np.mean(marks_array), 2))
print("Highest Average     :", round(np.max(marks_array), 2))
print("Lowest Average      :", round(np.min(marks_array), 2))
print("Median Average      :", round(np.median(marks_array), 2))
print("Standard Deviation  :", round(np.std(marks_array), 2))

# ==========================================================
# SORTING (DSA)
# ==========================================================

sorted_df = df.sort_values(
    by="Total",
    ascending=False
)

print("\n")
print("=" * 70)
print("STUDENT RANKINGS")
print("=" * 70)

rank = 1

for index, row in sorted_df.iterrows():

    print(
        f"Rank {rank} --> "
        f"{row['Student Name']} | "
        f"Total Marks = {row['Total']} | "
        f"Grade = {row['Grade']}"
    )

    rank += 1

# ==========================================================
# SEARCHING (LINEAR SEARCH)
# ==========================================================

print("\n")
print("=" * 70)
print("STUDENT SEARCH")
print("=" * 70)

search_name = input(
    "\nEnter Student Name to Search : "
)

result = df[
    df["Student Name"].str.lower()
    ==
    search_name.lower()
]

if not result.empty:

    print("\nStudent Found!\n")
    print(result)

else:

    print("\nStudent Not Found!")

# ==========================================================
# TOPPER DETAILS
# ==========================================================

topper = df.loc[df["Average"].idxmax()]

print("\n")
print("=" * 70)
print("CLASS TOPPER")
print("=" * 70)

print("Name      :", topper["Student Name"])
print("Semester  :", topper["Semester"])
print("Average   :", topper["Average"])
print("Grade     :", topper["Grade"])

# ==========================================================
# SUBJECT TOPPERS
# ==========================================================

print("\n")
print("=" * 70)
print("SUBJECT TOPPERS")
print("=" * 70)

subjects = ["Maths", "Science", "English"]

for subject in subjects:

    topper_index = df[subject].idxmax()

    print(
        subject,
        "Topper :",
        df.loc[topper_index, "Student Name"],
        "-",
        df.loc[topper_index, subject],
        "Marks"
    )

# ==========================================================
# SEMESTER ANALYSIS
# ==========================================================

print("\n")
print("=" * 70)
print("SEMESTER WISE ANALYSIS")
print("=" * 70)

semester_analysis = df.groupby("Semester")[
    ["Maths", "Science", "English", "Average"]
].mean()

print(semester_analysis)

# ==========================================================
# GRADE DISTRIBUTION
# ==========================================================

print("\n")
print("=" * 70)
print("GRADE DISTRIBUTION")
print("=" * 70)

print(df["Grade"].value_counts())

# ==========================================================
# SAVE CSV REPORT
# ==========================================================

df.to_csv(
    "student_marks_report.csv",
    index=False
)

print("\nCSV Report Saved Successfully!")

# ==========================================================
# GRAPH 1
# STUDENT AVERAGE MARKS
# ==========================================================

plt.figure(figsize=(12, 6))

plt.bar(
    df["Student Name"],
    df["Average"]
)

plt.title("Average Marks of Students")
plt.xlabel("Student Name")
plt.ylabel("Average Marks")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("average_marks_graph.png")

plt.show()

# ==========================================================
# GRAPH 2
# GRADE DISTRIBUTION PIE CHART
# ==========================================================

grade_count = df["Grade"].value_counts()

plt.figure(figsize=(8, 8))

plt.pie(
    grade_count,
    labels=grade_count.index,
    autopct="%1.1f%%"
)

plt.title("Grade Distribution")

plt.savefig("grade_distribution.png")

plt.show()

# ==========================================================
# GRAPH 3
# SEMESTER WISE PERFORMANCE
# ==========================================================

semester_avg = df.groupby("Semester")["Average"].mean()

plt.figure(figsize=(8, 5))

plt.plot(
    semester_avg.index,
    semester_avg.values,
    marker="o"
)

plt.title("Semester Wise Average Performance")
plt.xlabel("Semester")
plt.ylabel("Average Marks")

plt.grid(True)

plt.savefig("semester_performance.png")

plt.show()

# ==========================================================
# GRAPH 4
# SUBJECT WISE AVERAGE MARKS
# ==========================================================

subject_avg = [
    df["Maths"].mean(),
    df["Science"].mean(),
    df["English"].mean()
]

subject_names = [
    "Maths",
    "Science",
    "English"
]

plt.figure(figsize=(8, 5))

plt.bar(
    subject_names,
    subject_avg
)

plt.title("Subject Wise Average Marks")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")

plt.savefig("subject_average.png")

plt.show()

# ==========================================================
# GRAPH 5
# TOP 5 STUDENTS
# ==========================================================

top5 = df.sort_values(
    by="Total",
    ascending=False
).head(5)

plt.figure(figsize=(10, 5))

plt.bar(
    top5["Student Name"],
    top5["Total"]
)

plt.title("Top 5 Students")
plt.xlabel("Student Name")
plt.ylabel("Total Marks")

plt.xticks(rotation=25)

plt.tight_layout()

plt.savefig("top5_students.png")

plt.show()

# ==========================================================
# GRAPH 6
# SUBJECT COMPARISON
# ==========================================================

x = np.arange(len(df))

width = 0.25

plt.figure(figsize=(14, 6))

plt.bar(
    x - width,
    df["Maths"],
    width,
    label="Maths"
)

plt.bar(
    x,
    df["Science"],
    width,
    label="Science"
)

plt.bar(
    x + width,
    df["English"],
    width,
    label="English"
)

plt.xticks(
    x,
    df["Student Name"],
    rotation=45
)

plt.title("Student Subject Comparison")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.legend()

plt.tight_layout()

plt.savefig("subject_comparison.png")

plt.show()

# ==========================================================
# GRAPH 7
# HISTOGRAM OF AVERAGE MARKS
# ==========================================================

plt.figure(figsize=(8, 5))

plt.hist(
    df["Average"],
    bins=5
)

plt.title("Distribution of Average Marks")
plt.xlabel("Average Marks")
plt.ylabel("Number of Students")

plt.savefig("average_histogram.png")

plt.show()

# ==========================================================
# PROJECT COMPLETION MESSAGE
# ==========================================================

print("\n")
print("=" * 70)
print("PROJECT COMPLETED SUCCESSFULLY")
print("=" * 70)

print("\nGenerated Files:")
print("1. student_marks_report.csv")
print("2. average_marks_graph.png")
print("3. grade_distribution.png")
print("4. semester_performance.png")
print("5. subject_average.png")
print("6. top5_students.png")
print("7. subject_comparison.png")
print("8. average_histogram.png")

print("\nThank You!")
