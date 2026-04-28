---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-detect-simulated-click-risk-enhanced
title: Web应用模拟点击检测
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 管理网页交互 > Web应用模拟点击检测
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:140f950e8506da9f79012c37b15d04d82dfd50c458820c57e6c1b0f3ec25cf80
---

从API version 23开始，新增支持Web应用模拟点击检测。

Web应用通过Javascript调用window.detectSimulatedClickRiskEnhanced接口，获取模拟点击检测结果。用于自动化点击、设备墙等作弊行为检测。

应用可以根据检测结果评估如何进行业务操作。

## 约束与限制

* 每30秒最多可以调用10次，每个应用在每个设备上每天最多可以调用20次。
* 当前检测仅支持设备：Phone。

## 接口说明

window.detectSimulatedClickRiskEnhanced(algorithm, nonce, version)

获取模拟点击检测结果。使用Promise异步回调。

**入参：**

| 参数名 | 类型 | 可选 | 说明 |
| --- | --- | --- | --- |
| algorithm | number | 否 | 数字签名算法。可选值：  0 - SHA256withECDSA算法。 |
| nonce | array | 否 | 包含随机数的数组，用于防重放攻击，在检测结果中会包含该值。  长度范围[24, 80]，元素数值范围[-128, 127]。 |
| version | number | 是 | 检测结果消息格式的版本，当前仅支持1。  默认值：1。 |

**返回值：**

Promise对象，返回模拟点击检测结果，格式为一个JSON Web Signature格式（JWS）的字符串，使用Base64URL编码，如果发生异常或错误，则返回错误码。JWS中包含Header、Payload、Signature三部分，每个部分之间以"."分割。解码后的各字段定义如下：

* **Header**

样例：

```
1. {
2. "alg": "ES256",
3. "x5c": ["", ""],
4. "nonce": "R2Rra24fVm5xa2Mg",
5. "appId": "xxxxxxxx",
6. "authToken": "xxxxxxxx"
7. }
```

| 字段 | 描述 |
| --- | --- |
| alg | 签名算法名称，ES256表示为使用ECDSA和SHA256算法进行签名。 |
| x5c | 华为签名服务器对JWS签名的证书链，x5c[0]为给JWS签名的证书，x5c[1]为签名证书链二级CA。 |
| nonce | 请求参数nonce值的Base64编码。 |
| appId | 您在华为开发者联盟网站上申请的APP ID。 |

* **Payload**

样例：

```
1. {
2. "timestampMs": 9860437986543,
3. "version": 1,
4. "riskDecision": "fake",
5. "tags": ["AbnormalTap"]
6. }
```

| 字段 | 描述 |
| --- | --- |
| timestampMs | 发起请求时生成的时间戳。 |
| version | 检测结果消息格式的版本。默认值为1，当前只支持1。 |
| riskDecision | 风险检测结果。 |
| tags | 模拟点击关键特征。  如果tags列表为空，表示未发现关键特征。 |

| riskDecision | 含义 |
| --- | --- |
| fake | 当前设备存在作弊风险行为。存在自动化操控行为或设备墙作弊行为，详情见tags。 |
| likelyReal | 当前操作设备的时真人用户的可能性较高。 |
| unknown | 未知。未检测到明显特征，无法识别。 |

| tags | 含义 |
| --- | --- |
| AbnormalDeviceIntegrity | 设备完整性遭到破坏。 |
| AbnormalDeviceBehavior | 设备行为异常，例如，设备连接状态、传感器状态等行为异常。 |
| AbnormalTap | 存在异常点击行为，例如，点击事件注入，自动化点击等。 |

* **Signature**

使用JWS签名证书x5c[0]对包含Header和Payload计算的签名。签名的输出格式参考RFC7518标准。

* **错误码**

当调用出现异常时，可通过Promise的catch方法捕获异常。e.code为错误码，e.message为错误信息。

| 错误码 | 错误信息 |
| --- | --- |
| 1012500001 | Internal error. |
| 1012500002 | The network is unreachable. |
| 1012500003 | Access cloud server fail. |
| 1012500005 | The interface access frequency exceeds the limit. |
| 1012500006 | Internal timeout. |
| 1012500007 | Invalid parameters. |

## 代码示例

```
1. // 兼容性判断
2. if (window.detectSimulatedClickRiskEnhanced) {
3. // 此处nonce入参仅为示例，实际开发时应为包含随机数的数组
4. window.detectSimulatedClickRiskEnhanced(0, new Array(48).fill(0), 1).then(result => {
5. console.info('Detect simulated click risk success. length: ', result.length);
6. const resultArray = result.split('.');
7. const header = resultArray[0];
8. const payload = resultArray[1];
9. const signature = resultArray[2];
10. }).catch(e => {
11. console.error('Detect simulated click risk failed: ', e.code, e.message);
12. });
13. } else {
14. // 不支持该接口时
15. }
```

## 开发流程

**1. 开发者应用获取nonce**

在调用window.detectSimulatedClickRiskEnhanced接口时，开发者必须传入一个随机生成的nonce数组。在检测结果中会包含这个nonce值，您可以通过校验这个nonce值来确定返回结果能够对应您的请求，并且没有被重放攻击。

说明

* nonce是一个数组，数组长度范围[24, 80]，其中元素数值范围[-128, 127]。
* 推荐的做法是，每次请求都从服务器随机生成新的nonce数组。

**2. 发起模拟点击检测请求**

设备端收到请求后，首先采集当前设备模拟点击线索数据，然后将线索数据与nonce一起发送到Device Security服务器做检测，最后通过接口返回检测结果给开发者应用。

**3. 在开发者应用服务器中验证模拟点击检测结果**

在发起业务请求之前，开发者应用需在应用服务器中验证模拟点击检测结果。按以下步骤验证检测结果：

1. 解析JWS，获取header、payload、signature。
2. 从header中获取证书链，使用[Huawei CBG Device Attestation Root CA](https://pki.consumer.huawei.com/ca/cer/Huawei_CBG_ECC_Device_Attestation_Root_CA.cer)证书对其进行验证。
3. 校验证书链中x5c[0]证书的Common Name是否为Harmony OS Device Attestation Service。
4. 从signature中获取签名，校验其签名。
5. 最后从payload中获取模拟点击检测结果。

验证检测结果的完整示例可参考[java示例代码](https://gitcode.com/HarmonyOS_Samples/device-security-kit-sample-code-business-risk-intelligent-detection-server-demo-java)。
