#include "updatedialog.h"

updateDialog::updateDialog(QWidget *parent) : QMainWindow(parent)
{
    ud = new QProgressDialog("", "Cancel", 0, 100);
    ud->setModal(true);
    const QPoint global = parent->mapToGlobal(rect().center());
    ud->move(global.x() + 220, global.y() + 135);
    ud->setAutoReset(false);
    ud->setAutoClose(false);
    ud->setCancelButton(0);
    ud->show();
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
