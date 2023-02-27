import QtQuick 2.15

Rectangle {
    radius: 4
    color: "transparent"
    border.color: appStyle.div
    border.width: 1
    property string groupLbl
    Rectangle{
        color: appStyle.primaryDark
        width: fileLbl.width
        height: fileLbl.height
        anchors.verticalCenter: parent.top
        anchors.left: parent.left
        anchors.leftMargin: 8
        Text {
            id: fileLbl
            text: groupLbl
            color: appStyle.textHeader
            font.pixelSize: 11
            font.bold: true
            font.family: appStyle.font
            anchors.centerIn: parent
        }
    }
}
