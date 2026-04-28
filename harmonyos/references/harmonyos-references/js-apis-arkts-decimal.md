---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkts-decimal
title: @arkts.math.Decimal (高精度数学库Decimal)
breadcrumb: API参考 > 应用框架 > ArkTS（方舟编程语言） > ArkTS API > @arkts.math.Decimal (高精度数学库Decimal)
category: harmonyos-references
scraped_at: 2026-04-28T07:59:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:74a2d2054440f11afaed749d963c4eccdc2e12797e137678adf816c357181a9b
---

Decimal用于提供高精度数学运算的能力，支持高精度浮点计算。

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

此模块仅支持在ArkTS文件（文件后缀为.ets）中导入使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { Decimal } from '@kit.ArkTS';
```

## Value

PhonePC/2in1TabletTVWearable

type Value = string | number | Decimal

表示用于构建Decimal的参数类型。

取值类型为下列类型中的并集。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

| 类型 | 说明 |
| --- | --- |
| string | 表示值类型为字符串，可取任意值。 |
| number | 表示值类型为数字，可取任意值。 |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 表示值类型为Decimal类型。 |

## Rounding

PhonePC/2in1TabletTVWearable

type Rounding = 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8

表示可设置的舍入类型。

取值类型为下列类型中的并集。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

| 类型 | 说明 |
| --- | --- |
| 0 | 向远离零的方向舍入。与[Decimal.ROUND\_UP](js-apis-arkts-decimal.md#常量)一致。 |
| 1 | 向靠近零的方向舍入。与[Decimal.ROUND\_DOWN](js-apis-arkts-decimal.md#常量)一致。 |
| 2 | 向正无穷方向舍入。与[Decimal.ROUND\_CEILING](js-apis-arkts-decimal.md#常量)一致。 |
| 3 | 向负无穷方向舍入。与[Decimal.ROUND\_FLOOR](js-apis-arkts-decimal.md#常量)一致。 |
| 4 | 向最近的邻值舍入。如果距离相等，则远离零方向舍入。与[Decimal.ROUND\_HALF\_UP](js-apis-arkts-decimal.md#常量)一致。 |
| 5 | 向最近的邻值舍入。如果距离相等，则靠近零方向舍入。与[Decimal.ROUND\_HALF\_DOWN](js-apis-arkts-decimal.md#常量)一致。 |
| 6 | 向最近的邻值舍入。如果距离相等，则向偶数邻值舍入。与[Decimal.ROUND\_HALF\_EVEN](js-apis-arkts-decimal.md#常量)一致。 |
| 7 | 向最近的邻值舍入。如果距离相等，则向正无穷方向舍入。与[Decimal.ROUND\_HALF\_CEILING](js-apis-arkts-decimal.md#常量)一致。 |
| 8 | 向最近的邻值舍入。如果距离相等，则向负无穷方向舍入。与[Decimal.ROUND\_HALF\_FLOOR](js-apis-arkts-decimal.md#常量)一致。 |

## Modulo

PhonePC/2in1TabletTVWearable

type Modulo = Rounding | 9

表示可设置的取模方法舍入类型。

取值类型为下列类型中的并集。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

| 类型 | 说明 |
| --- | --- |
| [Rounding](js-apis-arkts-decimal.md#rounding) | 模运算下的舍入类型。与[Rounding](js-apis-arkts-decimal.md#常量)表示的舍入模式相同。 |
| 9 | 余模运算下，余数始终为正。欧几里得除法，与[Decimal.EUCLIDEAN](js-apis-arkts-decimal.md#常量)一致。 |

## DecimalConfig

PhonePC/2in1TabletTVWearable

用于设置Decimal的配置属性，可使用[Decimal.set](js-apis-arkts-decimal.md#set)方法进行配置。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| precision | number | 否 | 是 | 运算结果的最大有效位数，取值范围为[1, 1e9]，默认值为20。 |
| rounding | [Rounding](js-apis-arkts-decimal.md#rounding) | 否 | 是 | 舍入模式，取值范围为0到8的整数，默认值为4。 |
| toExpNeg | number | 否 | 是 | 指数表示法的负指数值的极限值，若Decimal的负指数小于等于该值时，使用科学计数法表示，[toString](js-apis-arkts-decimal.md#tostring)方法中使用，取值范围为[-9e15, 0]，默认值为-7。 |
| toExpPos | number | 否 | 是 | 指数表示法的正指数值的极限值，若Decimal的正指数大于等于该值时，使用科学计数法表示，[toString](js-apis-arkts-decimal.md#tostring)方法中使用，取值范围为[0, 9e15]，默认值为21。 |
| minE | number | 否 | 是 | 负指数极限，若Decimal的指数值小于该值，会下溢到零，取值范围为[-9e15, 0]，默认值为-9e15。 |
| maxE | number | 否 | 是 | 正指数极限，若Decimal的指数值大于该值，会溢出至无穷大，取值范围为[0, 9e15]，默认值为9e15。 |
| crypto | boolean | 否 | 是 | 确定是否使用加密安全伪随机数生成的值，true表示使用加密安全伪随机数，false表示不使用，默认值为false。该能力不支持使用，报错的错误码为：10200061。 |
| modulo | [Modulo](js-apis-arkts-decimal.md#modulo) | 否 | 是 | 模计算时使用的舍入模式，取值范围为0到9的整数，默认值为1。 |
| defaults | boolean | 否 | 是 | 表示未指定的属性是否被设置为默认值，true表示使用默认值，false表示不使用默认值，默认值为false。 |

## Decimal

PhonePC/2in1TabletTVWearable

任意精度的Decimal类型。

### 属性

PhonePC/2in1TabletTVWearable

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| d | number[] | 是 | 否 | digits：表示Decimal数整数部分和小数部分的数组。 |
| e | number | 是 | 否 | exponent：表示Decimal数的十进制指数。 |
| s | number | 是 | 否 | sign：表示Decimal数的符号位，0表示正数，1表示负数。 |

### 常量

PhonePC/2in1TabletTVWearable

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

| 名称 | 类型 | 值 | 说明 |
| --- | --- | --- | --- |
| ROUND\_UP | number | 0 | 向远离零的方向舍入。模运算下，如果被除数为负，则余数为正，否则为负。 |
| ROUND\_DOWN | number | 1 | 向靠近零的方向舍入。模运算下，余数与被除数的符号相同，使用截断除法。 |
| ROUND\_CEILING | number | 2 | 向正无穷方向舍入。 |
| ROUND\_FLOOR | number | 3 | 向负无穷方向舍入。模运算下，余数与除数的符号相同。 |
| ROUND\_HALF\_UP | number | 4 | 向最近的邻值舍入。如果距离相等，则向远离零的方向舍入。 |
| ROUND\_HALF\_DOWN | number | 5 | 向最近的邻值舍入。如果距离相等，则向靠近零方向舍入。 |
| ROUND\_HALF\_EVEN | number | 6 | 向最近的邻值舍入。如果距离相等，则向偶数邻值舍入。模运算下，IEEE 754 求余函数。 |
| ROUND\_HALF\_CEILING | number | 7 | 向最近的邻值舍入。如果距离相等，则向正无穷方向舍入。 |
| ROUND\_HALF\_FLOOR | number | 8 | 向最近的邻值舍入。如果距离相等，则向负无穷方向舍入。 |
| EUCLIDEAN | number | 9 | 模运算下，余数始终为正。使用欧几里得除法：q = sign(x) \* floor(a / abs(x))。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor(n: Value)

Decimal的构造函数。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| n | [Value](js-apis-arkts-decimal.md#value) | 是 | 构造Decimal时的初始值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

**示例：**

```
1. let data: Decimal = new Decimal(5);
2. console.info("test Decimal constructor:" + data.toString()); // 'test Decimal constructor:5'
```

### abs

PhonePC/2in1TabletTVWearable

abs(): Decimal

返回一个新的Decimal对象，其值是此Decimal的绝对值。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回绝对值运算后的Decimal对象实例。 |

**示例：**

```
1. let data: Decimal = new Decimal(-0.5).abs();
2. console.info("test Decimal abs:" + data.toString()); // 'test Decimal abs:0.5'
```

### floor

PhonePC/2in1TabletTVWearable

floor(): Decimal

返回一个新的Decimal对象，其值是此Decimal向负无穷方向舍入得到的结果。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回舍入之后的Decimal对象实例。 |

**示例：**

```
1. let data: Decimal = new Decimal(1.8).floor();
2. console.info("test Decimal floor:" + data.toString()); // 'test Decimal floor:1'
```

### ceil

PhonePC/2in1TabletTVWearable

ceil(): Decimal

返回一个新的Decimal对象，其值是此Decimal向正无穷方向舍入得到的结果。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回舍入之后的Decimal对象实例。 |

**示例：**

```
1. let data: Decimal = new Decimal(1.8).ceil();
2. console.info("test Decimal ceil:" + data.toString()); // 'test Decimal ceil:2'
```

### trunc

PhonePC/2in1TabletTVWearable

trunc(): Decimal

返回一个新的Decimal对象，其值是将此Decimal截断为整数部分。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回截断之后的Decimal对象实例。 |

**示例：**

```
1. let data: Decimal = new Decimal(2.5).trunc();
2. console.info("test Decimal trunc:" + data.toString()); // 'test Decimal trunc:2'
```

### clamp

PhonePC/2in1TabletTVWearable

clamp(min: Value, max: Value): Decimal

返回一个将Decimal值限制在min到max范围内的Decimal对象。如果值大于max，返回max；如果值小于min，返回min；否则，返回原值。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| min | [Value](js-apis-arkts-decimal.md#value) | 是 | 限制的最小值。包含该值。 |
| max | [Value](js-apis-arkts-decimal.md#value) | 是 | 限制的最大值。包含该值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回符合范围内的Decimal对象实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |
| 10200001 | The value of `min` is out of range. |

**示例：**

```
1. let data1: Decimal = new Decimal(10.1).clamp(0, 10);
2. console.info("test Decimal clamp:" + data1.toString()); // 'test Decimal clamp:10'

4. let data2: Decimal = new Decimal(-5).clamp(0, 10);
5. console.info("test Decimal clamp:" + data2.toString()); // 'test Decimal clamp:0'

