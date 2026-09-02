---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-huks
title: HUKS错误码
breadcrumb: API参考 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 错误码 > HUKS错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:01:48+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d51c72957e0d63b51825d2f368c8194f325f06704f747717fc1a343a25a04160
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 12000001 该子功能不支持（特性）

**错误信息**

The feature or capability is not supported.

**错误描述**

当前调用的特性（功能）不支持使用，具体特性（功能）可通过打印的errorMessage获取。

**可能原因**

1. 不支持使用的子特性。
2. 不支持使用的算法参数。

**处理步骤**

1. 查看errorMessage确认不支持的子特性，请避免在当前设备环境中调用该特性；如确属业务必要，请前往官方开发者社区提交反馈。
2. 参考[HUKS开发指南](../harmonyos-guides/huks-overview.md)中各能力介绍及算法规格的具体章节，确认调用接口规格，调整API参数，使用支持的算法参数。

## 12000002 缺少密钥算法参数

**错误信息**

The algorithm param is missing.

**错误描述**

缺少密钥操作必要的算法参数。

**可能原因**

未添加当前密钥操作必要的参数，例如密钥算法、密钥长度、填充算法等。

**处理步骤**

1. 查看errorMessage确认缺失的密钥参数。
2. 参考[HUKS开发指南](../harmonyos-guides/huks-overview.md)中各能力介绍及算法规格的具体章节，确认调用接口规格，调整API参数，添加对应的密钥参数。

## 12000003 无效的密钥算法参数

**错误信息**

The algorithm argument is invalid.

**错误描述**

无效的密钥算法参数。

**可能原因**

使用密钥时相关参数无效，例如算法和填充算法不匹配，算法和密钥操作不匹配等。

**处理步骤**

1. 查看errorMessage确认无效的密钥参数名。
2. 参考[HUKS开发指南](../harmonyos-guides/huks-overview.md)中各能力介绍及算法规格的具体章节，确认调用接口规格，调整API参数，修改对应的密钥参数为合法值。

## 12000004 文件错误

**错误信息**

The file operation failed.

**错误描述**

操作文件失败。

**可能原因**

1. 磁盘空间已满。
2. 获取文件大小失败。
3. 文件无法操作，具体原因可参考返回的errorMessage。

**处理步骤**

