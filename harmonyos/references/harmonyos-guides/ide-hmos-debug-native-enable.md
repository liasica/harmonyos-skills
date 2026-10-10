---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-debug-native-enable
title: 启动调试
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 启动调试
category: harmonyos-guides
scraped_at: 2026-10-11T07:23:21+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:2282d2b21fab49429634c79e6fe992cb816337ebc8b776a6997bd0d257a9f529
---

支持debug模式启动调试，启动调试前选择对应的设备进行调试，可参考[debug启动调试](ide-hmos-debug-arkts-debug.md)。

在启动调试前，点击编辑器上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/jpQpwLMST1yiskEWH8rhlg/zh-cn_image_0000002750169822.png "点击放大")按钮，在菜单中点击**Application**并选择相应模块，点击右侧![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/JyB7YTBJT5OB4McFwPdCIw/zh-cn_image_0000002750009928.png)按钮打开配置界面。在**调试器**中选择**调试类型**为Dual (ArkTS/JS + Native) 、Native 或Detect Automatically，设置调试代码类型为C/C++。

**说明** 

Detect Automatically类型会根据当前工程是否为Native工程判断是否启动Native调试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/cp1M-X9YT7aqTGZHkgRXUQ/zh-cn_image_0000002779608843.png)

**调试器**中还支持自定义以下配置：

* **查看静态/全局变量：**勾选**在变量面板中显示静态/全局变量**，调试过程中变量列表会展示静态/全局变量。
* **符号表路径：**在**符号目录**页签，点击**+**，可以添加符号表路径，即带有调试信息的so库。例如，您可以先编译带有调试信息的so库，然后将其调试信息裁剪掉，在设备侧运行无调试信息的so库，调试时将带有调试信息的so库路径添加在这里，可以实现对该so库的调试。
* **预设调试器命令：**在**LLDB启动命令**页签和**LLDB附加命令**页签中预设lldb命令。在**LLDB启动命令**页签中的命令会在LLDB调试器启动之后立即执行，在**LLDB附加命令**页签中的命令会在LLDB调试器成功attach到进程之后执行。
* **日志通道**：在**日志目标通道**中设置LLDB日志输出格式，以冒号分隔的条目列表，每个条目都以一个通道开头，后跟一个以空格分隔的类别列表。
