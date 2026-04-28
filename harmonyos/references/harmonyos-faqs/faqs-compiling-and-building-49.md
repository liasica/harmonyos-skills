---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-49
title: 如何解决SDK与镜像不匹配导致abc文件无法正常运行的问题
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何解决SDK与镜像不匹配导致abc文件无法正常运行的问题
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:17+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:45c8ade503ab0475d6c0e0ae1c6b81aea86f16ee3766accebc8053ea80172628
---

**问题现象**

当SDK版本与镜像版本不匹配时，应用将会闪退并出现jscrash错误，同时hilog中会记录相关日志。

**解决措施**

现象的根本原因是SDK工具与镜像版本不匹配。建议使用匹配的SDK和镜像版本。

查看SDK版本方法：

在工程目录下的 local.properties 文件中获取 SDK 路径，执行 {hwsdk.dir}/openharmony/11/ets/build-tools/ets-loader/bin/ark/build-win/bin/es2abc.exe --bc-version 查看 SDK 版本号，以检验 SDK 与镜像版本是否匹配。
