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
        nameFilters: ["Text files (*.txt)", "ais files (*.gpkg)", "GeoJson (*.geojson)", "CSV files(*.csv)"]
        onAccepted: {
            console.log(fileDialog.currentFile)
            textField.text = fileDialog.currentFile
        }
    }

    IconButton{
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
