---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-retrieve-process-memory-info
title: 获取进程内存信息
breadcrumb: 最佳实践 > 性能 > 性能分析 > 分析内存占用问题 > 获取进程内存信息
category: best-practices
scraped_at: 2026-04-29T14:13:24+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:cc4b12b77ff7dfdf434df85544f606c5d2ba2e6d8d60e38530556d86e5d2584e
---

## 通过HiDumper查看内存信息

开发者可以通过以下步骤，获取到当前应用的内存信息。

1. 打开示例应用，运行 hdc shell "hidumper -s WindowManagerService -a '-a'"获取到当前应用的pid。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/rwQ_-ByMT1y2HywkWZosJw/zh-cn_image_0000002404045153.png?HW-CC-KV=V1&HW-CC-Date=20260429T061323Z&HW-CC-Expire=86400&HW-CC-Sign=AB1EE7B80A969CBD187D7397D28AB36926947AE04B922AC0E8DF9B470BCB5DE3 "点击放大")
2. 输入 hdc shell "hidumper --mem [Pid]" ，并将命令中的 [Pid] 换成当前应用的Pid，就可以获取到示例应用的内存信息了

一般情况下，开发者只需要关注PSS （Proportional Set Size，实际使用物理内存）Total一列的数据，即示例应用实际使用的物理内存。如下图所示，应用总共占用了26279KB的内存，主要包括ArkTS Heap（ArkTS堆内存）的4712KB以及Native Heap的13164KB。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/qFg-DxivTuig2FbyJdQ3rA/zh-cn_image_0000002370565324.png?HW-CC-KV=V1&HW-CC-Date=20260429T061323Z&HW-CC-Expire=86400&HW-CC-Sign=B1E04CD496490C3B3F89424957AD97A05A8E399D90D58406E94A1CCF4C5A8948 "点击放大")

## 通过代码获取应用内存信息

开发者可使用[@ohos.hidebug (Debug调试)](../harmonyos-references/js-apis-hidebug.md)接口获取应用进程的内存信息，使用指导详见[获取内存信息](../harmonyos-guides/hidebug-guidelines.md#获取内存信息)。

## 使用onMemoryLevel()监听内存变化

onMemoryLevel()是HarmonyOS提供监听系统内存变化的接口，开发者可以通过onMemoryLevel()监听内存变化，从而调整应用的内存。onMemoryLevel()回调包括三种方式，分别为[AbilityStage](../harmonyos-references/js-apis-app-ability-abilitystage.md#abilitystage)、[UIAbility](../harmonyos-references/js-apis-app-ability-ability.md#abilityonmemorylevel)、[EnvironmentCallback](../harmonyos-references/js-apis-app-ability-environmentcallback.md)。

* AbilityStage：当HAP中的代码首次被加载到进程中的时候，系统会先创建AbilityStage实例，系统决定调整内存时，再回调AbilityStage实例的onMemoryLevel()方法。

* UIAbility：Ability是UIAbility的基类，在Ability中，提供系统内存变化的回调方法。
* EnvironmentCallback：EnvironmentCallback模块提供应用上下文ApplicationContext对系统环境变化监听回调的能力。

MemoryLevel分为MEMORY\_LEVEL\_MODERATE、MEMORY\_LEVEL\_LOW和MEMORY\_LEVEL\_CRITICAL三种。其中，MEMORY\_LEVEL\_MODERATE代表当前系统内存压力适中，应用可以正常运行而不会受到太大影响，MEMORY\_LEVEL\_LOW代表当前系统的内存已经比较低了，应用应该释放不必要的内存资源，避免造成系统卡顿，MEMORY\_LEVEL\_CRITICAL代表当前所剩的系统内存非常紧张，应用应该尽可能释放更多的资源，以确保系统的稳定性和性能。开发人员应该根据不同的内存级别来采取相应的措施，如释放资源、优化内存使用等，以确保应用在不同内存状态下都能正常运行。MemoryLevel具体等级定义如下所示：

**表1** onMemoryLevel等级定义

| 等级 | 值 | 说明 |
| --- | --- | --- |
| MEMORY\_LEVEL\_MODERATE | 0 | 系统内存适中。系统可能会开始根据LRU缓存规则杀死进程。 |
| MEMORY\_LEVEL\_LOW | 1 | 系统内存比较低。此时应该去释放掉一些不必要的资源以提升系统的性能。 |
| MEMORY\_LEVEL\_CRITICAL | 2 | 系统内存很低。此时应当尽可能地去释放任何不必要的资源，因为系统可能会杀掉所有缓存中的进程，并且开始杀掉应当保持运行的进程，比如后台运行的服务。 |

说明

后台已冻结的应用，AbilityStage、UIAbility、EnvironmentCallback的onMemoryLevel都不可以进行回调。
