import sys
import argparse
from PySide2.QtCore import (Qt)
from PySide2.QtGui import QColor, QPainter
from PySide2.QtWidgets import (QApplication, QMainWindow)
from PySide2.QtCharts import QtCharts

if __name__ == "__main__":    
    app = QApplication(sys.argv)

    series = QtCharts.QSplineSeries()

    series.setName("spline")

    series.append(0, 6);
    series.append(2, 4);
    series.append(3, 8);
    series.append(7, 4);
    series.append(10, 5);
    series.append(11, 1)  
    series.append(13, 3)  
    series.append(17, 6)  
    series.append(18, 3) 
    series.append(20, 2)

    chart = QtCharts.QChart()
    chart.legend().hide()
    chart.addSeries(series)
    chart.setTitle("Spline chart")
    chart.createDefaultAxes()
    chart.axes(Qt.Vertical)[0].setRange(0, 10)

    chartView = QtCharts.QChartView(chart)
    chartView.setRenderHint(QPainter.Antialiasing)
            
    window = QMainWindow()
    window.setCentralWidget(chartView)
    window.resize(400, 300);
    window.show();
    

    # window.show()
    """рисует все на экране """
    sys.exit(app.exec_())
    """осуществляет процесс корректного закрытия приложения """
