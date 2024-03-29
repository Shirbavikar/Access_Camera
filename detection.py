from PyQt5.QtCore import QThread,Qt,pyqtSignal
from PyQt5.QtGui import QImage
import cv2


class Detection(QThread):
    def __init__(self):
        super(Detection,self).__init__()


    changePixmap=pyqtSignal(QImage)

    def run(self):
        self.running=True

        cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)

        # if self.running==False:
        #     cv2.destroyAllWindows()
        
        while self.running:
            ret,frame=cap.read()
        if ret:
            height,width,channels=frame.shape
            rgbImage=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            bytesPerline=channels*width
            convertToQtFormat=QImage(rgbImage.data,width,height,bytesPerline,QImage.Format_RGB888)
            p=convertToQtFormat.scaled(854,400,Qt.KeepAspectRatio)
            self.changePixmap.emit(p)