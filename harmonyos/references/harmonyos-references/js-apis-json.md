---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-json
title: @ohos.util.json (JSON解析与生成)
breadcrumb: API参考 > 应用框架 > ArkTS（方舟编程语言） > ArkTS API > @ohos.util.json (JSON解析与生成)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:08+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:44fe4e36192bbc4fc36b176e42b2e96127c71ba5faa969d3235390fb2d95a047
---

本模块提供了将JSON文本转换为JSON对象或值，以及将对象转换为JSON文本等功能。

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { JSON } from '@kit.ArkTS';
```

## Transformer

PhonePC/2in1TabletTVWearable

type Transformer = (this: Object, key: string, value: Object) => Object | undefined | null

用于转换结果函数的类型。

作为[JSON.parse](js-apis-json.md#jsonparse)函数的参数时，对象的每个成员将会调用此函数，允许在解析过程中对数据进行自定义处理或转换。

作为[JSON.stringify](js-apis-json.md#jsonstringify-1)函数的参数时，序列化时，每个属性都会经过该函数的转换处理。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| this | Object | 是 | 在解析的键值对所属的对象。 |
| key | string | 是 | 属性名。 |
| value | Object | 是 | 在解析的键值对的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Object | undefined | null | 返回修改后的对象或undefined或null。 |

## BigIntMode

PhonePC/2in1TabletTVWearable

定义处理BigInt的模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 0 | 不支持BigInt。 |
| PARSE\_AS\_BIGINT | 1 | 当整数小于-(2^53-1)或大于(2^53-1)时，解析为BigInt。 |
| ALWAYS\_PARSE\_AS\_BIGINT | 2 | 所有整数都解析为BigInt。 |

## ParseOptions

PhonePC/2in1TabletTVWearable

解析的选项，可定义处理BigInt的模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bigIntMode | [BigIntMode](js-apis-json.md#bigintmode) | 否 | 否 | 定义处理BigInt的模式。 |

## JSON.parse

PhonePC/2in1TabletTVWearable

parse(text: string, reviver?: Transformer, options?: ParseOptions): Object | null

解析JSON字符串生成ArkTS对象或null。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 有效的JSON字符串。 |
| reviver | [Transformer](js-apis-json.md#transformer) | 否 | 转换函数，传入该参数，可以用来修改解析生成的原始值。默认值是undefined。 |
| options | [ParseOptions](js-apis-json.md#parseoptions) | 否 | 解析的配置，传入该参数，可以用来控制解析生成的类型。默认值是undefined。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Object | null | 返回ArkTS对象或null。当入参是null时，返回null。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { JSON } from '@kit.ArkTS';

3. function reviverFunc(key: string, value: Object): Object | undefined | null {
4. if (key === "age" && typeof value === 'number') {
5. return value + 1;
6. }
7. return value;
8. }

10. const jsonText = '{"name": "John", "age": 30, "city": "ChongQing"}';
11. let obj = JSON.parse(jsonText);
12. console.info((obj as object)?.["name"]);
13. // 打印结果：John

15. const jsonTextStr = '{"name": "John", "age": 30}';
16. let objRst = JSON.parse(jsonTextStr, reviverFunc);
17. console.info((objRst as object)?.["age"]);
18. // 打印结果：31

20. const numberText = '{"number": 10, "largeNumber": 112233445566778899}';
21. let options: JSON.ParseOptions = { bigIntMode: JSON.BigIntMode.PARSE_AS_BIGINT }
22. let numberObj = JSON.parse(numberText, null, options) as Object;

24. console.info(typeof (numberObj as object)?.["number"]);
25. // 打印结果: number
26. console.info((numberObj as object)?.["number"]);
27. // 打印结果: 10

29. console.info(typeof (numberObj as object)?.["largeNumber"]);
30. // 打印结果: bigint
31. console.info((numberObj as object)?.["largeNumber"]);
32. // 打印结果: 112233445566778899
```

## JSON.stringify

PhonePC/2in1TabletTVWearable

stringify(value: Object, replacer?: (number | string)[] | null, space?: string | number): string

该方法将一个ArkTS对象或数组转换为JSON字符串，支持线性容器的转换，不支持非线性容器。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Object | 是 | ArkTS对象或数组。支持线性容器的转换，不支持非线性容器。 |
| replacer | number[] | string[] | null | 否 | 当参数是数组时，只有包含在这个数组中的属性名才会被序列化到最终的JSON字符串中；当参数为null或者未提供时，则对象所有的属性都会被序列化。默认值是undefined。 |
| space | string | number | 否 | 指定缩进用的空格或字符串，用于美化输出。当参数是数字时表示缩进空格数；当参数是字符串时表示缩进字符；无参数则无缩进。默认值是空字符串。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 转换后的JSON字符串。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { JSON } from '@kit.ArkTS';

