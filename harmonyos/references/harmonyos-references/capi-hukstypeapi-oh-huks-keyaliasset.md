---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-keyaliasset
title: OH_Huks_KeyAliasSet
breadcrumb: API参考 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > C API > 结构体 > OH_Huks_KeyAliasSet
category: harmonyos-references
scraped_at: 2026-09-02T15:01:47+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:dc8f5d56dbc510183b02db14387ebef7e8305783b2fd667ef519a2570e804f5b
---

```c
struct OH_Huks_KeyAliasSet {...}
```

## 概述

定义密钥别名集的结构体类型。

**起始版本：** 20

**相关模块：** [HuksTypeApi](capi-hukstypeapi.md)

**所在头文件：** [native\_huks\_type.h](capi-native-huks-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t aliasesCnt | 密钥别名集个数。 |
| struct [OH\_Huks\_Blob](capi-hukstypeapi-oh-huks-blob.md) \*aliases | 指向密钥别名集数据的指针。 |