7. let data3: Decimal = new Decimal(7.5).clamp(0, 10);
8. console.info("test Decimal clamp:" + data3.toString()); // 'test Decimal clamp:7.5'
```

### add

PhonePC/2in1TabletTVWearable

add(n: Value): Decimal

返回一个新的Decimal对象，其值是将此Decimal的值加上n。

使用[DecimalConfig.precision](js-apis-arkts-decimal.md#decimalconfig)的值进行有效数字的保留，使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| n | [Value](js-apis-arkts-decimal.md#value) | 是 | 加法运算的加数。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回加法运算后的Decimal对象实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

**示例：**

```
1. let data: Decimal = new Decimal(0.5).add(0.5);
2. console.info("test Decimal add:" + data.toString()); // 'test Decimal add:1'
```

### sub

PhonePC/2in1TabletTVWearable

sub(n: Value): Decimal

返回一个新的Decimal对象，其值是将此Decimal的值减去n。

使用[DecimalConfig.precision](js-apis-arkts-decimal.md#decimalconfig)的值进行有效数字的保留，使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| n | [Value](js-apis-arkts-decimal.md#value) | 是 | 减法运算的减数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回减法运算后的Decimal对象实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

**示例：**

```
1. let data: Decimal = new Decimal(1).sub(0.5);
2. console.info("test Decimal sub:" + data.toString()); // 'test Decimal sub:0.5'
```

### mul

PhonePC/2in1TabletTVWearable

mul(n: Value): Decimal

返回一个新的Decimal对象，其值是将此Decimal的值乘以n。

使用[DecimalConfig.precision](js-apis-arkts-decimal.md#decimalconfig)的值进行有效数字的保留，使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| n | [Value](js-apis-arkts-decimal.md#value) | 是 | 乘法运算的乘数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回乘法运算后的Decimal对象实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

**示例：**

```
1. let data: Decimal = new Decimal(1).mul(0.5);
2. console.info("test Decimal mul:" + data.toString()); // 'test Decimal mul:0.5'
```

### div

PhonePC/2in1TabletTVWearable

div(n: Value): Decimal

返回一个新的Decimal对象，其值是将此Decimal的值除以n。

使用[DecimalConfig.precision](js-apis-arkts-decimal.md#decimalconfig)的值进行有效数字的保留，使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| n | [Value](js-apis-arkts-decimal.md#value) | 是 | 除法运算的除数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回除法运算后的Decimal对象实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

**示例：**

```
1. let data: Decimal = new Decimal(1).div(0.5);
2. console.info("test Decimal div:" + data.toString()); // 'test Decimal div:2'
```

### mod

PhonePC/2in1TabletTVWearable

mod(n: Value): Decimal

返回一个新的Decimal对象，其值是将此Decimal的值除以n后的模。

使用[DecimalConfig.precision](js-apis-arkts-decimal.md#decimalconfig)的值进行有效数字的保留，使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| n | [Value](js-apis-arkts-decimal.md#value) | 是 | 取模运算的除数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回取模运算后的Decimal对象实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

**示例：**

```
1. let data: Decimal = new Decimal(2).mod(1);
2. console.info("test Decimal mod:" + data.toString()); // 'test Decimal mod:0'
```

### sqrt

PhonePC/2in1TabletTVWearable

sqrt(): Decimal

返回一个新的Decimal对象，其值是当前Decimal的平方根。

使用[DecimalConfig.precision](js-apis-arkts-decimal.md#decimalconfig)的值进行有效数字的保留，使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回平方根运算后的Decimal对象实例。 |

**示例：**

```
1. let data: Decimal = new Decimal(3).sqrt();
2. console.info("test Decimal sqrt:" + data.toString()); // 'test Decimal sqrt:1.7320508075688772935'
```

### cbrt

PhonePC/2in1TabletTVWearable

cbrt(): Decimal

返回一个新的Decimal对象，其值是当前Decimal对象的立方根。

使用[DecimalConfig.precision](js-apis-arkts-decimal.md#decimalconfig)的值进行有效数字的保留，使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回立方根运算后的Decimal对象实例。 |

**示例：**

```
1. let data: Decimal = new Decimal(3).cbrt();
2. console.info("test Decimal cbrt:" + data.toString()); // 'test Decimal cbrt:1.4422495703074083823'
```

### pow

PhonePC/2in1TabletTVWearable

pow(n: Value): Decimal

返回一个新的Decimal对象，其值是这个Decimal值的n次幂。

使用[DecimalConfig.precision](js-apis-arkts-decimal.md#decimalconfig)的值进行有效数字的保留，使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| n | [Value](js-apis-arkts-decimal.md#value) | 是 | 幂运算的幂的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回幂运算后的Decimal对象实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |
| 10200060 | Precision limit exceeded. |

**示例：**

```
1. let data: Decimal = new Decimal(3).pow(-2);
2. console.info("test Decimal pow:" + data.toString()); // 'test Decimal pow:0.11111111111111111111'
```

### exp

PhonePC/2in1TabletTVWearable

exp(): Decimal

返回一个新的Decimal对象，其值是此Decimal值的自然指数。

使用[DecimalConfig.precision](js-apis-arkts-decimal.md#decimalconfig)的值进行有效数字的保留，使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回自然指数运算后的Decimal对象实例。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200060 | Precision limit exceeded. |

**示例：**

```
1. let data: Decimal = new Decimal(2).exp();
2. console.info("test Decimal exp:" + data.toString()); // 'test Decimal exp:7.3890560989306502272'
```

### log

PhonePC/2in1TabletTVWearable

log(n: Value): Decimal

返回一个对数运算后的Decimal对象，其值是以n为底的对数值。

使用[DecimalConfig.precision](js-apis-arkts-decimal.md#decimalconfig)的值进行有效数字的保留，使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| n | [Value](js-apis-arkts-decimal.md#value) | 是 | 对数计算的底数值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回对数运算后的Decimal对象实例。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |
| 10200060 | Precision limit exceeded. |

**示例：**

```
1. let data: Decimal = new Decimal(2).log(256);
2. console.info("test Decimal log:" + data.toString()); // 'test Decimal log:0.125'
```

### ln

PhonePC/2in1TabletTVWearable

ln(): Decimal

返回一个新的Decimal对象，其值是此Decimal值的自然对数。

使用[DecimalConfig.precision](js-apis-arkts-decimal.md#decimalconfig)的值进行有效数字的保留，使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回自然对数运算后的Decimal对象实例。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200060 | Precision limit exceeded. |

**示例：**

```
1. let data: Decimal = new Decimal(1.23e+30).ln();
2. console.info("test Decimal ln:" + data.toString()); // 'test Decimal ln:69.284566959205696648'
```

### cos

PhonePC/2in1TabletTVWearable

cos(): Decimal

返回一个新的Decimal对象，其值是此Decimal的余弦值。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回计算余弦值的Decimal对象实例。 |

**示例：**

```
1. let data: Decimal = new Decimal(-0.25).cos();
2. console.info("test Decimal cos:" + data.toString()); // 'test Decimal cos:0.96891242171064478414'
```

### sin

PhonePC/2in1TabletTVWearable

sin(): Decimal

返回一个新的Decimal对象，其值是此Decimal的正弦值。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回计算正弦值的Decimal对象实例。 |

**示例：**

```
1. let data: Decimal = new Decimal(0.75).sin();
2. console.info("test Decimal sin:" + data.toString()); // 'test Decimal sin:0.68163876002333416673'
```

### tan

PhonePC/2in1TabletTVWearable

tan(): Decimal

返回一个新的Decimal对象，其值是此Decimal的正切值。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回计算正切值的Decimal对象实例。 |

**示例：**

```
1. let data: Decimal = new Decimal(0.75).tan();
2. console.info("test Decimal tan:" + data.toString()); // 'test Decimal tan:0.93159645994407246117'
```

### cosh

PhonePC/2in1TabletTVWearable

cosh(): Decimal

返回一个新的Decimal对象，其值是此Decimal的双曲余弦值。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回计算双曲余弦值的Decimal对象实例。 |

**示例：**

```
1. let data: Decimal = new Decimal(0.5).cosh();
2. console.info("test Decimal cosh:" + data.toString()); // 'test Decimal cosh:1.1276259652063807852'
```

### sinh

PhonePC/2in1TabletTVWearable

sinh(): Decimal

返回一个新的Decimal对象，其值是此Decimal的双曲正弦值。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回计算双曲正弦值的Decimal对象实例。 |

**示例：**

```
1. let data: Decimal = new Decimal(0.5).sinh();
2. console.info("test Decimal sinh:" + data.toString()); // 'test Decimal sinh:0.52109530549374736162'
```

### tanh

PhonePC/2in1TabletTVWearable

tanh(): Decimal

返回一个新的Decimal对象，其值是此Decimal的双曲正切值。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回计算双曲正切值的Decimal对象实例。 |

**示例：**

```
1. let data: Decimal = new Decimal(0.5).tanh();
2. console.info("test Decimal tanh:" + data.toString()); // 'test Decimal tanh:0.4621171572600097585'
```

### acos

PhonePC/2in1TabletTVWearable

acos(): Decimal

返回一个新的Decimal对象，其值是此Decimal的反余弦值。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回计算反余弦值的Decimal对象实例。 |

**错误码**：

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200060 | Precision limit exceeded. |

**示例：**

```
1. let data: Decimal = new Decimal(0.5).acos();
2. console.info("test Decimal acos:" + data.toString()); // 'test Decimal acos:1.0471975511965977462'
```

### asin

PhonePC/2in1TabletTVWearable

asin(): Decimal

返回一个新的Decimal对象，其值是此Decimal的反正弦值。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回计算反正弦值的Decimal对象实例。 |

**错误码**：

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200060 | Precision limit exceeded. |

**示例：**

```
1. let data: Decimal = new Decimal(0.75).asin();
2. console.info("test Decimal asin:" + data.toString()); // 'test Decimal asin:0.84806207898148100805'
```

### atan

PhonePC/2in1TabletTVWearable

atan(): Decimal

返回一个新的Decimal对象，其值是此Decimal的反正切值。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回计算反正切值的Decimal对象实例。 |

**错误码**：

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200060 | Precision limit exceeded. |

**示例：**

```
1. let data: Decimal = new Decimal(0.75).atan();
2. console.info("test Decimal atan:" + data.toString()); // 'test Decimal atan:0.6435011087932843868'
```

### acosh

PhonePC/2in1TabletTVWearable

acosh(): Decimal

返回一个新的Decimal对象，其值是此Decimal值的双曲余弦的倒数。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回计算双曲余弦的倒数值的Decimal对象实例。 |

**错误码**：

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200060 | Precision limit exceeded. |

**示例：**

```
1. let data: Decimal = new Decimal(50).acosh();
2. console.info("test Decimal acosh:" + data.toString()); // 'test Decimal acosh:4.6050701709847571595'
```

### asinh

PhonePC/2in1TabletTVWearable

asinh(): Decimal

返回一个新的Decimal对象，其值是此Decimal值的双曲正弦的倒数。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回计算双曲正弦的倒数值的Decimal对象实例。 |

**错误码**：

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200060 | Precision limit exceeded. |

**示例：**

```
1. let data: Decimal = new Decimal(50).asinh();
2. console.info("test Decimal asinh:" + data.toString()); // 'test Decimal asinh:4.6052701709914238266'
```

### atanh

PhonePC/2in1TabletTVWearable

atanh(): Decimal

返回一个新的Decimal对象，其值是此Decimal值的双曲正切的倒数。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回计算双曲正切的倒数值的Decimal对象实例。 |

**错误码**：

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200060 | Precision limit exceeded. |

**示例：**

```
1. let data: Decimal = new Decimal(0.75).atanh();
2. console.info("test Decimal atanh:" + data.toString()); // 'test Decimal atanh:0.97295507452765665255'
```

### comparedTo

PhonePC/2in1TabletTVWearable

comparedTo(n: Value): number

Decimal的比较方法。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| n | [Value](js-apis-arkts-decimal.md#value) | 是 | 待比较的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回该Decimal与n的比较结果：  1:该Decimal大于比较值。  -1:该Decimal小于比较值。  0:该Decimal等于比较值。  NaN:该Decimal与比较值有一个值为NaN。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

**示例：**

```
1. let data: Decimal = new Decimal(Infinity);
2. let data1: Decimal = new Decimal(5);
3. let data2: number = data.comparedTo(data1);
4. console.info("test Decimal comparedTo:" + data2); // 'test Decimal comparedTo:1'

