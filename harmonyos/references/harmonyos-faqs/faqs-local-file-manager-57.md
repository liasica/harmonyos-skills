---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-57
title: 通过API获取文件系统总存储空间、空闲可用存储空间与手机存储内存显示不一致
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 通过API获取文件系统总存储空间、空闲可用存储空间与手机存储内存显示不一致
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:30+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:63b55158914138770faec5ed31ae069adb14f5c7982d7eca73edde15614c164e
---

## 问题现象

通过系统API读取到的存储空间数据（总空间、可用空间），与手机系统设置中显示的内存信息存在偏差，两者无法对应。

## 背景知识

[@ohos.file.statvfs](../harmonyos-references/js-apis-file-statvfs.md)（文件系统空间统计）模块提供文件系统相关存储信息的功能：向应用程序提供获取文件系统总字节数、空闲字节数的接口。[@ohos.hidebug](../harmonyos-references/js-apis-hidebug.md)（Debug调试）模块为应用提供多种以供调试、调优的方法。包括但不限于内存、CPU、GPU、GC等相关数据的获取，进程trace、profiler采集，VM堆快照转储等。

* 获取总存储空间API：[statfs.getTotalSize](../harmonyos-references/js-apis-file-statvfs.md#statfsgettotalsize)。
* 获取空闲存储空间API：[statfs.getFreeSize](../harmonyos-references/js-apis-file-statvfs.md#statfsgetfreesize)。
* 获取系统运行内存情况API：[hidebug.getSystemMemInfo](../harmonyos-references/js-apis-hidebug.md#hidebuggetsystemmeminfo12)。

## 问题定位

1. 查看手机设备内存大小。
2. 调用相关API获取相应大小。
3. 对比设备内存大小与API接口返回的大小是否一致。
4. 确认API接口返回的内存值是属于哪一部分的内存。

## 分析结论

* getTotalSizeAPI获取的是沙箱目录可使用的大小，getFreeSize获取的是沙箱目录剩余可使用的大小，不是手机内存大小。三方应用只能通过statvfs.getTotalSize()与statvfs.getFreeSize()获取应用沙箱目录的内存大小。
* hidebug.getSystemMemInfo接口可以获取手机的运行内存情况，包括系统总的运行内存、系统空闲的运行内存、系统可用的运行内存。

## 修改建议

* 获取三方应用沙箱目录可使用的大小建议使用@ohos.file.statvfs模块的接口。
* 获取手机运行内存情况可以使用@ohos.hidebug模块的getSystemMemInfo接口获取。
