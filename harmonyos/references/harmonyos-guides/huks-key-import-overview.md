---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-import-overview
title: 密钥导入介绍及算法规格
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 密钥生成/导入 > 密钥导入 > 密钥导入介绍及算法规格
category: harmonyos-guides
scraped_at: 2026-04-29T13:31:56+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:88f2c8304e852e750bba4fb53c7acb90e68527e06167f46c0b4886b686a3e89b
---

如果业务在HUKS外部生成密钥（比如应用间协商生成、服务器端生成），业务可以将密钥导入到HUKS中由HUKS进行管理。密钥一旦导入到HUKS中，在密钥的生命周期内，其明文仅在安全环境中进行访问操作，不会传递出安全环境。

密钥导入的方式包含明文导入和安全导入两种方式。

说明

使用现有密钥别名作为导入的密钥别名会把现有密钥覆盖。

从API 23开始支持[群组密钥](huks-group-key-overview.md)特性。

## 明文导入

该方式直接将密钥明文导入HUKS，在导入过程中密钥明文会暴露在非安全环境中，一般适用于轻量级智能穿戴或低安业务。

* 推荐使用该方式导入的密钥类型：非对称密钥的公钥。
* 不推荐使用该方式导入的密钥类型：对称密钥、非对称密钥对。

  说明

  轻量级智能穿戴只支持明文导入，不支持安全导入。

## 安全导入

该方式支持业务与HUKS建立端到端的加密传输通道，将密钥安全加密导入到HUKS中，确保导入过程中密钥不被泄露，适用于高安敏感业务。相较于明文导入，安全导入步骤更多，密钥材料更复杂。

* 推荐使用该方式导入的密钥类型：对称密钥、非对称密钥对。

下图为安全导入密钥开发时序图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/aUXf7evQSEaIMbqlmAsuww/zh-cn_image_0000002558764910.png?HW-CC-KV=V1&HW-CC-Date=20260429T053155Z&HW-CC-Expire=86400&HW-CC-Sign=ACC9B19CFEBF285C779C9C7B158E81E46791F5321AD7A65DB40962AB3C49EBC4)

根据开发流程，在安全导入密钥过程中，需要依次调用HUKS的能力包括：

* 生成非对称密钥对并导出公钥，用于设备间密钥协商。
* 生成对称密钥，用于加密待导入密钥。
* 使用对称密钥加密待导入密钥，形成密钥密文。
* 导入加密密钥。
* 删除密钥。

