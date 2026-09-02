---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-27
title: 在IDE的控制台中输入ohpm -v报错Failed to find the executable 'node' command怎么处理
breadcrumb: FAQ > DevEco Studio > 环境准备 > 在IDE的控制台中输入ohpm -v报错Failed to find the executable 'node' command怎么处理
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:52+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:11c1d8079a03b392c487cc2d10f617e871f6414cf889649a9626219587097787
---

## 问题现象

在终端中输入ohpm -v报错Failed to find the executable 'node' command怎么处理？日志信息如下：

```log
PS D:\MyApplication2> node -v
v18.20.1
PS D:\MyApplication2> npm -v
10.5.0
PS D:\MyApplication2> ohpm -v
ERROR: Failed to find the executable 'node' command, please check the following possible causes:
  1. NodeJS is not installed.
  2. 'node' command not added to PATH
  and the 'NODE_HOME' variable is not set in the environment variables to match your NodeJs installation Location.
```

## 解决方案

1. 检查系统的[环境变量](../harmonyos-guides/ide-environment-config.md)是否配置了SDK的toolchains。
2. 检查DevEco Studio的Terminal是否自动添加了ohpm到path。配置路径：Settings->Terminal->Add XXX path to %PATH%。
3. 手动[将Node.js配置到系统环境变量中](../harmonyos-guides/ide-environment-config.md#section197296441787)。
4. 卸载重装[最新版DevEco Studio](https://developer.huawei.com/consumer/cn/download/)。

   DevEco Studio从DevEco Studio 5.0.0 Release（5.0.3.906）[新增特性](../harmonyos-releases/deveco-studio-new-features-500-release.md#section158413188453)，提供开箱即用的开发体验，将SDK、Node.js、Hvigor、OHPM等工具链进行合一打包，简化DevEco Studio安装配置流程。按照提示正确安装后，无需配置即可使用。
