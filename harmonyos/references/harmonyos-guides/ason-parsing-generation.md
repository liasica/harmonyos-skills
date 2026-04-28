---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ason-parsing-generation
title: ASON解析与生成
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 并发线程间通信 > 线程间通信对象 > Sendable对象 > ASON解析与生成
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6df9364004d81bda5078bf9f108f57b95fe461ea0967dbc29ee31ff20eab80b3
---

[ASON工具](../harmonyos-references/arkts-apis-arkts-utils-ason.md)与JS提供的JSON工具类似，JSON用于进行JS对象的序列化（stringify）、反序列化（parse）。ASON则提供了[Sendable对象](arkts-sendable.md)的序列化、反序列化能力。使用ASON.stringify方法可将对象转换为字符串，使用ASON.parse方法可将字符串转换为Sendable对象，从而实现对象在并发任务间的高性能引用传递。

ASON.stringify方法还支持将Map和Set对象转换为字符串，可转换的Map和Set类型包括：Map、Set、[collections.Map](../harmonyos-references/arkts-apis-arkts-collections-map.md)、[collections.Set](../harmonyos-references/arkts-apis-arkts-collections-set.md)、[HashMap](../harmonyos-references/js-apis-hashmap.md#hashmap)、[HashSet](../harmonyos-references/js-apis-hashset.md#hashset)。

说明

ASON.parse默认生成的对象为Sendable对象，布局不可变，不支持增删属性。如果返回的对象需要支持增删属性，可以指定返回类型为[collections.Map](../harmonyos-references/arkts-apis-arkts-collections-map.md)对象。

## 使用示例

使用ASON提供的接口，对[Sendable对象](arkts-sendable.md)进行序列化、反序列化。

```
1. import { ArkTSUtils, collections } from '@kit.ArkTS';

3. ArkTSUtils.ASON.parse("{}")
4. ArkTSUtils.ASON.stringify(new collections.Array(1, 2, 3))

6. let options2: ArkTSUtils.ASON.ParseOptions = {
7. bigIntMode: ArkTSUtils.ASON.BigIntMode.PARSE_AS_BIGINT,
8. parseReturnType: ArkTSUtils.ASON.ParseReturnType.MAP,
9. }
10. let jsonText = '{"largeNumber":112233445566778899}';
11. let map = ArkTSUtils.ASON.parse(jsonText, undefined, options2);
12. // 执行结果为：{"largeNumber":112233445566778899}
13. console.info(ArkTSUtils.ASON.stringify(map));
```
