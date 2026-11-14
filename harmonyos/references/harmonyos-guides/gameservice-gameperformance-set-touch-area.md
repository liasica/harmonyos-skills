---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-gameperformance-set-touch-area
title: 设置游戏触控区域（ArkTS）
breadcrumb: 指南 > 应用服务 > Game Service Kit（游戏服务） > 游戏场景感知（可选） > 开发指导（ArkTS） > 设置游戏触控区域（ArkTS）
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:17+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:414ca5cc025efdbb2efb3d74c51274ab353982b1b4bc533c23631979397bd769
---

从API版本26.0.1开始，游戏场景感知服务支持触控区域优化设置触控区域能力。通过传入游戏触控区域信息，优化游戏跟手性，提升游戏触控响应速度。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/3mm8K2vDQyam3FE427U46Q/zh-cn_image_0000002817507459.png?HW-CC-KV=V1&HW-CC-Date=20261114T004634Z&HW-CC-Expire=31536000000&HW-CC-Sign=A4048AF386453C963E19C13557009D483B0716A8761F9FCA18F6AF82361922EC)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/ZknqrYzpSqGcLcXKl-7vVg/zh-cn_image_0000002788308028.png?HW-CC-KV=V1&HW-CC-Date=20261114T004634Z&HW-CC-Expire=31536000000&HW-CC-Sign=8C7FE9132D5E1EA6ACDC5B82B8BC990A4FCD10C6601829768A3C31870B4F5FBB)
3. 采集结束后，点击“查看Trace”查看采集的trace文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/6hA4nZ3vTqe0SRiUlRmjHw/zh-cn_image_0000002817427391.png?HW-CC-KV=V1&HW-CC-Date=20261114T004634Z&HW-CC-Expire=31536000000&HW-CC-Sign=145D3E2553DB440AD94F1D466F5639747A7799F53E4D92D286D37475D5E9921B)
4. 在trace文件内搜索“thp”，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/oHpnwxCzS2mEgrvUjuxH-g/zh-cn_image_0000002788467972.png?HW-CC-KV=V1&HW-CC-Date=20261114T004634Z&HW-CC-Expire=31536000000&HW-CC-Sign=9BB1BB04C5B5674651406AE5FF0FED9167852C4ADBE852216E7562047FA1A86A)打开对应的进程，并点击thp旁的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/tgwdantKR1qaXgNiaUjv_A/zh-cn_image_0000002817507461.png?HW-CC-KV=V1&HW-CC-Date=20261114T004634Z&HW-CC-Expire=31536000000&HW-CC-Sign=D39C17AF7608091F47F1FFCCE412DFB126439F9B7E61489501B06511B311F041)进行标记。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/fsFxV_tBQkKuwAw6mUkDiQ/zh-cn_image_0000002788308030.png?HW-CC-KV=V1&HW-CC-Date=20261114T004634Z&HW-CC-Expire=31536000000&HW-CC-Sign=E91D1AE273BAAA22110DC20641EC7CED06D4DCA4359E95F261F4075CC5220FF3)
5. 在trace文件内搜索“aptouch\_daemon”，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/D2vVj-JcRI2_K_0L_NeEyw/zh-cn_image_0000002788467972.png?HW-CC-KV=V1&HW-CC-Date=20261114T004634Z&HW-CC-Expire=31536000000&HW-CC-Sign=70E3F0617F9DB198A509CF11D429FEFDF2498BED96055DCCB446DFB06B2DC016)打开对应的进程，并点击aptouch\_daemon旁的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/E-4EypBpSD-KCFIoLlsXvQ/zh-cn_image_0000002817507461.png?HW-CC-KV=V1&HW-CC-Date=20261114T004634Z&HW-CC-Expire=31536000000&HW-CC-Sign=1B5E6A82AA38F2B277955383477F3450E5CB55A5C10B8DDD89656B4E73BD719E)进行标记。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/Wj4yfTaFRu6gq0oDmFjTvw/zh-cn_image_0000002817427393.png?HW-CC-KV=V1&HW-CC-Date=20261114T004634Z&HW-CC-Expire=31536000000&HW-CC-Sign=16C3CA637A6145086768DEB7824D7241F5B97EA490F2EF3875F21FE0AEF2543C)
6. 在trace文件内搜索“mmi\_service”，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/EVAOLOEtS3G3Hk0F3EbCwg/zh-cn_image_0000002788467972.png?HW-CC-KV=V1&HW-CC-Date=20261114T004634Z&HW-CC-Expire=31536000000&HW-CC-Sign=AC7368BE53C69AF4481FDE2FBE1293741383B4F96A46002C8C5351DA7264A615)打开对应的进程，并点击mmi\_service旁的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/VgaLkry1Ri6cb2dUlu-yqA/zh-cn_image_0000002817507461.png?HW-CC-KV=V1&HW-CC-Date=20261114T004634Z&HW-CC-Expire=31536000000&HW-CC-Sign=F734C854E915229A22DD4C8616E7CEFF1357AAE4EAF589559455C913FCB0EC95)进行标记。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/aO3hgq5tTt-OJQSSvL0lhA/zh-cn_image_0000002788467974.png?HW-CC-KV=V1&HW-CC-Date=20261114T004634Z&HW-CC-Expire=31536000000&HW-CC-Sign=953FFD1446E06632D677B38C5E67DA2063317F9C706BE622B80905E08CEB0786)
7. 展开测试游戏的包名，并点击游戏包名和touchEventDispatch旁的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/XLhW4FNzSVC581XkZD1Gaw/zh-cn_image_0000002817507461.png?HW-CC-KV=V1&HW-CC-Date=20261114T004634Z&HW-CC-Expire=31536000000&HW-CC-Sign=80E7A60E8109E2633A06C88EE85BECD6CDB88F4BCA03FC4AFD3FCE626C3BBC2D)进行标记。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/Wy0MAfmbS-me9Bgw-N6esA/zh-cn_image_0000002817507463.png?HW-CC-KV=V1&HW-CC-Date=20261114T004634Z&HW-CC-Expire=31536000000&HW-CC-Sign=B8CD7D04960C592BAE97093183735E80431C6B8DEA58396CECFD3A5F68444EE5)
8. 通过对比设置触控区域前后从出现thp信号到mmi响应的时间，即可验证设置触控区域的效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/ClrHcs1VR26aipQlOY1CZg/zh-cn_image_0000002788308032.png?HW-CC-KV=V1&HW-CC-Date=20261114T004634Z&HW-CC-Expire=31536000000&HW-CC-Sign=153B0E26A57302A74735D618157547D040F283CBDA5ABD78B35240ED41EDBADF)
