---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-39
title: 按照Axios三方库的下载安装步骤安装Axios，报错404如何解决
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 按照Axios三方库的下载安装步骤安装Axios，报错404如何解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:36+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:9b12f68fdc8c681d15e3ea6625f5db21983859259a1a0845c69d205a003d0eee
---

**问题现象**

按照Axios三方库的下载安装步骤安装Axios，执行命令npm install @ohos/axios --save报错，错误码为404。

**解决措施**

错误码404表示资源文件未找到。可能镜像环境配置错误或者OHPM代理配置错误。

1. 打开DevEco中的终端命令窗口。
2. 输入命令：

   ```powershell
   ohpm config set registry https://repo.harmonyos.com/ohpm/
   ```
3. 执行安装Axios三方库的命令：

   ```powershell
   ohpm install @ohos/axios
   ```

OHPM代理配置可参考[配置OHPM代理](../harmonyos-guides/ide-environment-config.md#section10372836765)
