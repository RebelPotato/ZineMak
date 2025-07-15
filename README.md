# Zinemaker

A script that rearranges electronic zines. Print and read!

## Schematic

```plaintext
+-----+            +-----+
|  p  |            |  q  |
+-----+            + - - +
| p p |            |  p  |
+-----+            +-----+
| q q |            | b b |
+-----+            + - - +
|  q  |            | d d |
+-----+    --->    +-----+
|  p  |            | p p |
+-----+            + - - +
| p p |            | q q |
+-----+            +-----+
| q q |            |  b  |
+-----+            + - - +
|  q  |            |  d  |
+-----+            +-----+
```

## Usage

```py
uv run zine.py input.pdf output.pdf
```
