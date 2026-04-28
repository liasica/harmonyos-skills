---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-logs
title: Console (控制台)
breadcrumb: API参考 > 公共基础能力 > ArkTS API > Console (控制台)
category: harmonyos-references
scraped_at: 2026-04-28T08:19:16+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:229ba6564cf686fb9e4f09eb3162078bf6a9b0c2737aba0b6c29a25203adead9
---

本模块提供了一个简单的调试控制台，类似于浏览器提供的JavaScript控制台机制。

说明

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## console.debug

PhonePC/2in1TabletTVWearable

static debug(message: string, ...arguments: any[]): void

以格式化输出方式打印调试信息。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | string | 是 | 表示要打印的文本信息。 |
| arguments | any[] | 否 | 表示其余要打印的信息或message的替换值。 |

**示例：**

```
1. const number = 5;
2. console.debug('count: %d', number);  // 格式化输出替换message中的文本。
3. // count: 5
4. console.debug('count:', number);  // 打印message以及其余信息
5. // count: 5
6. console.debug('count:'); // 仅打印message
7. // count:
```

## console.log

PhonePC/2in1TabletTVWearable

static log(message: string, ...arguments: any[]): void

以格式化输出方式打印日志信息。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | string | 是 | 表示要打印的文本信息。 |
| arguments | any[] | 否 | 表示其余要打印的信息或message的替换值。 |

**示例：**

```
1. const number = 5;
2. console.log('count: %d', number);  // 格式化输出替换message中的文本。
3. // count: 5
4. console.log('count:', number);  // 打印message以及其余信息
5. // count: 5
6. console.log('count:'); // 仅打印message
7. // count:
```

## console.info

PhonePC/2in1TabletTVWearable

static info(message: string, ...arguments: any[]): void

