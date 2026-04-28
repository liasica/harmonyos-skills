---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-dlp
title: DLP服务错误码
breadcrumb: API参考 > 系统 > 安全 > Data Protection Kit（数据保护服务） > 错误码 > DLP服务错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:07:11+08:00
doc_updated_at: 2026-03-23
content_hash: sha256:92a19f5bf51664289f570479c7229a627971cee85299c20463b138f0b79a4c17
---

说明

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 19100001 入参错误

PhonePC/2in1TabletTV

**错误信息**

Invalid parameter value.

**错误描述**

非法参数。

**可能原因**

1. 账号长度为空或长度大于1024。
2. 账号类型错误。
3. aesKey或iv非法。
4. 系统时间晚于授权到期时间。
5. Fd小于0。
6. tokenId等于0。
7. 包名为空。
8. appIndex小于0。
9. userId小于0。

**处理步骤**

请传入正确的参数。

## 19100002 加解密出错

PhonePC/2in1TabletTV

**错误信息**

Credential service busy due to too many tasks or duplicate tasks.

**错误描述**

启动加解密出错。

**可能原因**

1. 当前运行的加解密任务数大于100。
2. 加解密任务重复。

**处理步骤**

请等待一段时间后重试。

## 19100003 加解密超时

PhonePC/2in1TabletTV

**错误信息**

Credential task time out.

**错误描述**

加解密超时。

**可能原因**

DLP文件加解密时间超过10秒。

**处理步骤**

请等待一段时间后重试。

## 19100004 凭据服务错误

PhonePC/2in1TabletTV

**错误信息**

Credential service error.

**错误描述**

凭据服务错误。

**可能原因**

1. DLP凭据服务不存在。
2. DLP凭据服务异常。

**处理步骤**

请等待一段时间后重试，或者重启设备。

## 19100005 凭据认证服务器错误

PhonePC/2in1TabletTV

**错误信息**

Credential authentication server error.

**错误描述**

凭据认证服务器错误。

**可能原因**

1. 凭据认证服务器无法连接。
2. 凭据认证服务器不存在。

**处理步骤**

请检查凭据认证服务器后重试。

## 19100006 非DLP沙箱应用

PhonePC/2in1TabletTV

**错误信息**

No permission to call this API, which is available only for DLP sandbox applications.

**错误描述**

调用方不是DLP沙箱应用。

**可能原因**

调用方不是DLP沙箱应用。

**处理步骤**

请确认调用场景后重试。

## 19100007 DLP沙箱应用不允许调用此接口

PhonePC/2in1TabletTV

**错误信息**

No permission to call this API, which is available only for non-DLP sandbox applications.

**错误描述**

调用方不可以是DLP沙箱应用。

**可能原因**

调用方是DLP沙箱应用。

**处理步骤**

请确认调用场景后重试。

## 19100008 非DLP文件

PhonePC/2in1TabletTV

**错误信息**

The file is not a DLP file.

**错误描述**

文件不是DLP文件。

**可能原因**

操作非DLP文件格式文件。

**处理步骤**

请使用经过DLP加密的DLP文件。

## 19100009 操作DLP文件失败

PhonePC/2in1TabletTV

**错误信息**

Failed to operate the DLP file.

**错误描述**

操作DLP文件失败。

**可能原因**

1. 当前用户不在授权范围内。
2. 安装沙箱应用失败。
3. 关联link文件失败。
4. 打开DLP文件数大于1000。

**处理步骤**

1. 请确认访问权限。
2. 请等待一段时间或重启后重试。

## 19100011 系统服务工作异常

PhonePC/2in1TabletTV

**错误信息**

The system ability works abnormally.

**错误描述**

系统服务工作异常。

**可能原因**

1. DLP权限服务无法正常启动。
2. DLP权限服务的RPC对象无法获取。
3. DLP权限服务依赖的其他服务无法正常启动。
4. IPC数据读取写入失败。
5. 服务未初始化。

**处理步骤**

系统服务内部工作异常，请稍后重试，或者重启设备尝试。

## 19100012 内存申请失败

**错误信息**

System memory is insufficient.

**错误描述**

内存申请失败。

**可能原因**

系统内存不足。

**处理步骤**

系统内存不足，请稍后重试，或者重启设备。

## 19100013 用户无权限

PhonePC/2in1TabletTV

**错误信息**

The user does not have the permission.

**错误描述**

用户无权限。

**可能原因**

当前登录账号无此文件的权限。

**处理步骤**

请检查权限。

## 19100014 账号未登录

PhonePC/2in1TabletTV

**错误信息**

Account not logged in.

**错误描述**

账号未登录。

**可能原因**

对应类型账号未登录。

**处理步骤**

请登录账号。

## 19100016 want参数中没有uri

PhonePC/2in1TabletTV

**错误信息**

The uri field is missing in the want parameter.

**错误描述**

want参数中没有uri。

**可能原因**

want参数中没有uri。

**处理步骤**

请传入正确的参数。

## 19100017 want参数中parameters内没有displayName

PhonePC/2in1TabletTV

**错误信息**

The displayName field is missing in the want parameter.

**错误描述**

want参数中parameters内没有displayName。

**可能原因**

want参数中parameters内没有displayName。

**处理步骤**

请传入正确的参数。

## 19100018 应用未授权

PhonePC/2in1TabletTV

**错误信息**

The application is not authorized.

**错误描述**

应用未授权。

**可能原因**

应用不在授信应用名单中。

**处理步骤**

接入授信应用名单。请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)方式获取技术支持。

## 19100021 设置企业应用策略失败

PhonePC/2in1TabletTV

**错误信息**

Failed to set the enterprise policy.

**错误描述**

设置企业应用策略失败。

**可能原因**

输入策略格式异常。

**处理步骤**

请检查策略格式，并进行重试。

## 19110001 参数错误

PhonePC/2in1TabletTV

**错误信息**

Parameter error.

**错误描述**

参数错误。

**可能原因**

1. 策略格式错误。
2. 参数范围错误。

**处理步骤**

请传入正确的参数。

## 19110002 文件敏感信息识别超时

PhonePC/2in1TabletTV

**错误信息**

Sensitive file content identification timed out.

**错误描述**

文件敏感信息识别超时。

**可能原因**

文件敏感信息识别超时。

**处理步骤**

请等待一段时间后重试。

## 19110003 文件不支持

PhonePC/2in1TabletTV

**错误信息**

The file is not supported.

**错误描述**

文件不支持。

**可能原因**

1. 文件路径不存在。
2. 文件类型不支持。
3. 文件权限不支持。

**处理步骤**

请确认传入的文件是否正确。

## 19110004 系统功能运行异常

PhonePC/2in1TabletTV

**错误信息**

A system error has occurred.

**错误描述**

系统功能运行异常。

**可能原因**

1. 服务无法正常启动。
2. 服务依赖的服务无法正常启动。
3. IPC数据读写失败。
4. 服务未初始化。

**处理步骤**

系统服务内部工作异常，请稍后重试，或者重启设备尝试。
