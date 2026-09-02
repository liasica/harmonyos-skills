---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-scheduling-optimization-8h
title: scheduling_optimization.h
breadcrumb: API参考 > 系统 > 基础功能 > FAST Kit（算法加速服务） > C API > 头文件和结构体 > 头文件 > scheduling_optimization.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:06+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2f63492ca0b468f5c25f24d99b9f947ab585748aa2f2d2c2b4099219805f6b9a
---

## 概述

允许应用程序向系统提供性能场景信息，系统将据此在API生效范围内尽可能优化应用性能，从而提升用户体验。

**说明** 

1. perfHint只是应用向系统发送的性能优化提示，系统收到提示后会综合考量整机CPU负载、系统温度等因素进行决策，**不保证一定进行性能提升**。
2. **性能提示仅当应用在前台运行时才会生效**，应用切换到后台后提示将失效。
3. 上报线程ID提升QoS优先级不能与QoS API混用。

**引用文件：** <FASTKit/scheduling\_optimization.h>

**库：** libscheduling\_optimization.z.so

**系统能力：** SystemCapability.FAST.SchedulingOptimization

**起始版本：** 26.0.0

**相关模块：** [FAST](fast-kit-fast.md)

## 汇总

### 类型定义

| 名称 | 描述 |
| --- | --- |
| typedef struct HMS\_FAST\_PerfHintConfigBuilder HMS\_FAST\_PerfHintConfigBuilder | 系统性能优化配置参数构建器。 |
| typedef struct HMS\_FAST\_PerfHintConfig HMS\_FAST\_PerfHintConfig | 系统性能优化配置参数。 |

### 枚举

