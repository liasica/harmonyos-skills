---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-gameperformance-set-touch-area
title: 设置游戏触控区域（ArkTS）
breadcrumb: 指南 > 应用服务 > Game Service Kit（游戏服务） > 游戏场景感知（可选） > 开发指导（ArkTS） > 设置游戏触控区域（ArkTS）
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:5e5337eb03e373b86cbfc0a6fa714ba2c25d41c1eb51b0501b7360d6d768d8d9
---

从API版本26.0.1开始，游戏场景感知服务支持触控区域优化设置触控区域能力。通过传入游戏触控区域信息，优化游戏跟手性，提升游戏触控响应速度。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/wK1dZAiOTeKjPtTjJxzT5g/zh-cn_image_0000002815399799.png?HW-CC-KV=V1&HW-CC-Date=20261112T233230Z&HW-CC-Expire=31536000000&HW-CC-Sign=EB8ED69ACFF8AAEDECBF8C9307DCB2535C2B4DA6810AF02FA4DE206281969AB5)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/F5hbAkpaS2SZsDzWGCF16A/zh-cn_image_0000002786520224.png?HW-CC-KV=V1&HW-CC-Date=20261112T233230Z&HW-CC-Expire=31536000000&HW-CC-Sign=963FE5CB1BA965D90946242C491E8559E0E8C9B62850F001325B7E248475B71C)
3. 采集结束后，点击“查看Trace”查看采集的trace文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/QUrtfIr7SgSLTxRuRnMIZg/zh-cn_image_0000002786360296.png?HW-CC-KV=V1&HW-CC-Date=20261112T233230Z&HW-CC-Expire=31536000000&HW-CC-Sign=6247339DFD30C62E5894F4BAE91886DAD769AC98BF4E34E7FD8E38C8556E9FE0)
4. 在trace文件内搜索“thp”，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/V---exPUT1WHg2cxicG3aA/zh-cn_image_0000002815559717.png?HW-CC-KV=V1&HW-CC-Date=20261112T233230Z&HW-CC-Expire=31536000000&HW-CC-Sign=AC9BC0123CF3302101F4A8BF0B041DDC52A759A4A5EE4A65148417546A9D0209)打开对应的进程，并点击thp旁的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/Fa04aVDCR1yWONKhxK-CIQ/zh-cn_image_0000002815399801.png?HW-CC-KV=V1&HW-CC-Date=20261112T233230Z&HW-CC-Expire=31536000000&HW-CC-Sign=78E27F6336DCCBB61F4C2D8895B630635B1D1F9E19E84883435ADBD9A443198B)进行标记。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/XZwjzMJ-S3yEnP1tQAkFJg/zh-cn_image_0000002786520226.png?HW-CC-KV=V1&HW-CC-Date=20261112T233230Z&HW-CC-Expire=31536000000&HW-CC-Sign=84253B1A251349E5E6F586B7CC9244E8A48F7735FB690D36E980AF3D7A98E3B1)
5. 在trace文件内搜索“aptouch\_daemon”，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/Ofvss_hCQ1mtrB8AIZgAQg/zh-cn_image_0000002815559717.png?HW-CC-KV=V1&HW-CC-Date=20261112T233230Z&HW-CC-Expire=31536000000&HW-CC-Sign=03216EE6ADD242B92DE80B9691839FD1B643178E3B145B0C00D8F77DB1D203C5)打开对应的进程，并点击aptouch\_daemon旁的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/LOQgXrTQTCKi5QArDA-krg/zh-cn_image_0000002815399801.png?HW-CC-KV=V1&HW-CC-Date=20261112T233230Z&HW-CC-Expire=31536000000&HW-CC-Sign=65D5C9492E599D45BCD458D4639CC525556EDFBF514C72E32309FEBD7F8738E2)进行标记。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/CsimLhN9QtO7z7lqXwTi1g/zh-cn_image_0000002786360298.png?HW-CC-KV=V1&HW-CC-Date=20261112T233230Z&HW-CC-Expire=31536000000&HW-CC-Sign=F5CF819DC149C40F8818D9B7C1999826F348F72A33CC6E3DBE0E49B14AFE3139)
6. 在trace文件内搜索“mmi\_service”，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/Cxe-CX9hSFmm1f6mUYhvnQ/zh-cn_image_0000002815559717.png?HW-CC-KV=V1&HW-CC-Date=20261112T233230Z&HW-CC-Expire=31536000000&HW-CC-Sign=A67F00D3C42E505BEB4DB23B24A75F326018671F5D0B3ABADA6372254821B602)打开对应的进程，并点击mmi\_service旁的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/hbwQcQVHRZq4p6qr64ZIiw/zh-cn_image_0000002815399801.png?HW-CC-KV=V1&HW-CC-Date=20261112T233230Z&HW-CC-Expire=31536000000&HW-CC-Sign=FCB179BDCFB8384529CBEB24F7EAEC376A7B4957F177439DE32D5C0085326BC8)进行标记。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/xVKPKNikQ5yYCtS8WRgUfg/zh-cn_image_0000002815559719.png?HW-CC-KV=V1&HW-CC-Date=20261112T233230Z&HW-CC-Expire=31536000000&HW-CC-Sign=06049855710C0B9E292C33CFA0C88FC3B70937F82A988ED22CF09B672C66829D)
7. 展开测试游戏的包名，并点击游戏包名和touchEventDispatch旁的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/W_gpkWR2S6idcrf3UHhhfQ/zh-cn_image_0000002815399801.png?HW-CC-KV=V1&HW-CC-Date=20261112T233230Z&HW-CC-Expire=31536000000&HW-CC-Sign=43381BAB48298591AD9429B7D78EDA2BD932C7025BF25FFE3668E5702F6F2857)进行标记。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/EfjVO8ZpTuWcA1hZdA-Wfw/zh-cn_image_0000002815399803.png?HW-CC-KV=V1&HW-CC-Date=20261112T233230Z&HW-CC-Expire=31536000000&HW-CC-Sign=82259D9EEAC0466EF2E7871BE0043B441EC151B7F37292FF28375ADAE332C1BC)
8. 通过对比设置触控区域前后从出现thp信号到mmi响应的时间，即可验证设置触控区域的效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/Jg54WniPSEe0NuByQ7yvyg/zh-cn_image_0000002786520228.png?HW-CC-KV=V1&HW-CC-Date=20261112T233230Z&HW-CC-Expire=31536000000&HW-CC-Sign=E1CE61C0F00BAEF1E2C5E23FD52E4747440138D33015A9EC3E0A90FC2C18CA65)
