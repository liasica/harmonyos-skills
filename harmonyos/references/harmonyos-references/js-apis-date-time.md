---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-date-time
title: "@ohos.systemDateTime (系统时间、时区)"
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > ArkTS API > 其他 > @ohos.systemDateTime (系统时间、时区)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:04+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:16df30c843bdf23defe516235982cb1577c145174735c16832b374b03ad3ec66
---

本模块主要由系统时间和系统时区功能组成。开发者可以获取系统时间（含Unix纪元时间和系统启动时间）、系统日期、系统时区及自动设置时间开关状态，支持同步和异步两种获取方式，适用于需要在应用中展示当前时间、进行时间计算或处理时区相关业务的场景。

**说明** 

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { systemDateTime } from '@kit.BasicServicesKit';
```

## TimeType10+

定义获取时间的枚举类型。

**系统能力：** SystemCapability.MiscServices.Time

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STARTUP | 0 | 自系统启动以来经过的时间，包括深度睡眠时间。 |
| ACTIVE | 1 | 自系统启动以来经过的时间，不包括深度睡眠时间。 |

## systemDateTime.getCurrentTime(deprecated)

getCurrentTime(isNano: boolean, callback: AsyncCallback<number>): void

获取自Unix纪元以来经过的时间，使用callback异步回调。

**说明** 

从API version 9开始支持，从API version 12开始废弃。建议使用[systemDateTime.getTime10+](js-apis-date-time.md#systemdatetimegettime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isNano | boolean | 是 | 返回结果是否为纳秒数。  - true：表示返回结果为纳秒数（ns）。  - false：表示返回结果为毫秒数（ms）。 |
| callback | AsyncCallback<number> | 是 | 回调函数，返回自Unix纪元以来经过的时间戳。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Incorrect parameter types. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getCurrentTime(true, (error: BusinessError, time: number) => {
    if (error) {
      console.error(`Failed to get currentTime. Code: ${error.code}, message: ${error.message}`);
      return;
    }
    console.info(`Succeeded in getting currentTime : ${time}`);
  });
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to get currentTime. Code: ${error.code}, message: ${error.message}`);
}
```

## systemDateTime.getCurrentTime(deprecated)

getCurrentTime(callback: AsyncCallback<number>): void

获取自Unix纪元以来经过的时间，使用callback异步回调。

**说明** 

从API version 9开始支持，从API version 12开始废弃。建议使用[systemDateTime.getTime10+](js-apis-date-time.md#systemdatetimegettime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数，返回自Unix纪元以来经过的时间戳（ms）。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Incorrect parameter types. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getCurrentTime((error: BusinessError, time: number) => {
    if (error) {
      console.error(`Failed to get currentTime. Code: ${error.code}, message: ${error.message}`);
      return;
    }
    console.info(`Succeeded in getting currentTime : ${time}`);
  });
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to get currentTime. Code: ${error.code}, message: ${error.message}`);
}
```

## systemDateTime.getCurrentTime(deprecated)

getCurrentTime(isNano?: boolean): Promise<number>

获取自Unix纪元以来经过的时间，使用Promise异步回调。

**说明** 

从API version 9开始支持，从API version 12开始废弃。建议使用[systemDateTime.getTime10+](js-apis-date-time.md#systemdatetimegettime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isNano | boolean | 否 | 返回结果是否为纳秒数，默认值为false。  - true：表示返回结果为纳秒数（ns）。  - false：表示返回结果为毫秒数（ms）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回自Unix纪元以来经过的时间戳。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Incorrect parameter types. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getCurrentTime().then((time: number) => {
    console.info(`Succeeded in getting currentTime : ${time}`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to get currentTime. Code: ${error.code}, message: ${error.message}`);
  });
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to get currentTime. Code: ${error.code}, message: ${error.message}`);
}
```

## systemDateTime.getRealActiveTime(deprecated)

getRealActiveTime(isNano: boolean, callback: AsyncCallback<number>): void

