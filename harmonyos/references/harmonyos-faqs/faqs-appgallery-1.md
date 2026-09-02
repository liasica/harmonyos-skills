---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-1
title: 应用前台使用时发生闪退，或在后台时退出
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 应用前台使用时发生闪退，或在后台时退出
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:50+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:58100dd246d903128f6853b27d9102c13dea5b5f68070d5a1c688a31d89a81c9
---

## 问题现象

在前台使用过程中，应用出现闪退，或是应用在后台时，程序终止。

## 背景知识

* PROCESS\_KILL是因为各种原因（如应用内存超限、运行锁异常等）导致应用被操作系统强制停止。
* 当前支持的PROCESS\_KILL问题种类可以参考[分析PROCESS KILL问题](../app/agc-help-apms-appterminate-0000002577580566.md)。
* LowMemoryKill：系统在需要内存时，会杀死应用程序和服务释放内存，优先在后台的应用程序，但如果后台程序全部清理完，依旧处于低内存状态，也会终止前台应用。
* SWAP\_FULL：SWAP交换空间接近占满，存在个别进程内存泄漏，或者是后台进程个数太多。
* ILLEGAL\_AUDIO\_RENDERER\_BY\_SUSPEND、ILLEGAL\_AUDIO\_CAPTURER\_BY\_SUSPEND：后台非法放音、后台非法录音，未申请合理的后台任务。
* [长时任务(ArkTS)](../harmonyos-guides/continuous-task.md)：应用退至后台后，在后台需要长时间运行用户可感知的任务，如播放音乐、导航等。为防止应用进程被挂起，导致对应功能异常，可以申请长时任务，使应用在后台长时间运行。

## 问题定位

1. 从faultlogger目录下查看并无带有应用包名的故障日志。
2. 从memory\_leak目录下查看并无带有应用包名的故障日志。
3. 在hilog日志下查看故障发生时间日志，搜索kill reason|kill\_reason|kill.\*【应用包名】，发现有带有应用包名的应用被终止。
   * 终止原因是：LowMemoryKill，低内存。

     priority代表终止优先级，0代表前台应用，从高到低依次终止。

     ```txt
     kill_reason=LowMemoryKill, killing proc[pid=xxx, uid=xxx, procName=com.hx.example, priority=xxx type=x], freedBuf=xxx
     ```
   * 终止原因是：StabilityCheckKill，低内存。

     StabilityCheckKill是6.0新增的memmgr终止机制，区别LowMemoryKill仅包含能快速回收的内存，可以提供给用户态使用。

     ```txt
     KillOneProcessByPid process com.hx.example has been Killed, isAncoApp=0, errno=0, pid=23348, freedSize=5391580 KB, rssKB:222888, rssAnonKB:107760, dmaKB:5164672, gpuKB=119148, pssKB=0, childrenFreedKB=0, useAmsKill=0, amsKillResult=-1, useBrokerKill=0, brokerKillResult=-1, useMemmgrKill=1, memmgrKillResult=0, reason=StabilityCheckKill
     ```
   * 终止原因是：SWAP\_FULL，虚拟内存满。

     同LowMemoryKill，根据priority，从优先级最低的应用进行终止。

     ```txt
     C02699/memmgrservice/MemMgr: KillHelper::WriteKillEvent hisysevent write result=0, send event [FRAMEWORK,PROCESS_KILL], pid=36844, processName=com.hx.example, msg=Kill reason: SWAP_FULL; Current buffer is: 1683456; Freed buffer is: 85436; Killed process [uid is: 20020277, priority is: 382, type is: 3, diffTimeMs is: 1156471], foreground=0
     ```

     参考文档[获取进程内存信息](../best-practices/bpta-retrieve-process-memory-info.md)，找到占用SWAP内存最大的应用，再通过Profiler工具中的Snapshot模板，排查是否存在可疑的泄漏对象。
   * 终止原因是：ILLEGAL\_AUDIO\_RENDERER\_BY\_SUSPEND，后台非法放音。

     ```txt
     C01713/resource_schedule_service/SUSPEND_MANAGER: [(ReportKillAppEvent):267] hisysevent write result=0, send event [FRAMEWORK,PROCESS_KILL], pid=30627, processName=com.hm.example, msg=Kill Reason:ILLEGAL_AUDIO_RENDERER_BY_SUSPEND
     ```
   * 终止原因是：ILLEGAL\_AUDIO\_CAPTURER\_BY\_SUSPEND，后台非法录音。

     ```txt
     C01713/resource_schedule_service/SUSPEND_MANAGER: [(ReportKillAppEvent):277] hisysevent write result=0, send event [FRAMEWORK,PROCESS_KILL], pid=64424, processName=com.hm.example, msg=Kill Reason:ILLEGAL_AUDIO_CAPTURER_BY_SUSPEND, foreground=0
     ```
   * 终止原因是：Power Save Clean，整机切换到省电模式或应急模式。

     ```txt
     C01336/foundation/AMS: [app_exit_reason_data_manager.cpp:220]current bundle name: com.hx.example, tokenId:<private>, reason: 6,  exitMsg: Kill Reason:Power Save Clean, abilityName:EntryAbility isSetReason:1
     ```
   * 终止原因是：CPU Highload，CPU高负载。

     ```txt
     C01716/resource_schedule_service/RESOURCE_QUOTA_CONTROL: [a92ab77a9eb01c1 0 0][KillApplication:158] hisysevent write result=0, send event [FRAMEWORK,PROCESS_KILL], uid=1000080, pid=38811, processName=com.hx.example:render, KillReason=Kill Reason:CPU Highload, Msg=, FOREGROUND=0
     ```

