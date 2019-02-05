#include "updatedialog.h"

updateDialog::updateDialog(QWidget *parent) : QMainWindow(parent)
{
    ud = new QProgressDialog("", "Cancel", 0, 100);
    ud->setAutoReset(false);
    ud->setAutoClose(false);
    ud->setCancelButton(0);
//    ud->exec();

}

updateDialog::~updateDialog(){}

void updateDialog::updateValue(int value)
{
    ud->setValue(value);
}

void updateDialog::showButton(QString text)
{
    QPushButton *pb = new QPushButton();
    ud->setCancelButton(pb);
    ud->setCancelButtonText(text);
}

void updateDialog::setText(QString text)
{
    ud->setLabelText(text);
}
