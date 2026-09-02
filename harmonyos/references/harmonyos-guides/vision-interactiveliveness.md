---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/vision-interactiveliveness
title: 人脸活体检测
breadcrumb: 指南 > AI > Vision Kit（场景化视觉服务） > 人脸活体检测
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:15+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e4f7a155933139e489976ca9c84cfabfe84c660f09c80b28282303cae322056a
---

## 场景介绍

人脸活体检测支持动作活体检测模式。

动作活体检测支持实时捕捉人脸，需要用户配合做指定动作就可以判断是真实活体，还是非活体攻击（比如：打印图片、人脸翻拍视频以及人脸面具等）。

**说明** 

活体检测是一项纯端侧算法、试用期免费的系统基础服务，推荐开发者使用在考勤打卡、辅助登录和实名认证等低危业务场景中。活体检测减少动作数量或者指定特定动作会降低其安全性，增加被攻破的风险。

端侧算法在HarmonyOS NEXT/5.0.x已完成权威机构（CFCA）检测认证。鉴于支付和金融应用的高风险性，建议开发者基于现有的安全性，针对不同的功能场景进行风险评估和风控策略评估，并采取必要的安全措施。

**图1** 权威认证**增强级**检测报告

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/L65dHT8YSUOoQlZ-3koYxg/zh-cn_image_0000002706675492.png)

**图2** 活体检测示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/dQGGwhF1R6uueiVOe8qgjg/zh-cn_image_0000002736434579.png)

## 约束与限制

* 平板仅支持竖屏检测，大折叠屏仅支持折叠时使用，小折叠屏仅支持展开时使用。
* 支持的文本语种类型：简体中文、繁体中文、英文、维吾尔文、藏文。
* 支持的播报语种类型：简体中文、英文。
* 人脸活体检测服务暂不支持横屏、分屏进行检测。
* 人脸图像清晰、完整，环境光线充足，无强光直射，无反光，无遮挡。

## 接口说明

以下仅列出demo中调用的部分主要接口，具体API说明详见[API参考](../harmonyos-references/vision-interactive-liveness.md)。

