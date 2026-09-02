---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/appkilled-guidelines
title: App Killed（应用终止）检测
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 故障检测 > App Killed（应用终止）检测
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:10+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:8bfda97a9630791b882d9ddcbb17cd8b78f9d5070d2a5f2ecb8e83ade116c576
---

## 简介

应用闪退指应用在使用过程中突然异常终止。当应用行为异常，比如消耗过多CPU、内存等系统资源时，系统为了保持整机健康状态，会按照规则挑选应用进行管控，通常通过服务进程向应用发送SIGKILL信号（信号值是9）来实施终止的。操作系统对SIGKILL的默认行为是不生成栈日志等维测信息的，导致应用闪退时faultlogger中无日志。

## 基本概念

应用退出通常包含以下几种情况：

1. 应用自身发生异常或主动抛出异常，例如因SIGSEGV、SIGABRT触发的CPP\_CRASH异常，系统可监控并记录维测日志。
2. 用户主动终止应用，例如在任务列表中点击清理按钮以清除所有应用，或上划清除单个应用，不会生成栈等维测日志。
3. 应用开发者主动调用exit系统调用时，不会生成栈等维测日志。
4. 应用发生主线程堵塞，导致界面冻结，通常会生成APP\_FREEZE日志。
5. 资源使用过度将导致系统对应用进行管控，并提供详细的维测信息。例如，应用发生内存泄漏时，通常会生成资源泄漏类的维测日志。开发者可以通过HiAppEvent订阅RESOURCE\_OVERLIMIT获取对应的事件和日志。
6. 系统对应用进行管控时，部分场景无法提供详细的维测信息，比如LowMemoryKiller、应用的RSS内存超过4GB、快速泄漏等。

本节主要覆盖在场景5和6中因SIGKILL信号导致的应用终止。

## 实现原理

1. 内核和服务进程都会监控系统资源。
2. 发现异常后，选择应用进行管控。
3. 系统触发管控，终止应用时会添加系统事件打点。
4. 打点事件中包含uid、包名、前后台信息、终止原因和维测信息。

## 约束和限制

1. 应用需先通过HiAppEvent订阅，才能接收终止事件。
2. 终止事件以异步的方式传递给应用，应用需在下次启动时才能接收到。
3. 系统的管控行为会随着版本演进而不断新增，不保证当前的管控机制是系统的全部。

## 触发场景

系统终止应用，有以下的场景:

1. 应用的内存、CPU和IO类负载超过一定限额，文件句柄和线程数量超标。
2. 整机低内存时，会根据内存使用情况和优先级终止应用。
3. 功耗类检查，包括应用Binder调用导致频繁唤醒、音频播放或录音导致系统无法冻结、GPS或蓝牙等外设使用异常问题。

## 感知方式

应用可以通过两种方式感知到被异常终止。