以格式化输出方式打印日志信息。(console.log()的别名）。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | string | 是 | 表示要打印的文本信息。 |
| arguments | any[] | 否 | 表示其余要打印的信息或message的替换值。 |

**示例：**

```
1. const number = 5;
2. console.info('count: %d', number);  // 格式化输出替换message中的文本。
3. // count: 5
4. console.info('count:', number);  // 打印message以及其余信息
5. // count: 5
6. console.info('count:'); // 仅打印message
7. // count:
```

## console.warn

PhonePC/2in1TabletTVWearable

static warn(message: string, ...arguments: any[]): void

以格式化输出方式打印警告信息。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | string | 是 | 表示要打印的警告信息。 |
| arguments | any[] | 否 | 表示其余要打印的信息或message的替换值。 |

**示例：**

```
1. const str = "name should be string";
2. console.warn('warn: %d', str);  // 格式化输出替换message中的文本。
3. // warn: name should be string
4. console.warn('warn:', str);  // 打印message以及其余信息
5. // warn: name should be string
6. console.warn('warn:'); // 仅打印message
7. // warn:
```

## console.error

PhonePC/2in1TabletTVWearable

static error(message: string, ...arguments: any[]): void

以格式化输出方式打印错误信息。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| message | string | 是 | 表示要打印的错误信息。 |
| arguments | any[] | 否 | 表示其余要打印的信息或message的替换值。 |

**示例：**

```
1. const str = "value is not defined";
2. console.error('error: %d', str);  // 格式化输出替换message中的文本。
3. // error: value is not defined
4. console.error('error:', str);  // 打印message以及其余信息
5. // error: value is not defined
6. console.error('error:'); // 仅打印message
7. // error:
```

## console.assert10+

PhonePC/2in1TabletTVWearable

static assert(value?: Object, ...arguments: Object[]): void

断言打印。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Object | 否 | 语句结果值。若value为假（false）或者省略，则输出以"Assertion failed"开头。如果value为真值（true），则无打印。 |
| arguments | Object | 否 | value为假（false）的后续错误消息打印。省略则不打印。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. console.assert(true, 'does nothing');  // 表达式结果值为true, 无打印。
2. console.assert(2 % 1 == 0, 'does nothing');  // 表达式结果值为true, 无打印。

4. console.assert(false, 'console %s work', 'didn\'t');
5. // Assertion failed: console didn't work

7. console.assert();
8. // Assertion failed
```

## console.count10+

PhonePC/2in1TabletTVWearable

static count(label?: string): void

维护一个内部计数器，调用时，打印此标签名以及对应的计数次数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| label | string | 否 | 计数器标签名。默认值为'default'。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. console.count()
2. // default: 1
3. console.count('default')
4. // default: 2
5. console.count('abc')
6. // abc: 1
7. console.count('xyz')
8. // xyz: 1
9. console.count('abc')
10. // abc: 2
11. console.count()
12. // default: 3
```

## console.countReset10+

PhonePC/2in1TabletTVWearable

static countReset(label?: string): void

清除指定标签名的计数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| label | string | 否 | 计数器标签名。默认值为'default'。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. console.count('abc');
2. // abc: 1
3. console.countReset('abc');
4. console.count('abc');
5. // abc: 1
```

## console.dir10+

PhonePC/2in1TabletTVWearable

static dir(dir?: Object): void

打印对象内容。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dir | Object | 否 | 需要打印内容的对象。省略则无任何打印。 |

**示例：**

```
1. class bar {
2. baz: boolean = true;
3. }
4. let b: bar = {baz: true}
5. class foo{
6. bar: bar = b;
7. }
8. let c: foo = {bar: b}
9. class  c1{
10. foo: foo = c;
11. }
12. let a: c1 = {foo: c}
13. console.dir(a);
14. // Object: {"foo":{"bar":{"baz":true}}}

16. console.dir(); // 无打印
```

## console.dirxml10+

PhonePC/2in1TabletTVWearable

static dirxml(...arguments: Object[]): void

此方法通过内部调用console.log()实现。此方法不会产生任何 XML 格式。使用方法与console.log()一致。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arguments | Object | 否 | 要打印的信息。省略则无任何打印。 |

**示例：**

```
1. const number = 5;
2. console.dirxml('count: %d', number);
3. // count: 5
4. console.dirxml('count:', number);
5. // count: 5
6. console.dirxml('count:');
7. // count:
```

## console.group10+

PhonePC/2in1TabletTVWearable

static group(...arguments: Object[]): void

默认将后续行的缩进增加两个空格。

如果提供需要打印的信息，则首先打印信息，没有额外的缩进。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arguments | Object | 否 | 要打印的信息。省略则仅打印两个空格。 |

**示例：**

```
1. console.info("outer");
2. // outer
3. console.group();
4. console.info("level 1");
5. //   level 1
6. console.group("in level1");
7. //   in level1
8. console.info("level 2");
9. //     level 2
```

## console.groupCollapsed10+

PhonePC/2in1TabletTVWearable

static groupCollapsed(...arguments: Object[]): void

使用与功能同console.group()一致。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arguments | Object | 否 | 要打印的信息。省略则仅打印两个空格。 |

**示例：**

```
1. console.groupCollapsed("outer");
2. // outer
3. console.groupCollapsed();
4. console.info("level 1");
5. //   level 1
6. console.groupCollapsed("in level1");
7. //   in level1
8. console.info("level 2");
9. //     level 2
```

## console.groupEnd10+

PhonePC/2in1TabletTVWearable

static groupEnd(): void

将后续行的缩进减少两个空格。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**示例：**

```
1. console.info("outer");
2. // outer
3. console.group();
4. console.info("level 1");
5. //   level 1
6. console.groupEnd();
7. console.info("outer");
8. // outer
```

## console.table10+

PhonePC/2in1TabletTVWearable

static table(tableData?: Object): void

以表格形式打印数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tableData | Object | 否 | 要打印为表格形式的对象。省略则无任何打印。 |

**示例：**

```
1. console.table([1, 2, 3]);
2. // ┌─────────┬────────┐
3. // │ (index) │ Values │
4. // ├─────────┼────────┤
5. // │    0    │   1    │
6. // │    1    │   2    │
7. // │    2    │   3    │
8. // └─────────┴────────┘

10. console.table({ a: [1, 2, 3, 4, 5], b: 5, c: { e: 5 } });

12. // ┌─────────┬───┬───┬───┬───┬───┬───┬────────┐
13. // │ (index) │ 0 │ 1 │ 2 │ 3 │ 4 │ e │ Values │
14. // ├─────────┼───┼───┼───┼───┼───┼───┼────────┤
15. // │    a    │ 1 │ 2 │ 3 │ 4 │ 5 │   │        │
16. // │    b    │   │   │   │   │   │   │   5    │
17. // │    c    │   │   │   │   │   │ 5 │        │
18. // └─────────┴───┴───┴───┴───┴───┴───┴────────┘
```

## console.time10+

PhonePC/2in1TabletTVWearable

static time(label?: string): void

启动可用于计算操作持续时间的计时器。可使用console.timeEnd()关闭计时器并打印经过的时间(单位：ms)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| label | string | 否 | 计时器标识。默认值为'default'。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. console.time('abc');
```

## console.timeEnd10+

PhonePC/2in1TabletTVWearable

static timeEnd(label?: string): void

停止之前通过调用 console.time() 启动的计时器并将打印经过的时间(单位：ms)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| label | string | 否 | 计时器标识。默认值为'default'。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. console.time('abc');
2. console.timeEnd('abc');
3. // abc: 225.438ms
```

## console.timeLog10+

PhonePC/2in1TabletTVWearable

static timeLog(label?: string, ...arguments: Object[]): void

对于先前通过调用 console.time() 启动的计时器，打印经过时间和其他data参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| label | string | 否 | 计时器标识。默认值为'default'。 |
| arguments | Object | 否 | 需要打印的其他日志。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. console.time('timer1');
2. console.timeLog('timer1', 17);
3. // timer1: 365.227ms 17
4. console.timeEnd('timer1');
5. // timer1: 513.22ms
```

## console.trace10+

PhonePC/2in1TabletTVWearable

static trace(...arguments: Object[]): void

打印当前堆栈。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| arguments | Object | 否 | 需要打印的其他日志。省略则仅打印堆栈信息。 |

**示例：**

```
1. console.trace();
2. // Trace:
3. //     xxxxxxxxxx(当前堆栈信息)
4. console.trace("Show the trace");
5. // Trace: Show the trace
6. //     xxxxxxxxxx(当前堆栈信息)
```

## console.traceHybridStack12+

PhonePC/2in1TabletTVWearable

static traceHybridStack(): void

在主线程/worker线程中可打印当前线程混合堆栈信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**示例：**

```
1. console.traceHybridStack();
2. // TraceHybridStack:
3. //     xxxxxxxxxx(当前线程混合堆栈信息)
```