6. let data3: number = data1.comparedTo(10.5);
7. console.info("test Decimal comparedTo:" + data3); // 'test Decimal comparedTo:-1'
```

### equals

PhonePC/2in1TabletTVWearable

equals(n: Value): boolean

返回该Decimal是否等于比较值。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| n | [Value](js-apis-arkts-decimal.md#value) | 是 | 待比较的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true表示该Decimal与比较值相等，其余情况为false。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

**示例：**

```
1. let data: Decimal = new Decimal(0);
2. let data1: boolean = data.equals('1e-324');
3. console.info("test Decimal equals:" + data1); // 'test Decimal equals:false'
```

### greaterThan

PhonePC/2in1TabletTVWearable

greaterThan(n: Value): boolean

返回该Decimal是否大于比较值。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| n | [Value](js-apis-arkts-decimal.md#value) | 是 | 待比较的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true表示该Decimal大于比较值，其余情况为false。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

**示例：**

```
1. let data: Decimal = new Decimal(0.1);
2. let data1: boolean = data.greaterThan(new Decimal(0.3).sub(0.2));
3. console.info("test Decimal greaterThan:" + data1); // 'test Decimal greaterThan:false'
```

### greaterThanOrEqualTo

PhonePC/2in1TabletTVWearable

greaterThanOrEqualTo(n: Value): boolean

返回该Decimal是否大于等于比较值。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| n | [Value](js-apis-arkts-decimal.md#value) | 是 | 待比较的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true表示该Decimal大于等于比较值，其余情况为false。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

**示例：**

```
1. let data: Decimal = new Decimal(0.3).sub(0.2);
2. let data1: boolean = data.greaterThanOrEqualTo(0.1);
3. console.info("test Decimal greaterThanOrEqualTo:" + data1); // 'test Decimal greaterThanOrEqualTo:true'
```

### lessThan

PhonePC/2in1TabletTVWearable

lessThan(n: Value): boolean

返回该Decimal是否小于比较值。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| n | [Value](js-apis-arkts-decimal.md#value) | 是 | 待比较的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true表示该Decimal小于比较值，其余情况为false。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

**示例：**

```
1. let data: Decimal = new Decimal(0.3).sub(0.2);
2. let data1: boolean = data.lessThan(0.1)
3. console.info("test Decimal lessThan:" + data1); // 'test Decimal lessThan:false'
```

### lessThanOrEqualTo

PhonePC/2in1TabletTVWearable

lessThanOrEqualTo(n: Value): boolean

返回该Decimal是否小于等于比较值。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| n | [Value](js-apis-arkts-decimal.md#value) | 是 | 待比较的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true表示该Decimal小于等于比较值，其余情况为false。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

**示例：**

```
1. let data: Decimal = new Decimal(0.1);
2. let data1: boolean = data.lessThanOrEqualTo(new Decimal(0.3).sub(0.2))
3. console.info("test Decimal lessThanOrEqualTo:" + data1); // 'test Decimal lessThanOrEqualTo:true'
```

### isFinite

PhonePC/2in1TabletTVWearable

isFinite(): boolean

返回该Decimal是否为有限值。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true表示该Decimal为有限值，其余情况为false。 |

**示例：**

```
1. let data: Decimal = new Decimal(1);
2. let data1: boolean = data.isFinite();
3. console.info("test Decimal isFinite:" + data1); // 'test Decimal isFinite:true'
```

### isInteger

PhonePC/2in1TabletTVWearable

isInteger(): boolean

返回该Decimal是否为整数。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true表示该Decimal为整数，其余情况为false。 |

**示例：**

```
1. let data: Decimal = new Decimal(123.456);
2. let data1: boolean = data.isInteger();
3. console.info("test Decimal isInteger:" + data1); // 'test Decimal isInteger:false'
```

### isNaN

PhonePC/2in1TabletTVWearable

isNaN(): boolean

返回该Decimal是否为无效值。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true表示该Decimal为NaN，其余情况为false。 |

**示例：**

```
1. let data: Decimal = new Decimal(NaN);
2. let data1: boolean = data.isNaN();
3. console.info("test Decimal isNaN:" + data1); // 'test Decimal isNaN:true'
```

### isNegative

PhonePC/2in1TabletTVWearable

isNegative(): boolean

返回该Decimal是否为负数（区分正负零）。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true表示该Decimal为负数，其余情况为false。 |

**示例：**

```
1. let data: Decimal = new Decimal(-5);
2. let data1: boolean = data.isNegative();
3. console.info("test Decimal isNegative:" + data1); // 'test Decimal isNegative:true'

5. let data2: Decimal = new Decimal(-0);
6. let data3: boolean = data2.isNegative();
7. console.info("test Decimal isNegative:" + data3); // 'test Decimal isNegative:true'
```

### isPositive

PhonePC/2in1TabletTVWearable

isPositive(): boolean

返回该Decimal是否为正数（区分正负零）。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true表示该Decimal为正数，其余情况为false。 |

**示例：**

```
1. let data: Decimal = new Decimal(5);
2. let data1: boolean = data.isPositive();
3. console.info("test Decimal isPositive:" + data1); // 'test Decimal isPositive:true'

