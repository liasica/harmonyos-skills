---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-profiler-13
title: 在macOS上使用Profiler录制数据时，必现trace相关泳道显示“No Data”
breadcrumb: FAQ > DevEco Studio > 性能分析 > 在macOS上使用Profiler录制数据时，必现trace相关泳道显示“No Data”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:34+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:78cb09e15b2c2d9cdc089e3e331029461100307c58afe5bb80cf53720120dd1e
---

**问题现象**

在macOS上使用Profiler录制数据时，可能必现trace相关泳道显示“No Data”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/6aceKO6bS5KwEMOiNB97jw/zh-cn_image_0000002516464433.png?HW-CC-KV=V1&HW-CC-Date=20260429T062133Z&HW-CC-Expire=86400&HW-CC-Sign=1735EDAFE587614FD64B871C545ABDA86EB3CF20A5C31714772B22D42A89DEB2 "点击放大")

**问题原因**

当前macOS型号的芯片不支持trace\_streamer解析，导致在录制数据时，trace相关泳道显示“No Data”。

**根因验证**

可以通过以下步骤验证：

1. 在macOS的DevEco Studio安装目录下，找到trace\_streamer.exe所在的目录。
2. 使用命令行工具，运行trace\_streamer.exe 1.htrace -e 1.db命令来解析一个trace文件。
3. 如果命令执行结果为zsh: bad CPU type in executable，说明当前macOS芯片不支持trace\_streamer解析。

**解决措施**

由于提供的trace\_streamer.exe二进制文件是针对x86架构的，如果macOS使用的是ARM架构，则无法支持。可以通过安装Rosetta转义层来解决此问题。
