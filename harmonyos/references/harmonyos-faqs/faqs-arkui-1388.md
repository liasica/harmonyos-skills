---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1388
title: 列表展开动效异常，与正在下移的组件重叠
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 列表展开动效异常，与正在下移的组件重叠
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2128bc8fc112775d0e6685b1bf94b475d2e1c14d888d6adeb78fb24390d25434
---

## 问题现象

列表展开时，与正在下移的组件存在重叠，部分列表内容被下移的组件遮挡。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/lnvdHoZBQ76ZARfcZ1sYgA/zh-cn_image_0000002658841935.png "点击放大")

## 背景知识

* [组件内转场 (transition)](../harmonyos-references/ts-transition-animation-component.md)主要通过transition属性配置转场参数，在组件插入和删除时显示过渡动效，主要用于容器组件中的子组件插入和删除时，提升用户体验。
* [TransitionEffect](../harmonyos-references/ts-transition-animation-component.md#transitioneffect10对象说明)以函数的形式指定转场效果。
* 组件的某些通用属性变化时，可以通过[属性动画 (animation)](../harmonyos-references/ts-animatorproperty.md)实现渐变过渡效果，提升用户体验。

## 问题定位

1. 使用DevEco Testing查看发生异常的页面，发现问题组件为List组件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/Qt8rlx61Q322er3QKgzCGA/zh-cn_image_0000002628762564.png "点击放大")
2. 查看该List组件的相关设置，List组件使用了OPACITY进行透明度形式的转场，其父组件使用animation在高度变化时使用动画，达到组件平移的动画效果。

   ```screen
   @Entry
   @Component
   struct ListRefreshLoad {
     @State showList: boolean[] = [false, false];
     private arr: number[] = [1, 2, 3, 4];

     build() {
       Column({ space: 15 }) {
         Column() {
           Row() {
             Text('列表一')
               .height('100%')
               .fontSize(20)
               .textAlign(TextAlign.Start);
             Image($r('sys.media.ohos_ic_public_arrow_right'))
               .height(25)
               .width(25)
               .objectFit(ImageFit.Contain)
               .rotate({ angle: this.showList[0] ? 90 : 0 });
           }
           .height(30)
           .width('100%')
           .onClick(() => {
             this.showList[0] = !this.showList[0];
           });

           if (this.showList[0]) {
             List({ space: 5 }) {
               ForEach(this.arr, (item: number) => {
                 ListItem() {
                   Text('子列表' + item.toString())
                     .height(40)
                     .width('90%')
                     .fontSize(20)
                     .textAlign(TextAlign.Start);
                 }
                 .width('100%')
                 .padding({ left: 5, right: 5 });
               });
             }
             .backgroundColor('#f1f3f5')
             .borderRadius(16)
             .transition(TransitionEffect.OPACITY.animation({ duration: 1000, curve: Curve.Ease })); // 使用了OPACITY进行透明度形式的转场
           }
           Row() {
             Text('列表二')
               .height('100%')
               .fontSize(20)
               .textAlign(TextAlign.Start);

             Image($r('sys.media.ohos_ic_public_arrow_right'))
               .height(25)
               .width(25)
               .objectFit(ImageFit.Contain)
               .rotate({ angle: this.showList[1] ? 90 : 0 });
           }
           .height(30)
           .width('100%')
           .onClick(() => {
             this.showList[1] = !this.showList[1];
           });
         }
         .width('100%')
         .height(this.showList[0] ? 265 : 90)
         // 组件高度改变时使用动画进行过渡
         .animation({
           duration: 1000,
           curve: Curve.EaseOut,
           playMode: PlayMode.Normal
         })
         .justifyContent(FlexAlign.SpaceBetween);
       }
       .padding({ left: 10, right: 10 })
       .width('100%')
       .height('100%');
     }
   }
   ```

## 分析结论

List组件使用了OPACITY进行透明度形式的转场，与下方组件平移式的转场效果冲突，造成与正在下移的组件重叠。

## 修改建议

将List组件的转场效果改为逐渐铺展开，与下方组件平移式的转场效果匹配。

```ts
@Entry
@Component
struct ListRefreshLoad {
  @State showList: boolean[] = [false, false];
  private arr: number[] = [1, 2, 3, 4];
  @State listHeight: number = 1;

  build() {
    Column({ space: 15 }) {
      Column() {
        Row() {
          Text('列表一')
            .height('100%')
            .fontSize(20)
            .textAlign(TextAlign.Start);
          Image($r('sys.media.ohos_ic_public_arrow_right'))
            .height(25)
            .width(25)
            .objectFit(ImageFit.Contain)
            .rotate({ angle: this.showList[0] ? 90 : 0 });
        }
        .height(30)
        .width('100%')
        .onClick(() => {
          if (!this.showList[0]) {
            this.showList[0] = true;
          } else {
            this.getUIContext().animateTo(
              {
                duration: 1000, // 动画时长 1 秒
                curve: Curve.Linear,
                onFinish: () => {
                  this.showList[0] = false;
                }
              },
              () => {
                this.listHeight = 1;
              });
          }
        });

        if (this.showList[0]) {
          Column() {
            List({ space: 5 }) {
              ForEach(this.arr, (item: number) => {
                ListItem() {
                  Text('子列表' + item.toString())
                    .height(40)
                    .width('90%')
                    .fontSize(20)
                    .textAlign(TextAlign.Start);
                }
                .width('100%')
                .padding({ left: 5, right: 5 });
              });
            };
          }
          .height(this.listHeight)
          .backgroundColor('#f1f3f5')
          .borderRadius(16)
          .onAppear(() => {
            // 对列表展开使用与父组件一样的动画
            this.getUIContext().animateTo(
              {
                duration: 1000, // 动画时长 1 秒
                curve: Curve.Linear
              },
              () => {
                this.listHeight = 175; // 改变列表组件的高度
              });
          });

        }
        Row() {
          Text('列表二')
            .height('100%')
            .fontSize(20)
            .textAlign(TextAlign.Start);

          Image($r('sys.media.ohos_ic_public_arrow_right'))
            .height(25)
            .width(25)
            .objectFit(ImageFit.Contain)
            .rotate({ angle: this.showList[1] ? 90 : 0 });
        }
        .height(30)
        .width('100%')
        .onClick(() => {
          this.showList[1] = !this.showList[1];
        });
      }
      .width('100%')
      .height(this.showList[0] ? 265 : 90)
      .animation({
        duration: 1000,
        curve: Curve.EaseOut,
        playMode: PlayMode.Normal
      })
      .justifyContent(FlexAlign.Start);
    }
    .padding({ left: 10, right: 10 })
    .width('100%')
    .height('100%');
  }
}
```
