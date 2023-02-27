import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import Qt5Compat.GraphicalEffects

import "../components"

Row {
    id: row
    spacing: 0

    // Log Properties
    property string logText: "N/A"
    property string logTime: "N/A"
    property string logType: "info"
    property string logSource: ""

    // Width
    width: parent.parent.width

    Rectangle{
        id: bg
        width: row.width - 12
        height: column.height
        color: "#00000000"
        anchors.top: row.top
        anchors.topMargin: 3
        
        Row{
            id: column
            width: bg.width

            MouseArea{
                id: mouseArea
                width: bg.width
                height: rowContent.height
                hoverEnabled: true
                onEntered: {
                    bg.color = "#32353b"
                }
                onExited: {
                    bg.color = "#00000000"
                }

                RowLayout{
                    id: rowContent
                    width: bg.width
                    spacing: 0

                    Column{
                        id: column_top
                        clip: true
                        Layout.fillWidth: true
                        Item{
                            id: logBox
                            height: 20
                            width: column_top.width

                            TextEdit {
                                id: textTime_2
                                color: "#7e7e7e"
                                text: "Todat at " + logTime
                                anchors.verticalCenter: logBox.verticalCenter
                                anchors.left: logBox.left
                                verticalAlignment: Text.AlignVCenter
                                wrapMode: Text.Wrap
                                anchors.verticalCenterOffset: 2
                                anchors.leftMargin: 8
                                Layout.leftMargin: 8
                                Layout.topMargin: 5
                                Layout.fillWidth: true
                                Layout.alignment: Qt.AlignLeft | Qt.AlignTop
                                font.pointSize: 8
                                font.family: appStyle.font
                                selectByMouse: true
                                selectByKeyboard: true
                                selectedTextColor: "#ffffff"
                                selectionColor: "#4568e2"
                                activeFocusOnPress: false
                            }
                        }

                        TextEdit {
                            width: column_top.width - 120
                            color: (logType === "info" ? appStyle.infoLog : (logType === "important" ? appStyle.red: (logType === "success" ? appStyle.green:( logType === "warning"? appStyle.warning : appStyle.infoLog))))
                            text: logText
                            wrapMode: Text.Wrap
                            bottomPadding: 3
                            topPadding: 2
                            leftPadding: 8
                            Layout.alignment: Qt.AlignLeft | Qt.AlignTop
                            Layout.fillWidth: true
                            font.pointSize: 11
                            font.family: appStyle.font
                            selectByMouse: true
                            selectByKeyboard: true
                            selectedTextColor: "#ffffff"
                            selectionColor: "#4568e2"
                            activeFocusOnPress: false
                        }
                    }
                }
            }
        }
    }

    Item {
        width: 12
    }
}






/*##^##
Designer {
    D{i:0;formeditorColor:"#000000";height:48;width:300}
}
##^##*/
