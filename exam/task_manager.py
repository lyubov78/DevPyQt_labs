import sys
import psutil
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QTextBrowser, QComboBox
from PySide6.QtCore import QTimer
import wmi
import win32com.client


class TaskManagerWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

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

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_info)
        self.timer.start(1000)

        self.update_info()

    def update_info(self):
        cpuInfo, memoryInfo, diskInfo = getSystemInfo()
        self.cpuLabel.setText(cpuInfo)
        self.memoryLabel.setText(memoryInfo)
        self.diskLabel.setText(diskInfo)

        processes = getRunningProcesses()
        self.processesText.setPlainText(processes)

        services = getRunningServices()
        self.servicesText.setPlainText(services)

        tasks = getScheduledTasks()
        self.tasksText.setPlainText(tasks)

    def updateIntervalChanged(self):
        index = self.updateIntervalCombo.currentIndex()
        if index == 0:
            self.timer.setInterval(1000)
        elif index == 1:
            self.timer.setInterval(5000)
        elif index == 2:
            self.timer.setInterval(10000)
        elif index == 3:
            self.timer.setInterval(30000)


def getSystemInfo():
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


def getRunningProcesses():
    return "\n".join([f"{p.pid} {p.name()} {p.status()}" for p in psutil.process_iter(['pid', 'name', 'status'])])


def getRunningServices():
    c = wmi.WMI()
    services = c.Win32_Service()
    return "\n".join([f"{service.Name} {service.DisplayName} {service.State}" for service in services])


def getScheduledTasks():
    scheduler = win32com.client.Dispatch('Schedule.Service')
    scheduler.Connect()
    folder = scheduler.GetFolder("\\")
    tasks = folder.GetTasks(0)
    return "\n".join([f"{task.Name}" for task in tasks])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TaskManagerWindow()
    window.show()
    sys.exit(app.exec())
