---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-widget-event-uiability
title: 通过router或call事件刷新卡片内容
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > ArkTS卡片开发（推荐） > ArkTS卡片提供方开发指导 > ArkTS卡片页面交互 > 通过router或call事件刷新卡片内容
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:25+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2eb33288ac9d4c4e16e33430300a4472a970dc1162b2da815821fa4e4135b91d
---

使用router事件，点击卡片可拉起对应应用的UIAbility至前台，并刷新卡片。使用call事件，点击卡片可拉起对应应用的UIAbility至后台，并刷新卡片。在卡片页面中可以通过[postCardAction](../harmonyos-references/js-apis-postcardaction.md#postcardaction-1)接口触发router事件或者call事件拉起UIAbility，然后由UIAbility刷新卡片内容，下面是这种刷新方式的简单示例。

**说明** 

本文主要介绍动态卡片的事件开发。对于静态卡片，请参见[FormLink](../harmonyos-references/ts-container-formlink.md)。

## 通过router事件刷新卡片内容

* 在卡片页面代码文件中，通过注册Button的onClick点击事件回调并在回调中调用postCardAction接口，触发router事件拉起UIAbility至前台。

  ```typescript
  // entry/src/main/ets/widgetupdaterouter/pages/WidgetUpdateRouterCard.ets
  let storageUpdateRouter = new LocalStorage();

  @Entry(storageUpdateRouter)
  @Component
  struct WidgetUpdateRouterCard {
    // $r('app.string.init')需要替换为开发者所需的资源文件
    @LocalStorageProp('routerDetail') routerDetail: ResourceStr = $r('app.string.init');

    build() {
      Column() {
        Column() {
          Text(this.routerDetail)
            .fontColor('#FFFFFF')
            .opacity(0.9)
            .fontSize(14)
            .margin({ top: '8%', left: '10%', right: '10%' })
            .textOverflow({ overflow: TextOverflow.Ellipsis })
            .maxLines(2)
        }.width('100%').height('50%')
        .alignItems(HorizontalAlign.Start)

        Row() {
          Button() {
            // $r('app.string.JumpLabel')需要替换为开发者所需的资源文件
            Text($r('app.string.JumpLabel'))
              .fontColor('#45A6F4')
              .fontSize(12)
          }
          .width(120)
          .height(32)
          .margin({ top: '30%', bottom: '10%' })
          .backgroundColor('#FFFFFF')
          .borderRadius(16)
          .onClick(() => {
            postCardAction(this, {
              action: 'router',
              abilityName: 'WidgetEventRouterEntryAbility', // 只能跳转到当前应用下的UIAbility
              params: {
                routerDetail: 'RouterFromCard',
              }
            });
          })
        }.width('100%').height('40%')
        .justifyContent(FlexAlign.Center)
      }
      .width('100%')
      .height('100%')
      .alignItems(HorizontalAlign.Start)
      // $r('app.media.CardEvent')需要替换为开发者所需的资源文件
      .backgroundImage($r('app.media.CardEvent'))
      .backgroundImageSize(ImageSize.Cover)
    }
  }
  ```
* 在UIAbility的onCreate或者onNewWant生命周期中可以通过入参want获取卡片的formID和传递过来的参数信息，然后调用[updateForm](../harmonyos-references/js-apis-app-form-formprovider.md#formproviderupdateform)接口刷新卡片。

  ```typescript
  // entry/src/main/ets/widgetevententryability/WidgetEventRouterEntryAbility.ts
  import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
  import { window } from '@kit.ArkUI';
  import { BusinessError } from '@kit.BasicServicesKit';
  import { formBindingData, formInfo, formProvider } from '@kit.FormKit';
  import { hilog } from '@kit.PerformanceAnalysisKit';

  const TAG: string = 'WidgetEventRouterEntryAbility';
  const DOMAIN_NUMBER: number = 0xFF00;

  export default class WidgetEventRouterEntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
      this.handleFormRouterEvent(want, 'onCreate');
    }

    handleFormRouterEvent(want: Want, source: string): void {
      hilog.info(DOMAIN_NUMBER, TAG, `handleFormRouterEvent ${source}, Want: ${JSON.stringify(want)}`);
      if (want.parameters && want.parameters[formInfo.FormParam.IDENTITY_KEY] !== undefined) {
        let curFormId = want.parameters[formInfo.FormParam.IDENTITY_KEY].toString();
        // want.parameters.params 对应 postCardAction() 中 params 内容
        let message: string = (JSON.parse(want.parameters?.params as string))?.routerDetail;
        hilog.info(DOMAIN_NUMBER, TAG, `UpdateForm formId: ${curFormId}, message: ${message}`);
        let formData: Record<string, string> = {
          'routerDetail': message + ' ' + source + ' UIAbility', // 和卡片布局中对应
        };
        let formMsg = formBindingData.createFormBindingData(formData);
        formProvider.updateForm(curFormId, formMsg).then((data) => {
          hilog.info(DOMAIN_NUMBER, TAG, 'updateForm success.', JSON.stringify(data));
        }).catch((error: BusinessError) => {
          hilog.info(DOMAIN_NUMBER, TAG, 'updateForm failed.', JSON.stringify(error));
        });
      }
    }

    // 如果UIAbility已在后台运行，在收到Router事件后会触发onNewWant生命周期回调
    onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
      hilog.info(DOMAIN_NUMBER, TAG, 'onNewWant Want:', JSON.stringify(want));
      this.handleFormRouterEvent(want, 'onNewWant');
    }

    onWindowStageCreate(windowStage: window.WindowStage): void {

      hilog.info(DOMAIN_NUMBER, TAG, '%{public}s', 'Ability onWindowStageCreate');

      windowStage.loadContent('pages/Index', (err, data) => {
        if (err.code) {
          hilog.error(DOMAIN_NUMBER, TAG, 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
          return;
        }
        hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
      });
    }
  }
  ```

## 通过call事件刷新卡片内容

* 在卡片页面代码文件中，通过注册Button的onClick点击事件回调并在回调中调用postCardAction接口，触发call事件拉起UIAbility至后台。

  ```typescript
  // entry/src/main/ets/widgetupdatecall/pages/WidgetUpdateCallCard.ets
  let storageUpdateCall = new LocalStorage();

  @Entry(storageUpdateCall)
  @Component
  struct WidgetUpdateCallCard {
    @LocalStorageProp('formId') formId: string = '12400633174999288';
    // $r('app.string.init')需要替换为开发者所需的资源文件
    @LocalStorageProp('calleeDetail') calleeDetail: ResourceStr = $r('app.string.init');

    build() {
      Column() {
        Column() {
          Text(this.calleeDetail)
            .fontColor('#FFFFFF')
            .opacity(0.9)
            .fontSize(14)
            .margin({ top: '8%', left: '10%' })
        }.width('100%').height('50%')
        .alignItems(HorizontalAlign.Start)

        Row() {
          Button() {
            // $r('app.string.CalleeJumpLabel')需要替换为开发者所需的资源文件
            Text($r('app.string.CalleeJumpLabel'))
              .fontColor('#45A6F4')
              .fontSize(12)
          }
          .width(120)
          .height(32)
          .margin({ top: '30%', bottom: '10%' })
          .backgroundColor('#FFFFFF')
          .borderRadius(16)
          .onClick(() => {
            postCardAction(this, {
              action: 'call',
              abilityName: 'WidgetCalleeEntryAbility', // 只能拉起当前应用下的UIAbility
              params: {
                method: 'funA',
                formId: this.formId,
                calleeDetail: 'CallFrom'
              }
            });
          })
        }.width('100%').height('40%')
        .justifyContent(FlexAlign.Center)
      }
      .width('100%')
      .height('100%')
      .alignItems(HorizontalAlign.Start)
      // $r('app.media.CardEvent')需要替换为开发者所需的资源文件
      .backgroundImage($r('app.media.CardEvent'))
      .backgroundImageSize(ImageSize.Cover)
    }
  }
  ```
* 在UIAbility的onCreate生命周期中监听call事件所需的方法，然后在对应方法中调用[updateForm](../harmonyos-references/js-apis-app-form-formprovider.md#formproviderupdateform)接口刷新卡片。

  ```typescript
  // entry/src/main/ets/widgetcalleeentryability/WidgetCalleeEntryAbility.ts
  import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
  import { window } from '@kit.ArkUI';
  import { BusinessError } from '@kit.BasicServicesKit';
  import { formBindingData, formProvider } from '@kit.FormKit';
  import { rpc } from '@kit.IPCKit';
  import { hilog } from '@kit.PerformanceAnalysisKit';

  const TAG: string = 'WidgetCalleeEntryAbility';
  const DOMAIN_NUMBER: number = 0xFF00;
  const MSG_SEND_METHOD: string = 'funA';
  const CONST_NUMBER_1: number = 1;

  class MyParcelable implements rpc.Parcelable {
    num: number;
    str: string;

    constructor(num: number, str: string) {
      this.num = num;
      this.str = str;
    };

    marshalling(messageSequence: rpc.MessageSequence): boolean {
      messageSequence.writeInt(this.num);
      messageSequence.writeString(this.str);
      return true;
    };

    unmarshalling(messageSequence: rpc.MessageSequence): boolean {
      this.num = messageSequence.readInt();
      this.str = messageSequence.readString();
      return true;
    };
  }

  // 在收到call事件后会触发callee监听的方法
  let funACall = (data: rpc.MessageSequence): MyParcelable => {
    // 获取call事件中传递的所有参数
    let params: Record<string, string> = JSON.parse(data.readString());
    if (params.formId !== undefined) {
      let curFormId: string = params.formId;
      let message: string = params.calleeDetail;
      hilog.info(DOMAIN_NUMBER, TAG, `UpdateForm formId: ${curFormId}, message: ${message}`);
      let formData: Record<string, string> = {
        'calleeDetail': message
      };
      let formMsg: formBindingData.FormBindingData = formBindingData.createFormBindingData(formData);
      formProvider.updateForm(curFormId, formMsg).then((data) => {
        hilog.info(DOMAIN_NUMBER, TAG, `updateForm success. ${JSON.stringify(data)}`);
      }).catch((error: BusinessError) => {
        hilog.error(DOMAIN_NUMBER, TAG, `updateForm failed: ${JSON.stringify(error)}`);
      });
    }
    return new MyParcelable(CONST_NUMBER_1, 'aaa');
  };

  export default class WidgetCalleeEntryAbility extends UIAbility {
    onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
      try {
        // 监听call事件所需的方法
        this.callee.on(MSG_SEND_METHOD, funACall);
      } catch (error) {
        hilog.error(DOMAIN_NUMBER, TAG, `${MSG_SEND_METHOD} register failed with error ${JSON.stringify(error)}`);
      }
    }

    onWindowStageCreate(windowStage: window.WindowStage): void {
      // Main window is created, set main page for this ability
      hilog.info(DOMAIN_NUMBER, TAG, '%{public}s', 'Ability onWindowStageCreate');

      windowStage.loadContent('pages/Index', (err, data) => {
        if (err.code) {
          hilog.error(DOMAIN_NUMBER, TAG, 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
          return;
        }
        hilog.info(DOMAIN_NUMBER, TAG, 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
      });
    }
  }
  ```

  要拉起UIAbility至后台，需要在module.json5配置文件中，配置ohos.permission.KEEP\_BACKGROUND\_RUNNING权限。

  ```json5
  //src/main/module.json5
  "requestPermissions": [
    {
      "name": "ohos.permission.KEEP_BACKGROUND_RUNNING",
    },
  // ···
  ]
  ```
