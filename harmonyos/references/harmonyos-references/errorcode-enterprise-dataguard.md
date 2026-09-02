---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-enterprise-dataguard
title: 企业数据保护服务错误码
breadcrumb: API参考 > 系统 > 安全 > Enterprise Data Guard Kit（企业数据保护服务） > ArkTS API > 企业数据保护服务错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:01:44+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:4a2c0cb00257354a7b862f2f062cf648aab029892768c974c57753de0710c143
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码详情请参见[通用错误码](errorcode-universal.md)说明文档。若您的问题仍无法解决，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1014400001 系统服务异常

**错误信息**

System service error.

**错误描述**

系统服务异常。

**可能原因**

系统处于非安全状态，或者硬件故障。

**处理步骤**

尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1014400006 用户取消了身份认证流程

**错误信息**

The user canceled the identity verification process.

**错误描述**

用户取消了身份认证流程。

**可能原因**

用户手动点击了取消。

**处理步骤**

业务重新发起认证流程。

## 1014400102 用户身份校验超时

**错误信息**

User identity authentication timed out.

**错误描述**

用户身份校验超时。

**可能原因**

用户身份认证超时未处理。

**处理步骤**

重新进行用户身份认证流程。

## 1014400103 身份校验失败

**错误信息**

Identity authentication failed.

**错误描述**

身份校验失败。

**可能原因**

用户的锁屏密码不正确。

**处理步骤**

请确认用户输入的锁屏密码是否正确。

## 1014400201 无效的设备类型

**错误信息**

Invalid device type. The current device is not an enterprise device.

**错误描述**

无效的设备类型。当前设备不是企业设备。

**可能原因**

当前设备不是企业设备。

**处理步骤**

请确认设备类型是否是企业设备，参考[MDM Kit开发指南](../harmonyos-guides/mdm-kit-guide.md)开发步骤。

## 1014400202 无效的userId

**错误信息**

Invalid userId.

**错误描述**

无效的userId。

**可能原因**

企业用户ID无效。

**处理步骤**

请确认企业用户ID是否有效。

## 1014400203 企业恢复密钥已存在

**错误信息**

The enterprise recovery key already exists.

**错误描述**

企业恢复密钥已存在。

**可能原因**

企业恢复密钥已经被获取过，无法再次获取。

**处理步骤**

先调用[getAuthChallenge](dataguard-recoverykey.md#recoverykeygetauthchallenge)接口获取挑战值并签名，再调用[deleteEnterpriseRecoveryKey](dataguard-recoverykey.md#recoverykeydeleteenterpriserecoverykey)删除企业恢复密钥。

## 1014400204 无效的签名

**错误信息**

Invalid signature.

**错误描述**

无效的签名。

**可能原因**

1. 使用同一个挑战值发起两次业务。
2. 接口请求超时。
3. 使用错误的企业私钥进行签名。

**处理步骤**

1. 调用[getAuthChallenge](dataguard-recoverykey.md#recoverykeygetauthchallenge)接口，重新获取挑战值并[签名](../harmonyos-guides/recoverykey-signature.md)。
2. 请确认企业私钥是否正确。

## 1014400205 无效的证书

**错误信息**

Invalid certificate.

**错误描述**

无效的证书。

**可能原因**

1. 证书格式不正确。
2. 证书携带的公钥格式错误。

**处理步骤**

1. 请检查证书格式是否符合PEM。
2. 请确认证书携带的公钥是否是ECC公钥。
3. 请确认证书已携带企业根证书的合法签名。

## 1001700001 系统服务异常

**错误信息**

System service error.

**错误描述**

系统服务异常。

**可能原因**

1. 系统IPC通信失败。
2. 系统参数获取/设置失败。

**处理步骤**

尝试重试操作或请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1001700101 无效用户ID

**错误信息**

Invalid userId.

**错误描述**

无效的userId。

**可能原因**

1. 未创建该用户。
2. 输入错误。

**处理步骤**

检查传入的用户ID，确认用户存在。

## 1001700103 路径无效

**错误信息**

Invalid path.

**错误描述**

路径无效。

**可能原因**

1. 需打标签的文件不存在。
2. 输入路径不在保护范围内。
3. 当前用户无权限访问。

**处理步骤**

请检查[默认路径范围](../harmonyos-guides/dataguard-introduction.md#访问限制)下对应的文件是否存在。

## 1001700104 标签列表检查失败

**错误信息**

Failed to check the tag list.

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

## 1001700105 无效的appId

**错误信息**

Invalid appId.

**错误描述**

无效的appId。

**可能原因**

appId校验失败。

**处理步骤**

确认输入的[appId](../harmonyos-guides/common-problem-of-application.md#什么是appid)和从bundleManager中获取的appId一致。

## 1001700106 无效的策略信息

**错误信息**

Invalid policy.

**错误描述**

无效的策略信息。

**可能原因**

1. 时长超过最大可配置数86400000ms。
2. 未下发对应的策略。

**处理步骤**

1. 确定policy中的时长未超限制。
2. 确定配置的policy策略已成功下发。

## 1001700201 HDC状态异常

**错误信息**

The HDC status is abnormal.

**错误描述**

HDC状态异常。

**可能原因**

1. HDC未使能。
2. 未打开USB调试功能。

**处理步骤**

打开USB调试功能，并启动HDC功能。

## 1001700202 保存私钥失败

**错误信息**

Failed to save the private key.

**错误描述**

保存私钥失败。

**可能原因**

1. 私钥解析失败。
2. 加密库调用失败。

**处理步骤**

1. 确认传入的私钥算法、格式正确。
2. 重启设备后重新调用。

## 1001700203 保存公钥失败

**错误信息**

Failed to save the public key.

**错误描述**

保存公钥失败。

**可能原因**

公钥解析失败。

**处理步骤**

确认传入的公钥算法、格式正确。

## 1001700204 密钥类型与设备类型不匹配

**错误信息**

The key type does not match the device type.

**错误描述**

密钥类型与设备类型不匹配。

**可能原因**

传入的密钥类型和设备类型无效。

**处理步骤**

修改类型组合方式，请避免使用无效的类型组合方式。