5. let data2: Decimal = new Decimal(0);
6. let data3: boolean = data2.isPositive();
7. console.info("test Decimal isPositive:" + data3); // 'test Decimal isPositive:true'
```

### isZero

PhonePC/2in1TabletTVWearable

isZero(): boolean

返回该Decimal是否为0或是-0。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true表示该Decimal为0或是-0，其余情况为false。 |

**示例：**

```
1. let data: Decimal = new Decimal(0);
2. let data1: boolean = data.isZero();
3. console.info("test Decimal isZero:" + data1.toString()); // 'test Decimal isZero:true'
```

### dividedToIntegerBy

PhonePC/2in1TabletTVWearable

dividedToIntegerBy(n: Value): Decimal

返回该Decimal除以n后获得的整数部分。

使用[DecimalConfig.precision](js-apis-arkts-decimal.md#decimalconfig)的值进行有效数字的保留，使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| n | [Value](js-apis-arkts-decimal.md#value) | 是 | 除法的除数值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回一个Decimal对象，其值是将此Decimal的值除以n值的整数部分。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

**示例：**

```
1. let data: Decimal = new Decimal(5);
2. let data1: Decimal = new Decimal(3);
3. let data2: Decimal = data.dividedToIntegerBy(data1);
4. console.info("test Decimal dividedToIntegerBy:" + data2.toString()); // 'test Decimal dividedToIntegerBy:1'
```

### negate

PhonePC/2in1TabletTVWearable

negate(): Decimal

对Decimal值进行取反操作。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回一个Decimal对象，其值将此Decimal的值乘以-1。 |

**示例：**

```
1. let data: Decimal = new Decimal(1.8);
2. let data1: Decimal = data.negate();
3. console.info("test Decimal negate:" + data1.toString()); // 'test Decimal negate:-1.8'
```

### toBinary

PhonePC/2in1TabletTVWearable

toBinary(): string

将Decimal转换为二进制表示的字符串。

使用[DecimalConfig.precision](js-apis-arkts-decimal.md#decimalconfig)的值进行有效数字的保留，使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回二进制表示的字符串。 |

**示例：**

```
1. let data: Decimal = new Decimal(256);
2. let data1: string = data.toBinary();
3. console.info("test Decimal toBinary:" + data1); // 'test Decimal toBinary:0b100000000'
```

### toBinary

PhonePC/2in1TabletTVWearable

toBinary(significantDigits: number): string

将Decimal转换为二进制表示的字符串，并可按照significantDigits设置有效数字。

使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| significantDigits | number | 是 | 转换时保留的有效数字，取值范围为[1, 1e9]的整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回二进制表示的字符串。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of `significantDigits` is out of range. |

**示例：**

```
1. let data: Decimal = new Decimal(256);
2. let data1: string = data.toBinary(1);
3. console.info("test Decimal toBinary:" + data1); // 'test Decimal toBinary:0b1p+8'
```

### toBinary

PhonePC/2in1TabletTVWearable

toBinary(significantDigits: number, rounding: Rounding): string

将Decimal转换为二进制表示的字符串，并可按照significantDigits设置有效数字，以及按照rounding设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| significantDigits | number | 是 | 转换时保留的有效数字，取值范围为[1, 1e9]的整数。 |
| rounding | [Rounding](js-apis-arkts-decimal.md#rounding) | 是 | 转换时使用的舍入模式，取值范围参考[Rounding](js-apis-arkts-decimal.md#rounding)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回二进制表示的字符串。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of `significantDigits | rounding` is out of range. |

**示例：**

```
1. let data: Decimal = new Decimal(256);
2. let data1: string = data.toBinary(1, Decimal.ROUND_HALF_UP);
3. console.info("test Decimal toBinary:" + data1); // 'test Decimal toBinary:0b1p+8'
```

### toOctal

PhonePC/2in1TabletTVWearable

toOctal(): string

转换为八进制表示的字符串。

使用[DecimalConfig.precision](js-apis-arkts-decimal.md#decimalconfig)的值进行有效数字的保留，使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回八进制表示的字符串。 |

**示例：**

```
1. let data: Decimal = new Decimal(256);
2. let data1: string = data.toOctal();
3. console.info("test Decimal toOctal:" + data1); // 'test Decimal toOctal:0o400'
```

### toOctal

PhonePC/2in1TabletTVWearable

toOctal(significantDigits: number): string

转换为八进制表示的字符串，可按照significantDigits设置有效数字。

使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| significantDigits | number | 是 | 转换时保留的有效数字，取值范围为[1, 1e9]的整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回八进制表示的字符串。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of `significantDigits` is out of range. |

**示例：**

```
1. let data: Decimal = new Decimal(256);
2. let data1: string = data.toOctal(1);
3. console.info("test Decimal toOctal:" + data1); // 'test Decimal toOctal:0o1p+8'
```

### toOctal

PhonePC/2in1TabletTVWearable

toOctal(significantDigits: number, rounding: Rounding): string

转换为八进制表示的字符串，可按照significantDigits设置有效数字，可按照rounding设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| significantDigits | number | 是 | 转换时保留的有效数字，取值范围为[1, 1e9]的整数。 |
| rounding | [Rounding](js-apis-arkts-decimal.md#rounding) | 是 | 转换时使用的舍入模式，取值范围参考[Rounding](js-apis-arkts-decimal.md#rounding)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回八进制表示的字符串。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of `significantDigits | rounding` is out of range. |

**示例：**

```
1. let data: Decimal = new Decimal(256);
2. let data1: string = data.toOctal(1, Decimal.ROUND_HALF_UP);
3. console.info("test Decimal toOctal:" + data1); // 'test Decimal toOctal:0o1p+8'
```

### toHexadecimal

PhonePC/2in1TabletTVWearable

toHexadecimal(): string

转换为十六进制表示的字符串。

使用[DecimalConfig.precision](js-apis-arkts-decimal.md#decimalconfig)的值进行有效数字的保留，使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回十六进制表示的字符串。 |

**示例：**

```
1. let data: Decimal = new Decimal(256);
2. let data1: string = data.toHexadecimal();
3. console.info("test Decimal toHexadecimal:" + data1); // 'test Decimal toHexadecimal:0x100'
```

### toHexadecimal

PhonePC/2in1TabletTVWearable

toHexadecimal(significantDigits: number): string

转换为十六进制表示的字符串，可按照significantDigits设置有效数字。

使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| significantDigits | number | 是 | 转换时保留的有效数字，取值范围为[1, 1e9]的整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回十六进制表示的字符串。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of `significantDigits` is out of range. |

**示例：**

```
1. let data: Decimal = new Decimal(256);
2. let data1: string = data.toHexadecimal(1);
3. console.info("test Decimal toHexadecimal:" + data1); // 'test Decimal toHexadecimal:0x1p+8'
```

### toHexadecimal

PhonePC/2in1TabletTVWearable

toHexadecimal(significantDigits: number, rounding: Rounding): string

转换为十六进制表示的字符串，可按照significantDigits设置有效数字，可按照rounding设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| significantDigits | number | 是 | 转换时保留的有效数字，取值范围为[1, 1e9]的整数。 |
| rounding | [Rounding](js-apis-arkts-decimal.md#rounding) | 是 | 转换时使用的舍入模式，取值范围参考[Rounding](js-apis-arkts-decimal.md#rounding)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回十六进制表示的字符串。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of `significantDigits | rounding` is out of range. |

**示例：**

```
1. let data: Decimal = new Decimal(256);
2. let data1: string = data.toHexadecimal(1, Decimal.ROUND_HALF_UP);
3. console.info("test Decimal toHexadecimal:" + data1); // 'test Decimal toHexadecimal:0x1p+8'
```

### toDecimalPlaces

PhonePC/2in1TabletTVWearable

toDecimalPlaces(): Decimal

返回一个保留小数点后指定位数的Decimal对象，不进行小数的取舍。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回一个Decimal对象保留小数点后指定位数。 |

**示例：**

```
1. let data: Decimal = new Decimal(12.34567);
2. let data1: Decimal = data.toDecimalPlaces();
3. console.info("test Decimal toDecimalPlaces:" + data1.toString()); // 'test Decimal toDecimalPlaces:12.34567'
```

### toDecimalPlaces

PhonePC/2in1TabletTVWearable

toDecimalPlaces(decimalPlaces: number): Decimal

返回一个保留小数点后指定位数的Decimal对象，可按照decimalPlaces设置小数位数。

使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| decimalPlaces | number | 是 | 转换时保留的小数点后有效位数，取值范围为[0, 1e9]的整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回一个Decimal对象保留小数点后指定位数。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of `decimalPlaces` is out of range. |

**示例：**

```
1. let data: Decimal = new Decimal(9876.54321);
2. let data1: Decimal = data.toDecimalPlaces(3);
3. console.info("test Decimal toDecimalPlaces:" + data1.toString()); // 'test Decimal toDecimalPlaces:9876.543'
```

### toDecimalPlaces

PhonePC/2in1TabletTVWearable

toDecimalPlaces(decimalPlaces: number, rounding: Rounding): Decimal

返回一个保留小数点后指定位数的Decimal对象，可按照decimalPlaces设置小数位数，可按照rounding设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| decimalPlaces | number | 是 | 转换时保留的小数点后有效位数，取值范围为[0, 1e9]的整数。 |
| rounding | [Rounding](js-apis-arkts-decimal.md#rounding) | 是 | 转换时使用的舍入模式。取值范围参考[Rounding](js-apis-arkts-decimal.md#rounding)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回一个Decimal对象保留小数点后指定位数。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of `decimalPlaces | rounding` is out of range. |

**示例：**

```
1. let data: Decimal = new Decimal(9876.54321);
2. let data1: Decimal = data.toDecimalPlaces(1, 0);
3. console.info("test Decimal toDecimalPlaces:" + data1.toString()); // 'test Decimal toDecimalPlaces:9876.6'
4. data1 = data.toDecimalPlaces(1, Decimal.ROUND_DOWN) // data1：'9876.5'
```

### toExponential

PhonePC/2in1TabletTVWearable

toExponential(): string

将数值转换为指数表示法的字符串，不进行小数部分的舍入。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回按照指数表示法显示的字符串。 |

**示例：**

```
1. let data: Decimal = new Decimal(45.6);
2. let data1: string = data.toExponential();
3. console.info("test Decimal toExponential:" + data1); // 'test Decimal toExponential:4.56e+1'
```

### toExponential

PhonePC/2in1TabletTVWearable

toExponential(decimalPlaces: number): string

将数值转换为按照指数表示法显示的字符串，可按照decimalPlaces设置小数位数。

使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| decimalPlaces | number | 是 | 转换时保留的小数点后有效位数，取值范围为[0, 1e9]的整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回按照指数表示法显示的字符串。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of `decimalPlaces` is out of range. |

**示例：**

```
1. let data: Decimal = new Decimal(45.6);
2. let data1: string = data.toExponential(0);
3. console.info("test Decimal toExponential:" + data1); // 'test Decimal toExponential:5e+1'
4. data1 = data.toExponential(1); // data1：'4.6e+1'
5. data1 = data.toExponential(3); // data1：'4.560e+1'
```

### toExponential

PhonePC/2in1TabletTVWearable

toExponential(decimalPlaces: number, rounding: Rounding): string

转换为按照指数表示法显示的字符串，可按照decimalPlaces设置小数位数，可按照rounding设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| decimalPlaces | number | 是 | 转换时保留的小数点后有效位数，取值范围为[0, 1e9]的整数。 |
| rounding | [Rounding](js-apis-arkts-decimal.md#rounding) | 是 | 转换时使用的舍入模式，取值范围参考[Rounding](js-apis-arkts-decimal.md#rounding)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回按照指数表示法显示的字符串。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of `decimalPlaces | rounding` is out of range. |

**示例：**

```
1. let data: Decimal = new Decimal(45.6);
2. let data1 = data.toExponential(1, Decimal.ROUND_DOWN);
3. console.info("test Decimal toExponential:" + data1); // 'test Decimal toExponential:4.5e+1'
```

### toFixed

PhonePC/2in1TabletTVWearable

toFixed(): string

将数值转换为十进制定点模式表示的字符串，不进行小数的取舍。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回按照正常模式（十进制定点模式）表示的字符串。 |

**示例：**

```
1. let data: Decimal = new Decimal(3.456);
2. let data1: string = data.toFixed();
3. console.info("test Decimal toFixed:" + data1); // 'test Decimal toFixed:3.456'
```

### toFixed

PhonePC/2in1TabletTVWearable

toFixed(decimalPlaces: number): string

将数组转换为十进制定点模式表示的字符串，可按照decimalPlaces设置小数位数。

使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| decimalPlaces | number | 是 | 转换时保留的小数点后有效位数，取值范围为[0, 1e9]的整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回按照正常模式（十进制定点模式）表示的字符串。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of `decimalPlaces` is out of range. |

**示例：**

```
1. let data: Decimal = new Decimal(3.456);
2. let data1: string = data.toFixed(0)
3. console.info("test Decimal toFixed:" + data1); // 'test Decimal toFixed:3'
4. data1 = data.toFixed(2) // data1：'3.46'
5. data1 = data.toFixed(5) // data1：'3.45600'
```

### toFixed

PhonePC/2in1TabletTVWearable

toFixed(decimalPlaces: number, rounding: Rounding): string

将数值转换为十进制定点模式表示的字符串，可按照decimalPlaces设置小数位数，可按照rounding设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| decimalPlaces | number | 是 | 转换时保留的小数点后有效位数，取值范围为[0, 1e9]的整数。 |
| rounding | [Rounding](js-apis-arkts-decimal.md#rounding) | 是 | 转换时使用的舍入模式，取值范围参考[Rounding](js-apis-arkts-decimal.md#rounding)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回按照正常模式（十进制定点模式）表示的字符串。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of `decimalPlaces | rounding` is out of range. |

**示例：**

```
1. let data: Decimal = new Decimal(3.456);
2. let data1: string = data.toFixed(2, Decimal.ROUND_DOWN);
3. console.info("test Decimal toFixed:" + data1); // b：'test Decimal toFixed:3.45'
```

### toFraction

PhonePC/2in1TabletTVWearable

toFraction(): Decimal[]

转换为分数表示的数。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal)[] | 返回一个Decimal数组，该数组长度固定为2，其值表示为具有整数分子和整数分母的简单分数。且分子在前，分母在后。 |

**示例：**

```
1. let data: Decimal = new Decimal(1.75);
2. let data1: Decimal[] = data.toFraction();
3. console.info("test Decimal toFraction:" + data1.toString()); // 'test Decimal toFraction:7,4'
```

### toFraction

PhonePC/2in1TabletTVWearable

toFraction(maxDenominator: Value): Decimal[]

将数值转换为分数表示的数，可以通过maxDenominator设置最大分母值。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| maxDenominator | [Value](js-apis-arkts-decimal.md#value) | 是 | 分母的最大值。包含该值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal)[] | 返回一个Decimal数组，该数组长度固定为2，其值表示为具有整数分子和整数分母的简单分数。且分子在前，分母在后。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

**示例：**

```
1. let pi: Decimal = new Decimal('3.14159265358');
2. let data1 = pi.toFraction(); // data1：'157079632679,50000000000'
3. data1 = pi.toFraction(100000); // data1：'312689, 99532'
4. data1 = pi.toFraction(10000); // data1：'355, 113'
5. data1 = pi.toFraction(100); // data1：'311, 99'
6. data1 = pi.toFraction(10); // data1：'22, 7'
7. data1 = pi.toFraction(1); // data1：'3, 1'
```

### toNearest

PhonePC/2in1TabletTVWearable

toNearest(n: Value): Decimal

返回一个新的Decimal对象，此Decimal为指定值乘以一个倍数后与原Decimal最接近的值。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| n | [Value](js-apis-arkts-decimal.md#value) | 是 | 参考的指定值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Decimal | 返回一个Decimal对象，为最接近原值的指定值的倍数值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

**示例：**

```
1. let data: Decimal = new Decimal(1.39);
2. let data1: Decimal = data.toNearest(0.25);
3. console.info("test Decimal toNearest:" + data1.toString()); // 'test Decimal toNearest:1.5'
```

### toNearest

PhonePC/2in1TabletTVWearable

toNearest(n: Value, rounding: Rounding): Decimal

返回一个新的Decimal对象，此Decimal为指定值乘以一个倍数后与原Decimal最接近的值，可按照rounding设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| n | [Value](js-apis-arkts-decimal.md#value) | 是 | 参考的指定值。 |
| rounding | [Rounding](js-apis-arkts-decimal.md#rounding) | 是 | 转换时使用的舍入模式，取值范围参考[Rounding](js-apis-arkts-decimal.md#rounding)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回一个Decimal对象，为最接近原值的指定值的倍数值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |
| 10200001 | The value of `rounding` is out of range. |

**示例：**

```
1. let data: Decimal = new Decimal(9.499);
2. let data1 = data.toNearest(0.5, Decimal.ROUND_UP); // data1：'9.5'
3. data1 = data.toNearest(0.5, Decimal.ROUND_DOWN); // data1：'9'
```

### toPrecision

PhonePC/2in1TabletTVWearable

toPrecision(): string

将Decimal对象转换为字符串。

使用[DecimalConfig.precision](js-apis-arkts-decimal.md#decimalconfig)的值进行有效数字的保留，使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回一个表示Decimal对象的字符串。 |

**示例：**

```
1. let data: Decimal = new Decimal(45.6);
2. let data1: string = data.toPrecision();
3. console.info("test Decimal toPrecision:" + data1); // 'test Decimal toPrecision:45.6'
```

### toPrecision

PhonePC/2in1TabletTVWearable

toPrecision(significantDigits: number): string

将数值转换为字符串，可按照significantDigits设置有效数字。

使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| significantDigits | number | 是 | 转换时保留的有效数字。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回一个表示Decimal对象的字符串。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of `significantDigits` is out of range. |

**示例：**

```
1. let data: Decimal = new Decimal(45.6);
2. let data1: string = data.toPrecision(1);
3. console.info("test Decimal toPrecision:" + data1); // 'test Decimal toPrecision:5e+1'
4. data1 = data.toPrecision(5); // data1：'45.600'
```

### toPrecision

PhonePC/2in1TabletTVWearable

toPrecision(significantDigits: number, rounding: Rounding): string

转换为字符串，可按照significantDigits设置有效数字，可按照rounding设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| significantDigits | number | 是 | 转换时保留的有效数字，取值范围为[1, 1e9]的整数。 |
| rounding | [Rounding](js-apis-arkts-decimal.md#rounding) | 是 | 转换时使用的舍入模式，取值范围参考[Rounding](js-apis-arkts-decimal.md#rounding)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回一个表示Decimal对象的字符串。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of `significantDigits | rounding` is out of range. |

**示例：**

```
1. let data: Decimal = new Decimal(45.6);
2. let data1: string = data.toPrecision(2, Decimal.ROUND_UP); // data1：'46'
3. data1 = data.toPrecision(2, Decimal.ROUND_DOWN); // data1：'45'
```

### toSignificantDigits

PhonePC/2in1TabletTVWearable

toSignificantDigits(): Decimal

返回一个按照保留有效数字的转换的Decimal对象。

使用[DecimalConfig.precision](js-apis-arkts-decimal.md#decimalconfig)的值进行有效数字的保留，使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回一个保留有效数字后的Decimal对象实例。 |

**示例：**

```
1. let data: Decimal = new Decimal(987.654321);
2. let data1: Decimal = data.toSignificantDigits();
3. console.info("test Decimal toSignificantDigits:" + data1.toString()); // 'test Decimal toSignificantDigits:987.654321'
```

### toSignificantDigits

PhonePC/2in1TabletTVWearable

toSignificantDigits(significantDigits: number): Decimal

返回一个按照保留有效数字的转换的Decimal对象，可按照significantDigits设置有效数字。

使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| significantDigits | number | 是 | 转换时保留的有效数字。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回一个保留有效数字后的Decimal对象实例。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of `significantDigits` is out of range. |

**示例：**

```
1. let data: Decimal = new Decimal(987.654321);
2. let data1: Decimal = data.toSignificantDigits(6);
3. console.info("test Decimal toSignificantDigits:" + data1.toString()); // 'test Decimal toSignificantDigits:987.654'
```

### toSignificantDigits

PhonePC/2in1TabletTVWearable

toSignificantDigits(significantDigits: number, rounding: Rounding): Decimal

返回一个按照保留有效数字的转换的Decimal对象，可按照significantDigits设置有效数字，可按照rounding设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| significantDigits | number | 是 | 转换时保留的有效数字，取值范围为[1, 1e9]的整数。 |
| rounding | [Rounding](js-apis-arkts-decimal.md#rounding) | 是 | 转换时使用的舍入模式，取值范围参考[Rounding](js-apis-arkts-decimal.md#rounding)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回一个保留有效数字后的Decimal对象实例。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of `significantDigits | rounding` is out of range. |

**示例：**

```
1. let data: Decimal = new Decimal(987.654321);
2. let data1: Decimal = data.toSignificantDigits(6, Decimal.ROUND_UP);
3. console.info("test Decimal toSignificantDigits:" + data1.toString()); // 'test Decimal toSignificantDigits:987.655'
```

### toNumber

PhonePC/2in1TabletTVWearable

toNumber(): number

将值转换为number类型。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回一个表示Decimal的number值。 |

**示例：**

```
1. let data: Decimal = new Decimal(456.789);
2. let data1: number = data.toNumber();
3. console.info("test Decimal toNumber:" + data1.toString()); // 'test Decimal toNumber:456.789'
```

### toString

PhonePC/2in1TabletTVWearable

toString(): string

返回一个字符串，表示此 Decimal 的值，如果此 Decimal 的正指数等于或大于[toExpPos](js-apis-arkts-decimal.md#decimalconfig)，或负指数等于或小于[toExpNeg](js-apis-arkts-decimal.md#decimalconfig)，则将返回指数表示法。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回一个表示Decimal的字符串。 |

**示例：**

```
1. let data: Decimal = new Decimal(750000);
2. let data1: string = data.toString();
3. console.info("test Decimal toString:" + data1); // 'test Decimal toString:750000'

