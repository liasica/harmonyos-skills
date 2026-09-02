---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-161
title: Web组件如何解决切换可见状态出现残留帧
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > Web组件如何解决切换可见状态出现残留帧
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:10+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5424c6102b0b656b7cc107ebd01fa26d1bddb69b1fbacc70a9ff7bbdc997d68a
---

## 问题现象

当复用同一个WebviewController，Web组件切换到不可见状态时，通过loadUrl加载新的网页后再切换到可见状态，会出现上一个页面的残留帧。

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/PaBfSx7qTseR0oT7pj6esw/zh-cn_image_0000002659258387.png "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/6ItruIUITBS63i4yUYBFSQ/zh-cn_image_0000002659138433.png "点击放大")

## 背景知识

* [onInactive](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#oninactive)：调用此接口通知Web组件进入未激活状态。开发者可以在此回调中实现应用失去焦点时应表现的恰当行为。
* [onActive](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#onactive)：调用此接口通知Web组件进入前台激活状态。
* [WebviewController](../harmonyos-references/arkts-apis-webview-webviewcontroller.md)：通过WebviewController可以控制Web组件各种行为（包括页面导航、生命周期状态、JavaScript交互等行为）。

## 解决方案

该问题主要由于Web组件在不可见到可见状态切换时，存在之前Web页面的残留帧导致的。可参考以下方案解决：

* 当Web组件的页面视图切走后，Web组件会被系统切换为onInactive状态，所以当Web组件不可见时，在调用loadUrl方法加载新页面前需要将Web组件设为onActive状态。
* 复用同一个WebviewController，当Web组件从不可见状态切换到可见状态时，会出现之前Web页面的残留帧，所以需要在Web组件切换至不可见后并在加载新页面前，使用loadUrl方法加载空URL（加载空URL前也需将Web组件置为onActive状态），这会使Web组件加载一个空白的页面，将之前页面的残留帧替换为该空白页面。加载空URL的时机，如可在Web组件由可见至不可见时就加载空URL，若存在用户切换操作，也可在用户退出时加载空URL。
* Web组件在后台时若一直保持onActive状态，可能会对功耗有影响。所以当存在使用loadUrl加载页面后但Web组件长时间未切换为可见状态的场景，需要在页面加载完成后将Web组件状态设为onInactive状态。

Web组件所在页面代码逻辑示例：

```ts
import { webview } from '@kit.ArkWeb';
import { emitter } from '@kit.BasicServicesKit';
import { PromptAction } from '@kit.ArkUI';

@Entry
@Component
struct WebPages {
  @State selectedIndex: number = 0;
  @State currentIndex: number = 0;
  private controller: TabsController = new TabsController();

  @Builder
  tabBuilder(title: string, targetIndex: number) {
    Column() {
      Text(title).fontColor(this.selectedIndex === targetIndex ? '#0a59f7' : '#6B6B6B');
    }.width('100%')
    .height(50)
    .justifyContent(FlexAlign.Center);
  }

  build() {
    Column() {
      Tabs({ barPosition: BarPosition.End, index: this.currentIndex, controller: this.controller }) {
        TabContent() {
          TabOne();
        }.tabBar(this.tabBuilder('Tab', 0));

        TabContent() {
          TabTwo();
        }.tabBar(this.tabBuilder('Tab', 1));
      }
      .vertical(false)
      .barMode(BarMode.Fixed)
      .barWidth(360)
      .barHeight(60)
      .animationDuration(0)
      .onChange((index: number) => {
        this.currentIndex = index;
        this.selectedIndex = index;
      })
      .width('100%')
      .height('100%');
    };
  }
}

@Component
export struct TabOne {
  @State webviewController: webview.WebviewController = new webview.WebviewController();
  // 用户标识
  @StorageProp('userInfo') userInfo: string = '';
  // 监听用户登录及退出操作
  @StorageProp('isLogged') @Watch('isLoggedChange') isLogged: boolean = false;
  loadNewUrl: () => void = () => {
    // 通过loadUrl加载网页前，将Web组件设置为onActive状态
    this.webviewController.onActive();
    // 此处地址实际使用过程中替换为三个不同的真实地址
    if (this.userInfo === '1') {
      this.webviewController.loadUrl('xx.xx.xx');
    } else if (this.userInfo === '2') {
      this.webviewController.loadUrl('xx.xx.xx');
    } else {
      this.webviewController.loadUrl('xx.xx.xx');
    }
  };

  aboutToAppear(): void {
    // 订阅网页加载事件，其它Tab页面会通知加载网页
    emitter.on('loadUrl', this.loadNewUrl);
  }

  isLoggedChange() {
    if (!this.isLogged) {
      // 当用户退出时，将Web组件设置为onActive状态后加载空URL
      this.webviewController.onActive();
      this.webviewController.loadUrl('about:blank');
    }
  }

  aboutToDisappear(): void {
    emitter.off('loadUrl');
  }

  getSrc() {
    // 此处地址实际使用过程中替换为三个不同的真实地址
    let src = 'xx.xx.xx';
    if (this.userInfo === '1') {
      src = 'xx.xx.xx';
    } else if (this.userInfo === '2') {
      src = 'xx.xx.xx';
    }
    return src;
  }

  build() {
    Web({
      src: this.getSrc(),
      controller: this.webviewController
    })
      .onPageEnd((event) => {
        // Web组件在后台时若一直保持onActive状态，可能会对功耗有影响。此处判断加载的URL，当加载空URL完成时将Web组件设置回onInactive状态
        if (event.url == 'about:blank') {
          this.webviewController.onInactive();
        }
      })
      .geolocationAccess(false)
      .fileAccess(true)
      .domStorageAccess(true);
  }
}

@Component
export struct TabTwo {
  @StorageProp('userInfo') userInfo: string = '';
  @StorageProp('isLogged') isLogged: boolean = false;
  promptAction: PromptAction = this.getUIContext().getPromptAction();

  build() {
    Column({ space: 20 }) {

      Text(`当前登录状态：${this.isLogged ? '已登录' : '未登录'}`);
      Text(`当前用户：${this.userInfo}`);

      // 模拟用户登录退出操作
      Button('登录用户1 网页1')
        .onClick(() => {
          AppStorage.setOrCreate('isLogged', true);
          AppStorage.setOrCreate('userInfo', '1');
          emitter.emit('loadUrl');
          this.promptAction.showToast({
            message: '用户1  登录成功'
          });
        });
      Button('登录用户2 网页2')
        .onClick(() => {
          AppStorage.setOrCreate('isLogged', true);
          AppStorage.setOrCreate('userInfo', '2');
          emitter.emit('loadUrl');
          this.promptAction.showToast({
            message: '用户2  登录成功'
          });
        });
      Button('退出登录')
        .onClick(() => {
          AppStorage.setOrCreate('isLogged', false);
          AppStorage.setOrCreate('userInfo', '');
          this.promptAction.showToast({
            message: '退出登录成功'
          });
        });
    };
  }
}
```

**说明** 

访问在线网页时需添加网络权限：[ohos.permission.INTERNET](../harmonyos-guides/permissions-for-all.md#ohospermissioninternet)，具体申请方式请参考[声明权限](../harmonyos-guides/declare-permissions.md)。
