---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-520
title: 跑马灯效果实现
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 跑马灯效果实现
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:01+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:07d376993fbdcbeb740d55af456d4d4f931da92980885d825b54dc06a4aebbce
---

## 问题现象

HarmonyOS是否有组件可以实现跑马灯效果？

## 背景知识

* 在HarmonyOS中，使用[Marquee组件](../harmonyos-references/ts-basic-components-marquee.md)可实现跑马灯文字效果。
* 在HarmonyOS中，使用[Swiper组件](../harmonyos-references/ts-container-swiper.md)的自动播放属性可模拟跑马灯效果。
* 从API version 18开始，[Text](../harmonyos-guides/arkts-common-components-text-display.md)文本超长时设置跑马灯的方式展示时，支持设置跑马灯的配置项，比如开关、步长、循环次数、方向等。
* Marquee组件无法展示一系列图片的滚动，可通过使用Row组件的[translate](../harmonyos-references/ts-universal-attributes-transformation.md#translate)属性将图片沿水平方向平移指定距离实现图片滚动，自定义图片实现跑马灯效果。

## 解决方案

* **场景一**：使用Marquee组件实现文字跑马灯效果。

  ```ts
  @Entry
  @Component
  struct MarqueeExample {
    @State start: boolean = false;
    @State fontSizeNum: number = 32;
    @State marqueeText: string =  '我是一串超级超级超级超级超级超级超级超级超级超级超级超级超级超级超级超级超级超级超级超级超级超级超级超级超级超级超级超级超级超级超级超级超级长的文本';
    private fromStart: boolean = true;
    @State step: number = 10;

    build() {
      Column() {
        Marquee({
          start: this.start,
          step: this.step,
          loop: -1,
          fromStart: this.fromStart,
          src: this.marqueeText
        })
          .marqueeUpdateStrategy(MarqueeUpdateStrategy.PRESERVE_POSITION)
          .width('300vp')
          .fontColor('#FFFFFF')
          .fontSize(this.fontSizeNum)
          .fontWeight(700)
          .backgroundColor('#182431')
          .margin({ bottom: '40vp' })
          .onClick(()=>{
            this.fontSizeNum=this.fontSizeNum>16?16:this.fontSizeNum;
            this.start=!this.start;
          })

      }
      .justifyContent(FlexAlign.Center)
      .width('100%')
      .height('100%')
    }
  }
  ```

  效果预览:

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/CGeUOMNYSvyYS7lCNf3iew/zh-cn_image_0000002658910373.png "点击放大")
* **场景二**：使用Swiper组件实现文字跑马灯效果。

  ```ts
  @Entry
  @Component
  struct MarqueeExample2 {
    build() {
      Column() {
        Swiper() {
          ForEach(['Running', 'Swiper', 'test'], (item: string) => {
            Text(item)
              .fontColor($r('sys.color.black'))
              .fontSize(14)
              .textAlign(TextAlign.Start)
              .width('100%')
          }, (item: string) => item)
        }
        .displayMode(SwiperDisplayMode.STRETCH)
        .loop(true)
        .autoPlay(true)
        // 垂直方向
        .vertical(false)
        // 去掉指示器
        .indicator(false)
        .duration(2500)
        .curve(Curve.Linear)
        .interval(1000)
        .margin(16)
        .width(100)
      }
      .width('100%')
      .height('100%')
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/rB3FlR6YR-iaXPE_hN8D9w/zh-cn_image_0000002628391168.png "点击放大")
* **场景三**：使用Text组件实现文字跑马灯效果。

  ```ts
  @Entry
  @Component
  struct MarqueeExample3 {
    build() {
      Column() {
        Text('当文本溢出其尺寸时，文本将滚动显示。When the text overflows its dimensions, the text will scroll for displaying.')
          .width(250)
          .textOverflow({ overflow: TextOverflow.MARQUEE })
          .maxLines(1)
          .fontSize(12)
          .border({ width: 1 })
          .padding(10)
        Text('当文本溢出其尺寸时，文本将滚动显示，支持设置跑马灯配置项。When the text overflows its dimensions, the text will scroll for displaying.')
          .width(250)
          .textOverflow({ overflow: TextOverflow.MARQUEE })
          .maxLines(1)
          .fontSize(12)
          .border({ width: 1 })
          .padding(10)
          .marqueeOptions({
            start: true,
            fromStart: true,
            step: 6,
            loop: -1,
            delay: 0,
            fadeout: false,
            marqueeStartPolicy: MarqueeStartPolicy.DEFAULT
          })
      }
      .width('100%')
      .height('100%')
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/_gY5UEBzReeViUaET1qBzA/zh-cn_image_0000002658790417.png "点击放大")
* **场景四**：使用Row组件的translate属性平移方式实现图片的跑马灯效果。

  ```ts
  // 将图片沿着水平方向平移offsetX的距离，设置超时时间duration，平移距离offsetX>=0或者小于等于2倍的contentWidth宽度时，则将平移距离offsetX进行重置可实现图片循环滚动，
  @Entry
  @Component
  struct MarqueeExample4 {
    @State isAnimating: boolean = false;
    duration: number = 20;
    @State offsetX: number = 100; // 设置偏移，可使界面左右都能滑动
    contentWidth: number = 100; // 数据内容宽度初始值
    autoOffset: number = 1; // 偏移值

    build() {
      Row({ space: 2 }) {
        ForEach(['', '', ''], () => {
          Row() {
            this.currentItem();
          }
          .translate({ x: this.offsetX })
        }, () => {
          return `xxxx`;
        })
      }
      .onAppear(() => {
        // 在组件出现时获取高度
        this.startScrolling();
      })
      .width('100%').backgroundColor(Color.Transparent).height('100%')
    }

    @Builder
    currentItem() {
      Image($r('app.media.startIcon')).width(100).height(100); // 此处'app.media.startIcon'仅作示例，请开发者自行更换
      Image($r('app.media.startIcon')).width(100).height(100);
      Image($r('app.media.startIcon')).width(100).height(100);
      Image($r('app.media.startIcon')).width(100).height(100);
      Image($r('app.media.startIcon')).width(100).height(100);
      Image($r('app.media.startIcon')).width(100).height(100);
      Image($r('app.media.startIcon')).width(100).height(100);
      Image($r('app.media.startIcon')).width(100).height(100);
    }

    private startScrolling() {
      this.isAnimating = true;
      this.animate();
    }

    private animate() {
      if (!this.isAnimating) {
        return;
      }
      setTimeout(() => {
        // 继续当前方向的滚动
        this.offsetX = this.offsetX - this.autoOffset;
        // 检查是否需要重置位置
        if (this.offsetX >= 0 || this.offsetX <= -this.contentWidth * 2) {
          this.offsetX = -this.contentWidth;
        }
        if (this.isAnimating) {
          this.animate();
        }
      }, this.duration);
    }
  }
  ```

  效果预览:

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/KQVUIBzuS5ObzzPXKgpHMw/zh-cn_image_0000002628551058.png "点击放大")
* **场景五**：每条消息会先停留两秒以便阅读，然后自动从左到右滚动显示全文；滚动结束后再停顿两秒，随后显示下一条消息，循环往复。

  ```ts
  import { AnimatorResult } from '@kit.ArkUI';

  const data: string[] =
    ['KeyboardAvoidMode.OFFSET是一种软键盘避让模式，用于解决键盘弹出时页面元素的遮挡问题。',
      '当软键盘弹出时，整个页面会整体上移，确保当前聚焦的输入框不被遮挡。',
      '余弦定理（Cosine Theorem）是三角形中一个重要的几何公式，用于计算三角形的边长或角度，尤其适用于已知两边及其夹角求第三边。'];

  // 滚动速度单位vp/s
  const speed: number = 30;

  @Entry
  @Component
  struct MarqueeExample5 {
    @State message: string = data[1];
    @State newsPosition: Position = { x: 0, y: 0 };
    @State textWidth: number = 0;
    private controller = new TextController();
    private maxWidth: number = 0;
    private animator?: AnimatorResult;
    private timer: number = -1;

    aboutToAppear(): void {
      this.textWidth =
        this.getUIContext().px2vp(this.getUIContext().getMeasureUtils().measureText({ textContent: this.message }));
      this.animator = this.getUIContext().createAnimator({
        // 建议使用this.getUIContext().createAnimator()接口
        duration: 2000,
        easing: 'linear',
        delay: 0,
        fill: 'forwards',
        direction: 'normal',
        iterations: 1,
        begin: 0, // 动画插值起点
        end: 2000 // 动画插值终点
      });
    }

    aboutToDisappear(): void {
      this.animator = undefined;
    }

    async sleep(time: number) {
      return await new Promise<void>(resolve => {
        this.timer = setTimeout(() => {
          resolve();
        }, time);
      });
    }

    async move() {
      this.textWidth =
        this.getUIContext().px2vp(this.getUIContext().getMeasureUtils().measureText({ textContent: this.message }));
      this.newsPosition.x = 0;
      await this.sleep(2000);
      clearTimeout(this.timer);
      let line = this.controller.getLayoutManager().getLineMetrics(0);
      let promise: Promise<boolean> = new Promise(resolve => {
        if (line) {
          let time = Math.max(0, this.getUIContext().px2vp(line.width) - this.maxWidth) / speed;
          if (time <= 0) {
            resolve(false);
          } else {
            if (this.animator) {
              this.animator.reset({
                // 建议使用this.getUIContext().createAnimator()接口
                duration: time * 1000,
                easing: 'linear',
                delay: 0,
                fill: 'forwards',
                direction: 'normal',
                iterations: 1,
                begin: 0, // 动画插值起点
                end: Math.floor(time * 1000) // 动画插值终点
              });
              this.animator.onFrame = progress => {
                this.newsPosition.x =
                  -Math.max(0, this.getUIContext().px2vp(line.width) - this.maxWidth) * progress /
                  Math.floor(time * 1000);
              };
              this.animator.play();
              this.animator.onFinish = () => {
                resolve(true);
              };
            } else {
              resolve(false);
            }
          }
        } else {
          resolve(false);
        }
      });
      await promise;
      await this.sleep(2000);
      clearTimeout(this.timer);
      this.message = this.message === data[0] ? data[1] : data[0];
      this.move();
    }

    build() {
      Column() {
        Row() {
          Text(this.message, { controller: this.controller })
            .offset(this.newsPosition,)
            .maxLines(1)
            .width(this.textWidth)
            .onAppear(() => {
              this.move();
            })
        }
        .clip(true)
        .width('80%')
        .onAreaChange((_, newValue) => {
          this.maxWidth = Number(newValue.width);
        })

        Button('更新')
          .onClick(() => {
            this.message = data[2];
            this.animator?.pause();
            clearTimeout(this.timer);
            this.move();
          })
      }
      .width('100%')
      .height('100%')
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/SFzz7UciTf6nCWn6IBhoBw/zh-cn_image_0000002658910375.png "点击放大")

## 常见FAQ

Q：同样设置loop=-1，为什么Marquee在卡片场景动效只执行一次，在普通场景可无限循环？

A：根据[MarqueeOptions说明文档](../harmonyos-references/ts-basic-components-marquee.md#marqueeoptions18对象说明)，ArkTS卡片上Marquee的loop参数设置任意值都仅在可见时滚动一次。

Q：使用Marquee组件如何实现如下场景：给智慧屏设备和column容器（包含图片和文本）添加悬浮事件，当无悬浮事件时，超长文本展示为省略号样式。当存在悬浮事件时，超长文本展示效果为跑马灯效果。

A：实现代码示例参考如下：

```ts
@Entry
@Component
struct Faq1 {
  @State message: string = 'Hello World Hello World Hello World Hello World Hello World';
  @State isRun: boolean = false;