5. Decimal.set({ toExpPos: 5 });
6. data1 = data.toString(); // data1:'7.5e+5'

8. let data2: Decimal = new Decimal(0.000000123);
9. console.info("test Decimal toString:" + data2.toString()); // 'test Decimal toString:1.23e-7'

11. Decimal.set({ toExpNeg: -7 });
12. data1 = data2.toString(); // data1:'1.23e-7'
```

### valueOf

PhonePC/2in1TabletTVWearable

valueOf(): string

返回一个字符串，表示此 Decimal 的值，负零包含负号。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回一个表示Decimal的字符串。 |

**示例：**

```
1. let data: Decimal = new Decimal(-0);
2. let data1: string = data.valueOf();
3. console.info("test Decimal valueOf:" + data1); // 'test Decimal valueOf:-0'
```

### decimalPlaces

PhonePC/2in1TabletTVWearable

decimalPlaces(): number

返回Decimal对象的小数位数。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回Decimal对象的小数位数。 |

**示例：**

```
1. let data: Decimal = new Decimal(1.234);
2. let data1: number = data.decimalPlaces();
3. console.info("test Decimal decimalPlaces:" + data1); // 'test Decimal decimalPlaces:3'
```

### precision

PhonePC/2in1TabletTVWearable

precision(): number

返回Decimal对象的有效数字位数。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回Decimal对象的有效位数。 |

**示例：**

```
1. let data: Decimal = new Decimal(1.234);
2. let data1: number = data.precision();
3. console.info("test Decimal precision:" + data1); // 'test Decimal precision:4'
```

### precision

PhonePC/2in1TabletTVWearable

precision(includeZeros: boolean | number): number

返回Decimal对象的有效数字位数，通过includeZeros判断是否计算整数部分的尾随零。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| includeZeros | boolean | number | 是 | 是否计算整数部分尾随零。true或1表示计算整数部分尾随零，false或0表示不计算整数部分尾随零。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回Decimal对象的有效位数。 |

**错误码：**

以下错误码的详细介绍请参见[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200001 | The value of `includeZeros` is out of range. |

**示例：**

```
1. let data: Decimal = new Decimal(987000);
2. let data1: number = data.precision();
3. console.info("test Decimal precision:" + data1); // 'test Decimal precision:3'
4. data1 = data.precision(true); // data1:'6'
```

### abs

PhonePC/2in1TabletTVWearable

static abs(n: Value): Decimal

返回一个新的Decimal对象，Decimal的值为参数n的绝对值。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| n | [Value](js-apis-arkts-decimal.md#value) | 是 | 取绝对值的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回一个值为参数n的绝对值的Decimal。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

**示例：**

```
1. let data: Decimal = Decimal.abs(-0.5);
2. console.info("test Decimal abs:" + data.toString()); // 'test Decimal abs:0.5'
```

### floor

PhonePC/2in1TabletTVWearable

static floor(n: Value): Decimal

返回一个新的Decimal对象，其值为该Decimal向负无穷方向舍入得到的结果。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| n | [Value](js-apis-arkts-decimal.md#value) | 是 | 需要舍入的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回舍入之后的Decimal对象实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

**示例：**

```
1. let data: Decimal = Decimal.floor(1.8);
2. console.info("test Decimal floor:" + data.toString()); // 'test Decimal floor:1'
```

### ceil

PhonePC/2in1TabletTVWearable

static ceil(n: Value): Decimal

返回一个新的Decimal对象，其值为该Decimal向正无穷方向舍入得到的结果。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| n | [Value](js-apis-arkts-decimal.md#value) | 是 | 需要舍入的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回舍入之后的Decimal对象实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

**示例：**

```
1. let data: Decimal = Decimal.ceil(1.8);
2. console.info("test Decimal ceil:" + data.toString()); // 'test Decimal ceil:2'
```

### trunc

PhonePC/2in1TabletTVWearable

static trunc(n: Value): Decimal

返回一个新的Decimal对象，其值是将此Decimal截断为整数部分。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| n | [Value](js-apis-arkts-decimal.md#value) | 是 | 需要截断的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回截断之后的Decimal对象实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

**示例：**

```
1. let data: Decimal = Decimal.trunc(2.5);
2. console.info("test Decimal trunc:" + data.toString()); // 'test Decimal trunc:2'
```

### clamp

PhonePC/2in1TabletTVWearable

static clamp(n: Value, min: Value, max: Value): Decimal

返回一个值为将该Decimal的值限制在min到max范围内的Decimal对象，当大于限制的最大值时返回max，小于限制的最小值时返回min，在范围内返回值不变。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| n | [Value](js-apis-arkts-decimal.md#value) | 是 | 需要被限制的值。 |
| min | [Value](js-apis-arkts-decimal.md#value) | 是 | 限制的最小值。包含该值。 |
| max | [Value](js-apis-arkts-decimal.md#value) | 是 | 限制的最大值。包含该值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回符合范围的Decimal对象实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |
| 10200001 | The value of `min` is out of range. |

**示例：**

```
1. let data: Decimal = Decimal.clamp(10.1, 0, 10);
2. console.info("test Decimal clamp:" + data.toString()); // 'test Decimal clamp:10'
```

### add

PhonePC/2in1TabletTVWearable

static add(x: Value, y: Value): Decimal

返回一个值为x加y的和的Decimal对象。

使用[DecimalConfig.precision](js-apis-arkts-decimal.md#decimalconfig)的值进行有效数字的保留，使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | [Value](js-apis-arkts-decimal.md#value) | 是 | 加法的一个加数。 |
| y | [Value](js-apis-arkts-decimal.md#value) | 是 | 加法的另一个加数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回加法运算后的Decimal对象实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

**示例：**

```
1. let data: Decimal = Decimal.add(0.5, 0.5);
2. console.info("test Decimal add:" + data.toString()); // 'test Decimal add:1'
```

### sum

PhonePC/2in1TabletTVWearable

static sum(...n: Value[]): Decimal

返回一个值为数组元素和的Decimal对象。该接口用于对参数求和，当无入参时会抛出运行时异常。

使用[DecimalConfig.precision](js-apis-arkts-decimal.md#decimalconfig)的值进行有效数字的保留，使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| n | [Value](js-apis-arkts-decimal.md#value)[] | 否 | 加数的序列。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回加法运算后的Decimal对象实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

**示例：**

```
1. let data: Decimal = Decimal.sum(0.5, 0.5);
2. console.info("test Decimal sum:" + data.toString()); // 'test Decimal sum:1'
```

### sub

PhonePC/2in1TabletTVWearable

static sub(x: Value, y: Value): Decimal

返回一个值为x减y的差的Decimal对象。

使用[DecimalConfig.precision](js-apis-arkts-decimal.md#decimalconfig)的值进行有效数字的保留，使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | [Value](js-apis-arkts-decimal.md#value) | 是 | 减法的被减数。 |
| y | [Value](js-apis-arkts-decimal.md#value) | 是 | 减法的减数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回减法运算后的Decimal对象实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

**示例：**

```
1. let data: Decimal = Decimal.sub(1, 0.5);
2. console.info("test Decimal sub:" + data.toString()); // 'test Decimal sub:0.5'
```

### mul

PhonePC/2in1TabletTVWearable

static mul(x: Value, y: Value): Decimal

返回一个值为x乘以y的积的Decimal对象。

使用[DecimalConfig.precision](js-apis-arkts-decimal.md#decimalconfig)的值进行有效数字的保留，使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | [Value](js-apis-arkts-decimal.md#value) | 是 | 乘法的被乘数。 |
| y | [Value](js-apis-arkts-decimal.md#value) | 是 | 乘法的乘数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回乘法运算后的Decimal对象实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

**示例：**

```
1. let data: Decimal = Decimal.mul(1, 0.5);
2. console.info("test Decimal mul:" + data.toString()); // 'test Decimal mul:0.5'
```

### div

PhonePC/2in1TabletTVWearable

static div(x: Value, y: Value): Decimal

返回一个值为x除以y的商的Decimal对象。

使用[DecimalConfig.precision](js-apis-arkts-decimal.md#decimalconfig)的值进行有效数字的保留，使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | [Value](js-apis-arkts-decimal.md#value) | 是 | 除法的被除数。 |
| y | [Value](js-apis-arkts-decimal.md#value) | 是 | 除法的除数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回除法运算后的Decimal对象实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

**示例：**

```
1. let data: Decimal = Decimal.div(1, 0.5);
2. console.info("test Decimal div:" + data.toString()); // 'test Decimal div:2'
```

### mod

PhonePC/2in1TabletTVWearable

static mod(x: Value, y: Value): Decimal

返回一个新的Decimal对象，其值是x除以y的模。

使用[DecimalConfig.precision](js-apis-arkts-decimal.md#decimalconfig)的值进行有效数字的保留，使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | [Value](js-apis-arkts-decimal.md#value) | 是 | 模除运算的被除数。 |
| y | [Value](js-apis-arkts-decimal.md#value) | 是 | 模除运算的除数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回模除运算后的Decimal对象实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

**示例：**

```
1. let data: Decimal = Decimal.mod(2, 1);
2. console.info("test Decimal mod:" + data.toString()); // 'test Decimal mod:0'
```

### sqrt

PhonePC/2in1TabletTVWearable

static sqrt(n: Value): Decimal

返回一个值为n的平方根的Decimal对象。

使用[DecimalConfig.precision](js-apis-arkts-decimal.md#decimalconfig)的值进行有效数字的保留，使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| n | [Value](js-apis-arkts-decimal.md#value) | 是 | 取平方根的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回平方根运算后的Decimal对象实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

**示例：**

```
1. let data: Decimal = Decimal.sqrt(3);
2. console.info("test Decimal sqrt:" + data.toString()); // 'test Decimal sqrt:1.7320508075688772935'
```

### cbrt

PhonePC/2in1TabletTVWearable

static cbrt(n: Value): Decimal

返回一个值为n的立方根的Decimal对象。

使用[DecimalConfig.precision](js-apis-arkts-decimal.md#decimalconfig)的值进行有效数字的保留，使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| n | [Value](js-apis-arkts-decimal.md#value) | 是 | 取立方根的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回立方根运算后的Decimal对象实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

**示例：**

```
1. let data: Decimal = Decimal.cbrt(3);
2. console.info("test Decimal cbrt:" + data.toString()); // 'test Decimal cbrt:1.4422495703074083823'
```

### pow

PhonePC/2in1TabletTVWearable

static pow(base: Value, exponent: Value): Decimal

返回一个值为base的exponent次幂的Decimal对象，按照[DecimalConfig.precision](js-apis-arkts-decimal.md#decimalconfig)设置有效位数，按照[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| base | [Value](js-apis-arkts-decimal.md#value) | 是 | 幂运算的底数的值。 |
| exponent | [Value](js-apis-arkts-decimal.md#value) | 是 | 幂运算的幂的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回幂运算后的Decimal对象实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |
| 10200060 | Precision limit exceeded. |

**示例：**

```
1. let data: Decimal = Decimal.pow(3, -2);
2. console.info("test Decimal pow:" + data.toString()); // 'test Decimal pow:0.11111111111111111111'
```

### exp

PhonePC/2in1TabletTVWearable

static exp(n: Value): Decimal

返回一个值为n的自然指数的Decimal对象。

使用[DecimalConfig.precision](js-apis-arkts-decimal.md#decimalconfig)的值进行有效数字的保留，使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| n | [Value](js-apis-arkts-decimal.md#value) | 是 | 需要求自然指数的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回自然指数运算后的Decimal对象实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |
| 10200060 | Precision limit exceeded. |

**示例：**

```
1. let data: Decimal = Decimal.exp(2);
2. console.info("test Decimal exp:" + data.toString()); // 'test Decimal exp:7.3890560989306502272'
```

### log

PhonePC/2in1TabletTVWearable

static log(n: Value, base: Value): Decimal

返回一个以base为底n的对数的Decimal对象。

使用[DecimalConfig.precision](js-apis-arkts-decimal.md#decimalconfig)的值进行有效数字的保留，使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| n | [Value](js-apis-arkts-decimal.md#value) | 是 | 对数运算的真数。 |
| base | [Value](js-apis-arkts-decimal.md#value) | 是 | 对数运算的底数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回对数运算后的Decimal对象实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |
| 10200060 | Precision limit exceeded. |

**示例：**

```
1. let data: Decimal = Decimal.log(2, 256);
2. console.info("test Decimal log:" + data.toString()); // 'test Decimal log:0.125'
```

### ln

PhonePC/2in1TabletTVWearable

static ln(n: Value): Decimal

返回一个值为n的自然对数的Decimal对象。

使用[DecimalConfig.precision](js-apis-arkts-decimal.md#decimalconfig)的值进行有效数字的保留，使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| n | [Value](js-apis-arkts-decimal.md#value) | 是 | 对数运算的真数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回自然对数运算后的Decimal对象实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |
| 10200060 | Precision limit exceeded. |

**示例：**

```
1. let data: Decimal = Decimal.ln(1.23e+30);
2. console.info("test Decimal ln:" + data.toString()); // 'test Decimal ln:69.284566959205696648'
```

### log2

PhonePC/2in1TabletTVWearable

static log2(n: Value): Decimal

返回一个以2为底n的对数的Decimal对象。

使用[DecimalConfig.precision](js-apis-arkts-decimal.md#decimalconfig)的值进行有效数字的保留，使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| n | [Value](js-apis-arkts-decimal.md#value) | 是 | 对数运算的真数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回以2为底的对数运算后的Decimal对象实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |
| 10200060 | Precision limit exceeded. |

**示例：**

```
1. let data: Decimal = Decimal.log2(4);
2. console.info("test Decimal log2:" + data.toString()); // 'test Decimal log2:2'
```

### log10

PhonePC/2in1TabletTVWearable

static log10(n: Value): Decimal

返回一个以10为底n的对数的Decimal对象。

使用[DecimalConfig.precision](js-apis-arkts-decimal.md#decimalconfig)的值进行有效数字的保留，使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| n | [Value](js-apis-arkts-decimal.md#value) | 是 | 对数运算的真数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回以10为底的对数运算后的Decimal对象实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |
| 10200060 | Precision limit exceeded. |

**示例：**

```
1. let data: Decimal = Decimal.log10(10000);
2. console.info("test Decimal log10:" + data.toString()); // 'test Decimal log10:4'
```

### cos

PhonePC/2in1TabletTVWearable

static cos(n: Value): Decimal

返回一个新的Decimal对象，其值是n的余弦值。

使用[DecimalConfig.precision](js-apis-arkts-decimal.md#decimalconfig)的值进行有效数字的保留，使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| n | [Value](js-apis-arkts-decimal.md#value) | 是 | 要求余弦值的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回n的余弦值对应的Decimal对象实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

**示例：**

```
1. let data: Decimal = Decimal.cos(-0.25);
2. console.info("test Decimal cos:" + data.toString()); // 'test Decimal cos:0.96891242171064478414'
```

### sin

PhonePC/2in1TabletTVWearable

static sin(n: Value): Decimal

返回一个新的Decimal对象，其值是n的正弦值。

使用[DecimalConfig.precision](js-apis-arkts-decimal.md#decimalconfig)的值进行有效数字的保留，使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| n | [Value](js-apis-arkts-decimal.md#value) | 是 | 要求正弦值的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回n的正弦值对应的Decimal对象实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

**示例：**

```
1. let data: Decimal = Decimal.sin(0.75);
2. console.info("test Decimal sin:" + data.toString()); // 'test Decimal sin:0.68163876002333416673'
```

### tan

PhonePC/2in1TabletTVWearable

static tan(n: Value): Decimal

返回一个新的Decimal对象，其值是n的正切值。

使用[DecimalConfig.precision](js-apis-arkts-decimal.md#decimalconfig)的值进行有效数字的保留，使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| n | [Value](js-apis-arkts-decimal.md#value) | 是 | 要求的正切值的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回n的正切值对应的Decimal对象实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

**示例：**

```
1. let data: Decimal = Decimal.tan(0.75);
2. console.info("test Decimal tan:" + data.toString()); // 'test Decimal tan:0.93159645994407246117'
```

### cosh

PhonePC/2in1TabletTVWearable

static cosh(n: Value): Decimal

返回一个新的Decimal对象，其值是n的双曲余弦值。

使用[DecimalConfig.precision](js-apis-arkts-decimal.md#decimalconfig)的值进行有效数字的保留，使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| n | [Value](js-apis-arkts-decimal.md#value) | 是 | 需要求的双曲余弦值的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回n的双曲余弦值对应的Decimal对象实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

**示例：**

```
1. let data: Decimal = Decimal.cosh(0.5);
2. console.info("test Decimal cosh:" + data.toString()); // 'test Decimal cosh:1.1276259652063807852'
```

### sinh

PhonePC/2in1TabletTVWearable

static sinh(n: Value): Decimal

返回一个新的Decimal对象，其值是n的双曲正弦值。

使用[DecimalConfig.precision](js-apis-arkts-decimal.md#decimalconfig)的值进行有效数字的保留，使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| n | [Value](js-apis-arkts-decimal.md#value) | 是 | 需要求的双曲正弦值的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回n的双曲正弦值对应的Decimal对象实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

**示例：**

```
1. let data: Decimal = Decimal.sinh(0.5);
2. console.info("test Decimal sinh:" + data.toString()); // 'test Decimal sinh:0.52109530549374736162'
```

### tanh

PhonePC/2in1TabletTVWearable

static tanh(n: Value): Decimal

返回一个新的Decimal对象，其值是n的双曲正切值。

使用[DecimalConfig.precision](js-apis-arkts-decimal.md#decimalconfig)的值进行有效数字的保留，使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| n | [Value](js-apis-arkts-decimal.md#value) | 是 | 需要求双曲正切值的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回n的双曲正切值对应的Decimal对象实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

**示例：**

```
1. let data: Decimal = Decimal.tanh(0.5);
2. console.info("test Decimal tanh:" + data.toString()); // 'test Decimal tanh:0.4621171572600097585'
```

### acos

PhonePC/2in1TabletTVWearable

static acos(n: Value): Decimal

返回一个新的Decimal对象，其值是n的反余弦值。

使用[DecimalConfig.precision](js-apis-arkts-decimal.md#decimalconfig)的值进行有效数字的保留，使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| n | [Value](js-apis-arkts-decimal.md#value) | 是 | 需要求反余弦值的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回n的反余弦值对应的Decimal对象实例。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |
| 10200060 | Precision limit exceeded. |

**示例：**

```
1. let data: Decimal = Decimal.acos(0.5);
2. console.info("test Decimal acos:" + data.toString()); // 'test Decimal acos:1.0471975511965977462'
```

### asin

PhonePC/2in1TabletTVWearable

static asin(n: Value): Decimal

返回一个新的Decimal对象，其值是n的反正弦值。

使用[DecimalConfig.precision](js-apis-arkts-decimal.md#decimalconfig)的值进行有效数字的保留，使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| n | [Value](js-apis-arkts-decimal.md#value) | 是 | 需要求反正弦值的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回n的反正弦值对应的Decimal对象实例。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |
| 10200060 | Precision limit exceeded. |

**示例：**

```
1. let data: Decimal = Decimal.asin(0.75);
2. console.info("test Decimal asin:" + data.toString()); // 'test Decimal asin:0.84806207898148100805'
```

### atan

PhonePC/2in1TabletTVWearable

static atan(n: Value): Decimal

返回一个新的Decimal对象，其值是n的反正切值。

使用[DecimalConfig.precision](js-apis-arkts-decimal.md#decimalconfig)的值进行有效数字的保留，使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| n | [Value](js-apis-arkts-decimal.md#value) | 是 | 需要求反正切值的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回n的反正切值对应的Decimal对象实例。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |
| 10200060 | Precision limit exceeded. |

**示例：**

```
1. let data: Decimal = Decimal.atan(0.75);
2. console.info("test Decimal atan:" + data.toString()); // 'test Decimal atan:0.6435011087932843868'
```

### acosh

PhonePC/2in1TabletTVWearable

static acosh(n: Value): Decimal

返回一个新的Decimal对象，其值是n的双曲余弦值的倒数。

使用[DecimalConfig.precision](js-apis-arkts-decimal.md#decimalconfig)的值进行有效数字的保留，使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| n | [Value](js-apis-arkts-decimal.md#value) | 是 | 需要求的双曲余弦的倒数的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回n的双曲余弦的倒数对应的Decimal对象实例。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |
| 10200060 | Precision limit exceeded. |

**示例：**

```
1. let data: Decimal = Decimal.acosh(50);
2. console.info("test Decimal acosh:" + data.toString()); // 'test Decimal acosh:4.6050701709847571595'
```

### asinh

PhonePC/2in1TabletTVWearable

static asinh(n: Value): Decimal

返回一个新的Decimal对象，其值是n的双曲正弦值的倒数。

使用[DecimalConfig.precision](js-apis-arkts-decimal.md#decimalconfig)的值进行有效数字的保留，使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| n | [Value](js-apis-arkts-decimal.md#value) | 是 | 需要求双曲正弦的倒数的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回n的双曲正弦的倒数对应的Decimal对象实例。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |
| 10200060 | Precision limit exceeded. |

**示例：**

```
1. let data: Decimal = Decimal.asinh(50);
2. console.info("test Decimal asinh:" + data.toString()); // 'test Decimal asinh:4.6052701709914238266'
```

### atanh

PhonePC/2in1TabletTVWearable

static atanh(n: Value): Decimal

返回一个新的Decimal对象，其值是n的双曲正切值的倒数。

使用[DecimalConfig.precision](js-apis-arkts-decimal.md#decimalconfig)的值进行有效数字的保留，使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| n | [Value](js-apis-arkts-decimal.md#value) | 是 | 需要求双曲正切的倒数的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回n的双曲正切的倒数对应的Decimal对象实例。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |
| 10200060 | Precision limit exceeded. |

**示例：**

```
1. let data: Decimal = Decimal.atanh(0.75);
2. console.info("test Decimal atanh:" + data.toString()); // 'test Decimal atanh:0.97295507452765665255'
```

### atan2

PhonePC/2in1TabletTVWearable

static atan2(y: Value, x: Value): Decimal

返回一个新的Decimal对象，其值是为-π到π范围内的y/x反正切值。

使用[DecimalConfig.precision](js-apis-arkts-decimal.md#decimalconfig)的值进行有效数字的保留，使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| y | [Value](js-apis-arkts-decimal.md#value) | 是 | 除法的被除数。 |
| x | [Value](js-apis-arkts-decimal.md#value) | 是 | 除法的除数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回-pi 到 pi 范围内的"y/x"反正切值对应的Decimal对象实例。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |
| 10200060 | Precision limit exceeded. |

**示例：**

```
1. let data: Decimal = Decimal.atan2(2, 3);
2. console.info("test Decimal atan2:" + data.toString()); // 'test Decimal atan2:0.58800260354756755125'
```

### hypot

PhonePC/2in1TabletTVWearable

static hypot(...n: Value[]): Decimal

返回一个新的Decimal对象，其值是参数平方和的平方根。无入参时默认返回0。

使用[DecimalConfig.precision](js-apis-arkts-decimal.md#decimalconfig)的值进行有效数字的保留，使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)的值设置舍入模式。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| n | [Value](js-apis-arkts-decimal.md#value)[] | 否 | 需要求平方和的序列。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回值为所有参数平方和的平方根的Decimal对象实例。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

**示例：**

```
1. let data: Decimal = Decimal.hypot(2, 3, 4);
2. console.info("test Decimal hypot:" + data.toString()); // 'test Decimal hypot:5.3851648071345040313'
```

### max

PhonePC/2in1TabletTVWearable

static max(...n: Value[]): Decimal

返回一个值为所有参数中最大值的Decimal对象。该接口用于求参数中的最大值，当无入参时会发生运行时异常。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| n | [Value](js-apis-arkts-decimal.md#value)[] | 否 | 需要求最大值的序列。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回所有参数中的最大值的Decimal对象实例。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

**示例：**

```
1. let data: Decimal = Decimal.max(2, 3, 4);
2. console.info("test Decimal max:" + data.toString()); // 'test Decimal max:4'
```

### min

PhonePC/2in1TabletTVWearable

static min(...n: Value[]): Decimal

返回一个值为所有参数中最小值的Decimal对象。该接口用于求参数中的最小值，当无入参时会发生运行时异常。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| n | [Value](js-apis-arkts-decimal.md#value)[] | 否 | 需要求最小值的序列。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回所有参数中的最小值的Decimal对象实例。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

**示例：**

```
1. let data: Decimal = Decimal.min(2, 3, 4);
2. console.info("test Decimal min:" + data.toString()); // 'test Decimal min:2'
```

### random

PhonePC/2in1TabletTVWearable

static random(): Decimal

返回一个值为大于等于0小于1的随机值的Decimal对象。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 大于等于0小于1的随机值的Decimal对象实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 10200061 | Crypto unavailable. |

**示例：**

```
1. let data: Decimal = Decimal.random();
```

### random

PhonePC/2in1TabletTVWearable

static random(significantDigits: number): Decimal

返回一个值为大于等于0小于1的随机值的Decimal对象，随机值保留significantDigits位有效数字。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| significantDigits | number | 是 | 随机值保留的有效数字。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 大于等于0小于1的随机值的Decimal对象实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |
| 10200061 | Crypto unavailable. |

**示例：**

```
1. let data: Decimal = Decimal.random(20);
```

### sign

PhonePC/2in1TabletTVWearable

static sign(n: Value): number

根据参数的值进行判断返回对应的值：当n>0返回1，当n<0返回-1，当n==0返回0，当n==-0返回-0，否则返回NaN。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| n | [Value](js-apis-arkts-decimal.md#value) | 是 | 需要判断的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 根据参数的值进行判断返回对应的值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

**示例：**

```
1. let data1: number = Decimal.sign(2);
2. console.info("test Decimal sign:" + data1); // 'test Decimal sign:1'

