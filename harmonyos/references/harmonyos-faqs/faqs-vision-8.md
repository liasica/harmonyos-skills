---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-vision-8
title: 活体检测完成返回指定Navigation路由页面功能实现
breadcrumb: FAQ > AI功能开发 > 机器学习 > 场景化视觉（Vision） > 活体检测完成返回指定Navigation路由页面功能实现
category: harmonyos-faqs
scraped_at: 2026-09-02T14:55:00+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:e9eb09bcc9e389adc9cb23a0a74bcdcb2a23ebbca1fb736af3863d43f2c4ef45
---

## 问题现象

[startLivenessDetection](../harmonyos-references/vision-interactive-liveness.md#startlivenessdetection)接口的参数[InteractiveLivenessConfig](../harmonyos-references/vision-interactive-liveness.md#interactivelivenessconfig)中可以设置successfulRouteUrl和failedRouteUrl分别作为人脸活体检测成功/失败后跳转的页面路径。页面路由只支持Router方式，不支持Navigation方式。

如何实现检测结束后自动跳转到Navigation路由的指定页面？

## 背景知识

* 人脸活体检测具有两个同名startLivenessDetection接口：

  [startLivenessDetection](../harmonyos-references/vision-interactive-liveness.md#startlivenessdetection)跳转到人脸活体检测页面的入口，使用Promise异步回调；[startLivenessDetection](../harmonyos-references/vision-interactive-liveness.md#startlivenessdetection)跳转到人脸活体检测页面的入口，使用Promise异步回调获取跳转结果，使用callback回调获取检测结果。
* [Navigation路由操作](../harmonyos-guides/arkts-navigation-jump.md#路由操作)支持：页面跳转、页面替换、参数获取等多种。

## 解决方案

实现思路：在[startLivenessDetection](../harmonyos-references/vision-interactive-liveness.md#startlivenessdetection)接口的callback回调函数中获取检测结果，再根据检测结果调用NavPathStack.pushPath()（或NavPathStack.replacePath()）方法跳转到成功/失败页面。

具体步骤：

* 定义检测结果对象，可根据业务需求自定义实现，简单示例：

  ```ts
  /**
   * 人脸识别结果对象
   */
  export class DetectionResult {
    // 自定义code和message
    finalResult: Record<string, number | string>|undefined = undefined;
  }
  ```

* [startLivenessDetection](../harmonyos-references/vision-interactive-liveness.md#startlivenessdetection)接口的callback回调函数中获取检测结果：

  ```ts
  interactiveLiveness.startLivenessDetection(routerOptions, (err: BusinessError,
    result: interactiveLiveness.InteractiveLivenessResult | undefined) => { // 当路由跳转错误时，获取结果失败，result返回undefined
    let detectionResult: DetectionResult = new DetectionResult();
    if(err.code !== 0 && !result) { // 在发生错误如路由跳转失败/参数错误/权限被拒绝时，会抛出错误码，详见ArkTS API错误码
      console.error(`LivenessCollectionIndex failed to detect. Code: ${err.code}，message: ${err.message}`);
      detectionResult.finalResult = {
        'code': err.code,
        'message': 'Error'
      };

      this.pathStack.pushPath({name: 'StartLivenessDetectionFailed', param: detectionResult});
      return;
    }

    console.info(`LivenessCollectionIndex Succeeded in detecting result: ${result}`);

    if (result?.mPixelMap) {
      detectionResult.finalResult = {
        'code': 0,
        'message': 'Success'
      };

      this.pathStack.pushPath({name: 'StartLivenessDetectionSuccess', param: detectionResult});
    } else {
      detectionResult.finalResult = {
        'code': -1,
        'message': 'Failed'
      };
      this.pathStack.pushPath({name: 'Detection', param: detectionResult});
    }
  });
  ```
* 检测结果目标页面接收路由参数。

  ```ts
  .onReady((context: NavDestinationContext) => {
    this.pathStack = context.pathStack;
    let detectionResult: DetectionResult = this.pathStack.getParamByIndex(1) as DetectionResult;
    if (detectionResult?.finalResult) {
      let message = detectionResult?.finalResult['message'];
      console.info(`Detection result is ${message}.`);
    } else {
      console.info(`Detection result is succeed.`);
    }
  });
  ```

完整示例如下：

* 权限声明与路由配置（src/main/module.json5）：

  ```json
  {
    "module": {
      "name": "entry",
      "type": "entry",
      "description": "$string:module_desc",
      "mainElement": "EntryAbility",
      "deviceTypes": [
        "phone"
      ],
      "deliveryWithInstall": true,
      "installationFree": false,
      "pages": "$profile:main_pages",
      "routerMap": "$profile:route_map", // 路由配置
      "abilities": [
        {
          "name": "EntryAbility",
          "srcEntry": "./ets/entryability/EntryAbility.ets",
          "description": "$string:EntryAbility_desc",
          "icon": "$media:layered_image",
          "label": "$string:EntryAbility_label",
          "startWindowIcon": "$media:startIcon",
          "startWindowBackground": "$color:start_window_background",
          "exported": true,
          "skills": [
            {
              "entities": [
                "entity.system.home"
              ],
              "actions": [
                "ohos.want.action.home"
              ]
            }
          ]
        }
      ],
      "extensionAbilities": [
        {
          "name": "EntryBackupAbility",
          "srcEntry": "./ets/entrybackupability/EntryBackupAbility.ets",
          "type": "backup",
          "exported": false,
          "metadata": [
            {
              "name": "ohos.extension.backup",
              "resource": "$profile:backup_config"
            }
          ],
        }
      ],
      "requestPermissions": [ // 权限声明
        {
          "name": "ohos.permission.CAMERA",
          "reason": "$string:reason_of_camera",
          "usedScene": {
            "when": "always"
          }
        }
      ]
    }
  }
  ```
* 权限原因配置（src/main/resources/base/element/string.json）：

  ```json
  {
    "string": [
      {
        "name": "module_desc",
        "value": "module description"
      },
      {
        "name": "EntryAbility_desc",
        "value": "description"
      },
      {
        "name": "EntryAbility_label",
        "value": "label"
      },
      {
        "name": "reason_of_camera",
        "value": "活体检测"
      }
    ]
  }
  ```
* 路由配置文件（src/main/resources/base/profile/route\_map.json）：

  ```json
  {
    "routerMap": [
      {
        "name": "Detection",
        "pageSourceFile": "src/main/ets/pages/Detection.ets",
        "buildFunction": "DetectionBuilder",
        "data": {
          "description" : "this is Detection"
        }
      },
      {
        "name": "StartLivenessDetectionSuccess",
        "pageSourceFile": "src/main/ets/pages/StartLivenessDetectionSuccess.ets",
        "buildFunction": "StartLivenessDetectionSuccessBuilder",
        "data": {
          "description" : "this is StartLivenessDetectionSuccessBuilder"
        }
      },
      {
        "name": "StartLivenessDetectionFailed",
        "pageSourceFile": "src/main/ets/pages/StartLivenessDetectionFailed.ets",
        "buildFunction": "StartLivenessDetectionFailedBuilder",
        "data": {
          "description" : "this is StartLivenessDetectionFailedBuilder"
        }
      }
    ]
  }
  ```
* 首页（src/main/ets/pages/Index.ets）:

  ```ts
  @Entry
  @Component
  struct Index {
    pageInfos: NavPathStack = new NavPathStack();
    aboutToAppear(): void {
      let param = this.getUIContext().getRouter().getParams();
      if (param) {
        this.pageInfos.pushPath({name: 'StartLivenessDetectionSuccess'});
      }
    }
    build() {
      Navigation(this.pageInfos) {
        Column() {
          Button('去检测', { stateEffect: true, type: ButtonType.Capsule })
            .width('80%')
            .height(40)
            .margin(20)
            .onClick(() => {
              this.pageInfos.pushPath({ name: 'Detection' }); //将name指定的NavDestination页面信息入栈
            })
        }
      }
      .mode(NavigationMode.Auto)
      .title('首页')
    }
  }
  ```
* 检测页面（src/main/ets/pages/Detection.ets）：

  ```ts
  import { common, abilityAccessCtrl, Permissions } from '@kit.AbilityKit';
  import { interactiveLiveness } from '@kit.VisionKit';
  import { BusinessError } from '@kit.BasicServicesKit';

  /**
   * 人脸识别结果对象
   */
  export class DetectionResult {
    // 自定义code和message
    finalResult: Record<string, number | string>|undefined = undefined;
  }

  @Builder
  export function DetectionBuilder() {
    Detection()
  }

  @Component
  export struct Detection {
    private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    @State pathStack: NavPathStack = new NavPathStack();
    @State failResult: Record<string, number | string> = {
      'code': 1008302000,
      'message': ''
    };

    private array: Array<Permissions> = ['ohos.permission.CAMERA'];
    private actionsNum: number = 3;
    private isSilentMode: interactiveLiveness.DetectionMode.INTERACTIVE_MODE =
      interactiveLiveness.DetectionMode.INTERACTIVE_MODE;

    build() {
      NavDestination() {
        Stack({
          alignContent: Alignment.Top
        }) {
          Column() {
            Row() {
              Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
                Text('动作数量：' + this.actionsNum)
                  .fontSize(30)
                  .width('50%')
              }
            }
          }
          .margin({ left: 24, top: 80 })
          .zIndex(1)

          Stack({
            alignContent: Alignment.Bottom
          }) {
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
      }.title('检测页面')
      .onReady((context: NavDestinationContext) => {
        this.pathStack = context.pathStack;
        if (context.pathInfo.param) {
          let detectionResult = context.pathInfo.param as DetectionResult;
          if (detectionResult.finalResult) {
            this.failResult = detectionResult.finalResult;
          }
        }
      });
    }

    // 跳转到人脸活体检测控件
    private routerLibrary() {
      let routerOptions: interactiveLiveness.InteractiveLivenessConfig = {
        isSilentMode: this.isSilentMode,
        routeMode: interactiveLiveness.RouteRedirectionMode.BACK_MODE,
        actionsNum: this.actionsNum
      };

      if (canIUse('SystemCapability.AI.Component.LivenessDetect')) {
        interactiveLiveness.startLivenessDetection(routerOptions, (err: BusinessError,
          result: interactiveLiveness.InteractiveLivenessResult | undefined) => { // 当路由跳转错误时，获取结果失败，result返回undefined
          let detectionResult: DetectionResult = new DetectionResult();
          if(err.code !== 0 && !result) { // 在发生错误如路由跳转失败/参数错误/权限被拒绝时，会抛出错误码，详见ArkTS API错误码
            console.error(`LivenessCollectionIndex failed to detect. Code: ${err.code}，message: ${err.message}`);
            detectionResult.finalResult = {
              'code': err.code,
              'message': 'Error'
            };

            this.pathStack.pushPath({name: 'StartLivenessDetectionFailed', param: detectionResult});
            return;
          }

          console.info(`LivenessCollectionIndex Succeeded in detecting result: ${result}`);

          if (result?.mPixelMap) {
            detectionResult.finalResult = {
              'code': 0,
              'message': 'Success'
            };

            this.pathStack.pushPath({name: 'StartLivenessDetectionSuccess', param: detectionResult});
          } else {
            detectionResult.finalResult = {
              'code': -1,
              'message': 'Failed'
            };
            this.pathStack.pushPath({name: 'Detection', param: detectionResult});
          }
        });
      } else {
        console.error('LivenessCollectionIndex this api is not supported on this device');
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
        console.error(`Failed to request permissions from user. Code is ${err.code}, message is ${err.message}`);
      });
    }
  }
  ```
* 检测成功页面（src/main/ets/pages/StartLivenessDetectionSuccess.ets）：

  ```ts
  import { DetectionResult } from './Detection';

  @Builder
  export function StartLivenessDetectionSuccessBuilder() {
    StartLivenessDetectionSuccess()
  }

  @Component
  export struct StartLivenessDetectionSuccess {
    @State pathStack: NavPathStack = new NavPathStack();

    build() {
      NavDestination() {
        Stack({
          alignContent: Alignment.Top
        }) {
          Column() {
            Stack({
              alignContent: Alignment.Bottom
            }) {
              Text('Success')
                .fontSize(100)
                .fontColor(Color.Green)
                .align(Alignment.Center)
                .margin({ bottom: 260 })
            }
          }
        }
      }
      .onReady((context: NavDestinationContext) => {
        this.pathStack = context.pathStack;
        let detectionResult: DetectionResult = this.pathStack.getParamByIndex(1) as DetectionResult;
        if (detectionResult?.finalResult) {
          let message = detectionResult?.finalResult['message'];
          console.info(`Detection result is ${message}.`);
        } else {
          console.info(`Detection result is succeed.`);
        }
      });
    }
  }
  ```
* 检测失败页面（src/main/ets/pages/StartLivenessDetectionFailed.ets）：

  ```ts
  import { DetectionResult } from './Detection';

  @Builder
  export function StartLivenessDetectionFailedBuilder() {
    StartLivenessDetectionFailed()
  }

  @Component
  export struct StartLivenessDetectionFailed {
    @State pathStack: NavPathStack = new NavPathStack();

    build() {
      NavDestination() {
        Stack({
          alignContent: Alignment.Top
        }) {
          Column() {
            Stack({
              alignContent: Alignment.Bottom
            }) {
              Text('Failed')
                .fontSize(100)
                .fontColor(Color.Red)
                .fontWeight(FontWeight.Bolder)
                .align(Alignment.Center)
                .margin({ bottom: 260 })
            }
          }
        }
      }
      .onReady((context: NavDestinationContext) => {
        this.pathStack = context.pathStack;
        let detectionResult: DetectionResult = this.pathStack.getParamByIndex(1) as DetectionResult;
        if (detectionResult?.finalResult) {
          let message = detectionResult?.finalResult['message'];
          console.info(`Detection result is ${message}.`);
        } else {
          console.info(`Detection result is failed.`);
        }
      });
    }
  }
  ```

## 常见FAQ

Q：调用startLivenessDetection接口，没有像期望结果那样跳转到指定页面，而是跳转到默认页面，原因是什么？

A：使用callback回调获取检测结果的startLivenessDetection接口，当前只适用于RouteRedirectionMode.BACK\_MODE跳转模式。检查入参InteractiveLivenessConfig对象的routeMode属性值是否为RouteRedirectionMode.BACK\_MODE。

## 总结

通过自行判断检测结果跳转指定页面，可以突破路由方式的限制，更灵活的实现业务需求。
