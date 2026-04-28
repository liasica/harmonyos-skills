---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-graphic-error-code-h
title: graphic_error_code.h
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 头文件 > graphic_error_code.h
category: harmonyos-references
scraped_at: 2026-04-28T08:15:07+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:562f58f96c4427e22bbab247ddc720479dae2e76f8d5e788f18c2d93378d6bcb
---

## 概述

PhonePC/2in1TabletTVWearable

定义错误码。

**引用文件：** <native\_window/graphic\_error\_code.h>

**库：** libnative\_window.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 12

**相关模块：** [NativeWindow](capi-nativewindow.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OHNativeErrorCode](capi-graphic-error-code-h.md#ohnativeerrorcode) | OHNativeErrorCode | 接口错误码说明（仅用于查询）。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### OHNativeErrorCode

PhonePC/2in1TabletTVWearable

```
1. enum OHNativeErrorCode
```

**描述**

接口错误码说明（仅用于查询）。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| NATIVE\_ERROR\_OK = 0 | 成功。 |
| NATIVE\_ERROR\_MEM\_OPERATION\_ERROR = 30001000 | 内存操作错误。  **起始版本：** 15 |
| NATIVE\_ERROR\_INVALID\_ARGUMENTS = 40001000 | 入参无效。 |
| NATIVE\_ERROR\_NO\_PERMISSION = 40301000 | 无权限操作。 |
| NATIVE\_ERROR\_NO\_BUFFER = 40601000 | 无空闲可用的buffer。 |
| NATIVE\_ERROR\_NO\_CONSUMER = 41202000 | 消费端不存在。 |
| NATIVE\_ERROR\_NOT\_INIT = 41203000 | 未初始化。 |
| NATIVE\_ERROR\_CONSUMER\_CONNECTED = 41206000 | 消费端已经被连接。 |
| NATIVE\_ERROR\_BUFFER\_STATE\_INVALID = 41207000 | buffer状态不符合预期。 |
| NATIVE\_ERROR\_BUFFER\_IN\_CACHE = 41208000 | buffer已在缓存队列中。 |
| NATIVE\_ERROR\_BUFFER\_QUEUE\_FULL = 41209000 | 队列已满。 |
| NATIVE\_ERROR\_BUFFER\_NOT\_IN\_CACHE = 41210000 | buffer不在缓存队列中。 |
| NATIVE\_ERROR\_CONSUMER\_DISCONNECTED = 41211000 | 消费端已经被断开连接。 |
| NATIVE\_ERROR\_CONSUMER\_NO\_LISTENER\_REGISTERED = 41212000 | 消费端未注册listener回调函数。 |
| NATIVE\_ERROR\_UNSUPPORTED = 50102000 | 当前设备或平台不支持。 |
| NATIVE\_ERROR\_UNKNOWN = 50002000 | 未知错误，请查看日志。 |
| NATIVE\_ERROR\_HDI\_ERROR = 50007000 | HDI接口调用失败。 |
| NATIVE\_ERROR\_BINDER\_ERROR = 50401000 | 跨进程通信失败。 |
| NATIVE\_ERROR\_EGL\_STATE\_UNKNOWN = 60001000 | egl环境状态异常。 |
| NATIVE\_ERROR\_EGL\_API\_FAILED = 60002000 | egl接口调用失败。 |
