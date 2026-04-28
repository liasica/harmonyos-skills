---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-utils-sendablelrucache
title: SendableLruCache<K, V>
breadcrumb: API参考 > 应用框架 > ArkTS（方舟编程语言） > ArkTS API > @arkts.utils (ArkTS工具库) > SendableLruCache<K, V>
category: harmonyos-references
scraped_at: 2026-04-28T08:00:00+08:00
doc_updated_at: 2026-04-10
content_hash: sha256:fcad0a87e65bb38edc81c98f435dfa4857d2ae9983db18dbe039da5fbf1b0a62
---

SendableLruCache在缓存空间不足时，会用新数据替换近期最少使用的数据。此设计基于资源访问的考虑：近期访问的数据可能在不久的将来再次访问，因此最少访问的数据价值最小，应优先移出缓存。SendableLruCache支持Sendable特性，可保存Sendable对象，确保跨线程安全访问。

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

SendableLruCache首批接口从API version 18开始支持。

此模块仅支持在ArkTS文件（文件后缀为.ets）中导入使用。

**装饰器类型：**@Sendable

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { ArkTSUtils } from '@kit.ArkTS'
```

## 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| length18+ | number | 是 | 否 | 当前缓冲区中值的总数。 |

**示例：**

```
1. let pro = new ArkTSUtils.SendableLruCache<number, number>();
2. pro.put(2, 10);
3. pro.put(1, 8);
4. let result = pro.length;
5. console.info('result = ' + result);
6. // 期望输出：result = 2
```

## constructor18+

PhonePC/2in1TabletTVWearable

constructor(capacity?: number)

默认构造函数用于创建一个新的SendableLruCache实例，默认容量为64。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| capacity | number | 否 | 指示缓冲区的自定义容量。不传时，默认值为64，最大值不能超过2147483647；小于等于0时会抛出异常。 |

**示例：**

```
1. let pro = new ArkTSUtils.SendableLruCache<number, number>();
```

## updateCapacity18+

PhonePC/2in1TabletTVWearable

updateCapacity(newCapacity: number): void

将缓冲区容量设置为指定值。如果缓冲区中值的总数超过指定容量，将删除最少使用的键值对。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| newCapacity | number | 是 | 指示要为缓冲区自定义的容量，最大值不能超过2147483647；小于等于0时会抛出异常。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified;2.Incorrect parameter types. |

**示例：**

```
1. let pro = new ArkTSUtils.SendableLruCache<number, number>();
2. pro.updateCapacity(100);
```

## toString18+

PhonePC/2in1TabletTVWearable

toString(): string

返回对象的字符串表示形式。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回对象的字符串表示形式。 返回字符串格式是：SendableLruCache[ maxSize = (maxSize), hits = (hitCount), misses = (missCount), hitRate = (hitRate) ]。 (maxSize)表示缓存区最大值，(hitCount)表示查询值匹配成功的次数，(missCount)表示查询值匹配失败的次数，(hitRate)表示查询值匹配率。 |

**示例：**

```
1. let pro = new ArkTSUtils.SendableLruCache<number, number>();
2. pro.put(2, 10);
3. pro.get(2);
4. pro.get(3);
5. console.info(pro.toString());
6. // 预期输出：SendableLruCache[ maxSize = 64, hits = 1, misses = 1, hitRate = 50% ]
7. // maxSize: 缓存区最大值 hits: 查询值匹配成功的次数 misses: 查询值匹配失败的次数 hitRate: 查询值匹配率
```

## getCapacity18+

PhonePC/2in1TabletTVWearable

getCapacity(): number

获取当前缓冲区的容量。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回当前缓冲区的容量。 |

**示例：**

```
1. let pro = new ArkTSUtils.SendableLruCache<number, number>();
2. let result = pro.getCapacity();
3. console.info('result = ' + result);
4. // 预期输出：result = 64
```

## clear18+

PhonePC/2in1TabletTVWearable

clear(): void

从当前缓冲区清除所有键值对。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**示例：**

```
1. let pro = new ArkTSUtils.SendableLruCache<number, number>();
2. pro.put(2, 10);
3. let result = pro.length;
4. pro.clear();
5. let res = pro.length;
6. console.info('result = ' + result);
7. console.info('res = ' + res);
8. // 预期输出：result = 1
9. // 预期输出：res = 0
```

## getCreateCount18+

PhonePC/2in1TabletTVWearable

getCreateCount(): number

获取调用内部默认接口创建对象的次数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回使用内部默认接口创建对象的次数。 |

**示例：**

```
1. @Sendable
2. class ChildLRUCache extends ArkTSUtils.SendableLruCache<number, number> {
3. constructor() {
4. super();
5. }
6. createDefault(key: number): number {
7. return key;
8. }
9. }

