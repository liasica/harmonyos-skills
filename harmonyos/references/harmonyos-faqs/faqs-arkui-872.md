---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-872
title: 弹窗箭头位置错误，指示不明确
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 弹窗箭头位置错误，指示不明确
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2d2f691fa6983fa513d97f3f7557f0afd45fbe4e93c0c8f57cc3dfe7ce94cae5
---

## 问题现象

弹窗提示“点击图片可放大”，但是箭头并未指向图片。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/UxetenOvQ0CBx0RBrEPjQQ/zh-cn_image_0000002658798189.png "点击放大")

## 背景知识

通过[Popup控制](../harmonyos-references/ts-universal-attributes-popup.md)，可以为组件绑定Popup气泡，并设置气泡内容，交互逻辑和显示状态。

## 问题定位

1. 使用DevEco Testing查看问题组件，该弹窗组件为Popup气泡弹窗组件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/8Suw4NeQRPuVwZ-HVt_f1Q/zh-cn_image_0000002628558818.png "点击放大")
2. 查看该Popup气泡弹窗组件的设置，该组件并没有绑定在图片组件上，而是绑定在列表组件List上。

   ```screen
   @Entry
   @Component
   struct ScrollExample {
     private arr: number[] = [0, 1, 2, 3, 4];
     @State customPopup: boolean = false;

     build() {
       Column() {
         Text('壬戌之秋，七月既望，苏子与客泛舟游于赤壁之下。清风徐来，水波不兴。举酒属客，诵明月之诗，歌窈窕之章。少焉，月出于东山之上，徘徊于斗牛之间。白露横江，水光接天。纵一苇之所如，凌万顷之茫然。浩浩乎如冯虚御风，而不知其所止；飘飘乎如遗世独立，羽化而登仙。\n')
           .width('90%')
           .fontSize(20);

         List({ space: 5 })
           .onAppear(() => {
             this.customPopup = true;
           })
           // 气泡弹窗绑定在列表组件上
           .bindPopup(this.customPopup, {
             // PopupOptions类型气泡的内容
             message: '点击图片可放大'
           });
       }
       .width('100%')
       .height('100%');
     }
   }
   ```

## 分析结论

Popup气泡弹窗组件未绑定到图片组件上，而是绑定到列表组件上，导致弹窗箭头位置错误，指示不明确。

## 修改建议

Popup气泡弹窗组件绑定到图片组件上。

```screen
@Entry
@Component
struct ScrollExamplePop {
  private arr: number[] = [0, 1, 2, 3, 4];

  build() {
    Column() {
      Text('壬戌之秋，七月既望，苏子与客泛舟游于赤壁之下。清风徐来，水波不兴。举酒属客，诵明月之诗，歌窈窕之章。少焉，月出于东山之上，徘徊于斗牛之间。白露横江，水光接天。纵一苇之所如，凌万顷之茫然。浩浩乎如冯虚御风，而不知其所止；飘飘乎如遗世独立，羽化而登仙。\n')
        .width('90%')
        .margin({ top: 10 })
        .fontSize(20);

      List({ space: 5 }) {
        ForEach(this.arr, (item: number) => {
          ListItem() {
            Row() {
              Image($r('app.media.startIcon')) // $r('app.media.startIcon')需要替换为开发者需要的图片资源文件
                .height('80%')
                .width('20%')
                .objectFit(ImageFit.Contain)
                .margin({ left: 10 })
                // 绑定第一张图片
                .bindPopup(item === 0 ? true : false, {
                  // PopupOptions类型气泡的内容
                  message: '点击图片可放大',
                  messageOptions: {
                    // 气泡的文本样式
                    font: {
                      size: '14vp',
                      weight: FontWeight.Bolder
                    }
                  },
                  targetSpace: '15vp',
                  arrowHeight: 10,
                  radius: 8,
                  shadow: {
                    radius: 50,
                    color: '#dedede',
                    offsetX: 0,
                    offsetY: 0
                  }, // 设置气泡的阴影
                  placement: Placement.Top,
                });

              Text('123456')
                .fontSize(20)
                .width('70%')
                .height('100%')
                .margin({ left: 10 })
                .textAlign(TextAlign.Start);
            }
            .width('100%')
            .height('100%');
          }
          .width('90%')
          .height(80)
          .backgroundColor('#f1f3f5')
          .borderRadius(20);
        });
      }
      .alignListItem(ListItemAlign.Center)
      .margin({ top: 20 });
    }
    .width('100%')
    .height('100%');
  }
}
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/o1nXHoeESjWW2cO4BIZJ4g/zh-cn_image_0000002658918135.png "点击放大")
