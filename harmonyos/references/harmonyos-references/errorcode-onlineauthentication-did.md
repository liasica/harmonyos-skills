---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-onlineauthentication-did
title: DID数字身份服务
breadcrumb: API参考 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > ArkTS API > ArkTS API错误码 > DID数字身份服务
category: harmonyos-references
scraped_at: 2026-09-02T15:01:44+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:29741d247e554a2c720f74420732c5fb5cebd191213ca1a42b379b857b3aae7d
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参见[通用错误码](errorcode-universal.md)。

## 1024600001 参数错误

**错误信息**

Invalid parameters.

**错误描述**

参数错误时，系统会产生此错误码。

**可能原因**

1. 输入参数为空或格式不正确。
2. 参数类型不匹配。
3. 必填参数缺失。

**处理步骤**

1. 检查输入参数是否正确。
2. 确认参数类型是否符合接口要求。
3. 确保必填参数已正确填写。

## 1024600002 生物特征未录入或认证模块异常

**错误信息**

The user does not record biometric features or the authentication module is abnormal.

**错误描述**

用户未录入生物特征或认证模块异常时，系统会产生此错误码。

**可能原因**

1. 用户未录入指纹、人脸等生物特征。
2. 生物特征认证模块出现异常。
3. 生物特征识别服务不可用。

**处理步骤**

1. 引导用户录入生物特征。
2. 重启设备后重试。

## 1024600003 用户取消操作

**错误信息**

The user canceled the operation.

**错误描述**

用户主动取消操作时，系统会产生此错误码。

**可能原因**

1. 用户在认证过程中点击取消。
2. 用户在生物特征识别时取消操作。
3. 操作超时导致自动取消。

**处理步骤**

1. 无需特殊处理，此为用户主动行为。
2. 如需重试，可提示用户重新操作。

## 1024600004 密钥别名已使用

**错误信息**

The key alias has been used.

**错误描述**

密钥别名已被使用时，系统会产生此错误码。

**可能原因**

1. 该密钥别名已被其他密钥使用。
2. 重复使用相同的密钥别名。

**处理步骤**

1. 使用不同的密钥别名。
2. 先删除已存在的密钥，再使用该别名。

## 1024600005 密钥无效

**错误信息**

The key is invalid.

**错误描述**

密钥无效时，系统会产生此错误码。

**可能原因**

1. 密钥已过期。
2. 密钥格式不正确。
3. 密钥已被损坏或篡改。

**处理步骤**

1. 检查密钥是否有效。
2. 重新生成或导入有效的密钥。
3. 确认密钥格式是否符合要求。

## 1024600006 认证器安全级别不足

**错误信息**

The security level of the authenticator on the device is lower than ATL4.

**错误描述**

设备上的认证器安全级别低于ATL4时，系统会产生此错误码。

**可能原因**

1. 设备的生物特征认证器安全级别不足。
2. 设备硬件不支持高级别安全认证。

**处理步骤**

1. 使用支持高级别安全认证的设备。
2. 使用其他符合安全级别要求的认证方式。

## 1024600007 未知错误

**错误信息**

Unknown error.

**错误描述**

发生未知错误时，系统会产生此错误码。

**可能原因**

1. 系统内部错误。
2. 未预期的异常情况。

**处理步骤**

1. 重启设备后重试。

## 1024600008 DID不存在

**错误信息**

The DID does not exist.

**错误描述**

DID不存在时，系统会产生此错误码。

**可能原因**

1. 指定的DID未创建或已删除。
2. DID标识符输入错误。

**处理步骤**

1. 确认DID是否存在。
2. 检查DID标识符是否正确。
3. 如需使用，先[创建或导入DID](../harmonyos-guides/onlineauthentication-did.md#启用数字身份)。

## 1024600009 凭证解密失败

**错误信息**

Failed to decrypt the credential.

**错误描述**

凭证解密失败时，系统会产生此错误码。

**可能原因**

1. 解密密钥不正确。
2. 凭证数据已损坏。
3. 加密算法不匹配。

**处理步骤**

1. 检查解密密钥是否正确。
2. 确认凭证数据完整性。
3. 使用正确的加密算法。

## 1024600010 凭证不存在

**错误信息**

The credential does not exist.

**错误描述**

凭证不存在时，系统会产生此错误码。

**可能原因**

1. 指定的凭证未导入或已删除。
2. 凭证ID输入错误。

**处理步骤**

1. 确认凭证是否存在。
2. 检查凭证ID是否正确。
3. 如需使用，请先[创建或导入DID](../harmonyos-guides/onlineauthentication-did.md#启用数字身份)。

## 1024600011 无权限执行操作

**错误信息**

The application does not have permission to perform this operation.

**错误描述**

应用非DID或凭证属主，无权限执行操作时，系统会产生此错误码。

**可能原因**

1. 应用试图访问不归属于应用的DID或凭证。

**处理步骤**

1. 确认应用为指定的DID或凭证的属主。

## 1024600012 DID密钥数量达到上限

**错误信息**

The number of did keys has reached the maximum limit.

**错误描述**

DID密钥数量达到上限（500个）时，系统会产生此错误码。

**可能原因**

1. 设备上存储的DID密钥数量超过限制。
2. 尝试创建新的DID密钥时已达上限。

**处理步骤**

1. 删除不需要的DID密钥。
2. 使用已有的DID密钥。

## 1024600013 DID数量达到上限

**错误信息**

The number of DIDs has reached the maximum limit.

**错误描述**

DID数量达到上限（50个）时，系统会产生此错误码。

**可能原因**

1. 设备上存储的DID数量超过限制。
2. 尝试创建新的DID时已达上限。

**处理步骤**

1. 删除不需要的DID。
2. 使用已有的DID。

## 1024600014 凭证数量达到上限

**错误信息**

The number of credentials has reached the maximum limit.

**错误描述**

凭证数量达到上限（1000个）时，系统会产生此错误码。

**可能原因**

1. 设备上存储的凭证数量超过限制。
2. 尝试导入新的凭证时已达上限。

**处理步骤**

1. 删除不需要的凭证。
2. 使用已有的凭证。
