---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-83
title: HarmonyOS下hidumper与SP_daemon工具常见问题解析
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > HarmonyOS下hidumper与SP_daemon工具常见问题解析
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:50+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:5b9171857a56a93aa02dc6cdebfa6778d779b3464ceff5db85c906d342993c92
---

## 问题现象

**场景一：**

通过hidumper命令如何查询屏幕分辨率及折叠状态。

**场景二：**

通过hidumper如何查看应用占用的内存大小。

**场景三：**

通过hidumper --mem-jsheap命令生成内存快照文件时，当存在多个线程时会生成多个快照文件，应重点分析哪几个文件。

**场景四：**

SP\_daemon命令中的-VIEW参数DisplayNode如何获取？

## 解决方案

**场景一：**

* 通过"hdc shell hidumper -s 10 -a screen"命令可以查看屏幕分辨率，当前存在多个屏幕时，会依次展示各屏幕分辨率信息。
* 通过"hdc shell hidumper -s DisplayManagerService -a '-a'"命令可以查看折叠状态，当"FoldStatus"字段为"FOLDED"时，表示当前为折叠状态；当"FoldStatus"字段为"EXPAND"时，表示当前为展开状态。

**场景二：**

使用hidumper --mem pid命令可以获取指定进程的内存使用情况，pid为指定的进程号，具体见[查询进程内存](../harmonyos-guides/hidumper.md#查询进程内存)。重点关注PSS的大小，PSS是一种更精确的内存使用度量方法，它将共享库所占的内存按比例分配给每个使用该库的进程。

**场景三：**

应重点分析如下两个快照文件：

1. 主线程的快照文件。
2. 对比两次dump的子线程快照文件，找出文件大小变化最大和node\_count变化最大的子线程对应的快照文件，当node\_count持续增长而业务没有大量新创建对象时，很有可能存在内存泄漏。

**场景四：**

DisplayNode不是固定字符串，而是当前系统中真实存在的图层名称，可通过以下方式查看：

1. 执行"hidumper -s RenderService -a screen"或"hidumper -s RenderService -a surfaces"查看系统图层，输出中会列出类似EntryView、NavigationView、XComponent、WebView、Image等图层名称。
2. 找到目标图层名称后，作为-VIEW参数传入，例如"SP\_daemon -N 10 -VIEW XComponent -f"。
3. 也可以直接执行"hidumper -s RenderService"，搜索"surface node display"相关关键字，部分版本会打印完整的RenderNode树，从中找到当前页面对应的图层名。
4. 如果测试的是自己的应用，可执行"hidumper -s RenderService -a screen | grep [包名]"，直接定位到应用对应的Surface名称。
