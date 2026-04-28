---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-time
title: @ohos.systemTime (系统时间、时区)
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > ArkTS API > 已停止维护的接口 > @ohos.systemTime (系统时间、时区)
category: harmonyos-references
scraped_at: 2026-04-28T08:09:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f089d1d9fd193a7b318aa8dfcab4fadb4d9b5caee2418fccf3612f45dce36f6b
---

本模块主要由系统时间和系统时区功能组成。开发者可以设置、获取系统时间及系统时区。

说明

* 从API Version 9 开始，该模块接口不再维护，推荐使用新模块接口[@ohos.systemDateTime (系统时间、时区)](js-apis-date-time.md)。
* 本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { systemTime } from '@kit.BasicServicesKit';
```

## systemTime.getCurrentTime8+(deprecated)

PhonePC/2in1TabletTVWearable

getCurrentTime(isNano: boolean, callback: AsyncCallback<number>): void

获取自Unix纪元以来经过的时间，使用callback异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[systemDateTime.getTime](js-apis-date-time.md#systemdatetimegettime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isNano | boolean | 是 | 返回结果是否为纳秒数。  - true：表示返回结果为纳秒数（ns）。  - false：表示返回结果为毫秒数（ms）。 |
| callback | AsyncCallback<number> | 是 | 回调函数，返回自Unix纪元以来经过的时间。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](errorcode-time.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| -1 | Parameter check failed, permission denied, or system error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. systemTime.getCurrentTime(true, (error: BusinessError, time: number) => {
5. if (error) {
6. console.info(`Failed to get currentTime. message: ${error.message}, code: ${error.code}`);
7. return;
8. }
9. console.info(`Succeeded in getting currentTime: ${time}`);
10. });
11. } catch(e) {
12. let error = e as BusinessError;
13. console.info(`Failed to get currentTime. message: ${error.message}, code: ${error.code}`);
14. }
```

## systemTime.getCurrentTime8+(deprecated)

PhonePC/2in1TabletTVWearable

getCurrentTime(callback: AsyncCallback<number>): void

获取自Unix纪元以来经过的时间，使用callback异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[systemDateTime.getTime](js-apis-date-time.md#systemdatetimegettime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数，返回自Unix纪元以来经过的时间（ms）。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](errorcode-time.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| -1 | Parameter check failed, permission denied, or system error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. systemTime.getCurrentTime((error: BusinessError, time: number) => {
5. if (error) {
6. console.info(`Failed to get currentTime. message: ${error.message}, code: ${error.code}`);
7. return;
8. }
9. console.info(`Succeeded in getting currentTime : ${time}`);
10. });
11. } catch(e) {
12. let error = e as BusinessError;
13. console.info(`Failed to get currentTime. message: ${error.message}, code: ${error.code}`);
14. }
```

## systemTime.getCurrentTime8+(deprecated)

PhonePC/2in1TabletTVWearable

getCurrentTime(isNano?: boolean): Promise<number>

获取自Unix纪元以来经过的时间，使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[systemDateTime.getTime](js-apis-date-time.md#systemdatetimegettime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isNano | boolean | 否 | 返回结果是否为纳秒数，默认值为false。  默认值为false。  - true：表示返回结果为纳秒数（ns）。  - false：表示返回结果为毫秒数（ms）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回自Unix纪元以来经过的时间。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](errorcode-time.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| -1 | Parameter check failed, permission denied, or system error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. systemTime.getCurrentTime().then((time: number) => {
5. console.info(`Succeeded in getting currentTime : ${time}`);
6. }).catch((error: BusinessError) => {
7. console.info(`Failed to get currentTime. message: ${error.message}, code: ${error.code}`);
8. });
9. } catch(e) {
10. let error = e as BusinessError;
11. console.info(`Failed to get currentTime. message: ${error.message}, code: ${error.code}`);
12. }
```

## systemTime.getRealActiveTime8+(deprecated)

PhonePC/2in1TabletTVWearable

getRealActiveTime(isNano: boolean, callback: AsyncCallback<number>): void

