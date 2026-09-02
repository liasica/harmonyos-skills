---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1435
title: TabContent切换后onWillShow，onWillHide回调次数异常
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > TabContent切换后onWillShow，onWillHide回调次数异常
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:21+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3d5b7255d7ca510a5423d1ed28bd145b556beeaec29d3931d43d540e9ea46561
---

## 问题现象

Tabs组件中TabContent切换时，onWillShow，onWillHide均会回调两次。

问题代码示例参考如下：

```ts
@Entry
@Component
struct Index {
  private controller: TabsController = new TabsController();
  @State currentPageId: number = 0;

  build() {
    Column() {
      Tabs({ controller: this.controller }) {
        // Home
        TabContent() {
          Text('首页');
        }.tabBar('首页')
        .onWillShow(() => {
          console.info('MinePage onWillShow');
        })
        .onWillHide(() => {
          console.info('MinePage onPause');
        });

        // mine
        TabContent() {
          Text('我的');
        }.tabBar('我的');
      }
      .onTabBarClick((index: number) => {
        this.currentPageId = index;
        this.controller.changeIndex(index);
      })
      .animationMode(AnimationMode.NO_ANIMATION) // 关闭切换动画
      .edgeEffect(EdgeEffect.None)
      .scrollable(false);
    }.height('100%').width('100%');
  }
}
```

重复回调日志：

```log
11-21 16:28:13.573   2054-2054     A03d00/JSAPP                    com.example.tmp_demo  I     MinePage onWillShow
11-21 16:28:20.028   2054-2054     A03d00/JSAPP                    com.example.tmp_demo  I     MinePage onPause
11-21 16:28:20.028   2054-2054     A03d00/JSAPP                    com.example.tmp_demo  I     MinePage onPause
11-21 16:28:21.000   2054-2054     A03d00/JSAPP                    com.example.tmp_demo  I     MinePage onWillShow
11-21 16:28:21.000   2054-2054     A03d00/JSAPP                    com.example.tmp_demo  I     MinePage onWillShow
```

## 解决方案

Tabs组件点击页签后即可切换TabContent并触发对应的onWillShow，onWillHide，在[onTabBarClick](../harmonyos-references/ts-container-tabs.md#ontabbarclick10)中使用[changeIndex](../harmonyos-references/ts-container-tabs.md#changeindex)方法后使得TabContent跳转了两次，因而触发了两次onWillShow或onWillHide方法。

在onTabBarClick方法中删去语句this.controller.changeIndex(index)即可。使用自定义TabBar的情况下才需要点击后使用TabsController控制Tabs切换。
