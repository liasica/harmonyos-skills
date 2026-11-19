---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-gameperformance-set-touch-area
title: 设置游戏触控区域（ArkTS）
breadcrumb: 指南 > 应用服务 > Game Service Kit（游戏服务） > 游戏场景感知（可选） > 开发指导（ArkTS） > 设置游戏触控区域（ArkTS）
category: harmonyos-guides
scraped_at: 2026-11-19T09:48:58+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:0ac9343c0d393d1d1d50eca66951d5796ca3c9a85c3c37c5884e89641afb6c3c
---

从API版本26.0.1开始，游戏场景感知服务支持触控区域优化设置触控区域能力。通过传入游戏触控区域信息，优化游戏跟手性，提升游戏触控响应速度。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/fBNtmjAlQ-OU_ioJ6GnkZQ/zh-cn_image_0000002820526309.png?HW-CC-KV=V1&HW-CC-Date=20261119T014803Z&HW-CC-Expire=31536000000&HW-CC-Sign=51E76E092FDB436EF7BBA245286740A79EB0346B79CD9E763AE598A518AC53A7)

1. 游戏启动后调用[gamePerformance.init()](../harmonyos-references/gameservice-gameperformance.md#gameperformanceinit)接口对游戏场景感知进行初始化。
2. 初始化成功后，游戏调用[gamePerformance.updateGameInfo()](../harmonyos-references/gameservice-gameperformance.md#gameperformanceupdategameinfo)接口向游戏场景感知上报游戏触控信息。
3. 游戏场景感知服务根据接收到的游戏上报的触控信息设置触控区域。

## 接口说明

具体API说明详见[接口文档](../harmonyos-references/gameservice-gameperformance.md)。

| 接口名 | 描述 |
| --- | --- |
| [init](../harmonyos-references/gameservice-gameperformance.md#gameperformanceinit)(gamePackageInfo: GamePackageInfo): Promise<void> | 游戏初始化接口，对游戏场景感知进行初始化，通过Promise对象获取返回值。 |
| [updateGameInfo](../harmonyos-references/gameservice-gameperformance.md#gameperformanceupdategameinfo)<T extends BaseGameInfo>(gameInfo: T): Promise<void> | 更新游戏信息接口，主要用于上报游戏信息（包信息、配置信息、场景信息、网络信息和游戏触控信息等），通过Promise对象获取返回值。 |

## 接入步骤

### 导入模块

导入Game Service Kit及公共模块。

```typescript
import { gamePerformance } from '@kit.GameServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
```

### 初始化

导入相关模块后，需先调用[init()](../harmonyos-references/gameservice-gameperformance.md#gameperformanceinit)接口对游戏场景感知进行初始化。

**说明** 

init接口是调用其他接口的前提，如果未初始化或初始化失败，将无法调用其他接口。

```typescript
let gamePackageInfo: gamePerformance.GamePackageInfo = {
  messageType: 0,
  bundleName: 'com.example.demo', // 仅示例，请替换为实际的游戏包名
  appVersion: '1.0'
};
try {
  gamePerformance.init(gamePackageInfo).then(() => {
    // 初始化成功
    hilog.info(0x0001, 'demo', `Succeeded in initializing.`);
  });
} catch (error) {
  // 初始化失败
  let err = error as BusinessError;
  hilog.error(0x0001, 'demo', `Failed to initialize. Code: ${err.code}, message: ${err.message}`);
}
```

### 上报游戏触控信息

初始化成功后，可以通过调用[updateGameInfo()](../harmonyos-references/gameservice-gameperformance.md#gameperformanceupdategameinfo)接口上报游戏触控信息，提升游戏触控响应速度。

```typescript
let gameTouchArea: gamePerformance.GameTouchArea = {
  areaShape: gamePerformance.GameTouchAreaShape.RECTANGLE,
  coordinateType: gamePerformance.GameTouchAreaCoordinateType.NORMALIZED,
  xMin: 0.0,
  xMax: 1.0,
  yMin: 0.8,
  yMax: 1
};
let gameTouchInfo: gamePerformance.GameTouchInfo = {
  touchAreas: [gameTouchArea],
  messageType: 5
};
try {
  gamePerformance.updateGameInfo(gameTouchInfo).then(() => {
    console.info(`Update game touch info succeeded.`);
    this.logText = 'Update game touch info succeeded.'
  });
} catch (err) {
  let error = err as BusinessError;
  console.error(`Update game touch info failed. errCode is ${error.code}, errMessage is ${error.message}`);
  this.logText = `Update game touch info failed. errCode is ${error.code}, errMessage is ${error.message}`;
}
```

**说明** 

如果发生折叠屏幕切换/屏幕旋转等事件，需要重新设置热区。

## 使用HiSmartPerf验证收益

您可以使用[HiSmartPerf](../AppGallery-connect-Guides/smartperf-tool-0000001873208929.md)工具查看游戏设置触控区域前后的性能变化，验证设置触控区域的收益。

1. 安装HiSmartPerf工具并完成准备工作，详情请参见[准备工作](../AppGallery-connect-Guides/smartperf-tool-preparation-0000001530990002.md)。
2. 点击“游戏性能分析 > CPU Trace”，进入CPU Trace页面设置trace采集配置。设置完成后点击“开始采集”，分别采集设置触控区域前后，在游戏内点击相同区域时的trace信息。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/mtDKZpvuTYWXz4doEsPIwA/zh-cn_image_0000002820406309.png?HW-CC-KV=V1&HW-CC-Date=20261119T014803Z&HW-CC-Expire=31536000000&HW-CC-Sign=A1C7D89C50D0C4B15DBE7B3516A30420F3E6C1986C1AD37637737692ECE6A022)
3. 采集结束后，点击“查看Trace”查看采集的trace文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/gbjAaU-JT7yQZZRKsomMog/zh-cn_image_0000002791726330.png?HW-CC-KV=V1&HW-CC-Date=20261119T014803Z&HW-CC-Expire=31536000000&HW-CC-Sign=CB3BF2361DE21C4FB1B57CCAEBF9BD3D0971166C8C852443C4A458CDD86F7360)
4. 在trace文件内搜索“thp”，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/wZXGWRBHSh6A_2D8VSr3Ig/zh-cn_image_0000002791566358.png?HW-CC-KV=V1&HW-CC-Date=20261119T014803Z&HW-CC-Expire=31536000000&HW-CC-Sign=3E4FCD932737B58191B96B1BF6199E3973C03FB8B0544AE389502D900B52A52B)打开对应的进程，并点击thp旁的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/wD4f5U_nQaazp7UjJpaJ-A/zh-cn_image_0000002820526311.png?HW-CC-KV=V1&HW-CC-Date=20261119T014803Z&HW-CC-Expire=31536000000&HW-CC-Sign=B3A06960AD67ED4BE17D3FA1954ADB6938C6324DCF323492693CC2BD83EBE606)进行标记。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/B8tY70DqTX-Jfc_RULjyCA/zh-cn_image_0000002820406311.png?HW-CC-KV=V1&HW-CC-Date=20261119T014803Z&HW-CC-Expire=31536000000&HW-CC-Sign=118FB9A15E97F2956A9D7C1CE3906284F73DFFA07568883F7B0C3C235E43294C)
5. 在trace文件内搜索“aptouch\_daemon”，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/svqwzUH8Qja6lk-ww2kypA/zh-cn_image_0000002791566358.png?HW-CC-KV=V1&HW-CC-Date=20261119T014803Z&HW-CC-Expire=31536000000&HW-CC-Sign=F226F2EC891A0EC3A0EE2E39955DB1F5A87CAEE033D84E0F136D47BEEEAF475B)打开对应的进程，并点击aptouch\_daemon旁的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/9aE9MqJ_T9u0gvWJJs1YZw/zh-cn_image_0000002820526311.png?HW-CC-KV=V1&HW-CC-Date=20261119T014803Z&HW-CC-Expire=31536000000&HW-CC-Sign=30832D88959381B7860C94A5A8A290221A8D81C74A8E3D63BC749F925E392BF5)进行标记。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/onOB6EoHSI2ffI7KUfvA7Q/zh-cn_image_0000002791726332.png?HW-CC-KV=V1&HW-CC-Date=20261119T014803Z&HW-CC-Expire=31536000000&HW-CC-Sign=D9EF345E0AF5D7CABB39597323C5D99A5FE7EF77464E74DB45848E7898ED66DB)
6. 在trace文件内搜索“mmi\_service”，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/cSXrSG1rTVGlCghURZBGrg/zh-cn_image_0000002791566358.png?HW-CC-KV=V1&HW-CC-Date=20261119T014803Z&HW-CC-Expire=31536000000&HW-CC-Sign=32AD855A9B382A4837723C869455AF39FE9F8FE1CACB07598FD47C3160FE68B2)打开对应的进程，并点击mmi\_service旁的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/NO-GjW8ST02G3qz7rhXqyg/zh-cn_image_0000002820526311.png?HW-CC-KV=V1&HW-CC-Date=20261119T014803Z&HW-CC-Expire=31536000000&HW-CC-Sign=DB92073CD6A52F751F9979E6B29360966376A2B7FFE04F660129318DD3D503E4)进行标记。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/nlpP4EO2RziZaQB0Af4MsA/zh-cn_image_0000002791566360.png?HW-CC-KV=V1&HW-CC-Date=20261119T014803Z&HW-CC-Expire=31536000000&HW-CC-Sign=0DAB53E081F96CC4CF8364F573BD335C34BEFCCC90F8AE2EEC189BBFF99386E5)
7. 展开测试游戏的包名，并点击游戏包名和touchEventDispatch旁的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/r61KEazUS0-l5uvdry1rtQ/zh-cn_image_0000002820526311.png?HW-CC-KV=V1&HW-CC-Date=20261119T014803Z&HW-CC-Expire=31536000000&HW-CC-Sign=A5F8D442A01B51BD682733E3C335D088A568A38420198217C3DAD646223F4F64)进行标记。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/s7MQbiu1SCK9as2jJIwGsg/zh-cn_image_0000002820526313.png?HW-CC-KV=V1&HW-CC-Date=20261119T014803Z&HW-CC-Expire=31536000000&HW-CC-Sign=A6398AEEB1B5BD0796583B833E5103B3805A8385AD9DD8DC361DDDFFB8BF6B3E)
8. 通过对比设置触控区域前后从出现thp信号到mmi响应的时间，即可验证设置触控区域的效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/-SaZ03QqS4-5cZAtezsnSw/zh-cn_image_0000002820406313.png?HW-CC-KV=V1&HW-CC-Date=20261119T014803Z&HW-CC-Expire=31536000000&HW-CC-Sign=632FABB6EF39D2F47BE0A460E524EAD65A6EB368B2FA76A1E481D16C97CDB423)
