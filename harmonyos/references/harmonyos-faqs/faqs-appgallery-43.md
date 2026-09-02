---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-43
title: 如何实现应用升级自定义弹窗并监控点击事件
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 如何实现应用升级自定义弹窗并监控点击事件
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:29+08:00
doc_updated_at: 2026-08-12
content_hash: sha256:e883c97af2591e703b1607b4afb24d0d8e32236fc1bc64930d86dbd972583307
---

## 问题现象

如何实现应用升级自定义弹窗并监控点击事件，以及实现强制更新功能？

## 背景知识

* [应用市场更新功能](../harmonyos-guides/store-update.md)为开发者提供了应用升级检测[checkAppUpdate](../harmonyos-references/store-updatemanager.md#updatemanagercheckappupdate)和弹窗接口[showUpdateDialog](../harmonyos-references/store-updatemanager.md#updatemanagershowupdatedialog)，但是样式和内容是固定的，数据来源于上架提交的信息，也不能监控点击事件，无法获知到有多少用户点击了“立即更新”升级应用。
* 拉起应用市场，跳转至应用详情界面，可以通过[Deep Linking](../harmonyos-guides/deep-linking-startup.md)、[App Linking](../harmonyos-guides/app-linking-startup.md)和[loadProduct](../harmonyos-references/store-productviewmanager.md#productviewmanagerloadproduct)三种方式实现。
* 使用弹窗组件时，可优先考虑自定义弹窗，便于自定义弹窗的样式与内容。通过[CustomDialogController类](../harmonyos-references/ts-methods-custom-dialog-box.md)显示自定义弹窗，不支持直接在类中定义和使用。通常需要将弹框逻辑封装成Builder或其他组件，以便在需要时调用。

## 解决方案

* **场景一：**

  实现应用升级自定义弹窗，可保持应用内弹窗样式的统一，或监控“立即更新”按钮。

  操作步骤：

  1. 调用[updateManager.checkAppUpdate](../harmonyos-references/store-updatemanager.md#updatemanagercheckappupdate)接口，检查到有更新。
  2. 调用自定义的UI更新弹框[CustomDialog](../harmonyos-references/ts-methods-custom-dialog-box.md)。
  3. 用户点击自定义弹框里的“立即更新”按钮，调用[productViewManager.loadProduct](../harmonyos-references/store-productviewmanager.md#productviewmanagerloadproduct)接口展示应用详情页，用户在应用详情页里更新应用。
  4. 开发者结合自己的业务来监控“以后再说”或“立即更新”按钮，代码中是通过[hilog](../harmonyos-guides/hilog.md)输出日志体现。

  **说明** 

  采用这种自定义弹框，需要自己维护新版本的版本号、大小、更新详情描述信息。
* **场景二：**

  目前系统提供的更新弹窗没有提供强制更新功能，用户可以通过场景一中的应用升级自定义弹窗的基础上实现强制更新。

  操作步骤：

  1. 检查到有版本更新后，仅提供立即更新按钮。
  2. 通过注册[onWillDismiss](../harmonyos-references/ts-methods-custom-dialog-box.md#customdialogcontrolleroptions对象说明)回调拦截用户执行的点击遮障层关闭、左滑/右滑、三键back、键盘ESC关闭交互操作。
* 完整示例参考如下：

  ```screen
  import { common, Want } from '@kit.AbilityKit';
  import { productViewManager, updateManager } from '@kit.AppGalleryKit';
  import { BusinessError } from '@kit.BasicServicesKit';
  import { hilog } from '@kit.PerformanceAnalysisKit';

  @CustomDialog
  export struct BaseComHud {
    controller: CustomDialogController;

    build() {
      Column() {
        Text('有新版本更新，前往应用市场更新~')
          .fontSize(16)
          .margin({ top: 10, bottom: 10 });
        Row() {
          Button('立即更新')
            .onClick(() => {
              hilog.info(0, 'TAG', '用户选择了立即更新');
              try {
                updateManager.checkAppUpdate(this.getUIContext().getHostContext() as common.UIAbilityContext)
                  .then((checkResult: updateManager.CheckUpdateResult) => {
                    hilog.info(0, 'TAG', `Succeeded in checking Result updateAvailable: ${checkResult.updateAvailable}`);
                  }).catch((error: BusinessError) => {
                  hilog.error(0, 'TAG', `checkAppUpdate onError.code is ${error.code}, message is ${error.message}`);
                });
              } catch (error) {
                hilog.error(0, 'TAG', `checkAppUpdate onError.code is ${error.code}, message is ${error.message}`);
              }

              const wantParam: Want = {
                parameters: {
                  // 必填，此处填入要加载的应用包名，例如：bundleName:'com.xxx.xx'
                  bundleName: 'com.xxx.xx',
                }
              };
              const callback: productViewManager.ProductViewCallback = {
                onError: (error: BusinessError) => {
                  hilog.error(0, 'TAG', `loadService onError.code is ${error.code}, message is ${error.message}`);
                },
                onAppear: () => {
                  hilog.info(0, 'TAG', `loadProduct onAppear.`);
                },
                onDisappear: () => {
                  hilog.info(0, 'TAG', `loadProduct onDisappear.`);
                }
              };
              // 调用接口，拉起应用详情页
              productViewManager.loadProduct(this.getUIContext().getHostContext() as common.UIAbilityContext, wantParam,
                callback);
            });
        }
      }
      .backgroundColor(Color.White)
      .borderRadius(10)
      .padding(20);
    }
  }

  @Entry
  @Component
  struct Index {
    dialogController: CustomDialogController = new CustomDialogController({
      // 此处直接指定自定义弹窗，不要重新new
      builder: BaseComHud(),
      alignment: DialogAlignment.Center,
    });
    dialogController1: CustomDialogController = new CustomDialogController({
      // 此处直接指定自定义弹窗，不要重新new
      builder: BaseComHud(),
      alignment: DialogAlignment.Center,
      onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
        // 参数说明
        // PRESS_BACK为点击三键back、左滑/右滑、键盘ESC退出。
        // TOUCH_OUTSIDE为点击遮障层退出。
        // CLOSE_BUTTON为点击关闭按钮退出。
        // SLIDE_DOWN为下拉关闭（适用于半模态转场）
        if (dismissDialogAction.reason === DismissReason.PRESS_BACK) {
          // ...
          // 可使用dismiss方法可关闭弹窗，dismissDialogAction.dismiss()
        }
      },
    });

    build() {
      Column() {
        Button('更新弹窗')
          .onClick(() => {
            this.dialogController.open(); // 打开弹窗
          });

        Button('强制更新弹窗')
          .onClick(() => {
            this.dialogController1.open(); // 打开弹窗
          });
      }
      .width('100%')
      .height('100%')
      .justifyContent(FlexAlign.SpaceEvenly);
    }
  }
  ```
