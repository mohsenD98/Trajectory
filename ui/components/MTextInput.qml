import QtQuick 2.15
import QtQuick.Controls 2.15

Item{
    id: root
    height: 40
    property string lblText
    property string defaultValue
    property string value

    signal mValueChanged(var value)

    Text{
        id: lbl
        text: lblText
        anchors.verticalCenter: textField.verticalCenter
        color: appStyle.textHeader
    }

    TextField {
        id: textField
        height: 40
        anchors.left: lbl.right
        anchors.leftMargin: 4
        text: defaultValue
        anchors.right: parent.right
        placeholderText: qsTr("Enter #Value")
        placeholderTextColor: appStyle.textDetails
        font.weight: Font.Normal
        font.family: appStyle.font
        font.pointSize: 11
        color: appStyle.textHeader
        leftPadding: 8
        selectByMouse: true
        selectedTextColor: "#FFFFFF"
        selectionColor: "#4568e2"
        background: Rectangle{
            color: appStyle.primary
            radius: 4
        }

        onTextChanged: {
            mValueChanged(text)
            root.value = text
        }
    }

}
