---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1548
title: 如何使Grid组件的可拖拽子项居中显示
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何使Grid组件的可拖拽子项居中显示
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:fd8a0208a2ed8008cdd2f593f21a2fc8798ecb7af71b185ec8cde689c6a85f5c
---

## 问题现象

Grid组件无法兼顾高度100%、子组件居中、拖拽事件三者同时存在。具体现象是：设置高度100%后，可以拖拽，但子项无法上下居中；如果想居中，就必须设置rowsTemplate和columnsTemplate，但没有拖拽动画。

## 背景知识

* [Grid组件](../harmonyos-references/ts-container-grid.md)作为网格容器，仅支持[GridItem](../harmonyos-references/ts-container-griditem.md)子组件，[属性](../harmonyos-references/ts-container-grid.md#属性)支持[通用属性](../harmonyos-references/ts-component-general-attributes.md)、[滚动组件通用接口](../harmonyos-references/ts-container-scrollable-common.md)以及columnsTemplate、rowsTemplate等属性。
* [columnsTemplate](../harmonyos-references/ts-container-grid.md#columnstemplate)设置当前网格布局列的数量、固定列宽或最小列宽值，不设置时默认1列。设置为'0fr'时，该列的列宽为0，不显示GridItem。
* [supportAnimation](../harmonyos-references/ts-container-grid.md#supportanimation8)设置是否支持动画。仅在滚动模式下（只设置rowsTemplate、columnsTemplate其中一个）支持动画。

## 解决方案

在EntryAbility设置全局背景色，实现沉浸式效果，示例代码如下：

```screen
import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';

const DOMAIN = 0x0000;

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    try {
      this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
    } catch (err) {
      hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
    }
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
  }

  onDestroy(): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
        return;
      }
      hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
      windowStage.getMainWindowSync().setWindowBackgroundColor('#f1f3f5');

    });
  }

  onWindowStageDestroy(): void {
    // Main window is destroyed, release UI related resources
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
  }

  onForeground(): void {
    // Ability has brought to foreground
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
  }

  onBackground(): void {
    // Ability has back to background
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
  }
};
```

通过单独添加一个GridItem子项，将其中组件高度设置为100%，并将该项的宽值设置为0fr，这样可以保证其余GridItem子项上下居中显示，且单独添加的GridItem不显示，拖拽动画也可以保留。完整代码如下：

```screen
class TabItem {
  appletName: string = '';

  constructor(appletName: string) {
    this.appletName = appletName;
  }
}

@Entry
@Component
struct gridDemo {
  longPressTimer: number = 0;
  @State bottomNavList: TabItem[] = [
    new TabItem('首页'),
    new TabItem('消息'),
    new TabItem('通话'),
    new TabItem('设置'),
    new TabItem('我的'),
  ];

  $bottomNavList(list: TabItem[]) {
    this.bottomNavList = list;
  }

  swapBottomNavItemPosition(itemIndex: number, insertIndex: number) {
    let copyList = this.bottomNavList;
    let tmpBottomNavItem = copyList.splice(itemIndex, 1);
    copyList.splice(insertIndex, 0, tmpBottomNavItem[0]);
    this.$bottomNavList(copyList);
  }

  build() {
    Grid() {
      GridItem() { // 在最前单独添加一个GridItem，设置其中组件高度为100%
        Column()
          .height('100%');
      };

      ForEach(this.bottomNavList, (item: TabItem) => {
        GridItem() {
          this.BottomNavItem(item);
        };
      });
    }
    .height('100%')
    .layoutWeight(1)
    .align(Alignment.Center)
    .columnsTemplate('0fr 1fr 1fr 1fr 1fr 1fr') // 设置第一个GridItem的宽值为0fr，该项不显示
    .onItemDragStart((_, selectItemIndex: number) => {
      console.info('itemIndex:' + selectItemIndex);
      return this.BottomNavItem(this.bottomNavList[selectItemIndex - 1]); // 为保证拖拽时显示正确，需要将索引值-1
    })
    .onItemDrop((_, itemIndex: number, insertIndex: number) => {
      this.swapBottomNavItemPosition(itemIndex - 1, insertIndex - 1); // 为保证拖拽时显示正确，需要将索引值-1
    })
    .editMode(true)
    .backgroundColor('#F1F3F5')
    .supportAnimation(true)
    .align(Alignment.Center)
    .padding({
      left: 10,
      right: 10,
      bottom: 10 // 保留阴影不被截断
    })
  }

  // 底部Tab子项
  @Builder
  BottomNavItem(bottomNav: TabItem) {
    Column() {
      // 作用：设置padding来解决拖拽时阴影被截断的问题
      Stack({ alignContent: Alignment.TopEnd }) {
        Column({ space: 3 }) {
          Text(bottomNav.appletName)
            .fontSize(10)
            .margin({bottom:5})
        }
        .aspectRatio(1)
        .justifyContent(FlexAlign.Center)
        .shadow({ radius: 30, color: 'rgba(0,0,0,0.22)' })
        .borderRadius(12)
        .backgroundColor(Color.White)
        .margin({ top: 10, right: 10 })
        .padding({
          left: 16,
          top: 4,
          right: 16
        });
      };
    }
    .layoutWeight(1)
    .padding({
      left: 2,
      right: 2,
      bottom: 2,
      top: 2
    });
  }
}
```

**说明** 

此方法本质上是增加了一个GridItem子组件用于占满高度，保证其他GridItem子组件居中显示，所以针对拖拽时的索引值也要做出调整，上面例子将GridItem子组件添加在首位，所以对应的索引值需要-1。

实现效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/xhCeG6jNTB6TxmOkcPbSsw/zh-cn_image_0000002658848491.png "点击放大")
