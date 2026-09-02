---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilitybase-element
title: AbilityBase_Element
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > C API > 结构体 > AbilityBase_Element
category: harmonyos-references
scraped_at: 2026-09-02T15:00:37+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2f98b429d5bb8e705dae7bff4adcf558567c42f9904fbd242186570ecab4c216
---

```c
typedef struct AbilityBase_Element {...} AbilityBase_Element
```

## 概述

声明[Want](capi-want-h.md)中Element结构体。

**起始版本：** 15

**相关模块：** [AbilityBase](capi-abilitybase.md)

**所在头文件：** [want.h](capi-want-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char\* bundleName | 应用的包名。 |
| char\* moduleName | 模块名称。 |
| char\* abilityName | Ability名称。 |
