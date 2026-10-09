---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-commandline-get
title: 获取Command Line Tools
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 命令行工具 > 获取Command Line Tools
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:37+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:fa1bb871ed41c3ae5224e6c1577e0048e73f338f31d778ff26011683f139afea
---

Command Line Tools集合了HarmonyOS应用开发所用到的系列工具，包括代码检查codelinter、命令行构建hvigorw、三方依赖管理ohpm和SDK中包含的一系列工具，本文主要讲解codelinter、hvigorw等工具的使用方式，关于SDK中包含的工具的使用指导请参考[SDK命令行工具](command-line-tools-overview.md)。

## 下载Command Line Tools

请前往[下载中心](https://developer.huawei.com/consumer/cn/download/command-line-tools-for-hmos)获取命令行工具Command Line Tools，并根据下载中心页面**工具完整性**指导进行完整性校验。

**说明** 

HarmonyOS SDK已嵌入命令行工具中，无需额外下载配置。

## 解压命令行工具

在终端中执行命令，解压命令行工具commandline-tools-harmonyos-xxx.tar.gz，工具名称请根据实际情况进行修改。

```bash
tar -zxvf commandline-tools-harmonyos-xxx.tar.gz
```

## 配置环境变量

在~/.zshrc文件中配置环境变量。

1. 打开终端工具，执行以下命令。

   ```bash
   vim ~/.zshrc
   ```
2. 配置Node.js、sdk环境变量。

   ```bash
   export PATH=$PATH:${Command Line Tools解压路径}/command-line-tools/node/bin      # 配置Node.js环境变量
   export DEVECO_SDK_HOME=${Command Line Tools解压路径}/command-line-tools/sdk      # 配置sdk环境变量
   ```
3. 根据需要使用的工具，配置对应的环境变量。

   ```bash
   export PATH=$PATH:${Command Line Tools解压路径}/command-line-tools/hvigor/bin        # 配置hvigor环境变量
   export PATH=$PATH:${Command Line Tools解压路径}/command-line-tools/ohpm/bin          # 配置ohpm环境变量
   export PATH=$PATH:${Command Line Tools解压路径}/command-line-tools/codelinter/bin    # 配置codelinter环境变量
   ```
4. 保存并关闭文件，使用source命令重新加载.zshrc配置文件。

   ```bash
   source ~/.zshrc
   ```
5. 执行如下命令，查询版本信息，确认配置成功。

   ```screen
   node -v
   hvigorw -v
   ohpm -v
   codelinter -v
   ```
