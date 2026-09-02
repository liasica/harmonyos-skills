---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-result
title: OH_Huks_Result
breadcrumb: API参考 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > C API > 结构体 > OH_Huks_Result
category: harmonyos-references
scraped_at: 2026-09-02T15:01:47+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:99ac97abad5b3d88814a3a4b852b4fb497cb0cedfc27b71c305322b04e006b24
---

```c
struct OH_Huks_Result {...}
```

## 概述

表示状态返回数据，包括返回码和消息。

**起始版本：** 9

**相关模块：** [HuksTypeApi](capi-hukstypeapi.md)

**所在头文件：** [native\_huks\_type.h](capi-native-huks-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32\_t errorCode | 状态返回码，参考[OH\_Huks\_ErrCode](capi-native-huks-type-h.md#oh_huks_errcode)。 |
| const char \*errorMsg | 对状态返回码的说明信息。 |
| uint8\_t \*data | 其他返回数据。 |
