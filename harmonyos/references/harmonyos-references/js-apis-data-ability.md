---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-ability
title: @ohos.data.dataAbility (DataAbility谓词)
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > ArkTS API > @ohos.data.dataAbility (DataAbility谓词)
category: harmonyos-references
scraped_at: 2026-04-28T07:59:09+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:feb05181f75914b709e0dc2ecad68e00fa31e0fc5c7ee0894bf3ed861ac2aa31
---

DataAbility谓词用于构造关系型数据库的谓词，提供用于实现不同查询方法的谓词。

说明

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { dataAbility } from '@kit.ArkData';
```

## dataAbility.createRdbPredicates

PhonePC/2in1TabletTVWearable

createRdbPredicates(name: string, dataAbilityPredicates: DataAbilityPredicates): rdb.RdbPredicates

通过表名和DataAbility谓词对象创建Rdb谓词对象。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 数据库表中的表名。 |
| dataAbilityPredicates | [DataAbilityPredicates](js-apis-data-ability.md#dataabilitypredicates) | 是 | DataAbility谓词。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| rdb.[RdbPredicates](js-apis-data-rdb.md#rdbpredicates) | 返回RdbPredicates对象。 |

**示例：**

```
1. let dataAbilityPredicates = new dataAbility.DataAbilityPredicates()
2. dataAbilityPredicates.equalTo("NAME", "Rose")
3. // EMPLOYEE是使用关系型数据库创建的表。
4. let predicates = dataAbility.createRdbPredicates("EMPLOYEE", dataAbilityPredicates)
```

## DataAbilityPredicates

PhonePC/2in1TabletTVWearable

提供用于实现不同查询方法的谓词。

**初始化：**

```
1. let dataAbilityPredicates = new dataAbility.DataAbilityPredicates()
```

### equalTo

PhonePC/2in1TabletTVWearable

equalTo(field: string, value: ValueType): DataAbilityPredicates

配置谓词以匹配数据，数据的指定字段数据类型为ValueType且值等于指定值。

此方法类似于SQL语句的“=”。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |
| value | [ValueType](js-apis-data-ability.md#valuetype) | 是 | 指示要与谓词匹配的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataAbilityPredicates](js-apis-data-ability.md#dataabilitypredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. dataAbilityPredicates.equalTo("NAME", "lisi")
```

### notEqualTo

PhonePC/2in1TabletTVWearable

notEqualTo(field: string, value: ValueType): DataAbilityPredicates

配置谓词以匹配数据，数据的指定字段数据类型为ValueType且不等于指定值。

