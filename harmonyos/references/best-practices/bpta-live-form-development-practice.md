---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-live-form-development-practice
title: 互动卡片开发实践
breadcrumb: 最佳实践 > 技术创新 > 互动卡片开发实践
category: best-practices
scraped_at: 2026-09-02T15:03:15+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:9971fb82aa02aff9b8b98679b1183f24c9dd982fc6d79b02e2481aa98f8bfa7a
---

## 概述

[场景动效类型互动卡片](../harmonyos-guides/arkts-ui-liveform-sceneanimation.md)（本文后续简称为互动卡片），是一种支持动态动画和实时交互的卡片形态，区别于动态卡片，互动卡片能够在用户触发时展示流畅的帧动画、3D变换效果，并支持陀螺仪等传感器交互，还能将动效渲染区域扩展到卡片自身边界之外，营造“破框”效果。互动卡片包含非激活态和激活态两种状态：非激活态下，卡片与普通卡片行为一致，由FormExtensionAbility管理；激活态下，由LiveFormExtensionAbility加载动态UI页面展示动画和交互内容。

**说明** 

互动卡片包含趣味交互类型互动卡片和场景动效类型互动卡片两种类型，本文仅介绍**场景动效类型互动卡片**。

在阅读本文之前，建议先了解HarmonyOS卡片开发基础、ArkTS语法和[UIAbility生命周期](../harmonyos-guides/uiability-lifecycle.md)，并准备好DevEco Studio 6.1.0 Release及以上版本的开发环境。

## 场景介绍

本项目包含四种互动卡片，分别对应不同的交互场景和体验效果：

| 卡片名称 | 用途 | 实现方式 |
| --- | --- | --- |
| 睡眠卡片 | 状态提醒 | 帧动画、点击切换 |
| 快递卡片 | 动态呈现用户快递状态，当前演示状态为“运输中” | 帧动画、陀螺仪交互 |
| 运动卡片 | 开始运动、结束运动 | 帧动画、点击交互 |
| 音乐卡片 | 切歌、暂停等音频控制 | Canvas自绘制、点击交互 |

### 睡眠卡片

**触发方式**

点击。

**体验及交互**

点击卡片触发憨憨起床动画，三叶草旋转，气球飘出卡片边界，憨憨从睡姿变为醒姿，动画结束后卡片状态更新为“按时起床”。

**效果预览**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/quxqHEHkTbKo2PLm_sBc-w/zh-cn_image_0000002623694219.gif "点击放大")

### 快递卡片

**触发方式**

点击、摇一摇。

**体验及交互**

**点击****卡片**或**摇动****设备**激活卡片后，倾斜手机驱动憨憨沿路线跑动——向右倾斜憨憨向右移动并缩小（近→远透视），向左倾斜憨憨向左移动并放大（远→近透视）。

**效果预览**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/vBbvqzFAQzq9knnh4jRbeA/zh-cn_image_0000002623534345.gif "点击放大")

### 运动卡片

**触发方式**

点击。

**体验及交互**

* 开始运动：点击“开始运动”触发憨憨拉伸运动动画。
* 结束运动：点击“结束运动”触发庆祝动画并显示卡路里计数，从0逐步增长到300kcal。

**效果预览**

* 开始运动

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/zuqp166gQrWSL-WUoutFJg/zh-cn_image_0000002593094810.gif "点击放大")
* 结束运动

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/LfZHljUhR1WBLXRgo0hO4w/zh-cn_image_0000002593254736.gif "点击放大")

### 音乐卡片

**触发方式**

点击。

**体验及交互**

* 播放：播放音乐时憨憨跳舞、专辑封面旋转。
* 切歌：切歌时憨憨出框取专辑进行替换。

**效果预览**

* 播放：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/Q-UHy3Y9RTGBZ3Kmwp5pJw/zh-cn_image_0000002623694221.gif "点击放大")
* 切歌：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/kbuaoXdOT9-eH9NkkBIHxQ/zh-cn_image_0000002623534347.gif "点击放大")

## 整体方案

