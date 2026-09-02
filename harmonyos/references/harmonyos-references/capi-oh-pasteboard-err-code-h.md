---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-pasteboard-err-code-h
title: oh_pasteboard_err_code.h
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 头文件 > oh_pasteboard_err_code.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:05+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d073b9361a40a388d63aee57829bb68b54f981afa4a3ca5c78d1900013e7fc7d
---

## 概述

声明剪贴板框架错误码信息。剪贴板错误码用于标识剪贴板操作过程中的执行结果，开发者可通过错误码判断操作是否成功以及失败的具体原因。

**引用文件：** <database/pasteboard/oh\_pasteboard\_err\_code.h>

**库：** libpasteboard.so

**系统能力：** SystemCapability.MiscServices.Pasteboard

**起始版本：** 13

**相关模块：** [Pasteboard](capi-pasteboard.md)

## 汇总

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [PASTEBOARD\_ErrCode](capi-oh-pasteboard-err-code-h.md#pasteboard_errcode) | PASTEBOARD\_ErrCode | 错误码信息。 |

## 枚举类型说明

### PASTEBOARD\_ErrCode

```c
enum PASTEBOARD_ErrCode
```

**描述：**

剪贴板错误码枚举，用于标识剪贴板操作的执行结果，开发者可通过错误码判断操作是否成功以及失败的具体原因。

**起始版本：** 13

| 枚举项 | 描述 | 说明 |
| --- | --- | --- |
| ERR\_OK = 0 | 执行成功。 | - |
| ERR\_PERMISSION\_ERROR = 201 | 权限校验失败。 | 权限校验失败，请检查应用是否申请了相应权限或权限配置是否正确。 |
| ERR\_INVALID\_PARAMETER = 401 | 非法参数。 | 参数不合法，请检查参数类型、取值范围或参数是否为空。 |
| ERR\_DEVICE\_NOT\_SUPPORTED = 801 | 设备能力不支持。 | 当前设备不支持该功能，请检查设备是否具备相应能力。 |
| ERR\_INNER\_ERROR = 12900000 | 内部错误。 | 系统内部错误，请稍后重试或联系技术支持。 |
| ERR\_BUSY = 12900003 | 系统忙。 | 系统繁忙，请等待一段时间后重试。 |
| ERR\_PASTEBOARD\_COPY\_FILE\_ERROR = 12900007 | 文件拷贝失败。  起始版本：15 | 文件拷贝失败，请检查文件是否存在、存储空间是否充足或是否有访问权限。 |
| ERR\_PASTEBOARD\_PROGRESS\_START\_ERROR = 12900008 | 拉起进度显示失败。  起始版本：15 | 进度显示启动失败，请检查系统状态或稍后重试。 |
| ERR\_PASTEBOARD\_PROGRESS\_ABNORMAL = 12900009 | 进度显示异常。  起始版本：15 | 进度显示异常，请检查系统状态或重新尝试操作。 |
| ERR\_PASTEBOARD\_GET\_DATA\_FAILED = 12900010 | 获取剪贴板数据失败。  起始版本：15 | 获取剪贴板数据失败，请检查剪贴板是否有数据或权限是否正确。 |
