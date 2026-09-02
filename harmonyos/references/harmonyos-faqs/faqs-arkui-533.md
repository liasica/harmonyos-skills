---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-533
title: 页面中的图片资源无法正常显示
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 页面中的图片资源无法正常显示
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:12+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:083d5587d2c66ce4bf93a29a105e99dff8c2903631b79d2cc1b4345ad4e8f47a
---

## 问题现象

页面图片显示空白。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/mAtz0ampQUe4klYygXVAlA/zh-cn_image_0000002628391176.png "点击放大")

## 背景知识

* [Image](../harmonyos-references/ts-basic-components-image.md)为图片组件，常用于在应用中显示图片。
* [alt](../harmonyos-references/ts-basic-components-image.md#alt)属性可设置图片加载过程中显示的占位图。

## 问题定位

1. 使用DevEco Testing查看问题组件，问题所在位置缺少Image组件，而正常显示图片组件的相同位置使用了Image组件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/26fxKevzTKa_R9r7_m0GfA/zh-cn_image_0000002658790427.png "点击放大")
2. 排查Image组件的设置，发现添加了判断图片资源是否存在的逻辑。

   ```screen
   @Entry
   @Component
   struct ImgEmpty {
     imgSrcs: ResourceStr[] = ['', $r('app.media.myposter2')];

     build() {
       Stack() {
         List() {
           ForEach(this.imgSrcs, (img: ResourceStr, index: number) => {
             ListItem() {
               Row() {
                 Text('图片' + (index + 1))
                   .fontSize(20)
                   .height('100%')
                   .width(100)
                   .textAlign(TextAlign.Center)
                   .borderRadius(10);

                 // 图片资源为空时不显示图片组件
                 if (img !== '') {
                   Image(img)
                     .width(150)
                     .objectFit(ImageFit.Contain);
                 }
               }
               .width('100%')
               .height(120)
               .justifyContent(FlexAlign.Start)
               .borderRadius(10)
               .backgroundColor('#f1f3f5');
             }
             .margin({ top: 5, bottom: 5 });
           }, (item: string) => item);
         }
         .nestedScroll({
           scrollForward: NestedScrollMode.PARENT_FIRST,
           scrollBackward: NestedScrollMode.SELF_FIRST
         })
         .scrollBar(BarState.Off)
         .width('80%');
       }
       .width('100%')
       .height('100%');
     }
   }
   ```

## 分析结论

该图片资源不存在，导致无法显示图片。

## 修改建议

无图片资源时通过alt属性使用占位图片替代。

```screen
@Entry
@Component
struct ImgEmpty {
  imgSrcs: ResourceStr[] = ['', $r('app.media.startIcon')]; // $r('app.media.startIcon')需要替换为开发者需要的图片资源文件

  build() {
    Stack() {
      List() {
        ForEach(this.imgSrcs, (img: ResourceStr, index: number) => {
          ListItem() {
            Row() {
              Text('图片' + (index + 1))
                .fontSize(20)
                .height('100%')
                .width(100)
                .textAlign(TextAlign.Center)
                .borderRadius(10);

              Image(img)
                .width(100)
                // $r('app.media.empty')需要替换为开发者需要的图片资源文件
                .alt($r('app.media.empty')) // 图片资源为空时显示占位图片
                .objectFit(ImageFit.Contain);
            }
            .width('100%')
            .height(120)
            .justifyContent(FlexAlign.Start)
            .borderRadius(10)
            .backgroundColor('#f1f3f5');
          }
          .margin({ top: 5, bottom: 5 });
        }, (item: string) => item);
      }
      .nestedScroll({
        scrollForward: NestedScrollMode.PARENT_FIRST,
        scrollBackward: NestedScrollMode.SELF_FIRST
      })
      .scrollBar(BarState.Off)
      .width('80%');
    }
    .width('100%')
    .height('100%');
  }
}
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/BXGR1xwQRxSz8OvmHoMelg/zh-cn_image_0000002628551066.png "点击放大")
