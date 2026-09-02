---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-741
title: bindSheet如何在跳转后返回，仍保持原样
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > bindSheet如何在跳转后返回，仍保持原样
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:03+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f261735a80f0c7fa1862cc602ec26becd8347be809d89b251d97a6a969088e52
---

## 问题现象

bindSheet的内容是个List，点击某个ListItem跳转至其他页面，如何实现从其他页面返回后bindSheet仍是打开状态，且List仍保持原样？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/5rEyeVgiTxaIT8iSgSqQig/zh-cn_image_0000002628555360.png "点击放大")

## 背景知识

* [bindSheet](../harmonyos-guides/arkts-sheet-page.md)：默认是模态形式的非全屏弹窗式交互页面，允许部分底层父视图可见，帮助用户在与半模态交互时保留其父视图环境。
* [AppStorage](../harmonyos-guides/arkts-appstorage.md)：AppStorage是与应用进程绑定的全局UI状态存储中心，由UI框架在应用启动时创建，将UI状态数据存储于运行内存，实现应用级全局状态共享。

## 解决方案

在[onPageShow](../harmonyos-references/ts-custom-component-lifecycle.md#onpageshow)生命周期中，通过AppStorage获取当前bindSheet显示状态以及List滑动距离，在跳转其他页面时记录当前List滑动距离，当目标页面返回时将bindSheet显隐状态绑定的变量设置为true，且在List的onAppear中通过Scroller滑动至之前保存的位置，实现保持原样的效果。参考代码如下：

```ts
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct BindSheetOnePage {
  @StorageProp('isTrue') isShow: boolean = false;
  @State numArr: number[] = [];
  private scrollerForList: Scroller = new Scroller();
  @State currentY: number = 0;

  onPageShow(): void {
    // 全局获取半模态的状态
    this.isShow = AppStorage.get('isTrue') as boolean;
    // 全局获取List当前位置
    this.currentY = AppStorage.get('currentY') as number;
    // 设置沉浸式
    window.getLastWindow(this.getUIContext().getHostContext(), (err, win) => {
      console.error(`err: ${err}`);
      win.setWindowLayoutFullScreen(true);
    });
  }

  aboutToAppear(): void {
    // 插入list数据
    for (let index = 0; index < 20; index++) {
      this.numArr.push(index);
    }
  }

  @Builder
  myBuilder() {
    List({ scroller: this.scrollerForList }) {
      ForEach(this.numArr, (item: number) => {
        ListItem() {
          Column() {
            Text(item.toString());
          }
          .justifyContent(FlexAlign.Center)
          .height('20%')
          .width('100%')
          .backgroundColor('#F3F3F3')
          .onClick(() => {
            // 全局存储当前List滑动距离
            AppStorage.setOrCreate('currentY', this.scrollerForList.currentOffset().yOffset);
            // 跳转到下一个页面
            this.getUIContext().getRouter().pushUrl({
              url: 'pages/BindSheetTwoPage'
            }).catch((e: BusinessError) => {
              console.error(`e: ${e}`);
            });
          });
        };
      });
    }
    .margin({
      left: 16,
      right: 16
    })
    .onAppear(() => {
      // 通过Scroller滑动至之前保存的位置，实现保持原样的效果
      this.scrollerForList.scrollTo({ xOffset: 0, yOffset: this.currentY });
    })
    .height('100%');
  }

  build() {
    Column() {
      Button('transition modal 1')
        .onClick(() => {
          // 点击打开半模态
          this.isShow = true;
          // 全局存储半模态状态
          AppStorage.setOrCreate('isTrue', true);
        })
        .fontSize(20)
        .margin(10)
        // $$双向同步半模态的状态
        .bindSheet($$this.isShow, this.myBuilder(), {
          height: 600,
          title: { title: "title" },
          onAppear: () => {
            console.info('BindSheet onAppear.');
          },
          onDisappear: () => {
            console.info('BindSheet onDisappear.');
          }
        });
    }
    .backgroundColor($r('sys.color.point_color_checked'))
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%');
  }
}
```

路由目标页面代码如下：

```ts
@Entry
@Component
struct BindSheetTwoPage {
  build() {
    Column() {
      Text('Hello World')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .onClick(() => {
          // 点击返回上个页面
          this.getUIContext().getRouter().back();
        });
    }
    .backgroundColor($r('sys.color.point_color_checked'))
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%');
  }
}
```