获取自系统启动以来经过的时间，不包括深度睡眠时间，使用callback异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[systemDateTime.getUptime](js-apis-date-time.md#systemdatetimegetuptime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isNano | boolean | 是 | 返回结果是否为纳秒数。  - true：表示返回结果为纳秒数（ns）。  - false：表示返回结果为毫秒数（ms）。 |
| callback | AsyncCallback<number> | 是 | 回调函数，返回自系统启动以来经过的时间，不包括深度睡眠时间。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](errorcode-time.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| -1 | Parameter check failed, permission denied, or system error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. systemTime.getRealActiveTime(true, (error: BusinessError, time: number) => {
5. if (error) {
6. console.info(`Failed to get real active time. message: ${error.message}, code: ${error.code}`);
7. return;
8. }
9. console.info(`Succeeded in getting real active time : ${time}`);
10. });
11. } catch(e) {
12. let error = e as BusinessError;
13. console.info(`Failed to get real active time. message: ${error.message}, code: ${error.code}`);
14. }
```

## systemTime.getRealActiveTime8+(deprecated)

PhonePC/2in1TabletTVWearable

getRealActiveTime(callback: AsyncCallback<number>): void

获取自系统启动以来经过的时间，不包括深度睡眠时间，使用callback异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[systemDateTime.getUptime](js-apis-date-time.md#systemdatetimegetuptime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数，返回自系统启动以来经过的时间（ms），不包括深度睡眠时间。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](errorcode-time.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| -1 | Parameter check failed, permission denied, or system error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. systemTime.getRealActiveTime((error: BusinessError, time: number) => {
5. if (error) {
6. console.info(`Failed to get real active time. message: ${error.message}, code: ${error.code}`);
7. return;
8. }
9. console.info(`Succeeded in getting real active time : ${time}`);
10. });
11. } catch(e) {
12. let error = e as BusinessError;
13. console.info(`Failed to get real active time. message: ${error.message}, code: ${error.code}`);
14. }
```

## systemTime.getRealActiveTime8+(deprecated)

PhonePC/2in1TabletTVWearable

getRealActiveTime(isNano?: boolean): Promise<number>

获取自系统启动以来经过的时间，不包括深度睡眠时间，使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[systemDateTime.getUptime](js-apis-date-time.md#systemdatetimegetuptime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isNano | boolean | 否 | 返回结果是否为纳秒数，默认值为false。  - true：表示返回结果为纳秒数（ns）。  - false：表示返回结果为毫秒数（ms）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回自系统启动以来经过的时间，但不包括深度睡眠时间。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](errorcode-time.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| -1 | Parameter check failed, permission denied, or system error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. systemTime.getRealActiveTime().then((time: number) => {
5. console.info(`Succeeded in getting real active time : ${time}`);
6. }).catch((error: BusinessError) => {
7. console.info(`Failed to get real active time. message: ${error.message}, code: ${error.code}`);
8. });
9. } catch(e) {
10. let error = e as BusinessError;
11. console.info(`Failed to get real active time. message: ${error.message}, code: ${error.code}`);
12. }
```

## systemTime.getRealTime8+(deprecated)

PhonePC/2in1TabletTVWearable

getRealTime(isNano: boolean, callback: AsyncCallback<number>): void

获取自系统启动以来经过的时间，包括深度睡眠时间，使用callback异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[systemDateTime.getUptime](js-apis-date-time.md#systemdatetimegetuptime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isNano | boolean | 是 | 返回结果是否为纳秒数。  - true：表示返回结果为纳秒数（ns）。  - false：表示返回结果为毫秒数（ms）。 |
| callback | AsyncCallback<number> | 是 | 回调函数，返回自系统启动以来经过的时间，包括深度睡眠时间。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](errorcode-time.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| -1 | Parameter check failed, permission denied, or system error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. systemTime.getRealTime(true, (error: BusinessError, time: number) => {
5. if (error) {
6. console.info(`Failed to get real time. message: ${error.message}, code: ${error.code}`);
7. return;
8. }
9. console.info(`Succeeded in getting real time : ${time}`);
10. });
11. } catch(e) {
12. let error = e as BusinessError;
13. console.info(`Failed to get real time. message: ${error.message}, code: ${error.code}`);
14. }
```

## systemTime.getRealTime8+(deprecated)

PhonePC/2in1TabletTVWearable

getRealTime(callback: AsyncCallback<number>): void

