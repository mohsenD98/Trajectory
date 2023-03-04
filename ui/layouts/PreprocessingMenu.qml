import QtQuick 2.15
import QtQuick.Controls 2.15
import "../components"

import QtQuick.Layouts 1.15

Flickable {
    id: flickable
    flickableDirection: Flickable.VerticalFlick
    Layout.fillWidth: true
    Layout.fillHeight: true
    Layout.alignment: Qt.AlignLeft | Qt.AlignTop
    contentHeight: left_inside_column.height

    clip: true

    Column{
        id: left_inside_column

        Text {
            text: "preprocessing Config here!"
            color: "white"
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
