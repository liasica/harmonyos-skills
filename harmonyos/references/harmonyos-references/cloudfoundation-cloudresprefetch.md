---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cloudfoundation-cloudresprefetch
title: cloudResPrefetch（预加载模块）
breadcrumb: API参考 > 应用服务 > Cloud Foundation Kit（云开发服务） > ArkTS API > cloudResPrefetch（预加载模块）
category: harmonyos-references
scraped_at: 2026-04-28T08:16:32+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:ee775f8e205a4e609ad2b9867642d013b9295882b5039545f428a77ef2be7dae
---

本模块提供调用预加载的能力。

起始版本：5.0.3(15)

## 导入模块

PhonePC/2in1Tablet

```
1. import { cloudResPrefetch } from '@kit.CloudFoundationKit';
```

## registerPrefetchTask

PhonePC/2in1Tablet

registerPrefetchTask(options: PrefetchOptions): void

注册周期性预加载任务。周期性预加载适用，安装预加载不涉及。在应用启动后，需显式调用本接口，调用成功后才可触发周期性预加载任务。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DeviceCloudGateway.CloudResPrefetch

**起始版本：** 5.0.3(15)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [PrefetchOptions](cloudfoundation-cloudresprefetch.md#prefetchoptions) | 是 | 周期性预加载任务的初始化配置参数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS错误码](errorcode-cloudfoundation.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 1008240009 | Client internal error. |

**示例：**

```
1. import { cloudResPrefetch } from '@kit.CloudFoundationKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. try {
5. cloudResPrefetch.registerPrefetchTask({
6. token: "testToken",
7. params: "testParams"
8. });
9. hilog.info(0x0000, 'testTag', `Succeeded in registering prefetch task`);
10. } catch (err) {
11. hilog.error(0x0000, 'testTag', `Failed to register prefetch task`);
12. }
```

## PrefetchOptions

PhonePC/2in1Tablet

周期性预加载任务初始化配置参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DeviceCloudGateway.CloudResPrefetch

**起始版本：** 5.0.3(15)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| token | string | 否 | 是 | 自定义用户级别的访问令牌。会携带透传至开发者自己的函数中，由开发者自行完成认证。 |
| params | string | Object | 否 | 是 | 自定义参数。会携带透传至开发者自己的函数中，由开发者自行定义并解析。 |

## getPrefetchResult

PhonePC/2in1Tablet

getPrefetchResult(mode: PrefetchMode, callback: AsyncCallback<PrefetchResult>, params?: PrefetchParams): void

获取预加载数据。安装预加载和周期性预加载均适用。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DeviceCloudGateway.CloudResPrefetch

**起始版本：** 5.0.3(15)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [PrefetchMode](cloudfoundation-cloudresprefetch.md#prefetchmode) | 是 | 预加载类型。  **元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。 |
| callback | AsyncCallback<[PrefetchResult](cloudfoundation-cloudresprefetch.md#prefetchresult)> | 是 | 回调函数。当获取预加载数据成功，err为undefined，data为获取到的PrefetchResult；否则为错误对象。  **元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。 |
| params | [PrefetchParams](cloudfoundation-cloudresprefetch.md#prefetchparams) | 否 | 预加载参数。  **起始版本：** 6.1.0(23)  **说明：** 元服务不支持该字段。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS错误码](errorcode-cloudfoundation.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 1008240009 | Client internal error. |

**示例：**

```
1. import { cloudResPrefetch } from '@kit.CloudFoundationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. // 获取安装预加载数据
6. cloudResPrefetch.getPrefetchResult(cloudResPrefetch.PrefetchMode.INSTALL_PREFETCH,
7. (err: BusinessError, data: cloudResPrefetch.PrefetchResult) => {
8. if (err) {
9. hilog.error(0x0000, 'testTag', `Failed to get install prefetch data, code: ${err.code}, message: ${err.message}`);
10. } else {
11. hilog.info(0x0000, 'testTag',
12. `Succeeded in getting install prefetch data, result: ${JSON.stringify(data.result)}`);
13. }
14. });

16. // 获取周期性预加载数据
17. cloudResPrefetch.getPrefetchResult(cloudResPrefetch.PrefetchMode.PERIODIC_PREFETCH,
18. (err: BusinessError, data: cloudResPrefetch.PrefetchResult) => {
19. if (err) {
20. hilog.error(0x0000, 'testTag',
21. `Failed to get periodic prefetch data, code: ${err.code}, message: ${err.message}`);
22. } else {
23. hilog.info(0x0000, 'testTag',
24. `Succeeded in getting periodic prefetch data, result: ${JSON.stringify(data.result)}`);
25. }
26. });

28. // 获取跳链安装预加载数据
29. let params: cloudResPrefetch.PrefetchParams = {
30. link: 'link' // 需要替换为延迟链接
31. }
32. cloudResPrefetch.getPrefetchResult(cloudResPrefetch.PrefetchMode.LINK_PREFETCH,
33. (err: BusinessError, data: cloudResPrefetch.PrefetchResult) => {
34. if (err) {
35. hilog.error(0x0000, 'testTag',
36. `Failed to get link prefetch data, code: ${err.code}, message: ${err.message}`);
37. } else {
38. hilog.info(0x0000, 'testTag',
39. `Succeeded in getting link prefetch data, result: ${JSON.stringify(data.result)}`);
40. }
41. }, params);
```

## getPrefetchResult

PhonePC/2in1Tablet

getPrefetchResult(mode: PrefetchMode, params?: PrefetchParams): Promise<PrefetchResult>

获取预加载数据。安装预加载和周期性预加载均适用。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DeviceCloudGateway.CloudResPrefetch

**起始版本：** 5.0.3(15)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [PrefetchMode](cloudfoundation-cloudresprefetch.md#prefetchmode) | 是 | 预加载类型。  **元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。 |
| params | [PrefetchParams](cloudfoundation-cloudresprefetch.md#prefetchparams) | 否 | 预加载参数。  **起始版本：** 6.1.0(23)  **说明：** 元服务不支持该字段。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PrefetchResult](cloudfoundation-cloudresprefetch.md#prefetchresult)> | Promise对象，返回获取的预加载数据。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS错误码](errorcode-cloudfoundation.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified;  2. Incorrect parameter types;  3. Parameter verification failed. |
| 1008240009 | Client internal error. |

**示例：**

```
1. import { cloudResPrefetch } from '@kit.CloudFoundationKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. // 获取安装预加载数据
6. cloudResPrefetch.getPrefetchResult(cloudResPrefetch.PrefetchMode.INSTALL_PREFETCH)
7. .then((data: cloudResPrefetch.PrefetchResult) => {
8. hilog.info(0x0000, 'testTag', `Succeeded in getting install prefetch data, result: ${JSON.stringify(data.result)}`);
9. })
10. .catch((err: BusinessError) => {
11. hilog.error(0x0000, 'testTag', `Failed to get install prefetch data, code: ${err.code}, message: ${err.message}`);
12. });

14. // 获取周期性预加载数据
15. cloudResPrefetch.getPrefetchResult(cloudResPrefetch.PrefetchMode.PERIODIC_PREFETCH)
16. .then((data: cloudResPrefetch.PrefetchResult) => {
17. hilog.info(0x0000, 'testTag',
18. `Succeeded in getting periodic prefetch data, result: ${JSON.stringify(data.result)}`);
19. })
20. .catch((err: BusinessError) => {
21. hilog.error(0x0000, 'testTag', `Failed to get periodic prefetch data, code: ${err.code}, message: ${err.message}`);
22. });

24. // 获取跳链安装预加载数据
25. let params: cloudResPrefetch.PrefetchParams = {
26. link: 'link' // 需要替换为延迟链接
27. }
28. cloudResPrefetch.getPrefetchResult(cloudResPrefetch.PrefetchMode.LINK_PREFETCH, params)
29. .then((data: cloudResPrefetch.PrefetchResult) => {
30. hilog.info(0x0000, 'testTag',
31. `Succeeded in getting link prefetch data, result: ${JSON.stringify(data.result)}`);
32. })
33. .catch((err: BusinessError) => {
34. hilog.error(0x0000, 'testTag', `Failed to get link prefetch data, code: ${err.code}, message: ${err.message}`);
35. });
```

## PrefetchMode

PhonePC/2in1Tablet

枚举， 预加载类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DeviceCloudGateway.CloudResPrefetch

**起始版本：** 5.0.3(15)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| INSTALL\_PREFETCH | 1 | 安装预加载。  **元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。 |
| PERIODIC\_PREFETCH | 2 | 周期性预加载。  **元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。 |
| LINK\_PREFETCH | 3 | 跳链安装预加载。  **起始版本：** 6.1.0(23)  **说明：** 元服务不支持该字段。 |

## PrefetchParams

PhonePC/2in1Tablet

预加载参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.DeviceCloudGateway.CloudResPrefetch

**起始版本：** 6.1.0(23)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| link | string | 否 | 是 | 跳链安装预加载延迟链接。  **说明：** 元服务不支持该字段。 |

## PrefetchResult

PhonePC/2in1Tablet

获取预加载数据返回的结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DeviceCloudGateway.CloudResPrefetch

**起始版本：** 5.0.3(15)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| result | string | Object | 否 | 否 | 返回的预加载数据，字符串或JSON字符串转换的Object对象。 |
| timestamp | Date | 否 | 否 | 返回的预加载数据时间戳，UTC时间格式。 |
| token | string | 否 | 否 | 返回注册周期性预加载任务时所用的Token。 |
