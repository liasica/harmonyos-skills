---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-purax-10
title: 解决应用页面通过折叠屏展开出现自动放大的问题
breadcrumb: FAQ > 多设备场景 > 手机 > Pura X常见问题 > 解决应用页面通过折叠屏展开出现自动放大的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:05a9bd78e74865f1b5d33da5e73864cc5ee6326ae88992f3af38e28cb0f89d20
---

## 问题现象

应用首页在折叠屏展开时，内容区域（图标与图片）会自动放大填充屏幕，未能实现多列或更优的布局适配，导致实际展示的内容条目数量比折叠状态下更少。

## 背景知识

* 本案例的图标列表主要通过[自适应布局](../best-practices/bpta-multi-device-adaptive-layout.md)的[均分能力](../best-practices/bpta-multi-device-adaptive-layout.md#均分能力)实现，均分能力是指容器组件尺寸发生变化时，增加或减小的空间均匀分配给容器组件内所有空白区域。通过将Row组件、Column组件或Flex组件的justifyContent属性设置为FlexAlign.SpaceEvenly，即子元素在父容器主轴方向等间距布局，相邻元素之间的间距、第一个元素与行首的间距、最后一个元素到行尾的间距都完全一样。
* 图片列表主要通过响应式布局的[断点](../best-practices/bpta-multi-device-responsive-layout.md#section1532120147301)能力和[媒体查询](../best-practices/bpta-multi-device-responsive-layout.md#section1950102518311)实现。需要在windowStage.loadContent()页面加载后直接获取横向断点值，并通过window.on('windowSizeChange')监听窗口尺寸变化，自定义实现断点值的更新。

## 解决方案

1. 关于小图标栏目的宽度设置，建议尽量避免使用百分比数值，可替换为固定数值，以便适配折叠屏展开页面。
2. 对于图片显示列表，监听屏幕是否切换到折叠屏形态，若处于折叠屏，则将图片列表分为两列显示。

   示例代码如下：

```ts
@Entry
@Component
struct fold_test {
  @StorageLink('breakPoint') breakPoint: string = 'sm';
  allBusinessList: string[] = ['基金投资', '理财产品', '信用卡', '账单'];
  private arr: number[] = [0, 1, 2, 3];

  build() {
    Row() {
      Column() {
        Scroll() {
          Column() {
            Column() {
              // 应用图标
              this.buildButtonBusiness(this.allBusinessList.slice(0, 4));
            }
            .backgroundColor(Color.White)
            .width('100%')
            .justifyContent(FlexAlign.SpaceBetween)
            .borderRadius('16vp')
            .padding('16vp')
            .margin({
              top: '16vp',
              bottom: '10vp',
            });

            // 图片列表
            List({ space: 10 }) {
              ForEach(this.arr, () => {
                ListItem() {
                  // 本地资源，需自行替换
                  Image($r('app.media.startIcon'))
                    .width('100%')
                    .objectFit(ImageFit.Fill)
                    .borderRadius('16vp')
                    .margin({ top: 6 });
                };
              });
            }
            .scrollBar(BarState.Off)
            .lanes(this.breakPoint === 'sm' ? 1 : 2, '16vp')
            .width('100%')
            .height('100%');

          };
        }
        .scrollBar(BarState.Off);
      };
    }
    .padding({
      top: '8vp',
      left: '24vp',
      right: '24vp'
    })
    .alignItems(VerticalAlign.Top)
    .backgroundColor('#ffeeeded')
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
  }

  // 显示图标列表
  @Builder
  buildButtonBusiness(list: string[]) {
    Row() {
      ForEach(list, (item: string) => {
        Column({ space: 4 }) {
          // 本地资源，需自行替换
          Image($r('app.media.startIcon'))
            .width('24vp');
          Text(item.toString())
            .fontSize('12fp')
            .fontColor(Color.Black);
        };
      }, (item: String, index?: number) => index + JSON.stringify(item));
    }
    .justifyContent(FlexAlign.SpaceEvenly)
    .width('100%')
    .padding({
      top: '8vp'
    });
  }
}
```

EntryAbility.ets文件部分代码如下：

```ts
onWindowStageCreate(windowStage: window.WindowStage): void {
  let windowObj: window.Window | undefined = undefined;
  windowStage.getMainWindow().then((data: window.Window) => {
    windowObj = data;
    this.updateBreakpoint(windowObj.getWindowProperties().windowRect.width);
    windowObj.on('windowSizeChange', (windowSize: window.Size) => {
      this.updateBreakpoint(windowSize.width);
    });
  });

  windowStage.loadContent('pages/Index', (err) => {
    if (err.code) {
      hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
      return;
    }
    hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
  });
}

private updateBreakpoint(windowWidth: number): void {
  let windowWidthVp = windowWidth / display.getDefaultDisplaySync().densityPixels;
  let curBp: string = '';
  if (windowWidthVp < 600) {
    curBp = 'sm';
  } else if (windowWidthVp < 840) {
    curBp = 'md';
  }
  AppStorage.setOrCreate('breakPoint', curBp);
}
```
