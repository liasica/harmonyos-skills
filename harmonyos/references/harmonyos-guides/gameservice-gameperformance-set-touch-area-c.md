---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-gameperformance-set-touch-area-c
title: 设置游戏触控区域（C/C++）
breadcrumb: 指南 > 应用服务 > Game Service Kit（游戏服务） > 游戏场景感知（可选） > 开发指导（C/C++） > 设置游戏触控区域（C/C++）
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:24+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:3ad9bdda45d4ee16876de8b59fda16f29a2b7f19255c8222da802b4f6c9e360f
---

从API版本26.0.1开始，游戏场景感知服务支持触控区域优化设置触控区域能力。通过传入游戏触控区域信息，优化游戏跟手性，提升游戏触控响应速度。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/FedBuDC3R_CrqG2AlLuYGw/zh-cn_image_0000002793037980.png?HW-CC-KV=V1&HW-CC-Date=20261121T011056Z&HW-CC-Expire=31536000000&HW-CC-Sign=0D942F3072E6925084F1072BC1C71AAE7DA6E5D81B0FC65DE9A20D95127726F8)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/bZ89bgstS-6dzoJCxREo3A/zh-cn_image_0000002792878010.png?HW-CC-KV=V1&HW-CC-Date=20261121T011056Z&HW-CC-Expire=31536000000&HW-CC-Sign=51FCD6053E58B61C8B169FC858A74CEA0941CD2638982FEAC39BDDACCCF8B419)
3. 采集结束后，点击“查看Trace”查看采集的trace文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/ZBWCJCMRT_2-B--pm8EJeQ/zh-cn_image_0000002821837917.png?HW-CC-KV=V1&HW-CC-Date=20261121T011056Z&HW-CC-Expire=31536000000&HW-CC-Sign=03DF15CB0EF3B3C0EEAF6667BDE9AEF9E13A8FD8A7B920B68028CAE1025B0970)
4. 在trace文件内搜索“thp”，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/3iasMEBiTPWcnKmyHu8FgQ/zh-cn_image_0000002821757919.png?HW-CC-KV=V1&HW-CC-Date=20261121T011056Z&HW-CC-Expire=31536000000&HW-CC-Sign=DB18F561BE5D36E21B0FB0D49521BAE8D2DEA882AFC6452AF6F8CFB680454352)打开对应的进程，并点击thp旁的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/IYBeX5tTSBWEoUbhlwFsrA/zh-cn_image_0000002793037982.png?HW-CC-KV=V1&HW-CC-Date=20261121T011056Z&HW-CC-Expire=31536000000&HW-CC-Sign=249F5B1C5B07189E4ADAAD8D3953D224DE7FD654C758FC865E2BC084DFE64AB6)进行标记。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/UhCos30UQCCJJxLeHM28OQ/zh-cn_image_0000002792878012.png?HW-CC-KV=V1&HW-CC-Date=20261121T011056Z&HW-CC-Expire=31536000000&HW-CC-Sign=A82A036453A054DDE49027FC29F402EFF883E66BA4202A1B191A89364918C9F9)
5. 在trace文件内搜索“aptouch\_daemon”，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/R0Kiy7rrQoibLpYM1PfxxA/zh-cn_image_0000002821757919.png?HW-CC-KV=V1&HW-CC-Date=20261121T011056Z&HW-CC-Expire=31536000000&HW-CC-Sign=DDF4CB0224216674C93021F2DC33A3F5DC30ED109278E08CEBC8FA69290361A6)打开对应的进程，并点击aptouch\_daemon旁的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/8xYzSQw1RF26vVAmQ5SOQQ/zh-cn_image_0000002793037982.png?HW-CC-KV=V1&HW-CC-Date=20261121T011056Z&HW-CC-Expire=31536000000&HW-CC-Sign=79C6E341C4546DBD70254486680115649EAE319312CE670C410D14E147498491)进行标记。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/Xr_dsdLHSc6U2LCEVNY11A/zh-cn_image_0000002821837919.png?HW-CC-KV=V1&HW-CC-Date=20261121T011056Z&HW-CC-Expire=31536000000&HW-CC-Sign=F44A3966E7F323352DF756CEB240D033458E30684BDCA3FB28083E60DAD434CE)
6. 在trace文件内搜索“mmi\_service”，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/eQ-5VgGmTZKsBFEK_VqERA/zh-cn_image_0000002821757919.png?HW-CC-KV=V1&HW-CC-Date=20261121T011056Z&HW-CC-Expire=31536000000&HW-CC-Sign=BC24029284CABF251A9388C0E5BED0E06802E1EA8FD34427430A091DD164EFA6)打开对应的进程，并点击mmi\_service旁的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/sIk9St3_SgmmT04SxckUSA/zh-cn_image_0000002793037982.png?HW-CC-KV=V1&HW-CC-Date=20261121T011056Z&HW-CC-Expire=31536000000&HW-CC-Sign=FCE63464934E022C9CE76D30F1D5A698A2499AA1D5DC9D1DA6876DE6F88E4AB8)进行标记。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/RJOYUTJ_TXujDEg5HBgMgQ/zh-cn_image_0000002821757921.png?HW-CC-KV=V1&HW-CC-Date=20261121T011056Z&HW-CC-Expire=31536000000&HW-CC-Sign=AD5523B27CADC3EE72BBD679581B1A9AB7658CB09F3132DE0C16A2E53733EE11)
7. 展开测试游戏的包名，并点击游戏包名和touchEventDispatch旁的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/klvaXKB5QlO8zLPXeN7KAQ/zh-cn_image_0000002793037982.png?HW-CC-KV=V1&HW-CC-Date=20261121T011056Z&HW-CC-Expire=31536000000&HW-CC-Sign=E102099E3A6212E8BD4C266AE1EE0B90A5F44D1CACD3F914B0EBEA8AD3B97CE7)进行标记。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/obq3VCK6SeCLkbaffvNrgQ/zh-cn_image_0000002793037984.png?HW-CC-KV=V1&HW-CC-Date=20261121T011056Z&HW-CC-Expire=31536000000&HW-CC-Sign=D3E258C3DDEE343DD37379FFEA0AABA2CA3ED7FD004B1B4C38447522EE3B10A3)
8. 通过对比设置触控区域前后从出现thp信号到mmi响应的时间，即可验证设置触控区域的效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/y1VdOmNuRXqsczHEwqzaJg/zh-cn_image_0000002792878014.png?HW-CC-KV=V1&HW-CC-Date=20261121T011056Z&HW-CC-Expire=31536000000&HW-CC-Sign=3F204733320857A9760D7145FFFCC10E7B4847E374CDF264EC0A234DAAFF4374)