导出密钥接口返回的[公钥明文材料是按照**X.509**格式封装](huks-concepts.md#公钥材料格式)，导入加密密钥接口中的密钥材料需满足**LengthData-Data**的格式封装，形如：[(Lengthpart1Datapart1)……(LengthpartnDatapartn)]。

说明

1. 安全导入密钥时，协商算法支持ECDH和X25519，协商后的Shared\_Key使用AES-GCM算法加密Caller\_Kek。对应算法套件定义见[HuksUnwrapSuite](../harmonyos-references/js-apis-huks.md#huksunwrapsuite9)。
2. 安全导入不支持X.509格式。
3. 轻量级智能穿戴只支持明文导入，不支持安全导入。

### 安全导入密钥材料格式

| 内容 | 长度 |
| --- | --- |
| 业务公钥长度LCaller\_Pk | 4字节 |
| 业务公钥Caller\_Pk | LCaller\_Pk字节 |
| Shared\_Key加密参数AAD2长度LAAD2 | 4字节 |
| Shared\_Key加密参数AAD2 | LAAD2字节 |
| Shared\_Key加密参数NONCE2长度LNONCE2 | 4字节 |
| Shared\_Key加密参数NONCE2 | LNONCE2字节 |
| Shared\_Key加密参数TAG2长度LTAG2 | 4字节 |
| Shared\_Key加密参数TAG2 | LTAG2字节 |
| Caller\_Kek密文长度LCaller\_Kek\_enc | 4字节 |
| Caller\_Kek密文Caller\_Kek\_enc | LCaller\_Kek\_enc字节 |
| Caller\_Kek加密参数AAD3长度LAAD3 | 4字节 |
| Caller\_Kek加密参数AAD3 | LAAD3字节 |
| Caller\_Kek加密参数NONCE3长度LNONCE3 | 4字节 |
| Caller\_Kek加密参数NONCE3 | LNONCE3字节 |
| Caller\_Kek加密参数TAG3长度LTAG3 | 4字节 |
| Caller\_Kek加密参数TAG3 | LTAG3字节 |
| 密钥明文材料长度的长度LTo\_Import\_Key\_size | 4字节 |
| 密钥明文材料长度To\_Import\_Key\_size | LTo\_Import\_Key\_size字节 |
| To\_Import\_Key密文长度LTo\_Import\_Key\_enc | 4字节 |
| To\_Import\_Key密文To\_Import\_Key\_enc | LTo\_Import\_Key\_enc字节 |

## 数字信封导入

从API 23开始支持[数字信封](huks-key-import-overview.md#数字信封导入)特性。

该方式支持以数字信封形式导入密钥，确保密钥安全导入HUKS，防止传输过程中泄露，适用于高安全敏感业务。

推荐使用该方法导入的密钥类型：对称密钥、非对称密钥对。

下图为数字信封导入密钥开发时序图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/VF-JEuvIRPuL8KzwGVx2_A/zh-cn_image_0000002558605254.png?HW-CC-KV=V1&HW-CC-Date=20260429T053155Z&HW-CC-Expire=86400&HW-CC-Sign=13E837A79818F62E7DB61A4A53EFFAE2CC014AA296384144A8264C04F89D14AA)

根据业务流程，导入数字信封时需要调用HUKS的能力。

* 生成SM4密钥，用于加密将导入的密钥。
* 使用生成的SM4密钥并采用ECB，NoPadding模式对导入密钥明文进行加密，若业务导入非对称密钥仅需加密其私钥。
* 导出对端SM2公钥，用于加密生成的SM4密钥。
* 使用对端导出的SM2公钥，采用NoPadding模式并指定SM3为摘要算法加密本端生成的SM4密钥。
* 导入加密密钥。

导出密钥接口返回的[公钥材料格式](huks-concepts.md#公钥材料格式)按照X.509格式封装，导入加密密钥接口返回的密钥材料按照**LengthData-Data**的格式封装，分别是[(LengthEncSm4DataEncSm4)(LengthEncImpKeyDataEncImpKey)]。

说明

仅手机、平板、PC/2in1设备、TV、智能穿戴支持数字信封导入。

## 支持的算法

以下为密钥导入支持的规格说明。

说明

导入RSA密钥时，公钥必须大于或者等于65537。

数字信封不支持 DSA 算法，X25519密钥和Ed25519密钥，在使用数字信封导入密钥时公钥采用裸密钥的方式在该标签中填入。

**手机、平板、PC/2in1设备、TV、智能穿戴规格**

| 算法 | 支持的密钥长度 | API级别 |
| --- | --- | --- |
| AES | 128、192、256 | 8+ |
| RSA | 2048、3072、4096 | 8+ |
| RSA | 1024-2048（含），必须是8的倍数 | 18+ |
| HMAC | 8-1024（含），必须是8的倍数 | 8+ |
| ECC | 256、384、521 | 8+ |
| ED25519 | 256 | 8+ |
| X25519 | 256 | 8+ |
| DH | 2048 | 8+ |
| SM2 | 256 | 9+ |
| SM4 | 128 | 9+ |
| DES | 64 | 18+ |
| 3DES | 128、192 | 18+ |

**轻量级智能穿戴规格**

| 算法 | 支持的密钥长度 | API级别 |
| --- | --- | --- |
| AES | 128、192、256 | 12+ |
| DES | 64 | 12+ |
| 3DES | 128、192 | 12+ |
| RSA | 1024-2048（含），必须是8的倍数 | 12+ |
| HMAC | 8-1024（含），必须是8的倍数 | 12+ |
| CMAC | 128 | 12+ |

## 导入密钥格式

HUKS支持导入密钥类型众多，各种不同类型对应的密钥格式不尽相同。下表归纳了HUKS导入密钥所支持的密钥类型及对应的密钥材料格式。

| 密钥类型 | 算法 | 导入格式 |
| --- | --- | --- |
| 对称密钥 | - | 密钥字节数据 |
| 非对称密钥-密钥对 | - | [密钥对材料格式](huks-concepts.md#密钥对材料格式) |
| 非对称密钥-公钥 | ED25519、X25519 | 密钥字节数据，参考[导入X25519密钥公钥](huks-import-key-in-plaintext-arkts.md#导入x25519密钥公钥) |
| 非对称密钥-公钥 | RSA、ECC、ECDH、DH、SM2 | X.509规范的DER格式 |
