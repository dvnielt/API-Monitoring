# API-Monitoring
API Monitoring program that exposes your hardware statistics for your computer that is monitored by a tkinter gui program.

There are parent directories that contain the following four modules/files:

**remote_api.py** : Provide route handlers for three endpoints, /mem, /cpu, and /disk.
Use APIRouter as needed. Import class from remote_tools for the methods to provide
the actual system calls to retrieve disk, memory, and cpu statistics.

**remote_tools.py** : Create a class with three methods for retrieving statistics for
memory, cpu, and disk. Do all of the computations (such as arithmetic operations and
round()) in these methods to return a simple percentage value of system usage. An
example would be determining total system ram and then the amount of used ram to
determine a percentage of usage.

The remote_tools module should read an external file named tools_config to determine
the drive or path that needs to be checked for disk usage. This will depend on your
operating system.

**tools_config** : Configurations should not be hard coded but rather contained in non-
source code files that can be easily modified in production as need. This contains the
path of primary drive to monitor for usage.

[Windows file example : disk_path = "c:\ "]
[Mac file example : disk_path = "/"]

**system_monitor.py** : GUI program based on tkinter that displays CPU usage in %, Disk
usage in %, Memory usage in %. System_monitor will create api calls to retrieve data
using GET. Five points extra credit if gui program automatically updates values every 5
seconds. Below is an example of the system monitor.

***Instructions***
1. Use uvicorn server in your parent directory to expose your api endpoints.
2. Run the system_monitor.py module to monitor the out hardware statistics via API.