4. let data2: number = Decimal.sign(-3);
5. console.info("test Decimal sign:" + data2); // 'test Decimal sign:-1'

7. let data3: number = Decimal.sign(0);
8. console.info("test Decimal sign:" + data3); // 'test Decimal sign:0'

10. let data4: number = Decimal.sign(3.14);
11. console.info("test Decimal sign:" + data4); // 'test Decimal sign:1'

13. let data5: number = Decimal.sign(-1.618);
14. console.info("test Decimal sign:" + data5); // 'test Decimal sign:-1'

16. let data6: number = Decimal.sign("100");
17. console.info("test Decimal sign:" + data6); // 'test Decimal sign:1'

19. let data7: number = Decimal.sign("-50");
20. console.info("test Decimal sign:" + data7); // 'test Decimal sign:-1'

22. let data8: number = Decimal.sign(NaN);
23. console.info("test Decimal sign:" + data8); // 'test Decimal sign:NaN'
```

### round

PhonePC/2in1TabletTVWearable

static round(n: Value): Decimal

返回一个新的Decimal对象，其值是使用[DecimalConfig.rounding](js-apis-arkts-decimal.md#decimalconfig)模式舍入为整数的n。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| n | [Value](js-apis-arkts-decimal.md#value) | 是 | 需要舍入的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Decimal](js-apis-arkts-decimal.md#decimal) | 返回舍入之后的整数对应的Decimal对象实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |

**示例：**

```
1. let x = 3.3333333333333;
2. let data = Decimal.round(x);
3. console.info("test Decimal round:" + data.toString()); // 'test Decimal round:3'
```

### set

PhonePC/2in1TabletTVWearable

static set(config: DecimalConfig):void

用于设置Decimal的配置属性，通过set设置的属性是全局生效的。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [DecimalConfig](js-apis-arkts-decimal.md#decimalconfig) | 是 | 需要配置的属性集合。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[语言基础类库错误码](errorcode-utils.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Incorrect parameter types;2. Parameter verification failed. |
| 10200001 | The value of `DecimalConfig.properties` is out of range. |
| 10200061 | Crypto unavailable. |

**示例1：**

```
1. let data : Decimal = new Decimal(1.2345678901234567);
2. Decimal.set({
3. precision: 5,
4. rounding: 4,
5. toExpNeg: -7,
6. toExpPos: 7,
7. maxE: 9e15,
8. minE: -9e15,
9. modulo: 1,
10. crypto: false
11. });
12. let data1 : Decimal = data.add(0.5);
13. console.info("test Decimal set:" + data1.toString()); // "test Decimal set:1.7346"
14. // 将配置属性全部设置为默认值
15. Decimal.set({ defaults: true });
16. let data2 : Decimal = data.add(0.5);
17. console.info("test Decimal set:" + data2.toString()); // "test Decimal set:1.7345678901234567"
18. // 最大有效位数设置为10，其余配置属性设置为默认值
19. Decimal.set({ precision: 10, defaults: true });
20. let data3 : Decimal = data.add(0.5);
21. console.info("test Decimal set:" + data3.toString()); // "test Decimal set:1.73456789"

