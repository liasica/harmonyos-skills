---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-gameperformance-set-touch-area-c
title: 设置游戏触控区域（C/C++）
breadcrumb: 指南 > 应用服务 > Game Service Kit（游戏服务） > 游戏场景感知（可选） > 开发指导（C/C++） > 设置游戏触控区域（C/C++）
category: harmonyos-guides
scraped_at: 2026-11-19T09:48:58+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:22ad7e938ce283db47a03c59094945bbc521c18b8f16bd688df0e802c97a9500
---

从API版本26.0.1开始，游戏场景感知服务支持触控区域优化设置触控区域能力。通过传入游戏触控区域信息，优化游戏跟手性，提升游戏触控响应速度。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/8jyxfv1JRvqYvYyuf9ZlZA/zh-cn_image_0000002820526309.png?HW-CC-KV=V1&HW-CC-Date=20261119T014804Z&HW-CC-Expire=31536000000&HW-CC-Sign=D04156AD479A58F7E8E4C0A6E5CDA24AD81AC5ABA1BB15AE0254B6B0CA56C4DF)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/gwvc2P0dS2WFjPSGEAZfBg/zh-cn_image_0000002820406309.png?HW-CC-KV=V1&HW-CC-Date=20261119T014804Z&HW-CC-Expire=31536000000&HW-CC-Sign=46D8B2D183A72CC44D4922C0A4F9F41595D09375C397ED1ADDB25091F3BCE894)
3. 采集结束后，点击“查看Trace”查看采集的trace文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/DGCwkmZqTxCld16R-7oTGg/zh-cn_image_0000002791726330.png?HW-CC-KV=V1&HW-CC-Date=20261119T014804Z&HW-CC-Expire=31536000000&HW-CC-Sign=06E151FD6EDA89F7660C57A6DF6A658B1E651E3FE5942529AB56B67D0FF05B72)
4. 在trace文件内搜索“thp”，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/9hvCtaY7SjW_QUHUxqnMUA/zh-cn_image_0000002791566358.png?HW-CC-KV=V1&HW-CC-Date=20261119T014804Z&HW-CC-Expire=31536000000&HW-CC-Sign=2B69FE4A282FFD600C6C9BEF92CB16A4F55CD2BC762738868B1388A71EAB981D)打开对应的进程，并点击thp旁的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/SABG07LFQIqxAPeyD-HEdg/zh-cn_image_0000002820526311.png?HW-CC-KV=V1&HW-CC-Date=20261119T014804Z&HW-CC-Expire=31536000000&HW-CC-Sign=AA691BAF40D2199471AF70CBBF328989D2FDACE21BA74B136E45A48D773319F8)进行标记。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/4Pc7QvzIQF6-is2pH1TwYw/zh-cn_image_0000002820406311.png?HW-CC-KV=V1&HW-CC-Date=20261119T014804Z&HW-CC-Expire=31536000000&HW-CC-Sign=BF1FA6428C6198E74912EFF1BA2694EA241F9B9E087516F6F72CFA41034E73B0)
5. 在trace文件内搜索“aptouch\_daemon”，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/BJypaRENQcujg9cH_kvqjw/zh-cn_image_0000002791566358.png?HW-CC-KV=V1&HW-CC-Date=20261119T014804Z&HW-CC-Expire=31536000000&HW-CC-Sign=5E6FBFB614812E41DEAA79CFA536DEA50A7019CD051E5D29F7A0BFA596F6F351)打开对应的进程，并点击aptouch\_daemon旁的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/A2pW4eukStG0pEC6tbazmQ/zh-cn_image_0000002820526311.png?HW-CC-KV=V1&HW-CC-Date=20261119T014804Z&HW-CC-Expire=31536000000&HW-CC-Sign=5C38FC1B9A875D0A1C18739DD569FBF7280DA0ADB9A9B0A761374312C7937F91)进行标记。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/9T1oyrSRQueCpLdE1ZjfNw/zh-cn_image_0000002791726332.png?HW-CC-KV=V1&HW-CC-Date=20261119T014804Z&HW-CC-Expire=31536000000&HW-CC-Sign=BA9F6081BD20B9EF286B07526D7BA949854AC4ECB73B9843CD5C60FBD1BFC7FF)
6. 在trace文件内搜索“mmi\_service”，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/GFnEdqFMQFCD5DL3QIs3VA/zh-cn_image_0000002791566358.png?HW-CC-KV=V1&HW-CC-Date=20261119T014804Z&HW-CC-Expire=31536000000&HW-CC-Sign=835960A0735504316AA439461C6BC9238DAF1D467B96DEA75AD794DF5707194B)打开对应的进程，并点击mmi\_service旁的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/Tqnpq7swTeymVDKiu0hIiw/zh-cn_image_0000002820526311.png?HW-CC-KV=V1&HW-CC-Date=20261119T014804Z&HW-CC-Expire=31536000000&HW-CC-Sign=8ADD4D7A8A4EF2817D70809A93E9C827BA8049A650107E9E2BA753CCE8329462)进行标记。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/uWLzrCywTqKceisr7MjTmg/zh-cn_image_0000002791566360.png?HW-CC-KV=V1&HW-CC-Date=20261119T014804Z&HW-CC-Expire=31536000000&HW-CC-Sign=5E0E51901F83A8628BEC4D107EB105D9D9C5A9CBCBF47705DE0A7B211DF37BF0)
7. 展开测试游戏的包名，并点击游戏包名和touchEventDispatch旁的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/pUiKGQZORD6H8Jo1-90xqQ/zh-cn_image_0000002820526311.png?HW-CC-KV=V1&HW-CC-Date=20261119T014804Z&HW-CC-Expire=31536000000&HW-CC-Sign=734D0AC56A1F5A9C11E23381267B16516755DF4E5FA56FD4EE3B2052E8DCFA10)进行标记。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/k0p1HJPTQ3OiNWHjmNHvLw/zh-cn_image_0000002820526313.png?HW-CC-KV=V1&HW-CC-Date=20261119T014804Z&HW-CC-Expire=31536000000&HW-CC-Sign=391A8084FA6820C90551D905BB84009D2D3CBBC112F0E07CB31EA8DAED58A59B)
8. 通过对比设置触控区域前后从出现thp信号到mmi响应的时间，即可验证设置触控区域的效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/tLa7t8vNR-eML14zp7Qgbw/zh-cn_image_0000002820406313.png?HW-CC-KV=V1&HW-CC-Date=20261119T014804Z&HW-CC-Expire=31536000000&HW-CC-Sign=43326297A28DA0AD46C26B402C5177C2E35FE8E0457C9CB4933D5E9917263189)
