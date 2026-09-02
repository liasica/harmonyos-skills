---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-757
title: 如何解决动画瞬间出现效果不连续的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何解决动画瞬间出现效果不连续的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:21+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2f33e0aeb495b9c7c678f4dd2b8f6a27474258e86444d3a87cc851357d0b300e
---

## 问题现象

动画渲染异常，动画效果不流畅，列表的子组件是瞬间出现，而不是渐入渐出。

应用场景：列表添加数据等一系列场景。比如添加购物车时，所添加的商品会排在首位，渲染异常导致用户体验感差。

问题代码示例参考如下：

```ts
@Entry
@Component
struct ListDemo {
  @State message: number[] = [1, 2, 3];
  @State num: number = 4;
  listController: Scroller = new Scroller();

  build() {
    Column() {
      Stack() {
        List({ scroller: this.listController }) {
          ForEach(this.message, (item: number) => {
            ListItem() {
              ListItemComponent({ titleText: item.toString(), subTitleText: `sub:${item}` });
            }
            .margin({
              bottom: 5
            });
          }, (item: number) => item.toString());
        }
        .alignListItem(ListItemAlign.Center)
        .width('100%');
      }
      .alignContent(Alignment.TopStart)
      .layoutWeight(1);

      Button('添加')
        .onClick(() => {
          this.message.splice(1, 0, this.num);
          this.num++;
        });
    }
    .justifyContent(FlexAlign.Start)
    .height('100%')
    .width('100%');
  }
}

@Component
struct ListItemComponent {
  @Prop titleText: string = '';
  @Prop subTitleText: string = '';
  @State heightValue: number = 0;
  @State opacityValue: number = 0.0;

  build() {
    Column() {
      Text(this.titleText)
        .height(30);
      Blank()
        .height(10);
      Text(this.subTitleText)
        .height(25);
    }
    .justifyContent(FlexAlign.Center)
    .width('70%')
    .height(this.heightValue)
    .opacity(this.opacityValue)
    .border({ width: 1 })
    .justifyContent(FlexAlign.Center)
    .onAppear(() => {
      this.getUIContext().keyframeAnimateTo({},
        [{
          duration: 600,
          curve: Curve.EaseOut,
          event: () => {
            this.heightValue = 80;
          }
        },
          {
            duration: 200,
            curve: Curve.Linear,
            event: () => {
              this.opacityValue = 1.0;
            }
          }
        ]);
    });
  }
}
```

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/cVckybXrQXiVI5dqMOePgg/zh-cn_image_0000002658914689.gif "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/hS17NnvWRA6hpKQ5n4JYbA/zh-cn_image_0000002658794741.gif "点击放大")

## 背景知识

* 组件挂载显示后触发[onAppear](../harmonyos-references/ts-universal-events-show-hide.md#onappear)回调。可在回调中添加逻辑代码。
* [keyframeAnimateTo](../harmonyos-references/ts-keyframeanimateto.md)接口来指定若干个关键帧状态，实现分段的动画。

## 解决方案

可在onAppear回调中使用keyframeAnimateTo进行关键帧动画，改变高度和透明度，实现淡入和展开的效果。

```ts
@Entry
@Component
struct ListDemo {
  @State message: number[] = [1, 2, 3];
  @State num: number = 4;
  listController: Scroller = new Scroller();

  build() {
    Column() {
      Stack() {
        List({ scroller: this.listController }) {
          ForEach(this.message, (item: number) => {
            ListItem() {
              ListItemComponent2({ titleText: item.toString(), subTitleText: `sub:${item}` });
            }
            .margin({
              bottom: 5
            });
          }, (item: number) => item.toString());
        }
        .alignListItem(ListItemAlign.Center)
        .width('100%');
      }
      .alignContent(Alignment.TopStart)
      .layoutWeight(1);

      Button('添加')
        .onClick(() => {
          this.message.splice(1, 0, this.num);
          this.num++;
        });
    }
    .justifyContent(FlexAlign.Start)
    .height('100%')
    .width('100%');
  }
}

@Component
struct ListItemComponent2 {
  @Prop titleText: string = '';
  @Prop subTitleText: string = '';
  @State heightValue: number = 0;
  @State opacityValue: number = 0.0;

  build() {
    Column() {
      Text(this.titleText)
        .height(30);
      Blank()
        .height(10);
      Text(this.subTitleText)

        .height(25);
    }
    .width('70%')
    .height(this.heightValue)
    .opacity(this.opacityValue)
    .border({ width: 1 })
    .justifyContent(FlexAlign.Center)
    .onAppear(() => {
      // 通过keyframeAnimateTo分段调整高度和透明度实现淡入和展开的效果
      this.getUIContext().keyframeAnimateTo(
        { iterations: 1 },
        [
          {
            duration: 0,
            curve: Curve.EaseOut,
            event: () => {
              this.heightValue = 0;
            }
          },
          {
            duration: 600,
            curve: Curve.Linear,
            event: () => {
              this.heightValue = 80;
            }
          }
        ]);

      this.getUIContext().keyframeAnimateTo(
        { iterations: 1 },
        [
          {
            duration: 400,
            curve: Curve.EaseOut,
            event: () => {
              this.opacityValue = 0;
            }
          },
          {
            duration: 600,
            curve: Curve.Linear,
            event: () => {
              this.opacityValue = 1;
            }
          }
        ]);
    });
  }
}
```
