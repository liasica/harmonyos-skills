---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-gameperformance-set-touch-area-c
title: 设置游戏触控区域（C/C++）
breadcrumb: 指南 > 应用服务 > Game Service Kit（游戏服务） > 游戏场景感知（可选） > 开发指导（C/C++） > 设置游戏触控区域（C/C++）
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:24+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:4da636f54917de210befaca17b0a7228e3dd94789f3eb2c1e45e9998a845668a
---

从API版本26.0.1开始，游戏场景感知服务支持触控区域优化设置触控区域能力。通过传入游戏触控区域信息，优化游戏跟手性，提升游戏触控响应速度。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/H__tdIFiTuOjIWso9Revsg/zh-cn_image_0000002815399799.png)

1. 游戏启动后调用[HMS\_GamePerformance\_Init()](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_init)接口对游戏场景感知进行初始化。
2. 初始化成功后，游戏调用[HMS\_GamePerformance\_UpdateTouchInfo()](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_updatetouchinfo)接口向游戏场景感知上报游戏触控信息。
3. 游戏场景感知服务根据接收到的游戏上报的触控信息设置触控区域。

## 接口说明

具体API说明详见[GamePerformance](../harmonyos-references/gameservice-game-performance.md)。

| 接口名 | 描述 |
| --- | --- |
| [HMS\_GamePerformance\_Init()](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_init) | 游戏初始化接口，对游戏场景感知进行初始化。 |
| [HMS\_GamePerformance\_UpdateTouchInfo()](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_updatetouchinfo) | 更新游戏触控信息接口，用于上报游戏触控信息。 |

## 接入步骤

### 在 CMake 脚本中链接动态库

```c
target_include_directories(entry PUBLIC ${HMOS_SDK_NATIVE}/sysroot/usr/include)
target_link_directories(entry PUBLIC ${HMOS_SDK_NATIVE}/sysroot/usr/lib/aarch64-linux-ohos)
target_link_libraries(entry PUBLIC libgame_performance.z.so)
```

### 导入模块

导入Game Service Kit。

```c
#include <GameServiceKit/game_performance.h>
#include <cstdlib>
```

### 初始化

导入相关模块后，需先调用[HMS\_GamePerformance\_Init()](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_init)接口对游戏场景感知进行初始化。

**说明** 

HMS\_GamePerformance\_Init接口是调用其他接口的前提，如果未初始化或初始化失败，将无法调用其他接口。

```c
// 创建初始化参数
GamePerformance_InitParameters *initParameters = NULL;
HMS_GamePerformance_CreateInitParameters(&initParameters);

// 设置参数，所有SetXXX接口的第二个参数均为示例，请替换成实际参数
GamePerformance_ErrorCode appVersionSetCode =
    HMS_GamePerformance_InitParameters_SetAppVersion(initParameters, "1.0");

// 所有SetXXX接口，如果参数设置错误，将会返回错误码401；为确保参数设置无误，建议接收返回值并判断错误码
if (appVersionSetCode != GAME_PERFORMANCE_SUCCESS) {
    // 异常处理
}
HMS_GamePerformance_InitParameters_SetBundleName(initParameters, "com.example.demo");

// 初始化
GamePerformance_ErrorCode ret = HMS_GamePerformance_Init(initParameters);
if (ret != GAME_PERFORMANCE_SUCCESS) {
    // 异常处理
}

// 使用完释放内存
HMS_GamePerformance_DestroyInitParameters(&initParameters);
```

### 上报游戏触控信息