此方法类似于SQL语句的“!=”。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |
| value | [ValueType](js-apis-data-ability.md#valuetype) | 是 | 指示要与谓词匹配的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataAbilityPredicates](js-apis-data-ability.md#dataabilitypredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. dataAbilityPredicates.notEqualTo("NAME", "lisi")
```

### beginWrap

PhonePC/2in1TabletTVWearable

beginWrap(): DataAbilityPredicates

在谓词中添加左括号。此方法类似于SQL语句的“(”，需要与endWrap一起使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataAbilityPredicates](js-apis-data-ability.md#dataabilitypredicates) | 返回带有左括号的DataAbility谓词。 |

**示例：**

```
1. dataAbilityPredicates.equalTo("NAME", "lisi")
2. .beginWrap()
3. .equalTo("AGE", 18)
4. .or()
5. .equalTo("SALARY", 200.5)
6. .endWrap()
```

### endWrap

PhonePC/2in1TabletTVWearable

endWrap(): DataAbilityPredicates

在谓词中添加右括号。此方法类似于SQL语句的“)”，需要和beginWrap一起使用。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataAbilityPredicates](js-apis-data-ability.md#dataabilitypredicates) | 返回带有右括号的DataAbility谓词。 |

**示例：**

```
1. dataAbilityPredicates.equalTo("NAME", "lisi")
2. .beginWrap()
3. .equalTo("AGE", 18)
4. .or()
5. .equalTo("SALARY", 200.5)
6. .endWrap()
```

### or

PhonePC/2in1TabletTVWearable

or(): DataAbilityPredicates

将或条件添加到谓词中。

此方法类似于SQL语句“or”。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataAbilityPredicates](js-apis-data-ability.md#dataabilitypredicates) | 返回带有或条件的DataAbility谓词。 |

**示例：**

```
1. dataAbilityPredicates.equalTo("NAME", "Lisa")
2. .or()
3. .equalTo("NAME", "Rose")
```

### and

PhonePC/2in1TabletTVWearable

and(): DataAbilityPredicates

将和条件添加到谓词中。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataAbilityPredicates](js-apis-data-ability.md#dataabilitypredicates) | 返回带有和条件的DataAbility谓词。 |

**示例：**

```
1. dataAbilityPredicates.equalTo("NAME", "Lisa")
2. .and()
3. .equalTo("SALARY", 200.5)
```

### contains

PhonePC/2in1TabletTVWearable

contains(field: string, value: string): DataAbilityPredicates

配置谓词以匹配数据类型为string且value包含指定值的字段。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |
| value | string | 是 | 指示要与谓词匹配的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataAbilityPredicates](js-apis-data-ability.md#dataabilitypredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. dataAbilityPredicates.contains("NAME", "os")
```

### beginsWith

PhonePC/2in1TabletTVWearable

beginsWith(field: string, value: string): DataAbilityPredicates

配置谓词以匹配数据类型为string且值以指定字符串开头的字段。

此方法类似于SQL语句的“%”。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |
| value | string | 是 | 指示要与谓词匹配的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataAbilityPredicates](js-apis-data-ability.md#dataabilitypredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. dataAbilityPredicates.beginsWith("NAME", "os")
```

### endsWith

PhonePC/2in1TabletTVWearable

endsWith(field: string, value: string): DataAbilityPredicates

配置谓词以匹配数据类型为string且值以指定字符串结尾的字段。

此方法类似于SQL语句的“%”。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |
| value | string | 是 | 指示要与谓词匹配的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataAbilityPredicates](js-apis-data-ability.md#dataabilitypredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. dataAbilityPredicates.endsWith("NAME", "se")
```

### isNull

PhonePC/2in1TabletTVWearable

isNull(field: string): DataAbilityPredicates

配置谓词以匹配值为null的字段。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataAbilityPredicates](js-apis-data-ability.md#dataabilitypredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. dataAbilityPredicates.isNull("NAME")
```

### isNotNull

PhonePC/2in1TabletTVWearable

isNotNull(field: string): DataAbilityPredicates

配置谓词以匹配值不为null的指定字段。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataAbilityPredicates](js-apis-data-ability.md#dataabilitypredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. dataAbilityPredicates.isNotNull("NAME")
```

### like

PhonePC/2in1TabletTVWearable

like(field: string, value: string): DataAbilityPredicates

配置谓词以匹配数据类型为string且值类似于指定字符串的字段。

此方法类似于SQL语句“like”。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |
| value | string | 是 | 指示要与谓词匹配的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataAbilityPredicates](js-apis-data-ability.md#dataabilitypredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. dataAbilityPredicates.like("NAME", "%os%")
```

### glob

PhonePC/2in1TabletTVWearable

glob(field: string, value: string): DataAbilityPredicates

配置谓词以匹配数据类型为string的指定字段。与like方法不同，该方法的输入参数区分大小写。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |
| value | string | 是 | 指示要与谓词匹配的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataAbilityPredicates](js-apis-data-ability.md#dataabilitypredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. dataAbilityPredicates.glob("NAME", "?h*g")

3. // 仅可匹配到"name"字段值为“Lisa”
4. dataAbilityPredicates.glob("NAME", "Lisa")

6. // 仅可以匹配到"name"字段值为“lisa”
7. dataAbilityPredicates.glob("NAME", "lisa")
```

### between

PhonePC/2in1TabletTVWearable

between(field: string, low: ValueType, high: ValueType): DataAbilityPredicates

配置谓词以匹配数据类型为ValueType且value在指定范围内的指定字段。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |
| low | [ValueType](js-apis-data-ability.md#valuetype) | 是 | 指示与谓词匹配的最小值。 |
| high | [ValueType](js-apis-data-ability.md#valuetype) | 是 | 指示与谓词匹配的最大值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataAbilityPredicates](js-apis-data-ability.md#dataabilitypredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. dataAbilityPredicates.between("AGE", 10, 50)
```

### notBetween

PhonePC/2in1TabletTVWearable

notBetween(field: string, low: ValueType, high: ValueType): DataAbilityPredicates

配置谓词以匹配数据类型为ValueType且value超出给定范围的指定字段。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |
| low | [ValueType](js-apis-data-ability.md#valuetype) | 是 | 指示与谓词匹配的最小值。 |
| high | [ValueType](js-apis-data-ability.md#valuetype) | 是 | 指示与谓词匹配的最大值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataAbilityPredicates](js-apis-data-ability.md#dataabilitypredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. dataAbilityPredicates.notBetween("AGE", 10, 50)
```

### greaterThan

PhonePC/2in1TabletTVWearable

greaterThan(field: string, value: ValueType): DataAbilityPredicates

配置谓词以匹配数据类型为ValueType且值大于指定值的字段。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |
| value | [ValueType](js-apis-data-ability.md#valuetype) | 是 | 指示要与谓词匹配的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataAbilityPredicates](js-apis-data-ability.md#dataabilitypredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. dataAbilityPredicates.greaterThan("AGE", 18)
```

### lessThan

PhonePC/2in1TabletTVWearable

lessThan(field: string, value: ValueType): DataAbilityPredicates

配置谓词以匹配数据类型为valueType且value小于指定值的字段。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |
| value | [ValueType](js-apis-data-ability.md#valuetype) | 是 | 指示要与谓词匹配的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataAbilityPredicates](js-apis-data-ability.md#dataabilitypredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. dataAbilityPredicates.lessThan("AGE", 20)
```

### greaterThanOrEqualTo

PhonePC/2in1TabletTVWearable

greaterThanOrEqualTo(field: string, value: ValueType): DataAbilityPredicates

配置谓词以匹配数据类型为ValueType且value大于或等于指定值的字段。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |
| value | [ValueType](js-apis-data-ability.md#valuetype) | 是 | 指示要与谓词匹配的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataAbilityPredicates](js-apis-data-ability.md#dataabilitypredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. dataAbilityPredicates.greaterThanOrEqualTo("AGE", 18)
```

### lessThanOrEqualTo

PhonePC/2in1TabletTVWearable

lessThanOrEqualTo(field: string, value: ValueType): DataAbilityPredicates

配置谓词以匹配数据类型为ValueType且value小于或等于指定值的字段。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |
| value | [ValueType](js-apis-data-ability.md#valuetype) | 是 | 指示要与谓词匹配的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataAbilityPredicates](js-apis-data-ability.md#dataabilitypredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. dataAbilityPredicates.lessThanOrEqualTo("AGE", 20)
```

### orderByAsc

PhonePC/2in1TabletTVWearable

orderByAsc(field: string): DataAbilityPredicates

配置谓词以匹配其值按升序排序的列。当有多个orderByAsc使用时，最先使用的具有最高优先级。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataAbilityPredicates](js-apis-data-ability.md#dataabilitypredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. // 先按“name”字段排序，相同时按“AGE”字段排序，其次按“SALARY”排序
2. dataAbilityPredicates.orderByAsc("NAME").orderByAsc("AGE").orderByAsc("SALARY")
```

### orderByDesc

PhonePC/2in1TabletTVWearable

orderByDesc(field: string): DataAbilityPredicates

配置谓词以匹配其值按降序排序的列。当有多个orderByDesc使用时，最先使用的具有最高优先级。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataAbilityPredicates](js-apis-data-ability.md#dataabilitypredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. // 优先按“AGE”排序，相同时按“SALARY”排序
2. dataAbilityPredicates.orderByDesc("AGE").orderByDesc("SALARY")
```

### distinct

PhonePC/2in1TabletTVWearable

distinct(): DataAbilityPredicates

配置谓词以过滤重复记录并仅保留其中一个。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataAbilityPredicates](js-apis-data-ability.md#dataabilitypredicates) | 返回可用于过滤重复记录的谓词。 |

**示例：**

```
1. dataAbilityPredicates.equalTo("NAME", "Rose").distinct()
```

### limitAs

PhonePC/2in1TabletTVWearable

limitAs(value: number): DataAbilityPredicates

设置谓词的最大数据记录数量。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 最大数据记录数，取值为正整数。传入值小于等于0时，不会限制记录数量。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataAbilityPredicates](js-apis-data-ability.md#dataabilitypredicates) | 返回可用于设置最大数据记录数的谓词。 |

**示例：**

```
1. dataAbilityPredicates.equalTo("NAME", "Rose").limitAs(3)
```

### offsetAs

PhonePC/2in1TabletTVWearable

offsetAs(rowOffset: number): DataAbilityPredicates

设置谓词查询结果的起始位置。需要同步调用limitAs接口指定查询数量，否则无查询结果。查询指定偏移位置后的所有行时，limitAs接口需传入参数-1。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rowOffset | number | 是 | 返回结果的起始位置，取值为正整数。传入值小于等于0时，查询结果将从第一个元素位置返回。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataAbilityPredicates](js-apis-data-ability.md#dataabilitypredicates) | 返回具有指定返回结果起始位置的谓词。 |

**示例：**

```
1. // 跳过前三条数据，显示后续三条数据
2. dataAbilityPredicates.equalTo("NAME", "Rose").offsetAs(3).limitAs(3)
```

### groupBy

PhonePC/2in1TabletTVWearable

groupBy(fields: Array<string>): DataAbilityPredicates

配置谓词按指定列分组查询结果。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fields | Array<string> | 是 | 指定分组依赖的列名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataAbilityPredicates](js-apis-data-ability.md#dataabilitypredicates) | 返回分组查询列的谓词。 |

**示例：**

```
1. dataAbilityPredicates.groupBy(["AGE", "NAME"])
```

### indexedBy

PhonePC/2in1TabletTVWearable

indexedBy(field: string): DataAbilityPredicates

配置谓词以指定索引列。在使用此方法之前，您需要创建一个索引列。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 创建的索引列名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataAbilityPredicates](js-apis-data-ability.md#dataabilitypredicates) | 返回具有指定索引列的谓词。 |

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { dataAbility, relationalStore } from '@kit.ArkData';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export default class EntryAbility extends UIAbility {
6. async onCreate(): Promise<void> {
7. let store: relationalStore.RdbStore | undefined = undefined;
8. let context = this.context;

10. try {
11. const STORE_CONFIG: relationalStore.StoreConfig = {
12. name: 'RdbTest.db', // 数据库文件名
13. securityLevel: relationalStore.SecurityLevel.S3,
14. };
15. // 表结构：EMPLOYEE (NAME, AGE, SALARY, CODES)
16. const SQL_CREATE_TABLE =
17. 'CREATE TABLE IF NOT EXISTS EMPLOYEE (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT NOT NULL, AGE INTEGER, SALARY REAL, CODES BLOB)'; // 建表Sql语句
18. store = await relationalStore.getRdbStore(context, STORE_CONFIG);
19. console.info('Succeeded in getting RdbStore.');
20. await store.executeSql(SQL_CREATE_TABLE); // 创建数据表
21. } catch (e) {
22. const err = e as BusinessError;
23. console.error(`Failed to get RdbStore. Code:${err.code}, message:${err.message}`);
24. }

26. if (!store) {
27. return;
28. }

30. // 创建索引
31. const SQL_CREATE_INDEX = 'CREATE INDEX SALARY_INDEX ON EMPLOYEE(SALARY)'
32. await store.executeSql(SQL_CREATE_INDEX);
33. // ...

35. let dataAbilityPredicates = new dataAbility.DataAbilityPredicates()
36. dataAbilityPredicates.indexedBy("SALARY_INDEX")

38. //  ...
39. }
40. }
```

### in

PhonePC/2in1TabletTVWearable

in(field: string, value: Array<ValueType>): DataAbilityPredicates

配置谓词以匹配数据类型为ValueType数组且值在给定范围内的指定字段。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |
| value | Array<[ValueType](js-apis-data-ability.md#valuetype)> | 是 | 以ValueType类型数组形式指定的要匹配的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataAbilityPredicates](js-apis-data-ability.md#dataabilitypredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. dataAbilityPredicates.in("AGE", [18, 20])
```

### notIn

PhonePC/2in1TabletTVWearable

notIn(field: string, value: Array<ValueType>): DataAbilityPredicates

配置谓词以匹配数据类型为ValueType数组且值不在给定范围内的指定字段。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |
| value | Array<[ValueType](js-apis-data-ability.md#valuetype)> | 是 | 以ValueType类型数组形式指定的要匹配的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataAbilityPredicates](js-apis-data-ability.md#dataabilitypredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. dataAbilityPredicates.notIn("NAME", ["Lisa", "Rose"])
```

## ValueType

PhonePC/2in1TabletTVWearable

type ValueType = number | string | boolean

用于表示允许的数据字段类型。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

| 类型 | 说明 |
| --- | --- |
| number | 表示值类型为数字。 |
| string | 表示值类型为字符。 |
| boolean | 表示值类型为布尔值。 |
