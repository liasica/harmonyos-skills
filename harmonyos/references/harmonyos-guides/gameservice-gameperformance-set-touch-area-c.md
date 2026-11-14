---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-gameperformance-set-touch-area-c
title: 设置游戏触控区域（C/C++）
breadcrumb: 指南 > 应用服务 > Game Service Kit（游戏服务） > 游戏场景感知（可选） > 开发指导（C/C++） > 设置游戏触控区域（C/C++）
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:17+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:614435ecb189f337157bcfb8f9c2ac4dbcd408ab10bd5a21c9a628e9872a15bc
---

从API版本26.0.1开始，游戏场景感知服务支持触控区域优化设置触控区域能力。通过传入游戏触控区域信息，优化游戏跟手性，提升游戏触控响应速度。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/GSlQnkN1SkyG6uekR34RiQ/zh-cn_image_0000002817507459.png?HW-CC-KV=V1&HW-CC-Date=20261114T004634Z&HW-CC-Expire=31536000000&HW-CC-Sign=A93EB81615A07C888A4AF5638D32E2CD6B23EF2E37ACDBDD7676FFFFE9E257FE)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/DwcDpO3cSDO4ykfE5_Bpow/zh-cn_image_0000002788308028.png?HW-CC-KV=V1&HW-CC-Date=20261114T004634Z&HW-CC-Expire=31536000000&HW-CC-Sign=E143BDEF05DB9AED99AE5880B4C0D7CD27ABA6132975A512261FA6C2BCB0EE6C)
3. 采集结束后，点击“查看Trace”查看采集的trace文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/vKYP9hvXRq-pc_4jYB4vWw/zh-cn_image_0000002817427391.png?HW-CC-KV=V1&HW-CC-Date=20261114T004634Z&HW-CC-Expire=31536000000&HW-CC-Sign=13EE60E18F7EDE592870F0316DAFD8BA969E72A730ADD3BF36E340CC55E904B6)
4. 在trace文件内搜索“thp”，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/EfFgtWs-SEuyvW3mUAvVIg/zh-cn_image_0000002788467972.png?HW-CC-KV=V1&HW-CC-Date=20261114T004634Z&HW-CC-Expire=31536000000&HW-CC-Sign=D2C7DC0682442F3C09B087572A2673EB5EEF4CDEE092DDA6295894102311F57F)打开对应的进程，并点击thp旁的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/sgPkx1krQCiSHA59HPSMPg/zh-cn_image_0000002817507461.png?HW-CC-KV=V1&HW-CC-Date=20261114T004634Z&HW-CC-Expire=31536000000&HW-CC-Sign=E426777E36356E27B51DF8F94929F4C1564C31BD5C7E00183F34345E0CAB08EC)进行标记。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/MczPCpWOSJyhlu5LdjW2Gw/zh-cn_image_0000002788308030.png?HW-CC-KV=V1&HW-CC-Date=20261114T004634Z&HW-CC-Expire=31536000000&HW-CC-Sign=B02D606E6D95B96E355E38C659946F592EC30D25BACA6B58C9B23ED596895C36)
5. 在trace文件内搜索“aptouch\_daemon”，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/DfkH3WMFS4CBSxsPnnk06w/zh-cn_image_0000002788467972.png?HW-CC-KV=V1&HW-CC-Date=20261114T004634Z&HW-CC-Expire=31536000000&HW-CC-Sign=6CFF8BC8D94007D573D8BF6F41F8EF195001D1EE7F3A7A2C8AF7ED0B6BF87847)打开对应的进程，并点击aptouch\_daemon旁的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/0GihZ7D7QcuOvwwvdt_2cA/zh-cn_image_0000002817507461.png?HW-CC-KV=V1&HW-CC-Date=20261114T004634Z&HW-CC-Expire=31536000000&HW-CC-Sign=D17A4A82B3DA1EFA991D5D10076304326DE2E1109D21F8111C23A3025AB94CCF)进行标记。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/roe-xVk9Rh6GJ1wulFyCpw/zh-cn_image_0000002817427393.png?HW-CC-KV=V1&HW-CC-Date=20261114T004634Z&HW-CC-Expire=31536000000&HW-CC-Sign=6DA74718C03E62DA6735FD29F00DEE53503A245D7CA50FEB3AC1FCD72F258DB5)
6. 在trace文件内搜索“mmi\_service”，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/agEgp798RNuVAIJ6mJn7ZA/zh-cn_image_0000002788467972.png?HW-CC-KV=V1&HW-CC-Date=20261114T004634Z&HW-CC-Expire=31536000000&HW-CC-Sign=CBFE372DAEA41950CC3BA45C87F35BFBD066E23AA434D7BFF78F5D39245FA133)打开对应的进程，并点击mmi\_service旁的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/JzdkKtnaQ3iLdgfLERgBzQ/zh-cn_image_0000002817507461.png?HW-CC-KV=V1&HW-CC-Date=20261114T004634Z&HW-CC-Expire=31536000000&HW-CC-Sign=43BD590A35B3D22C3A2F421F49D2A8C4A827A31F00A3114CA7E18B210BC6FAFD)进行标记。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/8RlNMr7BTFOKBsaU4RyDrA/zh-cn_image_0000002788467974.png?HW-CC-KV=V1&HW-CC-Date=20261114T004634Z&HW-CC-Expire=31536000000&HW-CC-Sign=6198F55FCC182A13C1BD1FC0D0D717E72154AB4B23981580488EB1DB1B26294C)
7. 展开测试游戏的包名，并点击游戏包名和touchEventDispatch旁的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/eOE43oVhTE-Bz1uSw34htA/zh-cn_image_0000002817507461.png?HW-CC-KV=V1&HW-CC-Date=20261114T004634Z&HW-CC-Expire=31536000000&HW-CC-Sign=0B37B41FB6C3547573082242790678E4C35E11CCE1CF70EA3E005591C3E606A7)进行标记。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/FUSyjmxMTVOS9OcGznTGQQ/zh-cn_image_0000002817507463.png?HW-CC-KV=V1&HW-CC-Date=20261114T004634Z&HW-CC-Expire=31536000000&HW-CC-Sign=9006887357263801CE8318D00C49CE71A107E1EFCC676B055BBC2774F28CB1EF)
8. 通过对比设置触控区域前后从出现thp信号到mmi响应的时间，即可验证设置触控区域的效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/uIMrEjxRQ5mEj5ha7ASoyA/zh-cn_image_0000002788308032.png?HW-CC-KV=V1&HW-CC-Date=20261114T004634Z&HW-CC-Expire=31536000000&HW-CC-Sign=5664FC67186C5A37DE6487C60C59E88C7DC401637BEEBC739DD9F65BB424F04C)
