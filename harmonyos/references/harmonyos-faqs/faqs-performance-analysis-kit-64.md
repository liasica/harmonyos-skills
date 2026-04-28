---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-64
title: 解决hdc执行返回command not found
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 解决hdc执行返回command not found
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:23+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:74ef3b38ad1fee7fae000b8f85aa13a5ada59621e43d838402f59bb347f2503a
---

**问题现象**

在命令行工具中hdc执行返回command not found提示命令未找到。

**可能原因**

1. 未正确安装SDK；或安装后未配置环境变量，在非hdc所在目录下执行命令。

2. 环境变量已配置但未生效。

3. 环境变量配置了多个。

4. 输入命令有误。

**解决措施**

1. 请参考hdc[环境准备](../harmonyos-guides/hdc.md#环境准备)正确下载应用后配置完成。

2. 配置环境变量后未刷新

2.1 Windows：配置环境变量前已打开的终端窗口不生效配置，需要打开新的窗口后生效。

2.2 Linux/MacOS：参考hdc[环境准备](../harmonyos-guides/hdc.md#环境准备)编辑完成配置文件后，未完成最后一步source命令执行生效配置；如果仅需在当前终端窗口生效，可仅执行export命令后在当前窗口生效配置。

3. 检查hdc路径配置。

3.1 Windows：打开终端窗口执行where hdc查询，如果显示多条路径，需要在系统环境变量修改PATH的值，移除多余的hdc路径。

3.2 Linux/macOS：打开终端窗口执行which hdc查询，如果显示多条路径，参考hdc[环境准备](../harmonyos-guides/hdc.md#环境准备)中的配置文件，修改配置文件中PATH的变量值，移除多余的hdc路径。

4. 请参考[hdc命令列表](../harmonyos-guides/hdc.md#hdc命令列表)检查命令是否正确。
