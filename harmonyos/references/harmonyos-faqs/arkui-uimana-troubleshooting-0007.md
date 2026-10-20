---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-uimana-troubleshooting-0007
title: ArkUI-Image组件图片闪烁问题定位
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 故障排查 > ArkUI-Image组件图片闪烁问题定位
category: harmonyos-faqs
scraped_at: 2026-10-21T07:11:11+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:3a5632a750fd850c178b7a4590be4df810d65f5cff8cee226a6d1910b5c75065
---

## 图片旋转时闪烁

### 问题现象

用户旋转设备时，当前页面指针转动闪烁，影响用户体验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/WlBx00SqRHSNx7RStHzl-A/zh-cn_image_0000002795317937.png "点击放大")

### 定位过程

1. 使用DevEco Testing查看问题组件，该组件为Image组件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/oJrtqzOfRU-MQuf_BZsqzw/zh-cn_image_0000002766079180.png "点击放大")
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

### 分析结论

转动设备进行图片旋转时未设置旋转动画，导致跳帧，造成图片旋转时闪烁。

### 修改建议

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/Hiz8b1O4QrObcJq3xPfOkw/zh-cn_image_0000002766079538.png "点击放大")

## 页面上下滑动时，页面上的图片会闪跳

### 问题现象

图片在上下或左右滑动时，出现图片放大或缩小，又瞬间恢复原本大小的现象，视觉上内容闪烁。

### 定位过程

1. 上下滑动页面时，排查日志发现，每次滚动高度都发生了改变。

   ```ts
      PDF_RENDER --> method=updateTex
      PDF_RENDER --> updateText: width=1271 height=891, srcX=0, setY=0
      PDF_RENDER --> method=updateTex
      PDF_RENDER --> updateText: width=1271,height=305,srcX=0,setY=1492
      PDF_RENDER --> method=updateTex
      PDF_RENDER --> updateText: width=1271,height=1505,srcX=0,setY=0
   ```
2. 使用DevEco Testing查看页面布局，是由多张图片组合而成的界面，结合日志可以发现每次往下滑动时，缩小上面图片的高度，放大下面图片的高度，否则反之。

### 分析结论

每次滑动图片时，高度/宽度会被刷新，导致出现闪烁现象。

### 修改建议

* 方案一：将图片整合为一张长图，使用Scroll使其可上下滚动。
* 方案二：使用Swiper轮播图左右滑动图片，而非上下滑动放大缩小图片。

  ```ts
  @Entry
  @Component
  struct NestedScroll {
    private swiperController: SwiperController = new SwiperController();

    build() {
      Column() {
        // 使用Scroll组件使长图可以滚动
        Scroll() {
          Column() {
            // 加载一张长图，请提供真实的长图
            Image($r("app.media.example"))
          }
        }.width('100%').height('100%').backgroundColor(0xDCDCDC).padding(20)

        Column({ space: 5 }) {
          // 可左右滑动的轮播图，请提供真实的图片
          Swiper(this.swiperController) {
            Image($r("app.media.example"))
            Image($r("app.media.example"))
            Image($r("app.media.example"))
            Image($r("app.media.example"))
          }
          .index(1)
          .autoPlay(true)
          .interval(4000)
          .loop(true)
          .duration(1000)
          .itemSpace(0)

        }.width('100%')
        .height('100%')
        .margin({ top: 5 })
      }
    }
  }
  ```
