#include "filedownloader.h"
#include "qdebug.h"

FileDownloader::FileDownloader(QUrl fileUrl, QObject *parent) :
 QObject(parent)
{
 connect(
  &m_WebCtrl, SIGNAL (finished(QNetworkReply*)),
  this, SLOT (fileDownloaded(QNetworkReply*))
  );

 QNetworkRequest request(fileUrl);
 m_WebCtrl.get(request);
 this->fileName = fileUrl.fileName();
}

FileDownloader::~FileDownloader() { }

void FileDownloader::fileDownloaded(QNetworkReply* pReply) {
    qDebug() << pReply->error();
    if (pReply->error() == 203){
        emit networkError();
    }
    else
    {
    m_DownloadedData = pReply->readAll();
 //emit a signal
    pReply->deleteLater();
    emit downloaded();
    }

}

QByteArray FileDownloader::downloadedData() const {
 return m_DownloadedData;
}


