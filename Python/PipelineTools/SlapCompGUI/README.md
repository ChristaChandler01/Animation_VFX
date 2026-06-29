# SlapCompGUI

SlapCompGUI is a cross-DCC slap-comp pipeline tool designed to streamline the process of previewing
CG assets and animated Maya scenes inside Nuke. The tool renders Arnold AOVs from Maya, extracts
camera animation, and automatically builds a multipass composite in Nuke, complete with optional
Grade and Glow effects, over a user-defined background image.

This workflow allows artists to quickly evaluate lighting, animation, and AOV behavior without
waiting for full production composites.

## Cross-Platform Support (Windows + macOS)

SlapCompGUI was developed on Windows but has been tested and verified to run on macOS without
modification. The tool uses platform-agnostic Python, Maya commands, and Nuke process calls, 
allowing artists on both operating systems to generate slap comps using the same workflow.

This makes the tool ideal for classrooms, mixed-OS labs, and studio environments where artists
may work across different platforms.

## How It Works

1. **In Maya**
    - Select your camera, frame range, resolution, and Arnold AOVs.
    - Optionally enable Grade or Golow adjustments.
    - Render the CG asset or scene using Arnold.
    - Camera animation is sampled per-frame and passed to Nuke.

2. **In Nuke**
    - A multipass composite is built using Shuffle2 and Merge nodes.
    - Emission AOVs can receive Glow effects.
    - Diffuse AOVs can receive Grade adjustments.
    - A background image is projected onto a sphere and rendered with the imported camera.
    - The final composite is rendered to disk.

This creates a fast, artist-friendly slap comp for reviewing CG elements over a chosen
background plate.

## Launching in Maya

Create a shelf button with the following Python code:
import SlapComp_Launcher as sl
sl.launch()
