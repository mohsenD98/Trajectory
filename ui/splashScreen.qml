import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15
import QtQuick.Timeline 1.0
import Qt5Compat.GraphicalEffects

import "components"
import "Style"

Window {
    id: splashScreenWindow
    width: 300
    height: 350
    visible: true
    color: appStyle.transparent
    title: qsTr("درحال اجرا...")

    // Remove Title Bar
    flags: Qt.Window | Qt.FramelessWindowHint

    // Properties
    property int timeInterval: 2900

    Style {
        id: appStyle
    }

    Timer {
         id: timer
         interval: timeInterval
         running: true
         repeat: false
         onTriggered: {
             var component = Qt.createComponent("main.qml")
             var win = component.createObject()
             win.show()
             visible = false
         }
     }

    Rectangle {
        id: bg
        color: appStyle.primary
        radius: 0
        anchors.fill: parent
        anchors.margins: 10
        z: 1

        Image {
            id: logoImage
            width: 120
            height: 120
            opacity: 1
            anchors.top: bg.top
            source: "../ui/images/images/logo_90x90.png"
            rotation: 360
            sourceSize.height: 120
            sourceSize.width: 120
            anchors.topMargin: 70
            anchors.horizontalCenter: bg.horizontalCenter
            fillMode: Image.PreserveAspectFit
        }
        ColorOverlay {
            anchors.fill: logoImage
            source: logoImage
            color: "white"
            cached: true
        }

        FontLoader { id: vazir; source: "../ui/assets/fonts/Vazir.ttf" }

        Label {
            id: label
            opacity: 1
            color: appStyle.textHeader
            text: qsTr("پردازش بیگ دیتا علم و صنعت ایران")
            anchors.bottom: bg.bottom
            anchors.bottomMargin: 50
            font.family: vazir.name
            font.bold: true
            font.pointSize: 12
            anchors.horizontalCenter: bg.horizontalCenter
        }
    }

    DropShadow{
        anchors.fill: bg
        source: bg
        verticalOffset: 0
        horizontalOffset: 0
        radius: 10
        color: "#40000000"
        z: 0
    }

    Timeline {
        id: timeline
        animations: [
            TimelineAnimation {
                id: timelineAnimation
                duration: 3000
                running: true
                loops: 1
                to: 3000
                from: 0
            }
        ]
        enabled: true
        startFrame: 0
        endFrame: 3000
    }
}
