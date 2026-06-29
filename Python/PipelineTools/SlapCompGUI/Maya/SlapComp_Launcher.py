# Save this file as SlapComp_Launcher.py in your Maya scripts directory. This script is used 
# to launch the SlapComp GUI and ensure that the latest edits to the GUI and quick composite 
# modules are used.


# Import necessary modules
import importlib
import GUI_SlapComp as GUI
import quick_composite as qc


def launch():
    """
    Description:
        Launches the SlapComp GUI, initializes the quick composite module, and reloads the 
        modules to ensure the latest edits are used.
    Parameters:
        None
    Arguments:
        None
    Returns:
        None
    """
    # Reload both modules so Maya always uses you latest edits.
    importlib.reload(GUI)
    importlib.reload(qc)

    # Launch the GUI
    GUI.main()
