---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/appgallery-kit-faq-0006
title: 应用内版本更新实现与问题排查FAQ
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 常见问题 > 应用内版本更新实现与问题排查FAQ
category: harmonyos-faqs
scraped_at: 2026-11-27T10:51:45+08:00
doc_updated_at: 2026-11-26
content_hash: sha256:fe2fe5aeee3ac4e9a29a552404e03b19a13cfb291dbde9606a3353a991adfb78
---

**Q：应用上架应用市场后，有新的版本更新时，如何实现老版本用户打开应用能提示更新版本？**

A：业务流程：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/29BN4VOQR02VPMkgkq0GYw/zh-cn_image_0000002792076741.png?HW-CC-KV=V1&HW-CC-Date=20261127T025145Z&HW-CC-Expire=31536000000&HW-CC-Sign=897554626EF697ED15873786F1554DBEA697EBBCF50A6B1794CD5F26AE709F9B "点击放大")

1. 应用调用检查更新接口。
2. 升级服务API返回是否有新版本。
3. 调用显示升级对话框接口。
4. 升级服务API向应用返回显示结果。

核心接口有[updateManager.checkAppUpdate](../harmonyos-references/store-updatemanager.md#updatemanagercheckappupdate)和[updateManager.showUpdateDialog](../harmonyos-references/store-updatemanager.md#updatemanagershowupdatedialog)，功能描述如下：

* checkAppUpdate：检查更新接口，用于检测当前是否有新版本。
* showUpdateDialog：显示升级对话框接口，用于提示用户进行升级。

开发步骤：

* 调用checkAppUpdate[检测应用新版本](../harmonyos-guides/store-update.md#检测应用新版本)。

  **说明** 

  本地安装版本须低于应用市场在架版本才能检查到更新。

  本地安装版本须和应用市场在架版本签名信息保持一致。

  暂不支持邀请测试和公开测试。
* 调用showUpdateDialog[显示升级对话框](../harmonyos-guides/store-update.md#显示升级对话框)。

  **说明** 

  调用showUpdateDialog需要在执行checkAppUpdate后进行，不能单独执行showUpdateDialog，否则即使应用市场有新版本也无法显示升级框。

**Q：应用升级版本号如何定义，是通过versionName还是versionCode来控制的？**

**A**：要实现升级弹窗，更新版本versionCode必须大于老版本versionCode，versionName不做要求。

**Q：应用内版本更新检查如何实现？**

**A**：建议拆成版本检查、更新入口、强制更新、增量更新四部分实现。

1. 版本检查：比较versionCode。

   本地读取应用的整数versionCode，服务端返回latestVersionCode、minSupportedVersionCode、更新说明等。判断逻辑：

   * 本地版本低于minSupportedVersionCode：要求升级后继续使用相关业务。
   * 本地版本低于latestVersionCode：提示可选更新。

   versionName用于展示，不要直接按字符串比较大小。
2. 更新入口：优先接应用市场能力。

   已上架的HarmonyOS应用，可以使用@kit.AppGalleryKit的updateManager.checkAppUpdate(context)检查，再调用showUpdateDialog(context)显示升级提醒。要求本地与在架版本签名一致，且本地版本更低；不支持用模拟器验证。
3. 强制更新：由业务控制最低可用版本。

   当前上述接口没有通用的“强制更新”参数。可以由应用显示升级拦截页，服务端同步拒绝不再兼容的旧版本请求，用户完成更新后恢复业务。这属于业务准入控制，不能强制静默安装。启用强制更新前，应确认新版本已对目标用户实际可下载，避免灰度期间导致用户无法正常使用。
4. 增量更新：区分安装包和资源包。

   应用升级交给应用市场分发；上述接口没有开放自行配置HAP差分合成的能力，不能承诺每次都走增量。若是图片、模型、离线内容等资源，可以自建“版本清单＋文件哈希”，只下载变化文件，校验完成后切换版本，失败保留旧资源。二进制差分的原理是“旧文件＋补丁＝新文件”，但还需处理基线版本匹配、完整性校验和全量下载兜底。

启动检查建议异步进行并设置超时、调用间隔，普通网络失败不应直接判定为必须更新。

**Q：能否使用邀请测试实现检查更新和升级弹窗功能？**

**A**：暂不支持邀请测试和公开测试，使用邀请测试接口会返回[1009400001 服务异常](../harmonyos-references/errorcode-appgallery.md#section1009400001-服务异常)。需要先正式上架版本才能测试。

**Q：是否支持模拟器测试？**

**A**：暂不支持模拟器，请使用真机调试。在模拟器中使用该服务将会提示：无法获取内容，请点击屏幕重试。详情可参考[约束与限制](../harmonyos-guides/store-update.md#约束与限制)。

**Q：本地安装版本和应用市场在架版本签名保持一致怎么理解？**

**A**：应用升级需要进行[签名证书一致性校验](../harmonyos-guides/install-and-update-consistency-verification.md#签名证书一致性校验)和[配置文件一致性校验](../harmonyos-guides/install-and-update-consistency-verification.md#配置文件一致性校验)。只需要保证[appId](../harmonyos-guides/common-problem-of-application.md#什么是appid)和[appIdentifier](../harmonyos-guides/common-problem-of-application.md#什么是appidentifier)（对应HarmonyOS 开发者中心上应用的APP ID，应用的唯一标识）任一相同即可满足签名信息保持一致。

**Q：是否支持强制升级（不升级无法进入应用）？**

**A**：开发者可以自行实现强制更新，通过checkAppUpdate判断用户版本是否需要更新，根据返回的CheckUpdateResult的值来判断是否有新版本，从而可弹窗拉起应用市场的应用详情页更新。

**Q：升级弹窗是否能自定义？**

**A**：不可以，检测到有新版本需要更新后，系统弹窗的版本信息和更新说明来源于应用市场客户端应用详情页数据。如果需要修改，需要在上架版本时HarmonyOS 开发者中心页面更新。详情可参考[升级版本](../app/agc-help-maintain-upgrade-0000002236494386.md)。

**Q：为什么调用checkAppUpdate接口[UpdateAvailableCode](../harmonyos-references/store-updatemanager.md#updateavailablecode)返回结果为-1？**

**A**：应用只有上架过应用市场，checkAppUpdate接口才能正常返回0或1；如果从来没用上架过应用市场，就返回-1。

**Q：非公开上架的应用是否可以用接口updateManager.checkAppUpdate检查到更新？**

**A**：接口updateManager.checkAppUpdate可以用来检查非公开发布应用的版本更新。

**Q：自动签名在真机上运行的工程，为什么检查更新一直返回不需要更新？**

**A**：使用自动签名无法满足签名信息和在架版本保持一致，因此无法测试。需要使用调试证书签名。

**Q：checkAppUpdate和showUpdateDialog是否支持智慧屏类型的应用？**

**A**：对于API 19之前版本，该接口在Phone、Tablet、PC/2in1中可正常调用；对于API 20及之后版本，该接口在Phone、Tablet、PC/2in1、TV、Wearable中可正常调用。

**Q：In-house发布的应用是否可以支持升级？**

**A**：In-house应用未上架应用市场，调用升级检测接口会报错。In-house应用可以通过[openlink](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#openlink12)的方式去进行应用升级，该方式不会拉起浏览器，会直接拉起企业模块的下载能力，升级场景下可以在应用内直接触发Deeplink。openlink配置地址的就是Deeplink链接，详情可参考[构建Deeplink实现下载应用](../app/agc-help-inhouse-0000002281532696.md#section74503017418)。

**Q：应用市场更新应用时是否会触发卸载安装应用？**

**A**：在应用市场更新应用时，不会触发完整的卸载再安装流程，而是采用覆盖安装的方式实现应用更新。

**Q：未上架应用如何调试应用市场更新功能？**

**A**：得先正式上架一个不带更新弹窗功能的版本，版本号versionCode设得大于1000000。之后就可以用调测证书，在本地开发环境里，直接调试升级跳转应用市场的功能。可以参考[应用市场更新功能](../harmonyos-guides/store-update.md)。

**Q：CheckUpdateResult能否新增字段，用于判断已安装的历史版本是否需要强制更新到最新版本？**

**A**：当前CheckUpdateResult不支持新增字段用于判断是否需要强制更新。建议在应用服务端维护一个"最低允许版本号"或"强制更新版本列表"，应用启动时调用服务端接口获取当前最低允许版本，将本地versionCode与服务端返回的版本号对比，若本地版本过低，则通过[showUpdateDialog](../harmonyos-references/store-updatemanager.md#updatemanagershowupdatedialog)或拉起应用市场详情页，并阻止用户继续使用旧版。

**Q：应用测试（邀请测试）场景下，应用市场应用尝鲜页面中已安装低版本的应用为什么显示"安装"按钮而不是"更新"按钮？**

**A**：应用测试（邀请测试）场景不支持更新功能，需要正式上架版本后才能测试更新功能。详情可参考[应用市场FAQ](appgallery-kit-faq.md)。

**Q：更新应用版本是否支持通过API上传更新，绕开应用市场？**

**A**：目前应用更新暂不支持绕开应用市场，需要通过应用市场进行版本更新。若需检查更新并跳转到应用市场，可参考【解决方案】章节中的checkAppUpdate和showUpdateDialog接口实现。

**Q：穿戴设备系统版本较低时无法使用checkAppUpdate接口，如何实现应用内检查更新并引导用户升级？**

**A**：当穿戴设备系统版本较低（如5.1.0）无法使用checkAppUpdate等系统提供的API时，可采用以下方案：

1. 自行构建版本检测逻辑：比较latestVersionCode与localVersionCode判断是否有新版本。
2. 使用[自定义弹窗](../harmonyos-references/ts-methods-custom-dialog-box.md)提示用户更新。
3. 用户点击"立即更新"后，通过startAbility搭配Want跳转应用市场详情页，拉起方式参考[拉起应用市场并跳转应用详情](faqs-appgallery-31.md)。

**说明** 

loadProduct接口不支持穿戴设备。

若后续系统版本及应用市场版本满足要求（系统版本6.1.0.330 SP18及以上，应用市场7.6.1.300及以上），也可通过AppGallery Kit的checkAppUpdate接口检测应用是否有新版本，再通过showUpdateDialog弹出系统升级弹框，或使用自定义弹窗搭配loadProduct跳转应用市场详情页。参考[应用内检查更新实现及常见问题](faqs-appgallery-98.md)和[如何实现应用升级自定义弹窗](faqs-appgallery-43.md)。

**Q：如何实现应用升级自定义弹窗并监控点击事件？**

**A**：实现应用升级自定义弹窗，可保持应用内弹窗样式的统一，或监控“立即更新”按钮。

操作步骤：

1. 调用[updateManager.checkAppUpdate](../harmonyos-references/store-updatemanager.md#section10984155711373)接口，检查到有更新。
2. 调用自定义的UI更新弹框[CustomDialog](../harmonyos-references/ts-methods-custom-dialog-box.md)。
3. 用户点击自定义弹框里的“立即更新”按钮，调用[productViewManager.loadProduct](../harmonyos-references/store-productviewmanager.md#section144826162913)接口展示应用详情页，用户在应用详情页里更新应用。
4. 开发者结合自己的业务来监控“以后再说”或“立即更新”按钮，代码中是通过[hilog](../harmonyos-guides/hilog.md)输出日志体现。

**说明** 

采用这种自定义弹框，需要自己维护新版本的版本号、大小、更新详情描述信息。

**Q：如何实现强制更新功能？**

A：目前系统提供的更新弹窗没有提供强制更新功能，用户可以通过应用升级自定义弹窗的基础上实现强制更新。

目前系统提供的更新弹窗没有提供强制更新功能，用户可以通过场景一中的应用升级自定义弹窗的基础上实现强制更新。

操作步骤：

1. 检查到有版本更新后，仅提供立即更新按钮。
2. 通过注册[onWillDismiss](../harmonyos-references/ts-methods-custom-dialog-box.md#customdialogcontrolleroptions对象说明)回调拦截用户执行的点击遮障层关闭、左滑/右滑、三键back、键盘ESC关闭交互操作。

完整代码参考：

```ts
import { common, Want } from "@kit.AbilityKit";
import { productViewManager, updateManager } from "@kit.AppGalleryKit";
import { BusinessError } from "@kit.BasicServicesKit";
import { hilog } from "@kit.PerformanceAnalysisKit";

@CustomDialog
export struct BaseComHud {
  controller: CustomDialogController;

  build() {
    Column() {
      Text('有新版本更新，前往应用市场更新~')
        .fontSize(16)
        .margin({ top: 10, bottom: 10 });
      Row(){
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
            productViewManager.loadProduct(this.getUIContext().getHostContext() as common.UIAbilityContext, wantParam, callback);
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