初始化成功后，可以通过调用[HMS\_GamePerformance\_UpdateTouchInfo()](../harmonyos-references/gameservice-game-performance.md#hms_gameperformance_updatetouchinfo)接口上报游戏触控信息，提升游戏触控响应速度。

```c
// 创建触控信息
GamePerformance_TouchInfo *touchInfo = NULL;
HMS_GamePerformance_CreateTouchInfo(&touchInfo);
 
// 创建触控区域1
GamePerformance_TouchArea *area1 = NULL;
HMS_GamePerformance_CreateTouchArea(&area1);
 
// 设置触控区域1形状
HMS_GamePerformance_TouchArea_SetAreaShape(area1, static_cast<GamePerformance_TouchAreaShape>(0));
// 设置触控区域1坐标类型
HMS_GamePerformance_TouchArea_SetCoordinateType(area1, static_cast<GamePerformance_TouchAreaCoordinateType>(0));
// 设置触控区域1范围
HMS_GamePerformance_TouchArea_SetBoundary(area1, 0.0, 1.0, 0.8, 1.0);
 
// 把触控区域1添加到触控信息里
HMS_GamePerformance_TouchInfo_AddTouchArea(touchInfo, area1);
 
// 创建触控区域2
GamePerformance_TouchArea *area2 = NULL;
HMS_GamePerformance_CreateTouchArea(&area2);
 
// 设置触控区域2形状
HMS_GamePerformance_TouchArea_SetAreaShape(area2, static_cast<GamePerformance_TouchAreaShape>(0));
// 设置触控区域2坐标类型
HMS_GamePerformance_TouchArea_SetCoordinateType(area2, static_cast<GamePerformance_TouchAreaCoordinateType>(0));
// 设置触控区域2范围
HMS_GamePerformance_TouchArea_SetBoundary(area2, 0.8, 1.0, 0.0, 1.0);
 
// 把触控区域2添加到触控信息里
HMS_GamePerformance_TouchInfo_AddTouchArea(touchInfo, area2);
 
// 更新触控区域
HMS_GamePerformance_UpdateTouchInfo(touchInfo);
 
// 释放内存
HMS_GamePerformance_DestroyTouchArea(&area1);
HMS_GamePerformance_DestroyTouchArea(&area2);
HMS_GamePerformance_DestroyTouchInfo(&touchInfo);
```

**说明** 

如果发生折叠屏幕切换/屏幕旋转等事件，需要重新设置热区。

## 使用HiSmartPerf验证收益

您可以使用[HiSmartPerf](../AppGallery-connect-Guides/smartperf-tool-0000001873208929.md)工具查看游戏设置触控区域前后的性能变化，验证设置触控区域的收益。

1. 安装HiSmartPerf工具并完成准备工作，详情请参见[准备工作](../AppGallery-connect-Guides/smartperf-tool-preparation-0000001530990002.md)。
2. 点击“游戏性能分析 > CPU Trace”，进入CPU Trace页面设置trace采集配置。设置完成后点击“开始采集”，分别采集设置触控区域前后，在游戏内点击相同区域时的trace信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/lFYvG86NTH6c_FdGqDZkeg/zh-cn_image_0000002786520224.png)
3. 采集结束后，点击“查看Trace”查看采集的trace文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/54zLOdQoQmyybYXdKBiprg/zh-cn_image_0000002786360296.png)
4. 在trace文件内搜索“thp”，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/0ILffuSzTmCgXEpdBl7OgA/zh-cn_image_0000002815559717.png)打开对应的进程，并点击thp旁的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/5ryrfNEyRLuO9Di9g85axg/zh-cn_image_0000002815399801.png)进行标记。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/c2pXZV-rS4W8Md5Oh3yEjg/zh-cn_image_0000002786520226.png)
5. 在trace文件内搜索“aptouch\_daemon”，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/mEfsWk6gQoyMp7Gr1kcpXA/zh-cn_image_0000002815559717.png)打开对应的进程，并点击aptouch\_daemon旁的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/UE4CufK8T5STyvSyDlDB1g/zh-cn_image_0000002815399801.png)进行标记。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/eaASjh0zTwmtiVduS34x3w/zh-cn_image_0000002786360298.png)
6. 在trace文件内搜索“mmi\_service”，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/F2jecCMGSNewe2wherD4MQ/zh-cn_image_0000002815559717.png)打开对应的进程，并点击mmi\_service旁的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/GmgDUKGrTRSssUK9lWsLwg/zh-cn_image_0000002815399801.png)进行标记。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/El7uQDbkTzSO2RLobuYchQ/zh-cn_image_0000002815559719.png)
7. 展开测试游戏的包名，并点击游戏包名和touchEventDispatch旁的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/XaKOb5X3RBGsjX6A-mcR-Q/zh-cn_image_0000002815399801.png)进行标记。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/aEp_yGiKSI-p80ngPrwwFg/zh-cn_image_0000002815399803.png)
8. 通过对比设置触控区域前后从出现thp信号到mmi响应的时间，即可验证设置触控区域的效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/DDbkOjTMQ3ma_tzbdgp_Zw/zh-cn_image_0000002786520228.png)
