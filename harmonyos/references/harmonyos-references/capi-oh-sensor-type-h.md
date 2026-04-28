---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-sensor-type-h
title: oh_sensor_type.h
breadcrumb: API参考 > 系统 > 硬件 > Sensor Service Kit（传感器服务） > C API > 头文件 > oh_sensor_type.h
category: harmonyos-references
scraped_at: 2026-04-28T08:11:07+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c8b5268d3b7ed1b867422bc412e027a2ef25cef6ccee7cca6ff4f97651f13750
---

## 概述

PhonePC/2in1TabletTVWearable

定义常用传感器属性。

**引用文件：** <sensors/oh\_sensor\_type.h>

**库：** libohsensor.so

**系统能力：** SystemCapability.Sensors.Sensor

**起始版本：** 11

**相关模块：** [Sensor](capi-sensor.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [Sensor\_Info](capi-sensor-sensor-info.md) | Sensor\_Info | 定义传感器信息。 |
| [Sensor\_Event](capi-sensor-sensor-event.md) | Sensor\_Event | 定义传感器数据信息。 |
| [Sensor\_SubscriptionId](capi-sensor-sensor-subscriptionid.md) | Sensor\_SubscriptionId | 定义传感器订阅ID，唯一标识传感器。 |
| [Sensor\_SubscriptionAttribute](capi-sensor-sensor-subscriptionattribute.md) | Sensor\_SubscriptionAttribute | 定义传感器订阅属性。 |
| [Sensor\_Subscriber](capi-sensor-sensor-subscriber.md) | Sensor\_Subscriber | 定义传感器订阅者信息。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [Sensor\_Type](capi-oh-sensor-type-h.md#sensor_type) | Sensor\_Type | 枚举传感器类型。 |
| [Sensor\_Result](capi-oh-sensor-type-h.md#sensor_result) | Sensor\_Result | 定义传感器错误码。 |
| [Sensor\_Accuracy](capi-oh-sensor-type-h.md#sensor_accuracy) | Sensor\_Accuracy | 枚举传感器报告的数据的精度级别。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [Sensor\_Info \*\*OH\_Sensor\_CreateInfos(uint32\_t count)](capi-oh-sensor-type-h.md#oh_sensor_createinfos) | - | 用给定的数字创建一个实例数组，请参考[Sensor\_Info](capi-sensor-sensor-info.md)。 |
| [int32\_t OH\_Sensor\_DestroyInfos(Sensor\_Info \*\*sensors, uint32\_t count)](capi-oh-sensor-type-h.md#oh_sensor_destroyinfos) | - | 销毁实例数组并回收内存，请参考[Sensor\_Info](capi-sensor-sensor-info.md)。 |
| [int32\_t OH\_SensorInfo\_GetName(Sensor\_Info\* sensor, char \*sensorName, uint32\_t \*length)](capi-oh-sensor-type-h.md#oh_sensorinfo_getname) | - | 获取传感器名称。 |
| [int32\_t OH\_SensorInfo\_GetVendorName(Sensor\_Info\* sensor, char \*vendorName, uint32\_t \*length)](capi-oh-sensor-type-h.md#oh_sensorinfo_getvendorname) | - | 获取传感器的厂商名称。 |
| [int32\_t OH\_SensorInfo\_GetType(Sensor\_Info\* sensor, Sensor\_Type \*sensorType)](capi-oh-sensor-type-h.md#oh_sensorinfo_gettype) | - | 获取传感器类型。 |
| [int32\_t OH\_SensorInfo\_GetResolution(Sensor\_Info\* sensor, float \*resolution)](capi-oh-sensor-type-h.md#oh_sensorinfo_getresolution) | - | 获取传感器分辨率。 |
| [int32\_t OH\_SensorInfo\_GetMinSamplingInterval(Sensor\_Info\* sensor, int64\_t \*minSamplingInterval)](capi-oh-sensor-type-h.md#oh_sensorinfo_getminsamplinginterval) | - | 获取传感器的最小数据上报间隔。 |
| [int32\_t OH\_SensorInfo\_GetMaxSamplingInterval(Sensor\_Info\* sensor, int64\_t \*maxSamplingInterval)](capi-oh-sensor-type-h.md#oh_sensorinfo_getmaxsamplinginterval) | - | 获取传感器的最大数据上报间隔时间。 |
| [int32\_t OH\_SensorEvent\_GetType(Sensor\_Event\* sensorEvent, Sensor\_Type \*sensorType)](capi-oh-sensor-type-h.md#oh_sensorevent_gettype) | - | 获取传感器类型。 |
| [int32\_t OH\_SensorEvent\_GetTimestamp(Sensor\_Event\* sensorEvent, int64\_t \*timestamp)](capi-oh-sensor-type-h.md#oh_sensorevent_gettimestamp) | - | 获取传感器数据的时间戳。 |
| [int32\_t OH\_SensorEvent\_GetAccuracy(Sensor\_Event\* sensorEvent, Sensor\_Accuracy \*accuracy)](capi-oh-sensor-type-h.md#oh_sensorevent_getaccuracy) | - | 获取传感器数据的精度。 |
| [int32\_t OH\_SensorEvent\_GetData(Sensor\_Event\* sensorEvent, float \*\*data, uint32\_t \*length)](capi-oh-sensor-type-h.md#oh_sensorevent_getdata) | - | 获取传感器数据。数据的长度和内容依赖于监听的传感器类型，传感器上报的数据格式如下：SENSOR\_TYPE\_ACCELEROMETER: data[0]、data[1]、data[2]分别表示设备x、y、z轴的加速度分量，单位m/s2。SENSOR\_TYPE\_GYROSCOPE: data[0]、data[1]、data[2]分别表示设备x、y、z轴的旋转角速度，单位弧度/s。SENSOR\_TYPE\_AMBIENT\_LIGHT: data[0]表示环境光强度，单位勒克斯；从api版本12开始，将返回两个额外的数据，其中data[1]表示色温，单位为开尔文；data[2]表示红外亮度，单位cd/m2。SENSOR\_TYPE\_MAGNETIC\_FIELD: data[0]、data[1]、data[2]分别表示设备x、y、z轴的地磁分量，单位微特斯拉。SENSOR\_TYPE\_BAROMETER：data[0]表示气压值，单位hPa。SENSOR\_TYPE\_HALL: data[0]表示皮套吸合状态，0表示打开，大于0表示吸附。SENSOR\_TYPE\_PROXIMITY：data[0]表示接近状态，0表示接近，大于0表示远离。SENSOR\_TYPE\_ORIENTATION:data[0]、data[1]、data[2]分别表示设备绕z、x、y轴的角度，单位度。SENSOR\_TYPE\_GRAVITY：data[0]、data[1]、data[2]分别表示设备x、y、z轴的重力加速度分量，单位m/s2。SENSOR\_TYPE\_ROTATION\_VECTOR:data[0]、data[1]、data[2]分别表示设备x、y、z轴的旋转角度，单位度，data[3]表示旋转向量元素。SENSOR\_TYPE\_PEDOMETER\_DETECTION:data[0]表示几步检测状态，1表示检测到了步数变化。SENSOR\_TYPE\_PEDOMETER:data[0]表示步数。SENSOR\_TYPE\_HEART\_RATE：data[0]表示心率数值。SENSOR\_TYPE\_LINEAR\_ACCELERATION：从api版本13开始支持。data[0]，data[1]，data[2]，表示分别绕设备的x、y、z轴的线性加速度，单位为m/s2。SENSOR\_TYPE\_GAME\_ROTATION\_VECTOR：从api版本13支持。data[0]，data[1]和data[2]，表示设备分别围绕x、y、z轴的旋转角度，单位为度。data[3]表示旋转向量。 |
| [Sensor\_SubscriptionId \*OH\_Sensor\_CreateSubscriptionId(void)](capi-oh-sensor-type-h.md#oh_sensor_createsubscriptionid) | - | 创建一个[Sensor\_SubscriptionId](capi-sensor-sensor-subscriptionid.md)实例。 |
| [int32\_t OH\_Sensor\_DestroySubscriptionId(Sensor\_SubscriptionId \*id)](capi-oh-sensor-type-h.md#oh_sensor_destroysubscriptionid) | - | 销毁[Sensor\_SubscriptionId](capi-sensor-sensor-subscriptionid.md)实例并回收内存。 |
| [int32\_t OH\_SensorSubscriptionId\_GetType(Sensor\_SubscriptionId\* id, Sensor\_Type \*sensorType)](capi-oh-sensor-type-h.md#oh_sensorsubscriptionid_gettype) | - | 获取传感器类型。 |
| [int32\_t OH\_SensorSubscriptionId\_SetType(Sensor\_SubscriptionId\* id, const Sensor\_Type sensorType)](capi-oh-sensor-type-h.md#oh_sensorsubscriptionid_settype) | - | 设置传感器类型。 |
| [Sensor\_SubscriptionAttribute \*OH\_Sensor\_CreateSubscriptionAttribute(void)](capi-oh-sensor-type-h.md#oh_sensor_createsubscriptionattribute) | - | 创建[Sensor\_SubscriptionAttribute](capi-sensor-sensor-subscriptionattribute.md)实例。 |
| [int32\_t OH\_Sensor\_DestroySubscriptionAttribute(Sensor\_SubscriptionAttribute \*attribute)](capi-oh-sensor-type-h.md#oh_sensor_destroysubscriptionattribute) | - | 销毁[Sensor\_SubscriptionAttribute](capi-sensor-sensor-subscriptionattribute.md)实例并回收内存。 |
| [int32\_t OH\_SensorSubscriptionAttribute\_SetSamplingInterval(Sensor\_SubscriptionAttribute\* attribute, const int64\_t samplingInterval)](capi-oh-sensor-type-h.md#oh_sensorsubscriptionattribute_setsamplinginterval) | - | 设置传感器数据报告间隔。 |
| [int32\_t OH\_SensorSubscriptionAttribute\_GetSamplingInterval(Sensor\_SubscriptionAttribute\* attribute, int64\_t \*samplingInterval)](capi-oh-sensor-type-h.md#oh_sensorsubscriptionattribute_getsamplinginterval) | - | 获取传感器数据报告间隔。 |
| [typedef void (\*Sensor\_EventCallback)(Sensor\_Event \*event)](capi-oh-sensor-type-h.md#sensor_eventcallback) | Sensor\_EventCallback | 定义用于报告传感器数据的回调函数。 |
| [Sensor\_Subscriber \*OH\_Sensor\_CreateSubscriber(void)](capi-oh-sensor-type-h.md#oh_sensor_createsubscriber) | - | 创建一个[Sensor\_Subscriber](capi-sensor-sensor-subscriber.md)实例。 |
| [int32\_t OH\_Sensor\_DestroySubscriber(Sensor\_Subscriber \*subscriber)](capi-oh-sensor-type-h.md#oh_sensor_destroysubscriber) | - | 销毁[Sensor\_Subscriber](capi-sensor-sensor-subscriber.md)实例并回收内存。 |
| [int32\_t OH\_SensorSubscriber\_SetCallback(Sensor\_Subscriber\* subscriber, const Sensor\_EventCallback callback)](capi-oh-sensor-type-h.md#oh_sensorsubscriber_setcallback) | - | 设置一个回调函数来报告传感器数据。 |
| [int32\_t OH\_SensorSubscriber\_GetCallback(Sensor\_Subscriber\* subscriber, Sensor\_EventCallback \*callback)](capi-oh-sensor-type-h.md#oh_sensorsubscriber_getcallback) | - | 获取用于报告传感器数据的回调函数。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### Sensor\_Type

PhonePC/2in1TabletTVWearable

```
1. enum Sensor_Type
```

**描述**

枚举传感器类型。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| SENSOR\_TYPE\_ACCELEROMETER = 1 | 加速度传感器。  **起始版本：** 11 |
| SENSOR\_TYPE\_GYROSCOPE = 2 | 陀螺仪传感器。  **起始版本：** 11 |
| SENSOR\_TYPE\_AMBIENT\_LIGHT = 5 | 环境光传感器。  **起始版本：** 11 |
| SENSOR\_TYPE\_MAGNETIC\_FIELD = 6 | 地磁传感器。  **起始版本：** 11 |
| SENSOR\_TYPE\_BAROMETER = 8 | 气压传感器。  **起始版本：** 11 |
| SENSOR\_TYPE\_HALL = 10 | 霍尔传感器。  **起始版本：** 11 |
| SENSOR\_TYPE\_PROXIMITY = 12 | 接近光传感器。  **起始版本：** 11 |
| SENSOR\_TYPE\_ORIENTATION = 256 | 方向传感器。  **起始版本：** 11 |
| SENSOR\_TYPE\_GRAVITY = 257 | 重力传感器。  **起始版本：** 11 |
| SENSOR\_TYPE\_LINEAR\_ACCELERATION = 258 | 线性加速度传感器。  **起始版本：** 13 |
| SENSOR\_TYPE\_ROTATION\_VECTOR = 259 | 旋转矢量传感器。  **起始版本：** 11 |
| SENSOR\_TYPE\_GAME\_ROTATION\_VECTOR = 262 | 游戏旋转矢量传感器。  **起始版本：** 13 |
| SENSOR\_TYPE\_PEDOMETER\_DETECTION = 265 | 计步器检测传感器。  **起始版本：** 11 |
| SENSOR\_TYPE\_PEDOMETER = 266 | 计步器传感器。  **起始版本：** 11 |
| SENSOR\_TYPE\_HEART\_RATE = 278 | 心率传感器。  **起始版本：** 11 |

### Sensor\_Result

PhonePC/2in1TabletTVWearable

```
1. enum Sensor_Result
```

**描述**

定义传感器错误码。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| SENSOR\_SUCCESS = 0 | 操作成功。  **起始版本：** 11 |
| SENSOR\_PERMISSION\_DENIED = 201 | 权限验证失败。  **起始版本：** 11 |
| SENSOR\_PARAMETER\_ERROR = 401 | 参数检查失败。例如，没有传入强制参数，或者传入的参数类型不正确。  **起始版本：** 11 |
| SENSOR\_SERVICE\_EXCEPTION = 14500101 | 传感器服务异常。  **起始版本：** 11 |

### Sensor\_Accuracy

PhonePC/2in1TabletTVWearable

```
1. enum Sensor_Accuracy
```

**描述**

枚举传感器报告的数据的精度级别。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| SENSOR\_ACCURACY\_UNRELIABLE = 0 | 传感器数据不可靠。有可能传感器不与设备接触而进行测量。  **起始版本：** 11 |
| SENSOR\_ACCURACY\_LOW = 1 | 传感器数据精度较低。数据在使用前必须根据环境进行校准。  **起始版本：** 11 |
| SENSOR\_ACCURACY\_MEDIUM = 2 | 传感器数据处于中等精度水平。建议用户在使用前根据实际环境进行数据校准。  **起始版本：** 11 |
| SENSOR\_ACCURACY\_HIGH = 3 | 传感器数据具有很高的精度。数据可以直接使用。  **起始版本：** 11 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_Sensor\_CreateInfos()

PhonePC/2in1TabletTVWearable

```
1. Sensor_Info **OH_Sensor_CreateInfos(uint32_t count)
```

**描述**

用给定的数字创建一个实例数组，请参考[Sensor\_Info](capi-sensor-sensor-info.md)。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| uint32\_t count | 要创建的实例的数量，请参考 [Sensor\_Info](capi-sensor-sensor-info.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Sensor\_Info \*\*](capi-sensor-sensor-info.md) | 如果操作成功，返回指向[Sensor\_Info](capi-sensor-sensor-info.md)实例数组的双指针；否则返回**NULL**。 |

### OH\_Sensor\_DestroyInfos()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Sensor_DestroyInfos(Sensor_Info **sensors, uint32_t count)
```

**描述**

销毁实例数组并回收内存，请参考[Sensor\_Info](capi-sensor-sensor-info.md)。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Sensor\_Info](capi-sensor-sensor-info.md) \*\*sensors | 指向[Sensor\_Info](capi-sensor-sensor-info.md)实例数组的双指针。 |
| uint32\_t count | 要销毁的[Sensor\_Info](capi-sensor-sensor-info.md)实例的数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 如果操作成功返回**SENSOR\_SUCCESS**；否则返回[Sensor\_Result](capi-oh-sensor-type-h.md#sensor_result)中定义的错误代码。 |

### OH\_SensorInfo\_GetName()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_SensorInfo_GetName(Sensor_Info* sensor, char *sensorName, uint32_t *length)
```

**描述**

获取传感器名称。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Sensor\_Info](capi-sensor-sensor-info.md)\* sensor | 指向传感器信息的指针。 |
| char \*sensorName | 指向传感器名称的指针。 |
| uint32\_t \*length | 指向长度的指针，以字节为单位。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 如果操作成功返回**SENSOR\_SUCCESS**；否则返回[Sensor\_Result](capi-oh-sensor-type-h.md#sensor_result)中定义的错误代码。 |

### OH\_SensorInfo\_GetVendorName()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_SensorInfo_GetVendorName(Sensor_Info* sensor, char *vendorName, uint32_t *length)
```

**描述**

获取传感器的厂商名称。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Sensor\_Info](capi-sensor-sensor-info.md)\* sensor | 指向传感器信息的指针。 |
| char \*vendorName | 指向供应商名称的指针。 |
| uint32\_t \*length | 指向长度的指针，以字节为单位。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 如果操作成功返回**SENSOR\_SUCCESS**；否则返回[Sensor\_Result](capi-oh-sensor-type-h.md#sensor_result)中定义的错误代码。 |

### OH\_SensorInfo\_GetType()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_SensorInfo_GetType(Sensor_Info* sensor, Sensor_Type *sensorType)
```

**描述**

获取传感器类型。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Sensor\_Info](capi-sensor-sensor-info.md)\* sensor | 指向传感器信息的指针。 |
| [Sensor\_Type](capi-oh-sensor-type-h.md#sensor_type) \*sensorType | 指向传感器类型的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 如果操作成功返回**SENSOR\_SUCCESS**；否则返回[Sensor\_Result](capi-oh-sensor-type-h.md#sensor_result)中定义的错误代码。 |

### OH\_SensorInfo\_GetResolution()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_SensorInfo_GetResolution(Sensor_Info* sensor, float *resolution)
```

**描述**

获取传感器分辨率。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Sensor\_Info](capi-sensor-sensor-info.md)\* sensor | 指向传感器信息的指针。 |
| float \*resolution | 指向传感器分辨率[Sensor\_Accuracy](capi-oh-sensor-type-h.md#sensor_accuracy)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 如果操作成功返回**SENSOR\_SUCCESS**；否则返回[Sensor\_Result](capi-oh-sensor-type-h.md#sensor_result)中定义的错误代码。 |

### OH\_SensorInfo\_GetMinSamplingInterval()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_SensorInfo_GetMinSamplingInterval(Sensor_Info* sensor, int64_t *minSamplingInterval)
```

**描述**

获取传感器的最小数据上报间隔。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Sensor\_Info](capi-sensor-sensor-info.md)\* sensor | 指向传感器信息的指针。 |
| int64\_t \*minSamplingInterval | 指向最小数据报告间隔的指针，以纳秒为单位。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 如果操作成功返回**SENSOR\_SUCCESS**；否则返回[Sensor\_Result](capi-oh-sensor-type-h.md#sensor_result)中定义的错误代码。 |

### OH\_SensorInfo\_GetMaxSamplingInterval()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_SensorInfo_GetMaxSamplingInterval(Sensor_Info* sensor, int64_t *maxSamplingInterval)
```

**描述**

获取传感器的最大数据上报间隔时间。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Sensor\_Info](capi-sensor-sensor-info.md)\* sensor | 指向传感器信息的指针。 |
| int64\_t \*maxSamplingInterval | 指向最大数据报告间隔的指针，单位为纳秒。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 如果操作成功返回**SENSOR\_SUCCESS**；否则返回[Sensor\_Result](capi-oh-sensor-type-h.md#sensor_result)中定义的错误代码。 |

### OH\_SensorEvent\_GetType()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_SensorEvent_GetType(Sensor_Event* sensorEvent, Sensor_Type *sensorType)
```

**描述**

获取传感器类型。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Sensor\_Event](capi-sensor-sensor-event.md)\* sensorEvent | 指向传感器数据信息的指针。 |
| [Sensor\_Type](capi-oh-sensor-type-h.md#sensor_type) \*sensorType | 指向传感器类型的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 如果操作成功返回**SENSOR\_SUCCESS**；否则返回[Sensor\_Result](capi-oh-sensor-type-h.md#sensor_result)中定义的错误代码。 |

### OH\_SensorEvent\_GetTimestamp()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_SensorEvent_GetTimestamp(Sensor_Event* sensorEvent, int64_t *timestamp)
```

**描述**

获取传感器数据的时间戳。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Sensor\_Event](capi-sensor-sensor-event.md)\* sensorEvent | 指向传感器数据信息的指针。 |
| int64\_t \*timestamp | 时间戳指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 如果操作成功返回**SENSOR\_SUCCESS**；否则返回[Sensor\_Result](capi-oh-sensor-type-h.md#sensor_result)中定义的错误代码。 |

### OH\_SensorEvent\_GetAccuracy()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_SensorEvent_GetAccuracy(Sensor_Event* sensorEvent, Sensor_Accuracy *accuracy)
```

**描述**

获取传感器数据的精度。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Sensor\_Event](capi-sensor-sensor-event.md)\* sensorEvent | 指向传感器数据信息的指针。 |
| [Sensor\_Accuracy](capi-oh-sensor-type-h.md#sensor_accuracy) \*accuracy | 指向精度的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 如果操作成功返回**SENSOR\_SUCCESS**；否则返回[Sensor\_Result](capi-oh-sensor-type-h.md#sensor_result)中定义的错误代码。 |

### OH\_SensorEvent\_GetData()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_SensorEvent_GetData(Sensor_Event* sensorEvent, float **data, uint32_t *length)
```

**描述**

获取传感器数据。数据的长度和内容依赖于监听的传感器类型，传感器上报的数据格式如下：SENSOR\_TYPE\_ACCELEROMETER: data[0]、data[1]、data[2]分别表示设备x、y、z轴的加速度分量，单位m/s2。SENSOR\_TYPE\_GYROSCOPE: data[0]、data[1]、data[2]分别表示设备x、y、z轴的旋转角速度，单位弧度/s。SENSOR\_TYPE\_AMBIENT\_LIGHT: data[0]表示环境光强度，单位勒克斯；从api版本12开始，将返回两个额外的数据，其中data[1]表示色温，单位为开尔文；data[2]表示红外亮度，单位cd/m2。SENSOR\_TYPE\_MAGNETIC\_FIELD: data[0]、data[1]、data[2]分别表示设备x、y、z轴的地磁分量，单位微特斯拉。SENSOR\_TYPE\_BAROMETER：data[0]表示气压值，单位hPa。SENSOR\_TYPE\_HALL: data[0]表示皮套吸合状态，0表示打开，大于0表示吸附。SENSOR\_TYPE\_PROXIMITY：data[0]表示接近状态，0表示接近，大于0表示远离。SENSOR\_TYPE\_ORIENTATION:data[0]、data[1]、data[2]分别表示设备绕z、x、y轴的角度，单位度。SENSOR\_TYPE\_GRAVITY：data[0]、data[1]、data[2]分别表示设备x、y、z轴的重力加速度分量，单位m/s2。SENSOR\_TYPE\_ROTATION\_VECTOR:data[0]、data[1]、data[2]分别表示设备x、y、z轴的旋转角度，单位度，data[3]表示旋转向量元素。SENSOR\_TYPE\_PEDOMETER\_DETECTION:data[0]表示几步检测状态，1表示检测到了步数变化。SENSOR\_TYPE\_PEDOMETER:data[0]表示步数。SENSOR\_TYPE\_HEART\_RATE：data[0]表示心率数值。SENSOR\_TYPE\_LINEAR\_ACCELERATION：从api版本13开始支持。data[0]，data[1]，data[2]，表示分别绕设备的x、y、z轴的线性加速度，单位为m/s2。SENSOR\_TYPE\_GAME\_ROTATION\_VECTOR：从api版本13支持。data[0]，data[1]和data[2]，表示设备分别围绕x、y、z轴的旋转角度，单位为度。data[3]表示旋转向量。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Sensor\_Event](capi-sensor-sensor-event.md)\* sensorEvent | 传感器数据信息。 |
| float \*\*data | 出参，传感器数据。 |
| uint32\_t \*length | 出参，数组长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 如果操作成功返回**SENSOR\_SUCCESS**；否则返回[Sensor\_Result](capi-oh-sensor-type-h.md#sensor_result)中定义的错误代码。 |

### OH\_Sensor\_CreateSubscriptionId()

PhonePC/2in1TabletTVWearable

```
1. Sensor_SubscriptionId *OH_Sensor_CreateSubscriptionId(void)
```

**描述**

创建一个[Sensor\_SubscriptionId](capi-sensor-sensor-subscriptionid.md)实例。

**起始版本：** 11

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Sensor\_SubscriptionId \*](capi-sensor-sensor-subscriptionid.md) | 如果操作成功，返回指向[Sensor\_SubscriptionId](capi-sensor-sensor-subscriptionid.md)实例的指针;否则返回**NULL**。 |

### OH\_Sensor\_DestroySubscriptionId()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Sensor_DestroySubscriptionId(Sensor_SubscriptionId *id)
```

**描述**

销毁[Sensor\_SubscriptionId](capi-sensor-sensor-subscriptionid.md)实例并回收内存。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Sensor\_SubscriptionId](capi-sensor-sensor-subscriptionid.md) \*id | 指向[Sensor\_SubscriptionId](capi-sensor-sensor-subscriptionid.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 如果操作成功返回**SENSOR\_SUCCESS**；否则返回[Sensor\_Result](capi-oh-sensor-type-h.md#sensor_result)中定义的错误代码。 |

### OH\_SensorSubscriptionId\_GetType()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_SensorSubscriptionId_GetType(Sensor_SubscriptionId* id, Sensor_Type *sensorType)
```

**描述**

获取传感器类型。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Sensor\_SubscriptionId](capi-sensor-sensor-subscriptionid.md)\* id | 指向传感器订阅ID的指针。 |
| [Sensor\_Type](capi-oh-sensor-type-h.md#sensor_type) \*sensorType | 指向传感器类型的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 如果操作成功返回**SENSOR\_SUCCESS**；否则返回[Sensor\_Result](capi-oh-sensor-type-h.md#sensor_result)中定义的错误代码。 |

### OH\_SensorSubscriptionId\_SetType()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_SensorSubscriptionId_SetType(Sensor_SubscriptionId* id, const Sensor_Type sensorType)
```

**描述**

设置传感器类型。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Sensor\_SubscriptionId](capi-sensor-sensor-subscriptionid.md)\* id | 指向传感器订阅ID的指针。 |
| [const Sensor\_Type](capi-oh-sensor-type-h.md#sensor_type) sensorType | 要设置的传感器类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 如果操作成功返回**SENSOR\_SUCCESS**；否则返回[Sensor\_Result](capi-oh-sensor-type-h.md#sensor_result)中定义的错误代码。 |

### OH\_Sensor\_CreateSubscriptionAttribute()

PhonePC/2in1TabletTVWearable

```
1. Sensor_SubscriptionAttribute *OH_Sensor_CreateSubscriptionAttribute(void)
```

**描述**

创建[Sensor\_SubscriptionAttribute](capi-sensor-sensor-subscriptionattribute.md)实例。

**起始版本：** 11

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Sensor\_SubscriptionAttribute \*](capi-sensor-sensor-subscriptionattribute.md) | 如果操作成功，返回指向[Sensor\_SubscriptionAttribute](capi-sensor-sensor-subscriptionattribute.md)实例的指针；否则返回**NULL**。 |

### OH\_Sensor\_DestroySubscriptionAttribute()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Sensor_DestroySubscriptionAttribute(Sensor_SubscriptionAttribute *attribute)
```

**描述**

销毁[Sensor\_SubscriptionAttribute](capi-sensor-sensor-subscriptionattribute.md)实例并回收内存。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Sensor\_SubscriptionAttribute](capi-sensor-sensor-subscriptionattribute.md) \*attribute | 指向[Sensor\_SubscriptionAttribute](capi-sensor-sensor-subscriptionattribute.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 如果操作成功返回**SENSOR\_SUCCESS**；否则返回[Sensor\_Result](capi-oh-sensor-type-h.md#sensor_result)中定义的错误代码。 |

### OH\_SensorSubscriptionAttribute\_SetSamplingInterval()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_SensorSubscriptionAttribute_SetSamplingInterval(Sensor_SubscriptionAttribute* attribute, const int64_t samplingInterval)
```

**描述**

设置传感器数据报告间隔。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Sensor\_SubscriptionAttribute](capi-sensor-sensor-subscriptionattribute.md)\* attribute | 指向传感器订阅属性的指针。 |
| const int64\_t samplingInterval | 要设置的数据报告间隔，以纳秒为单位。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 如果操作成功返回**SENSOR\_SUCCESS**；否则返回[Sensor\_Result](capi-oh-sensor-type-h.md#sensor_result)中定义的错误代码。 |

### OH\_SensorSubscriptionAttribute\_GetSamplingInterval()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_SensorSubscriptionAttribute_GetSamplingInterval(Sensor_SubscriptionAttribute* attribute, int64_t *samplingInterval)
```

**描述**

获取传感器数据报告间隔。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Sensor\_SubscriptionAttribute](capi-sensor-sensor-subscriptionattribute.md)\* attribute | 指向传感器订阅属性的指针。 |
| int64\_t \*samplingInterval | 指向数据报告间隔的指针，以纳秒为单位。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 如果操作成功返回**SENSOR\_SUCCESS**；否则返回[Sensor\_Result](capi-oh-sensor-type-h.md#sensor_result)中定义的错误代码。 |

### Sensor\_EventCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*Sensor_EventCallback)(Sensor_Event *event)
```

**描述**

定义用于报告传感器数据的回调函数。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Sensor\_Event](capi-sensor-sensor-event.md)\* event | 指向传感器数据信息的指针。 |

### OH\_Sensor\_CreateSubscriber()

PhonePC/2in1TabletTVWearable

```
1. Sensor_Subscriber *OH_Sensor_CreateSubscriber(void)
```

**描述**

创建一个[Sensor\_Subscriber](capi-sensor-sensor-subscriber.md)实例。

**起始版本：** 11

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Sensor\_Subscriber \*](capi-sensor-sensor-subscriber.md) | 如果操作成功，返回指向[Sensor\_Subscriber](capi-sensor-sensor-subscriber.md)实例的指针;否则返回**NULL**。 |

### OH\_Sensor\_DestroySubscriber()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Sensor_DestroySubscriber(Sensor_Subscriber *subscriber)
```

**描述**

销毁[Sensor\_Subscriber](capi-sensor-sensor-subscriber.md)实例并回收内存。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Sensor\_Subscriber](capi-sensor-sensor-subscriber.md) \*subscriber | 指向[Sensor\_Subscriber](capi-sensor-sensor-subscriber.md)实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 如果操作成功返回**SENSOR\_SUCCESS**；否则返回[Sensor\_Result](capi-oh-sensor-type-h.md#sensor_result)中定义的错误代码。 |

### OH\_SensorSubscriber\_SetCallback()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_SensorSubscriber_SetCallback(Sensor_Subscriber* subscriber, const Sensor_EventCallback callback)
```

**描述**

设置一个回调函数来报告传感器数据。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Sensor\_Subscriber](capi-sensor-sensor-subscriber.md)\* subscriber | 指向传感器订阅者信息的指针。 |
| [const Sensor\_EventCallback](capi-oh-sensor-type-h.md#sensor_eventcallback) callback | 设置回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 如果操作成功返回**SENSOR\_SUCCESS**；否则返回[Sensor\_Result](capi-oh-sensor-type-h.md#sensor_result)中定义的错误代码。 |

### OH\_SensorSubscriber\_GetCallback()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_SensorSubscriber_GetCallback(Sensor_Subscriber* subscriber, Sensor_EventCallback *callback)
```

**描述**

获取用于报告传感器数据的回调函数。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Sensor\_Subscriber](capi-sensor-sensor-subscriber.md)\* subscriber | 指向传感器订阅者信息的指针。 |
| [Sensor\_EventCallback](capi-oh-sensor-type-h.md#sensor_eventcallback) \*callback | 指向回调函数的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 如果操作成功返回**SENSOR\_SUCCESS**；否则返回[Sensor\_Result](capi-oh-sensor-type-h.md#sensor_result)中定义的错误代码。 |
