import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Program Files\Python312\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Program Files\Python312\tcl\tk8.6"

executables = [cx_Freeze.Executable("Face recognition attendence system .py", base=base, icon="face icon.ico")]


cx_Freeze.setup(
    name = "Face recognition attendance system ",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["face icon.ico",'tcl86t.dll','tk86t.dll', 'Images of interface page','data','database','Attendance.csv']}},
    version = "1.0",
    description = "Face Recognition Automatic Attendace System | Developed By Sumit And Jeevan",
    executables = executables
    )