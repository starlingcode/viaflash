#include "repo.h"

Repo::Repo(QString json, QObject *parent = 0) :
    QObject(parent)
{
    m_json = QJsonDocument::fromJson(json.toUtf8());
    // obj = repository.object();
    QJsonArray elements = m_json.array();
    qDebug() << elements;
}

Repo::~Repo() { }

/*
void repo::read(const QJsonObject &json)
{
    if (json.contains("name") && json["name"].isString())
        mName = json["name"].toString();

    if (json.contains("level") && json["level"].isDouble())
        mLevel = json["level"].toInt();

    if (json.contains("classType") && json["classType"].isDouble())
        mClassType = ClassType(json["classType"].toInt());
}

void repo::getLatestVersion(const QJsonObject &json)
{
    if (json.contains("name") && json["name"].isString())
        mName = json["name"].toString();

    if (json.contains("level") && json["level"].isDouble())
        mLevel = json["level"].toInt();

    if (json.contains("classType") && json["classType"].isDouble())
        mClassType = ClassType(json["classType"].toInt());
}

*/