23. // toExpNeg和toExpPos的用法
24. Decimal.set({ toExpNeg: -7 });
25. let x0 : Decimal = new Decimal(0.00000123); // x0:'0.00000123'
26. let x1 : Decimal = new Decimal(0.000000123); // x1:'1.23e-7'

28. Decimal.set({ toExpPos: 2 });
29. let y0 : Decimal = new Decimal(12.3); // y0:'12.3'
30. let y1 : Decimal = new Decimal(123); // y1:'1.23e+2'

32. // 所有数据均使用科学计数法表示
33. Decimal.set({ toExpPos: 0 });

35. // minE和maxE的用法
36. Decimal.set({ minE: -500 });
37. let a0 : Decimal = new Decimal('1e-500'); // a0:'1e-500'
38. let a1 : Decimal = new Decimal('9.9e-501'); // a1:'0e0'

40. Decimal.set({ minE: -3 });
41. let b0 : Decimal = new Decimal(0.001); // b0:'0.001'
42. let b1 : Decimal = new Decimal(0.0001); // b1:'0e0'

44. Decimal.set({ maxE: 500 });
45. let c0 : Decimal = new Decimal('9.999e500'); // c0:'9.999e+500'
46. let c1 : Decimal = new Decimal('1e501'); // c1:'Infinity'

