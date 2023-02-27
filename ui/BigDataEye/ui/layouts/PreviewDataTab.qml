import QtQuick 2.15

import "../components"

Item {
    property var logger

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
            logger.sendLog("Request To Get Data Head!", "dataHead", "info")
            backendCore.getDataHead()
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
