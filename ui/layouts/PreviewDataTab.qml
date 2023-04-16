import QtQuick 2.15

import "../components"

Item {
    property var logger
    Component.onCompleted: {
        backendCore.sendDataHead.connect(handleDataHead)
        backendCore.sendMatplotLibImgUrl.connect(handleMatplotLib)
        backendCore.sendComovementPatternDetectionResult.connect(handleComovementPatternDetectionResult)
    }

    function handleDataHead(value){
        dataHead.text = value
        logger.sendLog("Data Head Received!", "dataHead", "success")
    }

    function handleMatplotLib(value){
        matplotLibDb.visible = true
        matplotLibDb.source = value
        logger.sendLog("MatplotLib Image Received!", "MatPlotLib", "success")
    }

    function handleComovementPatternDetectionResult(value){
        logger.sendLog("Results Received: "+ value, "coMovement", "success")
    }

    function reset() {
        dataHead.text = ""
        matplotLibDb.visible = false

        mathPlotItem.running = false
        dataHeadItem.running = false
        animationItem.running = false
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
        groupLbl: "Matplot"
        onRunThisBox: {
            backendCore.matplotLibDb()
        }
        Image{
            id: matplotLibDb
            anchors.fill: parent
            anchors.margins: 16
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
        groupLbl: "Data Head"
        onRunThisBox: {
            backendCore.getDataHead()
        }
        Rectangle{
            anchors.fill: parent
            color: "transparent"
            clip: true
            Text {
                id: dataHead
                color: appStyle.textHeader
                font.family: appStyle.font
                font.pixelSize: 14
                anchors.top: parent.top
                anchors.horizontalCenter: parent.horizontalCenter
                anchors.topMargin: 16
                clip: true
            }
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