| 接口名 | 描述 |
| --- | --- |
| [startLivenessDetection](../harmonyos-references/vision-interactive-liveness.md#startlivenessdetection)(config: InteractiveLivenessConfig): Promise<boolean> | 跳转到人脸活体检测页面的入口 |
| [getInteractiveLivenessResult](../harmonyos-references/vision-interactive-liveness.md#getinteractivelivenessresult)(): Promise<InteractiveLivenessResult> | 获取人脸活体检测的结果。使用Promise异步回调 |

## 开发步骤

1. 将实现人脸活体检测相关的类添加至工程。

   ```typescript
   import { common, abilityAccessCtrl, Permissions } from '@kit.AbilityKit';
   import { interactiveLiveness } from '@kit.VisionKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 在module.json5文件中添加CAMERA权限，其中reason，abilities标签必填，配置方式参见[requestPermissions标签说明](declare-permissions.md#在配置文件中声明权限)。

   ```typescript
   "requestPermissions":[
     {
       "name": "ohos.permission.CAMERA",
       "reason": "$string:camera_desc",
       "usedScene": {"abilities": []}
     }
   ]
   ```
3. 简单配置页面的布局，选择人脸活体检测验证完后的跳转模式。如果使用back跳转模式，表示人脸活体检测完成后返回到上一页。如果使用replace跳转模式，表示人脸活体检测完跳转到成功或失败页面。默认选择的是replace跳转模式。

   ```typescript
   Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
     Text('验证完的跳转模式：')
       .fontSize(18)
       .width('25%')
     Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
       Row() {
         Radio({ value: 'replace', group: 'routeMode' }).checked(true)
           .height(24)
           .width(24)
           .onChange((isChecked: boolean) => {
             this.routeMode = 'replace';
           })
         Text('replace')
           .fontSize(16)
       }
       .margin({ right: 15 })

       Row() {
         Radio({ value: 'back', group: 'routeMode' }).checked(false)
           .height(24)
           .width(24)
           .onChange((isChecked: boolean) => {
             this.routeMode = 'back';
           })
         Text('back')
           .fontSize(16)
       }
     }
     .width('75%')
   }
   ```
4. 如果选择动作活体模式，可填写验证的动作个数。

   ```typescript
   Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
     Text('动作数量：')
       .fontSize(18)
       .width('25%')
     TextInput({
       placeholder: this.actionsNum != 0 ? this.actionsNum.toString() : '动作数量为3或4个'
     })
       .type(InputType.Number)
       .placeholderFont({
         size: 18,
         weight: FontWeight.Normal,
         family: 'HarmonyHeiTi',
         style: FontStyle.Normal
       })
       .fontSize(18)
       .fontWeight(FontWeight.Bold)
       .fontFamily('HarmonyHeiTi')
       .fontStyle(FontStyle.Normal)
       .width('65%')
       .onChange((value: string) => {
         this.actionsNum = Number(value) as interactiveLiveness.ActionsNumber;
       })
   }
   ```
5. 点击“开始检测”按钮，触发点击事件。

   ```typescript
   Button('开始检测', { type: ButtonType.Normal, stateEffect: true })
     .width(192)
     .height(40)
     .fontSize(16)
     .backgroundColor(0x317aff)
     .borderRadius(20)
     .margin({
       bottom: 56
     })
     .onClick(() => {
       this.startDetection();
     })
   ```
6. 触发CAMERA权限校验。

   ```typescript
   private context: common.UIAbilityContext = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
   private array: Array<Permissions> = ['ohos.permission.CAMERA'];
   // 校验CAMERA权限
   private startDetection() {
     abilityAccessCtrl.createAtManager().requestPermissionsFromUser(this.context, this.array).then((res) => {
       for (let i = 0; i < res.permissions.length; i++) {
         if (res.permissions[i] === 'ohos.permission.CAMERA' && res.authResults[i] === 0) {
           this.routerLibrary();
         }
       }
     }).catch((err: BusinessError) => {
       hilog.error(0x0001, 'LivenessCollectionIndex', `Failed to request permissions from user. Code is ${err.code}, message is ${err.message}`);
     });
   }
   ```
7. 配置人脸活体检测控件的配置项[InteractiveLivenessConfig](../harmonyos-references/vision-interactive-liveness.md#interactivelivenessconfig)，用于跳转到人脸活体检测控件。

   配置中具体的参数可参考[API文档](../harmonyos-references/vision-interactive-liveness.md)。

   ```typescript
   let routerOptions: interactiveLiveness.InteractiveLivenessConfig = {
     isSilentMode: this.isSilentMode as interactiveLiveness.DetectionMode,
     routeMode: this.routeMode as interactiveLiveness.RouteRedirectionMode,
     actionsNum: this.actionsNum
   };
   ```
8. 调用interactiveLiveness的[startLivenessDetection](../harmonyos-references/vision-interactive-liveness.md#startlivenessdetection)接口，判断跳转到人脸活体检测控件是否成功。

   ```typescript
   private routerLibrary() {
     if (canIUse('SystemCapability.AI.Component.LivenessDetect')) {
       interactiveLiveness.startLivenessDetection(routerOptions).then((isSuccess) => {
         if (isSuccess) {
            hilog.info(0x0001, 'LivenessCollectionIndex', `Succeeded in jumping.`);
          } else {
            hilog.info(0x0001, 'LivenessCollectionIndex', `Redirection failed.`);
          }
       }).catch((err: BusinessError) => {
         hilog.error(0x0001, 'LivenessCollectionIndex', `Failed to jump. Code: ${err.code}, message: ${err.message}`);
       });
     } else {
       hilog.error(0x0001, 'LivenessCollectionIndex', 'this api is not supported on this device');
     }
   }
   ```
9. 检测结束后回到当前界面，可调用interactiveLiveness的[getInteractiveLivenessResult](../harmonyos-references/vision-interactive-liveness.md#getinteractivelivenessresult)接口，验证人脸活体检测的结果。

   ```typescript
   // 获取验证结果
   private getDetectionResultInfo() {
     // getInteractiveLivenessResult接口调用完会释放资源
     if (canIUse('SystemCapability.AI.Component.LivenessDetect')) {
       let resultInfo = interactiveLiveness.getInteractiveLivenessResult();
       resultInfo.then(data => {
         this.resultInfo = data;
       }).catch((err: BusinessError) => {
         this.failResult = {
           'code': err.code,
           'message': err.message
         };
       });
     } else {
       hilog.error(0x0001, 'LivenessCollectionIndex', 'this api is not supported on this device');
     }
   }
   ```

## 开发实例

### Index.ets

```typescript
import { common, abilityAccessCtrl, Permissions } from '@kit.AbilityKit';
import { interactiveLiveness } from '@kit.VisionKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct LivenessCollectionIndex{
  private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
  private array: Array<Permissions> = ['ohos.permission.CAMERA'];
  @State actionsNum: number = 0;
  @State isSilentMode: string = 'INTERACTIVE_MODE';
  @State routeMode: string = 'replace';
  @State resultInfo: interactiveLiveness.InteractiveLivenessResult = {
    livenessType: 0
  };
  @State failResult: Record<string, number | string> = {
    'code': 1008302000,
    'message': ''
  };

  build() {
    Stack({
      alignContent: Alignment.Top
    }) {
      Column() {
        Row() {
          Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
            Text('验证完的跳转模式：')
              .fontSize(18)
              .width('25%')
            Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
              Row() {
                Radio({ value: 'replace', group: 'routeMode' }).checked(true)
                  .height(24)
                  .width(24)
                  .onChange(() => {
                    this.routeMode = 'replace';
                  })
                Text('replace')
                  .fontSize(16)
              }
              .margin({ right: 15 })

              Row() {
                Radio({ value: 'back', group: 'routeMode' }).checked(false)
                  .height(24)
                  .width(24)
                  .onChange(() => {
                    this.routeMode = 'back';
                  })
                Text('back')
                  .fontSize(16)
              }
            }
            .width('75%')
          }
        }
        .margin({ bottom: 30 })

          Row() {
            Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
              Text('动作数量：')
                .fontSize(18)
                .width('25%')
              TextInput({
                placeholder: this.actionsNum != 0 ? this.actionsNum.toString() : '动作数量为3或4个'
              })
                .type(InputType.Number)
                .placeholderFont({
                  size: 18,
                  weight: FontWeight.Normal,
                  family: 'HarmonyHeiTi',
                  style: FontStyle.Normal
                })
                .fontSize(18)
                .fontWeight(FontWeight.Bold)
                .fontFamily('HarmonyHeiTi')
                .fontStyle(FontStyle.Normal)
                .width('65%')
                .onChange((value: string) => {
                  this.actionsNum = Number(value) as interactiveLiveness.ActionsNumber;
                })
            }
          }
      }
      .margin({ left: 24, top: 80 })
      .zIndex(1)

      Stack({
        alignContent: Alignment.Bottom
      }) {
        if (this.resultInfo?.mPixelMap) {
          Image(this.resultInfo?.mPixelMap)
            .width(260)
            .height(260)
            .align(Alignment.Center)
            .margin({ bottom: 260 })
          Circle()
            .width(300)
            .height(300)
            .fillOpacity(0)
            .strokeWidth(60)
            .stroke(Color.White)
            .margin({ bottom: 250, left: 0 })
        }

        Text(this.resultInfo.mPixelMap ?
          '检测成功' :
          this.failResult.code != 1008302000 ?
            '检测失败' :
            '')
          .width('100%')
          .height(26)
          .fontSize(20)
          .fontColor('#000000')
          .fontFamily('HarmonyHeiTi')
          .margin({ top: 50 })
          .textAlign(TextAlign.Center)
          .fontWeight('Medium')
          .margin({ bottom: 240 })

        if (this.failResult.code != 1008302000) {
          Text(this.failResult.message as string)
            .width('100%')
            .height(26)
            .fontSize(16)
            .fontColor(Color.Gray)
            .textAlign(TextAlign.Center)
            .fontFamily('HarmonyHeiTi')
            .fontWeight('Medium')
            .margin({ bottom: 200 })
        }

        Button('开始检测', { type: ButtonType.Normal, stateEffect: true })
          .width(192)
          .height(40)
          .fontSize(16)
          .backgroundColor(0x317aff)
          .borderRadius(20)
          .margin({
            bottom: 56
          })
          .onClick(() => {
            this.startDetection();
          })
      }
      .height('100%')
    }
  }

  onPageShow() {
    this.resultRelease();
    this.getDetectionResultInfo();
  }

  // 配置人脸活体检测参数并调用检测接口
  private routerLibrary() {
    let routerOptions: interactiveLiveness.InteractiveLivenessConfig = {
      isSilentMode: this.isSilentMode as interactiveLiveness.DetectionMode,
      routeMode: this.routeMode as interactiveLiveness.RouteRedirectionMode,
      actionsNum: this.actionsNum
    };

    if (canIUse('SystemCapability.AI.Component.LivenessDetect')) {
      interactiveLiveness.startLivenessDetection(routerOptions).then((isSuccess) => {
        if (isSuccess) {
            hilog.info(0x0001, 'LivenessCollectionIndex', `Succeeded in jumping.`);
          } else {
            hilog.info(0x0001, 'LivenessCollectionIndex', `Redirection failed.`);
          }
      }).catch((err: BusinessError) => {
        hilog.error(0x0001, 'LivenessCollectionIndex', `Failed to jump. Code: ${err.code}, message: ${err.message}`);
      });
    } else {
      hilog.error(0x0001, 'LivenessCollectionIndex', 'this api is not supported on this device');
    }
  }

  // 校验CAMERA权限
  private startDetection() {
    abilityAccessCtrl.createAtManager().requestPermissionsFromUser(this.context, this.array).then((res) => {
      for (let i = 0; i < res.permissions.length; i++) {
        if (res.permissions[i] === 'ohos.permission.CAMERA' && res.authResults[i] === 0) {
        this.routerLibrary();
      }
     }
    }).catch((err: BusinessError) => {
      hilog.error(0x0001, 'LivenessCollectionIndex', `Failed to request permissions from user. Code is ${err.code}, message is ${err.message}`);
    });
  }

  // 获取验证结果
  private getDetectionResultInfo() {
    // getInteractiveLivenessResult接口调用完会释放资源
    if (canIUse('SystemCapability.AI.Component.LivenessDetect')) {
      interactiveLiveness.getInteractiveLivenessResult().then(data => {
        this.resultInfo = data;
      }).catch((err: BusinessError) => {
        this.failResult = {
          'code': err.code,
          'message': err.message
        };
      });
    } else {
      hilog.error(0x0001, 'LivenessCollectionIndex', 'this api is not supported on this device');
    }
  }

  // result release
  private resultRelease() {
    this.resultInfo = {
      livenessType: 0
    };
    this.failResult = {
      'code': 1008302000,
      'message': ''
    };
  }
}
```
