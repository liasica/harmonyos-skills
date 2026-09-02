---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1582
title: 将点击事件中的坐标转换为相对坐标
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 将点击事件中的坐标转换为相对坐标
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:11+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:bbc82d07e08ba43c1953ccf7ab5082f02660279d0f69589fc4696412228f8da0
---

## 问题现象

通过子组件的点击事件获取点击处的坐标后，如何将该坐标转换为其相对于父组件的坐标？

## 背景知识

* [getRectangleById](../harmonyos-references/arkts-apis-uicontext-componentutils.md#getrectanglebyid)：根据组件ID获取组件实例对象，通过组件实例对象将获取的坐标位置和大小返回给开发者。组件的坐标值为组件左上角顶点的坐标值。
* [onAreaChange](../harmonyos-references/ts-universal-component-area-change-event.md#onareachange)在组件区域变化时触发该回调，返回目标元素变化之后的宽高以及目标元素相对父元素和页面左上角的坐标位置。

## 解决方案

* 方案一：使用componentUtils.getRectangleById获取的localOffset为子组件在父组件中的坐标，onTouch事件获取的x，y为触摸点在子组件中的坐标，二者相加，即可得到触摸点在父组件中的坐标。

  完整代码如下所示：

  ```ts
  @Entry
  @Component
  struct Index {
    @State startXIn: number = 0;
    @State startYIn: number = 0;

    build() {
      Column() {
        Column() {
          Image($r('app.media.background'))
            .id('123456')
            .width(150)
            .height(200)
            .onTouch((event) => {
              let modePosition = this.getUIContext().getComponentUtils().getRectangleById('123456');
              // 组件相对于父组件信息
              let imageX = this.getUIContext().px2vp(modePosition.localOffset.x);
              let imageY = this.getUIContext().px2vp(modePosition.localOffset.y);
              console.info('localOffset 是', `${imageX} `, `${imageY}`);
              // 子组件内位移
              let startX = event.touches[0].x;
              let startY = event.touches[0].y;
              console.info(`touches 是`, `${startX}`, `${startY}`);
              // 将坐标转换为相对于父组件的坐标
              this.startXIn = startX + imageX;
              this.startYIn = startY + imageY;
            });
        }.width(200)
        .height(250)
        .backgroundColor('#61CFBE')
        .justifyContent(FlexAlign.Center);

        Text(`点击处相对于父组件的横坐标：${this.startXIn}`);
        Text(`点击处相对于父组件的纵坐标：${this.startYIn}`);
      }
      .height('100%')
      .width('100%');
    }
  }
  ```
* 方案二：使用onAreaChange可以获取子组件相对于父组件的坐标offsetX和offsetY，ClickEvent中的x，y为点击处在子组件中的坐标，二者相加，即可得到触摸点在父组件中的坐标。

  完整代码如下所示：

  ```ts
  @Entry
  @Component
  struct Index2 {
    @State startXIn: number = 0;
    @State startYIn: number = 0;
    @State offsetX: number = 0;
    @State offsetY: number = 0;

    build() {
      Column() {
        Column() {
          Image($r('app.media.background'))
            .width(150)
            .height(200)
            .onAreaChange((oldValue: Area, newValue: Area) => {
              console.info(`${oldValue}`);
              this.offsetX = Number(newValue.position.x);
              this.offsetY = Number(newValue.position.y);
            })
            .onClick((event?: ClickEvent) => {
              if (event) {
                let startX = event.x;
                let startY = event.y;
                console.info(`touches 是`, `${startX}`, `${startY}`);
                this.startXIn = startX + this.offsetX;
                this.startYIn = startY + this.offsetY;
              }
            });
        }.width(200)
        .height(250)
        .backgroundColor('#61CFBE')
        .justifyContent(FlexAlign.Center);

        Text(`点击处相对于父组件的横坐标：${this.startXIn}`);
        Text(`点击处相对于父组件的纵坐标：${this.startYIn}`);
      }
      .height('100%')
      .width('100%');
    }
  }
  ```

两者实现思路相同，只是调用的方法不同。均是使点击位置在子组件中的坐标与子组件在父组件中的坐标相加，得到点击位置相对于父组件中的坐标。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/w036QVYBQLCFITpqHxzBDQ/zh-cn_image_0000002628770194.png "点击放大")
