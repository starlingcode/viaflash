#ifndef REPO_H
#define REPO_H

#include <QMainWindow>
#include <QString>
#include <QJsonDocument>
#include <QJsonArray>
#include <QJsonObject>
#include <QByteArray>

class Repo : public QObject
{
    Q_OBJECT

public:
    explicit Repo(QByteArray, QObject *parent = nullptr);
    virtual ~Repo();
    int length();
    void selectFirmware(int);
    QString nameAt(int);
    QString firmwareToken;
    QString firmwareName;
    QString firmwareVersion;
    QString firmwareManual;
    QString firmwareDetails;
    QString firmwareAuthor;
    QString firmwareLicense;
    QString firmwareSource;
    QString firmwareInfo;
    int firmwareOptionByte;
    QString repoStatus;
    bool exists;

private:
    QJsonDocument m_test; // json document from repo
    QJsonArray m_elements;  // json elements from repo metadata
    int m_repoSize;
    int m_currentSelection;

signals:

public slots:
};



#endif // REPO_H
