---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-vision-7
title: 活体检测返回后没有沉浸式如何解决
breadcrumb: FAQ > AI功能开发 > 机器学习 > 场景化视觉（Vision） > 活体检测返回后没有沉浸式如何解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:59+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c2ed4ed6760a7d1a13031dea4929b5f79a841ac03329cae34fde58b5a0012f9c
---

## 问题现象

在调用Vision API interactiveLiveness进入活体检测页面，点击活体检测页面返回或者侧滑手机返回原来的页面，原来页面的沉浸式效果会消失，运行的demo如下：

```ts
import { abilityAccessCtrl, Context } from '@kit.AbilityKit';
import { interactiveLiveness } from '@kit.VisionKit';
import { BusinessError } from '@kit.BasicServicesKit';

const TAG = 'FaceManager';

export class FaceManager {
  // 校验CAMERA权限
  public static privateStartDetection(context: Context) {
    let res = abilityAccessCtrl.createAtManager().verifyAccessTokenSync(100, 'ohos.permission.CAMERA');
    if (res === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED) {
      FaceManager.privateRouterLibrary();
    } else {
      abilityAccessCtrl.createAtManager()
        .requestPermissionsFromUser(context, ['ohos.permission.CAMERA'], (err, res) => {
          console.info(TAG, `res==${JSON.stringify(res)}`);
          for (let i = 0; i < res.permissions.length; i++) {
            if (res.permissions[i] === 'ohos.permission.CAMERA' && res.authResults[i] === 0) {
              FaceManager.privateRouterLibrary();
            }
          }
        });
    }
  }

  // 路由跳转到人脸活体验证控件
  public static privateRouterLibrary() {
    console.info(TAG, `camera open time start1==${new Date().getTime()}`);
    let routerOptions: interactiveLiveness.InteractiveLivenessConfig = {
      'isSilentMode': 'INTERACTIVE_MODE' as interactiveLiveness.DetectionMode,
      'actionsNum': 1
    };
    interactiveLiveness.startLivenessDetection(routerOptions).then((DetectState: boolean) => {
      console.info(TAG, `DetectState==${DetectState}`);
    }).catch((e: BusinessError) => {
      console.info(TAG, `DetectState1111==${JSON.stringify(e)}`);
    });
  }
}
@Entry
@Component
struct Index {
  build() {
    Column() {
      Text("打开人脸")
        .id('HelloWorld1')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        }).onClick(()=>{
          const context = this.getUIContext()?.getHostContext();
          if (context) {
            FaceManager.privateStartDetection(context);
          } else {
            console.error('FaceManager', 'Context is undefined');
          }
      })
    }
    .height('100%')
    .width('100%').justifyContent(FlexAlign.Center)
    .backgroundColor(Color.Orange)
  }
}
```

## 背景知识

通过配置组件的expandSafeArea属性来扩展安全区域，可以实现页面的沉浸式效果。同时需注意一些限制避免沉浸式效果不生效：

* 设置expandSafeArea属性进行组件绘制扩展时，组件不能设置固定宽高尺寸。可尝试用百分比或padding改变组件宽高。
* 设置expandSafeArea属性的组件需与安全区域边界重合。
* 当设置expandSafeArea属性的组件的父组件是滚动类容器，需设置父组件的clip属性，不裁剪内部组件。可参考[窗口沉浸式](../best-practices/bpta-multi-device-window-immersive.md)。

## 解决方案

通过设置expandSafeArea属性向顶部和底部扩展安全区域以此达到沉浸式效果，具体参考以下代码：

