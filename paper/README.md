# Research Paper Manuscript

This directory contains the complete LaTeX source and publication-ready compiled PDF for:

**"An IoT-Based Infrastructure Model for Reducing Urban Light Pollution: Empirical Assessment and System Design in Dhaka"**

**Authors:**
- **Md Reyad Hasan** (Corresponding Author: `reyadh418@gmail.com`) — *Government Science College, Dhaka, Bangladesh*
- **Ishrat Jahan Riya** (`ishratjahanriya123@gmail.com`) — *Mavenwood International School, Dhaka, Bangladesh*

**Date:** August 23, 2026

---

## 📄 Files

| File | Description |
| :--- | :--- |
| [`finalPaper.tex`](file:///c:/Code/Light-Pollution/paper/finalPaper.tex) | Complete self-contained LaTeX source code including document preamble, mathematical formulations, 8 detailed statistical tables, TikZ hardware architecture diagram, and bibliography. |
| [`Light_Pollution.pdf`](file:///c:/Code/Light-Pollution/paper/Light_Pollution.pdf) | Compiled 21-page publication-ready PDF document. |

---

## 🛠️ How to Compile `finalPaper.tex`

### Prerequisites
A modern TeX distribution such as **TeX Live**, **MikTeX**, or **MacTeX**, containing standard packages:
- `geometry`, `amsmath`, `amssymb`, `booktabs`, `tabularx`, `array`, `graphicx`, `hyperref`, `authblk`, `caption`, `float`, `tikz`, `makecell`, `microtype`.

### Compilation Command

Using `latexmk` (recommended):
```bash
latexmk -pdf finalPaper.tex
```

Or using standard multi-pass `pdflatex`:
```bash
pdflatex finalPaper.tex
pdflatex finalPaper.tex
```

*(Two passes are recommended to properly resolve all internal section labels, mathematical cross-references, and Table IDs).*