1. 从元能力的Ability的onCreate回调参数中获取终止原因。具体为LaunchParam启动参数中的LastExitReason字段，请参考[元能力LastExitReason章节](../harmonyos-references/js-apis-app-ability-abilityconstant.md#lastexitreason)。
2. 通过HiAppEvent订阅APP\_KILLED事件。订阅方式请参考[应用终止事件](hiappevent-watcher-app-killed-events.md)。

## 分析思路和分析步骤

1. 从Ability的onCreate回调参数中获取终止原因。

   可以参考下表进行处理。

   | lastExitReason(enum) | lastExitMessage(string) | 产生原因 | 处理策略 |
   | --- | --- | --- | --- |
   | APP\_FREEZE | APP\_FREEZE | 由于watchdog检测出应用Freeze故障，导致应用程序退出。 | 通过HiAppEvent订阅APP\_FREEZE事件，到APP\_FREEZE事件中去匹配。 |
   | RESOURCE\_CONTROL | CPU Highload | CPU高负载。 | 尝试降低应用自身的CPU负载。 |
   | RESOURCE\_CONTROL | CPU\_EXT Highload | 快速CPU负载检测。 | 尝试降低应用自身的CPU负载。 |
   | RESOURCE\_CONTROL | IO Manager Control | I/O管控。 | 尝试降低应用自身的I/O。 |
   | RESOURCE\_CONTROL | App Memory Deterioration | 应用内存超限劣化。 | 尝试通过HiAppEvent订阅RESOURCE\_OVERLIMIT获取更多日志。 |
   | RESOURCE\_CONTROL | Temperature Control | 温度管控。 | 尝试降低应用自身的CPU负载。 |
   | RESOURCE\_CONTROL | Memory Pressure | 整机低内存触发，按优先级由低到高终止应用。 | 尝试降低应用自身的内存占用，以减少被整机管控策略选中的概率。 |
2. 通过HiAppEvent订阅APP\_KILLED事件。

   通过APP\_KILLED事件，可以获取终止原因、应用前后台等关键信息，对照下表进行处理：

   | reason(string) | 产生原因 | 处理策略 | 是否应用自身异常触发管控 | 是否有关联事件 |
   | --- | --- | --- | --- | --- |
   | LowMemoryKill | 同前面的lastExitMessage值为Memory Pressure场景，即整机低内存触发，优先级由低到高终止应用。 | 尝试降低应用自身的内存占用，以减少被整机终止策略选中的概率。 | 否 | 否 |
   | SwapFull | Swap交换空间接近占满，可能存在个别进程内存泄漏，或者是后台进程个数太多。 | 尝试降低应用自身的内存占用，以减少被整机管控策略选中的概率。 | 否 | 否 |
   | ResourceLeak(IonLeak) | 应用占用的ION内存超标。 | 尝试通过HiAppEvent订阅RESOURCE\_OVERLIMIT获取更多的ION内存日志，找到泄漏点后，降低应用自身的ION内存占用，一般来说是Image组件或者Pixmap泄漏导致。 | 是 | 是 |
   | ResourceLeak(GpuRsLeak) | 应用的ArkUI组件在render\_service服务进程占用的GPU内存超标。 | 尝试降低应用ArkUI组件的GPU内存占用。 | 是 | 否 |
   | ResourceLeak(GpuLeak) | 应用在本进程内占用的GPU内存（即自渲染产生的GPU内存）超标。 | 尝试通过HiAppEvent订阅RESOURCE\_OVERLIMIT获取更多的GPU内存日志，找到泄漏点后，降低应用自渲染（使用XComponent组件）的GPU内存占用。 | 是 | 是 |
   | ResourceLeak(AshmemLeak) | 应用占用的ashmem内存超标。 | 尝试通过HiAppEvent订阅RESOURCE\_OVERLIMIT获取更多的ashmem内存日志，找到泄漏点后，降低应用自身的ashmem内存占用，一般来说是Image组件或者Pixmap泄漏导致。 | 是 | 是 |
   | ResourceLeak(CES) | CES注册超限。 | 尝试降低应用CES注册数量。 | 是 | 否 |
   | ResourceLeak(PSSSoftLeak) | 后台应用内存占用超过检测阈值两倍，其中pss内存占比最高。 | 尝试降低应用自身的内存占用。 | 是 | 是 |
   | ResourceLeak(PSSLeak) | 后台应用内存占用超过特定阈值，其中pss内存占比最高。 | 尝试降低应用自身的内存占用。 | 是 | 是 |
   | ResourceLeak(VMALeak) | VMA泄漏。 | 尝试降低应用自身的VMA内存占用，每次调用后释放对应虚拟内存区域。 | 否 | 否 |
   | ResourceLeak(FDLeak) | FD泄漏。 | 尝试通过HiAppEvent订阅RESOURCE\_OVERLIMIT获取更多的FD泄漏日志，找到泄漏点后，及时关闭不必要的文件句柄。 | 是 | 是 |
   | ResourceLeak(ThreadLeak) | 线程泄漏。 | 尝试通过HiAppEvent订阅RESOURCE\_OVERLIMIT获取更多的线程泄漏日志，找到泄漏点后，及时销毁不必要的线程。 | 是 | 是 |
   | ResourceLeak(KernelZoneLeak) | 页表内存泄漏。 | 无需处理。 | 是 | 否 |
   | IllegalAudioRendererBySuspend | 应用的音频播放未申请合理的后台任务，其退至后台后仍有大量音频播放。 | 应用退至后台时，应避免不必要的后台音频播放，或者合理使用后台任务，具体参考[后台任务开发服务](background-task-overview.md)。 | 是 | 否 |
   | PowerSaveClean | 整机切换到省电模式或应急模式。 | 无需处理。 | 否 | 否 |
   | VrsKill | 三方应用检测到恶意进程后，调用PC端病毒检测处置服务接口终止进程。 | 无需处理。 | 否 | 否 |
   | RssThresholdKiller | 应用的RSS内存超一定阈值。 | 尝试通过HiAppEvent订阅RESOURCE\_OVERLIMIT获取更多的RSS内存日志，找到泄漏点后，尝试降低应用自身的内存占用，避免出现RSS内存超过阈值的情况。 | 是 | 是 |
   | OomKiller | 整机低内存，触发了内核管控，按照一定策略终止应用。 | 尝试降低应用自身的内存占用，以减少被整机管控策略选中的概率。 | 否 | 否 |
   | CpaKiller | DRM（Digital Rights Management）业务申请内存但是内存不足时，会按照一定策略终止进程以回收内存。 | 尝试降低应用自身的内存占用，以减少被整机管控策略选中的概率。 | 否 | 否 |
   | KillApplication | 应用主动退出。 | 无需处理。 | 否 | 否 |
   | OnRemoteDied | 远程服务死亡。 | 检查依赖的远程服务是否正常。 | 否 | 否 |
   | Restart | 应用重启。 | 无需处理。 | 否 | 否 |
   | UserRequest | 最近任务上划或清理。 | 无需处理。 | 否 | 否 |
   | Uninstall | 应用卸载退出。 | 无需处理。 | 否 | 否 |
   | Upgrade | 应用更新退出。 | 无需处理。 | 否 | 否 |
   | Logout | 用户注销时，卸载应用沙箱。 | 无需处理。 | 否 | 否 |
   | PermissionUpdate | 应用权限更新。 | 检查应用权限使用是否合理。 | 否 | 否 |
   | aaForceStop | 通过aa命令强制停止应用。 | 无需处理。 | 否 | 否 |
   | ThreadBlock6S | 应用主线程卡死超时。 | 检查应用主线程是否存在阻塞操作，优化代码逻辑。 | 是 | 是，具体参考[ThreadBlock6S](appfreeze-guidelines.md#thread_block_6s应用主线程卡死超时)。 |
   | AppInputBlock | 用户输入响应超时。 | 检查应用UI响应是否及时，优化输入处理逻辑。 | 是 | 是，具体参考[AppInputBlock](appfreeze-guidelines.md#app_input_block用户输入响应超时)。 |
   | LifecycleTimeout | 应用生命周期超时。 | 检查应用生命周期回调是否存在耗时操作。 | 是 | 否 |
   | JsError | js层程序崩溃。 | 检查js代码是否存在异常，优化错误处理。 | 是 | 是，具体参考[JsError](jscrash-guidelines.md)。 |
   | CppCrash | native层程序崩溃。 | 检查native代码是否存在异常，优化错误处理。 | 是 | 是，具体参考[CppCrash](cppcrash-guidelines.md)。 |
   | RSPixelMapFdOverLimit | 应用使用图片PixelMap资源超限导致渲染服务fd泄漏。 | 尝试降低应用使用图片pixelMap资源的频率。 | 是 | 否 |
   | CPUHighloadNotify | 应用后台CPU高负载，出现弹框，用户选择停止该应用。 | 尝试降低应用自身的CPU负载。 | 否 | 否 |
   | CPUHighloadUserRequest | 应用后台CPU高负载，设置界面用户选择停止该应用。 | 尝试降低应用自身的CPU负载。 | 否 | 否 |
   | IllegalAudioCapturerBySuspend | 应用录音未申请合理的后台任务，其退至后台后仍进行录音。 | 应用退至后台时，应避免不必要的后台录音，或者合理使用后台任务。 | 是 | 否 |
   | IOHighload | IO高负载。 | 尝试降低应用自身的I/O操作。 | 否 | 否 |
   | AppFreeze | 应用冻屏无响应。 | 通过HiAppEvent订阅APP\_FREEZE事件，到APP\_FREEZE事件中去匹配。 | 是 | 是，具体参考[AppFreeze](appfreeze-guidelines.md)。 |
   | MaliciousContinuousTaskActive | 恶意连续任务活跃。 | 检查应用是否存在恶意连续任务，优化任务调度。 | 是 | 否 |
   | RsDataOverflow | RS数据溢出。 | 尝试降低应用RS数据使用量。 | 否 | 否 |
   | HighTemperature | 温度超限。 | 尝试降低应用自身的CPU负载，减少发热。 | 否 | 否 |
   | TransientTaskTimeout | 短时任务超时6s并且处于后台。 | 检查短时任务是否存在耗时操作，优化任务执行效率。 | 是 | 否 |
   | TooManyReadyThreads | 单进程就绪线程过多。 | 尝试减少应用创建的线程数量，优化线程管理。 | 是 | 否 |
   | JsHeapSleepCleanKill | sleep状态（夜间充电）进行js heapsize检测，超限后终止应用。 | 归类为整机后台内存清理，尝试优化js heap的使用率。 | 否 | 否 |
   | HardwareDecodingResourcesLimit | 硬件解码资源限制。 | 尝试减少应用对硬件解码资源的使用。 | 否 | 否 |
   | AppRecoveryNotifyAppOverLimit | 应用恢复通知应用超限。 | 检查应用恢复机制是否存在异常，优化恢复逻辑。 | 是 | 否 |
   | GpuError | GPU错误。 | 检查应用GPU使用是否合理，优化GPU资源管理。 | 是 | 否 |
   | NotAttachedToStatusBar | 未附加到状态栏。 | 检查应用状态栏附件逻辑是否正确。 | 是 | 否 |
   | CPUHighload | 应用后台CPU高负载，系统自动终止应用。 | 尝试降低应用自身的CPU负载。 | 否 | 否 |
   | AshmemKiller | 整机低内存，单进程ASHMEM内存超限。 | 尝试降低应用自身的ashmem内存占用。尝试通过HiAppEvent订阅RESOURCE\_OVERLIMIT获取更多的ashmem内存超限日志。 | 是 | 是 |
   | GpuKiller | 整机低内存，单进程GPU占用达到阈值。 | 尝试降低应用自身的GPU内存占用。尝试通过HiAppEvent订阅RESOURCE\_OVERLIMIT获取更多的单进程GPU占用达到阈值日志。 | 是 | 是 |
   | DmaKiller | 整机低内存，单进程Dma占用达到阈值。 | 尝试降低应用自身的Dma内存占用。尝试通过HiAppEvent订阅RESOURCE\_OVERLIMIT获取更多的Dma占用达到阈值日志。 | 是 | 是 |
   | ThreadKiller | 单进程线程超限。 | 尝试减少应用创建的线程数量，优化线程管理。 | 是 | 是 |
   | UninstallStorage | 卸载存储卡。 | 无需处理。 | 否 | 否 |
