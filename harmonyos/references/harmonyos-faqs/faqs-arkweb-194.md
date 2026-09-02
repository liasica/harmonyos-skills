---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-194
title: 如何实现Web组件在折叠屏上分栏展示
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 如何实现Web组件在折叠屏上分栏展示
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:34+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0d85b1848fbda22d9714168a406be1a3152081b2866ca34cd327db7a62516799
---

## 问题现象

当整个页面为Web组件加载H5页面时，折叠屏有时需要分栏展示不同页面内容，如何实现Web组件加载的页面在折叠屏上分栏展示？

## 背景知识

[ArkWeb（方舟Web）](../harmonyos-guides/web-component-overview.md)：提供了Web组件，用于在应用程序中显示Web页面内容。

常见使用场景包括：

* 应用集成Web页面：应用可以在页面中使用Web组件，嵌入Web页面内容，以降低开发成本，提升开发、运营效率。
* 浏览器网页浏览场景：浏览器类应用可以使用Web组件，打开三方网页，使用无痕模式浏览Web页面，设置广告拦截等。
* 小程序：小程序类宿主应用可以使用Web组件，渲染小程序的页面，实现同层渲染，视频托管等小程序的功能。

[分栏布局](../best-practices/bpta-multi-device-page-layout.md#section11897247142110)：分栏布局是指在空间充足时，将窗口划分为两栏或三栏，用于展示多类内容。常见的分栏布局包括侧边栏、单/双栏和三分栏。

[Navigation](../harmonyos-references/ts-basic-components-navigation.md)：Navigation组件是路由导航的根视图容器，一般作为Page页面的根容器使用，其内部默认包含了标题栏、内容区和工具栏，其中内容区默认首页显示导航内容（Navigation的子组件）或非首页显示（NavDestination的子组件），首页和非首页通过路由进行切换。

[断点](../best-practices/bpta-multi-device-responsive-layout.md#section1532120147301)：响应式布局中最常使用的特征是窗口宽度及窗口高宽比，可以将窗口宽度及窗口高宽比划分为不同的范围，称之为“断点”。当窗口宽度及窗口高宽比从一个断点变化到另一个断点时，改变页面布局（如将页面内容从单列排布调整为双列排布甚至三列排布等）以获得更好的显示效果。

## 解决方案

1. 实现Web组件折叠屏分栏，需了解分栏的原理，如下为单双栏实现原理：单双栏通常是使用Navigation实现的，Navigation是路由容器组件，一般作为首页的根容器，包括单栏（Stack）、分栏（Split）和自适应（Auto）三种显示模式。通过更改Navigation组件的mode值来实现单栏和双栏的切换。可以通过设置断点来自定义导航栏的显示模式。例如：当断点为sm时，将mode值设置为Stack；当断点不为sm时，将mode值设置为Split。这样可以实现单栏和双栏的自适应切换。
2. 通过设置Web组件onLoadIntercept事件，实现在Web组件加载url之前拦截并获取到该url。如果获取后的url既不是初始加载的url，也不是当前分栏第二屏加载的url，则在分栏第二屏加载该url，展示新页面。

示例代码如下：

EntryAbility.ets：

```ts
import { ConfigurationConstant, UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { display, window } from '@kit.ArkUI';
import { Constants } from '../constant/Constants';
import { BreakpointConstants } from '../constant/BreakpointConstants';

const DOMAIN = 0x0000;

export default class EntryAbility extends UIAbility {
  onCreate(): void {
    this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    windowStage.getMainWindow().then((windowObj) => {
      // 获取应用启动时的窗口尺寸
      this.updateBreakpoint(windowObj.getWindowProperties().windowRect.width,
        windowObj.getWindowProperties().windowRect.height);
      // 注册回调函数，监听窗口尺寸变化
      windowObj.on('windowSizeChange', (windowSize) => {
        this.updateBreakpoint(windowSize.width, windowSize.height);
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

  /**
   * 根据当前窗口尺寸更新断点
   * @param windowWidth
   * @param windowHeight
   */
  private updateBreakpoint(windowWidth: number, windowHeight: number): void {
    AppStorage.setOrCreate(Constants.windowWidth, windowWidth);
    AppStorage.setOrCreate(Constants.windowHeight, windowHeight);
    // 将长度的单位由px换算为vp
    let windowWidthVp = windowWidth / display.getDefaultDisplaySync().densityPixels;
    let newBp: string = '';
    if (windowWidthVp < 320) {
      newBp = BreakpointConstants.BREAKPOINT_XS;
    } else if (windowWidthVp < 600) {
      newBp = BreakpointConstants.BREAKPOINT_SM;
    } else if (windowWidthVp < 840) {
      newBp = BreakpointConstants.BREAKPOINT_MD;
    } else {
      newBp = BreakpointConstants.BREAKPOINT_LG;
    }
    // 使用状态变量记录当前断点值，使用方法:在组件添加@StorageProp(Constant.currentBreakpoint)curBp:string='md';
    AppStorage.setOrCreate(Constants.currentBreakpoint, newBp);
  }
};
```

Index.ets：

```ts
import { webview } from '@kit.ArkWeb';
import { BreakpointConstants } from '../constant/BreakpointConstants';
import { Constants } from '../constant/Constants';
import { SplitWeb } from './SplitWeb';

@Entry
@Component
struct Index {
  // 代码中url链接使用时更换为实际链接
  url = 'xxx.xxx.xxx';
  @Provide('lastPage') lastPage: string = '';
  controller: webview.WebviewController = new webview.WebviewController();
  @Provide('pageInfos') pageInfos: NavPathStack = new NavPathStack();
  @StorageProp(Constants.currentBreakpoint) currentBreakpoint: string = 'md';

  build() {
    Column() {
      Navigation(this.pageInfos) {
        Web({ src: this.url, controller: this.controller })
          .width('100%')
          .fileAccess(false)
          .geolocationAccess(false)
          .onLoadIntercept((event) => {
            let requestUrl = event.data.getRequestUrl();
            if (requestUrl !== this.url) {
              if (this.lastPage !== requestUrl) {
                if (this.pageInfos.getAllPathName().length > 0) {
                  this.pageInfos.replacePath({ name: 'webPageOne', param: requestUrl });
                } else {
                  this.pageInfos.pushPath({ name: 'webPageOne', param: requestUrl });
                }
                this.lastPage = requestUrl;
              }
              return true;
            }
            return false;
          })
          .onOverrideUrlLoading(() => {
            return false;
          });
      }
      .navDestination(this.PageMap)
      .hideTitleBar(true)
      .hideBackButton(true)
      .titleMode(NavigationTitleMode.Mini)
      .mode(new BreakpointConstants<NavigationMode>({
        sm: NavigationMode.Stack,
        md: NavigationMode.Split,
        lg: NavigationMode.Split
      }).getValue(this.currentBreakpoint))
      .height('100%')
      .width('100%')
      .navBarWidth(this.pageInfos.getAllPathName().length > 0 ? '50%' : '100%')
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM, SafeAreaEdge.TOP]);
    };
  }

  @Builder
  PageMap(name: string, param: string) {
    if (name == 'webPageOne') {
      SplitWeb({ url: param });
    }
  }
}
```

SplitWeb.ets：

```ts
import { webview } from '@kit.ArkWeb';

/**
 * web分屏页面
 */
@Component
export struct SplitWeb {
  @Consume('pageInfos') pageInfos: NavPathStack;
  @Consume('lastPage') lastPage: string;
  url = '';
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    NavDestination() {
      Column() {
        Web({ src: this.url, controller: this.controller })
          .javaScriptAccess(true)
          .domStorageAccess(true)
          .fileAccess(false)
          .geolocationAccess(false)
          .databaseAccess(true);
      }.width('100%').height('100%');
    }
    .hideTitleBar(true)
    .onBackPressed(() => {
      if (this.controller.accessBackward()) { // 判断web页面是否可以后退
        this.controller.backward(); // web页面后退
        return true;
      } else {
        this.pageInfos.pop(); // 弹出路由栈栈顶元素
        if (this.pageInfos.getAllPathName().length === 0) {
          this.lastPage = '';
        }
        return true;
      }
    });
  }
}
```

Constants.ets：

```ts
export class Constants {
  static readonly currentBreakpoint = 'currentBreakpoint';
  static readonly windowWidth = 'windowWidth';
  static readonly windowHeight = 'windowHeight';
}
```

BreakpointConstants.ets：

```ts
export class BreakpointConstants<T> {
  static readonly BREAKPOINT_XS: string = 'xs';
  static readonly BREAKPOINT_SM: string = 'sm';
  static readonly BREAKPOINT_MD: string = 'md';
  static readonly BREAKPOINT_LG: string = 'lg';
  static readonly GRID_ROW_COLUMNS: number[] = [12, 15, 4];
  static readonly GRID_COLUMN_SPANS: number[] = [12, 6, 7, 5, 3, 4, 2];
  static readonly BREAKPOINT_WIDTH_RANGES: number[] = [320, 600, 840];
  sm: T;
  md: T;
  lg: T;

  constructor(param: BreakpointTypes<T>) {
    this.sm = param.sm;
    this.md = param.md;
    this.lg = param.lg;
  }

  getValue(currentBreakpoint: string): T {
    if (currentBreakpoint === BreakpointConstants.BREAKPOINT_SM) {
      return this.sm;
    }
    if (currentBreakpoint === BreakpointConstants.BREAKPOINT_MD) {
      return this.md;
    }
    return this.lg;
  }
}

export interface BreakpointTypes<T> {
  sm: T;
  md: T;
  lg: T;
}
```