1. 若磁盘空间已经写满，请先清理磁盘。
2. 确认对应文件的操作权限，请查看[文件目录说明](../harmonyos-guides/app-sandbox-directory.md#应用文件目录与应用文件路径)。
3. 若文件系统存在其他异常，请前往官方开发者社区提交反馈。

## 12000005 进程通信错误

**错误信息**

IPC communication failed.

**错误描述**

IPC通信失败。

**可能原因**

1. 无法从IPC获取消息。
2. IPC出错，具体原因可参考返回的errorMessage。

**处理步骤**

查看错误信息，排查是否进程IPC通信问题。

## 12000006 算法库操作失败

**错误信息**

Crypto engine error or UKey driver error.

**错误描述**

算法库操作失败或者UKey驱动失败。

**可能原因**

该错误码表示算法库操作失败或者UKey驱动失败，可能原因如下。

1. 算法库加解密错误，可能是密文数据不对。
2. 密钥参数不正确。

**处理步骤**

1. 排查密文数据是否正确。
2. 排查加解密参数是否正确。

## 12000007 密钥访问失败-密钥已失效

**错误信息**

This credential is invalidated permanently.

**错误描述**

当前凭据已永久失效。

**可能原因**

该错误码表示密钥访问失败 - 密钥已失效，可能原因如下。

1. 该密钥设置了清除密码失效的用户认证访问控制属性，清除过设备密钥导致密钥失效。
2. 该密钥设置了新录入生物特征失效的用户认证访问控制属性，由于录入过新的指纹或人脸导致该密钥失败。

**处理步骤**

1. 确认日志中记录的认证失败方式。
2. 如果使用了正确参数，但是失效控制导致认证不通过，则该密钥已经无法使用。

## 12000008 密钥访问失败-密钥认证失败

**错误信息**

The authentication token verification failed.

**错误描述**

用户令牌无法通过认证。

**可能原因**

该密钥设置了用户认证访问控制属性，由于challenge参数不正确导致无法通过认证。

**处理步骤**

1. 检查userIAM认证的challenge参数组装是否正确。
2. 如果是challenge参数不正确导致，则修改正确的组装方式，使用huks生成challenge组装，并传入userIAM重新认证。

## 12000009 密钥访问失败-密钥访问超时

**错误信息**

This authentication token timed out.

**错误描述**

当前用户令牌已超时。

**可能原因**

该密钥设置了用户认证访问控制属性，并指定了认证超时时间（timeout）。由于密钥init操作后未在timeout时间窗内完成用户认证，认证令牌超时失效，导致当前密钥会话失效。

**处理步骤**

如果是timeout导致不正确，则重新触发密钥init并重新认证，使得认证时间和密钥init时间小于设置的timeout时间。

## 12000010 密钥操作会话数已达上限

**错误信息**

The number of key operation sessions has reached the limit.

**错误描述**

密钥操作会话数已达上限。

**可能原因**

HUKS密钥操作会话数已达上限（15个），无法处理更多同应用或跨应用的调用请求。

**处理步骤**

1. 检查同应用内部是否同时存在多个密钥会话操作（init），存在则修改避免同时调用。
2. 如不存在上述情形，则可能是其它应用同时调用多个会话，通过等待其它应用释放会话后再使用。

## 12000011 目标对象不存在

**错误信息**

Queried entity does not exist.

**错误描述**

目标对象不存在。

**可能原因**

该别名对应的密钥不存在。

**处理步骤**

1. 检查密钥别名是否拼写错误。
2. 检查密钥别名对应的密钥是否生成成功。

## 12000012 外部错误

**错误信息**

Device environment or input parameter abnormal.

**错误描述**

设备环境或输入参数异常。

**可能原因**

1. 设备无证书、证书过期会导致需要使用证书的相关业务失败，例如在线匿名密钥证明、分布式密钥服务。
2. 在线匿名密钥证明需要设备证书服务[Device Certificate Kit](../harmonyos-guides/device-certificate-kit.md)与云端交互获取证书链，需要网络畅通。未联网、网络不稳定、网络超时等场景会导致在线匿名密钥证明失败。
3. 匿名密钥证明涉及用户隐私，用户首次启用新设备时未同意OOBE(首次开机向导)中的隐私声明协议。
4. 在线匿名密钥证明采用的是异步逻辑，有固定时间限制，设备证书服务[Device Certificate Kit](../harmonyos-guides/device-certificate-kit.md)服务端与客户端连接超时会导致在线匿名密钥证明失败。
5. 设备首次启动时注册各种Ability（例如生成、导入、导出、删除密钥、加密、解密、签名、验签、派生、哈希、MAC等）失败。
6. 其它系统内部错误（IPC发送数据失败、NAPI层错误等）。

**处理步骤**

1. 检查设备证书有效性：可调用[Device Certificate Kit](../harmonyos-guides/device-certificate-kit.md)提供的[证书查询接口](device-certificate-api.md)，确认证书是否存在及是否在有效期内；若证书缺失或已过期，请参考[Device Certificate Kit](../harmonyos-guides/device-certificate-kit.md)文档处理。
2. 保证网络正常。
3. 同意OOBE(首次开机向导)中的隐私声明协议。
4. 可尝试重新调用在线匿名密钥证明接口，若问题持续，请参考[Device Certificate Kit](../harmonyos-guides/device-certificate-kit.md)文档排查故障原因。
5. 系统崩溃会导致Ability注册失败。可在DevEco Studio中打开 FaultLog，查看是否存在系统崩溃记录进一步分析。可尝试重启设备查看故障是否恢复。
6. 在日志中搜索huks具体定位系统层面的其它错误。

## 12000013 密钥设置生物访问控制时，待绑定的凭据不存在

**错误信息**

The credential does not exist.

**错误描述**

当前凭据不存在。

**可能原因**

密钥绑定PIN、指纹、人脸时，未录入相关凭据。

**处理步骤**

录入相关凭据，或更改绑定凭据类型。

## 12000014 内存不足

**错误信息**

可能为以下的其中一种：

* Insufficient memory.
* Malloc failed.

**错误描述**

可能为以下的其中一种：

* 内存不足。
* 内存分配失败。

**可能原因**

系统内存不足，或出参缓存太小。

**处理步骤**

1. 开发者释放部分内存或重启。
2. 检查传入的出参缓存大小。

## 12000015 调用其他系统服务失败

**错误信息**

Failed to obtain the information via UserIAM.

**错误描述**

无法通过UserIAM获取认证相关信息。

**可能原因**

其他系统服务未启动。

**处理步骤**

开发者等待一段时间后尝试再次触发调用。

## 12000016 设备密码未设置

**错误信息**

A device password is required but not set.

**错误描述**

设备密码未设置。

**可能原因**

该密钥配置了依赖设备密码的用户访问认证属性，但设备密码未配置，导致无法操作。

**处理步骤**

先设置设备密码，再进行密钥操作。

## 12000017 同名密钥已存在

**错误信息**

The key with the same alias already exists.

**错误描述**

同名密钥已存在。

**可能原因**

指定了不覆写同名密钥，但同名密钥已存在。

**处理步骤**

请根据业务需要检查是否应该覆写同名密钥。

## 12000018 输入参数非法

**错误信息**

The input parameter is invalid.

**错误描述**

当前输入的参数无效。

**可能原因**

1. 必选参数没有传入。
2. 参数类型错误（Type Error）。
3. 空参数错误（Null Argument Error）。
4. 参数值范围错误（Value Range Error）。

**处理步骤**

请检查必选参数是否传入，或者传入的参数类型是否错误。对于参数校验失败原因，请阅读参数规格约束，按照可能原因进行排查。

## 12000019 同名provider已注册

**错误信息**

The provider is already registered.

**错误描述**

注册的provider已存在。

**可能原因**

重复注册同名provider，或之前注册的provider未注销。

**处理步骤**

检查注册的provider是否正确，如果确定没问题，则需要先注销，再注册。

## 12000020 依赖的模块报错

**错误信息**

The provider operation failed.

**错误描述**

下游依赖的模块报错。

**可能原因**

下游依赖的模块报错。

**处理步骤**

根据下游返回的error code或者error message查看下游模块具体报错的原因。

## 12000021 UKey PIN码被锁定

**错误信息**

The UKey PIN is locked.

**错误描述**

UKey PIN码被锁定。

**可能原因**

PIN码输入错误次数过多导致被锁定。

**处理步骤**

咨询相关银行，解锁UKey。

## 12000022 UKey PIN码错误

**错误信息**

The UKey PIN is incorrect.

**错误描述**

UKey PIN码错误。

**可能原因**

PIN码输入错误。

**处理步骤**

输入正确PIN码。

## 12000023 UKey PIN码未认证

**错误信息**

The UKey PIN is not authenticated.

**错误描述**

UKey PIN码未认证。

**可能原因**

执行操作需要进行PIN码认证，但实际PIN码尚未认证。

**处理步骤**

先完成UKey PIN码认证，再执行需要认证的操作。

## 12000024 设备或资源繁忙

**错误信息**

The provider or UKey is busy.

**错误描述**

设备或资源繁忙。

**可能原因**

设备或资源繁忙。

**处理步骤**

再次重试或者插拔UKey后重试。

## 12000025 资源超过限制

**错误信息**

The resource exceeds the limit.

**错误描述**

资源超过限制。

**可能原因**

资源超过限制。

**处理步骤**

检查是否有未释放资源，释放已有资源后重试。

## 12000026 安全元件故障

**错误信息**

the secure element is not available.

**错误描述**

安全元件故障。

**可能原因**

安全元件故障。

**处理步骤**

1. 稍等片刻后重试，或重启设备后重试。
2. 如以上操作均无法解决故障，将错误码与日志提交到社区进行反馈。

## 12000027 网络不可用

**错误信息**

The Internet is unavailable.

**错误描述**

网络不可用。

**可能原因**

设备网络连接不可用。

**处理步骤**

1. 检查设备网络连接是否正常。
2. 恢复网络连接后重试。

## HUKS调用失败返回401

错误码401是[通用错误码](errorcode-universal.md)，标识参数检查失败。

使用HUKS时出现401错误码，可能由以下情况导致：

### 数据长度不满足要求

**可能原因**

1. 对称加密算法的数据长度不正确。
2. 非对称加密算法的数据长度不正确。
3. 签名算法的数据长度不正确。

**解决措施**

1. 确保对称加密算法数据长度满足要求：加密算法AES/ECB/NoPadding、AES/CBC/NoPadding要求明文长度是16字节的整数倍，AES/GCM要求[HUKS\_TAG\_AE\_TAG](js-apis-huks.md#hukstag)长度为16字节，AES/CCM要求NONCE长度是7~13字节，[HUKS\_TAG\_AE\_TAG\_LEN](js-apis-huks.md#hukstag)长度要求4~16且为2的整数倍字节。
2. 确保非对称加密算法数据长度满足要求：加密算法RSA/ECB/NoPadding要求明文长度等于密钥长度，RSA/ECB/PKCS1v1.5要求明文长度小于等于密钥长度-11字节，RSA/ECB/OAEP要求明文长度小于等于密钥长度-2\*摘要长度-2。
3. 确保签名算法数据长度满足要求：签名算法RSA/NoPadding/NoDigest要求消息长度等于密钥长度。

### 密钥长度、格式不符合要求

**可能原因**

明文导入或者加密导入的密钥长度不正确或者格式不正确。

**解决措施**

导入密钥的格式需要符合HUKS规范，查看[开发指导](../harmonyos-guides/huks-key-import-overview.md)。

### 传入参数不一致

**可能原因**

前后传入的参数不一致，例如算法、分组模式、摘要、密钥长度等常用参数。

例如生成密钥时传入算法参数为AES，加密时传入的算法参数是RSA。

**解决措施**

检查前后传入的参数是否不一致。

### 传入参数重复

**可能原因**

HuksOption中的paramset传入重复的参数。

**解决措施**

检查是否传入重复的参数。

### 二次访问控制设置失败

**可能原因**

1. 二次访问控制操作中获取认证类型、挑战值类型、访问类型、认证token失败或者认证类型无效、挑战值类型无效、访问类型无效、认证token无效。
2. 二次访问控制设置[HUKS\_TAG\_AUTH\_TIMEOUT](js-apis-huks.md#hukstag)值过大。

**解决措施**

1. 根据开发指导检查二次访问控制的各种参数类型是否正确。
2. 二次访问控制的[HUKS\_TAG\_AUTH\_TIMEOUT](js-apis-huks.md#hukstag)参数有最大限制6小时，超过这个限制会报错。

### 安全签名类型传入无效值

**可能原因**

安全签名类型[HUKS\_TAG\_KEY\_SECURE\_SIGN\_TYPE](js-apis-huks.md#hukstag)传入无效的值。

**解决措施**

安全签名类型[HUKS\_TAG\_KEY\_SECURE\_SIGN\_TYPE](js-apis-huks.md#hukstag)只支持[HUKS\_SECURE\_SIGN\_WITH\_AUTHINFO](js-apis-huks.md#hukstag)，其它均为无效类型。
