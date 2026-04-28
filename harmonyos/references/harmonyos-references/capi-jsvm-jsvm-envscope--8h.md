---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-envscope--8h
title: JSVM_EnvScope__*
breadcrumb: API参考 > 公共基础能力 > C API > 结构体 > JSVM_EnvScope__*
category: harmonyos-references
scraped_at: 2026-04-28T08:19:26+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c32b7116bcef611572447eff1bcc006adfe7db889d757527f6d8972d67dc98a8
---

```
1. typedef struct JSVM_EnvScope__* JSVM_EnvScope
```

## 概述

PhonePC/2in1TabletWearable

表示用于控制附加到当前虚拟机实例的环境。只有当线程通过OH\_JSVM\_OpenEnvScope进入该环境的JSVM\_EnvScope后，该环境才对线程的虚拟机实例可用。

**起始版本：** 11

**相关模块：** [JSVM](capi-jsvm.md)

**所在头文件：** [jsvm\_types.h](capi-jsvm-types-h.md)
