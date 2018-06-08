#ifndef REPO_H
#define REPO_H

#include <QMainWindow>
#include <QObject>
#include <QJsonDocument>
#include <QtDebug>
#include <QString>
#include <QJsonArray>

class Repo : public QObject
{
    Q_OBJECT

public:

    explicit Repo(QString json, QObject *parent = 0);
    virtual ~Repo();
    int size();

private:

    int m_size;

};

#endif // REPO_H
