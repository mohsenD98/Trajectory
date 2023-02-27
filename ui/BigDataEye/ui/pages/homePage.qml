import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import Qt5Compat.GraphicalEffects

import "../components"
import "../layouts"
import "../js/FunctionsJS.js" as FunctionJS

Item {
    id: homePageRoot
    width: 1100
    height: 780    

    // Show Right Column / showPreprocessingMenu
    property bool showPreprocessingMenu: false
    property alias changeStatusMemberList: rightMenu.item
    property var logger

    Rectangle {
        id: content
        color: "#36393f"
        anchors.fill: homePageRoot

        Rectangle {
            id: left_home_page
            width: 320
            color: appStyle.primaryDark
            anchors.left: content.left
            anchors.top: content.top
            anchors.bottom: content.bottom
            anchors.leftMargin: 0
            anchors.bottomMargin: 0
            anchors.topMargin: 0

            ColumnLayout {
                id: left_column
                anchors.fill: left_home_page
                spacing: 1
                anchors.bottomMargin: 50
                
                Loader{
                    id: loaderLeftMenu
                    Layout.alignment: Qt.AlignLeft | Qt.AlignTop
                    source: Qt.resolvedUrl("../layouts/FileSourcePropertyMenu.qml")
                    Layout.fillHeight: true
                    Layout.fillWidth: true
                    onLoaded: {
                        item.logger = logger
                    }
                }
            }

            Rectangle {
                id: bottomLeftChannel
                height: 50
                color: "#292b2f"
                anchors.left: left_home_page.left
                anchors.right: left_home_page.right
                anchors.bottom: left_home_page.bottom
                anchors.rightMargin: 0
                anchors.leftMargin: 0
                anchors.bottomMargin: 0

                // Loader Top Left Module
                Loader{
                    anchors.fill: bottomLeftChannel
                    source: Qt.resolvedUrl("../components/Profile.qml")
                }
            }
        }

        Rectangle {
            id: right_column
            width: showPreprocessingMenu ? 320 : 0
            color: appStyle.primaryDark
            anchors.right: content.right
            anchors.top: content.top
            anchors.bottom: content.bottom
            anchors.bottomMargin: 0
            anchors.rightMargin: 0
            anchors.topMargin: 0

            Loader{
                id: rightMenu
                anchors.fill: right_column
                source: Qt.resolvedUrl("../layouts/PreprocessingMenu.qml")
            }
        }
        Loader{
            id: visualization
            anchors.left: left_home_page.right
            anchors.right: right_column.left
            anchors.top: content.top
            height: homeMessagesLoader.item? homeMessagesLoader.item.expandMode?visualization.parent.height / 3 * 2: parent.height - 22: parent.height - 22
            source: Qt.resolvedUrl("../layouts/Visualization.qml")
            enabled: loaderLeftMenu.item? loaderLeftMenu.item.runningProgress : false
            opacity: enabled? 1: .4
            onLoaded: {
                item.logger = logger
            }
            onEnabledChanged: {
                if(!enabled && item){
                    item.reset()
                }
            }
        }
        Loader{
            id: homeMessagesLoader
            anchors.left: left_home_page.right
            anchors.right: right_column.left
            anchors.top: visualization.bottom
            anchors.bottom: content.bottom
            clip: true
            source: Qt.resolvedUrl("../layouts/Logs.qml")
            onLoaded: {
                logger = item
            }
        }
    }

}

