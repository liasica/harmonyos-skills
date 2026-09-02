---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-898
title: 并发接口拦截器中如何实现全局弹窗
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 并发接口拦截器中如何实现全局弹窗
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:18+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:09a0051880278e92238c0887eee870069cd1f9cfd98a3af57ee6150808c3ffc7
---

## 问题现象

在应用中，每个接口都可能返回响应码Code，需要在接口拦截器中实现一个全局弹窗。由于接口是并发的，弹窗只能弹出一次。那么如何实现这个全局弹窗呢？此外，由于弹窗可能会在多个页面弹出（如启动页、登录页、主页等），这些页面可能会被销毁，这会导致弹窗无法正常显示。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/G8bAFqjTSda5QX_XVd36Yg/zh-cn_image_0000002658799017.png "点击放大") ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/R2nvZl50THO9pbc2IX7ljw/zh-cn_image_0000002628559664.png "点击放大") ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/3rbbsyGxRwO3CuY69A4H-g/zh-cn_image_0000002658918971.png "点击放大")

## 背景知识

* 使用弹窗组件时，可优先考虑自定义弹窗，便于自定义弹窗的样式与内容。通过[CustomDialogController类](../harmonyos-references/ts-methods-custom-dialog-box.md)显示自定义弹窗，不支持直接在类中定义和使用。通常需要将弹框逻辑封装成Builder或其他组件，以便在需要时调用。
* 可以使用[@StorageLink与AppStorage](../harmonyos-guides/arkts-appstorage.md#storagelink)中的key对应的属性建立双向数据同步，该属性可以和UI组件同步，且可以在应用业务逻辑中被访问。

## 解决方案

在并发接口拦截器中，由于弹窗弹出位置不确定且仅弹出一次，因此需要维护一个全局变量来保证弹窗的弹出状态。可以在AppStorage中定义弹窗弹出状态，并通过@StorageLink来获取弹窗是否曾弹出，具体实现可参考以下示例：

1. EntryAbility.ets的onWindowStageCreate方法里通过AppStorage定义关于弹框显示的全局属性，默认false不显示：

   ```ts
   windowStage.loadContent('pages/Index', (err) => {
     AppStorage.setOrCreate('showGlobalCustomDialog', false);
     if (err.code) {
       hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
       return;
     }
     hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
   });
   ```

2. 封装1个弹框实例类CustomDialogLayout.ets：

   ```ts
   @CustomDialog
   export struct CustomDialogLayout {
     controller?: CustomDialogController;

     build() {
       Column() {
         Text('Global Custom Dialog Test');
       }
       .justifyContent(FlexAlign.Center)
       .alignItems(HorizontalAlign.Center)
       .height(400);
     }
   }
   ```
3. Index.ets，在该页面import并创建实例import { CustomDialogLayout } from './CustomDialogLayout'，并且监听showGlobalCustomDialog属性值的改变并进行拉起弹窗动作：

   ```ts
   import { CustomDialogLayout } from './CustomDialogLayout';

   @Entry
   @Component
   struct Index {
     @Provide('pathStack') pathStack: NavPathStack = new NavPathStack();
     @StorageLink('showGlobalCustomDialog') @Watch('globalCustomDialogStateChange') showGlobalCustomDialog: boolean = false;

     globalCustomDialogStateChange() {
       if (this.showGlobalCustomDialog) {
         if (this.dialogController != null) {
           this.dialogController.open();
           AppStorage.setOrCreate('showGlobalCustomDialog', false);
         }
       }
     }

     dialogController: CustomDialogController | null = new CustomDialogController({
       builder: CustomDialogLayout({}),
       autoCancel: true,
       alignment: DialogAlignment.Center,
     });

     build() {
       Navigation(this.pathStack) {
         RelativeContainer() {
           Button('跳转其他页面')
             .fontSize(15)
             .fontWeight(FontWeight.Bold)
             .alignRules({
               center: { anchor: '__container__', align: VerticalAlign.Center },
               middle: { anchor: '__container__', align: HorizontalAlign.Center }
             })

             .onClick(() => {
               this.pathStack.pushPathByName('DetailPage', null);
             });
         }
         .height('100%')
         .width('100%');
       }
       .mode(NavigationMode.Stack);
     }
   }
   ```

4. DetailPage.ets，在该页面设置showGlobalCustomDialog全局属性为true即可调起弹框：

   ```ts
   @Builder
   export function DetailPageBuilder() {
     DetailPage();
   }

   @Component
   export struct DetailPage {
     @Consume('pathStack') pathStack: NavPathStack;

     build() {
       NavDestination() {
         RelativeContainer() {
           Button('promptAction弹窗')
             .onClick(() => {
               AppStorage.setOrCreate('showGlobalCustomDialog', true);
             })
             .alignRules({
               center: { anchor: '__container__', align: VerticalAlign.Center },
               middle: { anchor: '__container__', align: HorizontalAlign.Center }
             });
         };
       }.title('DetailPage');
     }
   }
   ```

## 总结

在并发场景下，为了实现条件判断和控制弹窗弹出的行为，可以通过在AppStorage中维护一个全局变量，并使用@StorageLink进行同步监听。这种方法可以保证弹窗只弹出一次，从而避免重复弹出问题。
