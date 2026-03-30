# ComfyUI Image Hold Last

A minimal ComfyUI custom node that acts as an image passthrough — and holds the last received image when the upstream connection is bypassed or missing.

## What it does

| Situation | Output |
|---|---|
| Image is connected and flowing | Passes the image through and caches it |
| Upstream node is bypassed / disconnected | Returns the last cached image |
| No image has ever been received | Returns a 1×1 black pixel (safe fallback) |

This is useful in workflows where you conditionally bypass a generation node (e.g. a sampler or loader) and want downstream nodes to keep working with the previous result instead of receiving nothing.

## Installation

### Via ComfyUI Manager
Search for **Image Hold Last** in the Custom Nodes Manager and install.

### Manual
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/SeBL4RD/comfyui-image-hold-last
```

No extra dependencies required.

## Usage

1. Add the **Image Hold Last** node (found under `utils`).
2. Connect any `IMAGE` output to its optional `image` input.
3. Connect its output to your downstream nodes.

When the upstream node is muted or bypassed, the node silently replays the last image it received.

## Node reference

| | |
|---|---|
| **Input** | `image` (IMAGE, optional) |
| **Output** | `IMAGE` |
| **Category** | `utils` |
| **Display name** | Image Hold Last |

## Known limitation

If you use **multiple instances** of this node in the same workflow, they share a single internal cache. The last node to receive an image will overwrite the cache for all instances. Use one instance per pipeline branch to avoid conflicts.

## License

See [LICENSE](LICENSE).
