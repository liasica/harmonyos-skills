---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-command-line-tool-23
title: ohpm-repo私仓上传包失败，页面提示系统文件损坏
breadcrumb: FAQ > DevEco Studio > 命令行工具 > ohpm-repo私仓上传包失败，页面提示系统文件损坏
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:58+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0574a6c58179d1a29fec59b51e0179775c7ea706f2d2814ba71f983178a01bd3
---

## 问题现象

开发者发布包到ohpm私仓，报错：

```txt
ohpm ERROR: Publish failed, detail: The "Login" request to url "https://ohpm.xxx/repos/ohpm/login" has failed
```

访问私仓页面提示文件系统损坏。

## 背景知识

[ohpm-repo](../harmonyos-guides/ide-ohpm-repo-overview.md)是一个搭建轻量级的ohpm私仓服务的工具。它与ohpm包管理器兼容，并按需缓存所有依赖项，加速私有网络中的安装。

## 解决方案

根据报错信息分析是加密解密组件与公私钥不匹配导致的。开发者要停止私仓，把public\_key表里面的公私钥数据清除，删除私仓部署目录的meta文件，然后重新[ohpm-repo install](../harmonyos-guides/ide-ohpm-repo-install.md)，再启动私仓。公私钥配置可参考[ohpm-repo认证管理](../harmonyos-guides/ide-ohpm-certification.md)，确保通过ssh-keygen工具生成的公私钥文件是成对的，然后在ohpm-repo私仓管理界面配置公钥信息，在ohpm的.ohpmrc配置文件中配置publish\_id、publish\_registry和key\_path等参数。
