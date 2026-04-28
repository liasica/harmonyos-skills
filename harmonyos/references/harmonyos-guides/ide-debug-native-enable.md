---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-enable
title: 启动调试
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > Native代码调试 > 启动调试
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:49+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:d5cf9ab7e7bdf74e8baf6ebc47dc159f523b1d60384ac29ee8327a02ca4dedc1
---

Native代码调试依赖LLDB调试器，关于LLDB调试器的介绍请参考[LLDB高性能调试器](debug-lldb.md)。

在启动调试前，点击**Run > Edit Configurations**打开调试配置界面，在**Debugger**页签选择**Debug type**为Dual (ArkTS/JS + Native) 、Native 或Detect Automatically，设置调试代码类型为C/C++。

说明

* Detect Automatically类型会根据当前工程是否为native工程判断是否启动native调试。

* 如果调试时启用编译器优化，增加编译优化选项或使用[release编译模式](ide-hvigor-compilation-options-customizing-guide.md#section192461528194916)等，编译器会对编译后的汇编指令进行更改，从而使得代码运行更加高效。但优化后的指令难以与原始代码形成映射关系，可能会导致在调试的过程中出现异常或错误信息，例如局部变量信息被删除、无法正确跳转到期望的代码行等。因此，在调试的过程中需要关闭编译优化选项或者使用debug编译模式，避免因优化而导致的异常。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/lu3VT19ySqSUvJkBhe0ewg/zh-cn_image_0000002561753347.png?HW-CC-KV=V1&HW-CC-Date=20260427T235648Z&HW-CC-Expire=86400&HW-CC-Sign=333A5FC7A92D18F4D9C5167190E5A57B751769C4EE0E5C0CEEE558E35382DB9A)

**Debugger**页签中还支持自定义以下配置：

* **查看静态/全局变量：**勾选**Show static/global variables in the Variables Pane**，调试过程中变量列表会展示静态/全局变量。
* **符号表路径：**在**Symbol Directories**页签，点击**+**，可以添加符号表路径，即带有调试信息的so库。例如，您可以先编译带有调试信息的so库，然后将其调试信息裁减掉，在设备侧运行无调试信息的so库，调试时将带有调试信息的so库路径添加在这里，可以实现对该so库的调试。
* **预设调试器命令：**在**LLDB Startup Commands**页签和**LLDB Post Attach Commands**页签中预设lldb命令。在**LLDB Startup Commands**页签中的命令会在LLDB调试器启动之后立即执行，在**LLDB Post Attach Commands**页签中的命令会在LLDB调试器成功attach到进程之后执行。

配置完成后可启动Native代码调试，支持debug和attach模式启动调试，详细内容可参考[debug启动调试](ide-debug-arkts-debug.md)或[attach启动调试](ide-debug-arkts-attach.md)章节。
