---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fast-scheduling-optimization_c
title: 使用perfHint系统性能优化(C/C++)
breadcrumb: 指南 > 系统 > 基础功能 > FAST Kit（算法加速服务） > perfHint系统性能优化 > 使用perfHint系统性能优化(C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:36+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:e2222a98d4efce18558b7e998a2ad10192fc1384ba715d4f6da3a53f8c7b66a9
---

从API版本26.0.0版本开始，新增支持perfHint系统性能优化特性。

perfHint(Performance Hint)是系统性能优化的简称，用于向系统提供性能场景信息。

## 场景介绍

允许应用程序向系统提供性能场景信息，系统据此在API生效范围内尽可能优化应用性能，以提升用户体验。

* 支持多种场景上报，包括应用启动、页面切换、页面加载、网络文件处理、本地文件处理、页面绘制、动效、音视频播放与媒体编解码。
* 场景状态控制：场景开始和场景结束。
* 持续时间提示：短持续时间、中等持续时间和长持续时间。支持不同的间隔要求，以提高策略差异化。各类型界定标准如下：

  + 短持续时间（[HMS\_FAST\_SHORT](../harmonyos-references/fast-kit-fast.md#hms_fast_schedulingoptimization_durationtype)）：单次最大持续时间1秒，间隔大于3秒。
  + 中等持续时间（[HMS\_FAST\_MEDIUM](../harmonyos-references/fast-kit-fast.md#hms_fast_schedulingoptimization_durationtype)）：单次最大持续时间10秒，间隔大于30秒。
  + 长持续时间（[HMS\_FAST\_LONG](../harmonyos-references/fast-kit-fast.md#hms_fast_schedulingoptimization_durationtype)）：单次最大持续时间60秒，间隔大于180秒。
* 支持同时上报多个线程。可以携带线程ID数组。

## 约束与限制

* perfHint仅作为性能优化建议，系统在综合考量整机CPU负载、系统温度、当前任务队列等因素后决定是否实施优化措施，因此**不能保证每次调用都能获得性能提升**。
* **性能提示仅当应用在前台运行时才会生效**，应用切换到后台后提示将失效。
* 通过线程ID提升QoS优先级时，请避免与QoS API混用。

## 接口说明

perfHint系统性能优化场景提供以下C接口，具体API说明详见[接口文档](../harmonyos-references/fast-kit-fast.md)。

| 接口名 | 描述 |
| --- | --- |
| [HMS\_FAST\_PerfHintConfigBuilder\_Create](../harmonyos-references/fast-kit-fast.md#hms_fast_perfhintconfigbuilder_create) | 创建构建器实例。 |
| [HMS\_FAST\_PerfHintConfigBuilder\_Destroy](../harmonyos-references/fast-kit-fast.md#hms_fast_perfhintconfigbuilder_destroy) | 销毁构建器。 |
| [HMS\_FAST\_PerfHintConfigBuilder\_SetSceneType](../harmonyos-references/fast-kit-fast.md#hms_fast_perfhintconfigbuilder_setscenetype) | 设置需要系统性能优化的场景类型。 |
| [HMS\_FAST\_PerfHintConfigBuilder\_SetSceneState](../harmonyos-references/fast-kit-fast.md#hms_fast_perfhintconfigbuilder_setscenestate) | 设置需要系统性能优化的场景状态。 |
| [HMS\_FAST\_PerfHintConfigBuilder\_SetDurationType](../harmonyos-references/fast-kit-fast.md#hms_fast_perfhintconfigbuilder_setdurationtype) | 设置需要系统性能优化的持续时间选项。 |
| [HMS\_FAST\_PerfHintConfigBuilder\_SetTids](../harmonyos-references/fast-kit-fast.md#hms_fast_perfhintconfigbuilder_settids) | 设置需要优化QoS的线程ID。 |
| [HMS\_FAST\_PerfHintConfigBuilder\_Build](../harmonyos-references/fast-kit-fast.md#hms_fast_perfhintconfigbuilder_build) | 创建系统性能优化配置参数。 |
| [HMS\_FAST\_PerfHintConfig\_Destroy](../harmonyos-references/fast-kit-fast.md#hms_fast_perfhintconfig_destroy) | 销毁系统性能优化配置参数。 |
| [HMS\_FAST\_SchedulingOptimization\_PerfHint](../harmonyos-references/fast-kit-fast.md#hms_fast_schedulingoptimization_perfhint) | 系统性能优化接口，允许应用程序向系统提供性能场景信息，系统据此在API生效范围内尽可能优化应用性能，以提升用户体验。 |

## 使用指导

应用要使用SchedulingOptimization提供的系统性能优化能力，需要添加对应的头文件。

### 在CMake脚本中链接动态库

```cmake
find_library(
    lib_scheduling_optimization
    NAMES scheduling_optimization.z
)
target_link_libraries(entry PRIVATE ${lib_scheduling_optimization})
```

### 添加头文件

需要开发者引入[scheduling\_optimization.h](../harmonyos-references/fast-kit-fast.md)头文件后，才可以使用系统性能优化相关API。

```cpp
#include "FASTKit/scheduling_optimization.h"
```

## 完整示例

应用可以通过[HMS\_FAST\_SchedulingOptimization\_PerfHint](../harmonyos-references/fast-kit-fast.md#hms_fast_schedulingoptimization_perfhint)接口进行系统性能优化。

```cpp
#include <iostream>
#include "FASTKit/scheduling_optimization.h"

void demoSchedulingOptimization()
{
    HMS_FAST_PerfHintConfigBuilder* builder = nullptr;
    HMS_FAST_PerfHintConfig* config = nullptr;
    HMS_FAST_SchedulingOptimization_ErrorCode ret;
    int tids[] = {1001, 1002};

    // 创建构建器
    ret = HMS_FAST_PerfHintConfigBuilder_Create(&builder);
    if (ret != HMS_FAST_ERR_SCHEDULING_OPTIMIZATION_SUCCESS) {
        std::cerr << "Failed to create builder, error: " << ret << std::endl;
        return;
    }

    // 设置场景类型
    ret = HMS_FAST_PerfHintConfigBuilder_SetSceneType(builder, HMS_FAST_APP_LAUNCH);
    if (ret != HMS_FAST_ERR_SCHEDULING_OPTIMIZATION_SUCCESS) {
        std::cerr << "Failed to set scene type, error: " << ret << std::endl;
        goto cleanup;
    }

    // 设置场景状态
    ret = HMS_FAST_PerfHintConfigBuilder_SetSceneState(builder, HMS_FAST_BEGIN);
    if (ret != HMS_FAST_ERR_SCHEDULING_OPTIMIZATION_SUCCESS) {
        std::cerr << "Failed to set scene state, error: " << ret << std::endl;
        goto cleanup;
    }

    // 设置持续时间类型
    ret = HMS_FAST_PerfHintConfigBuilder_SetDurationType(builder, HMS_FAST_SHORT);
    if (ret != HMS_FAST_ERR_SCHEDULING_OPTIMIZATION_SUCCESS) {
        std::cerr << "Failed to set duration type, error: " << ret << std::endl;
        goto cleanup;
    }

    // 设置线程ID（可选）
    ret = HMS_FAST_PerfHintConfigBuilder_SetTids(builder, tids, 2);
    if (ret != HMS_FAST_ERR_SCHEDULING_OPTIMIZATION_SUCCESS) {
        std::cerr << "Failed to set tids, error: " << ret << std::endl;
        goto cleanup;
    }

    // 构建配置参数
    ret = HMS_FAST_PerfHintConfigBuilder_Build(builder, &config);
    if (ret != HMS_FAST_ERR_SCHEDULING_OPTIMIZATION_SUCCESS) {
        std::cerr << "Failed to build config, error: " << ret << std::endl;
        goto cleanup;
    }

    // 执行系统性能优化
    ret = HMS_FAST_SchedulingOptimization_PerfHint(config);
    if (ret == HMS_FAST_ERR_SCHEDULING_OPTIMIZATION_SUCCESS) {
        std::cout << "Scheduling optimization performed successfully" << std::endl;
    } else {
        std::cerr << "Failed to perform scheduling optimization, error: " << ret << std::endl;
    }

cleanup:
    // 销毁配置参数
    if (config) {
        HMS_FAST_PerfHintConfig_Destroy(config);
    }

    // 销毁构建器
    if (builder) {
        HMS_FAST_PerfHintConfigBuilder_Destroy(builder);
    }
}
```
