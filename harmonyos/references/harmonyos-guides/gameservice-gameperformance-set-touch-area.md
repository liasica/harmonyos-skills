---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-gameperformance-set-touch-area
title: 设置游戏触控区域（ArkTS）
breadcrumb: 指南 > 应用服务 > Game Service Kit（游戏服务） > 游戏场景感知（可选） > 开发指导（ArkTS） > 设置游戏触控区域（ArkTS）
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:23+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:a364fc20ebce6ba34419828b93dd1211185271589e2aec823f00180c45bf84d8
---

从API版本26.0.1开始，游戏场景感知服务支持触控区域优化设置触控区域能力。通过传入游戏触控区域信息，优化游戏跟手性，提升游戏触控响应速度。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/zmEHLqwiTGinLOXL4cxLdg/zh-cn_image_0000002793037980.png?HW-CC-KV=V1&HW-CC-Date=20261121T011056Z&HW-CC-Expire=31536000000&HW-CC-Sign=5F54E63A9BA619508548E171C1CEE52D0D4535CA174A124EA3CBE4F134C853AA)

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

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/LCUP-nx6SVWGWRlsRQHMTw/zh-cn_image_0000002792878010.png?HW-CC-KV=V1&HW-CC-Date=20261121T011056Z&HW-CC-Expire=31536000000&HW-CC-Sign=261864B29BC93C31B5B664064959FA83C81ABF6A38F221AC20A040788D0AD7CA)
3. 采集结束后，点击“查看Trace”查看采集的trace文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/ZLw3ARkKReKXj9KcZ7EjlA/zh-cn_image_0000002821837917.png?HW-CC-KV=V1&HW-CC-Date=20261121T011056Z&HW-CC-Expire=31536000000&HW-CC-Sign=B865F71A6CED242C599E70C91973919E9517FF706E726AF64C406D0E8B666BD6)
4. 在trace文件内搜索“thp”，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/Lh3VCDebQruRvgXlsRWGaw/zh-cn_image_0000002821757919.png?HW-CC-KV=V1&HW-CC-Date=20261121T011056Z&HW-CC-Expire=31536000000&HW-CC-Sign=CF3A26608F292741E24C9D8AAD065C261CA01A6636B23D4932B82F678E0F8A23)打开对应的进程，并点击thp旁的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/7lUxrYDyRmi9BtRjgQvktw/zh-cn_image_0000002793037982.png?HW-CC-KV=V1&HW-CC-Date=20261121T011056Z&HW-CC-Expire=31536000000&HW-CC-Sign=41E6737E8F14B8B3BC04EE3A30C50CD7281DC4A88BF1E218858FECEA7CC1B9B8)进行标记。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/6pfZ4RGgRBmJl2QSeIe43w/zh-cn_image_0000002792878012.png?HW-CC-KV=V1&HW-CC-Date=20261121T011056Z&HW-CC-Expire=31536000000&HW-CC-Sign=743C9E929143C51442609DB56626397C68A5712FB6575FC8FDE5EF385E5ED6C4)
5. 在trace文件内搜索“aptouch\_daemon”，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/emt2SZ26R_O8dOg-ELUqpg/zh-cn_image_0000002821757919.png?HW-CC-KV=V1&HW-CC-Date=20261121T011056Z&HW-CC-Expire=31536000000&HW-CC-Sign=49FE87C356388769FC6AA853EAFEF4441899A8BFD92A1B2B0E5ABC702B907252)打开对应的进程，并点击aptouch\_daemon旁的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/qlcZMXGQQRevVuRuL13ysQ/zh-cn_image_0000002793037982.png?HW-CC-KV=V1&HW-CC-Date=20261121T011056Z&HW-CC-Expire=31536000000&HW-CC-Sign=DD313E04A792A314D8B052B52454754E6EC8646B6D1B8F4957C97264DF394F62)进行标记。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/n2V3A92ISN6VZ2CNFpwNuA/zh-cn_image_0000002821837919.png?HW-CC-KV=V1&HW-CC-Date=20261121T011056Z&HW-CC-Expire=31536000000&HW-CC-Sign=9475E402500CA5A04DD6F37DC4E55936A4DF9CCBA445730F46E115552AAB3A9B)
6. 在trace文件内搜索“mmi\_service”，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/pAmPFdZdRXKLxICLsLDPfw/zh-cn_image_0000002821757919.png?HW-CC-KV=V1&HW-CC-Date=20261121T011056Z&HW-CC-Expire=31536000000&HW-CC-Sign=A1A8C5884169D8F78A5E651B8EC63FCEBFBBCA9E3E9E743DC2ADF36215F58D1E)打开对应的进程，并点击mmi\_service旁的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/mTNAd78GSKigl5pwoxvIIg/zh-cn_image_0000002793037982.png?HW-CC-KV=V1&HW-CC-Date=20261121T011056Z&HW-CC-Expire=31536000000&HW-CC-Sign=968CD29D415F2EE37F9E661A0471B6D9697AADDB375F4C99E80EB55B74965F17)进行标记。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/ruEY6EXVRjOA0quQm719oQ/zh-cn_image_0000002821757921.png?HW-CC-KV=V1&HW-CC-Date=20261121T011056Z&HW-CC-Expire=31536000000&HW-CC-Sign=F53844DAA548CC7F9A393040FD7CF583363A527044A0D45EBE96E850A12CCA45)
7. 展开测试游戏的包名，并点击游戏包名和touchEventDispatch旁的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/EoY1Bl-JT4S0PLWJyM5WdA/zh-cn_image_0000002793037982.png?HW-CC-KV=V1&HW-CC-Date=20261121T011056Z&HW-CC-Expire=31536000000&HW-CC-Sign=96147109FE297606212066BB9E25C32A537671CF09A602F7B37D537B5EA8E04D)进行标记。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/TlQbjudIRgyOJPvs1CbhmQ/zh-cn_image_0000002793037984.png?HW-CC-KV=V1&HW-CC-Date=20261121T011056Z&HW-CC-Expire=31536000000&HW-CC-Sign=A4C669041308A24D8D657F277A1D1B152ED9F9EEB03939DB17BB6236C6258590)
8. 通过对比设置触控区域前后从出现thp信号到mmi响应的时间，即可验证设置触控区域的效果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/gQGYMwq7RbevbwaxfYUKdQ/zh-cn_image_0000002792878014.png?HW-CC-KV=V1&HW-CC-Date=20261121T011056Z&HW-CC-Expire=31536000000&HW-CC-Sign=3479B56E16F273897C7D31606B00791368AC3149E62C89E9BE75040309822CF7)
