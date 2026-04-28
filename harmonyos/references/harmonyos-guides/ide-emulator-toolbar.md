---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-toolbar
title: 使用工具栏
breadcrumb: 指南 > 编写与调试应用 > 使用模拟器运行应用 > 使用模拟器 > 使用工具栏
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cedf45f2bd58d804b1b0aeb14f2ee65dce3c2c44b7be7ddddc7e42d3d5fe1b89
---

工具栏上集成了模拟器的各种调试工具和控制选项，其中的扩展菜单栏包含了更加丰富的扩展功能。注意，部分工具栏按键需要在模拟器开机亮屏后才能使用。以下对工具栏的各个按键功能作简要说明：

| 按键 | 功能描述 |
| --- | --- |
| 关闭 | 关闭模拟器。 |
| 最小化 | 最小化模拟器窗口。 |
| 更多 | 打开侧边扩展菜单。 |
| 电源 | 模拟电源，可模拟亮灭屏操作，从DevEco Studio 6.1.0 Beta1版本开始支持。 |
| 置顶 | 将模拟器置于所有打开窗口的顶层。 |
| 左旋转 | 将设备屏幕逆时针旋转90度。 |
| 右旋转 | 将设备屏幕顺时针旋转90度。 |
| 增大音量 | 调高设备音量，长按可持续调高设备音量。 |
| 减小音量 | 调低设备音量，长按可持续调低设备音量。 |
| 截屏 | 生成当前屏幕的截图，并将图片保存在本地计算机。 |
| 返回 | 返回上一屏幕或关闭对话框、选项菜单、通知面板或屏幕键盘。 |
| 主屏 | 返回Home界面。 |
| 最近 | 点按可打开最近使用过的应用的缩略图列表。要打开某个应用，请点按其缩略图。要从列表中删除缩略图，请向上滑动缩略图。 |
| 摇一摇 | 触发设备摇一摇操作，详情参考[摇一摇](ide-emulator-more-features.md#section1241612419541)。 |
| 多屏 | 打开多屏面板，可以动态增删屏幕，详情参考[多屏](ide-emulator-more-features.md#section9744191415368)。 |
| 电池 | 打开电池模拟面板，详情参考[电池](ide-emulator-more-features.md#section169214910812)。 |
| GPS | 打开GPS模拟面板，详情参考[GPS定位](ide-emulator-more-features.md#section81566471211)。 |
| 虚拟传感器 | 打开虚拟传感器面板，详情参考[虚拟传感器](ide-emulator-more-features.md#section830415558395)。 |
| 网络代理 | 打开网络代理面板，详情参考[网络](ide-emulator-more-features.md#section206461549731)。 |
| 设置 | 打开设置面板。可设置模拟器主题、截屏保存路径、模拟器使用语言。 |
| Bug报告 | 打开Bug报告面板。点击**保存并发送**按钮可以将Bug日志传递给我们。 |
| 关于 | 打开关于面板。可以查看模拟器相关信息及许可证。 |
| 展开 | 仅支持可折叠设备。切换设备形态至展开态。 |
| 悬停 | 仅支持可折叠设备。切换设备形态至悬停态，并显示折痕避让区。 |
| 折叠 | 仅支持可折叠设备。切换设备形态至折叠态。 |
| 三屏 | 仅支持三折叠设备。切换设备形态至左展开，右展开状态。对应[FOLD\_STATUS\_EXPANDED\_WITH\_SECOND\_EXPANDED](../best-practices/bpta-matext-guide.md#section152802181518)状态。 |
| 双屏 | 仅支持三折叠设备。切换设备形态至左折叠，右展开状态。对应FOLD\_STATUS\_EXPANDED状态。 |
| 单屏 | 仅支持三折叠设备。切换设备形态至左折叠，右折叠状态。对应FOLD\_STATUS\_FOLDED状态。 |
| 左半折，右展开 | 仅支持三折叠设备。切换设备形态至左半折，右展开状态，并显示折痕避让区。对应FOLD\_STATUS\_EXPANDED\_WITH\_SECOND\_HALF\_FOLDED状态。  从DevEco Studio 6.1.0 Beta2版本开始支持。 |
| 左展开，右半折 | 仅支持三折叠设备。切换设备形态至左展开，右半折状态，并显示折痕避让区。对应FOLD\_STATUS\_HALF\_FOLDED\_WITH\_SECOND\_EXPANDED状态。  从DevEco Studio 6.1.0 Beta2版本开始支持。 |
| 左半折，右半折 | 仅支持三折叠设备。切换设备形态至左半折，右半折状态，并显示折痕避让区。对应FOLD\_STATUS\_HALF\_FOLDED\_WITH\_SECOND\_HALF\_FOLDED状态。  从DevEco Studio 6.1.0 Beta2版本开始支持。 |
| 左折叠，右半折 | 仅支持三折叠设备。切换设备形态至左折叠，右半折状态，并显示折痕避让区。对应FOLD\_STATUS\_HALF\_FOLDED状态。  从DevEco Studio 6.1.0 Beta2版本开始支持。 |
| 左半折，右折叠 | 仅支持三折叠设备。切换设备形态至左半折，右折叠状态。对应FOLD\_STATUS\_FOLDED\_WITH\_SECOND\_HALF\_FOLDED状态。  从DevEco Studio 6.1.0 Beta2版本开始支持。 |
| 左展开，右折叠 | 仅支持三折叠设备。切换设备形态至左展开，右折叠状态。对应FOLD\_STATUS\_FOLDED\_WITH\_SECOND\_EXPANDED状态。  从DevEco Studio 6.1.0 Beta2版本开始支持。 |
| 横展 | 仅支持折叠2in1设备。切换设备形态至横展状态。 |
| 竖展 | 仅支持折叠2in1设备。切换设备形态至竖展状态。 |
| 悬停 | 仅支持折叠2in1设备。切换设备形态至悬停状态。 |
| 磁吸 | 仅支持折叠2in1设备。切换设备形态至磁吸状态。 |
