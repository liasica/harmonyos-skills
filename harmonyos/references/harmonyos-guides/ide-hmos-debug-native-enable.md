---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-debug-native-enable
title: 启动调试
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 启动调试
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:16+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:3e2ee6016cf1aa16bf528d20103d0dd53b97ea2d18cde412163ecd950f99e0bc
---

支持debug模式启动调试，启动调试前选择对应的设备进行调试，可参考[debug启动调试](ide-hmos-debug-arkts-debug.md)。

在启动调试前，点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/nfHAf0E5R8etZKUHKtdYXw/zh-cn_image_0000002781311356.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=4637FC1CD804965C8BE3F1AEC1DA598D125E5E6435B34EF509257558B9791BBE "点击放大")按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/zrBX43xEQkCzBpHzRJVnhA/zh-cn_image_0000002781311358.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=665FF8C8E81B0F8D463C5B805A70A4D16578509F812E08530BC2735EDC519EE9)按钮打开配置界面。在**调试器**中选择**调试类型**为Dual (ArkTS/JS + Native) 、Native 或Detect Automatically，设置调试代码类型为C/C++。

**说明** 

Detect Automatically类型会根据当前工程是否为Native工程判断是否启动Native调试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/ZhKiCG2ARgKmWkug2BA75A/zh-cn_image_0000002810750951.png?HW-CC-KV=V1&HW-CC-Date=20261114T004728Z&HW-CC-Expire=31536000000&HW-CC-Sign=83326C39308DED518E28FB178904437566B399A7A3E7F28C4B59CDD6E87914B9)

**调试器**中还支持自定义以下配置：

* **查看静态/全局变量：**勾选**在变量面板中显示静态/全局变量**，调试过程中变量列表会展示静态/全局变量。
* **符号表路径：**在**符号目录**页签，点击**+**，可以添加符号表路径，即带有调试信息的so库。例如，您可以先编译带有调试信息的so库，然后将其调试信息裁剪掉，在设备侧运行无调试信息的so库，调试时将带有调试信息的so库路径添加在这里，可以实现对该so库的调试。
* **预设调试器命令：**在**LLDB启动命令**页签和**LLDB附加命令**页签中预设lldb命令。在**LLDB启动命令**页签中的命令会在LLDB调试器启动之后立即执行，在**LLDB附加命令**页签中的命令会在LLDB调试器成功attach到进程之后执行。
* **日志通道**：在**日志目标通道**中设置LLDB日志输出格式，以冒号分隔的条目列表，每个条目都以一个通道开头，后跟一个以空格分隔的类别列表。