| 名称 | 描述 |
| --- | --- |
| [HMS\_FAST\_SchedulingOptimization\_SceneType](fast-kit-fast.md#hms_fast_schedulingoptimization_scenetype) {  HMS\_FAST\_APP\_LAUNCH = 1,  HMS\_FAST\_PAGE\_TRANSITION = 2,  HMS\_FAST\_PAGE\_LOAD = 3,  HMS\_FAST\_NETWORK\_FILE\_PROCESSING = 4,  HMS\_FAST\_LOCAL\_FILE\_PROCESSING = 5,  HMS\_FAST\_PAGE\_DRAWING = 6,  HMS\_FAST\_ANIMATION = 7,  HMS\_FAST\_MEDIA\_PLAYBACK = 8,  HMS\_FAST\_MEDIA\_ENCODING\_AND\_DECODING = 9  } | 需要系统性能优化的场景类型。 |
| [HMS\_FAST\_SchedulingOptimization\_SceneState](fast-kit-fast.md#hms_fast_schedulingoptimization_scenestate) {  HMS\_FAST\_END = 0,  HMS\_FAST\_BEGIN = 1  } | 需要系统性能优化的场景状态。 |
| [HMS\_FAST\_SchedulingOptimization\_DurationType](fast-kit-fast.md#hms_fast_schedulingoptimization_durationtype) {  HMS\_FAST\_SHORT = 1,  HMS\_FAST\_MEDIUM = 2,  HMS\_FAST\_LONG = 3  } | 需要系统性能优化的持续时间选项。 |
| [HMS\_FAST\_SchedulingOptimization\_ErrorCode](fast-kit-fast.md#hms_fast_schedulingoptimization_errorcode) {  HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_SUCCESS = 0,  HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_HIGH\_SYSTEM\_LOAD = 1027700001,  HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_POWER\_SAVING\_MODE = 1027700002,  HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_LOW\_POWER\_MODE = 1027700003,  HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_NON\_FRONTEND = 1027700004,  HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_INTERVAL = 1027700005,  HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_EXECUTE\_ERROR = 1027700006,  HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_INVALID\_PARAM = 1027700007,  HMS\_FAST\_ERR\_SCHEDULING\_OPTIMIZATION\_NO\_MEMORY = 1027700008  } | 系统性能优化的错误码。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [HMS\_FAST\_SchedulingOptimization\_ErrorCode](fast-kit-fast.md#hms_fast_schedulingoptimization_errorcode) [HMS\_FAST\_PerfHintConfigBuilder\_Create](fast-kit-fast.md#hms_fast_perfhintconfigbuilder_create) (HMS\_FAST\_PerfHintConfigBuilder\*\* builder) | 创建构建器实例。 |
| void [HMS\_FAST\_PerfHintConfigBuilder\_Destroy](fast-kit-fast.md#hms_fast_perfhintconfigbuilder_destroy) (HMS\_FAST\_PerfHintConfigBuilder\* builder) | 销毁构建器。 |
| [HMS\_FAST\_SchedulingOptimization\_ErrorCode](fast-kit-fast.md#hms_fast_schedulingoptimization_errorcode) [HMS\_FAST\_PerfHintConfigBuilder\_SetSceneType](fast-kit-fast.md#hms_fast_perfhintconfigbuilder_setscenetype) (HMS\_FAST\_PerfHintConfigBuilder\* builder, HMS\_FAST\_SchedulingOptimization\_SceneType sceneType) | 设置需要系统性能优化的场景类型。 |
| [HMS\_FAST\_SchedulingOptimization\_ErrorCode](fast-kit-fast.md#hms_fast_schedulingoptimization_errorcode) [HMS\_FAST\_PerfHintConfigBuilder\_SetSceneState](fast-kit-fast.md#hms_fast_perfhintconfigbuilder_setscenestate) (HMS\_FAST\_PerfHintConfigBuilder\* builder, HMS\_FAST\_SchedulingOptimization\_SceneState sceneState) | 设置需要系统性能优化的场景状态。 |
| [HMS\_FAST\_SchedulingOptimization\_ErrorCode](fast-kit-fast.md#hms_fast_schedulingoptimization_errorcode) [HMS\_FAST\_PerfHintConfigBuilder\_SetDurationType](fast-kit-fast.md#hms_fast_perfhintconfigbuilder_setdurationtype) (HMS\_FAST\_PerfHintConfigBuilder\* builder, HMS\_FAST\_SchedulingOptimization\_DurationType durationType) | 设置需要系统性能优化的持续时间选项。 |
| [HMS\_FAST\_SchedulingOptimization\_ErrorCode](fast-kit-fast.md#hms_fast_schedulingoptimization_errorcode) [HMS\_FAST\_PerfHintConfigBuilder\_SetTids](fast-kit-fast.md#hms_fast_perfhintconfigbuilder_settids) (HMS\_FAST\_PerfHintConfigBuilder\* builder, int\* tids, uint32\_t tidsSize) | 设置需要优化的线程ID。 |
| [HMS\_FAST\_SchedulingOptimization\_ErrorCode](fast-kit-fast.md#hms_fast_schedulingoptimization_errorcode) [HMS\_FAST\_PerfHintConfigBuilder\_Build](fast-kit-fast.md#hms_fast_perfhintconfigbuilder_build) (HMS\_FAST\_PerfHintConfigBuilder\* builder, HMS\_FAST\_PerfHintConfig\*\* config) | 创建系统性能优化配置参数。 |
| void [HMS\_FAST\_PerfHintConfig\_Destroy](fast-kit-fast.md#hms_fast_perfhintconfig_destroy) (HMS\_FAST\_PerfHintConfig\* config) | 销毁系统性能优化配置参数。 |
| [HMS\_FAST\_SchedulingOptimization\_ErrorCode](fast-kit-fast.md#hms_fast_schedulingoptimization_errorcode) [HMS\_FAST\_SchedulingOptimization\_PerfHint](fast-kit-fast.md#hms_fast_schedulingoptimization_perfhint) (const HMS\_FAST\_PerfHintConfig\* config) | 系统性能优化接口。 |
