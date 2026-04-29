---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hukstypeapi-oh-huks-result
title: OH_Huks_Result
breadcrumb: API参考 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > C API > 结构体 > OH_Huks_Result
category: harmonyos-references
scraped_at: 2026-04-29T13:58:18+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:fd427fc9b60843b477834073469a5fd97690ecb85229d83202b5b73f642d1fa9
---

```
1. struct OH_Huks_Result {...}
```

## 概述

PhonePC/2in1TabletTVWearable

表示状态返回数据，包括返回码和消息。

**起始版本：** 9

**相关模块：** [HuksTypeApi](capi-hukstypeapi.md)

**所在头文件：** [native\_huks\_type.h](capi-native-huks-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int32\_t errorCode | 状态返回码，参考[OH\_Huks\_ErrCode](capi-native-huks-type-h.md#oh_huks_errcode)。 |
| const char \*errorMsg | 对状态返回码的说明信息。 |
| uint8\_t \*data | 其他返回数据。 |
