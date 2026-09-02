---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-childprocessconfigs
title: Ability_ChildProcessConfigs
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > C API > 结构体 > Ability_ChildProcessConfigs
category: harmonyos-references
scraped_at: 2026-09-02T14:51:06+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:229c3e1fb0fab037e0a6c9bc4803e068b23165ef96c5ef675b0c7e041a8267fd
---

```c
typedef struct Ability_ChildProcessConfigs Ability_ChildProcessConfigs;
```

## 概述

启动子进程的配置信息，包括子进程的进程名、数据沙箱与网络环境的共享模式、主进程与子进程的uid是否隔离的配置。开发者可以使用[OH\_Ability\_ChildProcessConfigs\_SetProcessName](capi-native-child-process-h.md#oh_ability_childprocessconfigs_setprocessname)、[OH\_Ability\_ChildProcessConfigs\_SetIsolationMode](capi-native-child-process-h.md#oh_ability_childprocessconfigs_setisolationmode)、[OH\_Ability\_ChildProcessConfigs\_SetIsolationUid](capi-native-child-process-h.md#oh_ability_childprocessconfigs_setisolationuid)接口来修改相应的配置信息。

**起始版本：** 20

**相关模块：** [ChildProcess](capi-childprocess.md)

**所在头文件：** [native\_child\_process.h](capi-native-child-process-h.md)
