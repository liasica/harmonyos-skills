---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-attestation-overview
title: 密钥证明介绍及算法规格
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 密钥证明 > 密钥证明介绍及算法规格
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:24+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ffea5c83f83dee556616a58220e291bb19ad47865dc7a962dc901e8bbd2bd1ab
---

HUKS为密钥提供合法性证明能力，主要应用于非对称密钥的公钥的证明。

基于PKI证书链技术，HUKS可以为存储在HUKS中的非对称密钥对的公钥签发证书，证明其公钥的合法性。业务可以通过系统提供的根CA证书，逐级验证HUKS签发的密钥证明证书，来确保证书中的公钥以及对应的私钥，确实来自合法的硬件设备，且存储管理在HUKS中。

说明

* 当调用方为系统服务且APL等级为normal时，暂不支持密钥证明，此种情况下，processName与APL字段将置空。
* 密钥证明功能在模拟器场景不支持。
* 轻量级智能穿戴不支持密钥证明功能。
* 支持生成密钥和导入密钥进行密钥证明，业务方在服务器侧需要通过业务证书中的密钥来源字段校验密钥来源是否符合预期。

从API 23开始支持[群组密钥](huks-group-key-overview.md)特性。

密钥证明扩展域段为Asn.1 DER标准编码格式，数据结构定义如下：

```
1. KeyAttestation ::= SEQUENCE {
2. version            AttestationVersion DEFAULT v1,
3. claim1             AttestationClaim,
4. claim2             AttestationClaim,
5. claim3             AttestationClaim,
6. ... ...
7. }
8. AttestationVersion ::= INTEGER { v1(0) }
9. AttestationClaim ::= SEQUENCE {
10. securityLevel      SecurityLevel,
11. type               AttestationType,
12. value              AttestationValue
13. }
14. SecurityLevel ::= INTEGER
15. AttestationType ::= OBJECT IDENTIFIER
16. AttestationValue ::= ANY -- DEFINED BY AttestationType
17. ApplicationIDType ::= SEQUENCE {
18. type               OBJECT IDENTIFIER,
19. value              OCT_STR
20. }
```

常用AttestationClaim类型取值说明：

| type（OID）取值 | value的数据类型 | securityLevel | Claim说明 |
| --- | --- | --- | --- |
| 1.3.6.1.4.1.2011.2.376.2.1.4 | OCT\_STR | 保留字段，暂不使用 | 应用输入的挑战值Challenge。 |
| 1.3.6.1.4.1.2011.2.376.2.1.3 | ApplicationIDType | 保留字段，暂不使用 | 应用ID。 |
| 1.3.6.1.4.1.2011.2.376.2.1.5 | OCT\_STR | 保留字段，暂不使用 | 密钥来源，生成或者导入。 |
| 1.3.6.1.4.1.2011.2.376.2.2.4.8 | UTF8\_STR | 保留字段，暂不使用 | 产品型号Model。从API 20开始支持。 |

ApplicationIDType类型取值说明：

| type（OID）取值 | value取值说明 |
| --- | --- |
| 1.3.6.1.4.1.2011.2.376.2.1.3.1 | 样例：{appId:"xxx", bundleName:"xxx", appIdentifier:"xxx", appMode:"xxx"}  其中appIdentifier、appMode从API 20开始支持。 |
| 1.3.6.1.4.1.2011.2.376.2.1.3.2 | 样例：{processName:"xxx", APL:"system\_basic | system\_core"}  APL为[系统服务等级](app-permission-mgmt-overview.md#权限机制中的基本概念)。 |

密钥证明过程如下：

1. 业务将指定密钥别名和需要证明的密钥属性的标签传入HUKS。
2. 调用HUKS为应用生成一个依次由根CA证书、设备CA证书、设备证书、密钥证书组成的X.509证书链。
3. 将证书链传输至受信任的服务器，并在服务器上解析和验证证书链的有效性和单个证书是否吊销。

当前提供了匿名密钥证明的方式，不会泄露设备信息，没有权限管理。面向所有应用开放。为了保护用户设备信息，三方应用开发者只能使用匿名密钥证明。

当前模拟器支持匿名证书，调试环境中使用的证书非真实设备证书，云侧需要区分该场景，避免误用。

## 支持的算法

以下为密钥证明支持的规格说明。

| 算法 | 备注 | API级别 |
| --- | --- | --- |
| RSA | 支持Padding为PSS与PKCS1\_V1\_5的密钥 | 11+ |
| ECC | - | 11+ |
| X25519 | - | 16+ |
| ED25519 | - | 16+ |
| SM2 | - | 11+ |
