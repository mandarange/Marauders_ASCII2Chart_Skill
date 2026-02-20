# ASCII to Diagram Skill (`ascii-to-diagram-skill`)

A specialized **Antigravity IDE Creator Skill** that transforms text-based ASCII art, system architectures, and flowcharts found in Markdown documents into beautiful, styled Mermaid.js PNG diagrams.

## 🌟 Features
- **Smart Parsing & Conversion:** Intelligently analyzes text-based ASCII art and translates it into accurate, optimized Mermaid.js node/edge syntax.
- **Premium Aesthetics:** Injects the Mermaid diagram into a clean, modern HTML template pre-configured with a custom premium theme (`primaryColor: #f8fafc`, `fontFamily: Roboto`, etc.).
- **Headless High-Res Capture:** Leverages a Playwright-based Python script (`capture_diagram.py`) to render the diagram headlessly, capture it at a Retina-level resolution (`device_scale_factor=2`), and tightly crop the output.
- **Seamless Markdown Integration:** Automatically replaces the old ASCII text block in your Markdown document with an embedded image link `![text](./path.png)` pointing to the generated PNG asset.

## 🛠 Prerequisites

To use the automated capture script natively on your machine, ensure you have Python and Playwright installed:

```bash
pip install playwright
playwright install chromium
```

## 📂 Project Structure

- `SKILL.md`: The core Antigravity IDE skill definition. Contains YAML frontmatter and precise instructions (Phases 1-3) instructing the AI on how to process the text and execute the workflow.
- `capture_diagram.py`: The headless wrapper script used by the AI. It takes an HTML file path and an output PNG file path, renders the HTML using Chromium, crops the SVG bounding box, and saves the image.

## 🚀 How it Works (Under the Hood)

1. **Phase 1 (HTML Gen):** The skill parses the ASCII art in the markdown and creates a `.html` file injecting the translated Mermaid code into a styled `div`.
2. **Phase 2 (Capture):** The skill runs `python capture_diagram.py <diagram>.html <diagram>.png` to generate the image asset.
3. **Phase 3 (Embed):** Verify the newly generated `.png` size, then delete the old ASCII lines from the Markdown file and insert the standard Markdown image embed code.
