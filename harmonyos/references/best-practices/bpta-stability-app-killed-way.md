---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-app-killed-way
title: 应用被查杀类问题分析方法
breadcrumb: 最佳实践 > 稳定性 > 稳定性分析 > 应用异常退出类问题分析方法 > 应用被查杀类问题分析方法
category: best-practices
scraped_at: 2026-04-28T08:22:59+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:b78a67690b381dc4ad7712be1cc489e508cfdfb56ca52f8c8b1f970b30c672c5
---

## 日志获取

目前应用可以通过两种方式感知到应用被异常查杀

1. 元能力提供的Ability的onCreate回调参数中来获取到查杀原因。具体来说就是LaunchParam启动参数中的LastExitReason字段，请参考[LastExitReason](../harmonyos-references/js-apis-app-ability-abilityconstant.md#lastexitreason)。
2. 通过HiAppEvent订阅APP\_KILLED事件，订阅后就能在收到的回调函数中解析出查杀原因（如LowMemoryKill、OomKiller等），请参考[应用查杀事件介绍](../harmonyos-guides/hiappevent-watcher-app-killed-events.md)。

## 分析思路和分析步骤

1. 通过Ability的onCreate回调参数中获取查杀原因

   根据LastExitReason的不同取值，可参考下表采取对应处理策略：

   | **LastExitReason(enum**) | 产生原因 | 处理策略 |
   | --- | --- | --- |
   | APP\_FREEZE | 由于watchdog检测出应用冻屏故障，导致应用程序退出。 | 通过HiAppEvent订阅[应用冻屏事件](../harmonyos-guides/freeze-events.md)，到应用冻屏事件中去匹配。 |
   | RESOURCE\_CONTROL | CPU高负载。 | 尝试降低应用自身的CPU负载。 |
   | 快速CPU负载检测。 | 尝试降低应用自身的CPU负载。 |
   | I/O管控。 | 尝试降低应用自身的IO用量。 |
   | 应用内存超限劣化。 | 尝试通过HiAppEvent订阅RESOURCE\_OVERLIMIT获取更多日志。 |
   | 温度管控。 | 尝试降低应用自身的CPU负载。 |
   | 整机低内存触发按优先级由低到高查杀。 | 尝试降低应用自身的内存占用，以减少被整机查杀策略选中的概率。 |
2. 通过使用HiAppEvent订阅APP\_KILLED事件

   通过APP\_KILLED事件，能获取到查杀原因、应用前后台信息等关键信息，可以对照如下表进行处理

   | reason（string） | 产生原因 | 处理策略 | 是否应用自身异常触发管控 | 是否有关联事件 | 是否会查杀前台应用 |
   | --- | --- | --- | --- | --- | --- |
   | LowMemoryKill | 同前面的lastExitMessage值为Memory Pressure场景，即整机低内存触发按优先级由低到高查杀 | 尝试降低应用自身的内存占用，以减少被整机查杀策略选中的概率 | 否 | 否 | 是 |
   | SwapFull | Swap交换空间接近占满，可能存在个别进程内存泄漏，或者是后台进程个数太多 | 尝试降低应用自身的内存占用，以减少被整机查杀策略选中的概率 | 否 | 否 | 否 |
   | ResourceLeak(IonLeak) | 应用占用的ION内存超标 | 尝试通过HiAppEvent订阅RESOURCE\_OVERLIMIT获取更多的ION内存日志，找到泄漏点后，降低应用自身的ION内存占用，一般来说是Image组件或者Pixmap泄漏导致 | 是 | 是  （RESOURCE\_OVERLIMIT） | 是 |
   | ResourceLeak(GpuRsLeak) | 应用的ArkUI组件在render\_service服务进程占用的GPU内存超标 | 尝试降低应用ArkUI组件的GPU内存占用（例如使用image组件绘制超大图，使用autoResize优化内存占用） | 是 | 否 | 是 |
   | ResourceLeak(GpuLeak) | 应用在本进程内占用的GPU内存（即自渲染产生的GPU内存）超标 | 尝试通过HiAppEvent订阅RESOURCE\_OVERLIMIT获取更多的GPU内存日志，找到泄漏点后，降低应用自渲染（使用XComponent组件）的GPU内存占用 | 是 | 是  （RESOURCE\_OVERLIMIT） | 是 |
   | ResourceLeak(AshmemLeak) | 应用占用的ashmem内存超标 | 尝试通过HiAppEvent订阅RESOURCE\_OVERLIMIT获取更多的ashmem内存日志，找到泄漏点后，降低应用自身的ashmem内存占用，一般来说是Image组件或者Pixmap泄漏导致 | 是 | 是  （RESOURCE\_OVERLIMIT） | 是 |
   | IllegalAudioRendererBySuspend | 未申请合理的后台任务，但是后台有大量音频播放 | 应用退至后台时，应避免不必要的后台音频播放，或者合理使用后台任务，具体参考[后台任务开发服务](../harmonyos-guides/background-task-kit.md) | 是 | 否 | 否 |
   | PowerSaveClean | 整机切换到省电模式或应急模式 | 无需处理 | 否 | 否 | 否 |
   | RssThresholdKiller | 应用的RSS内存超一定阈值 | 尝试降低应用自身的内存占用，避免出现RSS内存超过阈值的情况 | 是 | 否 | 是 |
   | OomKiller | 整机低内存触发了内核按一定策略进行应用查杀 | 尝试降低应用自身的内存占用，以减少被整机查杀策略选中的概率 | 否 | 否 | 是 |
   | CpaKiller | DRM(Digital Right Management)业务申请内存但是内存不足时，会按照一定策略查杀进程以回收内存 | 尝试降低应用自身的内存占用，以减少被整机查杀策略选中的概率 | 否 | 否 | 是 |
