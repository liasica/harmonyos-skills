---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-582
title: 如何获取目标组件相对位置信息
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何获取目标组件相对位置信息
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:01+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b188eb2a4d64a7d6e4e8fbbe9a6d5654d7d45098cefe6b93205c61267387dd78
---

## 问题现象

如何获取当前组件相对位置信息有以下场景：

* 如何获取目标组件相对父元素位置信息？
* 如何获取目标组件相对屏幕顶部的信息？

## 背景知识

* [onAreaChange](../harmonyos-references/ts-universal-component-area-change-event.md#onareachange)：组件区域变化时触发该回调。仅会响应由布局变化所导致的组件大小、位置发生变化时的回调。
* [createComponentObserver](../harmonyos-references/arkts-apis-uicontext-uiinspector.md#createcomponentobserver)：注册组件布局和组件绘制送显完成回调通知。
* [getRectangleById](../harmonyos-references/arkts-apis-uicontext-componentutils.md#getrectanglebyid)：获取组件大小、位置、平移、缩放、旋转及仿射矩阵属性信息。

## 解决方案

* 方案一：通过onAreaChange中返回参数获取目标组件相对父元素和页面左上角的坐标位置。

  | 名称 | 类型 | 说明 |
  | --- | --- | --- |
  | position | [Position](../harmonyos-references/ts-types.md#position) | 目标元素左上角在以父元素为基准的组件坐标系中的位置。 |
  | globalPosition | Position | 目标元素左上角在当前窗口坐标系中的位置。 |

  ```ts
  import { window } from '@kit.ArkUI';

  interface T {
    x: string,
    y: string
  }

  @Entry
  @Component
  struct AreaExample {
    @State sizeValue: string = '';
    @State pos: T | undefined = undefined;
    @State statusBarHeight: number = 0;

    aboutToAppear(): void {
      let type1 = window.AvoidAreaType.TYPE_SYSTEM;
      window.getLastWindow(this.getUIContext().getHostContext())
        .then((data) => {
          // 获取系统默认区域，一般包括状态栏、导航栏
          let avoidArea1 = data.getWindowAvoidArea(type1);
          // 顶部状态栏高度
          this.statusBarHeight = avoidArea1.topRect.height;
        });
    }

    build() {
      Column() {
        Row() {
          Text('目标组件')
            .fontSize(20)
            .fontWeight(FontWeight.Bold)
            .onAreaChange((oldValue: Area, newValue: Area) => {
              this.sizeValue = `${Number(newValue.globalPosition.y).toFixed()}vp。`;
              this.pos = {
                x: Number(newValue.position.x).toFixed(),
                y: Number(newValue.position.y).toFixed()
              };
              console.info(oldValue.width.toString());
            });
        }
        .width('calc(100% - 32vp)')
        .height(200)
        .backgroundColor('#f1f3f5')
        .margin({
          left: 16,
          right: 16
        })
        .alignItems(VerticalAlign.Center)
        .justifyContent(FlexAlign.Center);

        Column() {
          Text(`通过getLastWindow获取顶部状态栏高度：${this.getUIContext().px2vp(this.statusBarHeight).toFixed()}vp。`)
            .width('100%');
          Divider().height(22).color('#182431').opacity(0.6);
          Text(`通过onAreaChange获取目标组件距离屏幕顶部的距离：${this.sizeValue}`).width('100%');
          Text(`通过onAreaChange获取目标组件距离父元素的位置：${JSON.stringify(this.pos)}。`).width('100%');
        }
        .margin({ top: 30, left: 16, right: 16});
      }
      .width('100%').height('100%');
    }
  }
  ```

  示例实现效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/DmIIuh3pRIOGkOboc8Ej9Q/zh-cn_image_0000002628392494.png "点击放大")

* 方案二：通过inspector.createComponentObserver绑定指定组件，返回对应的监听句柄，结合getRectangleById中返回参数获取目标组件相对父元素和相对于屏幕的信息。

  | 名称 | 类型 | 说明 |
  | --- | --- | --- |
  | localOffset | [Offset](../harmonyos-references/js-apis-arkui-componentutils.md#offset) | 组件相对于父组件信息。 |
  | screenOffset | Offset | 组件相对于屏幕信息。 |

  ```ts
  @Entry
  @Component
  struct AreaExample2 {
    @State localOffset: string = '';
    @State screenOffset: string = '';

    aboutToAppear(): void {
      this.init();
    }

    // 初始化方法：获取初始位置
    init() {
      // 绑定指定组件，返回对应的监听句柄
      let observer = this.getUIContext().getUIInspector().createComponentObserver('target');
      // 通过句柄向对应的查询条件注册回调，当组件布局完成时会触发该回调。type:必须填写字符串'layout'或'draw'。layout:组件布局完成。draw:组件绘制送显完成。
      observer.on('layout', () => {
        let node = this.getUIContext().getComponentUtils().getRectangleById('target');
        if (node) {
          this.localOffset = JSON.stringify(node.localOffset);
          this.screenOffset = JSON.stringify(node.screenOffset);
        }
        // 通过句柄向对应的查询条件取消注册回调，当组件布局完成时不再触发指定的回调。
        observer.off('layout');
      });
    }

    build() {
      Column() {
        Row() {
          Text('目标组件')
            .fontSize(20)
            .fontWeight(FontWeight.Bold)
            .key('target');
        }
        .width('calc(100% - 32vp)')
        .height(200)
        .backgroundColor('#f1f3f5')
        .margin({
          left: 16,
          right: 16
        })
        .alignItems(VerticalAlign.Center)
        .justifyContent(FlexAlign.Center);

        Column() {
          Text(`通过getRectangleById获取目标组件相对于屏幕信息：${this.screenOffset}。`).width('100%');
          Text(`通过getRectangleById获取目标组件距离父元素的位置：${this.localOffset}。`).width('100%');
        }
        .margin({ top: 30, left: 16, right: 16});
      }
      .width('100%').height('100%');
    }
  }
  ```

  示例实现效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/hRA3aYk3SlioonzUtfQ-1w/zh-cn_image_0000002658911711.png "点击放大")

## 总结

| 方案 | 区别 |
| --- | --- |
| 方案一 | onAreaChange组件区域变化时触发该回调。仅会响应由布局变化所导致的组件大小、位置发生变化时的回调。由绘制变化所导致的渲染属性变化不会响应回调，如translate、offset。若组件自身位置由绘制变化决定也不会响应回调，如bindSheet。 |
| 方案二 | createComponentObserver注册组件布局和组件绘制送显完成回调通知。getRectangleById可获取组件大小、位置、平移、缩放、旋转及仿射矩阵属性信息。 |
