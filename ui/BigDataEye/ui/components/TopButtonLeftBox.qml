import QtQuick 2.15
import QtQuick.Controls 2.15
import Qt5Compat.GraphicalEffects

Button {
    id: btn
    width: parent.width
    text: qsTr("Button")
    font.weight: Font.Medium
    leftPadding: 10
    rightPadding: 30
    font.pointSize: 10
    font.family: appStyle.font

    // Custom Properties
    property color colorBg: "#00000000"
    property color colorBgEntered: "#5c6fb1"
    property color colorBgPressed: "#5365a1"
    property color iconColor: "#b9bbbe"
    property color iconColorEntered: "#f9f9fc"
    property color textColor: "#b9bbbe"
    property color textColorEntered: "#f9f9fc"
    property url iconPath: "../../ui/images/svg_icons/icon_online.svg"
    property int btnHeight: 32
    property bool enableDescription: false
    property string descriptionText: "Set here a description for this button"
    property int iconWidth: 20
    property int iconHeight: 20

    // Hight
    height: btnHeight

    QtObject{
        id: internal

        property color dynamicBg: if(btn.down){
                                      btn.down ? colorBgPressed : colorBg
                                  } else {
                                      btn.hovered ? colorBgEntered : colorBg
                                  }
        property color dynamicIconColor: if(btn.down){
                                      btn.down ? iconColorEntered : iconColor
                                  } else {
                                      btn.hovered ? iconColorEntered : iconColor
                                  }
        property color dynamicText: if(btn.down){
                                      btn.down ? textColorEntered : textColor
                                  } else {
                                      btn.hovered ? textColorEntered : textColor
                                  }
    }

    contentItem: Item{
        id: item1
        Text{
            id: textBtn
            text: btn.text
            anchors.top: item1.top
            verticalAlignment: Text.AlignVCenter
            anchors.verticalCenter: parent.verticalCenter
            font.weight: btn.font.weight
            font.family: btn.font.family
            font.pointSize: btn.font.pointSize
            color: internal.dynamicText
        }
        Text{
            id: description
            text: descriptionText
            width: 175
            anchors.top: textBtn.bottom
            wrapMode: Text.Wrap
            rightPadding: 9
            anchors.verticalCenter: parent.verticalCenter
            font.weight: Font.Normal
            font.family: btn.font.family
            font.pointSize: 8
            color: internal.dynamicText
            visible: enableDescription
        }
    }

    background: Rectangle{
        id: bg
        color: internal.dynamicBg
        radius: 3
    }

    Image {
        id: icon
        source: iconPath
        fillMode: Image.PreserveAspectFit
        sourceSize.height: iconHeight
        sourceSize.width: iconWidth
        width: iconWidth
        height: iconHeight
        anchors.right: btn.right
        anchors.rightMargin: 10
        visible: false
        anchors.verticalCenter: btn.verticalCenter
    }

    ColorOverlay{
        id: overlay
        source: icon
        anchors.fill: icon
        color: internal.dynamicIconColor
        antialiasing: true
        cached: true
    }

    MouseArea{
        anchors.fill: btn
        cursorShape: Qt.PointingHandCursor
//        onPressed: mouse.accepted = false
    }

}
