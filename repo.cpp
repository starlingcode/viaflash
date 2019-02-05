#include "repo.h"

Repo::Repo(QByteArray data, QObject *parent) : QObject(parent)
{
    // convert to UTF-8
    m_test = QJsonDocument::fromJson(QString(data).toUtf8());
    if (!m_test.isNull())
    {
        exists = true;
        m_elements = m_test.array();
        m_repoSize = m_elements.size();
        m_currentSelection = 0;  // index of firmware in comboBox
    }
    else
    {
        exists = false;
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
    firmwareName = QString("<font face = 'IBM Plex Sans' size = 10> <span style = 'color:#ffdc64'> <strong> " + QJsonValue(obj["name"]).toString() + "</span>");
    firmwareVersion = QString("</strong> <br> <font size = 6>version " + QString::number(QJsonValue(obj["latestVersion"]).toInt()));
    firmwareManual = QString("<br> <a href = '" + QJsonValue(obj["manualUrl"]).toString() + "'> Manual</a>");
    firmwareDetails = QString("<br> <br> <font size = 5>" + QJsonValue(obj["description"]).toString());
    firmwareAuthor = QString("<br> <br> <font size = 6> Author: " + QJsonValue(obj["author"]).toString());
    firmwareLicense = QString("<br> License: " + QJsonValue(obj["license"]).toString());
    firmwareSource = QString("<br> <a href = '" + QJsonValue(obj["sourceUrl"]).toString() + "'>  Source</a>");
    firmwareToken = (QJsonValue(obj["token"]).toString());
    firmwareOptionByte = (QJsonValue(obj["optionByte"]).toInt());
    firmwareOptionByte2 = (QJsonValue(obj["latestVersion"]).toInt());
    firmwareInfo = QString(firmwareName + firmwareVersion + firmwareManual + firmwareDetails + firmwareAuthor + firmwareLicense + firmwareSource);
}

QString Repo::returnFirmwareName(int id)
{
    QString name;
    for (int i = 0; i < this->length(); i++)
    {
        QJsonObject obj = m_elements.at(i).toObject();
        if (QJsonValue(obj["optionByte"].toInt()) == id)
            name = QJsonValue(obj["name"]).toString();
    }
    if (name == "")
    {
        return QString("UNKNOWN");
    }
    else
    {
        return name;
    }
}