获取自系统启动以来经过的时间，包括深度睡眠时间，使用callback异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[systemDateTime.getUptime](js-apis-date-time.md#systemdatetimegetuptime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数，返回自系统启动以来经过的时间（ms），包括深度睡眠时间。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](errorcode-time.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| -1 | Parameter check failed, permission denied, or system error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. systemTime.getRealTime((error: BusinessError, time: number) => {
5. if (error) {
6. console.info(`Failed to get real time. message: ${error.message}, code: ${error.code}`);
7. return;
8. }
9. console.info(`Succeeded in getting real time : ${time}`);
10. });
11. } catch(e) {
12. let error = e as BusinessError;
13. console.info(`Failed to get real time. message: ${error.message}, code: ${error.code}`);
14. }
```

## systemTime.getRealTime8+(deprecated)

PhonePC/2in1TabletTVWearable

getRealTime(isNano?: boolean): Promise<number>

获取自系统启动以来经过的时间，包括深度睡眠时间，使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[systemDateTime.getUptime](js-apis-date-time.md#systemdatetimegetuptime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isNano | boolean | 否 | 返回结果是否为纳秒数，默认值为false。  默认值为false。  - true：表示返回结果为纳秒数（ns）。  - false：表示返回结果为毫秒数（ms）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回自系统启动以来经过的时间，包括深度睡眠时间。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](errorcode-time.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| -1 | Parameter check failed, permission denied, or system error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. systemTime.getRealTime().then((time: number) => {
5. console.info(`Succeeded in getting real time : ${time}`);
6. }).catch((error: BusinessError) => {
7. console.info(`Failed to get real time. message: ${error.message}, code: ${error.code}`);
8. });
9. } catch(e) {
10. let error = e as BusinessError;
11. console.info(`Failed to get real time. message: ${error.message}, code: ${error.code}`);
12. }
```

## systemTime.getDate8+(deprecated)

PhonePC/2in1TabletTVWearable

getDate(callback: AsyncCallback<Date>): void

获取当前系统日期，使用callback异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[如何将时间格式的字符串string转换为Date对象](https://gitcode.com/openharmony/docs/blob/master/zh-cn/application-dev/faqs/faqs-arkui-arkts.md#如何将时间格式的字符串string转换为date对象api-9)中的new Date()方法替代，new Date()返回Date实例对象。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Date> | 是 | 回调函数，返回当前系统日期。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](errorcode-time.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| -1 | Parameter check failed, permission denied, or system error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. systemTime.getDate((error: BusinessError, date: Date) => {
5. if (error) {
6. console.info(`Failed to get date. message: ${error.message}, code: ${error.code}`);
7. return;
8. }
9. console.info(`Succeeded in getting date : ${date}`);
10. });
11. } catch(e) {
12. let error = e as BusinessError;
13. console.info(`Failed to get date. message: ${error.message}, code: ${error.code}`);
14. }
```

## systemTime.getDate8+(deprecated)

PhonePC/2in1TabletTVWearable

getDate(): Promise<Date>

获取当前系统日期，使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[如何将时间格式的字符串string转换为Date对象](https://gitcode.com/openharmony/docs/blob/master/zh-cn/application-dev/faqs/faqs-arkui-arkts.md#如何将时间格式的字符串string转换为date对象api-9)中的new Date()方法替代，new Date()返回Date实例对象。

**系统能力：** SystemCapability.MiscServices.Time

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Date> | Promise对象，返回当前系统日期。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](errorcode-time.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| -1 | Parameter check failed, permission denied, or system error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. systemTime.getDate().then((date: Date) => {
5. console.info(`Succeeded in getting date : ${date}`);
6. }).catch((error: BusinessError) => {
7. console.info(`Failed to get date. message: ${error.message}, code: ${error.code}`);
8. });
9. } catch(e) {
10. let error = e as BusinessError;
11. console.info(`Failed to get date. message: ${error.message}, code: ${error.code}`);
12. }
```

## systemTime.getTimezone8+(deprecated)

PhonePC/2in1TabletTVWearable

getTimezone(callback: AsyncCallback<string>): void

