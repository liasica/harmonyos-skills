---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-61
title: USB-串口应用打开/dev/bus下文件无权限
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > USB-串口应用打开/dev/bus下文件无权限
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:39+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4dc39cc8bbcfeb35ef00ac000f7230b556573bde8367969faaa24346f4ab41af
---

## 问题现象

NAPI开发USB-串口应用（CH340转换），打开/dev/bus下文件提示Error: Permission denied。

## 解决方案

/dev下文件的读写权限不对外开放，如果需要对设备操作，可以用[usbManager.getFileDescriptor](../harmonyos-references/js-apis-usbmanager.md#usbmanagergetfiledescriptor)接口。
