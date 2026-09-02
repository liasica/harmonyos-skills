---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/free-flow-faqs-1
title: 应用接续任务失败
breadcrumb: FAQ > 多设备场景 > 自由流转 > 应用接续任务失败
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:68ac7dd7c386c96758080a3b9c84e6fb2624674cc448d59541581ae6c6a20112
---

## 问题现象

当使用应用接续时，目标设备已显示带有接续标志的应用图标，此时点击目标设备上的应用图标，没有在目标设备上成功拉起应用，并提示接续失败。

## 背景知识

* [应用接续](../best-practices/bpta-continue-cast.md)，指当用户在一个设备上操作某个应用时，可以在另一个设备的同一个应用中快速切换，并无缝衔接上一个设备的应用体验。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/71bWrp-vTCiAL_pjhLEfrQ/zh-cn_image_0000002628552418.png "点击放大")
* [DistributedSchedule错误码](../harmonyos-references/errorcode-distributedschedule.md)为分布式调度特有错误码。

## 问题定位

关键Hilog报错日志行如下：

```screen
05-16 09:19:30.572  5028 39439 E C05708/distributedsched/CommAdapter: SoftBusSocketGetError# getsockopt fd=59, errno=Permission denied, ret=-1
05-16 09:19:30.581  2898  2915 I C01334/com.ohos.sceneboard/Mission: [mission_continue_stub.cpp:42]NOTIFY_CONTINUATION_RESULT result: 16300501
05-16 09:19:30.581  2898  2915 I C01334/com.ohos.sceneboard/Mission: [distributed_mission_manager.cpp:2090]called. result = 16300501
05-16 09:19:30.581  2898  2915 I C01334/com.ohos.sceneboard/Mission: [distributed_mission_manager.cpp:2124]end
05-16 09:19:30.582  2898  2898 I C01334/com.ohos.sceneboard/Mission: [distributed_mission_manager.cpp:2046]uv_queue_work
05-16 09:19:30.582  2898  2898 I C01334/com.ohos.sceneboard/Mission: [distributed_mission_manager.cpp:2023]start
05-16 09:19:30.582  2898  2898 I C01334/com.ohos.sceneboard/Mission: [distributed_mission_manager.cpp:2052]resultCode: 16300501
05-16 09:19:30.582  5028  5172 I C04170/distributedsched/DSched_Service: DSchedContinueManager::HandleContinueEnd begin, continue info: SrcDevId: 9efa******aad7 SrcBundle: com.example.app DstDevId: b8f9******a1c9 DstBundle: com.example.app ContiType: EntryAbility MissionId: 0.
05-16 09:19:30.583  2898  2898 W A01B01/com.ohos.sceneboard/HOME: ContinuableViewModel --> continueMission fail, code: 16300501, app: com.example.app
```

* 从日志第1行得知SoftBusSocketGetError（软总线套接字获取失败），错误原因显示权限被拒绝。
* 从日志第9行得知接续任务失败，错误码为16300501，系统服务工作异常会报此错误码，可能原因如下：
  + DMS服务没有正常启动。
  + DMS的binder对象无法正常获取。
  + 流转依赖的其他服务没有正常启动或者binder对象无法获取。

## 分析结论

由背景知识得知，应用接续任务需要软总线服务支持，而此次应用运行过程中，软总线套接字因权限问题获取失败，导致接续任务失败，错误码16300501。

## 修改建议

参考应用接续开发指导中[权限申请模块](../best-practices/bpta-continue-cast.md#section157187257261)申请所需权限：

1. 声明ohos.permission.DISTRIBUTED\_DATASYNC权限，详见[声明权限](../harmonyos-guides/declare-permissions.md)。
2. 由于ohos.permission.DISTRIBUTED\_DATASYNC权限需要用户授权，应用需在首次启动、或进入接续页面时弹窗向用户申请授权，详见[向用户申请授权](../harmonyos-guides/request-user-authorization.md)。

## 常见FAQ

Q：HarmonyOS系统的华为PC是否支持应用接续？

A：支持应用接续，同时需要满足应用接续的[约束与限制](../best-practices/bpta-continue-cast.md#section157187257261)。
