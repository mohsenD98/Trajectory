import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Controls.Material 2.15

Item{
    height: 40
    property string lblText
    property real defaultIndex: 0
    property var inputModel
    signal mValueChanged(var index, var text)
    Component.onCompleted: {
        Material.background= appStyle.primary
    }

    Text{
        id: lbl
        text: lblText
        anchors.verticalCenter: comboField.verticalCenter
        color: appStyle.textHeader
    }

    ComboBox {
        id: comboField
        height: 40
        anchors.left: lbl.right
        anchors.leftMargin: 4
        anchors.right: parent.right
        font.weight: Font.Normal
        font.family: appStyle.font
        font.pointSize: 11
        currentIndex: defaultIndex
        model: inputModel
        onCurrentIndexChanged: {
            mValueChanged(currentIndex, inputModel[currentIndex])
        }
    }
}
