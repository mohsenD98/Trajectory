import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Dialogs

TextField {
    id: textField
    height: 40
    placeholderText: qsTr("Enter #Address")
    placeholderTextColor: appStyle.textDetails
    font.weight: Font.Normal
    font.family: appStyle.font
    font.pointSize: 11
    color: appStyle.textHeader
    leftPadding: 4
    rightPadding: selectFolder.width + 8
    onTextChanged: textField.text ? Font.Medium : Font.Light
    selectByMouse: true
    selectedTextColor: "#FFFFFF"
    selectionColor: "#4568e2"
    background: Rectangle{
        color: appStyle.primary
        radius: 4
    }

    FileDialog {
        id: fileDialog
        title: qsTr("Select the data directory")
//        nameFilters: ["GeoJson (*.geojson)", "Text files (*.txt)", "ais files (*.gpkg)", "CSV files(*.csv)"]
        onAccepted: {
            var acceptedUrl = fileDialog.currentFile+""
            if(acceptedUrl.includes("file:///"))
                textField.text = acceptedUrl.slice(7)
        }
    }

    IconButton{
        id: selectFolder
        width: 24
        height: 24
        iconColor: "#b9bbbe"
        iconWidth: 22
        iconHeight: 22
        anchors.right: parent.right
        anchors.rightMargin: 4
        anchors.verticalCenter: textField.verticalCenter
        iconPath: "../images/svg_icons/open_icon.svg"
        onClickDetected: {
            fileDialog.open()
        }
        CenteredTooltip{ text: "Choose DB"; inverted: true }
    }
}
