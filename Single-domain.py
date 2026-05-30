import tkinter as tk
from tkinter import filedialog, messagebox

FREQ = 765e3
FACTOR_H = 1.25e-6
FACTOR_M = 1 / 5300


def read_loop_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        raw = f.read().strip()

    blocks = [b.strip() for b in raw.split("\n\n") if b.strip()]

    if len(blocks) < 2:
        raise ValueError("The file must contain 2 branches separated by a blank line.")

    def parse_block(block):
        data = []
        for line in block.splitlines():
            parts = line.strip().split()
            if len(parts) < 2:
                continue
            try:
                h = float(parts[0])
                m = float(parts[1])
                data.append((h, m))
            except ValueError:
                continue
        return data

    branch1 = parse_block(blocks[0])
    branch2 = parse_block(blocks[1])

    if not branch1 or not branch2:
        raise ValueError("The two branches could not be read correctly.")

    return branch1, branch2


def convert_branches(branch1, branch2):
    conv1 = [(h * FACTOR_H, m * FACTOR_M) for h, m in branch1]
    conv2 = [(h * FACTOR_H, m * FACTOR_M) for h, m in branch2]
    return conv1, conv2


def interpolate_zero_crossing_h(data):
    for i in range(len(data) - 1):
        h1, m1 = data[i]
        h2, m2 = data[i + 1]

        if m1 == 0:
            return h1
        if m2 == 0:
            return h2
        if m1 * m2 < 0:
            return h1 - m1 * (h2 - h1) / (m2 - m1)

    return None


def interpolate_m_at_h0(data):
    for i in range(len(data) - 1):
        h1, m1 = data[i]
        h2, m2 = data[i + 1]

        if h1 == 0:
            return m1
        if h2 == 0:
            return m2
        if h1 * h2 < 0:
            return m1 + (0 - h1) * (m2 - m1) / (h2 - h1)

    return None


def slope_at_h0(data):
    for i in range(len(data) - 1):
        h1, m1 = data[i]
        h2, m2 = data[i + 1]

        if h2 == h1:
            continue

        if h1 == 0 or h2 == 0 or h1 * h2 < 0:
            return (m2 - m1) / (h2 - h1)

    return None


def loop_area_from_branches(branch1, branch2):
    loop = list(branch1) + list(reversed(branch2))

    if len(loop) < 3:
        return None

    if loop[0] != loop[-1]:
        loop.append(loop[0])

    area = 0.0

    for i in range(len(loop) - 1):
        x1, y1 = loop[i]
        x2, y2 = loop[i + 1]
        area += x1 * y2 - x2 * y1

    return abs(area) / 2.0


def analyze_converted_loop(branch1, branch2):
    ms1 = max(abs(m) for _, m in branch1)
    ms2 = max(abs(m) for _, m in branch2)
    ms = (abs(ms1) + abs(ms2)) / 2.0

    mr1 = interpolate_m_at_h0(branch1)
    mr2 = interpolate_m_at_h0(branch2)
    mr = None if (mr1 is None or mr2 is None) else (abs(mr1) + abs(mr2)) / 2.0

    hc1 = interpolate_zero_crossing_h(branch1)
    hc2 = interpolate_zero_crossing_h(branch2)
    hc = None if (hc1 is None or hc2 is None) else (abs(hc1) + abs(hc2)) / 2.0

    slope1 = slope_at_h0(branch1)
    slope2 = slope_at_h0(branch2)
    slope = None if (slope1 is None or slope2 is None) else (abs(slope1) + abs(slope2)) / 2.0

    area = loop_area_from_branches(branch1, branch2)
    slp = None if area is None else FREQ * area / 1000.0

    return {
        "Hc1 (T)": hc1,
        "Hc2 (T)": hc2,
        "Hc (T)": hc,
        "Mr1 (Am²/kg)": mr1,
        "Mr2 (Am²/kg)": mr2,
        "Mr (Am²/kg)": mr,
        "Ms1 (Am²/kg)": ms1,
        "Ms2 (Am²/kg)": ms2,
        "Ms (Am²/kg)": ms,
        "Slope1": slope1,
        "Slope2": slope2,
        "Slope": slope,
        "Area (J/kg)": area,
        "SLP (W/g)": slp,
    }


def save_converted_file(output_path, branch1, branch2):
    with open(output_path, "w", encoding="utf-8") as f:
        for h, m in branch1:
            f.write(f"{h:.12f}\t{m:.12f}\n")

        f.write("\n")

        for h, m in branch2:
            f.write(f"{h:.12f}\t{m:.12f}\n")


def print_results(results):
    print("\n--- LOOP ANALYSIS RESULTS ---")

    for key, value in results.items():
        if value is None:
            print(f"{key}: not found")
        else:
            print(f"{key}: {value:.10f}")


def main():
    root = tk.Tk()
    root.withdraw()

    input_file = filedialog.askopenfilename(
        title="Select the TXT file",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )

    if not input_file:
        print("No file was selected.")
        return

    try:
        branch1, branch2 = read_loop_file(input_file)

        conv1, conv2 = convert_branches(branch1, branch2)

        results = analyze_converted_loop(conv1, conv2)

        print_results(results)

    except Exception as e:
        messagebox.showerror("Error", str(e))
        return

    save_choice = messagebox.askyesno(
        title="Save",
        message="Do you want to save the converted file as well?"
    )

    if save_choice:
        output_file = filedialog.asksaveasfilename(
            title="Save Converted File",
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )

        if output_file:
            save_converted_file(output_file, conv1, conv2)

            print(f"\n✔ Converted file saved:\n{output_file}")


if __name__ == "__main__":
    main()