3. interface Person {
4. name: string;
5. age: number;
6. city: string;
7. }

9. let person: Person = {name: "John",age: 30, city: "New York"};

11. let rstArrStr = JSON.stringify(person, ["name", "age"]);
12. console.info(rstArrStr);
13. // 打印结果：{"name":"John","age":30}

15. let rstStrSpace = JSON.stringify(person, ["name", "age"], '  ');
16. console.info(rstStrSpace);
17. /*
18. 打印结果：
19. {
20. "name": "John",
21. "age": 30
22. }
23. */

25. let rstStrStar = JSON.stringify(person, ["name", "age"], '  &&');
26. console.info(rstStrStar);
27. /*
28. 打印结果：
29. {
30. &&"name": "John",
31. &&"age": 30
32. }
33. */

35. let bigIntObj = BigInt(112233445566778899n);
36. console.info(JSON.stringify(bigIntObj));
37. // 打印结果：112233445566778899
```

## JSON.stringify

PhonePC/2in1TabletTVWearable

stringify(value: Object, replacer?: Transformer, space?: string | number): string

该方法将一个ArkTS对象或数组转换为JSON字符串，支持线性容器的转换，不支持非线性容器。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Object | 是 | ArkTS对象或数组，支持线性容器的转换，不支持非线性容器。 |
| replacer | [Transformer](js-apis-json.md#transformer) | 否 | 在序列化过程中，被序列化的值的每个属性都会经过该函数的转换和处理。默认值是undefined。 |
| space | string | number | 否 | 指定缩进用的空格或字符串或空字符串，用于美化输出。当参数是数字时表示有多少个空格；当参数是字符串时，该字符串被当作空格；当参数没有提供时，将没有空格。默认值是空字符串。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 转换后的JSON字符串。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { JSON } from '@kit.ArkTS';

3. function replacer(key: string, value: Object): Object {
4. if (typeof value === "string") {
5. return value.toUpperCase();
6. }
7. return value;
8. }

10. interface Person {
11. name: string;
12. age: number;
13. city: string;
14. }
15. let inputObj = {"name": "John", "age": 30, "city": "ChongQing"} as Person;

17. console.info(JSON.stringify(inputObj, replacer));
18. // 打印结果：{"name":"JOHN","age":30,"city":"CHONGQING"}

20. console.info(JSON.stringify(inputObj, replacer, '  '));
21. /*
22. 打印结果：
23. {
24. "name": "JOHN",
25. "age": 30,
26. "city": "CHONGQING"
27. }
28. */
```

## JSON.has

PhonePC/2in1TabletTVWearable

has(obj: object, property: string): boolean

检查ArkTS对象是否包含某种属性，可用于[JSON.parse](js-apis-json.md#jsonparse)解析JSON字符串之后。has接口仅支持最外层为字典形式（即大括号而非中括号包围）的合法json串。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| obj | object | 是 | ArkTS对象。 |
| property | string | 是 | 属性名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回ArkTS对象是否包含某种属性结果。true表示包含，false表示不包含。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. import { JSON } from '@kit.ArkTS';

3. const jsonText = '{"name": "John", "age": 30, "city": "ChongQing"}';
4. let inputObj = JSON.parse(jsonText);
5. let result = JSON.has(inputObj, "name");
6. console.info("result = " + result);
7. // 打印结果：result = true
```

## JSON.remove

PhonePC/2in1TabletTVWearable

remove(obj: object, property: string): void

从ArkTS对象中删除某种属性，可用于[JSON.parse](js-apis-json.md#jsonparse)解析JSON字符串之后。JSON.remove接口仅支持最外层为字典形式（即大括号而非中括号包围）的合法json串。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| obj | object | 是 | ArkTS对象。 |
| property | string | 是 | 属性名。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |

**示例：**

```
1. import { JSON } from '@kit.ArkTS';

3. const jsonText = '{"name": "John", "age": 30, "city": "ChongQing"}';
4. let inputObj = JSON.parse(jsonText);
5. JSON.remove(inputObj, "name");
6. let result = JSON.has(inputObj, "name");
7. console.info("result = " + result);
8. // 打印结果：result = false
```
