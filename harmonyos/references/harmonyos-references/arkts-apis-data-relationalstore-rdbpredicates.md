---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-data-relationalstore-rdbpredicates
title: Class (RdbPredicates)
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > ArkTS API > @ohos.data.relationalStore (关系型数据库) > Class (RdbPredicates)
category: harmonyos-references
scraped_at: 2026-04-28T07:59:18+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:ff417764490d40b367ff62dca952cb897c566ccee347e503476b672a4db74986
---

表示关系型数据库（RDB）的谓词。该类确定RDB中条件表达式的值是true还是false。谓词间支持多语句拼接，拼接时默认使用and()连接。不支持Sendable跨线程传递。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { relationalStore } from '@kit.ArkData';
```

## constructor

PhonePC/2in1TabletTVWearable

constructor(name: string)

构造函数。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 数据库表名。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
```

## inDevices

PhonePC/2in1TabletTVWearable

inDevices(devices: Array<string>): RdbPredicates

同步分布式数据库时连接到组网内指定的远程设备。

说明

其中devices通过调用[deviceManager.getAvailableDeviceListSync](js-apis-distributeddevicemanager.md#getavailabledevicelistsync)方法得到。

数据库同步时调用Sync接口，需要在入参谓词中调用inDevices接口选择设备。如果不调用inDevices接口即默认连接组网内所有的设备。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| devices | Array<string> | 是 | 指定的组网内的远程设备ID。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 返回与指定字段匹配的谓词。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { distributedDeviceManager } from '@kit.DistributedServiceKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let dmInstance: distributedDeviceManager.DeviceManager;
5. let deviceIds: Array<string> = [];

7. try {
8. dmInstance = distributedDeviceManager.createDeviceManager("com.example.appdatamgrverify");
9. let devices: Array<distributedDeviceManager.DeviceBasicInfo> = dmInstance.getAvailableDeviceListSync();
10. for (let i = 0; i < devices.length; i++) {
11. deviceIds[i] = devices[i].networkId!;
12. }
13. } catch (err) {
14. let code = (err as BusinessError).code;
15. let message = (err as BusinessError).message;
16. console.error("createDeviceManager errCode:" + code + ",errMessage:" + message);
17. }

19. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
20. predicates.inDevices(deviceIds);
```

## inAllDevices

PhonePC/2in1TabletTVWearable

inAllDevices(): RdbPredicates

同步分布式数据库时连接到组网内所有的远程设备。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 返回与指定字段匹配的谓词。 |

**示例：**

```
1. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
2. predicates.inAllDevices();
```

## equalTo

PhonePC/2in1TabletTVWearable

equalTo(field: string, value: ValueType): RdbPredicates

配置谓词以匹配数据表的field列中值为value的字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |
| value | [ValueType](arkts-apis-data-relationalstore-t.md#valuetype) | 是 | 指示要与谓词匹配的值。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 返回与指定字段匹配的谓词。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // 匹配数据表的"NAME"列中值为"Lisa"的字段
2. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
3. predicates.equalTo("NAME", "Lisa");
```

## notEqualTo

PhonePC/2in1TabletTVWearable

notEqualTo(field: string, value: ValueType): RdbPredicates

配置谓词以匹配数据表的field列中值不为value的字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |
| value | [ValueType](arkts-apis-data-relationalstore-t.md#valuetype) | 是 | 指示要与谓词匹配的值。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 返回与指定字段匹配的谓词。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // 匹配数据表的"NAME"列中值不为"Lisa"的字段
2. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
3. predicates.notEqualTo("NAME", "Lisa");
```

## beginWrap

PhonePC/2in1TabletTVWearable

beginWrap(): RdbPredicates

向谓词添加左括号。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 返回带有左括号的Rdb谓词。 |

**示例：**

```
1. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
2. predicates.equalTo("NAME", "Lisa")
3. .beginWrap()
4. .equalTo("AGE", 18)
5. .or()
6. .equalTo("SALARY", 200.5)
7. .endWrap();
```

## endWrap

PhonePC/2in1TabletTVWearable

endWrap(): RdbPredicates

向谓词添加右括号。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 返回带有右括号的Rdb谓词。 |

**示例：**

```
1. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
2. predicates.equalTo("NAME", "Lisa")
3. .beginWrap()
4. .equalTo("AGE", 18)
5. .or()
6. .equalTo("SALARY", 200.5)
7. .endWrap();
```

## or

PhonePC/2in1TabletTVWearable

or(): RdbPredicates

将或条件添加到谓词中。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 返回带有或条件的Rdb谓词。 |

**示例：**

```
1. // 匹配数据表的"NAME"列中值为"Lisa"或"Rose"的字段
2. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
3. predicates.equalTo("NAME", "Lisa")
4. .or()
5. .equalTo("NAME", "Rose");
```

## and

PhonePC/2in1TabletTVWearable

and(): RdbPredicates

向谓词添加和条件。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 返回带有和条件的Rdb谓词。 |

**示例：**

```
1. // 匹配数据表的"NAME"列中值为"Lisa"且"SALARY"列中值为"200.5"的字段
2. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
3. predicates.equalTo("NAME", "Lisa")
4. .and()
5. .equalTo("SALARY", 200.5);
```

## contains

PhonePC/2in1TabletTVWearable

contains(field: string, value: string): RdbPredicates

配置谓词以匹配数据表的field列中包含value的字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |
| value | string | 是 | 指示要与谓词匹配的值。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 返回与指定字段匹配的谓词。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // 匹配数据表的"NAME"列中包含"os"的字段，如"Rose"
2. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
3. predicates.contains("NAME", "os");
```

## beginsWith

PhonePC/2in1TabletTVWearable

beginsWith(field: string, value: string): RdbPredicates

配置谓词以匹配数据表的field列中以value开头的字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |
| value | string | 是 | 指示要与谓词匹配的值。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 返回与指定字段匹配的谓词。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // 匹配数据表的"NAME"列中以"Li"开头的字段，如"Lisa"
2. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
3. predicates.beginsWith("NAME", "Li");
```

## endsWith

PhonePC/2in1TabletTVWearable

endsWith(field: string, value: string): RdbPredicates

配置谓词以匹配数据表的field列中以value结尾的字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |
| value | string | 是 | 指示要与谓词匹配的值。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 返回与指定字段匹配的谓词。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // 匹配数据表的"NAME"列中以"se"结尾的字段，如"Rose"
2. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
3. predicates.endsWith("NAME", "se");
```

## isNull

PhonePC/2in1TabletTVWearable

isNull(field: string): RdbPredicates

配置谓词以匹配数据表的field列中值为null的字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 返回与指定字段匹配的谓词。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```
1. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
2. predicates.isNull("NAME");
```

## isNotNull

PhonePC/2in1TabletTVWearable

isNotNull(field: string): RdbPredicates

配置谓词以匹配数据表的field列中值不为null的字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 返回与指定字段匹配的谓词。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
2. predicates.isNotNull("NAME");
```

## like

PhonePC/2in1TabletTVWearable

like(field: string, value: string): RdbPredicates

配置模糊查询条件，指定field列的模糊匹配条件。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |
| value | string | 是 | 指定模糊匹配条件，通常配合通配符使用，%表示任意长度任意字符，\_表示单个字符。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 返回与指定字段匹配的谓词。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // 查询NAME列中包含"os"子串的数据，例如会匹配"Rose"。
2. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
3. predicates.like("NAME", "%os%");
```

## glob

PhonePC/2in1TabletTVWearable

glob(field: string, value: string): RdbPredicates

配置谓词匹配数据字段为string的指定字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |
| value | string | 是 | 指示要与谓词匹配的值。  支持通配符，\*表示0个、1个或多个数字或字符，?表示1个数字或字符。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 返回与指定字段匹配的谓词。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // 匹配数据表的"NAME"列中类型为string且值为"?h*g"的字段
2. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
3. predicates.glob("NAME", "?h*g");
```

## between

PhonePC/2in1TabletTVWearable

between(field: string, low: ValueType, high: ValueType): RdbPredicates

配置谓词以匹配数据表的field列中值在给定范围内的字段（包含范围边界）。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |
| low | [ValueType](arkts-apis-data-relationalstore-t.md#valuetype) | 是 | 指示与谓词匹配的最小值。 |
| high | [ValueType](arkts-apis-data-relationalstore-t.md#valuetype) | 是 | 指示与谓词匹配的最大值。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 返回与指定字段匹配的谓词。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // 匹配数据表的"AGE"列中大于等于10且小于等于50的值
2. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
3. predicates.between("AGE", 10, 50);
```

## notBetween

PhonePC/2in1TabletTVWearable

notBetween(field: string, low: ValueType, high: ValueType): RdbPredicates

配置谓词以匹配数据表的field列中值超出给定范围的字段（不包含范围边界）。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |
| low | [ValueType](arkts-apis-data-relationalstore-t.md#valuetype) | 是 | 指示与谓词匹配的最小值。 |
| high | [ValueType](arkts-apis-data-relationalstore-t.md#valuetype) | 是 | 指示要与谓词匹配的最大值。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 返回与指定字段匹配的谓词。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // 匹配数据表的"AGE"列中小于10或大于50的值
2. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
3. predicates.notBetween("AGE", 10, 50);
```

## greaterThan

PhonePC/2in1TabletTVWearable

greaterThan(field: string, value: ValueType): RdbPredicates

配置谓词以匹配数据表的field列中值大于value的字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |
| value | [ValueType](arkts-apis-data-relationalstore-t.md#valuetype) | 是 | 指示要与谓词匹配的值。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 返回与指定字段匹配的谓词。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // 匹配数据表的"AGE"列中大于18的值
2. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
3. predicates.greaterThan("AGE", 18);
```

## lessThan

PhonePC/2in1TabletTVWearable

lessThan(field: string, value: ValueType): RdbPredicates

配置谓词以匹配数据表的field列中值小于value的字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |
| value | [ValueType](arkts-apis-data-relationalstore-t.md#valuetype) | 是 | 指示要与谓词匹配的值。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 返回与指定字段匹配的谓词。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // 匹配数据表的"AGE"列中小于20的值
2. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
3. predicates.lessThan("AGE", 20);
```

## greaterThanOrEqualTo

PhonePC/2in1TabletTVWearable

greaterThanOrEqualTo(field: string, value: ValueType): RdbPredicates

配置谓词以匹配数据表的field列中值大于或者等于value的字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |
| value | [ValueType](arkts-apis-data-relationalstore-t.md#valuetype) | 是 | 指示要与谓词匹配的值。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 返回与指定字段匹配的谓词。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // 匹配数据表的"AGE"列中大于等于18的值
2. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
3. predicates.greaterThanOrEqualTo("AGE", 18);
```

## lessThanOrEqualTo

PhonePC/2in1TabletTVWearable

lessThanOrEqualTo(field: string, value: ValueType): RdbPredicates

配置谓词以匹配数据表的field列中值小于或者等于value的字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |
| value | [ValueType](arkts-apis-data-relationalstore-t.md#valuetype) | 是 | 指示要与谓词匹配的值。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 返回与指定字段匹配的谓词。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // 匹配数据表的"AGE"列中小于等于20的值
2. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
3. predicates.lessThanOrEqualTo("AGE", 20);
```

## orderByAsc

PhonePC/2in1TabletTVWearable

orderByAsc(field: string): RdbPredicates

配置谓词以匹配数据表的field列中值按升序排序的列。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 返回与指定字段匹配的谓词。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
2. predicates.orderByAsc("NAME");
```

## orderByDesc

PhonePC/2in1TabletTVWearable

orderByDesc(field: string): RdbPredicates

配置谓词以匹配数据表的field列中值按降序排序的列。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 返回与指定字段匹配的谓词。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
2. predicates.orderByDesc("AGE");
```

## distinct

PhonePC/2in1TabletTVWearable

distinct(): RdbPredicates

配置谓词以过滤重复记录并仅保留其中一个。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 返回可用于过滤重复记录的谓词。 |

**示例：**

```
1. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
2. predicates.equalTo("NAME", "Rose").distinct(); // 对NAME列值为Rose的结果集去重
```

## limitAs

PhonePC/2in1TabletTVWearable

limitAs(value: number): RdbPredicates

设置谓词的最大数据记录数量。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 最大数据记录数，取值应为正整数，传入值小于等于0时，不会限制记录数量。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 返回可用于设置最大数据记录数的谓词。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
2. predicates.equalTo("NAME", "Rose").limitAs(3);
```

## offsetAs

PhonePC/2in1TabletTVWearable

offsetAs(rowOffset: number): RdbPredicates

设置谓词查询结果返回的起始位置。需要同步调用limitAs接口指定查询数量，否则将无查询结果。如需查询指定偏移位置后的所有行，limitAs接口入参需小于等于0。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rowOffset | number | 是 | 指定查询结果的起始位置，默认初始位置为结果集的最前端。当rowOffset为负数时，起始位置为结果集的最前端。当rowOffset超出结果集最后位置时，查询结果为空。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 返回具有指定返回结果起始位置的谓词。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
2. predicates.equalTo("NAME", "Rose").limitAs(-1).offsetAs(3);
```

## groupBy

PhonePC/2in1TabletTVWearable

groupBy(fields: Array<string>): RdbPredicates

配置谓词按指定列分组查询结果。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fields | Array<string> | 是 | 指定分组依赖的列名。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 返回分组查询列的谓词。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
2. predicates.groupBy(["AGE", "NAME"]);
```

## indexedBy

PhonePC/2in1TabletTVWearable

indexedBy(field: string): RdbPredicates

配置谓词以指定索引列。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 索引列的名称。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 返回具有指定索引列的RdbPredicates。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
2. predicates.indexedBy("SALARY");
```

## in

PhonePC/2in1TabletTVWearable

in(field: string, value: Array<ValueType>): RdbPredicates

配置谓词条件，表示字段field的值必须在给定的value集合内。

说明

value集合不能为空。如果传入空集，此条件将失效，导致操作针对所有数据（如全量查询、更新或删除）。请在调用前判断value是否为空集，避免误操作。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |
| value | Array<[ValueType](arkts-apis-data-relationalstore-t.md#valuetype)> | 是 | 以ValueType型数组形式指定的要匹配的值。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 返回与指定字段匹配的谓词。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // 匹配数据表的"AGE"列中在[18，20]中的值
2. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
3. predicates.in("AGE", [18, 20]);
```

## notIn

PhonePC/2in1TabletTVWearable

notIn(field: string, value: Array<ValueType>): RdbPredicates

将谓词配置为匹配数据字段为ValueType且值超出给定范围的指定字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |
| value | Array<[ValueType](arkts-apis-data-relationalstore-t.md#valuetype)> | 是 | 以ValueType数组形式指定的要匹配的值。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 返回与指定字段匹配的谓词。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // 匹配数据表的"NAME"列中不在["Lisa", "Rose"]中的值
2. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
3. predicates.notIn("NAME", ["Lisa", "Rose"]);
```

## notContains12+

PhonePC/2in1TabletTVWearable

notContains(field: string, value: string): RdbPredicates

配置谓词以匹配数据表的field列中不包含value的字段。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |
| value | string | 是 | 指示要与谓词匹配的值。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 返回与指定字段匹配的谓词。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // 匹配数据表的"NAME"列中不包含"os"的字段，如列表中的"Lisa"
2. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
3. predicates.notContains("NAME", "os");
```

## notLike12+

PhonePC/2in1TabletTVWearable

notLike(field: string, value: string): RdbPredicates

配置模糊查询条件，指定field列**不包含**的模糊匹配条件。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 数据库表中的列名。 |
| value | string | 是 | 指定**不包含**的模糊匹配条件，通常配合通配符使用，%表示任意长度任意字符，\_表示单个字符。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 返回与指定字段匹配的谓词。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // 查询NAME列中不包含"os"子串的数据，例如不会匹配"Rose"。
2. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
3. predicates.notLike("NAME", "%os%");
```

## having20+

PhonePC/2in1TabletTVWearable

having(conditions:string, args?: Array<ValueType>): RdbPredicates

筛选符合条件的分组数据。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| conditions | string | 是 | 用于过滤使用[groupBy](arkts-apis-data-relationalstore-rdbpredicates.md#groupby)获得的数据，不能为空且必须与[groupBy](arkts-apis-data-relationalstore-rdbpredicates.md#groupby)配合使用。 |
| args | Array<[ValueType](arkts-apis-data-relationalstore-t.md#valuetype)> | 否 | 条件中使用的参数，用来替换条件语句中的占位符，不传时默认为空数组。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [RdbPredicates](arkts-apis-data-relationalstore-rdbpredicates.md) | 返回与指定字段匹配的谓词。 |

**错误码：**

以下错误码的详细介绍请参见[关系型数据库错误码](errorcode-data-rdb.md)。

| **错误码ID** | **错误信息** |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1. Parameter is out of valid range; 2. Missing GROUP BY clause. |

**示例1：**

```
1. // 传递完整的条件
2. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
3. predicates.groupBy(["AGE"]);
4. predicates.having("NAME = zhangsan");
```

**示例2：**

```
1. // 条件中使用占位符替代，args参数传入替换占位符的值
2. let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
3. predicates.groupBy(["AGE"]);
4. predicates.having("NAME = ?", ["zhangsan"]);
```
