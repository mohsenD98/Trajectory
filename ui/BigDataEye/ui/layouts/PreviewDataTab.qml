import QtQuick 2.15

import "../components"

Item {
    property var logger
    Component.onCompleted: {
        backendCore.sendDataHead.connect(handleDataHead)
    }

    function handleDataHead(value){
        dataHead.text = value
        logger.sendLog("Data Head Received!", "dataHead", "success")
    }

    RunningGroupBox {
        id: dataHeadItem
        anchors.top: parent.top
        anchors.left: parent.left
        anchors.bottom: parent.bottom
        anchors.topMargin: 16
        anchors.bottomMargin: 16
        anchors.leftMargin: 8
        width: parent.width / 2 - 24
        groupLbl: "Data Head"
        onRunThisBox: {
            backendCore.getDataHead()
        }
        Text {
            id: dataHead
            color: appStyle.textHeader
            font.family: appStyle.font
            font.pixelSize: 14
            anchors.centerIn: parent
        }
    }

    RunningGroupBox {
        id: mathPlotItem
        anchors.top: parent.top
        anchors.right: parent.right
        anchors.topMargin: 16
        anchors.rightMargin: 8
        height: parent.height / 2 - 16
        width: parent.width / 2 - 4
        groupLbl: "Matplot"
        onRunThisBox: {
            logger.sendLog("Request To Get Matplot", "Matplot", "info")
        }
    }

    RunningGroupBox {
        id: animationItem
        anchors.top: mathPlotItem.bottom
        anchors.right: parent.right
        anchors.topMargin: 16
        anchors.rightMargin: 8
        height: parent.height / 2 - 30
        width: parent.width / 2 - 4
        groupLbl: "Animate Data"
        onRunThisBox: {
            logger.sendLog("Request To Animating Data", "animate", "info")
        }
    }
}
