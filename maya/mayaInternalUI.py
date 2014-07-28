"""
this is the simple fallback-ui for maya for the case that no pyQt is installed.
It should provide the common functionality but I won't invest much time into
layout.

This UI is mainly used for testing and may do stuff that Editor-specific UI parts
would do in a regual (PyQt or PySide based) UI.
This UI contains UE4 specific code!

"""

import pymel.core as pm
import m2u

def cbConnect(*args):
    m2u.core.getEditor().connectToInstance()

def cbSetupCamera(*args):
    m2u.core.getProgram().setupCamera()

def cbSyncCamera(*args):
    m2u.core.getProgram().setCameraSyncing(True)

def cbSyncCameraOff(*args):
    m2u.core.getProgram().setCameraSyncing(False)

def cbSyncObjects(*args):
    m2u.core.getProgram().setObjectSyncing(True)

def cbSyncObjectsOff(*args):
    m2u.core.getProgram().setObjectSyncing(False)

def cbSyncVisibility(*args):
    m2u.core.getProgram().setVisibilitySyncing(True)

def cbSyncVisibilityOff(*args):
    m2u.core.getProgram().setVisibilitySyncing(False)

def cbFetchSelected(*args):
    # this is circumventing the interface
    #m2u.maya.mayaCommand.fetchSelectedObjectsFromEditor()
    m2u.core.getEditor().ue4Export.fetchSelectedObjects()


def cbSendSelectedToEd(*args):
    
    
def cbUDKImportContent(*args):
    m2u.udk.udkUI.callImportContent("C:\\temp\\mp7_compact_export.fbx",None)

def createUI():
    v = m2u.getVersion()
    m2uwin = pm.window( title="m2u "+v+" (maya)", iconName='m2u',
                        widthHeight=(150, 300) )
    pm.columnLayout()
    pm.rowLayout(numberOfColumns = 2)
    pm.button( label='Connect', c=cbConnect )
    pm.button( label='Setup Cameras', c=cbSetupCamera )
    pm.setParent('..')
    pm.checkBox( label='Sync Camera', onc = cbSyncCamera,
                 ofc = cbSyncCameraOff, v = False)
    pm.checkBox( label='Sync Objects', onc = cbSyncObjects,
                 ofc = cbSyncObjectsOff, v = False)
    pm.checkBox( label='Sync Visibility', onc = cbSyncVisibility,
                 ofc = cbSyncVisibilityOff, v = False)
    pm.separator()
    pm.button( label='Fetch Selected', c = cbFetchSelected)
    pm.button( label='Send Selected To Editor', c = cbSendSelectedToEd)
    #pm.button( label='Import Content Test', c = cbUDKImportContent)
    pm.setParent( '..' )
    pm.showWindow( m2uwin )