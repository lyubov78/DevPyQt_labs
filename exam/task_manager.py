import sys
import psutil
from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QTextBrowser, QComboBox
import wmi
import win32com.client


class TaskManagerWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.initThreads()
        self.initSignals()

        self.startThreads()

    def initUi(self):
        self.setWindowTitle("Диспетчер системы")
        self.setGeometry(100, 100, 600, 400)

        self.layout = QVBoxLayout(self)

        self.cpuLabel = QLabel()
        self.memoryLabel = QLabel()
        self.diskLabel = QLabel()
        self.processesLabel = QLabel("Работающие процессы")
        self.processesLabel.setStyleSheet("font-weight: bold;")
        self.processesText = QTextBrowser()
        self.servicesLabel = QLabel("Работающие службы")
        self.servicesLabel.setStyleSheet("font-weight: bold;")
        self.servicesText = QTextBrowser()
        self.tasksLabel = QLabel("Задачи планировщика задач")
        self.tasksLabel.setStyleSheet("font-weight: bold;")
        self.tasksText = QTextBrowser()
        self.updateIntervalCombo = QComboBox()
        self.updateIntervalCombo.addItems(["1 сек.", "5 сек.", "10 сек.", "30 сек."])
        self.updateIntervalCombo.currentIndexChanged.connect(self.updateIntervalChanged)

        self.layout.addWidget(self.cpuLabel)
        self.layout.addWidget(self.memoryLabel)
        self.layout.addWidget(self.diskLabel)
        self.layout.addWidget(self.processesLabel)
        self.layout.addWidget(self.processesText)
        self.layout.addWidget(self.servicesLabel)
        self.layout.addWidget(self.servicesText)
        self.layout.addWidget(self.tasksLabel)
        self.layout.addWidget(self.tasksText)
        self.layout.addWidget(self.updateIntervalCombo)

    def initThreads(self):
        self.systemInfoThread = SystemInfoThread()
        self.processInfoThread = ProcessInfoThread()
        self.serviceInfoThread = ServiceInfoThread()
        self.taskInfoThread = TaskInfoThread()

    def initSignals(self):
        self.systemInfoThread.systemInfoReceived.connect(self.updateSystemInfo)
        self.processInfoThread.processesReceived.connect(self.updateProcesses)
        self.serviceInfoThread.servicesReceived.connect(self.updateServices)
        self.taskInfoThread.tasksReceived.connect(self.updateTasks)

    def startThreads(self):
        self.systemInfoThread.start()
        self.processInfoThread.start()
        self.serviceInfoThread.start()
        self.taskInfoThread.start()

    def updateSystemInfo(self, cpuInfo, memoryInfo, diskInfo):
        self.cpuLabel.setText(cpuInfo)
        self.memoryLabel.setText(memoryInfo)
        self.diskLabel.setText(diskInfo)

    def updateProcesses(self, processes):
        self.processesText.setPlainText(processes)

    def updateServices(self, services):
        self.servicesText.setPlainText(services)

    def updateTasks(self, tasks):
        self.tasksText.setPlainText(tasks)

    def updateIntervalChanged(self):
        interval_map = {0: 1, 1: 5, 2: 10, 3: 30}
        interval = interval_map[self.updateIntervalCombo.currentIndex()]
        self.systemInfoThread.updateInterval(interval)
        self.processInfoThread.updateInterval(interval)
        self.serviceInfoThread.updateInterval(interval)
        self.taskInfoThread.updateInterval(interval)


class SystemInfoThread(QtCore.QThread):
    systemInfoReceived = QtCore.Signal(str, str, str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.interval = 1

    def updateInterval(self, interval):
        self.interval = interval

    def run(self):
        while True:
            cpuInfo, memoryInfo, diskInfo = self.getSystemInfo()
            self.systemInfoReceived.emit(cpuInfo, memoryInfo, diskInfo)
            self.sleep(self.interval)

    def getSystemInfo(self):
        cpuInfo = f"Процессор: {psutil.cpu_freq().current} МГц " \
                  f"\nКоличество ядер: {psutil.cpu_count()}" \
                  f"\nТекущая загрузка: {psutil.cpu_percent()}%"
        memoryInfo = f"Оперативная память:\nОбщий объем: {psutil.virtual_memory().total / (1024 ** 3):.2f} Гб" \
                     f"\nТекущая загрузка: {psutil.virtual_memory().percent}%"
        diskInfo = "\n".join([f"Диск {part.device}\n"
                              f"Общий объем: {psutil.disk_usage(part.mountpoint).total / (1024 ** 3):.2f} Гб"
                              f"\nЗанято: {psutil.disk_usage(part.mountpoint).used / (1024 ** 3):.2f} Гб"
                              for part in psutil.disk_partitions()])
        return cpuInfo, memoryInfo, diskInfo


class ProcessInfoThread(QtCore.QThread):
    processesReceived = QtCore.Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.interval = 1

    def updateInterval(self, interval):
        self.interval = interval

    def run(self):
        while True:
            processes = self.getRunningProcesses()
            self.processesReceived.emit(processes)
            self.sleep(self.interval)

    def getRunningProcesses(self):
        return "\n".join([f"{p.pid} {p.name()} {p.status()}" for p in psutil.process_iter(['pid', 'name', 'status'])])


class ServiceInfoThread(QtCore.QThread):
    servicesReceived = QtCore.Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.interval = 1

    def updateInterval(self, interval):
        self.interval = interval

    def run(self):
        while True:
            services = self.getRunningServices()
            self.servicesReceived.emit(services)
            self.sleep(self.interval)

    def getRunningServices(self):
        c = wmi.WMI()
        services = c.Win32_Service()
        return "\n".join([f"{service.Name} {service.DisplayName} {service.State}" for service in services])


class TaskInfoThread(QtCore.QThread):
    tasksReceived = QtCore.Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.interval = 1

    def updateInterval(self, interval):
        self.interval = interval

    def run(self):
        scheduler = win32com.client.Dispatch('Schedule.Service')
        scheduler.Connect()
        while True:
            tasks = self.getScheduledTasks(scheduler)
            self.tasksReceived.emit(tasks)
            self.sleep(self.interval)

    def getScheduledTasks(self, scheduler):
        folder = scheduler.GetFolder("\\")
        tasks = folder.GetTasks(0)
        return "\n".join([f"{task.Name}" for task in tasks])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TaskManagerWindow()
    window.show()
    sys.exit(app.exec())
