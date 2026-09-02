---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-58
title: 使用串口开发API时提示系统能力不支持
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > 使用串口开发API时提示系统能力不支持
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:39+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:014068620073833800ba278c441b4f0aca16b0a618f165126f95eefeea7e131f
---

## 问题现象

使用API19的串口开发，提示系统能力不支持，需要配置syscap.json文件，详细报错如下：

```log
The default system capabilities of devices phone do not include SystemCapability.USB.USBManager.Serial. Configure the capabilities in syscap.json.
```

## 解决方案

在DevEco Studio工程的模块“/src/main”目录下，手动创建syscap.json文件,在addedSysCaps字段新增缺失的配置，参考：[多设备应用开发](../best-practices/bpta-multi-device-function.md#多设备应用开发)。