## 分析结论

* 终止原因是：LowMemoryKill，低内存。

  整机运行内存不足，系统在需要内存时杀死应用程序和服务。
* 终止原因是：StabilityCheckKill，低内存。

  整机运行内存不足，系统在需要内存时杀死应用程序和服务。
* 终止原因是：SWAP\_FULL，虚拟内存满。

  应用因为系统SWAP空间不足被系统终止。
* 终止原因是：ILLEGAL\_AUDIO\_RENDERER\_BY\_SUSPEND，后台非法放音。

  应用在后台非法播放音频导致被系统终止。
* 终止原因是：ILLEGAL\_AUDIO\_CAPTURER\_BY\_SUSPEND，后台非法录音。

  应用在后台非法录音导致被系统终止。
* 终止原因是：Power Save Clean，整机切换到省电模式或应急模式。

  因设备开启省电模式或应急模式，导致应用被终止，节省耗电。
* 终止原因是：CPU Highload，CPU高负载。

  CPU负载超出限制，导致应用进程被系统管控终止。

## 修改建议

* 终止原因是：LowMemoryKill，低内存。

  参考文档[分析内存占用问题](../best-practices/bpta-analyze-memory-problem.md)，找出内存占用过高的应用，再使用Snapshot和Allocation工具分析应用内存使用情况，及时释放不必要的内存资源，如需要排查是否存在内存泄漏问题，可参考[内存泄漏类问题检测方法](../best-practices/bpta-stability-memleak-detection-overview.md)。
* 终止原因是：StabilityCheckKill，低内存。

  参考文档分析内存占用问题，找出内存占用过高的应用，再使用Snapshot和Allocation工具分析应用内存使用情况，及时释放不必要的内存资源，如需要排查是否存在内存泄漏问题，可参考内存泄漏类问题检测方法。
* 终止原因是：SWAP\_FULL，虚拟内存满。

  如果后台进程个数太多且无应用内存占比过高，则是系统正常策略，可通过关闭其它应用，保持系统SWAP空间正常避免。

  如果分析出个别应用进程内存泄漏，根据相应场景，参考[资源泄漏类问题优化建议](../best-practices/bpta-stability-leak-opt.md)进行修改。
* 终止原因是：ILLEGAL\_AUDIO\_RENDERER\_BY\_SUSPEND，后台非法放音。

  参考[后台播放音乐](https://gitcode.com/HarmonyOS_Samples/video-player)中的示例，申请长时任务播放音频，禁止不操作或写入静音数据等恶意行为。
* 终止原因是：ILLEGAL\_AUDIO\_CAPTURER\_BY\_SUSPEND，后台非法录音。

  参考长时任务(ArkTS)中的示例，在开始录音时开启长时任务，在停止录音时停止长时任务。
* 终止原因是：Power Save Clean，整机切换到省电模式或应急模式。

  系统正常策略，无需修改。
* 终止原因是：CPU Highload，CPU高负载。

  降低应用自身的CPU负载，参考[CPU活动分析：CPU分析](../harmonyos-guides/ide-insight-session-cpu.md)，使用Profiler工具分析CPU资源使用情况，相关案例参考[CPU 高负载分析](../best-practices/bpta-high-cpu-load-analysis.md)。
