---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-hvigor-path
title: 自定义.hvigor目录路径
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 构建应用 > 配置构建流程 > 自定义.hvigor目录路径
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:35+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:77a2a8566fc2cba3430153fe4f5442c85faa674edc9808533df08e1ac23afcc0
---

.hvigor目录默认位于用户目录下：/storage/Users/currentUser/.hvigor

若默认目录的磁盘空间不足，开发者需要自定义.hvigor目录路径，可通过以下方式自行配置。

**说明** 

自定义.hvigor目录时，不能包含空格。

1. 打开终端工具，执行以下命令。

   ```bash
   vim ~/.zshrc
   ```
2. 添加HVIGOR\_USER\_HOME环境变量。

   ```bash
   export HVIGOR_USER_HOME=~/xx  #本处路径请替换为.hvigor目录的绝对路径
   ```
3. 保存并关闭文件，使用source命令重新加载.zshrc配置文件。

   ```bash
   source ~/.zshrc
   ```
