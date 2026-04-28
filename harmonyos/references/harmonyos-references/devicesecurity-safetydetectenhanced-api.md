---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-safetydetectenhanced-api
title: SafetyDetect（安全检测）
breadcrumb: API参考 > 系统 > 安全 > Device Security Kit（设备安全服务） > ArkTS API > SafetyDetect（安全检测）
category: harmonyos-references
scraped_at: 2026-04-28T08:07:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:48c7d0eff9bc6b872c7d6c74c4940e348486504e9452a23c0300dee247149785
---

* 判断设备环境是否安全，比如是否被越狱、被模拟等，您可基于结果评估如何响应。
* 判断用户访问的URL是否为恶意网址，对于恶意网址，由您评估提示或拦截用户的访问风险。

**起始版本：** 5.0.0(12)

## 导入模块

PhonePC/2in1TabletWearable

```
1. import { safetyDetect } from '@kit.DeviceSecurityKit';
```

## SysIntegrityRequest

PhonePC/2in1TabletWearable

系统完整性检测的请求参数。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SafetyDetect

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| nonce | string | 否 | 否 | 开发者应用传入的一个随机生成的nonce值，用于防重放攻击，在检测结果中会包含该值。 |

## SysIntegrityResponse

PhonePC/2in1TabletWearable

