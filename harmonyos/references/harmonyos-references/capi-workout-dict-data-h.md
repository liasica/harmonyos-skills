---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-workout-dict-data-h
title: workout_dict_data.h
breadcrumb: API参考 > 应用服务 > Health Service Kit（运动健康服务） > C API > 头文件 > workout_dict_data.h
category: harmonyos-references
scraped_at: 2026-11-12T09:57:21+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:aa646d9d419df3c84957fd7592be49b415877b53a330326bd7954964e0097284
---

## 概述

提供应用与穿戴设备进行运动数据交互的能力，如实时传输心率、卡路里等运动数据。

**引用文件：** <HealthServiceKit/workout\_dict\_data.h>

**库：** libworkout\_dict\_data\_ndk.so

**系统能力：** SystemCapability.Health.HealthService.Lite

**起始版本：** 26.0.1

**相关模块：** [Workout](capi-workout.md)

## 汇总

### 函数

| 名称 | 描述 |
| --- | --- |
| [int32\_t HMS\_Workout\_GetDictData(char\* userBuffer, uint32\_t userBufferSize, uint32\_t \*actualSize)](capi-workout-dict-data-h.md#hms_workout_getdictdata) | 获取穿戴设备记录的用户的运动数据，如心率、卡路里等。 |
| [int32\_t HMS\_Workout\_SetDictData(const char \*userBuffer, uint32\_t userBufferSize)](capi-workout-dict-data-h.md#hms_workout_setdictdata) | 应用向穿戴设备提供经算法处理后产生的数据。 |

## 函数说明

### HMS\_Workout\_GetDictData()

```c
int32_t HMS_Workout_GetDictData(char* userBuffer, uint32_t userBufferSize, uint32_t *actualSize)
```

**描述**

获取穿戴设备记录的用户的运动数据，如心率、卡路里等。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| char\* userBuffer | 运动数据字段的缓存。作为输出参数，不可为空，输出为JSON格式，字符串采用UTF-8编码。  当前仅支持羽毛球、网球、匹克球、笼式网球，字段内容具体如下：  羽毛球：[{"dataType": { "id": 50004 },"time": 1782869193,"fields": {"activeTime": 100,"aerobicTrainingStress": 3,"anaerobicTrainingStress": 3,"heartRate": 80,"duration": 100,"totalCalories": 100,"activeCalorie": 50,"avgShotSpeed": 50,"maxShotSpeed": 198,"shots": 1500,"maxContinuousRally": 421,"forehandStroke": 700,"backhandStroke": 600,"overhandStroke": 700,"underhandStroke": 300,"smash": 100,"highClear": 100}}]  网球：[{"dataType": { "id": 50004 },"time": 1782869193,"fields": {"activeTime": 100,"aerobicTrainingStress": 3,"anaerobicTrainingStress": 3,"heartRate": 80,"duration": 100,"totalCalories": 100,"activeCalorie": 50,"forehand": 200,"backhand": 300,"swingTimes": 400,"maxContinuousRally": 500}}]  匹克球：[{"dataType": { "id": 50004 },"time": 1782869193,"fields": {"activeTime": 100,"aerobicTrainingStress": 3,"anaerobicTrainingStress": 3,"heartRate": 80,"duration": 100,"totalCalories": 100,"activeCalorie": 50,"forehand": 200,"backhand": 300,"swingTimes": 400,"maxContinuousRally": 500}}]  笼式网球：[{"dataType": { "id": 50004 },"time": 1782869193,"fields": {"activeTime": 100,"aerobicTrainingStress": 3,"anaerobicTrainingStress": 3,"heartRate": 80,"duration": 100,"totalCalories": 100,"activeCalorie": 50,"serve": 50,"avgShotSpeed": 80,"maxShotSpeed": 100,"forehand": 100,"bandeja": 100,"vibora": 100,"forehandSmash": 100,"forehandDrop": 100,"forehandBajada": 100,"forehandDrive": 100,"forehandBackspin": 80,"forehandVolley": 100,"backhand": 100,"backhandSmash": 100,"backhandBajada": 100,"backhandDrop": 100,"backhandDrive": 100,"backhandBackspin": 100,"backhandVolley": 100,"swingTimes": 100,"maxContinuousRally": 100,"movementDistance": 100,"setsWon": 3,"totalSets": 5}}] |
| uint32\_t userBufferSize | 运动数据字段的缓存长度，包含末尾空字符。作为输入参数，长度取值范围为(0,actualSize]。 |
| uint32\_t \*actualSize | 运动数据字段的实际长度，包含末尾空字符。作为输出参数，不可为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 获取成功返回0，获取失败返回401。  失败原因包括：userBuffer为空、userBufferSize为0或缓存长度小于实际所需长度、actualSize为空。 |

### HMS\_Workout\_SetDictData()

```c
int32_t HMS_Workout_SetDictData(const char *userBuffer, uint32_t userBufferSize)
```

**描述**

应用向穿戴设备提供经算法处理后产生的数据。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*userBuffer | 运动数据字段的缓存。作为输入参数，不可为空，输入为JSON格式，字符串采用UTF-8编码。  当前仅支持羽毛球、网球、匹克球、笼式网球，字段内容具体如下：  羽毛球：[{"dataType": { "id": 50004 },"time": 1782869193,"fields": {"avgShotSpeed": 50,"maxShotSpeed": 198,"shots": 1500,"maxContinuousRally": 421,"forehandStroke": 700,"backhandStroke": 600,"overhandStroke": 700,"underhandStroke": 300,"smash": 100,"highClear": 100}}]  网球：[{"dataType": { "id": 50004 },"time": 1782869193,"fields": {"forehand": 200,"backhand": 300,"swingTimes": 400,"maxContinuousRally": 500}}]  匹克球：[{"dataType": { "id": 50004 },"time": 1782869193,"fields": {"forehand": 200,"backhand": 300,"swingTimes": 400,"maxContinuousRally": 500}}]  笼式网球：[{"dataType": { "id": 50004 },"time": 1782869193,"fields": {"serve": 50,"avgShotSpeed": 80,"maxShotSpeed": 100,"forehand": 100,"bandeja": 100,"vibora": 100,"forehandSmash": 100,"forehandDrop": 100,"forehandBajada": 100,"forehandDrive": 100,"forehandBackspin": 80,"forehandVolley": 100,"backhand": 100,"backhandSmash": 100,"backhandBajada": 100,"backhandDrop": 100,"backhandDrive": 100,"backhandBackspin": 100,"backhandVolley": 100,"swingTimes": 100,"maxContinuousRally": 100,"movementDistance": 100,"setsWon": 3,"totalSets": 5}}] |
| uint32\_t userBufferSize | 运动数据字段的缓存长度，包含末尾空字符。作为输入参数，长度取值范围为(0,4096]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 成功返回0，获取失败返回401。  失败原因包括：userBuffer为空、userBufferSize为0或超过4096字节。 |
