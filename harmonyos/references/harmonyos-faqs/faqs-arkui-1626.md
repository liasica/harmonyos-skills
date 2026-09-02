---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1626
title: 移动地图时连续弹出加载中的提示，造成闪屏
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 移动地图时连续弹出加载中的提示，造成闪屏
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:12+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e861e7e1de97264177613c0d509c9e9a7ae5a192878ee5ec92a7aecdc31ad8c3
---

## 问题现象

移动地图过程中一直显示加载中的弹窗。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/JQ_Zy2gaRmGsRhUfslLcIw/zh-cn_image_0000002628617574.png "点击放大")

## 背景知识

* 可通过[PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)实现页面滑动功能：滑动手势事件，当滑动的最小距离达到设定的最小值时触发滑动手势事件。
* 可通过以下方法实现页面滑动时的相关功能：

  | 方法 | 说明 |
  | --- | --- |
  | [onActionStart](../harmonyos-references/ts-basic-gestures-pangesture.md#onactionstart) | Pan手势识别成功回调。 |
  | [onActionUpdate](../harmonyos-references/ts-basic-gestures-pangesture.md#onactionupdate) | Pan手势移动过程中回调。 |
  | [onActionEnd](../harmonyos-references/ts-basic-gestures-pangesture.md#onactionend) | Pan手势识别成功，手指抬起后触发回调。 |

## 问题定位

1. 查看Hilog日志，全局搜索gesture，排查移动地图时相关日志，移动地图时一直显示更新日志。

   ```screen
   PanGesture update data={"repeat":false,"offsetX":17.983796296296298,"offsetY":-39.06653284143518,"scale":1,"angle":0,"speed":0,"timestamp":10211014178649,"pinchCenterX":0,"pinchCenterY":0,"source":2,"pressure":1,"tiltX":0,"tiltY":0,"rollAngle":0,"sourceTool":1,"velocityX":333.11482114696054,"velocityY":-630.1921235158158,"velocity":712.816664093331,"fingerList":[{"id":0,"hand":0,"globalX":207.31712962962962,"globalY":173.89643012152777,"localX":207.31712962962962,"localY":173.89643012152777,"displayX":207.31712962962962,"displayY":297.8223560474537}],"deviceId":0,"target":{"area":{"position":{"x":0,"y":0},"globalPosition":{"x":0,"y":0},"width":373,"height":719}},"axisVertical":0,"axisHorizontal":0,"targetDisplayId":0}
   PanGesture update data={"repeat":false,"offsetX":20.958387586805557,"offsetY":-45.27730758101852,"scale":1,"angle":0,"speed":0,"timestamp":10211022487696,"pinchCenterX":0,"pinchCenterY":0,"source":2,"pressure":1,"tiltX":0,"tiltY":0,"rollAngle":0,"sourceTool":1,"velocityX":378.85487822089453,"velocityY":-791.881945811817,"velocity":877.842830382796,"fingerList":[{"id":0,"hand":0,"globalX":210.29172092013889,"globalY":167.68565538194446,"localX":210.29172092013889,"localY":167.68565538194446,"displayX":210.29172092013889,"displayY":291.6115813078704}],"deviceId":0,"target":{"area":{"position":{"x":0,"y":0},"globalPosition":{"x":0,"y":0},"width":373,"height":719}},"axisVertical":0,"axisHorizontal":0,"targetDisplayId":0}
   PanGesture update data={"repeat":false,"offsetX":23.99197048611111,"offsetY":-51.53947844328704,"scale":1,"angle":0,"speed":0,"timestamp":10211030796608,"pinchCenterX":0,"pinchCenterY":0,"source":2,"pressure":1,"tiltX":0,"tiltY":0,"rollAngle":0,"sourceTool":1,"velocityX":389.47077439063247,"velocityY":-817.044698974646,"velocity":905.1240380340195,"fingerList":[{"id":0,"hand":0,"globalX":213.32530381944446,"globalY":161.42348451967592,"localX":213.32530381944446,"localY":161.42348451967592,"displayX":213.32530381944446,"displayY":285.34941044560185}],"deviceId":0,"target":{"area":{"position":{"x":0,"y":0},"globalPosition":{"x":0,"y":0},"width":373,"height":719}},"axisVertical":0,"axisHorizontal":0,"targetDisplayId":0}
   ```
2. 根据日志内容排查相关功能，应用使用PanGesture实现页面滑动时，通过onActionUpdate方法持续显示加载中的提示。

   ```screen
   @Entry
   @Component
   struct DragDemo {
     showDialog() {
       if (this.showLoading) {
         this.dialogController.open(); // 显示加载中弹窗
       } else {
         this.dialogController.close(); // 关闭加载中弹窗
       }
     }

     build() {
       Column() {
         Column() {
           Text('地图组件')
         }
         .gesture(
           PanGesture()
             .onActionUpdate((event: GestureEvent) => {
               if (event) {
                 this.showLoading = true; // 移动地图时显示加载中
               }
             })
             .onActionEnd(() => {
               this.showLoading = false; // 停止移动后不显示
             })
         );
       }
     }
   }
   ```

## 分析结论

由于onActionUpdate在手势移动过程中回调，应用在onActionUpdate中设置控制弹窗显隐的变量为true，导致在地图移动过程中一直显示弹窗。

## 修改建议

使用onActionEnd在页面滑动结束后再显示加载中的提示。

```screen
@CustomDialog
@Component
struct LoadingDialogExample {
  controller?: CustomDialogController;

  build() {
    Row() {
      LoadingProgress()
        .width('40%')
        .height('100%')
        .margin({ left: 10 });
      Text('加载中')
        .fontSize(20)
        .width('40%')
        .height('100%')
        .textAlign(TextAlign.Start)
        .margin({ left: 2 });
    }
    .width('100%')
    .height('100%');
  }
}

@Entry
@Component
struct DragDemo {
  @State offsetX: number = 0;
  @State offsetY: number = 0;
  positionX: number = 0;
  positionY: number = 0;
  private panOption: PanGestureOptions = new PanGestureOptions({ direction: PanDirection.All });
  @State @Watch('showDialog') showLoading: boolean = false;
  dialogController: CustomDialogController = new CustomDialogController({
    builder: LoadingDialogExample(),
    width: 250,
    height: 60,
    cornerRadius: 10
  });

  showDialog() {
    if (this.showLoading) {
      this.dialogController.open(); // 显示加载中弹窗
    } else {
      this.dialogController.close(); // 关闭加载中弹窗
    }
  }

  build() {
    Column() {
      Column() {
        Text('地图组件')
          .fontSize(20)
          .height('100%')
          .width('100%')
          .textAlign(TextAlign.Center);
      }
      .width(400)
      .height(500)
      .backgroundColor('#f1f3f5')
      .borderRadius(10)
      .translate({ x: this.offsetX, y: this.offsetY })
      .gesture(
        PanGesture(this.panOption)
          .onActionUpdate((event: GestureEvent) => {
            if (event) {
              this.offsetX = this.positionX + event.offsetX;
              this.offsetY = this.positionY + event.offsetY;
            }
          })
          .onActionEnd(() => {
            // 结束移动时才显示加载弹窗
            this.showLoading = true;
            // 模拟加载过程
            setTimeout(() => {
              this.showLoading = false;
            },1000);
            this.positionX = this.offsetX;
            this.positionY = this.offsetY;
          })
      );
    }
    .padding({ left: 10, right: 10 })
    .width('100%')
    .height('100%');
  }
}
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/Ajc62XvJS7udJSnwRG7JMw/zh-cn_image_0000002628777470.png "点击放大")