  build() {
    Column({ space: 10 }) {
      Image($r('app.media.startIcon'))
        .width(200)
        .height(200)

      if (this.isRun) {
        Marquee({
          start: this.isRun,
          step: 10,
          fromStart: true,
          src: this.message
        })
          .marqueeUpdateStrategy(MarqueeUpdateStrategy.DEFAULT)
          .width('300vp')
          .height('60vp')
          .fontSize('50fp')
          .allowScale(true)
          .backgroundColor('#666666')
          .margin({ top: '10vp' })
      } else {
        Text(this.message)
          .width(300)
          .height(60)
          .fontSize(50)
          .focusable(true)
          .focusOnTouch(true)
          .margin({ top: 10 })
          .maxLines(1)
          .textOverflow({ overflow: TextOverflow.Ellipsis })
          .backgroundColor('#666666')
      }
    }
    .onHover((isHover: boolean) => {
      this.isRun = isHover; // 悬浮事件，悬浮时为true，实现跑马灯效果
    })
    .alignItems(HorizontalAlign.Center)
    .height('50%')
    .width('100%')
    .backgroundColor(Color.Blue)
  }
}
```

Q：如何实现不同颜色文字的跑马灯？

A：可以在Text组件中添加不同颜色文字的Span组件，设置文本超长时以跑马灯的方式展示。

```ts
@Entry
@Component
struct Faq2 {
  build() {
    Column() {
      Text() {
        Span('实现不同')
          .fontColor(Color.Red)
        Span('文字颜色')
          .fontColor(Color.Blue)
        Span('跑马灯')
          .fontColor(Color.Black)
      }
      .margin(20)
      .width('100%')
      .fontSize(60)
      // 设置文本超长时以跑马灯的方式展示
      .textOverflow({ overflow: TextOverflow.MARQUEE })
    }
  }
}
```
