---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-21
title: DevEco Studio启动项目报错Project sync failed
breadcrumb: FAQ > DevEco Studio > 环境准备 > DevEco Studio启动项目报错Project sync failed
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:52+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:cad8215680768b271440cc224271167160d4d00f8582e9738be7af880cad8701
---

## 问题现象

DevEco Studio启动项目报错如下：

```txt
Project sync failed. Basic functionality (e.g. editing, debugging) will not work properly.
```

## 背景知识

* 工程项目目录参考：[ArkTS工程目录结构（Stage模型）](../harmonyos-guides/start-with-ets-stage.md#arkts工程目录结构stage模型)。
* 配置代理参考：[配置Proxy代理](../harmonyos-guides/ide-environment-config.md#section10369436568)。

## 问题定位

该报错常见的场景如下：

* **场景一**：检查打开的项目路径是否正确，有可能打开的是项目的父目录或子目录。
* **场景二**：检查是否有网络连接失败问题。
* **场景三**：DevEco Studio缓存问题导致。

## 分析结论

* **场景一**：打开的项目路径不正确。
* **场景二**：网络连接有失败。
* **场景三**：DevEco Studio缓存有问题。

## 修改建议

* **场景一**：确认打开的项目路径是否正确，项目的子目录应当是AppScope和hvigor等这些目录。注意如果打开的是项目的父目录，会导致无法正确识别项目工程，产生如上报错。
* **场景二**：确认是否是代理问题导致网络连接失败。一般来说，如果使用的是个人或家庭网络，是不需要配置代理信息的，部分企业网络受限的情况下，才需要配置代理信息。开发环境问题可以参考官方文档：[诊断开发环境](../harmonyos-guides/ide-environment-config.md#section1912218441119)。代理配置可以参考：[配置代理](../harmonyos-guides/ide-environment-config.md)。
* **场景三**：通过如下步骤清除缓存：DevEco Studio -> File -> Invalidate caches。
