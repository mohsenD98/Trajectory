import QtQuick 2.15

GroupBox {
    id: box
    property bool running: false

    signal runThisBox()

    IconButton{
        width: 24
        height: 24
        iconColor: "#b9bbbe"
        iconWidth: 22
        iconHeight: 22
        visible: running
        anchors.right: parent.right
        anchors.rightMargin: 8
        anchors.verticalCenter: box.top
        iconPath: "../images/svg_icons/play.svg"
        CenteredTooltip{ text: "Running!"; inverted: true }
    }

    IconButton{
        width: 50
        height: 50
        iconColor: "#b9bbbe"
        iconWidth: 48
        visible: !running
        iconHeight: 48
        anchors.centerIn: parent
        iconPath: "../images/svg_icons/play.svg"
        onClickDetected: {
            running = true

            runThisBox()
        }

        CenteredTooltip{ text: "Run"; inverted: true }
    }
}
