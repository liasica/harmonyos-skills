---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-datasharepredicates
title: @ohos.data.dataSharePredicates (数据共享谓词)
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > ArkTS API > @ohos.data.dataSharePredicates (数据共享谓词)
category: harmonyos-references
scraped_at: 2026-04-28T07:59:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:907934c04dc788abc114066ebf4d99cdc8b74b6f63b427176287d1335616b9cf
---

**谓词(DataSharePredicates)** 是开发者通过DataShare查询数据库中的数据所使用的筛选条件，经常被应用在更新数据、删除数据和查询数据中。

谓词的接口函数与数据库的筛选条件一一对应，开发者在使用前需了解数据库相关知识。

谓词(DataSharePredicates)的使用场景如下：

* 用于在媒体文件管理服务作为检索条件使用，参考相册管理模块检索条件[FetchOptions](arkts-apis-photoaccesshelper-i.md#fetchoptions)。此种场景下，开发者无需关注数据库类型。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { dataSharePredicates } from '@kit.ArkData';
```

## DataSharePredicates

PhonePC/2in1TabletTVWearable

提供用于不同实现不同查询方法的数据共享谓词。该类型不是多线程安全的，如果应用中存在多线程同时操作该类派生出的实例，注意加锁保护。

### equalTo10+

PhonePC/2in1TabletTVWearable

equalTo(field: string, value: ValueType): DataSharePredicates

该接口用于配置谓词以匹配值等于指定值的字段。

目前仅关系型数据库及键值型数据库支持该谓词。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。  field为undefined或者null时，此次调用接口配置的谓词无效。 |
| value | [ValueType](js-apis-data-valuesbucket.md#valuetype) | 是 | 指示要与谓词匹配的值。  value为undefined或者null时，此次调用接口配置的谓词无效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataSharePredicates](js-apis-data-datasharepredicates.md#datasharepredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. let predicates = new dataSharePredicates.DataSharePredicates();
2. predicates.equalTo("NAME", "Rose");
```

### and10+

PhonePC/2in1TabletTVWearable

and(): DataSharePredicates

该接口用于将和条件添加到谓词中。

目前仅关系型数据库及键值型数据库支持该谓词。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataSharePredicates](js-apis-data-datasharepredicates.md#datasharepredicates) | 返回带有和条件的谓词。 |

**示例：**

```
1. let predicates = new dataSharePredicates.DataSharePredicates();
2. predicates.equalTo("NAME", "lisi")
3. .and()
4. .equalTo("SALARY", 200.5);
```

### orderByAsc10+

PhonePC/2in1TabletTVWearable

orderByAsc(field: string): DataSharePredicates

该接口用于配置谓词以匹配其值按升序排序的列。

目前仅关系型数据库及键值型数据库支持该谓词。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。  field为undefined或者null时，此次调用接口配置的谓词无效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataSharePredicates](js-apis-data-datasharepredicates.md#datasharepredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. let predicates = new dataSharePredicates.DataSharePredicates();
2. predicates.orderByAsc("AGE");
```

### orderByDesc10+

PhonePC/2in1TabletTVWearable

orderByDesc(field: string): DataSharePredicates

该接口用于配置谓词以匹配其值按降序排序的列。

目前仅关系型数据库及键值型数据库支持该谓词。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。  field为undefined或者null时，此次调用接口配置的谓词无效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataSharePredicates](js-apis-data-datasharepredicates.md#datasharepredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. let predicates = new dataSharePredicates.DataSharePredicates();
2. predicates.orderByDesc("AGE");
```

### limit10+

PhonePC/2in1TabletTVWearable

limit(total: number, offset: number): DataSharePredicates

该接口用于配置谓词以指定结果数和起始位置。

目前仅关系型数据库及键值型数据库支持该谓词。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| total | number | 是 | 最大数据记录数。  当使用键值型数据库且total为undefined或null时，会限制最大记录数为0。  当使用关系型数据库且total为undefined或null时，不会限制最大记录数。  当使用键值型数据库时，取值范围参考[键值型数据库limit接口](js-apis-distributedkvstore.md#limit)中的total参数说明。  当使用关系型数据库时，取值范围参考[关系型数据库limitAs接口](arkts-apis-data-relationalstore-rdbpredicates.md#limitas)中的value参数说明。 |
| offset | number | 是 | 指定查询结果的起始位置。  当offset为undefined或null时，起始位置为结果集的最前端。  当使用键值型数据库时，取值范围参考[键值型数据库limit接口](js-apis-distributedkvstore.md#limit)中的offset参数说明。  当使用关系型数据库时，取值范围参考[关系型数据库offsetAs接口](arkts-apis-data-relationalstore-rdbpredicates.md#offsetas)中的rowOffset参数说明。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataSharePredicates](js-apis-data-datasharepredicates.md#datasharepredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. let predicates = new dataSharePredicates.DataSharePredicates();
2. predicates.equalTo("NAME", "Rose").limit(10, 3);
```

### in10+

PhonePC/2in1TabletTVWearable

in(field: string, value: Array<ValueType>): DataSharePredicates

该接口用于配置谓词以匹配值在指定范围内的字段。

目前仅关系型数据库及键值型数据库支持该谓词。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。  field为undefined或者null时，此次调用接口配置的谓词无效。 |
| value | Array<[ValueType](js-apis-data-valuesbucket.md#valuetype)> | 是 | 以ValueType型数组形式指定的要匹配的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataSharePredicates](js-apis-data-datasharepredicates.md#datasharepredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. let predicates = new dataSharePredicates.DataSharePredicates();
2. predicates.in("AGE", [18, 20]);
```

### notEqualTo23+

PhonePC/2in1TabletTVWearable

notEqualTo(field: string, value: ValueType): DataSharePredicates

该接口用于配置谓词以匹配值不等于指定值的字段。

目前仅关系型数据库及键值型数据库支持该谓词。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。  当field为undefined或null时，此次调用接口配置的谓词无效。  当field为字符串'null'或'undefined'时，键值型数据库和关系型数据库接口使用该谓词时，可能匹配结果非预期或抛出异常。 |
| value | [ValueType](js-apis-data-valuesbucket.md#valuetype) | 是 | 指示要与谓词匹配的值。  value为undefined或null时，此次调用接口配置的谓词无效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataSharePredicates](js-apis-data-datasharepredicates.md#datasharepredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. let predicates = new dataSharePredicates.DataSharePredicates();
2. predicates.notEqualTo("NAME", "Rose");
```

### beginWrap23+

PhonePC/2in1TabletTVWearable

beginWrap(): DataSharePredicates

该接口用于向谓词添加左括号，相当于sql语句的“(”，必须和右括号一起使用。

目前仅关系型数据库支持该谓词。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataSharePredicates](js-apis-data-datasharepredicates.md#datasharepredicates) | 返回带有左括号的谓词。 |

**示例：**

```
1. let predicates = new dataSharePredicates.DataSharePredicates();
2. predicates.equalTo("NAME", "lisi")
3. .beginWrap()
4. .equalTo("AGE", 18)
5. .or()
6. .equalTo("SALARY", 200.5)
7. .endWrap();
```

### endWrap23+

PhonePC/2in1TabletTVWearable

endWrap(): DataSharePredicates

该接口用于向谓词添加右括号，相当于sql语句的“)”，必须和左括号一起使用。

目前仅关系型数据库支持该谓词。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataSharePredicates](js-apis-data-datasharepredicates.md#datasharepredicates) | 返回带有右括号的谓词。 |

**示例：**

```
1. let predicates = new dataSharePredicates.DataSharePredicates();
2. predicates.equalTo("NAME", "lisi")
3. .beginWrap()
4. .equalTo("AGE", 18)
5. .or()
6. .equalTo("SALARY", 200.5)
7. .endWrap();
```

### or23+

PhonePC/2in1TabletTVWearable

or(): DataSharePredicates

该接口用于将或条件添加到谓词中。

目前仅关系型数据库及键值型数据库支持该谓词。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataSharePredicates](js-apis-data-datasharepredicates.md#datasharepredicates) | 返回带有或条件的谓词。 |

**示例：**

```
1. let predicates = new dataSharePredicates.DataSharePredicates()
2. predicates.equalTo("NAME", "lisi")
3. .or()
4. .equalTo("NAME", "Rose");
```

### like23+

PhonePC/2in1TabletTVWearable

like(field: string, value: string): DataSharePredicates

该接口用于配置谓词以匹配指定通配符表达式的字段。

目前仅关系型数据库及键值型数据库支持该谓词。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。  field为undefined或null时，此次调用接口配置的谓词无效。  当field为字符串'null'或'undefined'时，键值型数据库和关系型数据库接口使用该谓词时，可能匹配结果非预期或抛出异常。 |
| value | string | 是 | 指示要与谓词匹配的通配符表达式。  表达式中'%'代表零个、一个或多个数字或字符，'\_'代表一个单一的数字或字符，不区分大小写。  value为undefined或null时，此次调用接口配置的谓词无效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataSharePredicates](js-apis-data-datasharepredicates.md#datasharepredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. let predicates = new dataSharePredicates.DataSharePredicates();
2. predicates.like("NAME", "%os%");
```

### between23+

PhonePC/2in1TabletTVWearable

between(field: string, low: ValueType, high: ValueType): DataSharePredicates

该接口用于配置谓词以匹配值在指定范围内的字段。包含两端边界值，为左闭右闭区间。

目前仅关系型数据库支持该谓词。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。  field为undefined或null时，此次调用接口配置的谓词无效。  当field为字符串'null'或'undefined'时，键值型数据库和关系型数据库接口使用该谓词时，可能匹配结果非预期或抛出异常。 |
| low | [ValueType](js-apis-data-valuesbucket.md#valuetype) | 是 | 指示与谓词匹配的最小值。  low为number时，按数值排序指定匹配范围。  low为string时，按字典序排序指定匹配范围。  low为boolean时，按数值排序指定匹配范围。 |
| high | [ValueType](js-apis-data-valuesbucket.md#valuetype) | 是 | 指示与谓词匹配的最大值。  high为number时，按数值排序指定匹配范围。  high为string时，按字典序排序指定匹配范围。  high为boolean时，按数值排序指定匹配范围。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataSharePredicates](js-apis-data-datasharepredicates.md#datasharepredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. let predicates = new dataSharePredicates.DataSharePredicates();
2. predicates.between("AGE", 10, 50);
```

### notBetween23+

PhonePC/2in1TabletTVWearable

notBetween(field: string, low: ValueType, high: ValueType): DataSharePredicates

该接口用于配置谓词以匹配值超出指定范围的字段。不包含两端边界值，为左开右开区间。

目前仅关系型数据库支持该谓词。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。  field为undefined或null时，此次调用接口配置的谓词无效。  当field为字符串'null'或'undefined'时，键值型数据库和关系型数据库接口使用该谓词时，可能匹配结果非预期或抛出异常。 |
| low | [ValueType](js-apis-data-valuesbucket.md#valuetype) | 是 | 指示与谓词匹配的最小值。  low为number时，按数值排序指定匹配范围。  low为string时，按字典序排序指定匹配范围。  low为boolean时，按数值排序指定匹配范围。 |
| high | [ValueType](js-apis-data-valuesbucket.md#valuetype) | 是 | 指示与谓词匹配的最大值。  high为number时，按数值排序指定匹配范围。  high为string时，按字典序排序指定匹配范围。  high为boolean时，按数值排序指定匹配范围。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataSharePredicates](js-apis-data-datasharepredicates.md#datasharepredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. let predicates = new dataSharePredicates.DataSharePredicates();
2. predicates.notBetween("AGE", 10, 50);
```

### greaterThan23+

PhonePC/2in1TabletTVWearable

greaterThan(field: string, value: ValueType): DataSharePredicates

该接口用于配置谓词以匹配值大于指定值的字段。

目前仅关系型数据库及键值型数据库支持该谓词。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。  field为undefined或null时，此次调用接口配置的谓词无效。  当field为字符串'null'或'undefined'时，键值型数据库和关系型数据库接口使用该谓词时，可能匹配结果非预期或抛出异常。 |
| value | [ValueType](js-apis-data-valuesbucket.md#valuetype) | 是 | 指示要与谓词匹配的值。  value为undefined或null时，此次调用接口配置的谓词无效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataSharePredicates](js-apis-data-datasharepredicates.md#datasharepredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. let predicates = new dataSharePredicates.DataSharePredicates();
2. predicates.greaterThan("AGE", 10);
```

### lessThan23+

PhonePC/2in1TabletTVWearable

lessThan(field: string, value: ValueType): DataSharePredicates

该接口用于配置谓词以匹配值小于指定值的字段。

目前仅关系型数据库及键值型数据库支持该谓词。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。  当field为null或undefined时，此次调用接口配置的谓词无效。  当field为字符串'null'或'undefined'时，键值型数据库和关系型数据库接口使用该谓词时，可能匹配结果非预期或抛出异常。 |
| value | [ValueType](js-apis-data-valuesbucket.md#valuetype) | 是 | 指示要与谓词匹配的值。  value为undefined或null时，此次调用接口配置的谓词无效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataSharePredicates](js-apis-data-datasharepredicates.md#datasharepredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. let predicates = new dataSharePredicates.DataSharePredicates();
2. predicates.lessThan("AGE", 50);
```

### greaterThanOrEqualTo23+

PhonePC/2in1TabletTVWearable

greaterThanOrEqualTo(field: string, value: ValueType): DataSharePredicates

该接口用于配置谓词以匹配值大于或等于指定值的字段。

目前仅关系型数据库及键值型数据库支持该谓词。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。  field为undefined或null时，此次调用接口配置的谓词无效。  当field为字符串'null'或'undefined'时，此次调用接口配置的谓词匹配结果非预期或抛出异常。 |
| value | [ValueType](js-apis-data-valuesbucket.md#valuetype) | 是 | 指示要与谓词匹配的值。  value为undefined或null时，此次调用接口配置的谓词无效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataSharePredicates](js-apis-data-datasharepredicates.md#datasharepredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. let predicates = new dataSharePredicates.DataSharePredicates();
2. predicates.greaterThanOrEqualTo("AGE", 10);
```

### lessThanOrEqualTo23+

PhonePC/2in1TabletTVWearable

lessThanOrEqualTo(field: string, value: ValueType): DataSharePredicates

该接口用于配置谓词以匹配值小于或等于指定值的字段。

目前仅关系型数据库及键值型数据库支持该谓词。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。  field为undefined或null时，此次调用接口配置的谓词无效。  当field为字符串'null'或'undefined'时，键值型数据库和关系型数据库接口使用该谓词时，可能匹配结果非预期或抛出异常。 |
| value | [ValueType](js-apis-data-valuesbucket.md#valuetype) | 是 | 指示要与谓词匹配的值。  value为undefined或null时，此次调用接口配置的谓词无效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataSharePredicates](js-apis-data-datasharepredicates.md#datasharepredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. let predicates = new dataSharePredicates.DataSharePredicates();
2. predicates.lessThanOrEqualTo("AGE", 50);
```

### notIn23+

PhonePC/2in1TabletTVWearable

notIn(field: string, value: Array<ValueType>): DataSharePredicates

该接口用于配置谓词以匹配值不在指定范围内的字段。

目前仅关系型数据库及键值型数据库支持该谓词。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。  field为undefined或null时，此次调用接口配置的谓词无效。  当field为字符串'null'或'undefined'时，键值型数据库和关系型数据库接口使用该谓词时，可能匹配结果非预期或抛出异常。 |
| value | Array<[ValueType](js-apis-data-valuesbucket.md#valuetype)> | 是 | 以ValueType型数组形式指定的要匹配的值。  value为undefined或null时，此次调用接口配置的谓词无效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataSharePredicates](js-apis-data-datasharepredicates.md#datasharepredicates) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. let predicates = new dataSharePredicates.DataSharePredicates();
2. predicates.notIn("NAME", ["Lisa", "Rose"]);
```