获取系统时区，使用callback异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[systemDateTime.getTimezone](js-apis-date-time.md#systemdatetimegettimezone)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<string> | 是 | 回调函数，返回系统时区。具体可见[支持的系统时区](js-apis-system-time.md#支持的系统时区) 。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](errorcode-time.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| -1 | Parameter check failed, permission denied, or system error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. systemTime.getTimezone((error: BusinessError, data: string) => {
5. if (error) {
6. console.info(`Failed to get timezone. message: ${error.message}, code: ${error.code}`);
7. return;
8. }
9. console.info(`Succeeded in getting timezone : ${data}`);
10. });
11. } catch(e) {
12. let error = e as BusinessError;
13. console.info(`Failed to get timezone. message: ${error.message}, code: ${error.code}`);
14. }
```

## systemTime.getTimezone8+(deprecated)

PhonePC/2in1TabletTVWearable

getTimezone(): Promise<string>

获取系统时区，使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃。建议使用[systemDateTime.getTimezone](js-apis-date-time.md#systemdatetimegettimezone-1)替代。

**系统能力：** SystemCapability.MiscServices.Time

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回系统时区。具体可见[支持的系统时区](js-apis-system-time.md#支持的系统时区) 。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](errorcode-time.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| -1 | Parameter check failed, permission denied, or system error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. systemTime.getTimezone().then((data: string) => {
5. console.info(`Succeeded in getting timezone: ${data}`);
6. }).catch((error: BusinessError) => {
7. console.info(`Failed to get timezone. message: ${error.message}, code: ${error.code}`);
8. });
9. } catch(e) {
10. let error = e as BusinessError;
11. console.info(`Failed to get timezone. message: ${error.message}, code: ${error.code}`);
12. }
```

## systemTime.setTime(deprecated)

PhonePC/2in1TabletTVWearable

setTime(time : number, callback : AsyncCallback<void>) : void

设置系统时间，使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。

