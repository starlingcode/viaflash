#ifndef UPDATEDIALOG_H
#define UPDATEDIALOG_H

#include <QMainWindow>
#include <QProgressDialog>
#include <QPushButton>

class updateDialog : public QMainWindow
{
    Q_OBJECT
public:
    explicit updateDialog(QWidget *parent = 0);
    ~updateDialog();
    void showButton(QString);
    void setText(QString);


private:
    //void startFlash();
    QProgressDialog *ud;

signals:


public slots:
   void updateValue(int);
   // void setLabel(QString);
   // void buttonEnabled(bool);
};

#endif // UPDATEDIALOG_H
