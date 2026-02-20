---
name: ascii-to-diagram-skill
description: Converts text-based ASCII art, system architectures, and flowcharts in Markdown documents into beautiful Mermaid.js-based PNG image captures.
---
# ASCII to Diagram Converter

This skill converts text-based ASCII art, system architectures, and flowcharts within Markdown documents into styled Mermaid.js diagrams, rendered and embedded as PNG images.

## Instructions

When the user asks to convert ASCII art or text-based diagrams in a Markdown document into Mermaid.js PNG diagrams, strictly follow these steps:

### Phase 1: Analyze and Generate HTML Template
1. **Analyze** the text/ASCII diagram from the user's document to understand its core nodes, connections, and flow.
2. **Convert** the diagram into valid, optimized Mermaid.js graph code.
3. **Generate** an HTML file (e.g., `<diagram-name>.html`) to wrap the Mermaid code. 
4. Inject the Mermaid code inside the `<div class="mermaid">` block of the following Premium Theme HTML Template. Do not output only the Mermaid code block in chat.

**Premium Theme HTML Template:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Mermaid Diagram</title>
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
    <style>
        body {
            background-color: transparent;
            margin: 0;
            padding: 20px;
            display: inline-block;
        }
        .mermaid {
            background-color: transparent;
        }
    </style>
    <script>
        mermaid.initialize({
            startOnLoad: true,
            theme: 'base',
            themeVariables: {
                primaryColor: '#f8fafc',
                primaryBorderColor: '#64748b',
                primaryTextColor: '#1e293b',
                lineColor: '#94a3b8',
                fontFamily: '-apple-system, Roboto, sans-serif'
            },
            flowchart: { curve: 'basis' }
        });
    </script>
</head>
<body>
    <div class="mermaid">
<!-- INJECT_MERMAID_CODE_HERE -->
    </div>
</body>
</html>
```

### Phase 2: Image Capture
1. Use the Python script `capture_diagram.py` provided in this skill folder to headlessly render the generated HTML and capture it as a tightly cropped `.png` image.
2. Run the command:
   ```bash
   python capture_diagram.py <html-path> <png-path>
   ```
   (Replace `<html-path>` with your generated `.html` path, and `<png-path>` with the target `.png` path).

### Phase 3: Markdown Replacement
1. **Verify** that the generated PNG file exists on the disk and its size is greater than 0 bytes (a normal capacity).
2. **Modify** the user's original Markdown document. Delete the existing ASCII art portion and replace it with a markdown image embed in the format: `![설명](./경로.png)`.
3. (Optional) Delete the intermediate `.html` file and keep the workspace clean.
