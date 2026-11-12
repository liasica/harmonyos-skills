---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-retrieve-process-memory-info
title: 获取进程内存信息
breadcrumb: 最佳实践 > 性能 > 性能分析 > 分析内存占用问题 > 获取进程内存信息
category: best-practices
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:44086cf098496e793ad847d045797767c4b85071dc091056e4ee099665b0423b
---

## 通过HiDumper查看内存信息

开发者可以通过以下步骤，获取到当前应用的内存信息。

1. 打开示例应用，运行 hdc shell "hidumper -s WindowManagerService -a '-a'"获取到当前应用的pid。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/KFFJ8L4KT6Cz84AIuMEMZw/zh-cn_image_0000002404045153.png?HW-CC-KV=V1&HW-CC-Date=20261112T233140Z&HW-CC-Expire=31536000000&HW-CC-Sign=B529B841FFA2D72AB133EBA6311BFEBFC36B2CD9FABBA3FE80FA0EDACE662003 "点击放大")
2. 输入 hdc shell "hidumper --mem [Pid]" ，并将命令中的 [Pid] 换成当前应用的Pid，就可以获取到示例应用的内存信息了

一般情况下，开发者只需要关注PSS （Proportional Set Size，实际使用物理内存）Total一列的数据，即示例应用实际使用的物理内存。如下图所示，应用总共占用了26279KB的内存，主要包括ArkTS Heap（ArkTS堆内存）的4712KB以及Native Heap的13164KB。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/ckVT2LlIQjyjaa9ZpFL2pA/zh-cn_image_0000002370565324.png?HW-CC-KV=V1&HW-CC-Date=20261112T233140Z&HW-CC-Expire=31536000000&HW-CC-Sign=ED64C88E73E686213FCA0ECEEE61BF37ACF897E348B53B758D37D16B35CBBDBD "点击放大")

## 通过代码获取应用内存信息

开发者可使用[@ohos.hidebug (Debug调试)](../harmonyos-references/js-apis-hidebug.md)接口获取应用进程的内存信息，使用指导详见[获取内存信息](../harmonyos-guides/hidebug-guidelines.md#获取内存信息)。

## 使用onMemoryLevel()监听内存变化

[onMemoryLevel](../doccenter-references/api/js-apis-app-ability-abilitystage.md#onmemorylevel)是HarmonyOS提供监听系统内存变化的接口，开发者可以通过onMemoryLevel()监听内存变化，从而调整应用的内存。onMemoryLevel()回调包括三种方式，分别为[AbilityStage](../harmonyos-references/js-apis-app-ability-abilitystage.md#abilitystage)、[Ability.onMemoryLevel](../harmonyos-references/js-apis-app-ability-ability.md#abilityonmemorylevel)、[EnvironmentCallback](../doccenter-references/api/js-apis-app-ability-environmentcallback.md#environmentcallback)。

* AbilityStage：当HAP中的代码首次被加载到进程中的时候，系统会先创建AbilityStage实例，系统决定调整内存时，再回调AbilityStage实例的onMemoryLevel()方法。

* UIAbility：Ability是UIAbility的基类，在Ability中，提供系统内存变化的回调方法。
* EnvironmentCallback：EnvironmentCallback模块提供应用上下文ApplicationContext对系统环境变化监听回调的能力。

MemoryLevel分为MEMORY\_LEVEL\_MODERATE、MEMORY\_LEVEL\_LOW和MEMORY\_LEVEL\_CRITICAL三种。其中，MEMORY\_LEVEL\_MODERATE代表当前系统内存压力适中，应用可以正常运行而不会受到太大影响，MEMORY\_LEVEL\_LOW代表当前系统的内存已经比较低了，应用应该释放不必要的内存资源，避免造成系统卡顿，MEMORY\_LEVEL\_CRITICAL代表当前所剩的系统内存非常紧张，应用应该尽可能释放更多的资源，以确保系统的稳定性和性能。开发人员应该根据不同的内存级别来采取相应的措施，如释放资源、优化内存使用等，以确保应用在不同内存状态下都能正常运行。MemoryLevel具体等级定义如下所示：

**表1** onMemoryLevel等级定义

| 等级 | 值 | 说明 |
| --- | --- | --- |
| MEMORY\_LEVEL\_MODERATE | 0 | 系统内存适中。系统可能会开始根据LRU缓存规则杀死进程。 |
| MEMORY\_LEVEL\_LOW | 1 | 系统内存比较低。此时应释放不必要的资源以提升系统性能。 |
| MEMORY\_LEVEL\_CRITICAL | 2 | 系统内存很低。此时应当尽可能地去释放任何不必要的资源，因为系统可能会终止所有缓存中的进程，并且开始杀掉应当保持运行的进程，比如后台运行的服务。 |

**说明** 

后台已冻结的应用，AbilityStage、UIAbility、EnvironmentCallback的onMemoryLevel都不可以进行回调。
