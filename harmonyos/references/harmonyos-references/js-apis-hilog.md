---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hilog
title: "@ohos.hilog (HiLog日志打印)"
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > ArkTS API > @ohos.hilog (HiLog日志打印)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:15+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ac6e25909553e20fcbe507fbc037e4e51d1db7ed0ac5afe50565768268e9286b
---

hilog模块是HarmonyOS提供的日志打印子系统，允许应用或服务按照指定的日志类型、日志级别和格式字符串输出日志。开发者可利用hilog在应用运行过程中记录关键流程信息，异常情况和错误事件，从而了解应用的运行状态并更好地调试程序。hilog适用于应用和服务在开发调试阶段记录运行日志的场景，也适用于正式发布版本中通过级别控制减少日志输出和保护隐私数据的场景。

hilog模块提供以下核心功能：

**日志打印**：提供debug、info、warn、error、fatal五个级别函数，开发者可根据信息的严重程度选择合适的级别输出日志。日志内容支持格式化字符串和隐私标识，便于结构化记录和保护敏感数据。

**日志级别控制**：通过setMinLogLevel设置最小日志级别过滤低级别日志输出，或通过setLogLevel配合偏好策略（PreferStrategy）灵活决定新设置级别与系统控制级别的生效关系，避免冗余日志。

**日志可打印判断**：通过isLoggable在打印日志前判断指定domain、tag和级别的日志是否可输出，避免无效日志打印的性能开销。

**日志输出管理**：通过setOutputType设置日志输出到控制台、私有沙箱或公有沙箱，通过setOutputTypeByDomain按域ID列表精细化控制不同域的输出方式，并提供沙箱日志目录查询、沙箱日志文件获取、沙箱日志刷新与清理等管理能力。

**说明** 

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```js
import { hilog } from '@kit.PerformanceAnalysisKit';
```

## hilog.isLoggable

isLoggable(domain: number, tag: string, level: LogLevel) : boolean

