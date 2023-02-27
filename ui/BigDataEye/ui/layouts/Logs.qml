import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import Qt5Compat.GraphicalEffects

import "../components"
import "../js/FunctionsJS.js" as FunctionJS

Rectangle {
    id: logsPage

    property bool expandMode: true
    color:  "#202225"

    // Function Logs Scroll To End
    function scrollToEnd(){
        logsFlickable.contentY = logsFlickable.contentHeight
    }
    
    // Create New Log
    function sendLog(log, source, type){
        if(log){
            var component = Qt.createComponent("LogItem.qml")
            var msg = component.createObject(logsColumn, {
                "logText" : log,
                "logTime" : FunctionJS.msgTime(),
                "logSource" : source,
                "logType" : type
            })
            scrollToEnd()
        }
    }

    Rectangle{
        id: logsHeader
        height: 22
        width: parent.width
        color: "#202225"
        TopBarButton{
            id: btnClose
            opacityIcon: 0.8
            anchors.right: parent.right
            colorMouseDown: "#ab0000"
            colorMouseOver: "#f04747"
            btnIcon: "../../ui/images/svg_icons/expand_arrow.svg"
            onClicked: {
                if(expandMode){
                    visualization.height= visualization.parent.height - 22
                    expandMode = false
                    btnClose.btnIcon = "../../ui/images/svg_icons/collapse_arrow.svg"
                }else{
                    visualization.height= visualization.parent.height / 3 * 2
                    expandMode = true
                    btnClose.btnIcon = "../../ui/images/svg_icons/expand_arrow.svg"
                }
            }
        }
    }

    Flickable {
        id: logsFlickable
        anchors.top: logsHeader.bottom
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        anchors.rightMargin: 4
        contentHeight: logsColumn.height
        clip: true

        Column {
            id: logsColumn
            bottomPadding: 30
            topPadding: 10
            spacing: 3
        }

        ScrollBar.vertical: ScrollBar {
            id: controlScroll
            orientation: Qt.Vertical
            y: 3
            bottomPadding: 8
            topPadding: 0
            leftPadding: 0
            rightPadding: 0
            contentItem: Rectangle {
                implicitWidth: 8
                implicitHeight: 100
                radius: width / 2
                color: "#b9bbbe"
            }
            background: Rectangle{
                radius: width / 2
                color: "#32353b"
                border.width: 0
            }
        }
    }
}
