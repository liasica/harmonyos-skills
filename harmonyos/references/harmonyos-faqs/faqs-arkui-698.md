---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-698
title: 图片旋转时闪烁
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 图片旋转时闪烁
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c90d44c1adb414fab65aa60558b9d3cf359b45b98d0730741e33207298faee37
---

## 问题现象

用户旋转设备时，当前页面指针转动闪烁，影响用户体验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/4wIWXnsuTqGpiNizwiSPnA/zh-cn_image_0000002628394984.png "点击放大")

## 背景知识

* [Image](../harmonyos-references/ts-basic-components-image.md)为图片组件，常用于在应用中显示图片。
* [rotate](../harmonyos-references/ts-universal-attributes-transformation.md#rotate)：设置组件旋转。
* [animation](../harmonyos-references/ts-animatorproperty.md)：组件的某些通用属性变化时，可以通过属性动画实现渐变过渡效果，提升用户体验。

## 问题定位

1. 使用DevEco Testing查看问题组件，该组件为Image组件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/_j2wFIg9Sg2FTZOy2on1Sw/zh-cn_image_0000002658794249.png "点击放大")
2. 查看该Image组件的设置，该组件未使用animation属性对图片旋转设置动画效果，导致旋转设备时图片闪烁。

   ```ts
   import sensor from '@ohos.sensor';
   import base from '@ohos.base';
   import { window } from '@kit.ArkUI';
   import { common } from '@kit.AbilityKit';

   export function onDegree(callback: base.Callback<number>): void {
     // 监听屏幕旋转角度变化
     sensor.on(sensor.SensorId.GRAVITY, (data: sensor.GravityResponse) => {
       let degree: number = 0;
       degree = CalDegree(data.x, data.y, data.z);
       console.info('degree is ', degree);
       callback(degree);
     });
   }

   function CalDegree(x: number, y: number, z: number): number {
     let degree: number = 0;
     // 3为*有效_增量_角度_阈值_系数*
     if ((x * x + y * y) * 3 < z * z) {
       return degree;
     }
     degree = 90 - (Number)(Math.round(Math.atan2(y, -x) / Math.PI * 180));
     return degree >= 0 ? degree % 360 : degree % 360 + 360;
   }

   @Component
   @Entry
   struct Index {
     @State @Watch('changeMyRotate') degree: number = 0;
     @State myRotate: number = 0;

     changeMyRotate() {
       if (this.degree - this.myRotate > 180) {
         this.myRotate = this.degree - 360;
       } else {
         this.myRotate = this.degree;
       }
     }

     aboutToAppear() {
       let callback = async (degree: number) => {
         this.degree = degree;
       };
       onDegree(callback);
       let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
       window.getLastWindow(context).then((lastWindow) => {
         lastWindow.setWindowLayoutFullScreen(true);
         let systemBarProperties: window.SystemBarProperties = {
           statusBarColor: '#00000000',
           statusBarContentColor: '#ffffff'
         };
         lastWindow.setWindowSystemBarProperties(systemBarProperties);
       });
     }

     build() {
       Stack() {
         // 背景刻度
         Image($r('app.media.bg')) // $r('app.media.bg')需要替换为开发者需要的图片资源文件
           .width(400)
           .height(400)
           .objectFit(ImageFit.Contain)
         // 指针
         Image($r('app.media.compass')) // $r('app.media.compass')需要替换为开发者需要的图片资源文件
           .rotate({ angle: -this.myRotate }) // 图片旋转
           .width(250)
           .height(250)
           .objectFit(ImageFit.Contain)
           // 图片旋转时未设置动画效果
       }
       .height('100%')
       .width('100%')
       .backgroundColor(Color.Black)
     }
   }
   ```

## 分析结论

转动设备进行图片旋转时未设置旋转动画，导致跳帧，造成图片旋转时闪烁。

## 修改建议

转动设备进行图片旋转时通过animation设置旋转动画。

```ts
import sensor from '@ohos.sensor';
import base from '@ohos.base';
import { window } from '@kit.ArkUI';
import { common } from '@kit.AbilityKit';

export function onDegree(callback: base.Callback<number>): void {
  // 监听屏幕旋转角度变化
  sensor.on(sensor.SensorId.GRAVITY, (data: sensor.GravityResponse) => {
    let degree: number = 0;
    degree = CalDegree(data.x, data.y, data.z);
    console.info('degree is ', degree);
    callback(degree);
  });
}

function CalDegree(x: number, y: number, z: number): number {
  let degree: number = 0;
  // 3 为 有效_增量_角度_阈值_系数
  if ((x * x + y * y) * 3 < z * z) {
    return degree;
  }
  degree = 90 - (Number)(Math.round(Math.atan2(y, -x) / Math.PI * 180));
  return degree >= 0 ? degree % 360 : degree % 360 + 360;
}

@Component
@Entry
struct Index {
  @State @Watch('changeMyRotate') degree: number = 0;
  @State myRotate: number = 0;

  changeMyRotate() {
    if (this.degree - this.myRotate > 180) {
      this.myRotate = this.degree - 360;
    } else {
      this.myRotate = this.degree;
    }
  }

  aboutToAppear() {
    let callback = async (degree: number) => {
      this.degree = degree;
    };
    onDegree(callback);
    let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    window.getLastWindow(context).then((lastWindow) => {
      lastWindow.setWindowLayoutFullScreen(true);
      let systemBarProperties: window.SystemBarProperties = {
        statusBarColor: '#00000000',
        statusBarContentColor: '#ffffff'
      };
      lastWindow.setWindowSystemBarProperties(systemBarProperties);
    });
  }

  build() {
    Stack() {
      // 背景刻度
      Image($r('app.media.bg')) // $r('app.media.bg')需要替换为开发者需要的图片资源文件
        .width(400)
        .height(400)
        .objectFit(ImageFit.Contain);
      // 指针
      Image($r('app.media.compass')) // $r('app.media.compass')需要替换为开发者需要的图片资源文件
        .rotate({ angle: -this.myRotate }) // 图片旋转
        .width(250)
        .height(250)
        .objectFit(ImageFit.Contain)
        // 对图片旋转添加动画
        .animation({
          duration: 500,
          curve: Curve.EaseOut,
          playMode: PlayMode.Normal
        });
    }
    .height('100%')
    .width('100%')
    .backgroundColor(Color.Black);
  }
}
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/3mjHp3dKRO2E4nBFWisgXA/zh-cn_image_0000002628554886.png "点击放大")
