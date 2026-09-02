---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1394
title: 悬浮窗切换全屏，底部留白
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 悬浮窗切换全屏，底部留白
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:13+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ab5dc6c5b135662786c6dd675fe75e5c3d79bb885b4c49e64605f0983a5b037a
---

## 问题现象

悬浮窗模式下，点击全屏按钮，进入全屏后的页面底部会有大白块。

## 背景知识

* [on('windowSizeChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowsizechange7)：可监听窗口尺寸的变化，当窗口尺寸变化时，应用可通过改变自身的布局以适配不同的窗口尺寸。
* [@StorageLink](../harmonyos-guides/arkts-appstorage.md#storagelink)：@StorageLink(key)是和AppStorage中key对应的属性建立双向数据同步，该装饰器装饰的数据本身是状态变量，在数据发生变化时，会引起组件重新渲染。

## 问题定位

1. 检查代码中是否调用on('windowSizeChange')接口监听窗口尺寸的变化。
2. 检查页面代码中的组件尺寸属性数据是否为状态变量，即组件是否是随着数据变化重新渲染。

## 分析结论

组件的尺寸属性数据未关联状态变量，在窗口尺寸发生变化时，组件的尺寸也发生了变化，由于尺寸属性数据未关联状态变量，组件未重新渲染，底部出现大白块。

## 修改建议

1. 在EntryAbility中使用on('windowSizeChange')注册窗口尺寸变化时的监听，并写入AppStorage中供UI侧布局使用。

   ```screen
   onWindowStageCreate(windowStage: window.WindowStage): void {
     // Main window is created, set main page for this ability
     console.info('Ability onWindowStageCreate.');
     windowStage.getMainWindow().then((windowClass) => {
       // 获取窗口尺寸，存入AppStorage
       AppStorage.setOrCreate('winWidth', windowClass.getWindowProperties().windowRect.width);
       AppStorage.setOrCreate('winHeight', windowClass.getWindowProperties().windowRect.height);
       // 监听窗口尺寸变化
       windowClass.on('windowSizeChange', (windowSize) => {
         AppStorage.setOrCreate('winWidth', windowSize.width);
         AppStorage.setOrCreate('winHeight', windowSize.height);
       });
     });

     hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

     windowStage.loadContent('pages/Index', (err) => {
       if (err.code) {
         hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
         return;
       }
       hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
     });
   }
   ```
2. UI侧通过@StorageLink绑定窗口尺寸后，AppStorage中属性key值对应的数据一旦改变，UI侧会同步修改。

   ```screen
   @Entry
   @Component
   struct WinHeightExampleDemo {
     @StorageLink('winWidth') winWidth: number | undefined = AppStorage.get('winWidth');
     @StorageLink('winHeight') winHeight: number | undefined = AppStorage.get('winHeight');

     build() {
       Column() {
         Text('页面大小设为窗口大小，使页面不留白');
         Column()
           .width('100%')
           .height('100%')
           .backgroundColor(Color.Gray);
       }
       .width(this.getUIContext().px2vp(this.winWidth))
       .height(this.getUIContext().px2vp(this.winHeight));
     }
   }
   ```
