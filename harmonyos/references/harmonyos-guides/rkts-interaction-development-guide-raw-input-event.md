---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/rkts-interaction-development-guide-raw-input-event
title: 输入设备与事件
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 添加交互响应 > 输入设备与事件
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:50+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a10666b10874075d9a4f0350fe80259d6db17c72cc27d6edd563f0a8fb995ae5
---

不同的输入设备会产生不同的事件类型。只有在用户操作特定输入设备和工具时，才会触发基础事件。通过输入设备和工具类型，可以区分这些事件。

* 输入设备(source type)：即事件来源的设备类型，是真正产生了底层事件的设备，如触摸屏、鼠标、触控板、键盘、摇杆等；
* 输入工具(source tool)：表示产生该事件的具体工具，比如触摸屏上要产生触摸事件，那么可以使用的工具是手指或触控笔；

在很多情况下，输入设备自己本身也可以作为输入工具，如键盘、鼠标。

说明

建议直接使用手势系统来处理交互，可不关注基础事件之间的区别。

[支持触屏输入事件](arkts-interaction-development-guide-touch-screen.md)：触屏设备及对其产生的触摸事件。

[支持鼠标输入事件](arkts-interaction-development-guide-mouse.md)：鼠标设备及如何处理其产生的事件。

[支持触控板输入事件](arkts-interaction-development-guide-touchpad.md)：触控板设备及如何处理其产生的事件。

[支持键盘输入事件](arkts-interaction-development-guide-keyboard.md)：键盘类设备及如何处理其产生的事件。

[支持游戏手柄输入事件](arkts-interaction-development-guide-gamepad.md)：游戏手柄设备及如何处理其产生的事件。

[支持表冠输入事件](arkts-common-events-crown-event.md)：旋转表冠及其如何处理其产生的事件。

* **[支持触屏输入事件](arkts-interaction-development-guide-touch-screen.md)**
* **[支持鼠标输入事件](arkts-interaction-development-guide-mouse.md)**
* **[支持触控板输入事件](arkts-interaction-development-guide-touchpad.md)**
* **[支持键盘输入事件](arkts-interaction-development-guide-keyboard.md)**
* **[支持游戏手柄输入事件](arkts-interaction-development-guide-gamepad.md)**
* **[支持表冠输入事件](arkts-common-events-crown-event.md)**
