---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-profiler-13
title: 在macOS上使用Profiler录制数据时，必现trace相关泳道显示“No Data”
breadcrumb: FAQ > DevEco Studio > 性能分析 > 在macOS上使用Profiler录制数据时，必现trace相关泳道显示“No Data”
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:57+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:314eaf46db34abd2c9a008976043bf8cddf93e9220c73dcc388554a3ccd61936
---

**问题现象**

在macOS上使用Profiler录制数据时，可能必现trace相关泳道显示“No Data”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/gy6OV4qGRJ--dXSzNQmMYw/zh-cn_image_0000002624478814.png "点击放大")

**问题原因**

当前macOS型号的芯片不支持trace\_streamer解析，导致在录制数据时，trace相关泳道显示“No Data”。

**根因验证**

可以通过以下步骤验证：

1. 在macOS的DevEco Studio安装目录下，找到trace\_streamer.exe所在的目录。
2. 使用命令行工具，运行trace\_streamer.exe 1.htrace -e 1.db命令来解析一个trace文件。
3. 如果命令执行结果为zsh: bad CPU type in executable，说明当前macOS芯片不支持trace\_streamer解析。

**解决措施**

由于提供的trace\_streamer.exe二进制文件是针对x86架构的，如果macOS使用的是ARM架构，则无法支持。可以通过安装Rosetta转义层来解决此问题。
