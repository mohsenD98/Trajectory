import QtQuick 2.15
import QtQuick.Controls 2.15
import Qt5Compat.GraphicalEffects

import "../../components"

Item {
    id: bottomBox
    width: 240
    height: 50
    property url imagePath: "../../../ui/images/images/me.png"
    property url statusIcon: "../../../ui/images/svg_icons/icon_idle.svg"
    property bool showPopup: false

    Rectangle {
        id: profileSettings
        width: 300
        height: 100
        color: "#18191c"
        radius: 5
        anchors.bottom: bottomBox.bottom
        anchors.horizontalCenter: bottomBox.horizontalCenter
        anchors.bottomMargin: 55
        clip: true
        scale: 0
        visible: true
        transformOrigin: Item.Bottom
        z: 40

    }

    // Set Image BTN
    Rectangle{
        id: iconBox
        width: 34
        height: 34
        radius: 17
        clip: false
        anchors.verticalCenter: bottomBox.verticalCenter
        anchors.left: bottomBox.left
        anchors.leftMargin: 8
        color: "#292b2f"

        Image {
            id: image
            anchors.verticalCenter: iconBox.verticalCenter
            source: imagePath
            anchors.horizontalCenter: iconBox.horizontalCenter
            fillMode: Image.PreserveAspectFit
            sourceSize.height: 34
            sourceSize.width: 34
            width: 34
            height: 34

            // Enable Layer
            layer.enabled: true
            layer.effect: OpacityMask{
                maskSource: iconBox
            }
        }

        // Icon Status
        Rectangle {
            id: iconCircle
            anchors.right: iconBox.right
            anchors.bottom: iconBox.bottom
            anchors.rightMargin: -2
            anchors.bottomMargin: -2
            width: 16
            height: 16
            color: "#292b2f"
            radius: 8
            clip: true

            Image{
                id: icon
                source: statusIcon
                anchors.horizontalCenter: iconCircle.horizontalCenter
                fillMode: Image.PreserveAspectFit
                sourceSize.height: 12
                sourceSize.width: 12
                width: 12
                height: 12
                anchors.verticalCenter: iconCircle.verticalCenter

                // Enable Layer
                layer.enabled: true
                layer.effect: OpacityMask{
                    maskSource: iconCircle
                }
            }
        }
    }

    Rectangle {
        id: textBox
        width: 80
        height: 34
        color: "#00000000"
        anchors.verticalCenter: bottomBox.verticalCenter
        anchors.left: iconBox.right
        anchors.leftMargin: 8

        Text{
            width: textBox.width
            text: "Dehghanzadeh"
            font.pointSize: 10
            font.family: appStyle.font
            font.weight: Font.Bold
            anchors.verticalCenter: parent.verticalCenter
            color: "#ffffff"
        }
    }

    IconButtonBg {
        id: iconSettings
        width: 32
        height: 32
        anchors.verticalCenter: bottomBox.verticalCenter
        anchors.right: bottomBox.right
        iconPath: "../../ui/images/svg_icons/icon_settings.svg"
        anchors.rightMargin: 8
        hoverEnabled: true
        onPressed: console.log("User Settings")
        CenteredTooltip{ text: "User Settings"; }
    }


    MouseArea{
        anchors.fill: iconSettings
        hoverEnabled: true
        onEntered: iconSettings.opacity = 0.8
        onExited: iconSettings.opacity = 1
        onPressed: {
            if(!showPopup){
                statusClicked.running = true
                console.log("Show Popup")
                showPopup = true
            } else {
                statusExited.running = true
                console.log("Hide Popup")
                showPopup = false
            }
        }
        cursorShape: Qt.PointingHandCursor
    }

    // Animation
    PropertyAnimation{
        id: statusClicked
        target: profileSettings
        properties: "scale"
        to: 1
        duration: 200
        easing.type: Easing.OutQuint
    }
    PropertyAnimation{
        id: statusExited
        target: profileSettings
        properties: "scale"
        to: 0
        duration: 25
        easing.type: Easing.OutQuint
    }
}
