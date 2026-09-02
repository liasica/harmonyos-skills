---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avscreen-capture-errors-h
title: native_avscreen_capture_errors.h
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 头文件 > native_avscreen_capture_errors.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:35+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c682f3dde1561219b6dabf9d1456f7b91cafb8eb841eece98e3670b11aefbc62
---

## 概述

声明屏幕录制接口调用的错误码，帮助开发者识别和处理屏幕录制中的各类异常情况，适用于屏幕录制故障排查和错误处理的开发场景。

**引用文件：** <multimedia/player\_framework/native\_avscreen\_capture\_errors.h>

**库：** libnative\_avscreen\_capture.so

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 10

**相关模块：** [AVScreenCapture](capi-avscreencapture.md)

## 汇总

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](capi-native-avscreen-capture-errors-h.md#oh_avscreen_capture_errcode) | OH\_AVSCREEN\_CAPTURE\_ErrCode | 屏幕录制过程中产生的不同结果码。 |

## 枚举类型说明

### OH\_AVSCREEN\_CAPTURE\_ErrCode

```c
enum OH_AVSCREEN_CAPTURE_ErrCode
```

**描述**

屏幕录制过程中产生的不同结果码。

开发者可在屏幕录制应用、在线会议屏幕共享、远程协助等场景中，根据返回的错误码判断接口调用的异常原因并进行相应的错误处理。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| AV\_SCREEN\_CAPTURE\_ERR\_BASE = 0 | 错误码的基础值，其他错误码在此基础上递增，用于标识不同的错误类型。 |
| AV\_SCREEN\_CAPTURE\_ERR\_OK = AV\_SCREEN\_CAPTURE\_ERR\_BASE | 操作成功。 |
| AV\_SCREEN\_CAPTURE\_ERR\_NO\_MEMORY = AV\_SCREEN\_CAPTURE\_ERR\_BASE + 1 | 内存不足。  可能原因：系统可用内存不足。  解决措施：请检查录制参数或系统内存状况。 |
| AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT = AV\_SCREEN\_CAPTURE\_ERR\_BASE + 2 | 不允许操作。  可能原因：当前操作未获得必要权限或处于非法状态。  解决措施：请检查操作权限和当前状态后重试。 |
| AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL = AV\_SCREEN\_CAPTURE\_ERR\_BASE + 3 | 无效参数。  可能原因：传入的参数不符合接口要求或取值范围不正确。  解决措施：请检查参数类型和取值范围后重试。 |
| AV\_SCREEN\_CAPTURE\_ERR\_IO = AV\_SCREEN\_CAPTURE\_ERR\_BASE + 4 | 输入输出流异常。  可能原因：文件读写失败或数据传输错误。  解决措施：请检查文件路径、权限和存储空间后重试。 |
| AV\_SCREEN\_CAPTURE\_ERR\_TIMEOUT = AV\_SCREEN\_CAPTURE\_ERR\_BASE + 5 | 网络超时。  可能原因：网络连接不稳定或服务器响应超时。  解决措施：请检查网络连接状态后重试。 |
| AV\_SCREEN\_CAPTURE\_ERR\_UNKNOWN = AV\_SCREEN\_CAPTURE\_ERR\_BASE + 6 | 未知错误。  可能原因：发生了未预期的异常情况。  解决措施：请检查日志信息。 |
| AV\_SCREEN\_CAPTURE\_ERR\_SERVICE\_DIED = AV\_SCREEN\_CAPTURE\_ERR\_BASE + 7 | 媒体服务已终止。  可能原因：媒体服务进程崩溃或被系统终止。  解决措施：请检查系统资源或重启服务。 |
| AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_STATE = AV\_SCREEN\_CAPTURE\_ERR\_BASE + 8 | 当前状态不支持此操作。  可能原因：调用接口时实例处于错误状态。  解决措施：请检查当前状态并按正确流程调用接口。 |
| AV\_SCREEN\_CAPTURE\_ERR\_UNSUPPORT = AV\_SCREEN\_CAPTURE\_ERR\_BASE + 9 | 不支持的接口。  可能原因：当前版本不支持此接口或功能。  解决措施：请检查API版本或设备兼容性。 |
| AV\_SCREEN\_CAPTURE\_ERR\_EXTEND\_START = AV\_SCREEN\_CAPTURE\_ERR\_BASE + 100 | 预期之外的错误。  可能原因：发生了扩展的错误情况。  解决措施：请查看详细错误信息。 |
