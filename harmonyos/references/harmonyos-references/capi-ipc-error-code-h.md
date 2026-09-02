---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ipc-error-code-h
title: ipc_error_code.h
breadcrumb: API参考 > 应用框架 > IPC Kit（进程间通信服务） > C API > 头文件 > ipc_error_code.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:36+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:310e99f26fa16511c02a81f627525f22937472606fdfb9c6936bb026f5772a86
---

## 概述

提供IPC错误码定义，用于标识和处理IPC通信过程中可能发生的各类错误。开发者可根据返回的错误码快速定位问题原因，如参数错误、序列化失败、内存分配失败、远端对象死亡等场景，从而采取相应的错误处理措施。

**引用文件：** <IPCKit/ipc\_error\_code.h>

**库：** libipc\_capi.so

**系统能力：** SystemCapability.Communication.IPC.Core

**支持设备类型：** 不区分设备类型，可通过系统能力SystemCapability.Communication.IPC.Core判断功能是否可用。

**起始版本：** 12

**相关模块：** [OHIPCErrorCode](capi-ohipcerrorcode.md)

## 汇总

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_IPC\_ErrorCode](capi-ipc-error-code-h.md#oh_ipc_errorcode) | OH\_IPC\_ErrorCode | IPC错误码定义。 |

## 枚举类型说明

### OH\_IPC\_ErrorCode

```c
enum OH_IPC_ErrorCode
```

**描述：**

IPC错误码定义。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| OH\_IPC\_SUCCESS = 0 | 执行成功。 |
| OH\_IPC\_ERROR\_CODE\_BASE = 1901000 | 错误码区间起始值。 |
| OH\_IPC\_CHECK\_PARAM\_ERROR = OH\_IPC\_ERROR\_CODE\_BASE | 参数错误。当传入的参数为空指针、参数值超出有效范围或参数类型不匹配时返回此错误码。开发者应检查参数的有效性和合法性。 |
| OH\_IPC\_PARCEL\_WRITE\_ERROR = OH\_IPC\_ERROR\_CODE\_BASE + 1 | 序列化对象写入数据失败。当数据序列化时内存不足或数据格式不支持时可能发生此错误。开发者应检查数据大小和格式是否符合要求。 |
| OH\_IPC\_PARCEL\_READ\_ERROR = OH\_IPC\_ERROR\_CODE\_BASE + 2 | 序列化对象读取数据失败。当读取的数据长度超出实际数据长度或数据格式不匹配时可能发生此错误。开发者应检查数据读取顺序和数据格式是否正确。 |
| OH\_IPC\_MEM\_ALLOCATOR\_ERROR = OH\_IPC\_ERROR\_CODE\_BASE + 3 | 内存分配失败。当系统内存不足或内存分配器异常时返回此错误码。开发者应检查内存使用情况，释放不必要的资源后重试。 |
| OH\_IPC\_CODE\_OUT\_OF\_RANGE = OH\_IPC\_ERROR\_CODE\_BASE + 4 | 命令字超出定义范围[0x01,0x00FFFFFF]。当IPC通信使用的命令字不在有效范围内时返回此错误码。开发者应检查命令字定义是否符合规范要求。 |
| OH\_IPC\_DEAD\_REMOTE\_OBJECT = OH\_IPC\_ERROR\_CODE\_BASE + 5 | 远端对象死亡。当IPC通信的对端进程已退出或远端对象已被销毁时返回此错误码。开发者应重新建立连接或使用替代服务。 |
| OH\_IPC\_INVALID\_USER\_ERROR\_CODE = OH\_IPC\_ERROR\_CODE\_BASE + 6 | 用户自定义错误码超出范围[1909000, 1909999]。当开发者设置的自定义错误码不在允许范围内时返回此错误码。开发者应确保自定义错误码在有效范围内。 |
| OH\_IPC\_INNER\_ERROR = OH\_IPC\_ERROR\_CODE\_BASE + 7 | IPC内部错误。当IPC系统内部发生未知错误时返回此错误码。开发者可记录日志并联系技术支持或稍后重试。 |
| OH\_IPC\_ERROR\_CODE\_MAX = OH\_IPC\_ERROR\_CODE\_BASE + 1000 | 错误码区间最大值。 |
| OH\_IPC\_USER\_ERROR\_CODE\_MIN = 1909000 | 用户自定义错误码最小值。 |
| OH\_IPC\_USER\_ERROR\_CODE\_MAX = 1909999 | 用户自定义错误码最大值。 |
