---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-command-line-tool-37
title: 如何获取当前最前台UI界面的应用包名
breadcrumb: FAQ > DevEco Studio > 命令行工具 > 如何获取当前最前台UI界面的应用包名
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:58+08:00
doc_updated_at: 2026-07-22
content_hash: sha256:46e0e043d3e95bf4e97217214a222f2e0bf41bf2e498ed8779cb1c13d2b0784f
---

## 问题现象

如何获取当前最前台UI界面所属应用的信息（如包名）？通过hdc shell aa dump -l或hdc shell aa dump -a命令只能获取最近运行应用的包名，无法准确获取当前最前台UI界面的包名。

## 背景知识

使用[hdc](../harmonyos-guides/hdc.md)工具可以与设备进行交互调试。[uitest dumpLayout](../harmonyos-references/js-apis-uitest.md#dumplayout)命令可以导出当前页面的布局信息，其中包含当前最前台UI界面对应的应用信息。

## 解决方案

通过uitest dumpLayout命令获取最前台UI界面应用信息。

1. 执行以下hdc命令，在设备的/data/local/tmp目录下生成布局信息的JSON文件：

   ```bash
   hdc shell uitest dumpLayout
   ```
2. 通过DevEco Device File Browser（DevEco Studio右侧边工具栏的设备文件浏览器）查看/data/local/tmp目录下的layout\_xxx.json文件。
3. 在JSON文件中，type为root的节点的attributes属性展示了当前页面对应的应用信息，包括abilityName、bundleName以及当前页面对应的页面路径PagePath。

更多详细信息可参考[文档](faq-stability-52.md)。
