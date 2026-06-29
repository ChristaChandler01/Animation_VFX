# Animation_VFX
This is where I will put all my scripts and tools for animation and VFX workflows.

# Tool Placement and Pipeline Structure

This repository uses a production-oriented folder layout designed for clarity and scalability:
    
    - Single-application tools are placed directly inside their corresponding DCC folders 
    to keep them isolated, simple, and easy to maintain.
    
    - Cross-DCC workflow tools are housed under PipelineTools/ in their own top-level directory. 
    Each of these tools includes sub-folders for the supported DCCs (e.g., Maya, Nuke, Houdini) 
    as well as shared modules, documentation, and tests.

This approach reflects standard studio pipeline practices and supports future expansion into 
additional DCCs, shared libraries, and unified workflows.
