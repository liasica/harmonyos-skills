---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-tablet-27
title: 平板横屏状态下，页面两侧出现大量黑边
breadcrumb: FAQ > 多设备场景 > 平板 > 常见问题 > 平板横屏状态下，页面两侧出现大量黑边
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:472b938cbb466c7e2a350d65e7e5ca4203a70bdc8c294b2e039431939b8e6e28
---

## 问题现象

在平板横屏状态下，播放视频两侧出现了大量黑边。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/ije4rhAoQ7W_WtfCRZJ1Qw/zh-cn_image_0000002658911557.png "点击放大")

## 背景知识

* [XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)：提供用于图形绘制和媒体数据写入的Surface，XComponent负责将其嵌入到视图中，支持应用自定义Surface位置和大小。具体指南请参考[自定义渲染 (XComponent)文档](../harmonyos-guides/napi-xcomponent-guidelines.md)。
* [on('windowSizeChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowsizechange7)：可监听窗口尺寸的变化，当窗口尺寸变化时，应用可通过改变自身的布局以适配不同的窗口尺寸。

## 问题定位

1. 使用[DevEco Testing](https://developer.huawei.com/consumer/cn/download/deveco-testing)查看页面布局，发现该页面使用了XComponent组件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/u0rSXCApRsu5yFm4PL2k5A/zh-cn_image_0000002628392338.png)
2. 根据布局查看，发现XComponent组件的宽高属性没有铺满整个屏幕。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/5ki4GtmlTk2NdHrVwLQrmA/zh-cn_image_0000002658791623.png)
3. 检查代码中是否设置了固定宽高，是否没有通过on('windowSizeChange')接口动态调整布局。示例代码如下：

   ```ts
   Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Start }) {
     XComponent({
       id: 'xComponentId',
       type: XComponentType.SURFACE,
       controller: this.myXComponentController
     })
       .width(this.getUIContext().px2vp(this.windowWidth))
       .height(this.getUIContext().px2vp(this.windowHeight))
   }
   ```

## 分析结论

XComponent组件设置了固定宽高，没有通过on('windowSizeChange')获取到当前窗口最新尺寸，动态调整页面布局，导致两侧出现大量黑边。

## 修改建议

1. 在EntryAbility.ets中，通过on('windowSizeChange')监听窗口尺寸的变化，存入AppStorage中。

   ```ts
   onWindowStageCreate(windowStage: window.WindowStage): void {
     // Main window is created, set main page for this ability
     hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
     windowStage.getMainWindow().then((windowClass) => {
       // 获取窗口尺寸，存入AppStorage
       AppStorage.setOrCreate('windowWidth', windowClass.getWindowProperties().windowRect.width);
       AppStorage.setOrCreate('windowHeight', windowClass.getWindowProperties().windowRect.height);
       // 监听窗口尺寸变化
       windowClass.on('windowSizeChange', (windowSize) => {
         AppStorage.setOrCreate('windowWidth', windowSize.width);
         AppStorage.setOrCreate('windowHeight', windowSize.height);
       });
     });
     windowStage.loadContent('pages/Index', (err) => {
       if (err.code) {
         hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
         return;
       }
       hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
     });
   }
   ```
2. 页面通过@StorageLink装饰的数据在窗口尺寸发生变化时会引起组件的重新渲染，根据最新的窗口尺寸动态调整页面布局，确保页面铺满整个屏幕。

   ```ts
   import { media } from '@kit.MediaKit';

   @Entry
   @Component
   struct XComponentIndex {
     private avPlayer: media.AVPlayer | null = null; // AVPlayer实例
     private surfaceId: string = ''; // 播放窗口SurfaceID
     // 初始化参数，这里会初始化为AppStorage中存储的值
     @StorageLink('windowWidth') windowWidth: number | undefined = AppStorage.get('windowWidth');
     @StorageLink('windowHeight') windowHeight: number | undefined = AppStorage.get('windowHeight');
     myXComponentController: XComponentController = new XComponentController();

     // 初始化播放器
     async initAVPlayer() {
       try {
         // 创建AVPlayer实例
         this.avPlayer = await media.createAVPlayer();
         // 设置监听事件
         this.avPlayer.on('stateChange', async (state: string) => {
           if (state === 'initialized') {
             // 设置播放窗口
             this.avPlayer!.surfaceId = this.surfaceId;
             await this.avPlayer!.prepare();
           } else if (state === 'prepared') {
             await this.avPlayer!.play(); // 自动开始播放
           }
         });
         this.avPlayer.url = 'https://xxx.mp4'; // 替换为实际地址
       } catch (error) {
         console.error(`Player initialization failed: ${error}`);
       }
     }

     build() {
       Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Start }) {
         XComponent({
           id: 'xComponentId',
           type: XComponentType.SURFACE,
           controller: this.myXComponentController
         })
           .onLoad(async () => {
             // 获取SurfaceID并初始化播放器
             this.surfaceId = this.myXComponentController.getXComponentSurfaceId();
             this.initAVPlayer();
           })
           .width(this.getUIContext().px2vp(this.windowWidth))
           .height(this.getUIContext().px2vp(this.windowHeight));
       };
     }
   }
   ```
3. 配置必要权限，在module.json5中添加网络访问权限。

   ```ts
   "requestPermissions": [
     {
       "name": "ohos.permission.INTERNET"
     }
   ],
   ```