**需要权限：** ohos.permission.SET\_TIME

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| time | number | 是 | 目标时间戳（ms）。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](errorcode-time.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| -1 | Parameter check failed, permission denied, or system error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // time对应的时间为2021-01-20 02:36:25
4. let time = 1611081385000;
5. try {
6. systemTime.setTime(time, (error: BusinessError) => {
7. if (error) {
8. console.info(`Failed to set time. message: ${error.message}, code: ${error.code}`);
9. return;
10. }
11. console.info(`Succeeded in setting time`);
12. });
13. } catch(e) {
14. let error = e as BusinessError;
15. console.info(`Failed to set time. message: ${error.message}, code: ${error.code}`);
16. }
```

## systemTime.setTime(deprecated)

PhonePC/2in1TabletTVWearable

setTime(time : number) : Promise<void>

设置系统时间，使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。

**需要权限：** ohos.permission.SET\_TIME

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| time | number | 是 | 目标时间戳（ms）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](errorcode-time.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| -1 | Parameter check failed, permission denied, or system error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. // time对应的时间为2021-01-20 02:36:25
4. let time = 1611081385000;
5. try {
6. systemTime.setTime(time).then(() => {
7. console.info(`Succeeded in setting time.`);
8. }).catch((error: BusinessError) => {
9. console.info(`Failed to set time. message: ${error.message}, code: ${error.code}`);
10. });
11. } catch(e) {
12. let error = e as BusinessError;
13. console.info(`Failed to set time. message: ${error.message}, code: ${error.code}`);
14. }
```

## systemTime.setDate(deprecated)

PhonePC/2in1TabletTVWearable

setDate(date: Date, callback: AsyncCallback<void>): void

设置系统日期，使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。

**需要权限：** ohos.permission.SET\_TIME

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| date | Date | 是 | 目标日期。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](errorcode-time.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| -1 | Parameter check failed, permission denied, or system error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let date = new Date();
4. try {
5. systemTime.setDate(date, (error: BusinessError) => {
6. if (error) {
7. console.info(`Failed to set date. message: ${error.message}, code: ${error.code}`);
8. return;
9. }
10. console.info(`Succeeded in setting date.`);
11. });
12. } catch(e) {
13. let error = e as BusinessError;
14. console.info(`Failed to set date. message: ${error.message}, code: ${error.code}`);
15. }
```

## systemTime.setDate(deprecated)

PhonePC/2in1TabletTVWearable

setDate(date: Date): Promise<void>

设置系统日期，使用Promise异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。

**需要权限：** ohos.permission.SET\_TIME

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| date | Date | 是 | 目标日期。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](errorcode-time.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| -1 | Parameter check failed, permission denied, or system error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let date = new Date();
4. try {
5. systemTime.setDate(date).then(() => {
6. console.info(`Succeeded in setting date.`);
7. }).catch((error: BusinessError) => {
8. console.info(`Failed to set date. message: ${error.message}, code: ${error.code}`);
9. });
10. } catch(e) {
11. let error = e as BusinessError;
12. console.info(`Failed to set date. message: ${error.message}, code: ${error.code}`);
13. }
```

## systemTime.setTimezone(deprecated)

PhonePC/2in1TabletTVWearable

setTimezone(timezone: string, callback: AsyncCallback<void>): void

设置系统时区，使用callback异步回调。

说明

从API version 7开始支持，从API version 9开始废弃。

**需要权限：** ohos.permission.SET\_TIME\_ZONE

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timezone | string | 是 | 系统时区。具体可见[支持的系统时区](js-apis-system-time.md#支持的系统时区) 。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](errorcode-time.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| -1 | Parameter check failed, permission denied, or system error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. systemTime.setTimezone('Asia/Shanghai', (error: BusinessError) => {
5. if (error) {
6. console.info(`Failed to set timezone. message: ${error.message}, code: ${error.code}`);
7. return;
8. }
9. console.info(`Succeeded in setting timezone.`);
10. });
11. } catch(e) {
12. let error = e as BusinessError;
13. console.info(`Failed to set timezone. message: ${error.message}, code: ${error.code}`);
14. }
```

## systemTime.setTimezone(deprecated)

PhonePC/2in1TabletTVWearable

setTimezone(timezone: string): Promise<void>

使用Promise异步回调设置系统时区。

说明

从API version 7开始支持，从API version 9开始废弃。

**需要权限：** ohos.permission.SET\_TIME\_ZONE

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timezone | string | 是 | 系统时区。具体可见[支持的系统时区](js-apis-system-time.md#支持的系统时区) 。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](errorcode-time.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| -1 | Parameter check failed, permission denied, or system error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. try {
4. systemTime.setTimezone('Asia/Shanghai').then(() => {
5. console.info(`Succeeded in setting timezone.`);
6. }).catch((error: BusinessError) => {
7. console.info(`Failed to set timezone. message: ${error.message}, code: ${error.code}`);
8. });
9. } catch(e) {
10. let error = e as BusinessError;
11. console.info(`Failed to set timezone. message: ${error.message}, code: ${error.code}`);
12. }
```

## 支持的系统时区

PhonePC/2in1TabletTVWearable

支持的系统时区及各时区与0时区相比的偏移量（单位：h）可见下表。

| 时区 | 偏移量 |
| --- | --- |
| Antarctica/McMurdo | 12 |
| America/Argentina/Buenos\_Aires | -3 |
| Australia/Sydney | 10 |
| America/Noronha | -2 |
| America/St\_Johns | -3 |
| Africa/Kinshasa | 1 |
| America/Santiago | -3 |
| Asia/Shanghai | 8 |
| Asia/Nicosia | 3 |
| Europe/Berlin | 2 |
| America/Guayaquil | -5 |
| Europe/Madrid | 2 |
| Pacific/Pohnpei | 11 |
| America/Godthab | -2 |
| Asia/Jakarta | 7 |
| Pacific/Tarawa | 12 |
| Asia/Almaty | 6 |
| Pacific/Majuro | 12 |
| Asia/Ulaanbaatar | 8 |
| America/Mexico\_City | -5 |
| Asia/Kuala\_Lumpur | 8 |
| Pacific/Auckland | 12 |
| Pacific/Tahiti | -10 |
| Pacific/Port\_Moresby | 10 |
| Asia/Gaza | 3 |
| Europe/Lisbon | 1 |
| Europe/Moscow | 3 |
| Europe/Kiev | 3 |
| Pacific/Wake | 12 |
| America/New\_York | -4 |
| Asia/Tashkent | 5 |
