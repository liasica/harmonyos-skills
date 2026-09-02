---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-870
title: 页面的弹窗阴影遮挡页面内容
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 页面的弹窗阴影遮挡页面内容
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:12508b4138ec106e8de1f70c05d5c1d2d426cf9c034aaa30c2e0794d70748c33
---

## 问题现象

页面使用弹窗进行提示时，弹窗阴影过重，遮挡页面内容。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/wzTnaUgsQrSZdRjJUcpF1A/zh-cn_image_0000002628558814.png "点击放大")

## 背景知识

* 通过[Popup控制](../harmonyos-references/ts-universal-attributes-popup.md)，可以为组件绑定Popup气泡，并设置气泡内容，交互逻辑和显示状态。
* 通过shadow参数可设置气泡阴影，支持[ShadowOptions](../harmonyos-references/ts-universal-attributes-image-effect.md#shadowoptions对象说明)和[ShadowStyle](../harmonyos-references/ts-universal-attributes-image-effect.md#shadowstyle10枚举说明)类型。

## 问题定位

1. 使用DevEco Testing查看问题页面，该弹窗组件为Popup组件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/7GtPgOKrQGi5GyKOjc49dQ/zh-cn_image_0000002658918133.png "点击放大")
2. 查看该Popup组件的设置，shadow参数设置不合理，阴影半径radius过大，且阴影颜色color为纯黑色。

   ```screen
   Image($r('app.media.startIcon'))
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
         radius: 200, // 半径设置过大
         color: Color.Black, // 颜色为黑色
         offsetX: 0,
         offsetY: 0
       }, // 设置气泡的阴影
       placement: Placement.Top,
     });
   ```

## 分析结论

气泡弹窗组件的shadow参数设置不合理，阴影半径radius过大，且阴影颜色color为纯黑色，导致阴影遮挡页面内容。

## 修改建议

合理设置气泡弹窗组件的shadow参数，阴影半径radius调小，阴影颜色color设置为浅灰色。

```screen
@Entry
@Component
struct PopupDemo {
  private arr: number[] = [0, 1, 2, 3, 4];

  build() {
    Column() {
      Text('他望车外看了看，说，“我买几个橘子去。你就在此地，不要走动。”我看那边月台的栅栏处有几个卖东西的等着顾客。走到那边月台，须穿过铁道，须跳下去又爬上去。父亲是一个胖子，走过去自然要费事些。我本来要去的，他不肯，只好让他去。我看见他戴着黑布小帽，穿着黑布大马褂，深青布棉袍，蹒跚地走到铁道边，慢慢探身下去，尚不大难。可是他穿过铁道，要爬上那边月台，就不容易了。')
        .width('90%')
        .fontSize(20);

      List({ space: 5 }) {
        ForEach(this.arr, (item: number) => {
          ListItem() {
            Row() {
              Image($r('app.media.startIcon')) // $r('app.media.startIcon')需要替换为开发者需要的图片资源文件
                .height('80%')
                .width('30%')
                .objectFit(ImageFit.Contain)
                .margin({ left: 10 })
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
                    radius: 50, // 半径调小
                    color: '#dedede', // 颜色改为灰色
                    offsetX: 0,
                    offsetY: 0
                  }, // 设置气泡的阴影
                  placement: Placement.Top,
                });

              Text('123456')
                .fontSize(20)
                .width('70%')
                .height('100%')
                .textAlign(TextAlign.Center);
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
      .margin({ top: 65 });
    }
    .padding({ top: 5 })
    .width('100%')
    .height('100%');
  }
}
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/UKUeRNpyQQGAWOMMH-DLyw/zh-cn_image_0000002628398910.png "点击放大")
