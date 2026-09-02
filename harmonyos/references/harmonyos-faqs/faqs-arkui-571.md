---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-571
title: 自定义字体无法全局使用如何处理
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 自定义字体无法全局使用如何处理
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:01+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:ca77e5622e36970a6aea233ea4749506d11c68c98418d7b764e851bb1a019864
---

## 问题现象

registerFont注册**应用全局生效**的自定义字体失败。

* 预期效果：注册自定义字体后，在应用中能成功使用该字体。
* 实际效果：注册自定义字体后，显示效果与默认字体相同。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/LDJkcGqqS86PuGyESC3XXw/zh-cn_image_0000002684134941.png "点击放大")

问题代码如下：

* 注册字体。

  ```ts
  // 注册iconFont
  this.getUIContext().getFont().registerFont({
    familyName: 'iconFont',
    // 自定义字体存储在rawfile的font文件夹下
    familySrc: $rawfile('font/XXXX.TTF')
  });
  ```
* 使用字体。

  ```ts
  @Entry
  @Component
  struct Index {
    build() {
      Column() {
        // 使用自定义字体的文字
        Text('图标字体')
          .fontSize(30)
          .fontFamily('iconfont');
        // 使用默认字体的文字
        Text('图标字体')
          .fontSize(30);
      }.width('100%');
    }
  }
  ```

## 背景知识

可参考官方文档[@ohos.font(注册自定义字体)](../harmonyos-references/js-apis-font.md)。

## 问题定位

定位自定义字体无法使用的原因时，首先应确认字体注册信息配置是否正确。若字体注册信息配置无误，但字体仍无法正常显示，则需进一步检查字体实例的生命周期状态是否处于有效范围。

## 分析结论

1. 注册信息填写不正确。

   请根据接口文档[registerFont](../harmonyos-references/arkts-apis-uicontext-font.md#registerfont)进行检查。
2. 注册生命周期不正确。

   当自定义字体注册信息填写正确，但仍然无法使用时，是因为**全局使用自定义字体，需在EntryAbility.ets文件的onWindowStageCreate生命周期中，通过windowStage.loadContent回调来注册**。详情参考[loadContent](../harmonyos-references/arkts-apis-window-windowstage.md#loadcontent9)回调方法。

## 修改建议

根据定位思路可以做出如下操作：

1. 检查注册信息。

   首先请检查注册信息填写是否有误。

   确保注册路径正确无误，如将自定义字体放在rawfile的font文件夹下，则在代码中使用时须保持路径正确$rawfile('font/XXX.ttf')。
2. 检查生命周期。

   根据定位思路，其次检查全局定义的字体生命周期是否正确。
   * 在entryability.ets的onWindowStageCreate中注册自定义字体。

     ```ts
     onWindowStageCreate(windowStage: window.WindowStage): void {
         // Main window is created, set main page for this ability
         hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
         windowStage.loadContent('pages/Index', (err) => {
           if (err.code) {
             hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
             return;
           }
           windowStage.getMainWindow().then(res => {
             // 注册全局生效的自定义字体
             const uiCtc = res.getUIContext();
             uiCtc.getFont().registerFont({
               familyName: 'iconfont',
               // 字体文件保存在rawfile目录下，字体资源文件需自行配置
               familySrc: $rawfile('font/HarmonyOS_Sans_SC_Thin.ttf')
             });
           });
           hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
         });
       }
     ```
   * Index文件。

     ```ts
     @Entry
     @Component
     struct Index {
       build() {
         Column() {
           // 使用自定义字体的文字
           Text('图标字体')
             .fontSize(30)
             .fontFamily('iconfont');
           // 使用默认字体的文字
           Text('图标字体')
             .fontSize(30);
         }.justifyContent(FlexAlign.Center)
         .height('100%')
         .width('100%');
       }
     }
     ```

效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/EUYcPkBLRZW3z7vK08JX5Q/zh-cn_image_0000002684295417.png "点击放大")

**其他注意事项：**

* 字体文件需要下载到**本地使用**，并且unicode编码要获取正确。
* 编译时需要**在真机/模拟器上调试**，预览器上不能正常展示。

## 常见FAQ

Q：在onWindowStageCreate中全局注册了自定义字体，有无全局设置应用自定义字体的方法？

A：可以使用[ApplicationContext.setFont](../harmonyos-references/js-apis-inner-application-applicationcontext.md#applicationcontextsetfont12)来全局设置字体应用到整个项目。在windowStage.loadContent方法中调用ApplicationContext.setFont()即可。

Q：使用ApplicationContext.setFont切换到自定义字体后，如何切换回跟随系统字体？

A：调用[ApplicationContext.setFont](../harmonyos-references/js-apis-inner-application-applicationcontext.md#applicationcontextsetfont12)传入"null"即可恢复跟随系统字体。

## 总结

@ohos.font可以注册页面级的字体，也可以注册全局性的字体，全局字体需要通过windowStage.loadContent进行回调注册。
