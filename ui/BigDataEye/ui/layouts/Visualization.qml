import QtQuick 2.15
import QtQuick.Controls 2.15

Rectangle {
    id: visRoot
    color: "transparent"
    property var logger

    TabBar{
        id: bar
        width: parent.width
        onCurrentIndexChanged: {
            if(logger) logger.sendLog("Visualization Tab Index Changed To " + currentIndex, "visualizationTab", "warning")
        }

        TabButton {
         text: qsTr("Preview Data")
        }

        TabButton {
         text: qsTr("Results")
        }
    }

    SwipeView{
        anchors.top: bar.bottom
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        currentIndex: bar.currentIndex
        clip: true
        interactive: false

        PreviewDataTab {
            id: firstPage
            logger: visRoot.logger
        }

        Item {
            id: secondPage
        }

        Item {
            id: thirdPage
        }
    }
}