系统完整性检测返回值。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SafetyDetect

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| result | string | 否 | 否 | JWS格式的系统完整性检测结果。JWS内容详见《Device Security Kit开发指南》中的系统完整性检测[开发步骤](../harmonyos-guides/devicesecurity-sysintegrity-check.md#开发步骤)。 |

## UrlCheckRequest

PhonePC/2in1TabletWearable

URL检测请求参数。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SafetyDetect

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| urls | Array<string> | 否 | 否 | 被检测的URL列表 |

## UrlCheckResponse

PhonePC/2in1TabletWearable

URL检测返回值。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SafetyDetect

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| results | Array<[UrlCheckResult](devicesecurity-safetydetectenhanced-api.md#urlcheckresult)> | 否 | 否 | URL检测返回的检测结果 |

## UrlCheckResult

PhonePC/2in1TabletWearable

URL检测结果详情。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SafetyDetect

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| url | string | 否 | 否 | 对应到输入参数中被检测的URL |
| threat | [UrlThreatType](devicesecurity-safetydetectenhanced-api.md#urlthreattype) | 否 | 否 | URL的威胁类型 |

## UrlThreatType

PhonePC/2in1TabletWearable

枚举URL威胁类型。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SafetyDetect

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NORMAL | 0 | 未发现威胁。 |
| MALWARE | 1 | 恶意类型的URL。 |
| PHISHING | 2 | 钓鱼类型的URL |
| OTHERS | 3 | 其他威胁类型的URL |

## checkSysIntegrity

PhonePC/2in1TabletWearable

checkSysIntegrity(req: [SysIntegrityRequest](devicesecurity-safetydetectenhanced-api.md#sysintegrityrequest)): Promise<[SysIntegrityResponse](devicesecurity-safetydetectenhanced-api.md#sysintegrityresponse)>

获取本设备的系统完整性的在线检测结果。使用Promise异步回调。

注意

该接口涉及端云协同，需要联网等耗时操作，因此不要在UI线程中执行，避免阻塞UI线程。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SafetyDetect

**起始版本：** 5.0.0(12)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| req | [SysIntegrityRequest](devicesecurity-safetydetectenhanced-api.md#sysintegrityrequest) | 是 | 请求参数，包含nonce。  nonce长度必须16至66字节之间，有效值为base64编码范围。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SysIntegrityResponse](devicesecurity-safetydetectenhanced-api.md#sysintegrityresponse)> | Promise对象，返回系统完整性检测结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-safetydetect.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameters.  Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |
| 801 | API is not supported. |
| 1010800001 | Internal error. |
| 1010800002 | The network is unreachable. |
| 1010800003 | Access cloud server fail. |
| 1010800005 | The number of calls exceeds the parallel threshold. |
| 1010800006 | The invoking frequency exceeds the threshold. |
| 1010800007 | Operation timeout. |
| 1010800008 | The cloud service traffic exceeds the threshold. |

**示例：**

```
1. import { safetyDetect } from '@kit.DeviceSecurityKit';
2. import { BusinessError} from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG = "SafetyDetectJsTest";

7. // 请求系统完整性检测，并处理结果
8. let req : safetyDetect.SysIntegrityRequest = {
9. nonce : 'imEe1PCRcjGkBCAhOCh6ImADztOZ8ygxlWRs' // 从服务器生成的随机的nonce值
10. };
11. try {
12. hilog.info(0x0000, TAG, 'CheckSysIntegrity begin.');
13. const data: safetyDetect.SysIntegrityResponse = await safetyDetect.checkSysIntegrity(req);
14. hilog.info(0x0000, TAG, 'Succeeded in checkSysIntegrity: %{public}s', data.result);
15. } catch (err) {
16. let e: BusinessError = err as BusinessError;
17. hilog.error(0x0000, TAG, 'CheckSysIntegrity failed: %{public}d %{public}s', e.code, e.message);
18. }
```

## checkUrlThreat

PhonePC/2in1TabletWearable

checkUrlThreat(req: [UrlCheckRequest](devicesecurity-safetydetectenhanced-api.md#urlcheckrequest)): Promise<[UrlCheckResponse](devicesecurity-safetydetectenhanced-api.md#urlcheckresponse)>

检测URL是否为恶意网址。使用Promise异步回调。

注意

该接口涉及端云协同，需要联网等耗时操作，因此不要在UI线程中执行，避免阻塞UI线程。

**元服务API：** 从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SafetyDetect

**起始版本：** 5.0.0(12)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| req | [UrlCheckRequest](devicesecurity-safetydetectenhanced-api.md#urlcheckrequest) | 是 | 请求参数，包含被检测的URL列表。  传入的URL数量最多10个并且每个URL长度不大于4096字节。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[UrlCheckResponse](devicesecurity-safetydetectenhanced-api.md#urlcheckresponse)> | Promise对象，返回URL检测结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-safetydetect.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Invalid parameters.  Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |
| 801 | API is not supported. |
| 1010800001 | Internal error. |
| 1010800002 | The network is unreachable. |
| 1010800003 | Access cloud server fail. |
| 1010800005 | The number of calls exceeds the parallel threshold. |
| 1010800006 | The invoking frequency exceeds the threshold. |
| 1010800007 | Operation timeout. |
| 1010800008 | The cloud service traffic exceeds the threshold. |

**示例：**

```
1. import { safetyDetect } from '@kit.DeviceSecurityKit';
2. import { BusinessError} from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG = "SafetyDetectJsTest";

7. // 请求URL检测，并处理结果
8. let req : safetyDetect.UrlCheckRequest = {
9. urls : ['https://test1.com']
10. };
11. try {
12. hilog.info(0x0000, TAG, 'CheckUrlThreat begin.');
13. const data: safetyDetect.UrlCheckResponse = await safetyDetect.checkUrlThreat(req);
14. hilog.info(0x0000, TAG, 'Succeeded in checkUrlThreat: %{public}s %{public}d', data.results[0].url, data.results[0].threat);
15. } catch (err) {
16. let e: BusinessError = err as BusinessError;
17. hilog.error(0x0000, TAG, 'CheckUrlThreat failed: %{public}d %{public}s', e.code, e.message);
18. }
```

## checkSysIntegrityOnLocal

PhonePC/2in1TabletWearable

checkSysIntegrityOnLocal(): Promise<string>

获取本设备的系统完整性的本地检测结果。使用Promise异步回调。

**元服务API：** 从版本5.1.0(18)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SafetyDetect

**起始版本：** 5.1.0(18)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回JSON格式的系统完整性检测结果。JSON内容详见《Device Security Kit开发指南》中的本地系统完整性检测[开发步骤](../harmonyos-guides/devicesecurity-sysintegrity-check-onlocal.md#开发步骤)。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-safetydetect.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | API is not supported. |
| 1010800001 | Internal error. |
| 1010800004 | Verify capability fail. |
| 1010800005 | The number of calls exceeds the parallel threshold. |
| 1010800006 | The invoking frequency exceeds the threshold. |
| 1010800007 | Operation timeout. |

**示例：**

```
1. import { safetyDetect } from '@kit.DeviceSecurityKit';
2. import { BusinessError} from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG = "SafetyDetectJsTest";

7. // 请求本地系统完整性检测，并处理结果
8. try {
9. hilog.info(0x0000, TAG, 'CheckSysIntegrityOnLocal begin.');
10. const result: string = await safetyDetect.checkSysIntegrityOnLocal();
11. hilog.info(0x0000, TAG, 'Succeeded in checkSysIntegrityOnLocal: %{public}s', result);
12. } catch (err) {
13. let e: BusinessError = err as BusinessError;
14. hilog.error(0x0000, TAG, 'CheckSysIntegrityOnLocal failed: %{public}d %{public}s', e.code, e.message);
15. }
```

## checkSysIntegrityEnhanced

PhonePC/2in1TabletWearable

checkSysIntegrityEnhanced(req: [SysIntegrityRequest](devicesecurity-safetydetectenhanced-api.md#sysintegrityrequest)): Promise<[SysIntegrityResponse](devicesecurity-safetydetectenhanced-api.md#sysintegrityresponse)>

获取本设备的系统完整性的在线增强检测结果。使用Promise异步回调。

注意

该接口涉及端云协同，需要联网等耗时操作，因此不要在UI线程中执行，避免阻塞UI线程。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.SafetyDetect

**起始版本：** 6.0.0(20)

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| req | [SysIntegrityRequest](devicesecurity-safetydetectenhanced-api.md#sysintegrityrequest) | 是 | 请求参数，包含nonce。  nonce长度必须16至66字节之间，有效值为base64编码范围。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SysIntegrityResponse](devicesecurity-safetydetectenhanced-api.md#sysintegrityresponse)> | Promise对象，返回系统完整性增强检测结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](devicesecurity-arktsapi-errcode-safetydetect.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | API is not supported. |
| 1010800001 | Internal error. |
| 1010800002 | The network is unreachable. |
| 1010800003 | Access cloud server fail. |
| 1010800004 | Verify capability fail. |
| 1010800005 | The number of calls exceeds the parallel threshold. |
| 1010800006 | The invoking frequency exceeds the threshold. |
| 1010800007 | Operation timeout. |
| 1010800008 | The cloud service traffic exceeds the threshold. |

**示例：**

```
1. import { safetyDetect } from '@kit.DeviceSecurityKit';
2. import { BusinessError} from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG = "SafetyDetectJsTest";

7. // 请求系统完整性增强检测，并处理结果
8. let req : safetyDetect.SysIntegrityRequest = {
9. nonce : 'imEe1PCRcjGkBCAhOCh6ImADztOZ8ygxlWRs' // 从服务器生成的随机的nonce值
10. };
11. try {
12. hilog.info(0x0000, TAG, 'CheckSysIntegrityEnhanced begin.');
13. const data: safetyDetect.SysIntegrityResponse = await safetyDetect.checkSysIntegrityEnhanced(req);
14. hilog.info(0x0000, TAG, 'Succeeded in checkSysIntegrityEnhanced: %{public}s', data.result);
15. } catch (err) {
16. let e: BusinessError = err as BusinessError;
17. hilog.error(0x0000, TAG, 'CheckSysIntegrityEnhanced failed: %{public}d %{public}s', e.code, e.message);
18. }
```
