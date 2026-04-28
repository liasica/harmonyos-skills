---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-utils-ason
title: ArkTSUtils.ASON
breadcrumb: API参考 > 应用框架 > ArkTS（方舟编程语言） > ArkTS API > @arkts.utils (ArkTS工具库) > ArkTSUtils.ASON
category: harmonyos-references
scraped_at: 2026-04-28T08:00:00+08:00
doc_updated_at: 2026-04-10
content_hash: sha256:31ccd24616d2dfcd1509641e9d998f08ad176b66212027e0692f3b3c4b2bec9a
---

为支持将JSON字符串解析为共享数据，即[Sendable支持的数据类型](../harmonyos-guides/arkts-sendable.md#sendable支持的数据类型)，ArkTS语言基础库新增了ASON工具。ASON工具支持解析JSON字符串并生成共享数据，用于跨并发实例引用传递，同时也支持将共享数据转换为JSON字符串。

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

此模块仅支持在ArkTS文件（文件后缀为.ets）中导入使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { ArkTSUtils } from '@kit.ArkTS'
```

## ISendable

PhonePC/2in1TabletTVWearable

type ISendable = lang.ISendable

ISendable是所有Sendable类型（除null和undefined）的父类型。自身没有任何必要的方法和属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

| 类型 | 说明 |
| --- | --- |
| [lang.ISendable](js-apis-arkts-lang.md#langisendable) | 所有Sendable类型的父类型。 |

## Transformer

PhonePC/2in1TabletTVWearable

type Transformer = (this: ISendable, key: string, value: ISendable | undefined | null) => ISendable | undefined | null

用于转换结果函数的类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| this | [ISendable](arkts-apis-arkts-utils-ason.md#isendable) | 是 | 所解析的键值对所属的对象。 |
| key | string | 是 | 属性名。 |
| value | [ISendable](arkts-apis-arkts-utils-ason.md#isendable) | undefined | null | 是 | 所解析的键值对的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ISendable](arkts-apis-arkts-utils-ason.md#isendable) | undefined | null | 返回转换结果后的ISendable对象或undefined或null。 |

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

## ParseReturnType

PhonePC/2in1TabletTVWearable

定义解析结果的返回类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 值 | 说明 |
| --- | --- | --- |
| OBJECT | 0 | 返回 SendableObject 对象。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| MAP13+ | 1 | 返回 SendableMap 对象。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |

## ParseOptions

PhonePC/2in1TabletTVWearable

解析的选项，可定义处理BigInt的模式和解析结果的返回类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bigIntMode | [BigIntMode](arkts-apis-arkts-utils-ason.md#bigintmode) | 否 | 否 | 定义处理BigInt的模式。 |
| parseReturnType | [ParseReturnType](arkts-apis-arkts-utils-ason.md#parsereturntype) | 否 | 否 | 定义解析结果的返回类型。 |

## parse

PhonePC/2in1TabletTVWearable

parse(text: string, reviver?: Transformer, options?: ParseOptions): ISendable | null

用于解析JSON字符串生成ISendable数据或null。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 有效的JSON字符串。 |
| reviver | [Transformer](arkts-apis-arkts-utils-ason.md#transformer) | 否 | 转换函数，传入该参数，可以用来修改解析生成的原始值。默认值是undefined。该参数目前仅支持传入undefined值，其他值会被忽略或视为无效。 |
| options | [ParseOptions](arkts-apis-arkts-utils-ason.md#parseoptions) | 否 | 解析的配置，传入该参数，可以用来控制解析生成的结果类型。默认值是undefined。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ISendable](arkts-apis-arkts-utils-ason.md#isendable) | null | 返回ISendable数据或null。入参为null时，返回null。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Invalid JSON string. |

**示例：**

```
1. import { ArkTSUtils, collections, lang} from '@kit.ArkTS';

3. type ISendable = lang.ISendable;
4. let jsonText = '{"name": "John", "age": 30, "city": "ChongQing"}';
5. let obj = ArkTSUtils.ASON.parse(jsonText) as ISendable;
6. console.info((obj as object)?.["name"]);
7. // 期望输出: 'John'
8. console.info((obj as object)?.["age"]);
9. // 期望输出: 30
10. console.info((obj as object)?.["city"]);
11. // 期望输出: 'ChongQing'

13. let options: ArkTSUtils.ASON.ParseOptions = {
14. bigIntMode: ArkTSUtils.ASON.BigIntMode.PARSE_AS_BIGINT,
15. parseReturnType: ArkTSUtils.ASON.ParseReturnType.OBJECT,
16. }
17. let numberText = '{"largeNumber":112233445566778899}';
18. let numberObj = ArkTSUtils.ASON.parse(numberText,undefined,options) as ISendable;

20. console.info((numberObj as object)?.["largeNumber"]);
21. // 期望输出: 112233445566778899

23. let options2: ArkTSUtils.ASON.ParseOptions = {
24. bigIntMode: ArkTSUtils.ASON.BigIntMode.PARSE_AS_BIGINT,
25. parseReturnType: ArkTSUtils.ASON.ParseReturnType.MAP,
26. }
27. let mapText = '{"largeNumber":112233445566778899}';
28. let map  = ArkTSUtils.ASON.parse(mapText,undefined,options2);
29. console.info("map is " + map);
30. // 期望输出: map is [object SendableMap]
31. console.info("largeNumber is " + (map as collections.Map<string,bigint>).get("largeNumber"));
32. // 期望输出: largeNumber is 112233445566778899
```

## stringify

PhonePC/2in1TabletTVWearable

stringify(value: Object | null | undefined): string

该方法将ArkTS对象数据转换为JSON字符串，额外支持Map和Set相关类型。

说明

从API 18开始参数修改为Object类型，API 18之前参数只支持ISendable类型（除[Int8Array](arkts-apis-arkts-collections-int8array.md)、[Uint8Array](arkts-apis-arkts-collections-uint8array.md)、[Int16Array](arkts-apis-arkts-collections-int16array.md)、[Uint16Array](arkts-apis-arkts-collections-uint16array.md)、[Int32Array](arkts-apis-arkts-collections-int32array.md)、[Uint32Array](arkts-apis-arkts-collections-uint32array.md)、[Uint8ClampedArray](arkts-apis-arkts-collections-uint8clampedarray.md)、[Float32Array](arkts-apis-arkts-collections-float32array.md)外）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Object | null | undefined | 是 | ArkTS对象数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 转换后的JSON字符串。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Invalid ArkTS value. |

**示例：**

```
1. import { ArkTSUtils, collections, HashMap, HashSet } from '@kit.ArkTS';

3. let hashMap = new HashMap<string,string>();
4. hashMap.set("ha","a");
5. hashMap.set("sh","b");
6. hashMap.set("map","c");
7. let str1 = ArkTSUtils.ASON.stringify(hashMap);
8. console.info(str1);
9. // 因HashMap的存储顺序由hashCode决定，因此存储位置不确定，输出可能是：'{"sh":"b","ha":"a","map":"c"}'
10. let hashSet = new HashSet<string>();
11. hashSet.add("ha");
12. hashSet.add("sh");
13. hashSet.add("set");
14. let str2 = ArkTSUtils.ASON.stringify(hashSet);
15. console.info(str2);
16. // 因HashSet的存储顺序由hashCode决定，因此存储位置不确定，输出可能是：'["set","sh","ha"]'
17. let map = new Map<string,string>();
18. map.set("m","a");
19. map.set("a","b");
20. map.set("p","c");
21. let str3 = ArkTSUtils.ASON.stringify(map);
22. console.info(str3);
23. // 期望输出：'{"m":"a","a":"b","p":"c"}'
24. let set = new Set<string>();
25. set.add("s");
26. set.add("e");
27. set.add("t");
28. let str4 = ArkTSUtils.ASON.stringify(set);
29. console.info(str4);
30. // 期望输出：'["s","e","t"]'
31. let sendableMap = new collections.Map<string,string>();
32. sendableMap.set("send","a");
33. sendableMap.set("able","b");
34. sendableMap.set("map","c");
35. let str5 = ArkTSUtils.ASON.stringify(sendableMap);
36. console.info(str5);
37. // 期望输出：'{"send":"a","able":"b","map":"c"}'
38. let sendableSet = new collections.Set<string>();
39. sendableSet.add("send");
40. sendableSet.add("able");
41. sendableSet.add("set");
42. let str6 = ArkTSUtils.ASON.stringify(sendableSet);
43. console.info(str6);
44. // 期望输出：'["send","able","set"]'
```
