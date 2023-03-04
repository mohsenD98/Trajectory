import QtQuick 2.15
import QtQuick.Controls 2.15
import Qt5Compat.GraphicalEffects
import QtQuick.Layouts 1.15
import Qt.labs.settings 1.0

import "../components"
import "../Style"

Flickable {
    id: flickable
    flickableDirection: Flickable.VerticalFlick
    Layout.fillWidth: true
    Layout.fillHeight: true
    Layout.alignment: Qt.AlignLeft | Qt.AlignTop
    contentHeight: left_inside_column.height
    clip: true

    property var logger
    property bool runningProgress: false
    onLoggerChanged: {
        if(logger){
            backendCore.sendLog.connect(handleBackendLog)
        }
    }

    function handleBackendLog(txt, source, important){
        logger.sendLog(txt, source, important)
    }

    Settings {
        id: settings
        category: "FileSourcePropertyMenu"
        property alias dbPath: dbPath.text
        property alias idColName: idColName.value
        property alias timeColName: timeColName.value
        property alias formatColName: formatColName.value
        property alias geoColName: geoColName.value
        property alias clusteringType: clusteringType.currentIndex
        property alias clusteringMinSamplesCount: clusteringMinSamplesCount.value
        property alias clusteringMaxDistance: clusteringMaxDistance.value
    }

    Column{
        id: left_inside_column
        anchors.top: parent.top
        anchors.topMargin: 8
        width: parent.width
        spacing: 16
        GroupBox{
            height: fileInputsCol.height + 23
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.margins: 4
            groupLbl: "File Settings"
            enabled: !runningProgress
            opacity: enabled? 1: .6

            Column{
                id: fileInputsCol
                width: parent.width
                anchors.top: parent.top
                anchors.topMargin: 16
                spacing: 8

                AddressInput {
                    id: dbPath
                    anchors.left: parent.left
                    anchors.right: parent.right
                    anchors.margins: 4
                    text: settings.dbPath
                }

                MTextInput{
                    id: idColName
                    anchors.left: parent.left
                    anchors.right: parent.right
                    anchors.margins: 4
                    lblText: "Id Column Name: "
                    defaultValue: settings.idColName
                    onMValueChanged: (value)=> {
                        if(logger) {
                            logger.sendLog(lblText + value, "id", "info")
                        }
                    }
                }

                MTextInput{
                    id: timeColName
                    anchors.left: parent.left
                    anchors.right: parent.right
                    anchors.margins: 4
                    lblText: "Time Column Name:"
                    defaultValue: settings.timeColName
                    onMValueChanged: (value)=> {
                        if(logger) {
                            logger.sendLog(lblText + value, "Timestamp", "info")
                        }
                    }
                }

                MTextInput{
                    id: formatColName
                    anchors.left: parent.left
                    anchors.right: parent.right
                    anchors.margins: 4
                    lblText: "Time Format:"
                    defaultValue: settings.formatColName
                    onMValueChanged: (value)=> {
                        if(logger) {
                            logger.sendLog(lblText + value, "Format", "info")
                        }
                    }
                }

                MTextInput{
                    id: geoColName
                    anchors.left: parent.left
                    anchors.right: parent.right
                    anchors.margins: 4
                    lblText: "Geometery Column Name:"
                    defaultValue: settings.geoColName
                    onMValueChanged: (value)=> {
                        if(logger) {
                            logger.sendLog(lblText + value, "Geometery", "info")
                        }
                    }
                }
            }
        }

        GroupBox{
            height: programInputsCol.height + 15
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.margins: 4
            groupLbl: "Clustering Settings"
            enabled: !runningProgress
            opacity: enabled? 1: .6

            Column{
                id: programInputsCol
                width: parent.width
                anchors.top: parent.top
                anchors.topMargin: 8
                spacing: 8

                ComboBoxInput {
                    id: clusteringType
                    lblText: "Select Clustering Method: "
                    anchors.left: parent.left
                    anchors.right: parent.right
                    anchors.margins: 4
                    inputModel: ["DB Scan", "KMeans"]
                    defaultIndex: settings.clusteringType
                    onMValueChanged: (index, text)=>{
                        if(logger) {
                            logger.sendLog(lblText + index + text, "Clustering", "info")
                            currentValue = text
                            currentIndex = index
                        }
                    }
                    property string currentValue: inputModel[defaultIndex]
                    property real currentIndex: defaultIndex
                }

                MTextInput{
                    id: clusteringMinSamplesCount
                    anchors.left: parent.left
                    anchors.right: parent.right
                    anchors.margins: 4
                    lblText: "Min Samples: "
                    defaultValue: settings.clusteringMinSamplesCount
                    onMValueChanged: (value)=> {
                        if(logger) {
                            logger.sendLog(lblText + value, "minSamples", "info")
                        }
                    }
                }

                MTextInput{
                    id: clusteringMaxDistance
                    anchors.left: parent.left
                    anchors.right: parent.right
                    anchors.margins: 4
                    lblText: "Max Distance: "
                    defaultValue: settings.clusteringMaxDistance
                    onMValueChanged: (value)=> {
                        if(logger) {
                            logger.sendLog(lblText + value, "maxSamples", "info")
                        }
                    }
                }
            }
        }

        Button {
            id: runBtn
            highlighted: true
            text: "Set Params And Run"
            font.capitalization: Font.MixedCase
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.margins: 4
            visible: !runningProgress
            Material.accent: appStyle.green
            onClicked: {
                runningProgress = true

                backendParams.setFilePath(dbPath.text)
                backendParams.setIdNameInHeader(idColName.value)
                backendParams.setTimeNameInHeader(timeColName.value)
                backendParams.setFormatNameInHeader(formatColName.value)
                backendParams.setGeometeryNameInHeader(geoColName.value)
                backendParams.setClusteringType(clusteringType.currentValue)
                backendParams.setClusteringParams(clusteringMaxDistance.value, clusteringMinSamplesCount.value)

                logger.sendLog("Params Setted And Run Clicked!", "runBtn", "success")
                backendCore.run()
            }
        }
        Button {
            id: stopBtn
            highlighted: true
            text: "Stop"
            font.capitalization: Font.MixedCase
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.margins: 4
            visible: runningProgress
            Material.accent: appStyle.red
            onClicked: {
                runningProgress = false
                logger.sendLog("Progress Stopped!", "stopBtn", "important")
            }
        }
    }

    ScrollBar.vertical: ScrollBar {
        id: control
        size: 0.3
        position: 0.2
        orientation: Qt.Vertical
        visible: flickable.moving

        contentItem: Rectangle {
            implicitWidth: 4
            implicitHeight: 100
            radius: width / 2
            color: control.pressed ? appStyle.accent : "#202225"
        }
    }
}