```ts
import { abilityAccessCtrl, Context } from '@kit.AbilityKit';
import { interactiveLiveness } from '@kit.VisionKit';
import { BusinessError } from '@kit.BasicServicesKit';

const TAG = 'FaceManager';

export class FaceManager {
  // 校验CAMERA权限
  public static privateStartDetection(context: Context) {
    let res = abilityAccessCtrl.createAtManager().verifyAccessTokenSync(100, 'ohos.permission.CAMERA');
    if (res === abilityAccessCtrl.GrantStatus.PERMISSION_GRANTED) {
      FaceManager.privateRouterLibrary();
    } else {
      abilityAccessCtrl.createAtManager()
        .requestPermissionsFromUser(context, ['ohos.permission.CAMERA'], (err, res) => {
          console.info(TAG, `res====${JSON.stringify(res)}`);
          for (let i = 0; i < res.permissions.length; i++) {
            if (res.permissions[i] === 'ohos.permission.CAMERA' && res.authResults[i] === 0) {
              FaceManager.privateRouterLibrary();
            }
          }
        });
    }
  }

  // 路由跳转到人脸活体验证控件
  public static privateRouterLibrary() {
    console.info(TAG, `camera open time start1===${new Date().getTime()}`);
    let routerOptions: interactiveLiveness.InteractiveLivenessConfig = {
      'isSilentMode': 'INTERACTIVE_MODE' as interactiveLiveness.DetectionMode,
      'actionsNum': 1
    };
    interactiveLiveness.startLivenessDetection(routerOptions).then((DetectState: boolean) => {
      console.info(TAG, `DetectState===${DetectState}`);
    }).catch((e: BusinessError) => {
      console.info(TAG, `DetectState1111===${JSON.stringify(e)}`);
    });
  }
}

@Entry
@Component
struct FaceDetectionPage {
  build() {
    Column() {
      Text('打开人脸')
        .id('HelloWorld1')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          const context = this.getUIContext()?.getHostContext();
          if (context) {
            FaceManager.privateStartDetection(context);
          } else {
            console.error(TAG, 'Context is undefined');
          }
        });
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.Center)
    .backgroundColor(Color.White)
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
  }
}
```

## 常见FAQ

Q：人脸活体检测是否支持前后置摄像头？

A：目前人脸活体检测仅支持前置摄像头，不支持后置摄像头。

Q：人脸活体检测是否金融级安全，是否支持炫彩，防注入攻击？

A：目前动作活体检测能力已经是金融支付级别的安全等级了，支持防注入攻击暂不支持炫彩。

Q：如何实现人脸活体检测功能？

A：可直接参考官网[人脸活体检测API](../harmonyos-references/vision-interactive-liveness.md)文档。

Q：静默活体人脸检测与动态活体人脸检测的区别是什么？

A：静默活体的安全等级低，检测的是图片，是无法区分图片和真人的。动作活体检测支持实时捕捉人脸，需要用户配合做指定动作就可以判断是真实活体，安全性比较高。

Q：如何在应用中接入生物特征能力？

A：应用接入生物特征能力分为两种。一种是纯本地生物特征接入，使用User Authentication Kit即可。另一种是在线身份认证协议的接入，这种方式本身系统已经完成FIDO和IIFAA协议和本地身份认证的对接，因此只需要调用Online Authentication Kit，具体可参考[用户认证服务](../harmonyos-guides/user-authentication-kit.md)和[人脸活体检测](../harmonyos-references/vision-interactive-liveness.md)。

Q：活体检测服务是否有进行本人认证？

A：[人脸活体检测](../harmonyos-guides/vision-interactiveliveness.md)支持实时捕捉人脸，需要用户配合做指定动作就可以判断是真实活体，还是非活体攻击（比如：打印图片、人脸翻拍视频以及人脸面具等），并没有进行本人认证。当前活体检测成功后会返回最具活体特征的图片，如果要进行本人认证，需开发者自行使用该图片进行后续处理。

Q：活体检测是否可以横屏使用？

A：目前不支持。

Q：人脸活体检测时，输入参数设为空值或自定义测试值，报错17630001。

A：17630001报错是参数格式不对，人脸活体检测SDK不支持自行伪造假输入参数获取返回值，只能使用真实的数据接口，才能去初始化SDK拉起摄像头，通过封装好的回调去获取相应的数据。
