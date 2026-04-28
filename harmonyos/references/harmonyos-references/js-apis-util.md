---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-util
title: @ohos.util (util工具函数)
breadcrumb: API参考 > 应用框架 > ArkTS（方舟编程语言） > ArkTS API > @ohos.util (util工具函数)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:851d58a7fbed9ed531f3a676b15a309e2d4e2e33a1a4a5a0d4f87690a8f80a80
---

该模块主要提供常用的工具函数，实现字符串编解码（[TextEncoder](js-apis-util.md#textencoder)，[TextDecoder](js-apis-util.md#textdecoder)）、有理数运算（[RationalNumber8+](js-apis-util.md#rationalnumber8)）、缓冲区管理（[LRUCache9+](js-apis-util.md#lrucache9)）、范围判断（[ScopeHelper9+](js-apis-util.md#scopehelper9)）、Base64编解码（[Base64Helper9+](js-apis-util.md#base64helper9)）、内置对象类型检查（[types8+](js-apis-util.md#types8)）、对方法进行插桩和替换（[Aspect11+](js-apis-util.md#aspect11)）等功能。

说明

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { util } from '@kit.ArkTS';
```

## util.format9+

PhonePC/2in1TabletTVWearable

format(format: string, ...args: Object[]): string

使用样式化字符串将输入内容按特定格式输出。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| format | string | 是 | 格式化字符串，可以包含零个或多个占位符，用于指定要插入的参数的位置和格式。 |
| ...args | Object[] | 否 | 替换format参数中占位符的数据，此参数缺失时，默认返回第一个参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 格式化后的字符串。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**格式说明符：**

| 格式说明符 | 说明 |
| --- | --- |
| %s | 将参数转换为字符串，用于除Object，BigInt和-0之外的所有值。 |
| %d | 将参数作为十进制整数进行格式化输出，用于除Symbol和BigInt之外的所有值。 |
| %i | 将字符串转换为十进制整数，用于除BigInt和Symbol之外的所有值。 |
| %f | 将字符串转换为浮点数，用于除BigInt和Symbol之外的所有值。 |
| %j | 将JavaScript对象转换为JSON字符串进行格式化输出。 |
| %o | 用于将JavaScript对象进行格式化输出，将对象转换为字符串表示，但不包含对象的原型链信息。 |
| %O | 用于将JavaScript对象进行格式化输出，将对象转换为字符串表示。 |
| %c | 只在浏览器环境中有效。其余环境不会产生样式效果。 |
| %% | 转义百分号的特殊格式化占位符。 |

**示例：**

```
1. import { util } from '@kit.ArkTS';

3. interface utilAddressType {
4. city: string;
5. country: string;
6. }
7. interface utilPersonType {
8. name: string;
9. age: number;
10. address: utilAddressType;
11. }

13. let name = 'John';
14. let age = 20;
15. let formattedString = util.format('My name is %s and I am %s years old', name, age);
16. console.info(formattedString);
17. // 输出结果：My name is John and I am 20 years old
18. let num = 10.5;
19. formattedString = util.format('The number is %d', num);
20. console.info(formattedString);
21. // 输出结果：The number is 10.5
22. num = 100.5;
23. formattedString = util.format('The number is %i', num);
24. console.info(formattedString);
25. // 输出结果：The number is 100
26. const pi = 3.141592653;
27. formattedString = util.format('The value of pi is %f', pi);
28. console.info(formattedString);
29. // 输出结果：The value of pi is 3.141592653
30. const obj: Record<string,number | string> = { "name": 'John', "age": 20 };
31. formattedString = util.format('The object is %j', obj);
32. console.info(formattedString);
33. // 输出结果：The object is {"name":"John","age":20}
34. const person: utilPersonType = {
35. name: 'John',
36. age: 20,
37. address: {
38. city: 'New York',
39. country: 'USA'
40. }
41. };
42. console.info(util.format('Formatted object using %%O: %O', person));
43. console.info(util.format('Formatted object using %%o: %o', person));
44. /*
45. 输出结果：
46. Formatted object using %O: { name: 'John',
47. age: 20,
48. address:
49. { city: 'New York',
50. country: 'USA' } }
51. Formatted object using %o: { name: 'John',
52. age: 20,
53. address:
54. { city: 'New York',
55. country: 'USA' } }
56. */
57. const percentage = 80;
58. let arg = 'homework';
59. formattedString = util.format('John finished %d%% of the %s', percentage, arg);
60. console.info(formattedString);
61. // 输出结果：John finished 80% of the homework
```

## util.errnoToString9+

PhonePC/2in1TabletTVWearable

errnoToString(errno: number): string

获取系统错误码对应的详细信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| errno | number | 是 | 系统发生错误产生的错误码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 错误码对应的详细信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. let errnum = -1; // -1 : a system error number
2. let result = util.errnoToString(errnum);
3. console.info("result = " + result);
4. // 输出结果：result = operation not permitted
```

**部分错误码及信息示例：**

| 错误码 | 信息 |
| --- | --- |
| -1 | operation not permitted |
| -2 | no such file or directory |
| -3 | no such process |
| -4 | interrupted system call |
| -5 | i/o error |
| -11 | resource temporarily unavailable |
| -12 | not enough memory |
| -13 | permission denied |
| -100 | network is down |

## util.callbackWrapper

PhonePC/2in1TabletTVWearable

callbackWrapper(original: Function): (err: Object, value: Object)=>void

对异步函数进行回调化处理，回调中第一个参数是拒绝原因（如果Promise已解决，则为null），第二个参数是已解决的值。

说明

该接口要求参数original必须是异步函数类型。如果传入的参数不是异步函数，不会进行拦截，但是会输出错误信息："callbackWrapper: The type of Parameter must be AsyncFunction"。

该接口用于将返回Promise的async函数转换为错误优先回调风格的函数，调用此接口返回的函数接收一个回调函数作为第二个入参，调用此方法时会先执行original函数。当original的Promise返回resolve时，入参的回调函数的第一个参数为null，第二个参数为resolve的值。当original的Promise返回reject时，入参的回调函数的第一个参数为错误对象，第二个参数为null。当original为无入参的函数时，此接口返回的函数第一个入参需传入一个无效的占位参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| original | Function | 是 | 异步函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| (err: Object, value: Object)=>void | 返回一个回调函数，该函数第一个参数err是拒绝原因（如果 Promise 已解决，则为 null），第二个参数value是已解决的值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. async function fn(input: string) {
2. return input;
3. }
4. let cb = util.callbackWrapper(fn);
5. cb('hello world', (err : Object, ret : string) => {
6. if (err) throw new Error;
7. console.info(ret);
8. });
9. // 输出结果：hello world
```

## util.promisify9+

PhonePC/2in1TabletTVWearable

promisify(original: (err: Object, value: Object) => void): Function

接收一个采用“错误优先”回调模式的函数，即以(err, value) => callback作为最后一个参数，并返回其Promise函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| original | (err: Object, value: Object) => void | 是 | 回调函数中第一个参数err是拒绝原因（如果 Promise 已解决，则为 null），第二个参数value是已解决的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Function | 返回一个 Promise 的函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. async function fn() {
2. return 'hello world';
3. }
4. const addCall = util.promisify(util.callbackWrapper(fn));
5. (async () => {
6. try {
7. let res: string = await addCall();
8. console.info(res);
9. // 输出结果：hello world
10. } catch (err) {
11. console.info(err);
12. }
13. })();
```

## util.generateRandomUUID9+

PhonePC/2in1TabletTVWearable

generateRandomUUID(entropyCache?: boolean): string

使用加密安全随机数生成器生成随机的RFC 4122版本4的string类型UUID。为了提升性能，此接口会默认使用缓存，即入参为true，最多可缓存128个随机的UUID。当缓存中128个UUID用尽后，会重新生成，以保证UUID的随机性。如需禁用缓存，请将入参设置为false。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| entropyCache | boolean | 否 | 是否使用已缓存的UUID，true表示使用缓存的UUID，false表示不使用缓存的UUID，默认true。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 表示此UUID的字符串。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |

**示例：**

```
1. let uuid = util.generateRandomUUID(true);
2. console.info("RFC 4122 Version 4 UUID:" + uuid);
3. // 输出随机生成的UUID
```

## util.generateRandomBinaryUUID9+

PhonePC/2in1TabletTVWearable

generateRandomBinaryUUID(entropyCache?: boolean): Uint8Array

使用加密安全随机数生成器生成随机的RFC 4122版本4的UUID。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| entropyCache | boolean | 否 | 是否使用已缓存的UUID，true表示使用缓存的UUID，false表示不使用缓存的UUID，默认true。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 表示此UUID的Uint8Array值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |

**示例：**

```
1. let uuid = util.generateRandomBinaryUUID(true);
2. console.info(JSON.stringify(uuid));
3. // 输出随机生成的UUID
```

## util.parseUUID9+

PhonePC/2in1TabletTVWearable

parseUUID(uuid: string): Uint8Array

将generateRandomUUID生成的string类型UUID转换为[util.generateRandomBinaryUUID](js-apis-util.md#utilgeneraterandombinaryuuid9)生成的UUID，符合RFC 4122版本规范。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uuid | string | 是 | UUID字符串。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 返回表示此UUID的Uint8Array，如果解析失败，则抛出SyntaxError。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |
| 10200002 | Invalid uuid string. |

**示例：**

```
1. let uuid = util.parseUUID("84bdf796-66cc-4655-9b89-d6218d100f9c");
2. console.info("uuid = " + uuid);
3. // 输出结果：uuid = 132,189,247,150,102,204,70,85,155,137,214,33,141,16,15,156
```

## util.printf(deprecated)

PhonePC/2in1TabletTVWearable

printf(format: string, ...args: Object[]): string

通过式样化字符串对输入的内容按特定格式输出。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[util.format9+](js-apis-util.md#utilformat9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| format | string | 是 | 式样化字符串。 |
| ...args | Object[] | 否 | 替换式样化字符串通配符的数据，此参数缺失时，默认返回第一个参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 按特定格式式样化后的字符串。 |

**示例：**

```
1. let res = util.printf("%s", "hello world!");
2. console.info(res);
3. // 输出结果：hello world!
```

## util.getErrorString(deprecated)

PhonePC/2in1TabletTVWearable

getErrorString(errno: number): string

获取系统错误码对应的详细信息。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[util.errnoToString9+](js-apis-util.md#utilerrnotostring9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| errno | number | 是 | 系统发生错误产生的错误码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 错误码对应的详细信息。 |

**示例：**

```
1. let errnum = -1; // -1 : a system error number
2. let result = util.getErrorString(errnum);
3. console.info("result = " + result);
4. // 输出结果：result = operation not permitted
```

## util.promiseWrapper(deprecated)

PhonePC/2in1TabletTVWearable

promiseWrapper(original: (err: Object, value: Object) => void): Object

接收一个采用“错误优先”回调模式的函数，即以(err, value) => callback作为最后一个参数，并返回其Promise函数。

说明

从API version 7开始支持，从API version 9开始废弃，此接口不可用，建议使用[util.promisify9+](js-apis-util.md#utilpromisify9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| original | (err: Object, value: Object) => void | 是 | 异步函数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Object | 返回promise函数，采用遵循常见的错误优先的回调风格的函数（也就是将(err, value) => ...回调作为最后一个参数）。 |

## util.getHash12+

PhonePC/2in1TabletTVWearable

getHash(object: object): number

获取对象的Hash值。

首次获取时，则计算Hash值并保存到对象的Hash域（返回随机的Hash值）；后续获取时，直接从Hash域中返回Hash值（同一对象多次返回值保持不变）。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| object | object | 是 | 需要获取Hash值的对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | Hash值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. interface Person {
2. name: string,
3. age: number
4. }
5. let obj: Person = { name: 'Jack', age: 20 };
6. let result1 = util.getHash(obj);
7. console.info('result1 is ' + result1);
8. let result2 = util.getHash(obj);
9. console.info('result2 is ' + result2);
10. // 输出结果：result1 与 result2 的值相等，且为随机的Hash值。
```

## util.getMainThreadStackTrace20+

PhonePC/2in1TabletTVWearable

getMainThreadStackTrace(): string

获取主线程的栈追踪信息，最多返回64层调用帧。

该接口可能对主线程性能产生影响，建议仅在必要时使用，如日志记录、错误分析或调试场景。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 主线程的栈追踪信息。若主线程未处于执行JS代码状态，则返回空字符串。 |

**示例：**

```
1. let stack = util.getMainThreadStackTrace();
2. console.info(stack);
3. // 输出当前主线程的栈追踪信息。
```

## ArkTSVM23+

PhonePC/2in1TabletTVWearable

ArkTSVM是一个类，用于给开发者提供虚拟机的维测能力。

### setMultithreadingDetectionEnabled23+

PhonePC/2in1TabletTVWearable

static setMultithreadingDetectionEnabled(enabled: boolean): void

若enabled为true则开启，为false则关闭。开启多线程检测，多线程问题的cppcrash文件里会包含多线程信息。关闭多线程检测，则多线程问题的cppcrash文件里不会包含多线程信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 控制多线程检测开关的开启或关闭 。true表示开启，false表示关闭。 |

**示例：**

```
1. import { util } from '@kit.ArkTS';

3. // 打开多线程检测开关
4. util.ArkTSVM.setMultithreadingDetectionEnabled(true);
5. // 关闭多线程检测开关
6. util.ArkTSVM.setMultithreadingDetectionEnabled(false);
```

## TextDecoderOptions11+

PhonePC/2in1TabletTVWearable

解码相关选项参数，包含两个属性fatal和ignoreBOM。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fatal | boolean | 否 | 是 | 是否显示致命错误，true表示显示致命错误，false表示不显示致命错误，默认值是false。 |
| ignoreBOM | boolean | 否 | 是 | 是否忽略BOM标记，true表示忽略待解码数据的BOM标记，false表示会对BOM标记解码，默认值是false。 |

## DecodeToStringOptions12+

PhonePC/2in1TabletTVWearable

用于配置decodeToString方法在解码字节流时的行为参数。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| stream | boolean | 否 | 是 | 输入末尾出现的不完整字节序列是否需要追加在下次调用decodeToString的参数中处理。设置为true，则不完整的字节序列会存储在内部缓存区直到下次调用该函数，false则会在当前调用时直接解码。默认为false。 |

## DecodeWithStreamOptions11+

PhonePC/2in1TabletTVWearable

解码是否跟随附加数据块相关选项参数。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| stream | boolean | 否 | 是 | 在随后的[decodeWithStream](js-apis-util.md#decodewithstreamdeprecated)调用中是否跟随附加数据块。如果以块的形式处理数据，则设置为true；如果处理最后的数据未分块，则设置为false。默认为false。 |

## Aspect11+

PhonePC/2in1TabletTVWearable

Aspect类用于封装提供切面能力（Aspect Oriented Programming，简写AOP）的接口，这些接口可用于对类方法进行前后插桩或替换实现。

### addBefore11+

PhonePC/2in1TabletTVWearable

static addBefore(targetClass: Object, methodName: string, isStatic: boolean, before: Function): void

在指定的类对象的原方法执行前插入一个函数。执行addBefore接口后，先运行插入的函数逻辑，再执行指定类对象的原方法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| targetClass | Object | 是 | 指定的类对象。 |
| methodName | string | 是 | 指定的原方法名，不支持read-only方法。 |
| isStatic | boolean | 是 | 指定的原方法是否为静态方法。true表示静态方法，false表示实例方法。 |
| before | Function | 是 | 要插入的函数对象。函数有参数，则第一个参数是this对象（若isStatic为true，则为类对象即targetClass；若isStatic为false，则为调用方法的实例对象），其余参数是原方法的参数。函数也可以无参数，无参时不做处理。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. class MyClass {
2. msg: string = 'msg000';
3. foo(arg: string): string {
4. console.info('foo arg is ' + arg);
5. return this.msg;
6. }

8. static data: string = 'data000';
9. static bar(arg: string): string {
10. console.info('bar arg is ' + arg);
11. return MyClass.data;
12. }
13. }

15. let asp = new MyClass();
16. let result = asp.foo('123');
17. // 输出结果：foo arg is 123
18. console.info('result is ' + result);
19. // 输出结果：result is msg000
20. console.info('asp.msg is ' + asp.msg);
21. // 输出结果：asp.msg is msg000

23. util.Aspect.addBefore(MyClass, 'foo', false, (instance: MyClass, arg: string) => {
24. console.info('arg is ' + arg);
25. instance.msg = 'msg111';
26. console.info('msg is changed to ' + instance.msg);
27. });

29. result = asp.foo('123');
30. // 输出结果：arg is 123
31. // 输出结果：msg is changed to msg111
32. // 输出结果：foo arg is 123
33. console.info('result is ' + result);
34. // 输出结果：result is msg111
35. console.info('asp.msg is ' + asp.msg);
36. // 输出结果：asp.msg is msg111

39. let res = MyClass.bar('456');
40. // 输出结果：bar arg is 456
41. console.info('res is ' + res);
42. // 输出结果：res is data000
43. console.info('MyClass.data is ' + MyClass.data);
44. // 输出结果：MyClass.data is data000

46. util.Aspect.addBefore(MyClass, 'bar', true, (target: Object, arg: string) => {
47. console.info('arg is ' + arg);
48. let newVal = 'data111';
49. Reflect.set(target, 'data', newVal);
50. console.info('data is changed to ' + newVal);
51. });

53. res = MyClass.bar('456');
54. // 输出结果：arg is 456
55. // 输出结果：data is changed to data111
56. // 输出结果：bar arg is 456
57. console.info('res is ' + res);
58. // 输出结果：res is data111
59. console.info('MyClass.data is ' + MyClass.data);
60. // 输出结果：MyClass.data is data111
```

### addAfter11+

PhonePC/2in1TabletTVWearable

static addAfter(targetClass: Object, methodName: string, isStatic: boolean, after: Function): void

在指定的类方法执行后插入一段逻辑。最终返回插入函数执行后的返回值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| targetClass | Object | 是 | 指定的类对象。 |
| methodName | string | 是 | 指定的原方法名，不支持read-only方法。 |
| isStatic | boolean | 是 | 指定的原方法是否为静态方法。true表示静态方法，false表示实例方法。 |
| after | Function | 是 | 要插入的函数。函数有参数时，则第一个参数是this对象（若isStatic为true，则为类对象即targetClass；若isStatic为false，则为调用方法的实例对象），第二个参数是原方法的返回值（如果原方法没有返回值，则为undefined），其余参数是原方法的参数。函数也可以无参，无参时不做处理。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. class MyClass {
2. msg: string = 'msg000';
3. foo(arg: string): string {
4. console.info('foo arg is ' + arg);
5. return this.msg;
6. }
7. }

9. let asp = new MyClass();
10. let result = asp.foo('123');
11. // 输出结果：foo arg is 123
12. console.info('result is ' + result);
13. // 输出结果：result is msg000
14. console.info('asp.msg is ' + asp.msg);
15. // 输出结果：asp.msg is msg000

17. util.Aspect.addAfter(MyClass, 'foo', false, (instance: MyClass, ret: string, arg: string): string => {
18. console.info('arg is ' + arg);
19. console.info('ret is ' + ret);
20. instance.msg = 'msg111';
21. console.info('msg is changed to ' + instance.msg);
22. return 'msg222';
23. });

25. result = asp.foo('123');
26. // 输出结果：foo arg is 123
27. // 输出结果：arg is 123
28. // 输出结果：ret is msg000
29. // 输出结果：msg is changed to msg111
30. console.info('result is ' + result);
31. // 输出结果：result is msg222
32. console.info('asp.msg is ' + asp.msg);
33. // 输出结果：asp.msg is msg111

35. // 前后插桩的例子
36. class AroundTest {
37. foo(arg: string) {
38. console.info('execute foo with arg ' + arg);
39. }
40. }
41. util.Aspect.addBefore(AroundTest, 'foo', false, () => {
42. console.info('execute before');
43. });
44. util.Aspect.addAfter(AroundTest, 'foo', false, () => {
45. console.info('execute after');
46. });

48. (new AroundTest()).foo('hello');
49. // 输出结果：execute before
50. // 输出结果：execute foo with arg hello
51. // 输出结果：execute after
```

### replace11+

PhonePC/2in1TabletTVWearable

static replace(targetClass: Object, methodName: string, isStatic: boolean, instead: Function) : void

将指定类的原方法替换为另一个函数。replace接口执行完成后，调用指定的类方法时，仅执行替换后的逻辑。最终返回替换函数执行完毕的返回值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| targetClass | Object | 是 | 指定的类对象。 |
| methodName | string | 是 | 指定的原方法名，不支持read-only方法。 |
| isStatic | boolean | 是 | 指定的原方法是否为静态方法。true表示静态方法，false表示实例方法。 |
| instead | Function | 是 | 要用来替换原方法的函数。函数有参数时，则第一个参数是this对象（若isStatic为true，则为类对象即targetClass；若isStatic为false，则为调用方法的实例对象），其余参数是原方法的参数。函数也可以无参，无参时不做处理。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. class MyClass {
2. msg: string = 'msg000';
3. foo(arg: string): string {
4. console.info('foo arg is ' + arg);
5. return this.msg;
6. }
7. }

9. let asp = new MyClass();
10. let result = asp.foo('123');
11. // 输出结果：foo arg is 123
12. console.info('result is ' + result);
13. // 输出结果：result is msg000
14. console.info('asp.msg is ' + asp.msg);
15. // 输出结果：asp.msg is msg000

17. util.Aspect.replace(MyClass, 'foo', false, (instance: MyClass, arg: string): string => {
18. console.info('execute instead');
19. console.info('arg is ' + arg);
20. instance.msg = 'msg111';
21. console.info('msg is changed to ' + instance.msg);
22. return 'msg222';
23. });

25. result = asp.foo('123');
26. // 输出结果：execute instead
27. // 输出结果：arg is 123
28. // 输出结果：msg is changed to msg111
29. console.info('result is ' + result);
30. // 输出结果：result is msg222
31. console.info('asp.msg is ' + asp.msg);
32. // 输出结果：asp.msg is msg111
```

## TextDecoder

PhonePC/2in1TabletTVWearable

TextDecoder用于将字节数组解码为字符串，支持utf-8、utf-16le/be、iso-8859和windows-1251等不同的编码格式。

### 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** 以下各项对应的系统能力均为SystemCapability.Utils.Lang。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| encoding | string | 是 | 否 | 编码格式。  - 支持格式：utf-8、ibm866、iso-8859-2、iso-8859-3、iso-8859-4、iso-8859-5、iso-8859-6、iso-8859-7、iso-8859-8、iso-8859-8-i、iso-8859-10、iso-8859-13、iso-8859-14、iso-8859-15、koi8-r、koi8-u、macintosh、windows-874、windows-1250、windows-1251、windows-1252、windows-1253、windows-1254、windows-1255、windows-1256、windows-1257、windows-1258、x-mac-cyrillic、gbk、gb18030、big5、euc-jp、iso-2022-jp、shift\_jis、euc-kr、utf-16be、utf-16le、gb2312、iso-8859-1。 |
| fatal | boolean | 是 | 否 | 是否显示致命错误，true表示显示，false表示不显示。 |
| ignoreBOM | boolean | 是 | 否 | 是否忽略BOM（byte order marker）标记，默认值为false，表示解码结果包含BOM标记。 |

### constructor9+

PhonePC/2in1TabletTVWearable

constructor()

TextDecoder的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**示例：**

```
1. let textDecoder = new util.TextDecoder();
2. let retStr = textDecoder.encoding;
3. console.info('retStr = ' + retStr);
4. // 输出结果：retStr = utf-8
```

### create9+

PhonePC/2in1TabletTVWearable

static create(encoding?: string, options?: TextDecoderOptions): TextDecoder

替代有参构造函数的功能。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| encoding | string | 否 | 编码格式，默认值是'utf-8'。 |
| options | [TextDecoderOptions](js-apis-util.md#textdecoderoptions11) | 否 | 解码相关选项参数，存在两个属性fatal和ignoreBOM。此参数不填时，对应各属性取其默认值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TextDecoder](js-apis-util.md#textdecoder) | 返回一个TextDecoder对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |

**示例：**

```
1. let textDecoderOptions: util.TextDecoderOptions = {
2. fatal: false,
3. ignoreBOM : true
4. }
5. let textDecoder = util.TextDecoder.create('utf-8', textDecoderOptions);
6. let retStr = textDecoder.encoding;
7. console.info('retStr = ' + retStr);
8. // 输出结果：retStr = utf-8
```

### decodeToString12+

PhonePC/2in1TabletTVWearable

decodeToString(input: Uint8Array, options?: DecodeToStringOptions): string

将输入参数解码后输出对应文本。

说明

该接口会正常解析值为\0的字节，将其转换为Unicode字符\u0000（空字符），不会导致解码中断或错误。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| input | Uint8Array | 是 | 需要解码的数组。 |
| options | [DecodeToStringOptions](js-apis-util.md#decodetostringoptions12) | 否 | 解码相关选项参数。默认undefined。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 解码后的数据。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. // 当解析不含有\0的字节的示例代码
2. let textDecoderOptions: util.TextDecoderOptions = {
3. fatal: false,
4. ignoreBOM : true
5. }
6. let decodeToStringOptions: util.DecodeToStringOptions = {
7. stream: false
8. }
9. let textDecoder = util.TextDecoder.create('utf-8', textDecoderOptions);
10. let uint8 = new Uint8Array([0xEF, 0xBB, 0xBF, 0x61, 0x62, 0x63]);
11. let retStr = textDecoder.decodeToString(uint8, decodeToStringOptions);
12. console.info("retStr = " + retStr);
13. // 输出结果：retStr = abc
```

```
1. // 当解析含有\0的字节的示例代码
2. let textDecoderOptions: util.TextDecoderOptions = {
3. fatal: false,
4. ignoreBOM : true
5. }
6. let decodeToStringOptions: util.DecodeToStringOptions = {
7. stream: false
8. }
9. let textDecoder = util.TextDecoder.create('utf-8', textDecoderOptions);
10. let uint8 = new Uint8Array([97, 98, 0, 99]);
11. let retStr = textDecoder.decodeToString(uint8, decodeToStringOptions);
12. console.info("retStr = " + retStr);
13. // 输出结果：retStr = abc
14. let retJson = JSON.stringify(retStr)
15. console.info("retJson = " + retJson);
16. // 输出结果：retJson = ab/u0000c
```

### decodeWithStream(deprecated)

PhonePC/2in1TabletTVWearable

decodeWithStream(input: Uint8Array, options?: DecodeWithStreamOptions): string

将输入参数解码后输出对应文本。当input是一个空数组时，返回undefined。

说明

从API version 9开始支持，从API version 12开始废弃，建议使用[decodeToString12+](js-apis-util.md#decodetostring12)替代。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| input | Uint8Array | 是 | 符合格式需要解码的数组。 |
| options | [DecodeWithStreamOptions](js-apis-util.md#decodewithstreamoptions11) | 否 | 解码相关选项参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 解码后的数据。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. let textDecoderOptions: util.TextDecoderOptions = {
2. fatal: false,
3. ignoreBOM : true
4. }
5. let decodeWithStreamOptions: util.DecodeWithStreamOptions = {
6. stream: false
7. }
8. let textDecoder = util.TextDecoder.create('utf-8', textDecoderOptions);
9. let uint8 = new Uint8Array(6);
10. uint8[0] = 0xEF;
11. uint8[1] = 0xBB;
12. uint8[2] = 0xBF;
13. uint8[3] = 0x61;
14. uint8[4] = 0x62;
15. uint8[5] = 0x63;
16. console.info("input num:");
17. let retStr = textDecoder.decodeWithStream(uint8, decodeWithStreamOptions);
18. console.info("retStr = " + retStr);
19. // 输出结果：retStr = abc
```

### constructor(deprecated)

PhonePC/2in1TabletTVWearable

constructor(encoding?: string, options?: { fatal?: boolean; ignoreBOM?: boolean })

TextDecoder的构造函数。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[create9+](js-apis-util.md#create9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| encoding | string | 否 | 编码格式，默认值是'utf-8'。 |
| options | { fatal?: boolean; ignoreBOM?: boolean } | 否 | 解码相关选项参数，存在两个属性fatal和ignoreBOM。 |

**表1** options

| 名称 | 参数类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fatal | boolean | 否 | 是否显示致命错误，true表示显示致命错误，false表示不显示致命错误，默认值是false。 |
| ignoreBOM | boolean | 否 | 是否忽略BOM标记，true表示忽略待解码数据的BOM标记，false表示会对BOM标记解码，默认值是false。 |

**示例：**

```
1. let textDecoder = new util.TextDecoder("utf-8",{ignoreBOM: true});
```

### decode(deprecated)

PhonePC/2in1TabletTVWearable

decode(input: Uint8Array, options?: { stream?: false }): string

通过输入参数解码后输出对应文本。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[decodeToString12+](js-apis-util.md#decodetostring12)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| input | Uint8Array | 是 | 符合格式需要解码的数组。 |
| options | { stream?: false } | 否 | 解码相关选项参数。 |

**表2** options

| 名称 | 参数类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| stream | boolean | 否 | 在随后的decode()调用中是否跟随附加数据块。如果以块的形式处理数据，则设置为true；如果处理数据未分块，则设置为false。默认为false。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 解码后的数据。 |

**示例：**

```
1. let textDecoder = new util.TextDecoder("utf-8",{ignoreBOM: true});
2. let uint8 = new Uint8Array(6);
3. uint8[0] = 0xEF;
4. uint8[1] = 0xBB;
5. uint8[2] = 0xBF;
6. uint8[3] = 0x61;
7. uint8[4] = 0x62;
8. uint8[5] = 0x63;
9. console.info("input num:");
10. let retStr = textDecoder.decode(uint8, {stream: false});
11. console.info("retStr = " + retStr);
12. // 输出结果：retStr = abc
```

## EncodeIntoUint8ArrayInfo11+

PhonePC/2in1TabletTVWearable

编码后的信息，包含读取的字符数和写入的字节数。

### 属性

PhonePC/2in1TabletTVWearable

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| read | number | 是 | 否 | 已读取的字符数。 |
| written | number | 是 | 否 | 已写入的字节数。 |

## TextEncoder

PhonePC/2in1TabletTVWearable

TextEncoder将字符串编码为字节数组，支持多种编码格式。

在使用TextEncoder进行编码时，需要注意不同编码格式下字符所占的字节数不同。务必明确指定编码格式，以确保编码结果正确。

### 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** 以下各项对应的系统能力均为SystemCapability.Utils.Lang。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| encoding | string | 是 | 否 | 编码格式。  - 支持格式：utf-8、gb2312、gb18030、ibm866、iso-8859-1、iso-8859-2、iso-8859-3、iso-8859-4、iso-8859-5、iso-8859-6、iso-8859-7、iso-8859-8、iso-8859-8-i、iso-8859-10、iso-8859-13、iso-8859-14、iso-8859-15、koi8-r、koi8-u、macintosh、windows-874、windows-1250、windows-1251、windows-1252、windows-1253、windows-1254、windows-1255、windows-1256、windows-1257、windows-1258、gbk、big5、euc-jp、iso-2022-jp、shift\_jis、euc-kr、x-mac-cyrillic、utf-16be、utf-16le。  - 默认值是：'utf-8'。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor()

TextEncoder的构造函数。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**示例：**

```
1. let textEncoder = new util.TextEncoder();
```

### constructor9+

PhonePC/2in1TabletTVWearable

constructor(encoding?: string)

TextEncoder的构造函数。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| encoding | string | 否 | 编码格式，默认值为'utf-8'。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |

**示例：**

```
1. let textEncoder = new util.TextEncoder("utf-8");
```

### create12+

PhonePC/2in1TabletTVWearable

static create(encoding?: string): TextEncoder

创建TextEncoder对象的方法。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| encoding | string | 否 | 编码格式，默认值为'utf-8'。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TextEncoder](js-apis-util.md#textencoder) | 返回一个TextEncoder对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |

**示例：**

```
1. let textEncoder = util.TextEncoder.create("utf-8");
```

### encodeInto9+

PhonePC/2in1TabletTVWearable

encodeInto(input?: string): Uint8Array

将输入参数编码后输出Uint8Array对象。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| input | string | 否 | 需要编码的字符串，默认值是空字符串。当入参是空字符串时，返回undefined。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 返回编码后的Uint8Array对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |

**示例：**

```
1. let textEncoder = new util.TextEncoder();
2. let result = textEncoder.encodeInto("\uD800¥¥");
3. console.info("result = " + result);
4. // 输出结果: result = 237,160,128,194,165,194,165
```

### encodeIntoUint8Array9+

PhonePC/2in1TabletTVWearable

encodeIntoUint8Array(input: string, dest: Uint8Array): EncodeIntoUint8ArrayInfo

对字符串进行编码，将结果存储到dest数组。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| input | string | 是 | 需要编码的字符串。 |
| dest | Uint8Array | 是 | Uint8Array对象实例，用于将生成的utf-8编码文本放入其中。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [EncodeIntoUint8ArrayInfo](js-apis-util.md#encodeintouint8arrayinfo11) | 返回一个对象，read表示已编码的字符数，written表示编码字符所占用的字节数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. let textEncoder = new util.TextEncoder();
2. let buffer = new ArrayBuffer(4);
3. let uint8 = new Uint8Array(buffer);
4. let result = textEncoder.encodeIntoUint8Array('abcd', uint8);
5. console.info("uint8 = " + uint8);
6. // 输出结果: uint8 = 97,98,99,100
7. console.info("result.read = " + result.read);
8. // 输出结果: result.read = 4
9. console.info("result.written = " + result.written);
10. // 输出结果: result.written = 4
```

### encodeInto(deprecated)

PhonePC/2in1TabletTVWearable

encodeInto(input: string, dest: Uint8Array): { read: number; written: number }

将生成的utf-8编码文本写入dest数组。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[encodeIntoUint8Array9+](js-apis-util.md#encodeintouint8array9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| input | string | 是 | 需要编码的字符串。 |
| dest | Uint8Array | 是 | Uint8Array对象实例，用于将生成的utf-8编码文本放入其中。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| { read: number; written: number } | 返回一个对象，read表示已编码的字符数，written表示编码字符所占用的字节数。 |

**示例：**

```
1. let textEncoder = new util.TextEncoder();
2. let buffer = new ArrayBuffer(4);
3. let uint8 = new Uint8Array(buffer);
4. let result = textEncoder.encodeInto('abcd', uint8);
5. console.info("uint8 = " + uint8);
6. // 输出结果: uint8 = 97,98,99,100
```

### encode(deprecated)

PhonePC/2in1TabletTVWearable

encode(input?: string): Uint8Array

将输入参数编码后输出对应文本。

说明

从API version 7开始支持，从API version 9开始废弃，建议使用[encodeInto9+](js-apis-util.md#encodeinto9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| input | string | 否 | 需要编码的字符串，默认值是空字符串。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 返回编码后的文本。 |

**示例：**

```
1. let textEncoder = new util.TextEncoder();
2. let result = textEncoder.encode("\uD800¥¥");
3. console.info("result = " + result);
4. // 输出结果: result = 237,160,128,194,165,194,165
```

## RationalNumber8+

PhonePC/2in1TabletTVWearable

RationalNumber主要用于有理数的比较，并提供获取分子和分母的方法。使用toString()方法可以将有理数转换为字符串形式，使用该类可以方便地进行有理数的各种操作。

### constructor9+

PhonePC/2in1TabletTVWearable

constructor()

RationalNumber的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**示例：**

```
1. let rationalNumber = new util.RationalNumber();
```

### parseRationalNumber9+

PhonePC/2in1TabletTVWearable

static parseRationalNumber(numerator: number,denominator: number): RationalNumber

创建具有给定分子和分母的RationalNumber实例。

说明

该接口要求参数numerator和denominator必须是整数类型。如果传入的参数是小数类型，不会进行拦截，但是会输出错误信息："parseRationalNumber: The type of Parameter must be integer"。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| numerator | number | 是 | 分子，整数类型。取值范围：-Number.MAX\_VALUE <= numerator <= Number.MAX\_VALUE。 |
| denominator | number | 是 | 分母，整数类型。取值范围：-Number.MAX\_VALUE <= denominator <= Number.MAX\_VALUE。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RationalNumber](js-apis-util.md#rationalnumber8) | RationalNumber对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. let rationalNumber = util.RationalNumber.parseRationalNumber(1,2);
```

### createRationalFromString8+

PhonePC/2in1TabletTVWearable

static createRationalFromString(rationalString: string): RationalNumber

使用给定的字符串创建RationalNumber对象。

说明

该接口要求参数rationalString是字符串格式。如果传入的参数是小数类型字符串格式，不会进行拦截，但是会输出错误信息："createRationalFromString: The type of Parameter must be integer string"。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rationalString | string | 是 | 字符串格式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RationalNumber](js-apis-util.md#rationalnumber8)​ | RationalNumber对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The type of rationalString must be string. |

**示例：**

```
1. let rational = util.RationalNumber.createRationalFromString("3/4");
```

### compare9+

PhonePC/2in1TabletTVWearable

compare(another: RationalNumber): number​

将当前RationalNumber对象与目标RationalNumber对象进行比较，并返回比较结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| another | [RationalNumber](js-apis-util.md#rationalnumber8) | 是 | 其他的有理数对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 两个对象相等时返回0；给定对象小于当前对象时返回1；给定对象大于当前对象时返回-1。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. let rationalNumber = util.RationalNumber.parseRationalNumber(1,2);
2. let rational = util.RationalNumber.createRationalFromString("3/4");
3. let result = rationalNumber.compare(rational);
4. console.info("result = " + result);
5. // 输出结果：result = -1
```

### valueOf8+

PhonePC/2in1TabletTVWearable

valueOf(): number

获取当前RationalNumber对象的整数或浮点数值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回整数或者浮点数的值。 |

**示例：**

```
1. let rationalNumber = new util.RationalNumber(1,2);
2. let result = rationalNumber.valueOf();
3. console.info("result = " + result);
4. // 输出结果：result = 0.5
```

API 9及以上建议使用以下写法：

```
1. let rationalNumber = util.RationalNumber.parseRationalNumber(1,2);
2. let result = rationalNumber.valueOf();
3. console.info("result = " + result);
4. // 输出结果：result = 0.5
```

### equals8+

PhonePC/2in1TabletTVWearable

equals(obj: Object): boolean

比较当前的RationalNumber对象与给定对象是否相等。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| obj | Object | 是 | 其他类型对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果给定对象与当前对象相同，则返回true；否则返回false。 |

**示例：**

```
1. let rationalNumber = new util.RationalNumber(1,2);
2. let rational = util.RationalNumber.createRationalFromString("3/4");
3. let result = rationalNumber.equals(rational);
4. console.info("result = " + result);
5. // 输出结果：result = false
```

API 9及以上建议使用以下写法：

```
1. let rationalNumber = util.RationalNumber.parseRationalNumber(1,2);
2. let rational = util.RationalNumber.createRationalFromString("3/4");
3. let result = rationalNumber.equals(rational);
4. console.info("result = " + result);
5. // 输出结果：result = false
```

### getCommonFactor9+

PhonePC/2in1TabletTVWearable

static getCommonFactor(number1: number, number2: number): number

获取两个整数的最大公约数。

说明

该接口要求参数number1和number2必须是整数类型。如果传入的参数是小数类型，不会进行拦截，但是会输出错误信息："getCommonFactor: The type of Parameter must be integer"。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| number1 | number | 是 | 整数类型。-Number.MAX\_VALUE <= number1 <= Number.MAX\_VALUE。 |
| number2 | number | 是 | 整数类型。-Number.MAX\_VALUE <= number2 <= Number.MAX\_VALUE。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回两个给定数字的最大公约数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. let result = util.RationalNumber.getCommonFactor(4,6);
2. console.info("result = " + result);
3. // 输出结果：result = 2
```

### getNumerator8+

PhonePC/2in1TabletTVWearable

getNumerator(): number

获取当前RationalNumber对象的分子。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回RationalNumber对象的分子。 |

**示例：**

```
1. let rationalNumber = new util.RationalNumber(1,2);
2. let result = rationalNumber.getNumerator();
3. console.info("result = " + result);
4. // 输出结果：result = 1
```

API 9及以上建议使用以下写法：

```
1. let rationalNumber = util.RationalNumber.parseRationalNumber(1,2);
2. let result = rationalNumber.getNumerator();
3. console.info("result = " + result);
4. // 输出结果：result = 1
```

### getDenominator8+

PhonePC/2in1TabletTVWearable

getDenominator(): number

获取当前RationalNumber对象的分母。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回RationalNumber对象的分母。 |

**示例：**

```
1. let rationalNumber = new util.RationalNumber(1,2);
2. let result = rationalNumber.getDenominator();
3. console.info("result = " + result);
4. // 输出结果：result = 2
```

API 9及以上建议使用以下写法：

```
1. let rationalNumber = util.RationalNumber.parseRationalNumber(1,2)
2. let result = rationalNumber.getDenominator();
3. console.info("result = " + result);
4. // 输出结果：result = 2
```

### isZero8+

PhonePC/2in1TabletTVWearable

isZero():boolean

检查当前RationalNumber对象是否为0。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果当前对象的值为0，则返回true；否则返回false。 |

**示例：**

```
1. let rationalNumber = new util.RationalNumber(1,2);
2. let result = rationalNumber.isZero();
3. console.info("result = " + result);
4. // 输出结果：result = false
```

API 9及以上建议使用以下写法：

```
1. let rationalNumber = util.RationalNumber.parseRationalNumber(1,2);
2. let result = rationalNumber.isZero();
3. console.info("result = " + result);
4. // 输出结果：result = false
```

### isNaN8+

PhonePC/2in1TabletTVWearable

isNaN(): boolean

检查当前RationalNumber对象是否表示非数字(NaN)值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果分母和分子都为0，则返回true；否则返回false。 |

**示例：**

```
1. let rationalNumber = new util.RationalNumber(1,2);
2. let result = rationalNumber.isNaN();
3. console.info("result = " + result);
4. // 输出结果：result = false
```

API 9及以上建议使用以下写法：

```
1. let rationalNumber = util.RationalNumber.parseRationalNumber(1,2);
2. let result = rationalNumber.isNaN();
3. console.info("result = " + result);
4. // 输出结果：result = false
```

### isFinite8+

PhonePC/2in1TabletTVWearable

isFinite():boolean

检查RationalNumber对象是否表示一个有限值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果分母不为0，则返回true；否则返回false。 |

**示例：**

```
1. let rationalNumber = new util.RationalNumber(1,2);
2. let result = rationalNumber.isFinite();
3. console.info("result = " + result);
4. // 输出结果：result = true
```

API 9及以上建议使用以下写法：

```
1. let rationalNumber = util.RationalNumber.parseRationalNumber(1,2);
2. let result = rationalNumber.isFinite();
3. console.info("result = " + result);
4. // 输出结果：result = true
```

### toString8+

PhonePC/2in1TabletTVWearable

toString(): string

获取RationalNumber对象的字符串表示形式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回Numerator/Denominator格式的字符串，例如3/5，如果分子为0，则返回0/1。如果分母为0，则返回Infinity。如果分子和分母都为0，则返回NaN。 |

**示例：**

```
1. let rationalNumber = new util.RationalNumber(1,2);
2. let result = rationalNumber.toString();
3. console.info("result = " + result);
4. // 输出结果：result = 1/2
```

API 9及以上建议使用以下写法：

```
1. let rationalNumber = util.RationalNumber.parseRationalNumber(1,2);
2. let result = rationalNumber.toString();
3. console.info("result = " + result);
4. // 输出结果：result = 1/2
```

### constructor(deprecated)

PhonePC/2in1TabletTVWearable

constructor(numerator: number,denominator: number)

RationalNumber的构造函数。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[parseRationalNumber9+](js-apis-util.md#parserationalnumber9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| numerator | number | 是 | 分子，整数类型。 |
| denominator | number | 是 | 分母，整数类型。 |

**示例：**

```
1. let rationalNumber = new util.RationalNumber(1,2);
```

### compareTo(deprecated)

PhonePC/2in1TabletTVWearable

compareTo(another: RationalNumber): number​

比较当前的RationalNumber对象与给定的对象。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[compare9+](js-apis-util.md#compare9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| another | RationalNumber | 是 | 其他的有理数对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 如果两个对象相等，则返回0；如果给定对象小于当前对象，则返回1；如果给定对象大于当前对象，则返回-1。 |

**示例：**

```
1. let rationalNumber = new util.RationalNumber(1,2);
2. let rational = util.RationalNumber.createRationalFromString("3/4");
3. let result = rationalNumber.compareTo(rational);
4. console.info("result = " + result);
5. // 输出结果：result = -1
```

### getCommonDivisor(deprecated)

PhonePC/2in1TabletTVWearable

static getCommonDivisor(number1: number,number2: number): number

获取两个指定整数的最大公约数。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[getCommonFactor9+](js-apis-util.md#getcommonfactor9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| number1 | number | 是 | 整数类型。 |
| number2 | number | 是 | 整数类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回两个给定数字的最大公约数。 |

## LRUCache9+

PhonePC/2in1TabletTVWearable

LRUCache用于在缓存空间不足时，将近期最少使用的数据替换为新数据。此设计基于资源访问的考虑：近期访问的数据，可能在不久的将来会再次访问。因此最少访问的数据被认为价值最低，应当优先从缓存中移除。

### 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** 以下各项对应的系统能力均为SystemCapability.Utils.Lang。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| length | number | 是 | 否 | 当前缓冲区中值的总数。 |

**示例：**

```
1. let pro = new util.LRUCache<number, number>();
2. pro.put(2, 10);
3. pro.put(1, 8);
4. let result = pro.length;
5. console.info('result = ' + result);
6. // 输出结果：result = 2
```

### constructor9+

PhonePC/2in1TabletTVWearable

constructor(capacity?: number)

默认构造函数用于创建一个新的LRUCache实例，默认容量为64。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| capacity | number | 否 | 指示要为缓冲区自定义的容量，不传默认值为64，最大值不能超过2147483647。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Incorrect parameter types. |

**示例：**

```
1. let pro = new util.LRUCache<number, number>();
```

### updateCapacity9+

PhonePC/2in1TabletTVWearable

updateCapacity(newCapacity: number): void

更新缓冲区容量为指定值，如果newCapacity小于或等于0，则抛出异常。当缓冲区中值的总数大于指定容量时，会执行删除操作。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| newCapacity | number | 是 | 指示要为缓冲区自定义的容量，最大值不能超过2147483647。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. |

**示例：**

```
1. let pro = new util.LRUCache<number, number>();
2. pro.updateCapacity(100);
```

### toString9+

PhonePC/2in1TabletTVWearable

toString(): string

返回对象的字符串表示。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回对象的字符串表示形式。 |

**示例：**

```
1. let pro = new util.LRUCache<number, number>();
2. pro.put(2, 10);
3. pro.get(2);
4. pro.get(3);
5. console.info(pro.toString());
6. // 输出结果：LRUCache[ maxSize = 64, hits = 1, misses = 1, hitRate = 50% ]
7. // maxSize: 缓存区最大值 hits: 查询值匹配成功的次数 misses: 查询值匹配失败的次数 hitRate: 查询值匹配率
```

### getCapacity9+

PhonePC/2in1TabletTVWearable

getCapacity(): number

获取当前缓冲区的容量。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回当前缓冲区的容量。 |

**示例：**

```
1. let pro = new util.LRUCache<number, number>();
2. let result = pro.getCapacity();
3. console.info('result = ' + result);
4. // 输出结果：result = 64
```

### clear9+

PhonePC/2in1TabletTVWearable

clear(): void

清除当前缓冲区中的键值对。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**示例：**

```
1. let pro = new util.LRUCache<number, number>();
2. pro.put(2, 10);
3. let result = pro.length;
4. pro.clear();
5. let res = pro.length;
6. console.info('result = ' + result);
7. console.info('res = ' + res);
8. // 输出结果：result = 1
9. // 输出结果：res = 0
```

### getCreateCount9+

PhonePC/2in1TabletTVWearable

getCreateCount(): number

获取对象创建的次数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回创建对象的次数。 |

**示例：**

```
1. // 创建新类ChildLRUCache继承LRUCache，重写createDefault方法，返回一个非undefined的值。
2. class ChildLRUCache extends util.LRUCache<number, number> {
3. constructor() {
4. super();
5. }

7. createDefault(key: number): number {
8. return key;
9. }
10. }
11. let lru = new ChildLRUCache();
12. lru.put(2, 10);
13. lru.get(3);
14. lru.get(5);
15. let res = lru.getCreateCount();
16. console.info('res = ' + res);
17. // 输出结果：res = 2
```

### getMissCount9+

PhonePC/2in1TabletTVWearable

getMissCount(): number

获取查询值不匹配的次数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回查询值不匹配的次数。 |

**示例：**

```
1. let pro = new util.LRUCache<number, number>();
2. pro.put(2, 10);
3. pro.get(2);
4. let result = pro.getMissCount();
5. console.info('result = ' + result);
6. // 输出结果：result = 0
```

### getRemovalCount9+

PhonePC/2in1TabletTVWearable

getRemovalCount(): number

获取缓冲区键值对的回收次数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回缓冲区键值对回收的次数。 |

**示例：**

```
1. let pro = new util.LRUCache<number, number>();
2. pro.put(2, 10);
3. pro.updateCapacity(2);
4. pro.put(50, 22);
5. let result = pro.getRemovalCount();
6. console.info('result = ' + result);
7. // 输出结果：result = 0
```

### getMatchCount9+

PhonePC/2in1TabletTVWearable

getMatchCount(): number

获取查询值匹配成功的次数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回查询值匹配成功的次数。 |

**示例：**

```
1. let pro = new util.LRUCache<number, number>();
2. pro.put(2, 10);
3. pro.get(2);
4. let result = pro.getMatchCount();
5. console.info('result = ' + result);
6. // 输出结果：result = 1
```

### getPutCount9+

PhonePC/2in1TabletTVWearable

getPutCount(): number

获取将值添加到缓冲区的次数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回将值添加到缓冲区的次数。 |

**示例：**

```
1. let pro = new util.LRUCache<number, number>();
2. pro.put(2, 10);
3. let result = pro.getPutCount();
4. console.info('result = ' + result);
5. // 输出结果：result = 1
```

### isEmpty9+

PhonePC/2in1TabletTVWearable

isEmpty(): boolean

检查缓冲区是否为空。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果缓冲区不包含任何值，则返回true。 |

**示例：**

```
1. let pro = new util.LRUCache<number, number>();
2. pro.put(2, 10);
3. let result = pro.isEmpty();
4. console.info('result = ' + result);
5. // 输出结果：result = false
```

### get9+

PhonePC/2in1TabletTVWearable

get(key: K): V | undefined

返回键对应的值。当键不在缓冲区中时，通过[createDefault9+](js-apis-util.md#createdefault9)接口创建，若createDefault创建的值不为undefined时，此时会调用[afterRemoval9+](js-apis-util.md#afterremoval9)接口，返回createDefault创建的值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 | 要查询的键。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| V | undefined | 如果指定的键存在于缓冲区中，则返回与键关联的值；否则返回createDefault创建的值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. let pro = new util.LRUCache<number, number>();
2. pro.put(2, 10);
3. let result  = pro.get(2);
4. console.info('result = ' + result);
5. // 输出结果：result = 10
```

### put9+

PhonePC/2in1TabletTVWearable

put(key: K,value: V): V

将键值对添加到缓冲区，返回与添加的键关联的值。当缓冲区中值的总数超过容量时，执行删除操作。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 | 要添加的键。 |
| value | V | 是 | 指示与要添加的键关联的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| V | 返回与添加的键关联的值。如果键或值为空，则抛出此异常。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. let pro = new util.LRUCache<number, number>();
2. let result = pro.put(2, 10);
3. console.info('result = ' + result);
4. // 输出结果：result = 10
```

### values9+

PhonePC/2in1TabletTVWearable

values(): V[]

获取当前缓冲区中所有值，从最近最少访问到最近访问的顺序列表。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| V[] | 返回当前缓冲区中所有值的列表，顺序为从最近最少访问（Least Recent）到最近访问（Most Recent）。 |

**示例：**

```
1. let pro = new util.LRUCache<number, string>();
2. pro.put(1, 'A');
3. pro.put(2, "B");
4. pro.put(3, 'C');
5. pro.put(4, 'D')
6. pro.put(5, 'E')
7. pro.put(6, 'F')
8. let result = pro.values();
9. console.info('result = ' + result);
10. // 输出结果：result = A,B,C,D,E,F
11. pro.get(1);
12. pro.get(2);
13. result = pro.values();
14. console.info('result = ' + result);
15. // 输出结果：result = C,D,E,F,A,B
```

### keys9+

PhonePC/2in1TabletTVWearable

keys(): K[]

获取当前缓冲区中所有键，从最近最少访问到最近访问的顺序列表。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| K[] | 返回当前缓冲区中所有键的列表，顺序为从最近最少访问（Least Recent）到最近访问（Most Recent）。 |

**示例：**

```
1. let pro = new util.LRUCache<number, string>();
2. pro.put(1, 'A');
3. pro.put(2, "B");
4. pro.put(3, 'C');
5. pro.put(4, 'D')
6. pro.put(5, 'E')
7. pro.put(6, 'F')
8. let result = pro.keys();
9. console.info('result = ' + result);
10. // 输出结果：result = 1,2,3,4,5,6
11. pro.get(5);
12. pro.get(3);
13. result = pro.keys();
14. console.info('result = ' + result);
15. // 输出结果：result = 1,2,4,6,5,3
```

### remove9+

PhonePC/2in1TabletTVWearable

remove(key: K): V | undefined

从当前缓冲区中删除指定的键及其关联的值，并返回键关联的值。如果指定的键不存在，则返回undefined。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 | 要删除的键值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| V | undefined | 返回一个包含已删除键值对的Optional对象；如果key不存在，则返回undefined，如果key为null，则抛出异常。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. let pro = new util.LRUCache<number, number>();
2. pro.put(2, 10);
3. let result = pro.remove(20);
4. console.info('result = ' + result);
5. // 输出结果：result = undefined
```

### afterRemoval9+

PhonePC/2in1TabletTVWearable

afterRemoval(isEvict: boolean, key: K, value: V, newValue: V): void

删除值后执行后续操作，这些操作由开发者自行实现。本接口会在删除操作时被调用，如[get9+](js-apis-util.md#get9)、[put9+](js-apis-util.md#put9)、[remove9+](js-apis-util.md#remove9)、[clear9+](js-apis-util.md#clear9)、[updateCapacity9+](js-apis-util.md#updatecapacity9)接口。

说明

若此回调方法在[clear9+](js-apis-util.md#clear9)、[updateCapacity9+](js-apis-util.md#updatecapacity9)接口调用之后触发执行，传入的key和value参数类型为MapIterator，可参照示例二进行后续操作。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isEvict | boolean | 是 | 当因容量不足而调用该方法时，参数值设置为true，其他情况设置为false。 |
| key | K | 是 | 表示删除的键。 |
| value | V | 是 | 表示删除的值。 |
| newValue | V | 是 | 如果已调用put方法并且要添加的键已经存在，则参数值是关联的新值。其他情况下参数值为空。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例一：**

```
1. class ChildLRUCache<K, V> extends util.LRUCache<K, V> {
2. constructor(capacity?: number) {
3. super(capacity);
4. }

6. afterRemoval(isEvict: boolean, key: K, value: V, newValue: V): void {
7. if (isEvict === true) {
8. console.info('key = ' + key);
9. // 输出结果：key = 1
10. console.info('value = ' + value);
11. // 输出结果：value = 1
12. console.info('newValue = ' + newValue);
13. // 输出结果：newValue = null
14. }
15. }
16. }
17. let lru = new ChildLRUCache<number, number>(2);
18. lru.put(1, 1);
19. lru.put(2, 2);
20. lru.put(3, 3);
```

**示例二：**

```
1. class TestClass {
2. str:string = '';
3. constructor(input: string) {
4. this.str = input;
5. }
6. }

8. class ChildLRUCache extends util.LRUCache<string, TestClass> {
9. constructor(capacity?: number) {
10. super(capacity);
11. }

13. afterRemoval(isEvict: boolean, key: string, value: TestClass, newValue: TestClass): void {
14. if(value.toString().indexOf('[object Map Iterator]') >= 0) {
15. console.info('调用clear进入');
16. console.info('isEvict = ' + isEvict);
17. const keysIterator = (key as ESObject as IterableIterator<string>);
18. const valuesIterator = (value as ESObject as IterableIterator<TestClass>);

20. let keyEntry = keysIterator.next();
21. let valueEntry = valuesIterator.next();
22. while (!keyEntry.done && !valueEntry.done) {
23. console.info(`key = ${keyEntry.value}, valueStr = ${valueEntry.value.str}`);
24. keyEntry = keysIterator.next();
25. valueEntry = valuesIterator.next();
26. }
27. } else {
28. console.info('调用put进入');
29. console.info('isEvict = ' + isEvict);
30. console.info('key = ' + key + '  valueStr = ' + value.str);
31. }
32. }
33. }
34. let test1 = new TestClass('testA');
35. let test2 = new TestClass('testB');
36. let test3 = new TestClass('testC');
37. let lru = new ChildLRUCache(2);
38. lru.put('aa', test1);
39. lru.put('bb', test2);
40. lru.put('cc', test3);    // 删除'aa'键值对
41. lru.clear();             // 清空整个缓冲区
42. /*
43. 输出结果：调用put进入
44. isEvict = true
45. key = aa  valueStr = testA
46. 调用clear进入
47. isEvict = false
48. key = bb, valueStr = testB
49. key = cc, valueStr = testC
50. */
```

### contains9+

PhonePC/2in1TabletTVWearable

contains(key: K): boolean

检查当前缓冲区是否包含指定的键。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 | 要检查的键。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果缓冲区包含指定的键，则返回 true。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. let pro = new util.LRUCache<number, number>();
2. pro.put(2, 10);
3. let result = pro.contains(2);
4. console.info('result = ' + result);
5. // 输出结果：result = true
```

### createDefault9+

PhonePC/2in1TabletTVWearable

createDefault(key: K): V

如果在缓冲区未匹配到键，则执行后续操作，参数表示未匹配的键，返回与键关联的值，默认返回undefined。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 | 表示未匹配的键。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| V | 返回与键关联的值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. let pro = new util.LRUCache<number, number>();
2. let result = pro.createDefault(50);
3. console.info('result = ' + result);
4. // 输出结果：result = undefined
```

### entries9+

PhonePC/2in1TabletTVWearable

entries(): IterableIterator<[K, V]>

返回一个迭代器对象，用于按插入顺序遍历当前对象中的所有键值对（[key, value]）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| IterableIterator<[K, V]> | 返回一个可迭代数组。 |

**示例：**

```
1. let pro = new util.LRUCache<number, number>();
2. pro.put(2, 10);
3. pro.put(3, 15);
4. let pair = pro.entries();
5. for (let value of pair) {
6. console.info(value[0]+ ', '+ value[1]);
7. }
8. // 输出结果：
9. // 2, 10
10. // 3, 15
```

### [Symbol.iterator]9+

PhonePC/2in1TabletTVWearable

[Symbol.iterator](): IterableIterator<[K, V]>

返回键值对形式的二维数组。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| IterableIterator<[K, V]> | 返回一个键值对形式的二维数组。 |

**示例：**

```
1. let pro = new util.LRUCache<number, number>();
2. pro.put(2, 10);
3. pro.put(3, 15);

5. for (let value of pro) {
6. console.info(value[0]+ ', '+ value[1]);
7. }
8. // 输出结果：
9. // 2, 10
10. // 3, 15
```

## ScopeComparable8+

PhonePC/2in1TabletTVWearable

ScopeComparable类型的值需要实现compareTo方法，确保传入的数据具有可比性。

**系统能力：** SystemCapability.Utils.Lang

### compareTo8+

PhonePC/2in1TabletTVWearable

compareTo(other: ScopeComparable): boolean

比较两个值的大小，返回一个布尔值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | [ScopeComparable](js-apis-util.md#scopecomparable8) | 是 | 表示要比较的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 调用compareTo的值大于等于传入的值返回true，否则返回false。 |

**示例：**

构造新类，实现compareTo方法。后续示例代码中，均以此Temperature类为例。

```
1. class Temperature implements util.ScopeComparable {
2. private readonly _temp: number;

4. constructor(value: number) {
5. this._temp = value;
6. }

8. compareTo(value: Temperature) {
9. return this._temp >= value.getTemp();
10. }

12. getTemp() {
13. return this._temp;
14. }

16. toString(): string {
17. return this._temp.toString();
18. }
19. }
```

## ScopeType8+

PhonePC/2in1TabletTVWearable

type ScopeType = ScopeComparable | number

表示范围中的值的类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

| 类型 | 说明 |
| --- | --- |
| number | 表示值的类型为数字。 |
| [ScopeComparable](js-apis-util.md#scopecomparable8) | 表示值的类型为ScopeComparable。 |

## ScopeHelper9+

PhonePC/2in1TabletTVWearable

ScopeHelper接口用于描述一个字段的有效范围。构造函数用于创建具有指定下限和上限的对象，并要求这些对象必须具有可比性。

### constructor9+

PhonePC/2in1TabletTVWearable

constructor(lowerObj: ScopeType, upperObj: ScopeType)

创建指定下限和上限的作用域实例，返回一个ScopeHelper对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lowerObj | [ScopeType](js-apis-util.md#scopetype8) | 是 | 指定作用域实例的下限。 |
| upperObj | [ScopeType](js-apis-util.md#scopetype8) | 是 | 指定作用域实例的上限。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. class Temperature implements util.ScopeComparable {
2. private readonly _temp: number;

4. constructor(value: number) {
5. this._temp = value;
6. }

8. compareTo(value: Temperature) {
9. return this._temp >= value.getTemp();
10. }

12. getTemp() {
13. return this._temp;
14. }

16. toString(): string {
17. return this._temp.toString();
18. }
19. }
20. let tempLower = new Temperature(30);
21. let tempUpper = new Temperature(40);
22. let range = new util.ScopeHelper(tempLower, tempUpper);
23. console.info("range = " + range);
24. // 输出结果：range = [30, 40]
```

### toString9+

PhonePC/2in1TabletTVWearable

toString(): string

该字符串化方法返回当前范围的字符串表示形式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回当前范围的字符串表示形式。 |

**示例：**

```
1. class Temperature implements util.ScopeComparable {
2. private readonly _temp: number;

4. constructor(value: number) {
5. this._temp = value;
6. }

8. compareTo(value: Temperature) {
9. return this._temp >= value.getTemp();
10. }

12. getTemp() {
13. return this._temp;
14. }

16. toString(): string {
17. return this._temp.toString();
18. }
19. }

21. let tempLower = new Temperature(30);
22. let tempUpper = new Temperature(40);
23. let range = new util.ScopeHelper(tempLower, tempUpper);
24. let result = range.toString();
25. console.info("result = " + result);
26. // 输出结果：result = [30, 40]
```

### intersect9+

PhonePC/2in1TabletTVWearable

intersect(range: ScopeHelper): ScopeHelper

获取给定范围和当前范围的交集。当交集为空集时，抛出异常。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| range | [ScopeHelper](js-apis-util.md#scopehelper9) | 是 | 传入给定范围。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ScopeHelper](js-apis-util.md#scopehelper9) | 返回给定范围和当前范围的交集。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. class Temperature implements util.ScopeComparable {
2. private readonly _temp: number;

4. constructor(value: number) {
5. this._temp = value;
6. }

8. compareTo(value: Temperature) {
9. return this._temp >= value.getTemp();
10. }

12. getTemp() {
13. return this._temp;
14. }

16. toString(): string {
17. return this._temp.toString();
18. }
19. }

21. let tempLower = new Temperature(30);
22. let tempUpper = new Temperature(40);
23. let range = new util.ScopeHelper(tempLower, tempUpper);
24. let tempMiDF = new Temperature(35);
25. let tempMidS = new Temperature(39);
26. let rangeFir = new util.ScopeHelper(tempMiDF, tempMidS);
27. let result = range.intersect(rangeFir);
28. console.info("result = " + result);
29. // 输出结果：result = [35, 39]
```

### intersect9+

PhonePC/2in1TabletTVWearable

intersect(lowerObj:ScopeType,upperObj:ScopeType):ScopeHelper

获取当前范围与指定下限和上限范围的交集。当交集为空集时，抛出异常。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lowerObj | [ScopeType](js-apis-util.md#scopetype8) | 是 | 给定范围的下限。 |
| upperObj | [ScopeType](js-apis-util.md#scopetype8) | 是 | 给定范围的上限。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ScopeHelper](js-apis-util.md#scopehelper9) | 返回当前范围与给定下限和上限范围的交集。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. class Temperature implements util.ScopeComparable {
2. private readonly _temp: number;

4. constructor(value: number) {
5. this._temp = value;
6. }

8. compareTo(value: Temperature) {
9. return this._temp >= value.getTemp();
10. }

12. getTemp() {
13. return this._temp;
14. }

16. toString(): string {
17. return this._temp.toString();
18. }
19. }

21. let tempLower = new Temperature(30);
22. let tempUpper = new Temperature(40);
23. let tempMiDF = new Temperature(35);
24. let tempMidS = new Temperature(39);
25. let range = new util.ScopeHelper(tempLower, tempUpper);
26. let result = range.intersect(tempMiDF, tempMidS);
27. console.info("result = " + result);
28. // 输出结果：result = [35, 39]
```

### getUpper9+

PhonePC/2in1TabletTVWearable

getUpper(): ScopeType

获取当前范围的上限。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ScopeType](js-apis-util.md#scopetype8) | 返回当前范围的上限值。 |

**示例：**

```
1. class Temperature implements util.ScopeComparable {
2. private readonly _temp: number;

4. constructor(value: number) {
5. this._temp = value;
6. }

8. compareTo(value: Temperature) {
9. return this._temp >= value.getTemp();
10. }

12. getTemp() {
13. return this._temp;
14. }

16. toString(): string {
17. return this._temp.toString();
18. }
19. }

21. let tempLower = new Temperature(30);
22. let tempUpper = new Temperature(40);
23. let range = new util.ScopeHelper(tempLower, tempUpper);
24. let result = range.getUpper();
25. console.info("result = " + result);
26. // 输出结果：result = 40
```

### getLower9+

PhonePC/2in1TabletTVWearable

getLower(): ScopeType

获取当前范围的下限。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ScopeType](js-apis-util.md#scopetype8) | 返回当前范围的下限值。 |

**示例：**

```
1. class Temperature implements util.ScopeComparable {
2. private readonly _temp: number;

4. constructor(value: number) {
5. this._temp = value;
6. }

8. compareTo(value: Temperature) {
9. return this._temp >= value.getTemp();
10. }

12. getTemp() {
13. return this._temp;
14. }

16. toString(): string {
17. return this._temp.toString();
18. }
19. }

21. let tempLower = new Temperature(30);
22. let tempUpper = new Temperature(40);
23. let range = new util.ScopeHelper(tempLower, tempUpper);
24. let result = range.getLower();
25. console.info("result = " + result);
26. // 输出结果：result = 30
```

### expand9+

PhonePC/2in1TabletTVWearable

expand(lowerObj: ScopeType,upperObj: ScopeType): ScopeHelper

创建并返回当前范围与给定下限和上限的并集。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lowerObj | [ScopeType](js-apis-util.md#scopetype8) | 是 | 给定范围的下限。 |
| upperObj | [ScopeType](js-apis-util.md#scopetype8) | 是 | 给定范围的上限。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ScopeHelper](js-apis-util.md#scopehelper9) | 返回当前范围和给定下限和上限的并集。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. class Temperature implements util.ScopeComparable {
2. private readonly _temp: number;

4. constructor(value: number) {
5. this._temp = value;
6. }

8. compareTo(value: Temperature) {
9. return this._temp >= value.getTemp();
10. }

12. getTemp() {
13. return this._temp;
14. }

16. toString(): string {
17. return this._temp.toString();
18. }
19. }

21. let tempLower = new Temperature(30);
22. let tempUpper = new Temperature(40);
23. let tempMiDF = new Temperature(35);
24. let tempMidS = new Temperature(39);
25. let range = new util.ScopeHelper(tempLower, tempUpper);
26. let result = range.expand(tempMiDF, tempMidS);
27. console.info("result = " + result);
28. // 输出结果：result = [30, 40]
```

### expand9+

PhonePC/2in1TabletTVWearable

expand(range: ScopeHelper): ScopeHelper

创建并返回当前范围和给定范围的并集。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| range | [ScopeHelper](js-apis-util.md#scopehelper9) | 是 | 传入一个给定范围。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ScopeHelper](js-apis-util.md#scopehelper9) | 返回包括当前范围和给定范围的并集。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. class Temperature implements util.ScopeComparable {
2. private readonly _temp: number;

4. constructor(value: number) {
5. this._temp = value;
6. }

8. compareTo(value: Temperature) {
9. return this._temp >= value.getTemp();
10. }

12. getTemp() {
13. return this._temp;
14. }

16. toString(): string {
17. return this._temp.toString();
18. }
19. }

21. let tempLower = new Temperature(30);
22. let tempUpper = new Temperature(40);
23. let tempMiDF = new Temperature(35);
24. let tempMidS = new Temperature(39);
25. let range = new util.ScopeHelper(tempLower, tempUpper);
26. let rangeFir = new util.ScopeHelper(tempMiDF, tempMidS);
27. let result = range.expand(rangeFir);
28. console.info("result = " + result);
29. // 输出结果：result = [30, 40]
```

### expand9+

PhonePC/2in1TabletTVWearable

expand(value: ScopeType): ScopeHelper

创建并返回当前范围和给定值的并集。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ScopeType](js-apis-util.md#scopetype8) | 是 | 传入一个给定值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ScopeHelper](js-apis-util.md#scopehelper9) | 返回包括当前范围和给定值的并集。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. class Temperature implements util.ScopeComparable {
2. private readonly _temp: number;

4. constructor(value: number) {
5. this._temp = value;
6. }

8. compareTo(value: Temperature) {
9. return this._temp >= value.getTemp();
10. }

12. getTemp() {
13. return this._temp;
14. }

16. toString(): string {
17. return this._temp.toString();
18. }
19. }

21. let tempLower = new Temperature(30);
22. let tempUpper = new Temperature(40);
23. let tempMiDF = new Temperature(35);
24. let range = new util.ScopeHelper(tempLower, tempUpper);
25. let result = range.expand(tempMiDF);
26. console.info("result = " + result);
27. // 输出结果：result = [30, 40]
```

### contains9+

PhonePC/2in1TabletTVWearable

contains(value: ScopeType): boolean

检查给定value是否在当前范围内。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ScopeType](js-apis-util.md#scopetype8) | 是 | 传入一个给定值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果给定值包含在当前范围内返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. class Temperature implements util.ScopeComparable {
2. private readonly _temp: number;

4. constructor(value: number) {
5. this._temp = value;
6. }

8. compareTo(value: Temperature) {
9. return this._temp >= value.getTemp();
10. }

12. getTemp() {
13. return this._temp;
14. }

16. toString(): string {
17. return this._temp.toString();
18. }
19. }

21. let tempLower = new Temperature(30);
22. let tempUpper = new Temperature(40);
23. let tempMiDF = new Temperature(35);
24. let range = new util.ScopeHelper(tempLower, tempUpper);
25. let result = range.contains(tempMiDF);
26. console.info("result = " + result);
27. // 输出结果：result = true
```

### contains9+

PhonePC/2in1TabletTVWearable

contains(range: ScopeHelper): boolean

检查给定range是否在当前范围内。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| range | [ScopeHelper](js-apis-util.md#scopehelper9) | 是 | 传入一个给定范围。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果给定范围在当前范围内则返回true，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. class Temperature implements util.ScopeComparable {
2. private readonly _temp: number;

4. constructor(value: number) {
5. this._temp = value;
6. }

8. compareTo(value: Temperature) {
9. return this._temp >= value.getTemp();
10. }

12. getTemp() {
13. return this._temp;
14. }

16. toString(): string {
17. return this._temp.toString();
18. }
19. }

21. let tempLower = new Temperature(30);
22. let tempUpper = new Temperature(40);
23. let range = new util.ScopeHelper(tempLower, tempUpper);
24. let tempLess = new Temperature(20);
25. let tempMore = new Temperature(45);
26. let rangeSec = new util.ScopeHelper(tempLess, tempMore);
27. let result = range.contains(rangeSec);
28. console.info("result = " + result);
29. // 输出结果：result = false
```

### clamp9+

PhonePC/2in1TabletTVWearable

clamp(value: ScopeType): ScopeType

将值限定到当前范围内。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ScopeType](js-apis-util.md#scopetype8) | 是 | 传入的给定值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ScopeType](js-apis-util.md#scopetype8) | 如果传入的value小于下限，返回lowerObj；如果大于上限值，返回upperObj；如果在当前范围内，返回value。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. class Temperature implements util.ScopeComparable {
2. private readonly _temp: number;

4. constructor(value: number) {
5. this._temp = value;
6. }

8. compareTo(value: Temperature) {
9. return this._temp >= value.getTemp();
10. }

12. getTemp() {
13. return this._temp;
14. }

16. toString(): string {
17. return this._temp.toString();
18. }
19. }

21. let tempLower = new Temperature(30);
22. let tempUpper = new Temperature(40);
23. let tempMiDF = new Temperature(35);
24. let range = new util.ScopeHelper(tempLower, tempUpper);
25. let result = range.clamp(tempMiDF);
26. console.info("result = " + result);
27. // 输出结果：result = 35
```

## Base64Helper9+

PhonePC/2in1TabletTVWearable

Base64Helper类提供Base64编解码和Base64URL编解码功能。Base64编码表包含A-Z、a-z、0-9这62个字符，以及"+"和"/"这两个特殊字符。在编码时，将原始数据按3个字节一组进行划分，得到若干个6位的数字，然后使用Base64编码表中对应的字符来表示这些数字。如果最后剩余1或2个字节，则需要使用"="字符进行补齐。Base64URL编码表包含A-Z、a-z、0-9以及"-"和"\_"64个字符，Base64URL编码结果不含"="。

### constructor9+

PhonePC/2in1TabletTVWearable

constructor()

Base64Helper的构造函数。

**系统能力：** SystemCapability.Utils.Lang

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**示例：**

```
1. let base64 = new util.Base64Helper();
```

### encodeSync9+

PhonePC/2in1TabletTVWearable

encodeSync(src: Uint8Array, options?: Type): Uint8Array

通过输入参数编码后输出Uint8Array对象。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | Uint8Array | 是 | 待编码的Uint8Array对象。 |
| options12+ | [Type](js-apis-util.md#type10) | 否 | 从API version 12开始支持该参数，表示对应的编码格式。  此参数可选，可选值为：util.Type.BASIC和util.Type.BASIC\_URL\_SAFE，默认值为：util.Type.BASIC。  util.Type.BASIC表示Base64编码。  util.Type.BASIC\_URL\_SAFE表示Base64URL编码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 返回编码后的Uint8Array对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. let base64Helper = new util.Base64Helper();
2. let array = new Uint8Array([115,49,51]);
3. let result = base64Helper.encodeSync(array);
4. console.info("result = " + result);
5. // 输出结果：result = 99,122,69,122
```

### encodeToStringSync9+

PhonePC/2in1TabletTVWearable

encodeToStringSync(src: Uint8Array, options?: Type): string

将输入的Uint8Array字节数组进行Base64编码，返回一个字符串结果。该方法支持多种编码格式，包括标准Base64编码、MIME格式的Base64编码（带有换行符）、URL安全格式的Base64编码等。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | Uint8Array | 是 | 待编码Uint8Array对象。 |
| options10+ | [Type](js-apis-util.md#type10) | 否 | 从API version 10开始支持该参数，表示对应的编码格式。  此参数可选，可选值为：util.Type.BASIC，util.Type.MIME，util.Type.BASIC\_URL\_SAFE 和util.Type.MIME\_URL\_SAFE，默认值为：util.Type.BASIC。  - 当参数取值为util.Type.BASIC，表示Base64编码，返回值没有回车符、换行符。  - 当参数取值为util.Type.MIME，表示使用Base64编码。如果返回值超过76个字符，则会在每76个字符处进行换行，并以'\r\n'结束每行。如果返回值少于76个字符，则会抛出异常。  - 当参数取值为util.Type.BASIC\_URL\_SAFE，表示Base64URL编码，返回值没有回车符、换行符。  - 当参数取值为util.Type.MIME\_URL\_SAFE，表示Base64URL编码，返回值每一行不超过76个字符，而且每行以'\r\n'符结束。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回编码后的字符串。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. // MIME编码
2. let base64Helper = new util.Base64Helper();
3. let array =
4. new Uint8Array([77, 97, 110, 105, 115, 100, 105, 115, 116, 105, 110, 103, 117, 105, 115, 104, 101, 100, 110, 111, 116,
5. 111, 110, 108, 121, 98, 121, 104, 105, 115, 114, 101, 97, 115, 111, 110, 98, 117, 116, 98, 121, 116, 104, 105, 115,
6. 115, 105, 110, 103, 117, 108, 97, 114, 112, 97, 115, 115, 105, 111, 110, 102, 114, 111, 109, 111, 116, 104, 101,
7. 114, 97, 110, 105, 109, 97, 108, 115, 119, 104, 105, 99, 104, 105, 115, 97, 108, 117, 115, 116, 111, 102, 116, 104,
8. 101, 109, 105, 110, 100, 101, 120, 99, 101, 101, 100, 115, 116, 104, 101, 115, 104, 111, 114, 116, 118, 101, 104,
9. 101, 109, 101, 110, 99, 101, 111, 102, 97, 110, 121, 99, 97, 114, 110, 97, 108, 112, 108, 101, 97, 115, 117, 114,
10. 101]);
11. let result = base64Helper.encodeToStringSync(array, util.Type.MIME);
12. console.info("result = " + result);
13. /*
14. 输出结果：result = TWFuaXNkaXN0aW5ndWlzaGVkbm90b25seWJ5aGlzcmVhc29uYnV0Ynl0aGlzc2luZ3VsYXJwYXNz
15. aW9uZnJvbW90aGVyYW5pbWFsc3doaWNoaXNhbHVzdG9mdGhlbWluZGV4Y2VlZHN0aGVzaG9ydHZl
16. aGVtZW5jZW9mYW55Y2FybmFscGxlYXN1cmU=
17. */

19. // BASIC编码
20. let base64Helper = new util.Base64Helper();
21. let array =
22. new Uint8Array([77, 97, 110, 105, 115, 100, 105, 115, 116, 105, 110, 103, 117, 105, 115, 104, 101, 100, 110, 111, 116,
23. 111, 110, 108, 121, 98, 121, 104, 105, 115, 114, 101, 97, 115, 111, 110, 98, 117, 116, 98, 121, 116, 104, 105, 115,
24. 115, 105, 110, 103, 117, 108, 97, 114, 112, 97, 115, 115, 105, 111, 110, 102, 114, 111, 109, 111, 116, 104, 101,
25. 114, 97, 110, 105, 109, 97, 108, 115, 119, 104, 105, 99, 104, 105, 115, 97, 108, 117, 115, 116, 111, 102, 116, 104,
26. 101, 109, 105, 110, 100, 101, 120, 99, 101, 101, 100, 115, 116, 104, 101, 115, 104, 111, 114, 116, 118, 101, 104,
27. 101, 109, 101, 110, 99, 101, 111, 102, 97, 110, 121, 99, 97, 114, 110, 97, 108, 112, 108, 101, 97, 115, 117, 114,
28. 101]);
29. let result = base64Helper.encodeToStringSync(array, util.Type.BASIC);
30. console.info("result = " + result);
31. /*
32. 输出结果：result = TWFuaXNkaXN0aW5ndWlzaGVkbm90b25seWJ5aGlzcmVhc29uYnV0Ynl0aGlzc2luZ3VsYXJwYXNzaW9uZnJvbW90aGVyYW5pbWFsc3doaWNoaXNhbHVzdG9mdGhlbWluZGV4Y2VlZHN0aGVzaG9ydHZlaGVtZW5jZW9mYW55Y2FybmFscGxlYXN1cmU=
33. */

35. // MIME_URL_SAFE编码
36. let base64Helper = new util.Base64Helper();
37. let array =
38. new Uint8Array([77, 97, 110, 105, 115, 100, 105, 115, 116, 105, 110, 103, 117, 105, 115, 104, 101, 100, 110, 111, 116,
39. 111, 110, 108, 121, 98, 121, 104, 105, 115, 114, 101, 97, 115, 111, 110, 98, 117, 116, 98, 121, 116, 104, 105, 115,
40. 115, 105, 110, 103, 117, 108, 97, 114, 112, 97, 115, 115, 105, 111, 110, 102, 114, 111, 109, 111, 116, 104, 101,
41. 114, 97, 110, 105, 109, 97, 108, 115, 119, 104, 105, 99, 104, 105, 115, 97, 108, 117, 115, 116, 111, 102, 116, 104,
42. 101, 109, 105, 110, 100, 101, 120, 99, 101, 101, 100, 115, 116, 104, 101, 115, 104, 111, 114, 116, 118, 101, 104,
43. 101, 109, 101, 110, 99, 101, 111, 102, 97, 110, 121, 99, 97, 114, 110, 97, 108, 112, 108, 101, 97, 115, 117, 114,
44. 101]);
45. let result = base64Helper.encodeToStringSync(array, util.Type.BASIC_URL_SAFE);
46. console.info("result = " + result);
47. /*
48. 输出结果：result = TWFuaXNkaXN0aW5ndWlzaGVkbm90b25seWJ5aGlzcmVhc29uYnV0Ynl0aGlzc2luZ3VsYXJwYXNzaW9uZnJvbW90aGVyYW5pbWFsc3doaWNoaXNhbHVzdG9mdGhlbWluZGV4Y2VlZHN0aGVzaG9ydHZlaGVtZW5jZW9mYW55Y2FybmFscGxlYXN1cmU
49. */
50. // MIME_URL_SAFE编码
51. let base64Helper = new util.Base64Helper();
52. let array =
53. new Uint8Array([77, 97, 110, 105, 115, 100, 105, 115, 116, 105, 110, 103, 117, 105, 115, 104, 101, 100, 110, 111, 116,
54. 111, 110, 108, 121, 98, 121, 104, 105, 115, 114, 101, 97, 115, 111, 110, 98, 117, 116, 98, 121, 116, 104, 105, 115,
55. 115, 105, 110, 103, 117, 108, 97, 114, 112, 97, 115, 115, 105, 111, 110, 102, 114, 111, 109, 111, 116, 104, 101,
56. 114, 97, 110, 105, 109, 97, 108, 115, 119, 104, 105, 99, 104, 105, 115, 97, 108, 117, 115, 116, 111, 102, 116, 104,
57. 101, 109, 105, 110, 100, 101, 120, 99, 101, 101, 100, 115, 116, 104, 101, 115, 104, 111, 114, 116, 118, 101, 104,
58. 101, 109, 101, 110, 99, 101, 111, 102, 97, 110, 121, 99, 97, 114, 110, 97, 108, 112, 108, 101, 97, 115, 117, 114,
59. 101]);
60. let result = base64Helper.encodeToStringSync(array, util.Type.MIME_URL_SAFE);
61. console.info("result = " + result);
62. /*
63. 输出结果：result = TWFuaXNkaXN0aW5ndWlzaGVkbm90b25seWJ5aGlzcmVhc29uYnV0Ynl0aGlzc2luZ3VsYXJwYXNz
64. aW9uZnJvbW90aGVyYW5pbWFsc3doaWNoaXNhbHVzdG9mdGhlbWluZGV4Y2VlZHN0aGVzaG9ydHZl
65. aGVtZW5jZW9mYW55Y2FybmFscGxlYXN1cmU
66. */
```

### decodeSync9+

PhonePC/2in1TabletTVWearable

decodeSync(src: Uint8Array | string, options?: Type): Uint8Array

将输入参数解码后输出对应Uint8Array对象。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | Uint8Array | string | 是 | 待解码的Uint8Array对象或者字符串。 |
| options10+ | [Type](js-apis-util.md#type10) | 否 | 从API version 10开始支持该参数，表示对应的解码格式。  此参数可选，可选值为：util.Type.BASIC，util.Type.MIME，util.Type.BASIC\_URL\_SAFE和util.Type.MIME\_URL\_SAFE，默认值为：util.Type.BASIC。  - 当参数取值为util.Type.BASIC，表示Base64解码。  - 当参数取值为util.Type.MIME，表示Base64解码，src入参包含回车符、换行符。  - 当参数取值为util.Type.BASIC\_URL\_SAFE，表示Base64URL解码。  - 当参数取值为util.Type.MIME\_URL\_SAFE，表示Base64URL解码，src入参包含回车符、换行符。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 返回解码后新分配的Uint8Array对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. let base64Helper = new util.Base64Helper();
2. let buff = 'TWFuaXNkaXN0aW5ndWlzaGVkbm90b25seWJ5aGlzcmVhc29uYnV0Ynl0aGlzc2luZ3VsYXJwYXNz\r\naW9uZnJvbW90aGVyYW5pbWFsc3doaWNoaXNhbHVzdG9mdGhlbWluZGV4Y2VlZHN0aGVzaG9ydHZl\r\naGVtZW5jZW9mYW55Y2FybmFscGxlYXN1cmU=\r\n';
3. let result = base64Helper.decodeSync(buff, util.Type.MIME);
4. console.info("result = " + result);
5. /*
6. 输出结果：result = 77,97,110,105,115,100,105,115,116,105,110,103,117,105,115,104,101,100,110,111,116,111,110,108,121,98,121,104,105,115,114,101,97,115,111,110,98,117,116,98,121,116,104,105,115,115,105,110,103,117,108,97,114,112,97,115,115,105,111,110,102,114,111,109,111,116,104,101,114,97,110,105,109,97,108,115,119,104,105,99,104,105,115,97,108,117,115,116,111,102,116,104,101,109,105,110,100,101,120,99,101,101,100,115,116,104,101,115,104,111,114,116,118,101,104,101,109,101,110,99,101,111,102,97,110,121,99,97,114,110,97,108,112,108,101,97,115,117,114,101
7. */
```

### encode9+

PhonePC/2in1TabletTVWearable

encode(src: Uint8Array, options?: Type): Promise<Uint8Array>

将输入参数异步编码后输出对应Uint8Array对象。使用Promise异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | Uint8Array | 是 | 待编码Uint8Array对象。 |
| options12+ | [Type](js-apis-util.md#type10) | 否 | 从API version 12开始支持该参数，表示对应的编码格式。  此参数可选，可选值为：util.Type.BASIC和util.Type.BASIC\_URL\_SAFE，默认值为：util.Type.BASIC。  util.Type.BASIC表示Base64编码。  util.Type.BASIC\_URL\_SAFE表示Base64URL编码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Uint8Array> | Promise对象，返回异步编码后新分配的Uint8Array对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. let base64Helper = new util.Base64Helper();
2. let array = new Uint8Array([115,49,51]);
3. base64Helper.encode(array).then((val) => {
4. console.info(val.toString());
5. // 输出结果：99,122,69,122
6. })
```

### encodeToString9+

PhonePC/2in1TabletTVWearable

encodeToString(src: Uint8Array, options?: Type): Promise<string>

将输入参数异步编码后输出对应文本。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | Uint8Array | 是 | 异步编码输入Uint8Array对象。 |
| options10+ | [Type](js-apis-util.md#type10) | 否 | 从API version 10开始支持该参数，表示对应的编码格式。  此参数可选，可选值为：util.Type.BASIC，util.Type.MIME，util.Type.BASIC\_URL\_SAFE和util.Type.MIME\_URL\_SAFE，默认值为：util.Type.BASIC。  - 当参数取值为util.Type.BASIC，表示Base64编码，返回值没有回车符、换行符。  - 当参数取值为util.Type.MIME，表示Base64编码，返回值每一行不超过76个字符，而且每行以'\r\n'符结束。  - 当参数取值为util.Type.BASIC\_URL\_SAFE，表示Base64URL编码，返回值没有回车符、换行符。  - 当参数取值为util.Type.MIME\_URL\_SAFE，表示Base64URL编码，返回值每一行不超过76个字符，而且每行以'\r\n'符结束。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | 返回异步编码后的字符串。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. let base64Helper = new util.Base64Helper();
2. let array = new Uint8Array([77,97,110,105,115,100,105,115,116,105,110,103,117,105,115,104,101,100,110,111,116,111,110,108,121,98,121,104,105,115,114,101,97,115,111,110,98,117,116,98,121,116,104,105,115,115,105,110,103,117,108,97,114,112,97,115,115,105,111,110,102,114,111,109,111,116,104,101,114,97,110,105,109,97,108,115,119,104,105,99,104,105,115,97,108,117,115,116,111,102,116,104,101,109,105,110,100,101,120,99,101,101,100,115,116,104,101,115,104,111,114,116,118,101,104,101,109,101,110,99,101,111,102,97,110,121,99,97,114,110,97,108,112,108,101,97,115,117,114,101]);
3. base64Helper.encodeToString(array, util.Type.MIME).then((val) => {
4. console.info(val);
5. /*
6. 输出结果：TWFuaXNkaXN0aW5ndWlzaGVkbm90b25seWJ5aGlzcmVhc29uYnV0Ynl0aGlzc2luZ3VsYXJwYXNz
7. aW9uZnJvbW90aGVyYW5pbWFsc3doaWNoaXNhbHVzdG9mdGhlbWluZGV4Y2VlZHN0aGVzaG9ydHZl
8. aGVtZW5jZW9mYW55Y2FybmFscGxlYXN1cmU=
9. */

11. })
```

### decode9+

PhonePC/2in1TabletTVWearable

decode(src: Uint8Array | string, options?: Type): Promise<Uint8Array>

将输入参数异步解码后输出对应Uint8Array对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | Uint8Array | string | 是 | 异步解码输入Uint8Array对象或者字符串。 |
| options10+ | [Type](js-apis-util.md#type10) | 否 | 从API version 10开始支持该参数，表示对应的解码格式。  此参数可选，可选值为：util.Type.BASIC，util.Type.MIME，util.Type.BASIC\_URL\_SAFE和util.Type.MIME\_URL\_SAFE，默认值为：util.Type.BASIC。  - 当参数取值为util.Type.BASIC时，表示Base64解码。  - 当参数取值为util.Type.MIME时，表示Base64解码，src入参包含回车符、换行符。  - 当参数取值为util.Type.BASIC\_URL\_SAFE，表示Base64URL解码。  - 当参数取值为util.Type.MIME\_URL\_SAFE，表示Base64URL解码，src入参包含回车符、换行符。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Uint8Array> | 返回异步解码后新分配的Uint8Array对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. let base64Helper = new util.Base64Helper();
2. let array = 'TWFuaXNkaXN0aW5ndWlzaGVkbm90b25seWJ5aGlzcmVhc29uYnV0Ynl0aGlzc2luZ3VsYXJwYXNz\r\naW9uZnJvbW90aGVyYW5pbWFsc3doaWNoaXNhbHVzdG9mdGhlbWluZGV4Y2VlZHN0aGVzaG9ydHZl\r\naGVtZW5jZW9mYW55Y2FybmFscGxlYXN1cmU=\r\n';
3. base64Helper.decode(array, util.Type.MIME).then((val) => {
4. console.info(val.toString());
5. /*
6. 输出结果：77,97,110,105,115,100,105,115,116,105,110,103,117,105,115,104,101,100,110,111,116,111,110,108,121,98,121,104,105,115,114,101,97,115,111,110,98,117,116,98,121,116,104,105,115,115,105,110,103,117,108,97,114,112,97,115,115,105,111,110,102,114,111,109,111,116,104,101,114,97,110,105,109,97,108,115,119,104,105,99,104,105,115,97,108,117,115,116,111,102,116,104,101,109,105,110,100,101,120,99,101,101,100,115,116,104,101,115,104,111,114,116,118,101,104,101,109,101,110,99,101,111,102,97,110,121,99,97,114,110,97,108,112,108,101,97,115,117,114,101
7. */
8. })
```

## StringDecoder12+

PhonePC/2in1TabletTVWearable

提供将二进制流解码为字符串的能力。支持的编码类型包括：utf-8、iso-8859-2、koi8-r、macintosh、windows-1250、windows-1251、gbk、gb18030、big5、utf-16be、utf-16le等。

### constructor12+

PhonePC/2in1TabletTVWearable

constructor(encoding?: string)

StringDecoder的构造函数。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| encoding | string | 否 | 输入数据的编码类型。默认值：'utf-8'。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. let decoder = new util.StringDecoder();
```

### write12+

PhonePC/2in1TabletTVWearable

write(chunk: string | Uint8Array): string

返回一个解码后的字符串，确保Uint8Array末尾的任何不完整的多字节字符从返回的字符串中被过滤，并保存在一个内部的buffer中用于下次调用。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| chunk | string | Uint8Array | 是 | 需要解码的字符串。会根据输入的编码类型进行解码，参数为Uint8Array时正常解码，参数为string时会将参数直接返回。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回解码后的字符串。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. let decoder = new util.StringDecoder('utf-8');
2. let input =  new Uint8Array([0xE4, 0xBD, 0xA0, 0xE5, 0xA5, 0xBD]);
3. const decoded = decoder.write(input);
4. console.info("decoded:", decoded);
5. // 输出结果：decoded: 你好
```

### end12+

PhonePC/2in1TabletTVWearable

end(chunk?: string | Uint8Array): string

结束解码过程，以字符串形式返回存储在内部缓冲区中的所有剩余输入。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| chunk | string | Uint8Array | 否 | 需要解码的字符串。默认为undefined。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回解码后的字符串。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. let decoder = new util.StringDecoder('utf-8');
2. let input = new Uint8Array([0xE4, 0xBD, 0xA0, 0xE5, 0xA5, 0xBD]);
3. const writeString = decoder.write(input.slice(0, 5));
4. const endString = decoder.end(input.slice(5));
5. console.info("writeString:", writeString);
6. // 输出结果：writeString: 你
7. console.info("endString:", endString);
8. // 输出结果：endString: 好
```

## Type10+

PhonePC/2in1TabletTVWearable

Base64编码格式枚举。

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BASIC | 0 | 表示BASIC编码格式。**元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| MIME | 1 | 表示MIME编码格式。**元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| BASIC\_URL\_SAFE12+ | 2 | 表示BASIC\_URL\_SAFE编码格式。  从API version 12开始支持此枚举。**元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| MIME\_URL\_SAFE12+ | 3 | 表示MIME\_URL\_SAFE编码格式。  从API version 12开始支持此枚举。**元服务API**：从API version 12开始，该接口支持在元服务中使用。 |

## types8+

PhonePC/2in1TabletTVWearable

types为不同类型的内置对象提供类型检查，可以避免由于类型错误导致的异常。该模块包含了多个工具函数，用于判断JS对象是否属于各种类型，例如：ArrayBuffer、Map、Set等。

### constructor8+

PhonePC/2in1TabletTVWearable

constructor()

Types的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**示例：**

```
1. let type = new util.types();
```

### isAnyArrayBuffer8+

PhonePC/2in1TabletTVWearable

isAnyArrayBuffer(value: Object): boolean

检查value是否为ArrayBuffer或SharedArrayBuffer类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Object | 是 | 待检测对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果是ArrayBuffer或SharedArrayBuffer类型则返回true，否则返回false。 |

**示例：**

```
1. let type = new util.types();
2. let result = type.isAnyArrayBuffer(new ArrayBuffer(0));
3. console.info("result = " + result);
4. // 输出结果：result = true
```

### isArrayBufferView8+

PhonePC/2in1TabletTVWearable

isArrayBufferView(value: Object): boolean

检查value是否为ArrayBufferView类型。

ArrayBufferView类型包括：Int8Array、Int16Array、Int32Array、Uint8Array、Uint8ClampedArray、Uint32Array、Float32Array、Float64Array、DataView。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Object | 是 | 待检测对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果是ArrayBufferView类型则返回true，否则返回false。 |

**示例：**

```
1. let type = new util.types();
2. let result = type.isArrayBufferView(new Int8Array([]));
3. console.info("result = " + result);
4. // 输出结果：result = true
```

### isArgumentsObject8+

PhonePC/2in1TabletTVWearable

isArgumentsObject(value: Object): boolean

检查value是否为arguments对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Object | 是 | 待检测对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果是arguments对象则返回true，否则返回false。 |

**示例：**

```
1. let type = new util.types();
2. function foo() {
3. let result = type.isArgumentsObject(arguments);
4. console.info("result = " + result);
5. }
6. let f = foo();
7. // 输出结果：result = true
```

### isArrayBuffer8+

PhonePC/2in1TabletTVWearable

isArrayBuffer(value: Object): boolean

检查value是否为ArrayBuffer类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Object | 是 | 待检测对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果是ArrayBuffer类型则返回true，否则返回false。 |

**示例：**

```
1. let type = new util.types();
2. let result = type.isArrayBuffer(new ArrayBuffer(0));
3. console.info("result = " + result);
4. // 输出结果：result = true
```

### isAsyncFunction8+

PhonePC/2in1TabletTVWearable

isAsyncFunction(value: Object): boolean

检查value是否为异步函数类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Object | 是 | 待检测对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果是异步函数则返回true，否则返回false。 |

**示例：**

```
1. let type = new util.types();
2. let result = type.isAsyncFunction(async () => {});
3. console.info("result = " + result);
4. // 输出结果：result = true
```

### isBooleanObject(deprecated)

PhonePC/2in1TabletTVWearable

isBooleanObject(value: Object): boolean

检查value是否为Boolean对象。

说明

从API version 8开始支持，从API version 14开始废弃，没有替代接口。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Object | 是 | 待检测对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果是Boolean对象则返回true，否则返回false。 |

**示例：**

```
1. let type = new util.types();
2. let result = type.isBooleanObject(new Boolean(true));
3. console.info("result = " + result);
4. // 输出结果：result = true
```

### isBoxedPrimitive(deprecated)

PhonePC/2in1TabletTVWearable

isBoxedPrimitive(value: Object): boolean

检查value是否为Boolean、Number、String或Symbol对象类型。

说明

从API version 8开始支持，从API version 14开始废弃，没有替代接口。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Object | 是 | 待检测对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果是Boolean、Number、String或Symbol对象则返回true，否则返回false。 |

**示例：**

```
1. let type = new util.types();
2. let result = type.isBoxedPrimitive(new Boolean(false));
3. console.info("result = " + result);
4. // 输出结果：result = true
```

### isDataView8+

PhonePC/2in1TabletTVWearable

isDataView(value: Object): boolean

检查value是否为DataView类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Object | 是 | 待检测对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果是DataView类型则返回true，否则返回false。 |

**示例：**

```
1. let type = new util.types();
2. const ab = new ArrayBuffer(20);
3. let result = type.isDataView(new DataView(ab));
4. console.info("result = " + result);
5. // 输出结果：result = true
```

### isDate8+

PhonePC/2in1TabletTVWearable

isDate(value: Object): boolean

检查value是否为Date类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Object | 是 | 待检测对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果是Date类型则返回true，否则返回false。 |

**示例：**

```
1. let type = new util.types();
2. let result = type.isDate(new Date());
3. console.info("result = " + result);
4. // 输出结果：result = true
```

### isExternal8+

PhonePC/2in1TabletTVWearable

isExternal(value: Object): boolean

检查value是否为native External类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Object | 是 | 待检测对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果是native External类型则返回true，否则返回false。 |

**示例：**

```
1. // /entry/src/main/cpp/napi_init.cpp
2. #include "napi/native_api.h"
3. #include <js_native_api.h>
4. #include <stdlib.h>

6. napi_value result;
7. static napi_value Testexternal(napi_env env, napi_callback_info info) {
8. int* raw = (int*) malloc(1024);
9. napi_status status = napi_create_external(env, (void*) raw, NULL, NULL, &result);
10. if (status != napi_ok) {
11. napi_throw_error(env, NULL, "create external failed");
12. return NULL;
13. }
14. return result;
15. }

17. EXTERN_C_START
18. static napi_value Init(napi_env env, napi_value exports)
19. {
20. napi_property_descriptor desc[] = {
21. {"testexternal", nullptr, Testexternal, nullptr, nullptr, nullptr, napi_default, nullptr},
22. };
23. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
24. return exports;
25. }
26. EXTERN_C_END
27. // 此处已省略模块注册的代码, 你可能需要自行注册Testexternal方法
28. ...
```

```
1. import testNapi from 'libentry.so';

3. let type = new util.types();
4. const data = testNapi.testexternal();
5. let result = type.isExternal(data);

7. let result01 = type.isExternal(true);
8. console.info("result = " + result);
9. console.info("result01 = " + result01);
10. // 输出结果：result = true
11. // 输出结果：result01 = false
```

### isFloat32Array8+

PhonePC/2in1TabletTVWearable

isFloat32Array(value: Object): boolean

检查value是否为Float32Array数组类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Object | 是 | 待检测对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果是Float32Array数组类型则返回true，否则返回false。 |

**示例：**

```
1. let type = new util.types();
2. let result = type.isFloat32Array(new Float32Array());
3. console.info("result = " + result);
4. // 输出结果：result = true
```

### isFloat64Array8+

PhonePC/2in1TabletTVWearable

isFloat64Array(value: Object): boolean

检查value是否为Float64Array数组类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Object | 是 | 待检测对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果是Float64Array数组类型则返回true，否则返回false。 |

**示例：**

```
1. let type = new util.types();
2. let result = type.isFloat64Array(new Float64Array());
3. console.info("result = " + result);
4. // 输出结果：result = true
```

### isGeneratorFunction8+

PhonePC/2in1TabletTVWearable

isGeneratorFunction(value: Object): boolean

检查value是否是为generator函数类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Object | 是 | 待检测对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果是generator函数类型则返回true，否则返回false。 |

**示例：**

```
1. // /entry/src/main/ets/pages/test.ts
2. export function* foo() {}
```

```
1. import { foo } from './test'

3. let type = new util.types();
4. let result = type.isGeneratorFunction(foo);
5. console.info("result = " + result);
6. // 输出结果：result = true
```

### isGeneratorObject8+

PhonePC/2in1TabletTVWearable

isGeneratorObject(value: Object): boolean

检查value是否为generator对象类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Object | 是 | 待检测对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果是generator对象则返回true，否则返回false。 |

**示例：**

```
1. // /entry/src/main/ets/pages/test.ts
2. function* foo() {}
3. export const generator = foo();
```

```
1. import { generator } from './test'

3. let type = new util.types();
4. let result = type.isGeneratorObject(generator);
5. console.info("result = " + result);
6. // 输出结果：result = true
```

### isInt8Array8+

PhonePC/2in1TabletTVWearable

isInt8Array(value: Object): boolean

检查value是否为Int8Array数组类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Object | 是 | 待检测对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果是Int8Array数组类型则返回true，否则返回false。 |

**示例：**

```
1. let type = new util.types();
2. let result = type.isInt8Array(new Int8Array([]));
3. console.info("result = " + result);
4. // 输出结果：result = true
```

### isInt16Array8+

PhonePC/2in1TabletTVWearable

isInt16Array(value: Object): boolean

检查value是否为Int16Array数组类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Object | 是 | 待检测对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果是Int16Array数组类型则返回true，否则返回false。 |

**示例：**

```
1. let type = new util.types();
2. let result = type.isInt16Array(new Int16Array([]));
3. console.info("result = " + result);
4. // 输出结果：result = true
```

### isInt32Array8+

PhonePC/2in1TabletTVWearable

isInt32Array(value: Object): boolean

检查value是否为Int32Array数组类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Object | 是 | 待检测对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果是Int32Array数组类型则返回true，否则返回false。 |

**示例：**

```
1. let type = new util.types();
2. let result = type.isInt32Array(new Int32Array([]));
3. console.info("result = " + result);
4. // 输出结果：result = true
```

### isMap8+

PhonePC/2in1TabletTVWearable

isMap(value: Object): boolean

检查value是否为Map类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Object | 是 | 待检测对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果是Map类型返回则返回true，否则返回false。 |

**示例：**

```
1. let type = new util.types();
2. let result = type.isMap(new Map());
3. console.info("result = " + result);
4. // 输出结果：result = true
```

### isMapIterator8+

PhonePC/2in1TabletTVWearable

isMapIterator(value: Object): boolean

检查value是否为Map的Iterator类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Object | 是 | 待检测对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果是Map的Iterator类型则返回true，否则返回false。 |

**示例：**

```
1. let type = new util.types();
2. const map : Map<number,number> = new Map();
3. let result = type.isMapIterator(map.keys());
4. console.info("result = " + result);
5. // 输出结果：result = true
```

### isNativeError8+

PhonePC/2in1TabletTVWearable

isNativeError(value: Object): boolean

检查value是否为Error类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Object | 是 | 待检测对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果是Error类型则返回true，否则返回false。 |

**示例：**

```
1. let type = new util.types();
2. let result = type.isNativeError(new TypeError());
3. console.info("result = " + result);
4. // 输出结果：result = true
```

### isNumberObject(deprecated)

PhonePC/2in1TabletTVWearable

isNumberObject(value: Object): boolean

检查value是否为Number对象类型。

说明

从API version 8开始支持，从API version 14开始废弃，没有替代接口。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Object | 是 | 待检测对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果是Number对象类型则返回true，否则返回false。 |

**示例：**

```
1. let type = new util.types();
2. let result = type.isNumberObject(new Number(0));
3. console.info("result = " + result);
4. // 输出结果：result = true
```

### isPromise8+

PhonePC/2in1TabletTVWearable

isPromise(value: Object): boolean

检查value是否为Promise类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Object | 是 | 待检测对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果是Promise类型则返回true，否则返回false。 |

**示例：**

```
1. let type = new util.types();
2. let result = type.isPromise(Promise.resolve(1));
3. console.info("result = " + result);
4. // 输出结果：result = true
```

### isProxy8+

PhonePC/2in1TabletTVWearable

isProxy(value: Object): boolean

检查value是否为Proxy类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Object | 是 | 待检测对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果是Proxy类型则返回true，否则返回false。 |

**示例：**

```
1. class Target{
2. }
3. let type = new util.types();
4. const target : Target = {};
5. const proxy = new Proxy(target, target);
6. let result = type.isProxy(proxy);
7. console.info("result = " + result);
8. // 输出结果：result = true
```

### isRegExp8+

PhonePC/2in1TabletTVWearable

isRegExp(value: Object): boolean

检查value是否为RegExp类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Object | 是 | 待检测对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果是RegExp类型则返回true，否则返回false。 |

**示例：**

```
1. let type = new util.types();
2. let result = type.isRegExp(new RegExp('abc'));
3. console.info("result = " + result);
4. // 输出结果：result = true
```

### isSet8+

PhonePC/2in1TabletTVWearable

isSet(value: Object): boolean

检查value是否为Set类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Object | 是 | 待检测对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果是Set类型则返回true，否则返回false。 |

**示例：**

```
1. let type = new util.types();
2. let set : Set<number> = new Set();
3. let result = type.isSet(set);
4. console.info("result = " + result);
5. // 输出结果：result = true
```

### isSetIterator8+

PhonePC/2in1TabletTVWearable

isSetIterator(value: Object): boolean

检查value是否为Set的Iterator类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Object | 是 | 待检测对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果是Set的Iterator类型则返回true，否则返回false。 |

**示例：**

```
1. let type = new util.types();
2. const set : Set<number> = new Set();
3. let result = type.isSetIterator(set.keys());
4. console.info("result = " + result);
5. // 输出结果：result = true
```

### isStringObject(deprecated)

PhonePC/2in1TabletTVWearable

isStringObject(value: Object): boolean

检查value是否为String对象类型。

说明

从API version 8开始支持，从API version 14开始废弃，没有替代接口。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Object | 是 | 待检测对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果是String对象类型则返回true，否则返回false。 |

**示例：**

```
1. let type = new util.types();
2. let result = type.isStringObject(new String('foo'));
3. console.info("result = " + result);
4. // 输出结果：result = true
```

### isSymbolObject(deprecated)

PhonePC/2in1TabletTVWearable

isSymbolObject(value: Object): boolean

检查value是否为Symbol对象类型。

说明

从API version 8开始支持，从API version 14开始废弃，没有替代接口。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Object | 是 | 待检测对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果是Symbol对象类型为则返回true，否则返回false。 |

**示例：**

```
1. // /entry/src/main/ets/pages/test.ts
2. export const symbols = Symbol('foo');
```

```
1. import { symbols } from './test'

3. let type = new util.types();
4. let result = type.isSymbolObject(Object(symbols));
5. console.info("result = " + result);
6. // 输出结果：result = true
```

### isTypedArray8+

PhonePC/2in1TabletTVWearable

isTypedArray(value: Object): boolean

检查value是否为TypedArray类型。

TypedArray类型，包括Int8Array、Int16Array、Int32Array、Uint8Array、Uint8ClampedArray、Uint16Array、Uint32Array、Float32Array、Float64Array、BigInt64Array、BigUint64Array。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Object | 是 | 待检测对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果是TypedArray包含的类型则返回true，否则返回false。 |

**示例：**

```
1. let type = new util.types();
2. let result = type.isTypedArray(new Float64Array([]));
3. console.info("result = " + result);
4. // 输出结果：result = true
```

### isUint8Array8+

PhonePC/2in1TabletTVWearable

isUint8Array(value: Object): boolean

检查value是否为Uint8Array数组类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Object | 是 | 待检测对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果是Uint8Array数组类型则返回true，否则返回false。 |

**示例：**

```
1. let type = new util.types();
2. let result = type.isUint8Array(new Uint8Array([]));
3. console.info("result = " + result);
4. // 输出结果：result = true
```

### isUint8ClampedArray8+

PhonePC/2in1TabletTVWearable

isUint8ClampedArray(value: Object): boolean

检查value是否为Uint8ClampedArray数组类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Object | 是 | 待检测对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果是Uint8ClampedArray数组类型则返回true，否则返回false。 |

**示例：**

```
1. let type = new util.types();
2. let result = type.isUint8ClampedArray(new Uint8ClampedArray([]));
3. console.info("result = " + result);
4. // 输出结果：result = true
```

### isUint16Array8+

PhonePC/2in1TabletTVWearable

isUint16Array(value: Object): boolean

检查value是否为Uint16Array数组类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Object | 是 | 待检测对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果是Uint16Array数组类型则返回true，否则返回false。 |

**示例：**

```
1. let type = new util.types();
2. let result = type.isUint16Array(new Uint16Array([]));
3. console.info("result = " + result);
4. // 输出结果：result = true
```

### isUint32Array8+

PhonePC/2in1TabletTVWearable

isUint32Array(value: Object): boolean

检查value是否为Uint32Array数组类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Object | 是 | 待检测对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果是Uint32Array数组类型则返回true，否则返回false。 |

**示例：**

```
1. let type = new util.types();
2. let result = type.isUint32Array(new Uint32Array([]));
3. console.info("result = " + result);
4. // 输出结果：result = true
```

### isWeakMap8+

PhonePC/2in1TabletTVWearable

isWeakMap(value: Object): boolean

检查value是否为WeakMap类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Object | 是 | 待检测对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果是WeakMap类型则返回true，否则返回false。 |

**示例：**

```
1. let type = new util.types();
2. let value : WeakMap<object, number> = new WeakMap();
3. let result = type.isWeakMap(value);
4. console.info("result = " + result);
5. // 输出结果：result = true
```

### isWeakSet8+

PhonePC/2in1TabletTVWearable

isWeakSet(value: Object): boolean

检查value是否为WeakSet类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Object | 是 | 待检测对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果是WeakSet类型则返回true，否则返回false。 |

**示例：**

```
1. let type = new util.types();
2. let result = type.isWeakSet(new WeakSet());
3. console.info("result = " + result);
4. // 输出结果：result = true
```

### isBigInt64Array8+

PhonePC/2in1TabletTVWearable

isBigInt64Array(value: Object): boolean

检查value是否为BigInt64Array类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Object | 是 | 待检测对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果是BigInt64Array类型则返回true，否则返回false。 |

**示例：**

```
1. let type = new util.types();
2. let result = type.isBigInt64Array(new BigInt64Array([]));
3. console.info("result = " + result);
4. // 输出结果：result = true
```

### isBigUint64Array8+

PhonePC/2in1TabletTVWearable

isBigUint64Array(value: Object): boolean

检查value是否为BigUint64Array类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Object | 是 | 待检测对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果是BigUint64Array类型则返回true，否则返回false。 |

**示例：**

```
1. let type = new util.types();
2. let result = type.isBigUint64Array(new BigUint64Array([]));
3. console.info("result = " + result);
4. // 输出结果：result = true
```

### isModuleNamespaceObject8+

PhonePC/2in1TabletTVWearable

isModuleNamespaceObject(value: Object): boolean

检查value是否为Module Namespace Object类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Object | 是 | 待检测对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果是Module Namespace Object类型则返回true，否则返回false。 |

**示例：**

```
1. // /entry/src/main/ets/pages/test.ts
2. export function func() {
3. console.info("hello world");
4. }
```

```
1. import * as nameSpace from './test';

3. let type = new util.types();
4. let result = type.isModuleNamespaceObject(nameSpace);
5. console.info("result = " + result);
6. // 输出结果：result = true
```

### isSharedArrayBuffer8+

PhonePC/2in1TabletTVWearable

isSharedArrayBuffer(value: Object): boolean

检查value是否为SharedArrayBuffer类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Object | 是 | 待检测对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果是SharedArrayBuffer类型则返回true，否则返回false。 |

**示例：**

```
1. let type = new util.types();
2. let result = type.isSharedArrayBuffer(new SharedArrayBuffer(0));
3. console.info("result = " + result);
4. // 输出结果：result = true
```

## AutoFinalizer<T>22+

PhonePC/2in1TabletTVWearable

AutoFinalizer是一个接口类，用于在ArkTS对象释放时提供回调。通过实现回调接口，开发者可自定义对象被回收时自动触发的资源清理逻辑。

说明

AutoFinalizer<T>需要和AutoFinalizerCleaner<T>一起使用，只实现该接口类没有任何功能。

### onFinalization22+

PhonePC/2in1TabletTVWearable

onFinalization(heldValue: T): void

开发者需要实现该接口，定义对象被回收时自动触发的资源清理回调。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| heldValue | T | 是 | 当监听的对象被回收时，该值会被传递给onFinalization回调方法。 |

## AutoFinalizerCleaner<T>22+

PhonePC/2in1TabletTVWearable

AutoFinalizerCleaner是用于关联对象生命周期与资源清理逻辑的工具类。主要的作用是将实现了AutoFinalizer<T>接口的对象与特定值绑定，当对象被回收时自动触发资源清理回调。

### register<T>22+

PhonePC/2in1TabletTVWearable

static register<T>(obj: AutoFinalizer<T>, heldValue: T): void

将AutoFinalizer接口的对象与输入值关联，当对象被回收时触发资源清理的回调。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| obj | [AutoFinalizer<T>](js-apis-util.md#autofinalizert22) | 是 | 实现了AutoFinalizer接口的对象，其onFinalization方法会在该对象被回收时调用。 |
| heldValue | T | 是 | 当监听的对象被回收时，该值会被传递给obj.onFinalization方法。 |

**示例：**

```
1. class DeviceManageViewModel implements util.AutoFinalizer<string> {
2. constructor(heldValue: string) {
3. util.AutoFinalizerCleaner.register(this, heldValue);
4. }

6. onFinalization(heldValue: string) {
7. console.info("onFinalization: ", heldValue);
8. // 等待触发垃圾回收，触发后会输出结果：onFinalization: test
9. }
10. }

12. const device = new DeviceManageViewModel("test");
```

## LruBuffer(deprecated)

PhonePC/2in1TabletTVWearable

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[LRUCache9+](js-apis-util.md#lrucache9)替代。

### 属性

PhonePC/2in1TabletTVWearable

**系统能力：** 以下各项对应的系统能力均为SystemCapability.Utils.Lang。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| length | number | 是 | 否 | 当前缓冲区中值的总数。 |

**示例：**

```
1. let pro : util.LruBuffer<number,number>= new util.LruBuffer();
2. pro.put(2,10);
3. pro.put(1,8);
4. let result = pro.length;
5. console.info("result = " + result);
6. // 输出结果：result = 2
```

### constructor(deprecated)

PhonePC/2in1TabletTVWearable

constructor(capacity?: number)

构造函数用于创建一个新的LruBuffer实例，默认容量为64。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[LRUCache.constructor9+](js-apis-util.md#constructor9-3)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| capacity | number | 否 | 指示要为缓冲区自定义的容量，默认值为64。 |

**示例：**

```
1. let pro : util.LruBuffer<number,number> = new util.LruBuffer();
```

### updateCapacity(deprecated)

PhonePC/2in1TabletTVWearable

updateCapacity(newCapacity: number): void

将缓冲区容量更新为指定容量，如果newCapacity小于或等于0，则抛出异常。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[LRUCache.updateCapacity9+](js-apis-util.md#updatecapacity9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| newCapacity | number | 是 | 指示要为缓冲区自定义的容量。 |

**示例：**

```
1. let pro : util.LruBuffer<number,number> = new util.LruBuffer();
2. pro.updateCapacity(100);
```

### toString(deprecated)

PhonePC/2in1TabletTVWearable

toString(): string

返回对象的字符串表示形式。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[LRUCache.toString9+](js-apis-util.md#tostring9)替代。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回对象的字符串表示形式。 |

**示例：**

```
1. let pro : util.LruBuffer<number,number> = new util.LruBuffer();
2. pro.put(2,10);
3. pro.get(2);
4. pro.remove(20);
5. let result = pro.toString();
6. console.info("result = " + result);
7. // 输出结果：result = Lrubuffer[ maxSize = 64, hits = 1, misses = 0, hitRate = 100% ]
```

### getCapacity(deprecated)

PhonePC/2in1TabletTVWearable

getCapacity(): number

获取当前缓冲区的容量。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[LRUCache.getCapacity9+](js-apis-util.md#getcapacity9)替代。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回当前缓冲区的容量。 |

**示例：**

```
1. let pro : util.LruBuffer<number,number> = new util.LruBuffer();
2. let result = pro.getCapacity();
3. console.info("result = " + result);
4. // 输出结果：result = 64
```

### clear(deprecated)

PhonePC/2in1TabletTVWearable

clear(): void

清除当前缓冲区中的键值对，后续调用afterRemoval()方法执行操作。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[LRUCache.clear9+](js-apis-util.md#clear9)替代。

**系统能力：** SystemCapability.Utils.Lang

**示例：**

```
1. let pro : util.LruBuffer<number,number> = new util.LruBuffer();
2. pro.put(2,10);
3. let result = pro.length;
4. pro.clear();
```

### getCreateCount(deprecated)

PhonePC/2in1TabletTVWearable

getCreateCount(): number

获取createDefault()返回值的次数。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[LRUCache.getCreateCount9+](js-apis-util.md#getcreatecount9)替代。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回createDefault()返回值的次数。 |

**示例：**

```
1. let pro : util.LruBuffer<number,number> = new util.LruBuffer();
2. pro.put(1,8);
3. let result = pro.getCreateCount();
4. console.info("result = " + result);
5. // 输出结果：result = 0
```

### getMissCount(deprecated)

PhonePC/2in1TabletTVWearable

getMissCount(): number

获取查询值不匹配的次数。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[LRUCache.getMissCount9+](js-apis-util.md#getmisscount9)替代。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回查询值不匹配的次数。 |

**示例：**

```
1. let pro : util.LruBuffer<number,number> = new util.LruBuffer();
2. pro.put(2,10);
3. pro.get(2);
4. let result = pro.getMissCount();
5. console.info("result = " + result);
6. // 输出结果：result = 0
```

### getRemovalCount(deprecated)

PhonePC/2in1TabletTVWearable

getRemovalCount(): number

获取从缓冲区中逐出值的次数。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[LRUCache.getRemovalCount9+](js-apis-util.md#getremovalcount9)替代。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回从缓冲区中驱逐的次数。 |

**示例：**

```
1. let pro : util.LruBuffer<number,number> = new util.LruBuffer();
2. pro.put(2,10);
3. pro.updateCapacity(2);
4. pro.put(50,22);
5. let result = pro.getRemovalCount();
6. console.info("result = " + result);
7. // 输出结果：result = 0
```

### getMatchCount(deprecated)

PhonePC/2in1TabletTVWearable

getMatchCount(): number

获取查询值匹配成功的次数。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[LRUCache.getMatchCount9+](js-apis-util.md#getmatchcount9)替代。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回查询值匹配成功的次数。 |

**示例：**

```
1. let pro : util.LruBuffer<number,number> = new util.LruBuffer();
2. pro.put(2,10);
3. pro.get(2);
4. let result = pro.getMatchCount();
5. console.info("result = " + result);
6. // 输出结果：result = 1
```

### getPutCount(deprecated)

PhonePC/2in1TabletTVWearable

getPutCount(): number

获取将值添加到缓冲区的次数。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[LRUCache.getPutCount9+](js-apis-util.md#getputcount9)替代。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回将值添加到缓冲区的次数。 |

**示例：**

```
1. let pro : util.LruBuffer<number,number> = new util.LruBuffer();
2. pro.put(2,10);
3. let result = pro.getPutCount();
4. console.info("result = " + result);
5. // 输出结果：result = 1
```

### isEmpty(deprecated)

PhonePC/2in1TabletTVWearable

isEmpty(): boolean

检查当前缓冲区是否为空。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[LRUCache.isEmpty9+](js-apis-util.md#isempty9)替代。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果当前缓冲区不包含任何值，则返回true。 |

**示例：**

```
1. let pro : util.LruBuffer<number,number> = new util.LruBuffer();
2. pro.put(2,10);
3. let result = pro.isEmpty();
4. console.info("result = " + result);
5. // 输出结果：result = false
```

### get(deprecated)

PhonePC/2in1TabletTVWearable

get(key: K): V | undefined

表示要查询的键。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[LRUCache.get9+](js-apis-util.md#get9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 | 要查询的键。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| V | undefined | 如果指定的键存在于缓冲区中，则返回与键关联的值；否则返回undefined。 |

**示例：**

```
1. let pro : util.LruBuffer<number,number> = new util.LruBuffer();
2. pro.put(2,10);
3. let result  = pro.get(2);
4. console.info("result = " + result);
5. // 输出结果：result = 10
```

### put(deprecated)

PhonePC/2in1TabletTVWearable

put(key: K,value: V): V

将键值对添加到缓冲区。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[LRUCache.put9+](js-apis-util.md#put9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 | 要添加的密钥。 |
| value | V | 是 | 指示与要添加的键关联的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| V | 返回与添加的键关联的值；如果要添加的键已经存在，则返回原始值，如果键或值为空，则抛出此异常。 |

**示例：**

```
1. let pro : util.LruBuffer<number,number> = new util.LruBuffer();
2. let result = pro.put(2,10);
3. console.info("result = " + result);
4. // 输出结果：result = 10
```

### values(deprecated)

PhonePC/2in1TabletTVWearable

values(): V[]

获取当前缓冲区中所有值从最近访问到最近最少访问的顺序列表。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[LRUCache.values9+](js-apis-util.md#values9)替代。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| V [] | 按从最近访问到最近最少访问的顺序返回当前缓冲区中所有值的列表。 |

**示例：**

```
1. let pro : util.LruBuffer<number|string,number|string> = new util.LruBuffer();
2. pro.put(2,10);
3. pro.put(2,"anhu");
4. pro.put("afaf","grfb");
5. let result = pro.values();
6. console.info("result = " + result);
7. // 输出结果：result = anhu,grfb
```

### keys(deprecated)

PhonePC/2in1TabletTVWearable

keys(): K[]

获取当前缓冲区中所有键从最近访问到最近最少访问的升序列表。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[LRUCache.keys9+](js-apis-util.md#keys9)替代。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| K [] | 按升序返回当前缓冲区中所有键的列表，从最近访问到最近最少访问。 |

**示例：**

```
1. let pro : util.LruBuffer<number,number> = new util.LruBuffer();
2. pro.put(2,10);
3. let result = pro.keys();
4. console.info("result = " + result);
5. // 输出结果：result = 2
```

### remove(deprecated)

PhonePC/2in1TabletTVWearable

remove(key: K): V | undefined

删除当前缓冲区中指定的键及其关联的值。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[LRUCache.remove9+](js-apis-util.md#remove9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 | 要删除的密钥。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| V | undefined | 返回一个包含已删除键值对的Optional对象；如果key不存在，则返回一个空的Optional对象，如果key为null，则抛出异常。 |

**示例：**

```
1. let pro : util.LruBuffer<number,number> = new util.LruBuffer();
2. pro.put(2,10);
3. let result = pro.remove(20);
4. console.info("result = " + result);
5. // 输出结果：result = undefined
```

### afterRemoval(deprecated)

PhonePC/2in1TabletTVWearable

afterRemoval(isEvict: boolean,key: K,value: V,newValue: V): void

删除值后执行后续操作。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[LRUCache.afterRemoval9+](js-apis-util.md#afterremoval9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isEvict | boolean | 是 | 因容量不足而调用该方法时，参数值为true，其他情况为false。 |
| key | K | 是 | 表示删除的键。 |
| value | V | 是 | 表示删除的值。 |
| newValue | V | 是 | 如果已调用put方法并且要添加的键已经存在，则参数值是关联的新值。其他情况下参数值为空。 |

**示例：**

```
1. class ChildLruBuffer<K, V> extends util.LruBuffer<K, V> {
2. constructor(capacity?: number) {
3. super(capacity);
4. }

6. afterRemoval(isEvict: boolean, key: K, value: V, newValue: V): void {
7. if (isEvict === true) {
8. console.info('key: ' + key);
9. // 输出结果：key: 11
10. console.info('value: ' + value);
11. // 输出结果：value: 1
12. console.info('newValue: ' + newValue);
13. // 输出结果：newValue: null
14. }
15. }
16. }
17. let lru: ChildLruBuffer<number, number> = new ChildLruBuffer(2);
18. lru.put(11, 1);
19. lru.put(22, 2);
20. lru.put(33, 3);
```

### contains(deprecated)

PhonePC/2in1TabletTVWearable

contains(key: K): boolean

检查当前缓冲区是否包含指定的键。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[LRUCache.contains9+](js-apis-util.md#contains9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 | 表示要检查的键。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果缓冲区包含指定的键，则返回 true。 |

**示例：**

```
1. let pro : util.LruBuffer<number,number> = new util.LruBuffer();
2. pro.put(2,10);
3. let result = pro.contains(20);
4. console.info('result = ' + result);
5. // 输出结果：result = false
```

### createDefault(deprecated)

PhonePC/2in1TabletTVWearable

createDefault(key: K): V

如果未计算特定键的值，则执行后续操作，参数表示丢失的键，返回与键关联的值。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[LRUCache.createDefault9+](js-apis-util.md#createdefault9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 | 表示丢失的键。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| V | 返回与键关联的值。 |

**示例：**

```
1. let pro : util.LruBuffer<number,number> = new util.LruBuffer();
2. let result = pro.createDefault(50);
```

### entries(deprecated)

PhonePC/2in1TabletTVWearable

entries(): IterableIterator<[K, V]>

允许迭代包含在这个对象中的所有键值对。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[LRUCache.entries9+](js-apis-util.md#entries9)替代。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| IterableIterator<[K, V]> | 返回一个可迭代数组。 |

**示例：**

```
1. let pro : util.LruBuffer<number,number> = new util.LruBuffer();
2. pro.put(2,10);
3. let result = pro.entries();
```

### [Symbol.iterator](deprecated)

PhonePC/2in1TabletTVWearable

[Symbol.iterator](): IterableIterator<[K, V]>

返回一个键值对形式的二维数组。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[LRUCache.[Symbol.iterator]9+](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-util#symboliterator9)替代。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| IterableIterator<[K, V]> | 返回一个键值对形式的二维数组。 |

**示例：**

```
1. let pro : util.LruBuffer<number,number> = new util.LruBuffer();
2. pro.put(2,10);
3. let result = pro[Symbol.iterator]();
```

## Scope(deprecated)

PhonePC/2in1TabletTVWearable

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[ScopeHelper9+](js-apis-util.md#scopehelper9)替代。

### constructor(deprecated)

PhonePC/2in1TabletTVWearable

constructor(lowerObj: ScopeType, upperObj: ScopeType)

创建指定下限和上限的作用域实例，并返回一个Scope对象。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[ScopeHelper.constructor9+](js-apis-util.md#constructor9-4)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lowerObj | [ScopeType](js-apis-util.md#scopetype8) | 是 | 指定作用域实例的下限。 |
| upperObj | [ScopeType](js-apis-util.md#scopetype8) | 是 | 指定作用域实例的上限。 |

**示例：**

```
1. class Temperature implements util.ScopeComparable {
2. private readonly _temp: number;

4. constructor(value: number) {
5. this._temp = value;
6. }

8. compareTo(value: Temperature) {
9. return this._temp >= value.getTemp();
10. }

12. getTemp() {
13. return this._temp;
14. }

16. toString(): string {
17. return this._temp.toString();
18. }
19. }

21. let tempLower = new Temperature(30);
22. let tempUpper = new Temperature(40);
23. let range = new util.Scope(tempLower, tempUpper);
24. console.info("range = " + range);
25. // 输出结果：range = [30, 40]
```

### toString(deprecated)

PhonePC/2in1TabletTVWearable

toString(): string

该字符串化方法返回一个包含当前范围的字符串表示形式。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[ScopeHelper.toString9+](js-apis-util.md#tostring9-1)替代。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回包含当前范围对象的字符串表示形式。 |

**示例：**

```
1. class Temperature implements util.ScopeComparable {
2. private readonly _temp: number;

4. constructor(value: number) {
5. this._temp = value;
6. }

8. compareTo(value: Temperature) {
9. return this._temp >= value.getTemp();
10. }

12. getTemp() {
13. return this._temp;
14. }

16. toString(): string {
17. return this._temp.toString();
18. }
19. }

21. let tempLower = new Temperature(30);
22. let tempUpper = new Temperature(40);
23. let range = new util.Scope(tempLower, tempUpper);
24. let result = range.toString();
25. console.info("result = " + result);
26. // 输出结果：result = [30, 40]
```

### intersect(deprecated)

PhonePC/2in1TabletTVWearable

intersect(range: Scope): Scope

获取给定范围和当前范围的交集。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[ScopeHelper.intersect9+](js-apis-util.md#intersect9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| range | [Scope](js-apis-util.md#scopedeprecated) | 是 | 传入一个给定范围。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Scope](js-apis-util.md#scopedeprecated) | 返回给定范围和当前范围的交集。 |

**示例：**

```
1. class Temperature implements util.ScopeComparable {
2. private readonly _temp: number;

4. constructor(value: number) {
5. this._temp = value;
6. }

8. compareTo(value: Temperature) {
9. return this._temp >= value.getTemp();
10. }

12. getTemp() {
13. return this._temp;
14. }

16. toString(): string {
17. return this._temp.toString();
18. }
19. }

21. let tempLower = new Temperature(30);
22. let tempUpper = new Temperature(40);
23. let range = new util.Scope(tempLower, tempUpper);
24. let tempMiDF = new Temperature(35);
25. let tempMidS = new Temperature(39);
26. let rangeFir = new util.Scope(tempMiDF, tempMidS);
27. let result = range.intersect(rangeFir );
28. console.info("result = " + result);
29. // 输出结果：result = [35, 39]
```

### intersect(deprecated)

PhonePC/2in1TabletTVWearable

intersect(lowerObj:ScopeType,upperObj:ScopeType):Scope

获取当前范围与给定下限和上限范围的交集。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[ScopeHelper.intersect9+](js-apis-util.md#intersect9-1)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lowerObj | [ScopeType](js-apis-util.md#scopetype8) | 是 | 给定范围的下限。 |
| upperObj | [ScopeType](js-apis-util.md#scopetype8) | 是 | 给定范围的上限。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Scope](js-apis-util.md#scopedeprecated) | 返回当前范围与给定下限和上限范围的交集。 |

**示例：**

```
1. class Temperature implements util.ScopeComparable {
2. private readonly _temp: number;

4. constructor(value: number) {
5. this._temp = value;
6. }

8. compareTo(value: Temperature) {
9. return this._temp >= value.getTemp();
10. }

12. getTemp() {
13. return this._temp;
14. }

16. toString(): string {
17. return this._temp.toString();
18. }
19. }

21. let tempLower = new Temperature(30);
22. let tempUpper = new Temperature(40);
23. let tempMiDF = new Temperature(35);
24. let tempMidS = new Temperature(39);
25. let range = new util.Scope(tempLower, tempUpper);
26. let result = range.intersect(tempMiDF, tempMidS);
27. console.info("result = " + result);
28. // 输出结果：result = [35, 39]
```

### getUpper(deprecated)

PhonePC/2in1TabletTVWearable

getUpper(): ScopeType

获取当前范围的上限。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[ScopeHelper.getUpper9+](js-apis-util.md#getupper9)替代。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ScopeType](js-apis-util.md#scopetype8) | 返回当前范围的上限值。 |

**示例：**

```
1. class Temperature implements util.ScopeComparable {
2. private readonly _temp: number;

4. constructor(value: number) {
5. this._temp = value;
6. }

8. compareTo(value: Temperature) {
9. return this._temp >= value.getTemp();
10. }

12. getTemp() {
13. return this._temp;
14. }

16. toString(): string {
17. return this._temp.toString();
18. }
19. }

21. let tempLower = new Temperature(30);
22. let tempUpper = new Temperature(40);
23. let range = new util.Scope(tempLower, tempUpper);
24. let result = range.getUpper();
25. console.info("result = " + result);
26. // 输出结果：result = 40
```

### getLower(deprecated)

PhonePC/2in1TabletTVWearable

getLower(): ScopeType

获取当前范围的下限。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[ScopeHelper.getLower9+](js-apis-util.md#getlower9)替代。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ScopeType](js-apis-util.md#scopetype8) | 返回当前范围的下限值。 |

**示例：**

```
1. class Temperature implements util.ScopeComparable {
2. private readonly _temp: number;

4. constructor(value: number) {
5. this._temp = value;
6. }

8. compareTo(value: Temperature) {
9. return this._temp >= value.getTemp();
10. }

12. getTemp() {
13. return this._temp;
14. }

16. toString(): string {
17. return this._temp.toString();
18. }
19. }

21. let tempLower = new Temperature(30);
22. let tempUpper = new Temperature(40);
23. let range = new util.Scope(tempLower, tempUpper);
24. let result = range.getLower();
25. console.info("result = " + result);
26. // 输出结果：result = 30
```

### expand(deprecated)

PhonePC/2in1TabletTVWearable

expand(lowerObj: ScopeType,upperObj: ScopeType): Scope

创建并返回包括当前范围和给定下限和上限的并集。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[ScopeHelper.expand9+](js-apis-util.md#expand9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| lowerObj | [ScopeType](js-apis-util.md#scopetype8) | 是 | 给定范围的下限。 |
| upperObj | [ScopeType](js-apis-util.md#scopetype8) | 是 | 给定范围的上限。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Scope](js-apis-util.md#scopedeprecated) | 返回当前范围和给定下限和上限的并集。 |

**示例：**

```
1. class Temperature implements util.ScopeComparable {
2. private readonly _temp: number;

4. constructor(value: number) {
5. this._temp = value;
6. }

8. compareTo(value: Temperature) {
9. return this._temp >= value.getTemp();
10. }

12. getTemp() {
13. return this._temp;
14. }

16. toString(): string {
17. return this._temp.toString();
18. }
19. }

21. let tempLower = new Temperature(30);
22. let tempUpper = new Temperature(40);
23. let tempMiDF = new Temperature(35);
24. let tempMidS = new Temperature(39);
25. let range = new util.Scope(tempLower, tempUpper);
26. let result = range.expand(tempMiDF, tempMidS);
27. console.info("result = " + result);
28. // 输出结果：result = [30, 40]
```

### expand(deprecated)

PhonePC/2in1TabletTVWearable

expand(range: Scope): Scope

创建并返回包括当前范围和给定范围的并集。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[ScopeHelper.expand9+](js-apis-util.md#expand9-1)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| range | [Scope](js-apis-util.md#scopedeprecated) | 是 | 传入一个给定范围。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Scope](js-apis-util.md#scopedeprecated) | 返回包括当前范围和给定范围的并集。 |

**示例：**

```
1. class Temperature implements util.ScopeComparable {
2. private readonly _temp: number;

4. constructor(value: number) {
5. this._temp = value;
6. }

8. compareTo(value: Temperature) {
9. return this._temp >= value.getTemp();
10. }

12. getTemp() {
13. return this._temp;
14. }

16. toString(): string {
17. return this._temp.toString();
18. }
19. }

21. let tempLower = new Temperature(30);
22. let tempUpper = new Temperature(40);
23. let tempMiDF = new Temperature(35);
24. let tempMidS = new Temperature(39);
25. let range = new util.Scope(tempLower, tempUpper);
26. let rangeFir = new util.Scope(tempMiDF, tempMidS);
27. let result = range.expand(rangeFir);
28. console.info("result = " + result);
29. // 输出结果：result = [30, 40]
```

### expand(deprecated)

PhonePC/2in1TabletTVWearable

expand(value: ScopeType): Scope

创建并返回包括当前范围和给定值的并集。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[ScopeHelper.expand9+](js-apis-util.md#expand9-2)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ScopeType](js-apis-util.md#scopetype8) | 是 | 传入一个给定值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Scope](js-apis-util.md#scopedeprecated) | 返回包括当前范围和给定值的并集。 |

**示例：**

```
1. class Temperature implements util.ScopeComparable {
2. private readonly _temp: number;

4. constructor(value: number) {
5. this._temp = value;
6. }

8. compareTo(value: Temperature) {
9. return this._temp >= value.getTemp();
10. }

12. getTemp() {
13. return this._temp;
14. }

16. toString(): string {
17. return this._temp.toString();
18. }
19. }

21. let tempLower = new Temperature(30);
22. let tempUpper = new Temperature(40);
23. let tempMiDF = new Temperature(35);
24. let range = new util.Scope(tempLower, tempUpper);
25. let result = range.expand(tempMiDF);
26. console.info("result = " + result);
27. // 输出结果：result = [30, 40]
```

### contains(deprecated)

PhonePC/2in1TabletTVWearable

contains(value: ScopeType): boolean

检查给定value是否包含在当前范围内。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[ScopeHelper.contains9+](js-apis-util.md#contains9-1)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ScopeType](js-apis-util.md#scopetype8) | 是 | 传入一个给定值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果给定值包含在当前范围内返回true，否则返回false。 |

**示例：**

```
1. class Temperature implements util.ScopeComparable {
2. private readonly _temp: number;

4. constructor(value: number) {
5. this._temp = value;
6. }

8. compareTo(value: Temperature) {
9. return this._temp >= value.getTemp();
10. }

12. getTemp() {
13. return this._temp;
14. }

16. toString(): string {
17. return this._temp.toString();
18. }
19. }

21. let tempLower = new Temperature(30);
22. let tempUpper = new Temperature(40);
23. let tempMiDF = new Temperature(35);
24. let range = new util.Scope(tempLower, tempUpper);
25. let result = range.contains(tempMiDF);
26. console.info("result = " + result);
27. // 输出结果：result = true
```

### contains(deprecated)

PhonePC/2in1TabletTVWearable

contains(range: Scope): boolean

检查给定range是否在当前范围内。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[ScopeHelper.contains9+](js-apis-util.md#contains9-2)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| range | [Scope](js-apis-util.md#scopedeprecated) | 是 | 传入一个给定范围。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果给定范围包含在当前范围内返回true，否则返回false。 |

**示例：**

```
1. class Temperature implements util.ScopeComparable {
2. private readonly _temp: number;

4. constructor(value: number) {
5. this._temp = value;
6. }

8. compareTo(value: Temperature) {
9. return this._temp >= value.getTemp();
10. }

12. getTemp() {
13. return this._temp;
14. }

16. toString(): string {
17. return this._temp.toString();
18. }
19. }

21. let tempLower = new Temperature(30);
22. let tempUpper = new Temperature(40);
23. let range = new util.Scope(tempLower, tempUpper);
24. let tempLess = new Temperature(20);
25. let tempMore = new Temperature(45);
26. let rangeSec = new util.Scope(tempLess, tempMore);
27. let result = range.contains(rangeSec);
28. console.info("result = " + result);
29. // 输出结果：result = false
```

### clamp(deprecated)

PhonePC/2in1TabletTVWearable

clamp(value: ScopeType): ScopeType

将给定值限定到当前范围内。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[ScopeHelper.clamp9+](js-apis-util.md#clamp9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ScopeType](js-apis-util.md#scopetype8) | 是 | 传入的给定值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ScopeType](js-apis-util.md#scopetype8) | 如果传入的value小于下限，则返回lowerObj；如果大于上限值则返回upperObj；如果在当前范围内，则返回value。 |

**示例：**

```
1. class Temperature implements util.ScopeComparable {
2. private readonly _temp: number;

4. constructor(value: number) {
5. this._temp = value;
6. }

8. compareTo(value: Temperature) {
9. return this._temp >= value.getTemp();
10. }

12. getTemp() {
13. return this._temp;
14. }

16. toString(): string {
17. return this._temp.toString();
18. }
19. }

21. let tempLower = new Temperature(30);
22. let tempUpper = new Temperature(40);
23. let tempMiDF = new Temperature(35);
24. let range = new util.Scope(tempLower, tempUpper);
25. let result = range.clamp(tempMiDF);
26. console.info("result = " + result);
27. // 输出结果：result = 35
```

## Base64(deprecated)

PhonePC/2in1TabletTVWearable

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[Base64Helper9+](js-apis-util.md#base64helper9)替代。

### constructor(deprecated)

PhonePC/2in1TabletTVWearable

constructor()

Base64的构造函数。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[Base64Helper.constructor9+](js-apis-util.md#constructor9-5)替代。

**系统能力：** SystemCapability.Utils.Lang

**示例：**

```
1. let base64 = new  util.Base64();
```

### encodeSync(deprecated)

PhonePC/2in1TabletTVWearable

encodeSync(src: Uint8Array): Uint8Array

将输入的Uint8Array字节数组进行Base64编码，返回编码后的Uint8Array数组。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[Base64Helper.encodeSync9+](js-apis-util.md#encodesync9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | Uint8Array | 是 | 编码输入Uint8数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 返回编码后新分配的Uint8数组。 |

**示例：**

```
1. let base64 = new util.Base64();
2. let array = new Uint8Array([115,49,51]);
3. let result = base64.encodeSync(array);
4. console.info("result = " + result);
5. // 输出结果：result = 99,122,69,122
```

### encodeToStringSync(deprecated)

PhonePC/2in1TabletTVWearable

encodeToStringSync(src: Uint8Array): string

将输入的Uint8Array字节数组进行Base64编码，返回编码后的字符串结果。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[Base64Helper.encodeToStringSync9+](js-apis-util.md#encodetostringsync9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | Uint8Array | 是 | 编码输入Uint8数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回编码后的字符串。 |

**示例：**

```
1. let base64 = new util.Base64();
2. let array = new Uint8Array([115,49,51]);
3. let result = base64.encodeToStringSync(array);
4. console.info("result = " + result);
5. // 输出结果：result = czEz
```

### decodeSync(deprecated)

PhonePC/2in1TabletTVWearable

decodeSync(src: Uint8Array | string): Uint8Array

通过输入参数解码后输出对应文本。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[Base64Helper.decodeSync9+](js-apis-util.md#decodesync9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | Uint8Array | string | 是 | 解码输入Uint8数组或者字符串。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 返回解码后新分配的Uint8数组。 |

**示例：**

```
1. let base64 = new util.Base64();
2. let buff = 'czEz';
3. let result = base64.decodeSync(buff);
4. console.info("result = " + result);
5. // 输出结果：result = 115,49,51
```

### encode(deprecated)

PhonePC/2in1TabletTVWearable

encode(src: Uint8Array): Promise<Uint8Array>

通过输入参数异步编码后输出对应文本。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[Base64Helper.encode9+](js-apis-util.md#encode9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | Uint8Array | 是 | 异步编码输入Uint8数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Uint8Array> | 返回异步编码后新分配的Uint8数组。 |

**示例：**

```
1. let base64 = new util.Base64();
2. let array = new Uint8Array([115,49,51]);
3. base64.encode(array).then((val) => {
4. console.info(val.toString());
5. // 输出结果：99,122,69,122
6. })
```

### encodeToString(deprecated)

PhonePC/2in1TabletTVWearable

encodeToString(src: Uint8Array): Promise<string>

通过输入参数异步编码后输出对应文本。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[Base64Helper.encodeToString9+](js-apis-util.md#encodetostring9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | Uint8Array | 是 | 异步编码输入Uint8数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | 返回异步编码后的字符串。 |

**示例：**

```
1. let base64 = new util.Base64();
2. let array = new Uint8Array([115,49,51]);
3. base64.encodeToString(array).then((val) => {
4. console.info(val);
5. // 输出结果：czEz
6. })
```

### decode(deprecated)

PhonePC/2in1TabletTVWearable

decode(src: Uint8Array | string): Promise<Uint8Array>

将输入参数异步解码后输出对应文本。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[Base64Helper.decode9+](js-apis-util.md#decode9)替代。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | Uint8Array | string | 是 | 异步解码输入Uint8数组或者字符串。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Uint8Array> | 返回异步解码后新分配的Uint8数组。 |

**示例：**

```
1. let base64 = new util.Base64();
2. let array = new Uint8Array([99,122,69,122]);
3. base64.decode(array).then((val) => {
4. console.info(val.toString());
5. // 输出结果：115,49,51
6. })
```
