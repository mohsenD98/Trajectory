import QtQuick 2.15
import "../components"

Item {
    function reset() {
        comovementMiningItem.running = false
    }

    RunningGroupBox {
        id: comovementMiningItem
        anchors.top: parent.top
        anchors.left: parent.left
        anchors.right: parent.right
        height: 400
        anchors.topMargin: 16
        anchors.leftMargin: 8
        anchors.rightMargin: 8
        groupLbl: "Co-Movement Pattern Detection"
        onRunThisBox: {
            backendCore.comovementPatternDetection()
        }
    }
}