获取自系统启动以来经过的时间，不包括深度睡眠时间，使用callback异步回调。

**说明** 

从API version 9开始支持，从API version 12开始废弃。建议使用[systemDateTime.getUptime10+](js-apis-date-time.md#systemdatetimegetuptime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isNano | boolean | 是 | 返回结果是否为纳秒数。  - true：表示返回结果为纳秒数（ns）。  - false：表示返回结果为毫秒数（ms）。 |
| callback | AsyncCallback<number> | 是 | 回调函数，返回自系统启动以来经过的时间，但不包括深度睡眠时间。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Incorrect parameter types. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getRealActiveTime(true, (error: BusinessError, time: number) => {
    if (error) {
      console.error(`Failed to get real active time. Code: ${error.code}, message: ${error.message}`);
      return;
    }
    console.info(`Succeeded in getting real active time : ${time}`);
  });
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to get real active time. Code: ${error.code}, message: ${error.message}`);
}
```

## systemDateTime.getRealActiveTime(deprecated)

getRealActiveTime(callback: AsyncCallback<number>): void

获取自系统启动以来经过的时间，不包括深度睡眠时间，使用callback异步回调。

**说明** 

从API version 9开始支持，从API version 12开始废弃。建议使用[systemDateTime.getUptime10+](js-apis-date-time.md#systemdatetimegetuptime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数，返回自系统启动以来经过的时间（ms），但不包括深度睡眠时间。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Incorrect parameter types. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getRealActiveTime((error: BusinessError, time: number) => {
    if (error) {
      console.error(`Failed to get real active time. Code: ${error.code}, message: ${error.message}`);
      return;
    }
    console.info(`Succeeded in getting real active time : ${time}`);
  });
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to get real active time. Code: ${error.code}, message: ${error.message}`);
}
```

## systemDateTime.getRealActiveTime(deprecated)

getRealActiveTime(isNano?: boolean): Promise<number>

获取自系统启动以来经过的时间，不包括深度睡眠时间，使用Promise异步回调。

**说明** 

从API version 9开始支持，从API version 12开始废弃。建议使用[systemDateTime.getUptime10+](js-apis-date-time.md#systemdatetimegetuptime10)替代。

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

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Incorrect parameter types. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getRealActiveTime().then((time: number) => {
    console.info(`Succeeded in getting real active time : ${time}`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to get real active time. Code: ${error.code}, message: ${error.message}`);
  });
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to get real active time. Code: ${error.code}, message: ${error.message}`);
}
```

## systemDateTime.getRealTime(deprecated)

getRealTime(isNano: boolean, callback: AsyncCallback<number>): void

获取自系统启动以来经过的时间，包括深度睡眠时间，使用callback异步回调。

**说明** 

从API version 9开始支持，从API version 12开始废弃。建议使用[systemDateTime.getUptime10+](js-apis-date-time.md#systemdatetimegetuptime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isNano | boolean | 是 | 返回结果是否为纳秒数。  - true：表示返回结果为纳秒数（ns）。  - false：表示返回结果为毫秒数（ms）。 |
| callback | AsyncCallback<number> | 是 | 回调函数，返回自系统启动以来经过的时间，包括深度睡眠时间。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Incorrect parameter types. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getRealTime(true, (error: BusinessError, time: number) => {
    if (error) {
      console.error(`Failed to get real time. Code: ${error.code}, message: ${error.message}`);
      return;
    }
    console.info(`Succeeded in getting real time : ${time}`);
  });
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to get real time. Code: ${error.code}, message: ${error.message}`);
}
```

## systemDateTime.getRealTime(deprecated)

getRealTime(callback: AsyncCallback<number>): void

获取自系统启动以来经过的时间，包括深度睡眠时间，使用callback异步回调。

**说明** 

从API version 9开始支持，从API version 12开始废弃。建议使用[systemDateTime.getUptime10+](js-apis-date-time.md#systemdatetimegetuptime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数，返回自系统启动以来经过的时间（ms），包括深度睡眠时间。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Incorrect parameter types. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getRealTime((error: BusinessError, time: number) => {
    if (error) {
      console.error(`Failed to get real time. Code: ${error.code}, message: ${error.message}`);
      return;
    }
    console.info(`Succeeded in getting real time : ${time}`);
  });
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to get real time. Code: ${error.code}, message: ${error.message}`);
}
```

## systemDateTime.getRealTime(deprecated)

getRealTime(isNano?: boolean): Promise<number>

获取自系统启动以来经过的时间，包括深度睡眠时间，使用Promise异步回调。

**说明** 

从API version 9开始支持，从API version 12开始废弃。建议使用[systemDateTime.getUptime10+](js-apis-date-time.md#systemdatetimegetuptime10)替代。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isNano | boolean | 否 | 返回结果是否为纳秒数，默认值为false。  - true：表示返回结果为纳秒数（ns）。  - false：表示返回结果为毫秒数（ms）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回自系统启动以来经过的时间，包括深度睡眠时间。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Incorrect parameter types. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getRealTime().then((time: number) => {
    console.info(`Succeeded in getting real time : ${time}`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to get real time. Code: ${error.code}, message: ${error.message}`);
  });
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to get real time. Code: ${error.code}, message: ${error.message}`);
}
```