互动卡片以动态卡片作为入口，通过form\_config.json中的[sceneAnimationParams标签](../harmonyos-guides/arkts-ui-widget-configuration.md#sceneanimationparams标签)配置关联LiveFormExtensionAbility。用户触发激活（点击或摇一摇）后，系统根据sceneAnimationParams.abilityName激活对应的LiveFormExtensionAbility实例，调用[onLiveFormCreate](../harmonyos-references/js-apis-app-form-liveformextensionability.md#onliveformcreate)方法加载动态UI页面，展示动画和交互内容。详见互动卡片[实现原理](../harmonyos-guides/arkts-ui-liveform-sceneanimation-overview.md#实现原理)。

### 动态卡片创建

[动态卡片](../harmonyos-guides/arkts-form-overview.md#动态卡片)是互动卡片的入口，开发者需按照[创建ArkTS卡片](../harmonyos-guides/arkts-ui-widget-creation.md)流程进行创建。

### 互动卡片配置及触发方法

互动卡片的配置和触发涉及三个关键部分：

1. 在module.json5的extensionAbilities中声明[LiveFormExtensionAbility](../harmonyos-references/js-apis-app-form-liveformextensionability.md#liveformextensionability)，type设置为liveForm，声明为互动卡片。

```screen
{
  "name": "DeliveryLiveCardAbility",
  "srcEntry": "./ets/livecardability/DeliveryLiveCardAbility.ets",
  "type": "liveForm",
  "exported": false
},
```

2. 在form\_config.json中通过sceneAnimationParams.abilityName指定触发动画时激活的[LiveFormExtensionAbility](../harmonyos-references/js-apis-app-form-liveformextensionability.md#liveformextensionability)名称。

3. 触发方式

互动卡片支持两种触发方式：

* 点击触发：用户点击卡片时，卡片通过[postCardAction](../harmonyos-references/js-apis-postcardaction.md)(MESSAGE)发送requestOverflow消息到FormExtensionAbility，FormExtensionAbility调用[formProvider.requestOverflow](../harmonyos-references/js-apis-app-form-formprovider.md#formproviderrequestoverflow20)激活互动卡片。
* 摇一摇触发：在form\_config.json中通过sceneAnimationParams.triggerTypes增加"shake"字段，系统自动监听摇动事件并激活LiveFormExtensionAbility。

摇一摇触发流程：

| **步骤** | **操作** | **说明** |
| --- | --- | --- |
| 1 | 用户摇动设备 | 系统识别摇一摇事件 |
| 2 | 查找sceneAnimationParams.triggerTypes配置的卡片 | 匹配支持的卡片 |
| 3 | 读取sceneAnimationParams.abilityName | 获取LiveFormExtensionAbility名称 |
| 4 | 触发FormExtensionAbility的onUpdateForm方法 | 系统将摇一摇事件发送给卡片 |
| 5 | 调用requestOverflow请求激活互动卡片 | FormExtensionAbility中主动拉起激活互动卡片 |
| 6 | 创建LiveFormExtensionAbility实例 | 系统自动创建 |
| 7 | 调用onLiveFormCreate方法 | 加载动画UI |

**说明** 

摇一摇激活互动卡片能力仅在HarmonyOS 7.0及以上版本触发。

### 通信方式

[动态卡片](../harmonyos-guides/arkts-form-overview.md#动态卡片)、应用和互动卡片三者之间存在多种通信方式，不同通信方向使用不同的API和数据传递机制：

| **通信方向** | **方式** | **核心API** | **说明** |
| --- | --- | --- | --- |
| 动态卡片 → 应用(EntryAbility) | 页面跳转 | [postCardAction](../harmonyos-references/js-apis-postcardaction.md)(ROUTER) | 点击卡片跳转到应用页面 |
| 动态卡片 → 应用(EntryAbility) | 方法调用 | [postCardAction](../harmonyos-references/js-apis-postcardaction.md)(CALL) | 通过[Callee](../harmonyos-references/js-apis-app-ability-uiability.md#callee)监听调用应用方法 |
| 动态卡片 → FormExtensionAbility | 发送消息 | [postCardAction](../harmonyos-references/js-apis-postcardaction.md)(MESSAGE) | 通过[FormExtensionAbility.onFormEvent](../harmonyos-references/js-apis-app-form-formextensionability.md#formextensionabilityonformevent)接收处理消息 |
| 应用 → 动态卡片 | 数据推送 | [formProvider.updateForm](../harmonyos-references/js-apis-application-formprovider.md#formproviderupdateform) + [formBindingData](../harmonyos-references/js-apis-app-form-formbindingdata.md#formbindingdata) | 键值对自动映射到[@LocalStorageProp](../harmonyos-guides/arkts-localstorage.md#localstorageprop) |
| 应用 → 互动卡片 | 数据持久化 | [@ohos.data.preferences (用户首选项)](../harmonyos-references/js-apis-data-preferences.md)/ [@ohos.data.relationalStore (关系型数据库)](../harmonyos-references/js-apis-data-relationalstore.md) / 文件存储 | 跨进程通信，[LiveFormExtensionAbility](../harmonyos-references/js-apis-app-form-liveformextensionability.md#liveformextensionability)读取 |
| 互动卡片内部 | 共享存储 | [LocalStorage](../harmonyos-references/ts-state-management.md#localstorage9) | 同一进程内，[LiveFormExtensionAbility](../harmonyos-references/js-apis-app-form-liveformextensionability.md#liveformextensionability)→ 互动卡片UI |
| 互动卡片 → 动态卡片 | 数据回推 | [formProvider.updateForm](../harmonyos-references/js-apis-application-formprovider.md#formproviderupdateform) | 互动卡片状态变化回推到动态卡片 |

各卡片使用的通信方式如下：

**睡眠卡片**：使用ROUTER跳转页面（CloverPage、SleepReport）、MESSAGE触发出框动画、formProvider.updateForm回推isSleep状态到动态卡片。LocalStorage在互动卡片内部传递formRect、borderRadius等初始数据。

**音乐卡片**：使用CALL调用播控方法（播放/暂停/切歌/收藏）、ROUTER跳转页面（MusicPage）、MESSAGE触发出框动画并携带triggerAction上下文。应用与互动卡片间通过RDB存储歌曲列表和收藏状态、文件存储触发动作上下文和当前歌曲，实现跨进程数据同步。应用在切歌、播放状态改变时，通过formProvider.updateForm将歌曲信息同步到所有动态卡片中。

**运动卡片**：使用CALL调用运动控制方法（开始/结束/重置）、ROUTER跳转页面（ExercisePage）、MESSAGE触发出框动画。应用与互动卡片间通过文件存储持久化运动状态，互动卡片通过formProvider.updateForm回推卡路里数据到动态卡片。

**快递卡片**：使用ROUTER跳转页面（DeliveryPage）、MESSAGE触发出框动画。互动卡片内部通过LocalStorage传递formRect、borderRadius等初始数据。

## 快递卡片详细开发步骤

### 场景描述

以快递卡片为例，演示完整的互动卡片开发流程。快递卡片需要实现点击触发出框动画、陀螺仪交互驱动憨憨移动、摇一摇激活等功能。效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/3cFP8NPCSTOYIgb_c10sWQ/zh-cn_image_0000002593094812.gif "点击放大")

### 实现原理

快递卡片涉及动态卡片UI、[LiveFormExtensionAbility](../harmonyos-references/js-apis-app-form-liveformextensionability.md#liveformextensionability)、数据通信、陀螺仪交互四个核心模块。动态卡片展示背景和憨憨；LiveFormExtensionAbility加载动画UI并传递卡片尺寸信息；通信机制实现点击触发动画和页面跳转；陀螺仪交互实现憨憨实时响应设备倾斜。

### 开发步骤

**配置卡片和Ability**

1. 配置form\_config.json：定义快递卡片基本信息、配置LiveFormExtensionAbility和摇一摇支持。

   ```json
   {
     "name": "DeliveryCard",
     "displayName": "$string:DeliveryCard",
     "description": "$string:DeliveryCardDes",
     "src": "./ets/widget/pages/DeliveryCard.ets",
     "uiSyntax": "arkts",
     // ...
     "defaultDimension": "2*2",
     "supportDimensions": [
       "2*2"
     ],
     "sceneAnimationParams": {
       "abilityName": "DeliveryLiveCardAbility",
       "triggerTypes": ["shake"]
     }
   }
   ```
2. 声明DeliveryLiveCardAbility：在module.json5中声明LiveFormExtensionAbility扩展能力。

   ```screen
   {
     "name": "DeliveryLiveCardAbility",
     "srcEntry": "./ets/livecardability/DeliveryLiveCardAbility.ets",
     "type": "liveForm",
     "exported": false
   },
   ```

**实现动态卡片UI**

创建DeliveryCard页面：展示背景图片、憨憨图片，点击触发动画激活。

```screen
let storageUpdateCall = new LocalStorage();

@Entry(storageUpdateCall)
@Component
struct DeliveryCard {
  @LocalStorageProp('formWidth') formWidth: number = 0;
  @LocalStorageProp('formHeight') formHeight: number = 0;

  build() {
    RelativeContainer() {
      Image($rawfile('delivery/background.png'))
        .objectFit(ImageFit.Contain)
        .width('100%')
        .height('100%')
        .aspectRatio(1);
      Image($rawfile('delivery/fuzzball.png'))
        .objectFit(ImageFit.Contain)
        .width('145%')
        .height('145%')
        .offset({
          x: `-22.5%`,
          y: `-22.5%`
        });
      Row() {
        Image($r('app.media.delivery_box'))
          .objectFit(ImageFit.Contain)
          .width(this.formWidth * 0.2 + 'px')
          .height(this.formHeight * 0.2 + 'px');
        Text($r('app.string.delivery_in_transit'))
          .fontSize('21.55f')
          .fontColor('#646166')
          .fontFamily('HarmonyOS Scans SC');
      }
      .justifyContent(FlexAlign.SpaceEvenly)
      .alignRules({
        middle: { anchor: '__container__', align: HorizontalAlign.Center },
        bottom: { anchor: '__container__', align: VerticalAlign.Bottom }
      })
      .backgroundColor('#BFFFFFFF')
      .width(this.formWidth * 0.830 + 'px')
      .height(this.formHeight * 0.205 + 'px')
      .margin({ bottom: this.formHeight * 0.082 + 'px' })
      .borderRadius('9%');
      Stack()
        .width('100%')
        .height('30%')
        .onClick(() => {
          ActionUtils.jumpAppPage(this, 'DeliveryPage');
        })
        .alignRules({
          left: { anchor: '__container__', align: HorizontalAlign.Start },
          bottom: { anchor: '__container__', align: VerticalAlign.Bottom }
        });
    }
    .width('100%')
    .height('100%')
    .onClick(() => {
      ActionUtils.requestOverFlow(this, LiveCardScale.DELIVERY_WIDTH,
        LiveCardScale.DELIVERY_HEIGHT, LIVE_CARD_DURATION);
    });
  }
}
```

**实现LiveFormExtensionAbility**

创建DeliveryLiveCardAbility：在onLiveFormCreate中存储卡片信息并加载动态UI。

```screen
onLiveFormCreate(liveFormInfo: LiveFormInfo, session: UIExtensionContentSession): void {
  let storage: LocalStorage = new LocalStorage();
  storage.setOrCreate('context', this.context);
  storage.setOrCreate('session', session);
  let formId: string = liveFormInfo.formId;
  storage.setOrCreate('formId', formId);

  let borderRadius: number = liveFormInfo.borderRadius;
  storage.setOrCreate('borderRadius', borderRadius);

  let formRect: formInfo.Rect = liveFormInfo.rect;
  storage.setOrCreate('formRect', formRect);

  try {
    session.loadContent('livecardability/pages/DeliveryLiveCard', storage);
  } catch (error) {
    Logger.error(TAG, `session.loadContent error`);
  }
}
```

**实现互动卡片激活流程**

1. 处理message类型消息：在FormExtensionAbility的onFormEvent中接收requestOverflow消息，激活互动卡片动画。

   ```screen
   onFormEvent(formId: string, message: string): void {
     const params: Record<string, Object> = JSON.parse(message);
     if (!params || typeof params.message !== 'string') {
       return;
     }
     let shortMessage: string = params.message as string;

     if (shortMessage === 'requestOverflow') {
       let widthRatio: number = Math.min(Math.max(params.widthRatio as number || 0, 0), LIVE_CARD_RATIO);
       let heightRatio: number = Math.min(Math.max(params.heightRatio as number || 0, 0), LIVE_CARD_RATIO);
       let duration: number = Math.min(Math.max(params.duration as number || 0, 0), LIVE_CARD_DURATION);
       // ...

       this.requestOverflow(formId, widthRatio, heightRatio, duration);
       return;
     } else if (shortMessage === 'updateRequestOverflowState') {
       updateRequestOverFlowState(formId, true);
     }
   }
   ```
2. 请求激活互动卡片。

   ```screen
   private async requestOverflow(formId: string, widthRatio: number, heightRatio: number,
     duration: number): Promise<void> {
     try {
       let formRect: formInfo.Rect = await formProvider.getFormRect(formId);
       // ...
       if (formRect.width <= 0 || formRect.height <= 0) {
         return;
       }
       let cardWidth = formRect.width * widthRatio;
       let cardHeight = formRect.height * heightRatio;
       let leftOffset = (formRect.width - cardWidth) / 2;
       let topOffset = (formRect.height - cardHeight) / 2;

       formProvider.requestOverflow(formId, {
         area: {
           left: leftOffset,
           top: topOffset,
           width: cardWidth,
           height: cardHeight
         },
         duration: duration
       }).catch((e: BusinessError) => {
         Logger.error(TAG, `requestOverflow error, code: ${e.code} message: ${e.message}`);
       }).finally(() => {
         const timeoutId = setTimeout(() => {
           updateRequestOverFlowState(formId, false);
           clearTimeout(timeoutId);
         }, 500)
       });
     } catch (error) {
       // ...
     }
   }
   ```

**实现互动卡片动画UI**

1. 创建DeliveryLiveCard页面。

   ```screen
   @Entry({ useSharedStorage: true })
   @Component
   struct DeliveryLiveCard {
     @LocalStorageProp('formRect') rect?: formInfo.Rect = undefined;
     @LocalStorageProp('borderRadius') radius: number = 0;
     // ...
     @State ballSize: number = 0.3;
     @State ballTranslateX: number = 150;
     @State ballY: number = 0;
     // ...
     build() {
       Stack({ alignContent: Alignment.TopStart }) {
         Image($rawfile('delivery/background.png'))
           .borderRadius(this.radius)
           .width(this.rect?.width || 0)
           .height(this.rect?.height || 0)
           .margin({
             top: this.rect?.top,
             left: this.rect?.left
           });
         Stack() {
           Image(this.img)
             .width('100%')
             .height('100%')
             .scale({
               x: this.ballSize,
               y: this.ballSize
             })
             .translate({
               x: this.ballTranslateX,
               y: this.ballY
             })
             // ...
         }
         // ...
       }
       .onClick(() => {
         formProvider.cancelOverflow(this.formId).catch(() => {
           Logger.error(TAG, `cancelOverflow error`);
         });
       })
       .width('100%')
       .height('100%');
     }

     // ...
   }
   ```
2. 订阅陀螺仪数据。

   ```screen
   subscribeGyroscope() {
     GyroscopeUtil.subscribe((data: GyroscopeData) => {
       this.gyroTranslateX = Math.max(-this.maxGyroValue, Math.min(this.maxGyroValue, data.y));
       this.gyroTranslateY = Math.max(-this.maxGyroValue, Math.min(this.maxGyroValue, data.x));
       this.gyroTranslateZ = Math.max(-this.maxGyroValue, Math.min(this.maxGyroValue, data.z));
       this.gyroMethod();
     });
   }
   ```
3. 更新憨憨位置。

   ```screen
   private updateBallPosition(): void {
     const normalizedValue = this.accumulatedY;
     // ...

     if (normalizedValue > this.threshold) {
       const t = Math.min((normalizedValue - this.threshold) / (1 - this.threshold), 1);
       this.targetBallX = t * 100; // towards right
       this.targetBallSize = 1 - t * 0.35;
       // ...
     } else if (normalizedValue < -this.threshold) {
       const t = Math.min((-normalizedValue - this.threshold) / (1 - this.threshold), 1);
       this.targetBallX = -t * 50; // towards left
       this.targetBallSize = 1 + t * 0.3;
       // ...
     } else {
       this.targetBallX = 0;
       this.targetBallSize = 1;
       // ...
     }
     // ...
   }
   ```
4. 触发动画变化。

   ```screen
   private animateBall(duration: number = 100): void {
     if (duration > 0) {
       this.getUIContext().animateTo({
         duration: duration,
         curve: Curve.Linear
       }, () => {
         this.ballTranslateX = this.targetBallX;
         this.ballSize = this.targetBallSize;
       });
     } else {
       this.ballTranslateX = this.targetBallX;
       this.ballSize = this.targetBallSize;
     }
   }
   ```

## 常见问题

### 互动卡片动画白屏

**问题描述**

点击卡片触发动画后，互动卡片UI显示白屏，动画内容未正常加载。

**可能根因**

在[onLiveFormCreate](../harmonyos-references/js-apis-app-form-liveformextensionability.md#onliveformcreate)中进行了异步操作后才调用[loadContent](../harmonyos-references/js-apis-app-ability-uiextensioncontentsession.md#loadcontent)，导致UI加载时机错误。loadContent必须在onLiveFormCreate中同步调用，异步数据加载应在loadContent之后执行。

**解决方案**

调整代码顺序，先同步调用loadContent加载UI，再执行异步数据获取操作：

1. 在onLiveFormCreate中先创建LocalStorage并调用session.loadContent加载UI页面。
2. loadContent必须在onLiveFormCreate中同步调用，确保UI框架在正确时机加载页面。
3. 异步数据获取操作（如网络请求、数据库读取等）应在loadContent之后执行，避免阻塞UI加载。

   ```screen
   onLiveFormCreate(liveFormInfo: LiveFormInfo, session: UIExtensionContentSession): void {
     let storage: LocalStorage = new LocalStorage();
     storage.setOrCreate('context', this.context);
     storage.setOrCreate('session', session);
     let formId: string = liveFormInfo.formId;
     storage.setOrCreate('formId', formId);

     let borderRadius: number = liveFormInfo.borderRadius;
     storage.setOrCreate('borderRadius', borderRadius);

     let formRect: formInfo.Rect = liveFormInfo.rect;
     storage.setOrCreate('formRect', formRect);

     try {
       session.loadContent('livecardability/pages/ExerciseLiveCard', storage);
     } catch (error) {
       Logger.error(TAG, 'loadContent error');
     }

     try {
       let savedState = ExerciseFileStore.readExerciseState(this.context);
       if (savedState === undefined) {
         savedState = ExerciseState.NOT_STARTED;
       }
       Logger.info(TAG, `savedState: ${savedState}`)
       storage.setOrCreate('exerciseState', savedState);
     } catch (err) {
       Logger.error(TAG, `readExerciseState error, code is ${err.code}, message is ${err.message}`);
       storage.setOrCreate('exerciseState', ExerciseState.NOT_STARTED);
     }
   }
   ```

### 动画切换不平滑

**问题描述**

陀螺仪控制憨憨移动时，动画切换出现卡顿或跳跃。

**可能根因**

更新频率和位移距离设置不合理，连续两段动画位移距离差距过大。

**解决方案**

优化动画参数配置，控制合理的过渡时间及位移距离：

```screen
private animateBall(duration: number = 100): void {
  if (duration > 0) {
    this.getUIContext().animateTo({
      duration: duration,
      curve: Curve.Linear
    }, () => {
      this.ballTranslateX = this.targetBallX;
      this.ballSize = this.targetBallSize;
    });
  } else {
    this.ballTranslateX = this.targetBallX;
    this.ballSize = this.targetBallSize;
  }
}
```

## 示例代码

* [互动卡片](https://gitcode.com/HarmonyOS_Samples/LiveCard)
