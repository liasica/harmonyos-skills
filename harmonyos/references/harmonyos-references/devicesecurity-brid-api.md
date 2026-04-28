---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-brid-api
title: BusinessRiskIntelligentDetection（业务风险检测）
breadcrumb: API参考 > 系统 > 安全 > Device Security Kit（设备安全服务） > ArkTS API > BusinessRiskIntelligentDetection（业务风险检测）
category: harmonyos-references
scraped_at: 2026-04-28T08:07:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bc0f0fb161459ef77c48f568549e9be5bb004841d966659d7ab64473c991601b
---

* 识别当前设备的涉诈行为风险。

**起始版本：** 5.0.0(12)

* 提供自动化点击、设备墙等作弊行为检测能力。

**起始版本：** 6.0.0(20)

## 导入模块

PhoneTablet

```
1. import { businessRiskIntelligentDetection } from '@kit.DeviceSecurityKit';
```

## FraudDetectionRequest

PhoneTablet

涉诈剧本检测的请求参数。

**系统能力：** SystemCapability.Security.BusinessRiskIntelligentDetection

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| nonce | Uint8Array | 否 | 否 | 开发者应用传入的一个随机生成的nonce值，用于防重放攻击，在检测结果中会包含该值。nonce值必须为24至80字节之间。 |
| algorithm | [SigningAlgorithm](devicesecurity-brid-api.md#signingalgorithm) | 否 | 否 | 数字签名算法。 |
| version | number | 否 | 是 | 检测结果消息格式的版本，默认值为1，可选1和2，取值为2时检测结果的Tag标签中带有时间属性和风险等级，其中时间属性表示该标签对应线索的最后一次发生时间，风险等级表示该标签对应的风险级别，取值为1时，检测结果Tag标签中不带时间属性和风险等级。  **起始版本：** 5.1.0(18) |

## SimulatedClickDetectionRequest

PhoneTablet

模拟点击检测的请求参数。

**系统能力：** SystemCapability.Security.BusinessRiskIntelligentDetection

**起始版本：** 6.0.0(20)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| version | number | 否 | 是 | 检测结果消息格式的版本，默认值为1，当前只支持1。 |

## SimulatedClickDetectionEnhancedRequest

PhoneTablet

模拟点击增强检测的请求参数。

系统能力：SystemCapability.Security.BusinessRiskIntelligentDetection

**起始版本：** 6.0.2(22)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| nonce | Uint8Array | 否 | 否 | 开发者应用传入的一个随机生成的nonce值，用于防重放攻击，在检测结果中会包含该值。nonce值必须为24至80字节之间。 |
| algorithm | [SigningAlgorithm](devicesecurity-brid-api.md#signingalgorithm) | 否 | 否 | 数字签名算法。 |
| version | number | 否 | 是 | 检测结果消息格式的版本，默认值为1，当前版本号只支持1。 |

## SigningAlgorithm

PhoneTablet

数字签名算法。

**系统能力：** SystemCapability.Security.BusinessRiskIntelligentDetection

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ES256 | 0 | SHA256withECDSA。 |

## detectFraudRisk

PhoneTablet

detectFraudRisk(params: [FraudDetectionRequest](devicesecurity-brid-api.md#frauddetectionrequest)): Promise<string>

获取本设备的涉诈行为风险。使用Promise异步回调。

**系统能力：** SystemCapability.Security.BusinessRiskIntelligentDetection

**起始版本：** 5.0.0(12)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [FraudDetectionRequest](devicesecurity-brid-api.md#frauddetectionrequest) | 是 | 请求参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回涉诈风险检测结果，一个JSON Web Signature格式的字符串，使用Base64URL编码，如果发生异常或错误，则返回错误码。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-brid.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameters. |
| 1012500001 | Internal error. |
| 1012500002 | The network is unreachable. |
| 1012500003 | Access cloud server fail. |
| 1012500004 | Verify cloud capability fail. |

**示例：**

```
1. import { businessRiskIntelligentDetection } from '@kit.DeviceSecurityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { cryptoFramework } from '@kit.CryptoArchitectureKit';

6. const TAG = "[BusinessRiskIntelligentDetectionModel]";

8. let rand = cryptoFramework.createRandom();
9. let len = 48;
10. let randData = rand.generateRandomSync(len);
11. let params = {
12. nonce: randData.data,
13. algorithm: businessRiskIntelligentDetection.SigningAlgorithm.ES256
14. } as businessRiskIntelligentDetection.FraudDetectionRequest;
15. try {
16. hilog.info(0x0000, TAG, 'Detect fraud risk begin.');
17. businessRiskIntelligentDetection.detectFraudRisk(params).then((result: string) => {
18. hilog.info(0x0000, TAG, 'Detect fraud risk success: %{public}s', result);
19. }).catch((error: Error) => {
20. let e: BusinessError = error as BusinessError;
21. hilog.error(0x0000, TAG, 'Detect fraud risk failed: %{public}d %{public}s', e.code, e.message);
22. });
23. } catch (error) {
24. let e: BusinessError = error as BusinessError;
25. hilog.error(0x0000, TAG, 'Detect fraud risk failed: %{public}d %{public}s', e.code, e.message);
26. }
```

## detectSimulatedClickRisk

PhoneTablet

detectSimulatedClickRisk(params: [SimulatedClickDetectionRequest](devicesecurity-brid-api.md#simulatedclickdetectionrequest)): Promise<string>

获取自动化点击、设备墙等作弊行为检测结果。使用Promise异步回调。

**系统能力：** SystemCapability.Security.BusinessRiskIntelligentDetection

**起始版本：** 6.0.0(20)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [SimulatedClickDetectionRequest](devicesecurity-brid-api.md#simulatedclickdetectionrequest) | 是 | 请求参数 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回模拟点击检测结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-brid.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1012500001 | Internal error. |
| 1012500002 | The network is unreachable. |
| 1012500003 | Access cloud server fail. |
| 1012500004 | Verify cloud capability fail. |
| 1012500005 | The interface access frequency exceeds the limit. |
| 1012500006 | Internal timeout. |
| 1012500007 | Invalid parameters. |

**示例：**

```
1. import { businessRiskIntelligentDetection } from '@kit.DeviceSecurityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG = "BusinessRiskIntelligentDetectionJsTest";

7. let params = {
8. version: 1
9. } as businessRiskIntelligentDetection.SimulatedClickDetectionRequest;
10. try {
11. hilog.info(0x0000, TAG, 'Detect simulated click risk begin.');
12. businessRiskIntelligentDetection.detectSimulatedClickRisk(params).then((result: string) => {
13. hilog.info(0x0000, TAG, 'Detect simulated click risk success: %{public}s', result);
14. }).catch((error: Error) => {
15. let e: BusinessError = error as BusinessError;
16. hilog.error(0x0000, TAG, 'Detect simulated click risk failed: %{public}d %{public}s', e.code, e.message);
17. });
18. } catch (error) {
19. let e: BusinessError = error as BusinessError;
20. hilog.error(0x0000, TAG, 'Detect simulated click risk failed: %{public}d %{public}s', e.code, e.message);
21. }
```

## detectSimulatedClickRiskEnhanced

PhoneTablet

detectSimulatedClickRiskEnhanced(params: SimulatedClickDetectionEnhancedRequest): Promise<string>

获取自动化点击、设备墙等作弊行为的增强检测结果。使用Promise异步回调。

**系统能力：** SystemCapability.Security.BusinessRiskIntelligentDetection

**起始版本：** 6.0.2(22)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [SimulatedClickDetectionEnhancedRequest](devicesecurity-brid-api.md#simulatedclickdetectionenhancedrequest) | 是 | 请求参数 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回模拟点击增强检测结果，一个JSON Web Signature格式的字符串，使用Base64URL编码，如果发生异常或错误，则返回错误码。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-brid.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1012500001 | Internal error |
| 1012500002 | The network is unreachable. |
| 1012500003 | Access cloud server fail. |
| 1012500005 | The interface access frequency exceeds the limit. |
| 1012500006 | Internal timeout. |
| 1012500007 | Invalid parameters. |

**示例：**

```
1. import { businessRiskIntelligentDetection } from '@kit.DeviceSecurityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { cryptoFramework } from '@kit.CryptoArchitectureKit';

6. const TAG = "BusinessRiskIntelligentDetectionJsTest";

8. let nonceLength = 48;
9. let nonceBlob = cryptoFramework.createRandom().generateRandomSync(nonceLength);
10. let params = {
11. version: 1,
12. nonce: nonceBlob.data,
13. algorithm: businessRiskIntelligentDetection.SigningAlgorithm.ES256
14. } as businessRiskIntelligentDetection.SimulatedClickDetectionEnhancedRequest;
15. try {
16. hilog.info(0x0000, TAG, 'Detect simulated click risk enhanced begin.');
17. businessRiskIntelligentDetection.detectSimulatedClickRiskEnhanced(params).then((result: string) => {
18. hilog.info(0x0000, TAG, 'Detect simulated click risk enhanced success: %{public}s', result);
19. }).catch((error: Error) => {
20. let e: BusinessError = error as BusinessError;
21. hilog.error(0x0000, TAG, 'Detect simulated click risk enhanced failed: %{public}d %{public}s', e.code, e.message);
22. });
23. } catch (error) {
24. let e: BusinessError = error as BusinessError;
25. hilog.error(0x0000, TAG, 'Detect simulated click risk enhanced failed: %{public}d %{public}s', e.code, e.message);
26. }
```
