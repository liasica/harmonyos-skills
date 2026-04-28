---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cloudfoundation-cloudcommon
title: cloudCommon (公共模块)
breadcrumb: API参考 > 应用服务 > Cloud Foundation Kit（云开发服务） > ArkTS API > cloudCommon (公共模块)
category: harmonyos-references
scraped_at: 2026-04-28T08:16:31+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b48b1adb88a066ff410c3939e7f63859e19917cdce84303af654f8a5453749bd
---

本模块提供初始化云开发服务的能力。

**起始版本：** 5.0.0(12)

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { cloudCommon } from '@kit.CloudFoundationKit';
```

## cloudCommon.init

PhonePC/2in1TabletTVWearable

init(options?: CloudOptions): void

初始化云开发服务。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [CloudOptions](cloudfoundation-cloudcommon.md#cloudoptions) | 否 | 设置初始化参数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |

**示例**：

说明

云函数业务免鉴权，开发云函数无需获取用户凭据。开发云存储或云数据库业务则需要获取用户凭据。获取用户凭据有两种方式，以下代码仅以通过AGC认证服务SDK获取为例，更多信息可参考[AuthProvider](cloudfoundation-cloudcommon.md#authprovider)。

```
1. import { cloudCommon } from '@kit.CloudFoundationKit';
2. import { request } from '@kit.BasicServicesKit';
3. import auth from '@hw-agconnect/auth';