48. Decimal.set({ maxE: 4 });
49. let d0 : Decimal = new Decimal(99999); // d0:'9.9999e+4'
50. let d1 : Decimal = new Decimal(100000); // d1:'Infinity'
```

**示例2：**

```
1. // /entry/src/main/ets/pages/test.ets
2. export function test(){
3. let data : Decimal = new Decimal(1.2345678901234567);
4. Decimal.set({
5. precision: 5,
6. rounding: 0,
7. toExpNeg: -7,
8. toExpPos: 7,
9. maxE: 9e15,
10. minE: -9e15,
11. modulo: 1,
12. crypto: false
13. });
14. let data1 : Decimal = data.add(0.5);
15. console.info("test Decimal set:" + data1.toString()); // 'test Decimal set:1.7346'
16. }
```

```
1. // /entry/src/main/ets/pages/Index.ets
2. import {test} from './test';

4. let data : Decimal = new Decimal(1.2345678901234567);
5. Decimal.set({
6. precision: 6,
7. rounding: 1,
8. toExpNeg: -7,
9. toExpPos: 7,
10. maxE: 9e15,
11. minE: -9e15,
12. modulo: 1,
13. crypto: false
14. });
15. let data1 : Decimal = data.add(0.5);
16. console.info("test Decimal set:" + data1.toString()); // 'test Decimal set:1.73456'
17. test();
18. data1 = data1.add(0); // data1:'1.7346'
19. console.info("test Decimal set:" + data1.toString()); // 'test Decimal set:1.7346'
```