11. let lru = new ChildLRUCache();
12. lru.put(2, 10);
13. lru.get(3);
14. lru.get(5);
15. let res = lru.getCreateCount();
16. console.info('res = ' + res);
17. // 预期输出：res = 2
18. // 执行get操作时，如果键值不存在，调用createDefault接口判断返回值是否等于undefined
19. // 如果不等于，则需要把key和返回值作为键值对添加到cache中，并且创建次数加1
```

## getMissCount18+

PhonePC/2in1TabletTVWearable

getMissCount(): number

获取查询值不匹配的次数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回查询值不匹配的次数。 |

**示例：**

```
1. let pro = new ArkTSUtils.SendableLruCache<number, number>();
2. pro.put(2, 10);
3. pro.get(2);
4. let result = pro.getMissCount();
5. console.info('result = ' + result);
6. // 预期输出：result = 0
```

## getRemoveCount18+

PhonePC/2in1TabletTVWearable

getRemoveCount(): number

获取缓冲区键值对的回收次数。当缓冲区数量超过容量限制时，最少使用的键值对将被回收。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回缓冲区键值对回收的次数。 |

**示例：**

```
1. let pro = new ArkTSUtils.SendableLruCache<number, number>();
2. pro.put(2, 10);
3. pro.updateCapacity(2);
4. pro.put(50, 22);
5. let result = pro.getRemoveCount();
6. console.info('result = ' + result);
7. // 预期输出：result = 0
```

## getMatchCount18+

PhonePC/2in1TabletTVWearable

getMatchCount(): number

获取查询值匹配成功的次数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回查询值匹配成功的次数。 |

**示例：**

```
1. let pro = new ArkTSUtils.SendableLruCache<number, number>();
2. pro.put(2, 10);
3. pro.get(2);
4. let result = pro.getMatchCount();
5. console.info('result = ' + result);
6. // 预期输出：result = 1
```

## getPutCount18+

PhonePC/2in1TabletTVWearable

getPutCount(): number

获取将值添加到缓冲区的次数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回将值添加到缓冲区的次数。 |

**示例：**

```
1. let pro = new ArkTSUtils.SendableLruCache<number, number>();
2. pro.put(2, 10);
3. let result = pro.getPutCount();
4. console.info('result = ' + result);
5. // 预期输出：result = 1
```

## isEmpty18+

PhonePC/2in1TabletTVWearable

isEmpty(): boolean

检查当前缓冲区是否为空。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示当前缓冲区为空，不包含任何键值对；返回false表示当前缓冲区不为空。 |

**示例：**

```
1. let pro = new ArkTSUtils.SendableLruCache<number, number>();
2. pro.put(2, 10);
3. let result = pro.isEmpty();
4. console.info('result = ' + result);
5. // 预期输出：result = false
```

## get18+

PhonePC/2in1TabletTVWearable

get(key: K): V | undefined

返回键对应的值。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 | 要查询的键。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| V | undefined | 如果指定的键存在于缓冲区中，则返回与键关联的值；否则调用内部默认接口，生成一个键与值相同的对象，并返回其值。如果内部默认接口返回undefined，则最终返回undefined。 |

**示例：**

```
1. let pro = new ArkTSUtils.SendableLruCache<number, number>();
2. pro.put(2, 10);
3. let result  = pro.get(2);
4. console.info('result = ' + result);
5. // 预期输出：result = 10
```

## put18+

PhonePC/2in1TabletTVWearable

put(key: K,value: V): V

将键值对添加到缓冲区，并返回与添加的键关联的值。当缓冲区中值的数量超过容量时，会执行删除操作。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 | 要添加的键。 |
| value | V | 是 | 与要添加的键关联的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| V | 返回与添加的键关联的值。 |

**示例：**

```
1. let pro = new ArkTSUtils.SendableLruCache<number, number>();
2. let result = pro.put(2, 10);
3. console.info('result = ' + result);
4. // 预期输出：result = 10
```

## values18+

PhonePC/2in1TabletTVWearable

values(): V[]

获取当前缓冲区中所有值的列表，按从最近访问到最少访问的顺序排列，最近访问的键值对表示有最新操作。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| V [] | 返回当前缓冲区中所有值的列表，按从最近访问到最少访问的顺序排列。 |

**示例：**

```
1. let pro = new ArkTSUtils.SendableLruCache<number|string,number|string>();
2. pro.put(2, 10);
3. pro.put(2, "anhu");
4. pro.put("afaf", "grfb");
5. let result = pro.values();
6. console.info('result = ' + result);
7. // 预期输出：result = anhu,grfb
```

## keys18+

PhonePC/2in1TabletTVWearable

keys(): K[]

获取当前缓冲区中所有键，按从最近访问到最少访问的顺序排列。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| K [] | 返回当前缓冲区中所有键的列表，按从最近访问到最少访问的顺序排列。 |

**示例：**

```
1. let pro = new ArkTSUtils.SendableLruCache<number, number>();
2. pro.put(2, 10);
3. pro.put(3, 1);
4. let result = pro.keys();
5. console.info('result = ' + result);
6. // 预期输出：result = 2,3
```

## remove18+

PhonePC/2in1TabletTVWearable

remove(key: K): V | undefined

从当前缓冲区中删除指定键及其关联值，返回该键关联的值。若键不存在，则返回undefined。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 | 要删除的键值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| V | undefined | 返回与key关联的值；若key不存在，则返回undefined。 |

**示例：**

```
1. let pro = new ArkTSUtils.SendableLruCache<number, number>();
2. pro.put(2, 10);
3. let result = pro.remove(20);
4. console.info('result = ' + result);
5. // 预期输出：result = undefined
```

## contains18+

PhonePC/2in1TabletTVWearable

contains(key: K): boolean

检查当前缓冲区是否包含指定的键，如果存在，返回true；否则，返回false。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | K | 是 | 表示要检查的键。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 如果缓冲区包含指定的键，则返回true，否则返回false。 |

**示例：**

```
1. let pro = new ArkTSUtils.SendableLruCache<number, number>();
2. pro.put(2, 10);
3. let result = pro.contains(2);
4. console.info('result = ' + result);
5. // 预期输出：result = true
```

## entries18+

PhonePC/2in1TabletTVWearable

entries(): IterableIterator<[K,V]>

允许迭代包含在这个对象中的所有键值对。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| IterableIterator<[K, V]> | 返回一个可迭代数组。 |

**示例：**

```
1. let pro = new ArkTSUtils.SendableLruCache<number, number>();
2. pro.put(2, 10);
3. pro.put(3, 15);
4. let pair:Iterable<Object[]> = pro.entries();
5. let arrayValue = Array.from(pair);
6. for (let value of arrayValue) {
7. console.info(value[0]+ ', '+ value[1]);
8. // 预期输出：
9. // 2, 10
10. // 3, 15
11. }
```
