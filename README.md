# Zinemaker

A script that rearranges electronic zines. Print and read!

## Schematic

```plaintext
+-----+            +-----+
|  p  1            | qqq 4
+-----+            + - - +
| p p 2            | ppp 5
+-----+            +-----+
| q q 3            | d d 3
+-----+            + - - +
| qqq 4            | b b 6
+-----+    --->    +-----+
| ppp 5            | p p 2
+-----+            + - - +
| p p 6            | q q 7
+-----+            +-----+
| q q 7            |  d  1
+-----+            + - - +
|  q  8            |  b  8
+-----+            +-----+
```

## Usage

```py
uv run zine.py input.pdf output.pdf
```
