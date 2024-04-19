import psutil


class Statistics:
    def cpu_usage(self):
        cpu = psutil.cpu_percent(interval=None)
        return round(cpu)

    def disk_usage(self):
        file = open("tools_config", "r")
        path = file.read()
        location = path.find('=')
        path = path[location+1:]
        # Creates a tuple of information where the percent value is stored at the 3rd index
        disk = psutil.disk_usage(path)
        return round(disk[3])

    def mem_usage(self):
        # Creates a tuple of information where the percent value is stored at the 2nd index.
        mem = psutil.virtual_memory()
        return round(mem[2])