在打印日志前调用该接口，用于检查指定领域标识、日志标识和级别的日志是否可以打印。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.HiviewDFX.HiLog

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| domain | number | 是 | 日志对应的领域标识，范围是0x0~0xFFFF，超出范围则日志无法打印。  建议开发者在应用内根据需要自定义划分。 |
| tag | string | 是 | 指定日志标识，可以为任意字符串，建议用于标识调用所在的类或者业务行为。tag长度最多为31字节，超出后会截断，不建议使用中文字符，可能出现乱码或者对齐问题。 |
| level | [LogLevel](js-apis-hilog.md#loglevel) | 是 | 日志级别。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果返回true，则该领域标识、日志标识和级别的日志可以打印，否则不能打印。 |

**示例：**

```js
hilog.isLoggable(0x0001, "testTag", hilog.LogLevel.INFO);
```

## LogLevel

日志级别。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.HiviewDFX.HiLog

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEBUG | 3 | 详细的流程记录，通过该级别的日志可以更详细地分析业务流程和定位问题。 |
| INFO | 4 | 用于记录业务关键流程节点，可以还原业务的主要运行过程；  用于记录可预料的非正常情况信息，如无网络信号、登录失败等。  这些日志都应该由该业务内处于支配地位的模块来记录，避免在多个被调用的模块或低级函数中重复记录。 |
| WARN | 5 | 用于记录较为严重的非预期情况，但是对用户影响不大，应用可以自动恢复或通过简单的操作就可以恢复的问题。 |
| ERROR | 6 | 应用发生了错误，该错误会影响功能的正常运行或用户的正常使用，可以恢复但恢复代价较高，如重置数据等。 |
| FATAL | 7 | 重大致命异常，表明应用即将崩溃，故障无法恢复。 |

## hilog.debug

debug(domain: number, tag: string, format: string, ...args: any[]) : void

打印DEBUG级别的日志。

DEBUG级别的日志在正式发布版本中默认不被打印，只有在调试版本或打开调试开关的情况下才会打印。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.HiviewDFX.HiLog

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| domain | number | 是 | 日志对应的领域标识，范围是0x0~0xFFFF，超出范围则日志无法打印。  建议开发者在应用内根据需要自定义划分。 |
| tag | string | 是 | 指定日志标识，可以为任意字符串，建议用于标识调用所在的类或者业务行为。tag长度最多为31字节，超出后会截断，不建议使用中文字符，可能出现乱码或者对齐问题。 |
| format | string | 是 | 格式字符串，用于日志的格式化输出。格式字符串中可以设置多个参数，参数需要包含参数类型、隐私标识。  可用的参数格式符包括%d、%i、%s、%o、%O等，详见[参数格式符](js-apis-hilog.md#参数格式符)。  隐私标识分为{public}和{private}，缺省为{private}。标识{public}的内容明文输出，标识{private}的内容以<private>过滤回显。隐私标识机制帮助开发者保护隐私敏感数据。 |
| args | any[] | 否 | 与格式字符串format对应的可变长度参数列表。参数数目、参数类型必须与格式字符串中的标识一一对应。当格式字符串中不包含占位符时，可以不传此参数，仅输出格式字符串本身。 |

**示例：**

输出一条DEBUG信息，格式字符串为"%{public}s World %{private}d"。其中变参%{public}s为明文显示的字符串；%{private}d为隐私的整型数。

```js
hilog.debug(0x0001, "testTag", "%{public}s World %{private}d", "hello", 3);
```

字符串"hello"填入%{public}s，整型数3填入%{private}d，输出日志：

```txt
08-05 12:21:47.579  2695-2703  A00001/com.example.hilogDemo/testTag  com.example.hilogDemo  D     hello World <private>
```

## hilog.info

info(domain: number, tag: string, format: string, ...args: any[]) : void

打印INFO级别的日志。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.HiviewDFX.HiLog

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| domain | number | 是 | 日志对应的领域标识，范围是0x0~0xFFFF，超出范围则日志无法打印。  建议开发者在应用内根据需要自定义划分。 |
| tag | string | 是 | 指定日志标识，可以为任意字符串，建议用于标识调用所在的类或者业务行为。tag长度最多为31字节，超出后会截断，不建议使用中文字符，可能出现乱码或者对齐问题。 |
| format | string | 是 | 格式字符串，用于日志的格式化输出。格式字符串中可以设置多个参数，参数需要包含参数类型、隐私标识。  可用的参数格式符包括%d、%i、%s、%o、%O等，详见[参数格式符](js-apis-hilog.md#参数格式符)。  隐私标识分为{public}和{private}，缺省为{private}。标识{public}的内容明文输出，标识{private}的内容以<private>过滤回显。隐私标识机制帮助开发者保护隐私敏感数据。 |
| args | any[] | 否 | 与格式字符串format对应的可变长度参数列表。参数数目、参数类型必须与格式字符串中的标识一一对应。当格式字符串中不包含占位符时，可以不传此参数，仅输出格式字符串本身。 |

**示例：**

输出一条INFO信息，格式字符串为"%{public}s World %{private}d"。其中变参%{public}s为明文显示的字符串；%{private}d为隐私的整型数。

```js
hilog.info(0x0001, "testTag", "%{public}s World %{private}d", "hello", 3);
```

字符串"hello"填入%{public}s，整型数3填入%{private}d，输出日志：

```txt
08-05 12:21:47.579  2695-2703  A00001/com.example.hilogDemo/testTag  com.example.hilogDemo  I     hello World <private>
```

## hilog.warn

warn(domain: number, tag: string, format: string, ...args: any[]) : void

打印WARN级别的日志。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.HiviewDFX.HiLog

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| domain | number | 是 | 日志对应的领域标识，范围是0x0~0xFFFF，超出范围则日志无法打印。  建议开发者在应用内根据需要自定义划分。 |
| tag | string | 是 | 指定日志标识，可以为任意字符串，建议用于标识调用所在的类或者业务行为。tag长度最多为31字节，超出后会截断，不建议使用中文字符，可能出现乱码或者对齐问题。 |
| format | string | 是 | 格式字符串，用于日志的格式化输出。格式字符串中可以设置多个参数，参数需要包含参数类型、隐私标识。  可用的参数格式符包括%d、%i、%s、%o、%O等，详见[参数格式符](js-apis-hilog.md#参数格式符)。  隐私标识分为{public}和{private}，缺省为{private}。标识{public}的内容明文输出，标识{private}的内容以<private>过滤回显。隐私标识机制帮助开发者保护隐私敏感数据。 |
| args | any[] | 否 | 与格式字符串format对应的可变长度参数列表。参数数目、参数类型必须与格式字符串中的标识一一对应。当格式字符串中不包含占位符时，可以不传此参数，仅输出格式字符串本身。 |

**示例：**

输出一条WARN信息，格式字符串为"%{public}s World %{private}d"。其中变参%{public}s为明文显示的字符串；%{private}d为隐私的整型数。

```js
hilog.warn(0x0001, "testTag", "%{public}s World %{private}d", "hello", 3);
```

字符串"hello"填入%{public}s，整型数3填入%{private}d，输出日志：

```txt
08-05 12:21:47.579  2695-2703  A00001/com.example.hilogDemo/testTag  com.example.hilogDemo  W     hello World <private>
```

## hilog.error

error(domain: number, tag: string, format: string, ...args: any[]) : void

打印ERROR级别的日志。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.HiviewDFX.HiLog

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| domain | number | 是 | 日志对应的领域标识，范围是0x0~0xFFFF，超出范围则日志无法打印。  建议开发者在应用内根据需要自定义划分。 |
| tag | string | 是 | 指定日志标识，可以为任意字符串，建议用于标识调用所在的类或者业务行为。tag长度最多为31字节，超出后会截断，不建议使用中文字符，可能出现乱码或者对齐问题。 |
| format | string | 是 | 格式字符串，用于日志的格式化输出。格式字符串中可以设置多个参数，参数需要包含参数类型、隐私标识。  可用的参数格式符包括%d、%i、%s、%o、%O等，详见[参数格式符](js-apis-hilog.md#参数格式符)。  隐私标识分为{public}和{private}，缺省为{private}。标识{public}的内容明文输出，标识{private}的内容以<private>过滤回显。隐私标识机制帮助开发者保护隐私敏感数据。 |
| args | any[] | 否 | 与格式字符串format对应的可变长度参数列表。参数数目、参数类型必须与格式字符串中的标识一一对应。当格式字符串中不包含占位符时，可以不传此参数，仅输出格式字符串本身。 |

**示例：**

输出一条ERROR信息，格式字符串为"%{public}s World %{private}d"。其中变参%{public}s为明文显示的字符串；%{private}d为隐私的整型数。

```js
hilog.error(0x0001, "testTag", "%{public}s World %{private}d", "hello", 3);
```

字符串"hello"填入%{public}s，整型数3填入%{private}d，输出日志：

```txt
08-05 12:21:47.579  2695-2703  A00001/com.example.hilogDemo/testTag  com.example.hilogDemo  E     hello World <private>
```

## hilog.fatal

fatal(domain: number, tag: string, format: string, ...args: any[]) : void

打印FATAL级别的日志。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.HiviewDFX.HiLog

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| domain | number | 是 | 日志对应的领域标识，范围是0x0~0xFFFF，超出范围则日志无法打印。  建议开发者在应用内根据需要自定义划分。 |
| tag | string | 是 | 指定日志标识，可以为任意字符串，建议用于标识调用所在的类或者业务行为。tag长度最多为31字节，超出后会截断，不建议使用中文字符，可能出现乱码或者对齐问题。 |
| format | string | 是 | 格式字符串，用于日志的格式化输出。格式字符串中可以设置多个参数，参数需要包含参数类型、隐私标识。  可用的参数格式符包括%d、%i、%s、%o、%O等，详见[参数格式符](js-apis-hilog.md#参数格式符)。  隐私标识分为{public}和{private}，缺省为{private}。标识{public}的内容明文输出，标识{private}的内容以<private>过滤回显。隐私标识机制帮助开发者保护隐私敏感数据。 |
| args | any[] | 否 | 与格式字符串format对应的可变长度参数列表。参数数目、参数类型必须与格式字符串中的标识一一对应。当格式字符串中不包含占位符时，可以不传此参数，仅输出格式字符串本身。 |

**示例：**

输出一条FATAL信息，格式字符串为"%{public}s World %{private}d"。其中变参%{public}s为明文显示的字符串；%{private}d为隐私的整型数。

```js
hilog.fatal(0x0001, "testTag", "%{public}s World %{private}d", "hello", 3);
```

字符串"hello"填入%{public}s，整型数3填入%{private}d，输出日志：

```txt
08-05 12:21:47.579  2695-2703  A00001/com.example.hilogDemo/testTag  com.example.hilogDemo  F     hello World <private>
```

## hilog.setMinLogLevel15+

setMinLogLevel(level: LogLevel): void

设置应用日志打印的最低日志级别，用于拦截低级别日志打印，在需要优化应用性能或减少低价值日志干扰时使用，避免冗余日志。

**注意** 

如果设置的日志级别低于[全局日志级别](../harmonyos-guides/hilog.md#查看和设置日志级别)，设置不生效。

debug版本应用下，此函数不生效。

**元服务API**：从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.HiviewDFX.HiLog

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| level | [LogLevel](js-apis-hilog.md#loglevel) | 是 | 日志级别。 |

**示例：**

以全局日志级别为INFO下，打印5条不同级别的hilog日志，在打印过程中调用两次setMinLogLevel接口为例：

```js
hilog.info(0x0001, "testTag", 'this is an info level log, id: %{public}d', 1);
hilog.setMinLogLevel(hilog.LogLevel.WARN);
hilog.info(0x0001, "testTag", 'this is an info level log, id: %{public}d', 2);
hilog.error(0x0001, "testTag", 'this is an error level log, id: %{public}d', 3);
hilog.setMinLogLevel(hilog.LogLevel.DEBUG);
hilog.debug(0x0001, "testTag", 'this is a debug level log, id: %{public}d', 4);
hilog.info(0x0001, "testTag", 'this is an info level log, id: %{public}d', 5);
```

由于全局日志起始为INFO，第一条日志可以正常打印。

在设置进程最低可打印日志级别为WARN后，第二条日志不符合该日志级别，第二条日志打印失败，第三条日志可以正常打印。

在设置进程最低日志级别为DEBUG后，但是此时全局日志级别为INFO，所以第四条日志不满足全局日志级别，打印失败，第五条日志可以打印。

最终打印结果如下所示：

```txt
08-07 23:50:01.532   13694-13694   A00001/com.example.hilogDemo/testTag  com.example.hilogDemo  I     this is an info level log, id: 1
08-07 23:50:01.532   13694-13694   A00001/com.example.hilogDemo/testTag  com.example.hilogDemo  E     this is an error level log, id: 3
08-07 23:50:01.532   13694-13694   A00001/com.example.hilogDemo/testTag  com.example.hilogDemo  I     this is an info level log, id: 5
```

## hilog.setLogLevel21+

setLogLevel(level: LogLevel, prefer: PreferStrategy): void

设置当前应用程序进程的最低日志级别。

可通过prefer参数配置不同的偏好策略。如果选择策略PREFER\_CLOSE\_LOG，等同于调用setMinLogLevel函数。

**注意** 

debug版本应用下，此函数不生效。

**元服务API**：从API version 21开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.HiviewDFX.HiLog

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| level | [LogLevel](js-apis-hilog.md#loglevel) | 是 | 日志级别。 |
| prefer | [PreferStrategy](js-apis-hilog.md#preferstrategy21) | 是 | 偏好策略。 |

## PreferStrategy21+

偏好策略。

**元服务API**：从API version 21开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.HiviewDFX.HiLog

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNSET\_LOGLEVEL | 0 | 清除设置，实际生效的最低日志级别是系统控制的最低级别。 |
| PREFER\_CLOSE\_LOG | 1 | 实际生效的最低日志级别是新设置的级别和系统控制的最低级别两个值的较大值，适用于需要严格限制日志输出的场景。 |
| PREFER\_OPEN\_LOG | 2 | 实际生效的最低日志级别是新设置的级别和系统控制的最低级别两个值的较小值，适用于需要尽可能多的打开日志输出的场景。 |

**示例：**

以全局日志级别为INFO下，打印5条不同级别的hilog日志，在打印过程中调用两次setLogLevel接口为例：

```js
hilog.info(0x0001, "testTag", 'this is an info level log, id: %{public}d', 1);
hilog.setLogLevel(hilog.LogLevel.WARN, hilog.PreferStrategy.PREFER_OPEN_LOG);
hilog.info(0x0001, "testTag", 'this is an info level log, id: %{public}d', 2);
hilog.error(0x0001, 'testTag', 'this is an error level log, id: %{public}d', 3);
hilog.setLogLevel(hilog.LogLevel.DEBUG, hilog.PreferStrategy.PREFER_CLOSE_LOG);
hilog.debug(0x0001, "testTag", 'this is a debug level log, id: %{public}d', 4);
hilog.info(0x0001, "testTag", 'this is an info level log, id: %{public}d', 5);
```

由于全局日志起始为INFO，第一条日志可以正常打印。

在设置进程最低日志级别为WARN，并选择策略PREFER\_OPEN\_LOG后，实际生效的最低日志级别是全局日志级别INFO，所以第二条和第三条日志均可正常打印。

在设置进程最低日志级别为DEBUG，并选择策略PREFER\_CLOSE\_LOG后（等同于hilog.setMinLogLevel(hilog.LogLevel.DEBUG)），但是此时全局日志级别为INFO，所以第四条日志不满足全局日志级别，打印失败，第五条日志可以打印。

最终打印结果如下所示：

```txt
08-07 23:50:01.532   13694-13694   A00001/com.example.hilogDemo/testTag  com.example.hilogDemo  I     this is an info level log, id: 1
08-07 23:50:01.532   13694-13694   A00001/com.example.hilogDemo/testTag  com.example.hilogDemo  I     this is an info level log, id: 2
08-07 23:50:01.532   13694-13694   A00001/com.example.hilogDemo/testTag  com.example.hilogDemo  E     this is an error level log, id: 3
08-07 23:50:01.532   13694-13694   A00001/com.example.hilogDemo/testTag  com.example.hilogDemo  I     this is an info level log, id: 5
```

## 参数格式符

上述接口中，日志打印的格式化参数需按照如下格式打印：

%{[private flag]}specifier

| 隐私标识符（private flag） | 说明 |
| --- | --- |
| 无 | 缺省值默认为private，不打印明文参数。 |
| private | 隐私参数类型，不打印明文参数。 |
| public | 明文显示参数。 |

| 格式说明符（specifier） | 说明 | 示例 |
| --- | --- | --- |
| d/i | 支持打印number和bigint类型。 | 123 |
| s | 支持打印string undefined bool 和null类型。 | "123" |
| o/O | 支持打印object、undefined和null类型。  从API version 20开始，支持该能力。 | { 'name': "Jack", 'age': 22 } |

**示例：**

```js
let testObj: Record<string, string | number> = {
    'name': "Jack",
    'age': 22
}
let isBol = true;
let bigNum = BigInt(1234567890123456789);
hilog.info(0x0001, "jsHilogTest", "print object: %{public}s", JSON.stringify(testObj));
hilog.info(0x0001, "jsHilogTest", "print object: %{public}o", testObj);
hilog.info(0x0001, "jsHilogTest", "private flag: %{private}s %s, print null: %{public}s", "hello", "world", null);
hilog.info(0x0001, "jsHilogTest", "print undefined: %{public}s", undefined);
hilog.info(0x0001, "jsHilogTest", "print number: %{public}d %{public}i", 123, 456);
hilog.info(0x0001, "jsHilogTest", "print bigNum: %{public}d %{public}i", bigNum, bigNum);
hilog.info(0x0001, "jsHilogTest", "print boolean: %{public}s", isBol);
```

**打印结果：**

```txt
08-09 13:26:29.094  2266-2266  A00001/com.example.hilogDemo/jsHilogTest  com.example.hilogDemo  I  print object: {"name":"Jack","age":22}
08-09 13:26:29.094  2266-2266  A00001/com.example.hilogDemo/jsHilogTest  com.example.hilogDemo  I  print object: {"name":"Jack","age":22}
08-09 13:26:29.094  2266-2266  A00001/com.example.hilogDemo/jsHilogTest  com.example.hilogDemo  I  private flag: <private> <private>, print null: null
08-09 13:26:29.094  2266-2266  A00001/com.example.hilogDemo/jsHilogTest  com.example.hilogDemo  I  print undefined: undefined
08-09 13:26:29.094  2266-2266  A00001/com.example.hilogDemo/jsHilogTest  com.example.hilogDemo  I  print number: 123 456
08-09 13:26:29.095  2266-2266  A00001/com.example.hilogDemo/jsHilogTest  com.example.hilogDemo  I  print bigNum: 1234567890123456768 1234567890123456768
08-09 13:26:29.095  2266-2266  A00001/com.example.hilogDemo/jsHilogTest  com.example.hilogDemo  I  print boolean: true
```

## OutputType

hilog输出类型的枚举值，DEFAULT和CONSOLE\_ONLY适用于仅输出到控制台的场景，PRIVATE\_SANDBOX\_ONLY适用于隐私日志存储，SHARE\_SANDBOX\_ONLY适用于需要云端采集日志的场景，PRIVATE\_SANDBOX\_WITH\_CONSOLE和SHARE\_SANDBOX\_WITH\_CONSOLE适用于同时需要控制台输出和沙箱存储的场景。

**起始版本**：26.0.0

**元服务API**：从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.HiviewDFX.HiLog

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 默认输出类型，hilog仅输出至控制台，等价于CONSOLE\_ONLY。 |
| CONSOLE\_ONLY | 0 | hilog仅输出至控制台，等价于DEFAULT。 |
| PRIVATE\_SANDBOX\_ONLY | 1 | hilog落盘至应用私有沙箱，该路径仅自身可访问。 |
| SHARE\_SANDBOX\_ONLY | 2 | hilog落盘至应用公有沙箱，该路径允许应用自身及系统访问。 |
| PRIVATE\_SANDBOX\_WITH\_CONSOLE | 3 | 同时启用CONSOLE\_ONLY和PRIVATE\_SANDBOX\_ONLY。 |
| SHARE\_SANDBOX\_WITH\_CONSOLE | 4 | 同时启用CONSOLE\_ONLY和SHARE\_SANDBOX\_ONLY。 |

## hilog.setOutputType

setOutputType(type: OutputType): OutputType

设置hilog的输出类型。

**起始版本**：26.0.0

**元服务API**：从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.HiviewDFX.HiLog

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [OutputType](js-apis-hilog.md#outputtype) | 是 | hilog的输出类型，用于设置hilog日志的输出目标（如控制台或沙箱）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [OutputType](js-apis-hilog.md#outputtype) | 返回上一次设置的输出类型。 |

**示例：**

```js
hilog.setOutputType(hilog.OutputType.SHARE_SANDBOX_ONLY);
hilog.info(0x0001, "testTag", 'sandbox log to share sandbox only');
hilog.flush();
```

**打印结果：**

沙箱日志输出。

```text
05-15 16:57:04.238 40518 40518 I A00001/testTag: sandbox log to share sandbox only
```

## hilog.setOutputTypeByDomainID

setOutputTypeByDomainID(type: OutputType, domainIDs: Array<number>, isExclude: boolean): OutputType

设置hilog的输出类型，并且配置输出的domainID列表，可选择仅输出列表中的domainID，或不输出列表中的domainID。

**起始版本**：26.0.0

**元服务API**：从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.HiviewDFX.HiLog

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [OutputType](js-apis-hilog.md#outputtype) | 是 | hilog的输出类型。 |
| domainIDs | Array<number> | 是 | domainID列表，每个domainID取值范围为0x0000~0xFFFF，仅对应用domain生效。 |
| isExclude | boolean | 是 | 用于决定domainIDs是否对输出类型生效。  true表示排除domainIDs列表，仅对非列表中的domain生效；false表示仅对列表中的domain生效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [OutputType](js-apis-hilog.md#outputtype) | 返回上一次设置的输出类型。 |

**示例：**

```js
hilog.setOutputTypeByDomainID(hilog.OutputType.SHARE_SANDBOX_ONLY, [0x0001, 0x0002, 0x0003], false);
hilog.info(0x0001, "testTag", 'sandbox log to share sandbox only');
hilog.info(0x0002, "testTag", 'sandbox log to share sandbox only');
hilog.info(0x0003, "testTag", 'sandbox log to share sandbox only');
hilog.info(0x0004, "testTag", 'sandbox log to share sandbox only');
hilog.flush();
```

**打印结果：**

沙箱日志输出，domain 0x0004的日志没有被打印。

```text
05-15 16:57:04.238 40518 40518 I A00001/testTag: sandbox log to share sandbox only
05-15 16:57:04.238 40518 40518 I A00002/testTag: sandbox log to share sandbox only
05-15 16:57:04.238 40518 40518 I A00003/testTag: sandbox log to share sandbox only
```

## hilog.getOutputType

getOutputType(): OutputType

获取当前hilog的输出类型。

**起始版本**：26.0.0

**元服务API**：从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.HiviewDFX.HiLog

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [OutputType](js-apis-hilog.md#outputtype) | 返回当前hilog的输出类型。 |

**示例：**

```js
hilog.setOutputType(hilog.OutputType.SHARE_SANDBOX_WITH_CONSOLE);
let last = hilog.getOutputType();
hilog.info(0x0001, "testTag", 'last output type:%{public}d', last);
```

**打印结果：**

控制台输出。

```txt
05-15 16:57:04.238  40518-40518  A00001/com.example.hilogDemo/testTag  com.example.hilogDemo  I  last output type:4
```

## hilog.getOutputDir

getOutputDir(): string

返回hilog日志在沙箱中的路径，如果hilog的输出类型为DEFAULT，则返回空。

**起始版本**：26.0.0

**元服务API**：从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.HiviewDFX.HiLog

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | hilog日志的沙箱路径。 |

**示例：**

```js
hilog.setOutputType(hilog.OutputType.SHARE_SANDBOX_WITH_CONSOLE);
let dir = hilog.getOutputDir();
hilog.info(0x0001, "testTag", 'sandbox output dir:%{public}s', dir);
```

**打印结果：**

控制台输出。

```txt
05-15 16:57:04.238  40518-40518  A00001/com.example.hilogDemo/testTag  com.example.hilogDemo  I  sandbox output dir:/data/storage/el2/log/hiapplog/
```

## hilog.clean

clean(): void

删除沙箱中的所有hilog日志。

**起始版本**：26.0.0

**元服务API**：从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.HiviewDFX.HiLog

**示例：**

```js
hilog.clean();
```

## hilog.flush

flush(): void

刷新沙箱中的hilog日志，确保日志落盘。

**起始版本**：26.0.0

**元服务API**：从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.HiviewDFX.HiLog

**示例：**

```js
hilog.flush();
```

## hilog.getLogFile

getLogFile(latestSeconds: number): Array<string>

返回指定秒数内修改过的hilog沙箱日志文件。

**起始版本**：26.0.0

**元服务API**：从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.HiviewDFX.HiLog

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| latestSeconds | number | 是 | 距离现在的时间间隔，以秒为单位。  若传入的值小于0，则为无效值，返回值为空。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 指定时间段内写入过的沙箱文件列表。 |

**示例：**

获取5分钟之内修改过的文件。

```js
hilog.info(0x0001, "testTag", 'sandbox log to share sandbox with console');
hilog.setOutputType(hilog.OutputType.SHARE_SANDBOX_WITH_CONSOLE);
let timeInterval
let logs = hilog.getLogFile(timeInterval);
hilog.info(0x0001, "testTag", 'sandbox log files:%{public}s', logs.toString());
hilog.flush();
```

**打印结果：**

沙箱日志输出。

```text
05-15 16:57:04.238 40518 40518 I A00001/testTag: sandbox log files:hiapplog.40518.001.20260515-165602.log
```
