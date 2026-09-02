---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-22
title: "DevEco Studio编译时报错FetchPackageInfo: \"@ohos/hamock\" failed"
breadcrumb: "FAQ > DevEco Studio > 环境准备 > DevEco Studio编译时报错FetchPackageInfo: \"@ohos/hamock\" failed"
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:52+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:56cf2cac8b1fc6e45e553fcd1d4b613f08eafac5d8e5b26150799baa16a14896
---

## 问题现象

DevEco Studio编译时报错，报错信息如下：

```txt
ohpm ERROR: NOTFOUND package '@ohos/hamock@1.0.1-rc2' not found from all the registries
ohpm ERROR: missing: @ohos/hamock@1.0.1-rc2, required by @
ohpm ERROR: Found exception: Error: FetchPackageInfo: "@ohos/hamock" failed, reached retry limit or non retryable error encountered.
ohpm ERROR: Install failed, detail: Error: FetchPackageInfo: "@ohos/hamock" failed
```

## 背景知识

* [Hamock](https://ohpm.openharmony.cn/#/cn/detail/@ohos%2Fhamock)是OpenHarmony上的模拟框架，提供预览场景的模拟功能。
* [配置代理](../harmonyos-guides/ide-environment-config.md)：DevEco Studio开发环境依赖于网络环境，需要连接上网络才能确保工具的正常使用。

## 解决方案

1. 修改ohpm代理信息，详情请参考：[配置OHPM代理](../harmonyos-guides/ide-environment-config.md#section10372836765)。
2. 将工程级目录下的oh-package.json5中的devDependencies中的@ohos/hamock版本修改为"1.0.0"。
3. 执行Build -> Clean Project操作后，再重新Build。
