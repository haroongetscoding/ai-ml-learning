"""
=============================================================
 MATPLOTLIB & SEABORN - DATA VISUALIZATION
=============================================================
 Repository: ai-ml-learning
 GitHub: https://github.com/haroongetscoding/ai-ml-learning
 
 Visualization is crucial for understanding data and
 presenting ML results.
=============================================================
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

print("=" * 60)
print(" MATPLOTLIB & SEABORN - VISUALIZATION")
print("=" * 60)


# ============================================================
# SECTION 1: MATPLOTLIB BASICS
# ============================================================

print("\n--- SECTION 1: MATPLOTLIB BASICS ---\n")

# Line Plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, label="sin(x)", color="blue", linewidth=2)
plt.plot(x, np.cos(x), label="cos(x)", color="red", linestyle="--")
plt.title("Trigonometric Functions", fontsize=16)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig("line_plot.png", dpi=100, bbox_inches="tight")
plt.close()
print("Saved: line_plot.png")


# ============================================================
# SECTION 2: SCATTER PLOT
# ============================================================

print("\n--- SECTION 2: SCATTER PLOT ---\n")

np.random.seed(42)
x = np.random.rand(50) * 100
y = x * 0.8 + np.random.randn(50) * 10

plt.figure(figsize=(10, 6))
plt.scatter(x, y, c=y, cmap="viridis", s=100, alpha=0.7, edgecolors="black")
plt.colorbar(label="Y Value")
plt.title("Scatter Plot: Study Hours vs Exam Score", fontsize=14)
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.savefig("scatter_plot.png", dpi=100, bbox_inches="tight")
plt.close()
print("Saved: scatter_plot.png")


# ============================================================
# SECTION 3: BAR PLOT
# ============================================================

print("\n--- SECTION 3: BAR PLOT ---\n")

departments = ["CS", "AI", "Data Science", "SE"]
students = [45, 38, 52, 41]

plt.figure(figsize=(10, 6))
bars = plt.bar(departments, students, color=["#3498db", "#e74c3c", "#2ecc71", "#f39c12"])
plt.title("Students per Department", fontsize=14)
plt.xlabel("Department")
plt.ylabel("Number of Students")

# Add value labels on bars
for bar, val in zip(bars, students):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
             str(val), ha="center", fontweight="bold")

plt.savefig("bar_plot.png", dpi=100, bbox_inches="tight")
plt.close()
print("Saved: bar_plot.png")


# ============================================================
# SECTION 4: HISTOGRAM
# ============================================================

print("\n--- SECTION 4: HISTOGRAM ---\n")

np.random.seed(42)
cgpa_data = np.random.normal(3.2, 0.5, 200)
cgpa_data = np.clip(cgpa_data, 0, 4)

plt.figure(figsize=(10, 6))
plt.hist(cgpa_data, bins=20, color="#9b59b6", edgecolor="black", alpha=0.7)
plt.axvline(cgpa_data.mean(), color="red", linestyle="--", label=f"Mean: {cgpa_data.mean():.2f}")
plt.title("CGPA Distribution", fontsize=14)
plt.xlabel("CGPA")
plt.ylabel("Frequency")
plt.legend()
plt.savefig("histogram.png", dpi=100, bbox_inches="tight")
plt.close()
print("Saved: histogram.png")


# ============================================================
# SECTION 5: PIE CHART
# ============================================================

print("\n--- SECTION 5: PIE CHART ---\n")

languages = ["Python", "JavaScript", "Java", "C++", "Others"]
usage = [35, 25, 20, 12, 8]
colors = ["#3498db", "#f1c40f", "#e74c3c", "#1abc9c", "#95a5a6"]
explode = (0.1, 0, 0, 0, 0)

plt.figure(figsize=(8, 8))
plt.pie(usage, labels=languages, colors=colors, explode=explode,
        autopct="%1.1f%%", shadow=True, startangle=90)
plt.title("Programming Language Popularity", fontsize=14)
plt.savefig("pie_chart.png", dpi=100, bbox_inches="tight")
plt.close()
print("Saved: pie_chart.png")


# ============================================================
# SECTION 6: SUBPLOTS
# ============================================================

print("\n--- SECTION 6: SUBPLOTS ---\n")

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Plot 1: Line
x = np.linspace(0, 10, 50)
axes[0, 0].plot(x, np.sin(x), "b-", label="sin")
axes[0, 0].plot(x, np.cos(x), "r--", label="cos")
axes[0, 0].set_title("Trigonometric")
axes[0, 0].legend()

# Plot 2: Scatter
axes[0, 1].scatter(np.random.rand(30), np.random.rand(30), c="green", s=50)
axes[0, 1].set_title("Random Scatter")

# Plot 3: Bar
axes[1, 0].bar(["A", "B", "C", "D"], [23, 45, 56, 78], color="orange")
axes[1, 0].set_title("Bar Chart")

# Plot 4: Histogram
axes[1, 1].hist(np.random.randn(100), bins=15, color="purple", alpha=0.7)
axes[1, 1].set_title("Normal Distribution")

plt.tight_layout()
plt.savefig("subplots.png", dpi=100, bbox_inches="tight")
plt.close()
print("Saved: subplots.png")


# ============================================================
# SECTION 7: SEABORN - STATISTICAL VIZ
# ============================================================

print("\n--- SECTION 7: SEABORN ---\n")

# Set style
sns.set_style("whitegrid")
sns.set_palette("husl")

# Create dataset
np.random.seed(42)
n = 200
df = pd.DataFrame({
    "Study Hours": np.random.uniform(1, 10, n),
    "CGPA": np.random.uniform(2.0, 4.0, n),
    "Department": np.random.choice(["CS", "AI", "DS"], n),
    "Pass": np.random.choice(["Pass", "Fail"], n, p=[0.7, 0.3])
})
df["Score"] = df["Study Hours"] * 8 + np.random.randn(n) * 5

# Seaborn line plot
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x="Study Hours", y="Score", hue="Department", style="Department")
plt.title("Study Hours vs Score by Department")
plt.savefig("seaborn_line.png", dpi=100, bbox_inches="tight")
plt.close()
print("Saved: seaborn_line.png")

# Seaborn box plot
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x="Department", y="CGPA", palette="Set2")
plt.title("CGPA Distribution by Department")
plt.savefig("seaborn_box.png", dpi=100, bbox_inches="tight")
plt.close()
print("Saved: seaborn_box.png")

# Seaborn heatmap
plt.figure(figsize=(8, 6))
corr = df[["Study Hours", "CGPA", "Score"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", center=0, fmt=".2f")
plt.title("Correlation Heatmap")
plt.savefig("seaborn_heatmap.png", dpi=100, bbox_inches="tight")
plt.close()
print("Saved: seaborn_heatmap.png")

# Seaborn pair plot
plt.figure(figsize=(10, 8))
sns.pairplot(df[["Study Hours", "CGPA", "Score", "Department"]],
             hue="Department", diag_kind="kde")
plt.savefig("seaborn_pairplot.png", dpi=100, bbox_inches="tight")
plt.close()
print("Saved: seaborn_pairplot.png")

# Seaborn count plot
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="Department", hue="Pass", palette="coolwarm")
plt.title("Pass/Fail by Department")
plt.savefig("seaborn_count.png", dpi=100, bbox_inches="tight")
plt.close()
print("Saved: seaborn_count.png")


# ============================================================
# SECTION 8: CUSTOMIZATION TIPS
# ============================================================

print("\n--- SECTION 8: CUSTOMIZATION ---\n")

# Custom style
plt.style.use("seaborn-v0_8-darkgrid")

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Before customization
axes[0].plot(np.random.rand(10), "b-", linewidth=2)
axes[0].set_title("Basic Plot")

# After customization
axes[1].plot(np.random.rand(10), "r-o", linewidth=2, markersize=8,
             markerfacecolor="yellow", markeredgecolor="black")
axes[1].set_title("Customized Plot", fontsize=16, fontweight="bold", color="darkblue")
axes[1].set_xlabel("X", fontsize=12, style="italic")
axes[1].set_ylabel("Y", fontsize=12, style="italic")
axes[1].grid(True, linestyle="--", alpha=0.7)
axes[1].set_facecolor("#f0f0f0")

plt.tight_layout()
plt.savefig("customization.png", dpi=100, bbox_inches="tight")
plt.close()
print("Saved: customization.png")


# ============================================================
# SECTION 9: PRACTICAL ML VISUALIZATION
# ============================================================

print("\n--- SECTION 9: ML VISUALIZATION ---\n")

# Linear Regression Visualization
np.random.seed(42)
X = np.random.rand(50, 1) * 10
y = 3 * X + 5 + np.random.randn(50, 1) * 2

# Fit line
m = np.sum((X - X.mean()) * (y - y.mean())) / np.sum((X - X.mean()) ** 2)
b = y.mean() - m * X.mean()

plt.figure(figsize=(10, 6))
plt.scatter(X, y, alpha=0.6, label="Data Points")
plt.plot(X, m * X + b, color="red", linewidth=2, label=f"y = {m:.2f}x + {b:.2f}")
plt.xlabel("X")
plt.ylabel("y")
plt.title("Linear Regression Visualization")
plt.legend()
plt.savefig("ml_regression.png", dpi=100, bbox_inches="tight")
plt.close()
print("Saved: ml_regression.png")

# Decision Boundary Visualization (conceptual)
from matplotlib.colors import ListedColormap

np.random.seed(42)
X1 = np.random.randn(100, 2)
y1 = (X1[:, 0] ** 2 + X1[:, 1] ** 2 < 1).astype(int)

plt.figure(figsize=(8, 8))
plt.scatter(X1[y1 == 0, 0], X1[y1 == 0, 1], c="red", label="Class 0", alpha=0.6)
plt.scatter(X1[y1 == 1, 0], X1[y1 == 1, 1], c="blue", label="Class 1", alpha=0.6)
theta = np.linspace(0, 2 * np.pi, 100)
plt.plot(np.cos(theta), np.sin(theta), "g--", linewidth=2, label="Decision Boundary")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Classification Visualization")
plt.legend()
plt.savefig("ml_classification.png", dpi=100, bbox_inches="tight")
plt.close()
print("Saved: ml_classification.png")


# ============================================================
# CLEANUP IMAGE FILES
# ============================================================

import os
image_files = [
    "line_plot.png", "scatter_plot.png", "bar_plot.png",
    "histogram.png", "pie_chart.png", "subplots.png",
    "seaborn_line.png", "seaborn_box.png", "seaborn_heatmap.png",
    "seaborn_pairplot.png", "seaborn_count.png", "customization.png",
    "ml_regression.png", "ml_classification.png"
]

for file in image_files:
    if os.path.exists(file):
        os.remove(file)

print("\nCleaned up image files!")


# ============================================================
# SUMMARY
# ============================================================

print("\n" + "=" * 60)
print(" VISUALIZATION COMPLETE!")
print("=" * 60)
print("\n Key Takeaways:")
print("  1. Matplotlib: Low-level, full control")
print("  2. Seaborn: High-level, statistical plots")
print("  3. Always label axes and add titles")
print("  4. Use appropriate plot for your data")
print("  5. Save plots with dpi=100 for quality")
print("\n You're ready for AI/ML!")
print("=" * 60)