5. let provider = auth.getAuthProvider(); // 在用户登录成功的情况下调用此方法获取authProvider
6. cloudCommon.init({
7. region: cloudCommon.CloudRegion.CHINA,
8. authProvider: provider,
9. functionOptions: { timeout: 10 * 1000 },
10. storageOptions: { mode: request.agent.Mode.BACKGROUND, network: request.agent.Network.ANY },
11. databaseOptions: { schema: "schema.json", traceId: "traceId" }
12. })
```

## CloudOptions

PhonePC/2in1TabletTVWearable

初始化选项。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| region | [CloudRegion](cloudfoundation-cloudcommon.md#cloudregion) | 否 | 是 | 存储地，默认为CHINA。 |
| authProvider | [AuthProvider](cloudfoundation-cloudcommon.md#authprovider) | 否 | 是 | 认证提供方。 |
| functionOptions | [FunctionOptions](cloudfoundation-cloudcommon.md#functionoptions) | 否 | 是 | 云函数初始化设置。 |
| storageOptions | [StorageOptions](cloudfoundation-cloudcommon.md#storageoptions) | 否 | 是 | 云存储初始化设置。 |
| databaseOptions | [DatabaseOptions](cloudfoundation-cloudcommon.md#databaseoptions) | 否 | 是 | 云数据库初始化设置。 |

## CloudRegion

PhonePC/2in1TabletTVWearable

枚举， 存储地类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CHINA | 0 | 数据存储到中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。 |
| GERMANY | 1 | 数据存储到德国区。 |
| RUSSIA | 2 | 数据存储到俄罗斯。 |
| SINGAPORE | 3 | 数据存储到新加坡。 |

## AuthProvider

PhonePC/2in1TabletTVWearable

认证提供方。开发者可以使用[AGC认证服务SDK](../app/agc-help-auth-introduction-0000002271496181.md)获取AuthProvider，或者使用华为账号服务Access Token接口自定义AuthProvider。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：** 5.0.0(12)

### getAccessToken

PhonePC/2in1TabletTVWearable

getAccessToken(isForceRefresh: boolean): Promise<string>

获取用户凭据。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isForceRefresh | boolean | 是 | 是否需要强制刷新返回用户凭据。true表示需要，false表示不需要。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回用户凭据（该用户凭据可使用AGC认证服务SDK或华为账号服务的获取用户级凭证接口生成）。 |

**示例：**

* （推荐）方式一：使用AGC认证服务SDK获取AuthProvider（SDK会主动调用getAccessToken方法，无需开发者操作）

  1. 在应用级（一般为entry目录下）“oh-package.json5”文件里面添加认证服务SDK依赖。

     ```
     1. "dependencies": {
     2. "@hw-agconnect/auth": "^1.0.5"
     3. }
     ```
  2. 使用手机、邮箱或华为账号进行[登录认证](../app/agc-help-auth-login-phone-0000002271416141.md)。
  3. 认证成功后获取AuthProvider。

     ```
     1. import { cloudCommon } from '@kit.CloudFoundationKit';
     2. import auth from '@hw-agconnect/auth';
     3. import { request } from '@kit.BasicServicesKit';

     5. let authProvider = auth.getAuthProvider();
     6. cloudCommon.init({
     7. region: cloudCommon.CloudRegion.CHINA,
     8. authProvider: authProvider,
     9. functionOptions: { timeout: 10 * 1000 },
     10. storageOptions: { mode: request.agent.Mode.BACKGROUND, network: request.agent.Network.ANY },
     11. databaseOptions: { schema: "schema.json", traceId: "traceId" }
     12. })
     ```
* 方式二：

  1. 使用华为账号服务的[获取用户级凭证](account-api-obtain-user-token.md)接口获取refresh\_token，然后基于refresh\_token换取access\_token自定义AuthProvider。可参考如下示例代码换取：

     ```
     1. import { cloudCommon } from '@kit.CloudFoundationKit';
     2. import { http } from '@kit.NetworkKit';
     3. import { hilog } from '@kit.PerformanceAnalysisKit';

     5. let accessToken = '';

     7. export class MyAuthProvider implements cloudCommon.AuthProvider {
     8. async getAccessToken(isForceRefresh: boolean): Promise<string> {
     9. let data =
     10. "grant_type=refresh_token&client_id=xxxx&client_secret=xxxx&refresh_token=";
     11. let refreshToken =
     12. encodeURIComponent('xxxx'); // xxxx为使用华为账号服务获取用户级凭证接口获取的refresh_token
     13. // access_token过期则强制刷新
     14. if (isForceRefresh) {
     15. data = data + refreshToken;
     16. try {
     17. let httpRequest = http.createHttp();
     18. let ohosOptions: http.HttpRequestOptions = {
     19. method: http.RequestMethod.POST,
     20. header: {
     21. 'Content-Type': 'application/x-www-form-urlencoded'
     22. },
     23. extraData: data,
     24. };
     25. let url = "https://oauth-login.cloud.huawei.com/oauth2/v3/token";
     26. let resp = await httpRequest.request(url, ohosOptions);
     27. accessToken = JSON.parse(resp.result.toString()).access_token;
     28. } catch (err) {
     29. hilog.error(0x0000, 'testTag', `Failed to get accessToken, code: ${err.code}, message: ${err.message}`);
     30. }
     31. }
     32. return Promise.resolve(accessToken);
     33. }
     34. }
     ```
  2. 使用自定义的AuthProvider完成初始化。

     ```
     1. import { cloudCommon } from '@kit.CloudFoundationKit';
     2. import { request } from '@kit.BasicServicesKit';
     3. import { MyAuthProvider } from 'xxx'; // xxx为您自定义的AuthProvider文件路径

     5. let authProvider = new MyAuthProvider();
     6. cloudCommon.init({
     7. region: cloudCommon.CloudRegion.CHINA, // 请填写实际数据处理位置
     8. authProvider: authProvider,
     9. functionOptions: { timeout: 10 * 1000 },
     10. storageOptions: { mode: request.agent.Mode.BACKGROUND, network: request.agent.Network.ANY },
     11. databaseOptions: { schema: "schema.json", traceId: "traceId" }
     12. })
     ```

## FunctionOptions

PhonePC/2in1TabletTVWearable

云函数初始化配置参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| timeout | number | 否 | 是 | 函数请求超时时间，单位毫秒，默认为70\*1000毫秒。  取值范围无限制，会转成unsigned long类型。 |

## StorageOptions

PhonePC/2in1TabletTVWearable

云存储初始化配置参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| mode | [request.agent.Mode](js-apis-request.md#requestagentmode10) | 否 | 是 | 任务的模式。前端任务在应用切换到后台一段时间后失败/暂停；后台任务不受影响。默认为BACKGROUND。  - BACKGROUND：后台任务。  - FOREGROUND：前端任务。 |
| network | [request.agent.Network](js-apis-request.md#requestagentnetwork10) | 否 | 是 | 使用的网络类型。网络不满足设置条件时，未执行的任务等待执行，执行中的任务失败/暂停。默认为Network.ANY。  - Network.ANY：不限网络类型。  - Network.WIFI：无线网络。  - Network.CELLULAR：蜂窝数据网络。 |

## DatabaseOptions

PhonePC/2in1TabletTVWearable

云数据库初始化配置参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DeviceCloudGateway.CloudFoundation

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| schema | string | 否 | 是 | 全量数据表结构及权限定义，使用从云端下载的schema.json配置文件，默认读取工程固定目录：rawfile。 |
| traceId | string | 否 | 是 | 用户自定义的traceId，用于跟踪请求操作。  自定义traceId的长度必须大于或等于1个字符，小于或等于32个字符，只能包含以下2种类型：  - 字母（a-f）  - 数字（0-9）  默认值为空。 |
