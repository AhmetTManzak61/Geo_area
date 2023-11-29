import math
import tkinter as tk
from tkinter import ttk

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def calculate_rectangle_area(length, width):
    return length * width

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def calculate_square_area(side):
    return side ** 2

def calculate_ellipse_area(a, b):
    return math.pi * a * b

def calculate_parallelogram_area(base, height):
    return base * height

def calculate_trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

def calculate_regular_polygon_area(apothem, side_length, num_sides):
    return 0.5 * apothem * side_length * num_sides

def calculate_area():
    choice = shape_var.get()

    if choice == 'Circle':
        radius = float(radius_entry.get())
        area = calculate_circle_area(radius)
        result_var.set(f"The area of the circle is: {area}")
    elif choice == 'Rectangle':
        length = float(length_entry.get())
        width = float(width_entry.get())
        area = calculate_rectangle_area(length, width)
        result_var.set(f"The area of the rectangle is: {area}")
    elif choice == 'Triangle':
        base = float(base_entry.get())
        height = float(height_entry.get())
        area = calculate_triangle_area(base, height)
        result_var.set(f"The area of the triangle is: {area}")
    elif choice == 'Square':
        side = float(side_entry.get())
        area = calculate_square_area(side)
        result_var.set(f"The area of the square is: {area}")
    elif choice == 'Ellipse':
        a = float(semi_major_entry.get())
        b = float(semi_minor_entry.get())
        area = calculate_ellipse_area(a, b)
        result_var.set(f"The area of the ellipse is: {area}")
    elif choice == 'Parallelogram':
        base = float(parallelogram_base_entry.get())
        height = float(parallelogram_height_entry.get())
        area = calculate_parallelogram_area(base, height)
        result_var.set(f"The area of the parallelogram is: {area}")
    elif choice == 'Trapezoid':
        base1 = float(trapezoid_base1_entry.get())
        base2 = float(trapezoid_base2_entry.get())
        height = float(trapezoid_height_entry.get())
        area = calculate_trapezoid_area(base1, base2, height)
        result_var.set(f"The area of the trapezoid is: {area}")
    elif choice == 'Regular Polygon':
        apothem = float(regular_polygon_apothem_entry.get())
        side_length = float(regular_polygon_side_length_entry.get())
        num_sides = float(regular_polygon_num_sides_entry.get())
        area = calculate_regular_polygon_area(apothem, side_length, num_sides)
        result_var.set(f"The area of the regular polygon is: {area}")
    else:
        result_var.set("Invalid choice. Please choose a valid option.")


window = tk.Tk()
window.title("Geometric Shapes Area Calculator")


notebook = ttk.Notebook(window)
notebook.pack(pady=10)


circle_frame = ttk.Frame(notebook)
rectangle_frame = ttk.Frame(notebook)
triangle_frame = ttk.Frame(notebook)
square_frame = ttk.Frame(notebook)
ellipse_frame = ttk.Frame(notebook)
parallelogram_frame = ttk.Frame(notebook)
trapezoid_frame = ttk.Frame(notebook)
regular_polygon_frame = ttk.Frame(notebook)


notebook.add(circle_frame, text="Circle")
notebook.add(rectangle_frame, text="Rectangle")
notebook.add(triangle_frame, text="Triangle")
notebook.add(square_frame, text="Square")
notebook.add(ellipse_frame, text="Ellipse")
notebook.add(parallelogram_frame, text="Parallelogram")
notebook.add(trapezoid_frame, text="Trapezoid")
notebook.add(regular_polygon_frame, text="Regular Polygon")


shape_var = tk.StringVar()
result_var = tk.StringVar()


tk.Label(circle_frame, text="Enter the radius:").pack()
radius_entry = tk.Entry(circle_frame)
radius_entry.pack()
tk.Button(circle_frame, text="Calculate", command=calculate_area).pack()


tk.Label(rectangle_frame, text="Enter the length:").pack()
length_entry = tk.Entry(rectangle_frame)
length_entry.pack()
tk.Label(rectangle_frame, text="Enter the width:").pack()
width_entry = tk.Entry(rectangle_frame)
width_entry.pack()
tk.Button(rectangle_frame, text="Calculate", command=calculate_area).pack()


tk.Label(triangle_frame, text="Enter the base:").pack()
base_entry = tk.Entry(triangle_frame)
base_entry.pack()
tk.Label(triangle_frame, text="Enter the height:").pack()
height_entry = tk.Entry(triangle_frame)
height_entry.pack()
tk.Button(triangle_frame, text="Calculate", command=calculate_area).pack()


tk.Label(square_frame, text="Enter the side length:").pack()
side_entry = tk.Entry(square_frame)
side_entry.pack()
tk.Button(square_frame, text="Calculate", command=calculate_area).pack()


tk.Label(ellipse_frame, text="Enter the semi-major axis:").pack()
semi_major_entry = tk.Entry(ellipse_frame)
semi_major_entry.pack()
tk.Label(ellipse_frame, text="Enter the semi-minor axis:").pack()
semi_minor_entry = tk.Entry(ellipse_frame)
semi_minor_entry.pack()
tk.Button(ellipse_frame, text="Calculate", command=calculate_area).pack()


tk.Label(parallelogram_frame, text="Enter the base:").pack()
parallelogram_base_entry = tk.Entry(parallelogram_frame)
parallelogram_base_entry.pack()
tk.Label(parallelogram_frame, text="Enter the height:").pack()
parallelogram_height_entry = tk.Entry(parallelogram_frame)
parallelogram_height_entry.pack()
tk.Button(parallelogram_frame, text="Calculate", command=calculate_area).pack()


tk.Label(trapezoid_frame, text="Enter the length of the first base:").pack()
trapezoid_base1_entry = tk.Entry(trapezoid_frame)
trapezoid_base1_entry.pack()
tk.Label(trapezoid_frame, text="Enter the length of the second base:").pack()
trapezoid_base2_entry = tk.Entry(trapezoid_frame)
trapezoid_base2_entry.pack()
tk.Label(trapezoid_frame, text="Enter the height:").pack()
trapezoid_height_entry = tk.Entry(trapezoid_frame)
trapezoid_height_entry.pack()
tk.Button(trapezoid_frame, text="Calculate", command=calculate_area).pack()

tk.Label(regular_polygon_frame, text="Enter the apothem:").pack()
regular_polygon_apothem_entry = tk.Entry(regular_polygon_frame)
regular_polygon_apothem_entry.pack()
tk.Label(regular_polygon_frame, text="Enter the side length:").pack()
regular_polygon_side_length_entry = tk.Entry(regular_polygon_frame)
regular_polygon_side_length_entry.pack()
tk.Label(regular_polygon_frame, text="Enter the number of sides:").pack()
regular_polygon_num_sides_entry = tk.Entry(regular_polygon_frame)
regular_polygon_num_sides_entry.pack()
tk.Button(regular_polygon_frame, text="Calculate", command=calculate_area).pack()


result_label = tk.Label(window, textvariable=result_var)
result_label.pack(pady=10)

window.mainloop()
