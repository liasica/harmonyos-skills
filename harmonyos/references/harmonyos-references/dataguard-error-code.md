---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataguard-error-code
title: ArkTS API 错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:07:22+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e194947f1984802e46e2f78280b2b9ecd0946572a62ed98cdf96a60f480609ce
---

说明

以下仅介绍本模块特有错误码，详情请参见[通用错误码说明文档](errorcode-universal.md)。若您的问题仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1014400001 系统内部错误

PC/2in1

**错误信息**

System service exception.

**错误描述**

系统内部错误。

**可能原因**

系统处于非安全状态，或者硬件故障。

**处理步骤**

尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1014400103 用户认证失败

PC/2in1

**错误信息**

Authentication is failed.

**错误描述**

用户认证失败。

**可能原因**

用户的锁屏密码不正确。

**处理步骤**

请确认用户输入的锁屏密码是否正确。

## 1014400201 无效设备类型

PC/2in1

**错误信息**

Invalid device type, current device is not enterprise device.

**错误描述**

无效设备类型，当前设备不是企业设备。

**可能原因**

当前设备不是企业设备。

**处理步骤**

请确认设备类型是否是企业设备，参考[MDM Kit开发指南](../harmonyos-guides/mdm-kit-guide.md)开发步骤。

## 1014400202 无效userId

PC/2in1

**错误信息**

Invalid userId.

**错误描述**

无效userId。

**可能原因**

企业用户ID无效。

**处理步骤**

请确认企业用户ID是否有效。

## 1014400203 企业恢复密钥已存在

PC/2in1

**错误信息**

Enterprise recovery key is already existed.

**错误描述**

企业恢复密钥已存在。

**可能原因**

企业恢复密钥已经被获取过，无法再次获取。

**处理步骤**

先调用[getAuthChallenge](dataguard-recoverykey.md#getauthchallenge)接口获取挑战值并签名，再调用[deleteEnterpriseRecoveryKey](dataguard-recoverykey.md#deleteenterpriserecoverykey)删除企业恢复密钥。

## 1014400204 签名校验失败

PC/2in1

**错误信息**

Invalid signature.

**错误描述**

挑战值签名校验失败。

**可能原因**

1. 使用同一个挑战值发起两次业务。
2. 接口请求超时。
3. 使用错误的企业私钥进行签名。

**处理步骤**

1. 调用[getAuthChallenge](dataguard-recoverykey.md#getauthchallenge)接口，重新获取挑战值并[签名](../harmonyos-guides/recoverykey-signature.md)。
2. 请确认企业私钥是否正确。

## 1014400205 证书校验失败

PC/2in1

**错误信息**

Invalid cert.

**错误描述**

无效证书。

**可能原因**

1. 证书格式不正确。
2. 证书携带的公钥格式错误。

**处理步骤**

1. 请检查证书格式是否符合PEM。
2. 请确认证书携带的公钥是否是ECC公钥。
3. 请确认证书已携带企业根证书的合法签名。

## 1001700103 需打标签的文件不存在

PC/2in1

**错误信息**

The path is not exist.

**错误描述**

需打标签的文件不存在。

**可能原因**

需打标签的文件不存在。

**处理步骤**

请检查[默认路径范围](../harmonyos-guides/dataguard-introduction.md#访问限制)下对应的文件是否存在。

## 1001700104 标签列表检查失败

PC/2in1

**错误信息**

The tag list check failed.

**错误描述**

标签列表检查失败。

**可能原因**

1. 标签列表中标签内容存在分号";"。
2. 标签列表中单个标签字符长度超过255。
3. 标签数量超过5个。

**处理步骤**

1. 请检查标签列表中标签是否存在分号。
2. 请确认标签列表中标签字符长度是否超过255。
3. 请确认标签数量是否超过5个。
