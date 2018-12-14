#include "repo.h"

Repo::Repo(QByteArray data, QObject *parent) : QObject(parent)
{
    // convert to UTF-8
    m_test = QJsonDocument::fromJson(QString(data).toUtf8());
    if (!m_test.isNull()){
        exists = true;
        m_elements = m_test.array();
        m_repoSize = m_elements.size();
        m_currentSelection = 0;  // index of firmware in comboBox
        repoStatus = ("Initialized repository.");
    }
    else
    {
        exists = false;
        repoStatus = ("Repo initialization failed.");
    }

}

Repo::~Repo(){}

int Repo::length()
{
    return m_repoSize;
}

QString Repo::nameAt(int index)
{
    QJsonObject obj = m_elements.at(index).toObject();
    QJsonValue val = obj["name"];
    return val.toString();
}


void Repo::selectFirmware(int index)
{
    QJsonObject obj = m_elements.at(index).toObject();
    firmwareName = QString("<font face = 'IBM Plex Sans' size = 10> <strong> " + QJsonValue(obj["name"]).toString());
    firmwareVersion = QString("</strong> <br> <font size = 6>version " + QJsonValue(obj["latestVersion"]).toString());
    firmwareManual = QString("<br> <a href = '" + QJsonValue(obj["manualUrl"]).toString() + "'> Manual</a>");
    firmwareDetails = QString("<br> <br> <font size = 5>" + QJsonValue(obj["description"]).toString());
    firmwareAuthor = QString("<br> <br> <font size = 6> Author: " + QJsonValue(obj["author"]).toString());
    firmwareLicense = QString("<br> License: " + QJsonValue(obj["license"]).toString());
    firmwareSource = QString("<br> <a href = '" + QJsonValue(obj["sourceUrl"]).toString() + "'>  Source</a>");
    firmwareToken = (QJsonValue(obj["token"]).toString());
    firmwareOptionByte = (QJsonValue(obj["optionByte"]).toInt());
    firmwareInfo = QString(firmwareName + firmwareVersion + firmwareManual + firmwareDetails + firmwareAuthor + firmwareLicense + firmwareSource);
}

