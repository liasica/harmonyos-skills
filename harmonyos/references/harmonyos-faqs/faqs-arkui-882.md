---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-882
title: 点击点赞按钮，动画播放完毕后点赞图标消失
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 点击点赞按钮，动画播放完毕后点赞图标消失
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:16+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:bcd0b66bc72958cf5ed5832b6545bd67a87cca62d7e74051dffa219073d7ad4f
---

## 问题信息

打开页面，正常显示点赞按钮，再点击按钮，播放完点赞动画后，点赞图片消失。

## 背景知识

* [if/else条件渲染](../harmonyos-guides/arkts-rendering-control-ifelse.md)：条件渲染可根据应用状态，使用if、else和else if渲染相应的UI内容。
* [setTimeout定时器](../harmonyos-references/js-apis-timer.md#settimeout)：设置一个定时器，该定时器在定时器到期后执行一个函数。

## 问题定位

1. 使用DevEco Testing的UIViewer工具分别检查点赞按钮正常显示时和消失时的UI结构。确认点赞图标是Image组件，在点赞动画播放完毕后页面上没有Image组件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/i-DesQy6Rm-EhSFCYVmOJg/zh-cn_image_0000002628559542.png "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/uBosGV4GTdmQ105sqmmlvA/zh-cn_image_0000002658918853.png "点击放大")
2. 排查代码中点赞图片的显隐逻辑。点赞图片使用的Image组件通过if/else条件渲染，当变量满足条件时才会正常显示，点赞/取消点赞动画播放完毕后并未修改变量的值，Image组件没有正常渲染。

   ```ts
   @Entry
   @Component
   struct ErrorCode {
     @State isLike: boolean = false; // 点赞状态
     @State clickLikeStatus: boolean | undefined = undefined; // 根据布尔值判断使用取消点赞/点赞动画
     // 点赞图片，请使用尺寸较小的本地图片
     likeIcon: ResourceStr = $r('app.media.ic_public_thumbs_up');
     // 未点赞时的颜色(灰色)
     unlikeColor: string = '#757575';
     // 点赞后的颜色(蓝色)
     likeColor: string = '#4eabe6';

     build() {
       Column() {
         Row() {
           Stack() {
             if (this.clickLikeStatus === undefined) {
               Image(this.likeIcon)
                 .objectFit(ImageFit.Contain) // 缩放填充
                 .aspectRatio(1) // 固定宽高比为1
                 .width(70)
                 .syncLoad(true) // 同步加载，避免闪烁
                 .fillColor(this.isLike ? this.likeColor : this.unlikeColor)
             } else {
               // 自定义组件，用于播放动画
               LikePlayer({ isLikeAnimation: this.clickLikeStatus })
             }
           }
         }
         .onClick(() => {
           if (this.clickLikeStatus === undefined) {
             this.clickLike();
           }
         })
       }
       .justifyContent(FlexAlign.Center)
       .height('100%')
       .width('100%')
     }

     // Image组件的点击事件，可以切换播放动画和显示图片
     clickLike() {
       if (this.isLike) {
         this.clickLikeStatus = false;
         // 播放取消点赞动画
       } else {
         this.clickLikeStatus = true;
         // 播放点赞动画
       }
     }
   }

   // 播放（取消）点赞动画，此处仅为模拟方案，实际按需替换
   @Component
   struct LikePlayer {
     @Prop isLikeAnimation: boolean; // 是否是点赞动画，有点赞动画和取消点赞动画
     @State isLike: boolean = !this.isLikeAnimation; // 当前点赞状态
     @State scaleValue: number = 1; // 缩放比例
     @State showAnimation: boolean = true; // 是否显示动画
     // 未点赞时的颜色(灰色)
     unlikeColor: string = '#757575';
     // 点赞后的颜色(蓝色)
     likeColor: string = '#4eabe6';
     // 点赞图片，请使用尺寸较小的本地图片
     likeIcon: ResourceStr = $r('app.media.ic_public_thumbs_up');

     build() {
       Image(this.likeIcon)
         .syncLoad(true) // 同步加载，避免闪烁
         .objectFit(ImageFit.Contain) // 缩放填充
         .aspectRatio(1) // 固定宽高比为1
         .width(70)
         .fillColor(this.isLike ? this.likeColor : this.unlikeColor)
         .scale({ x: this.scaleValue, y: this.scaleValue }) // 添加缩放效果
         .onComplete(() => {
           // 切换点赞状态
           this.isLike = !this.isLike;
           // 点赞动画-第一阶段：放大
           this.getUIContext().animateTo({
             duration: 300, // 动画持续300毫秒
             curve: Curve.Friction, // 使用摩擦曲线，效果更自然
             delay: 0 // 无延迟立即执行
           }, () => {
             this.scaleValue = 1.5; // 图标放大到1.5倍
           });
           // 点赞动画-第二阶段：恢复原大小
           this.getUIContext().animateTo({
             duration: 100, // 动画持续100毫秒
             curve: Curve.Friction, // 使用摩擦曲线
             delay: 300 // 延迟300毫秒执行，等第一阶段完成
           }, () => {
             this.scaleValue = 1; // 图标恢复到原始大小

           });
           // 模拟动画播放完毕后显示空白
           setTimeout(() => {
             this.showAnimation = false;
           }, 400);
         })
         .visibility(this.showAnimation ? Visibility.Visible : Visibility.Hidden)
     }
   }
   ```

## 分析结论

点击点赞按钮时，未延时修改if/else条件渲染中使用的变量的值，在动画播放完毕后，未渲染Image组件，导致点赞图片消失。

## 修改建议

在Image组件的点击事件中，延时修改if/else条件渲染中所使用的变量的值，保证点赞图片在动画播放完毕后正常渲染。

```ts
@Entry
@Component
struct ClickLikeBtn {
  @State isLike: boolean = false; // 点赞状态
  @State clickLikeStatus: boolean | undefined = undefined; // 根据布尔值判断使用取消点赞/点赞动画
  // 点赞图片，请使用尺寸较小的本地图片
  likeIcon: ResourceStr = $r('app.media.ic_public_thumbs_up');
  // 未点赞时的颜色(灰色)
  unlikeColor: string = '#666666';
  // 点赞后的颜色(蓝色)
  likeColor: string = '#0a59f7';

  build() {
    Column() {
      Row() {
        Stack() {
          if (this.clickLikeStatus == undefined) {
            Image(this.likeIcon)
              .objectFit(ImageFit.Contain) // 缩放填充
              .aspectRatio(1) // 固定宽高比为1
              .width(70)
              .syncLoad(true) // 同步加载，避免闪烁
              .fillColor(this.isLike ? this.likeColor : this.unlikeColor)
              .onAppear(() => {
                console.info('[LikeIcon]', 'appear');
              })
              .onDisAppear(() => {
                console.info('[LikeIcon]', 'disappear');
              });
          } else {
            // 自定义组件，用于播放动画
            AnimationPlayer({ isLikeAnimation: this.clickLikeStatus });
          }
        };
      }
      .onClick(() => {
        if (this.clickLikeStatus === undefined) {
          this.clickLike();
        }
      });
    }
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%');
  }

  // Image组件的点击事件，可以切换播放动画和显示图片
  clickLike() {
    if (this.isLike) {
      this.clickLikeStatus = false;
      // 播放取消点赞动画
    } else {
      this.clickLikeStatus = true;
      // 播放点赞动画
    }
    // 使用计时器，延时修改（在动画播放完毕后修改）变量的值为undefined，渲染图片
    // 第二参数是点赞/取消点赞动画的时长
    setTimeout(() => {
      this.isLike = !this.isLike;
      this.clickLikeStatus = undefined;
    }, 400);
  }
}

// 播放（取消）点赞动画，此处仅为模拟方案，实际按需替换
@Component
struct AnimationPlayer {
  @Prop isLikeAnimation: boolean; // 是否是点赞动画，有点赞动画和取消点赞动画
  @State isLike: boolean = !this.isLikeAnimation; // 当前点赞状态
  @State scaleValue: number = 1; // 缩放比例
  // 未点赞时的颜色(灰色)
  unlikeColor: string = '#666666';
  // 点赞后的颜色(蓝色)
  likeColor: string = '#0a59f7';
  // 点赞图片，请使用尺寸较小的本地图片
  likeIcon: ResourceStr = $r('app.media.ic_public_thumbs_up');

  build() {
    Image(this.likeIcon)
      .syncLoad(true) // 同步加载，避免闪烁
      .objectFit(ImageFit.Contain) // 缩放填充
      .aspectRatio(1) // 固定宽高比为1
      .width(70)
      .fillColor(this.isLike ? this.likeColor : this.unlikeColor)
      .scale({ x: this.scaleValue, y: this.scaleValue }) // 添加缩放效果
      .onComplete(() => {
        // 切换点赞状态
        this.isLike = !this.isLike;
        // 点赞动画-第一阶段：放大
        this.getUIContext().animateTo({
          duration: 300, // 动画持续300毫秒
          curve: Curve.Friction, // 使用摩擦曲线，效果更自然
          delay: 0 // 无延迟立即执行
        }, () => {
          this.scaleValue = 1.5; // 图标放大到1.5倍
        });
        // 点赞动画-第二阶段：恢复原大小
        this.getUIContext().animateTo({
          duration: 100, // 动画持续100毫秒
          curve: Curve.Friction, // 使用摩擦曲线
          delay: 300 // 延迟300毫秒执行，等第一阶段完成
        }, () => {
          this.scaleValue = 1; // 图标恢复到原始大小
        });
      });
  }
}
```