## systemDateTime.getTime10+

getTime(isNanoseconds?: boolean): number

获取自Unix纪元以来到当前系统时间所经过的时间，使用同步方式。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isNanoseconds | boolean | 否 | 返回结果是否为纳秒数。  - true：表示返回结果为纳秒数（ns）。  - false：表示返回结果为毫秒数（ms）。  默认值为false。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 自Unix纪元以来到当前系统时间所经过的时间。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let time: number = systemDateTime.getTime(true);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to get time. Code: ${error.code}, message: ${error.message}`);
}
```

## systemDateTime.getUptime10+

getUptime(timeType: TimeType, isNanoseconds?: boolean): number

使用同步方式获取自系统启动以来经过的时间。可根据TimeType选择获取包含深度睡眠时间的总启动时长（STARTUP，适用于统计设备总运行时长等场景）或不包含深度睡眠时间的活跃运行时长（ACTIVE，适用于性能监控、活跃时长统计等场景）。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timeType | [TimeType](js-apis-date-time.md#timetype10) | 是 | 获取时间的类型，仅能为STARTUP或者ACTIVE。 |
| isNanoseconds | boolean | 否 | 返回结果是否为纳秒数。  - true：表示返回结果为纳秒数（ns）。  - false：表示返回结果为毫秒数（ms）。  默认值为false。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 自系统启动以来经过的时间。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification  failed.This error code was added due to missing issues.  适用版本：12+ |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let time: number = systemDateTime.getUptime(systemDateTime.TimeType.ACTIVE, false);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to get uptime. Code: ${error.code}, message: ${error.message}`);
}
```

## systemDateTime.getDate(deprecated)

getDate(callback: AsyncCallback<Date>): void

获取当前系统日期，使用callback异步回调。

**说明** 

从API version 9开始支持，从API version 10开始废弃。建议使用new Date()方法替代（详见“如何将时间格式的字符串string转换为Date对象“文档），new Date()返回Date实例对象。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Date> | 是 | 回调函数，返回当前系统日期。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.System error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getDate((error: BusinessError, date: Date) => {
    if (error) {
      console.error(`Failed to get date. Code: ${error.code}, message: ${error.message}`);
      return;
    }
    console.info(`Succeeded in getting date : ${date}`);
  });
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to get date. Code: ${error.code}, message: ${error.message}`);
}
```

## systemDateTime.getDate(deprecated)

getDate(): Promise<Date>

获取当前系统日期，使用Promise异步回调。

**说明** 

从API version 9开始支持，从API version 10开始废弃。建议使用new Date()方法替代（详见“如何将时间格式的字符串string转换为Date对象“文档），new Date()返回Date实例对象。

**系统能力：** SystemCapability.MiscServices.Time

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Date> | Promise对象，返回当前系统日期。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.System error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getDate().then((date: Date) => {
    console.info(`Succeeded in getting date : ${date}`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to get date. Code: ${error.code}, message: ${error.message}`);
  });
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to get date. Code: ${error.code}, message: ${error.message}`);
}
```

## systemDateTime.getTimezone

getTimezone(callback: AsyncCallback<string>): void

获取系统时区，使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.Time

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<string> | 是 | 回调函数，返回系统时区。具体可见[支持的系统时区](js-apis-date-time.md#支持的系统时区)。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getTimezone((error: BusinessError, timezone: string) => {
    if (error) {
      console.error(`Failed to get timezone. Code: ${error.code}, message: ${error.message}`);
      return;
    }
    console.info(`Succeeded in getting timezone: ${timezone}`);
  });
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to get timezone. Code: ${error.code}, message: ${error.message}`);
}
```

## systemDateTime.getTimezone

getTimezone(): Promise<string>

获取系统时区，使用Promise异步回调。

**系统能力：** SystemCapability.MiscServices.Time

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回系统时区。具体可见[支持的系统时区](js-apis-date-time.md#支持的系统时区)。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  systemDateTime.getTimezone().then((timezone: string) => {
    console.info(`Succeeded in getting timezone: ${timezone}`);
  }).catch((error: BusinessError) => {
    console.error(`Failed to get timezone. Code: ${error.code}, message: ${error.message}`);
  });
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to get timezone. Code: ${error.code}, message: ${error.message}`);
}
```

## systemDateTime.getTimezoneSync10+

getTimezoneSync(): string

获取系统时区，使用同步方式。

**系统能力：** SystemCapability.MiscServices.Time

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回系统时区。具体可见[支持的系统时区](js-apis-date-time.md#支持的系统时区)。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let timezone: string = systemDateTime.getTimezoneSync();
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to get timezone. Code: ${error.code}, message: ${error.message}`);
}
```

## 支持的系统时区

支持的系统时区及各时区与0时区相比的标准时间偏移量（单位：h）可见下表。

| 时区 | 偏移量 |
| --- | --- |
| Antarctica/McMurdo | 12 |
| America/Argentina/Buenos\_Aires | -3 |
| Australia/Sydney | 10 |
| America/Noronha | -2 |
| America/St\_Johns | -3.5 |
| Africa/Kinshasa | 1 |
| America/Santiago | -4 |
| Asia/Shanghai | 8 |
| Asia/Nicosia | 3 |
| Europe/Berlin | 2 |
| America/Guayaquil | -5 |
| Europe/Madrid | 2 |
| Pacific/Pohnpei | 11 |
| America/Godthab | -1 |
| Asia/Jakarta | 7 |
| Pacific/Tarawa | 12 |
| Asia/Almaty | 6 |
| Pacific/Majuro | 12 |
| Asia/Ulaanbaatar | 8 |
| America/Mexico\_City | -6 |
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

## systemDateTime.getAutoTimeStatus21+

getAutoTimeStatus(): boolean

获取自动设置时间开关状态，使用同步方式。

**系统能力：** SystemCapability.MiscServices.Time

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回自动设置时间开关状态。  - true：表示自动设置时间开关状态为打开。  - false：表示自动设置时间开关状态为关闭。 |

**错误码：**

以下错误码的详细介绍请参见[时间时区服务错误码](errorcode-time.md)和[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 13000001 | Network connection error or OS error. Possible causes: 1.System memory is insufficient; 2.Calls the underlying system interface failed. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let status: boolean = systemDateTime.getAutoTimeStatus();
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to get autotime status. Code: ${error.code}, message: ${error.message}`);
}
```
