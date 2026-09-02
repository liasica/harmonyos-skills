---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkweb-155
title: 如何实现系统状态栏颜色随H5改变
breadcrumb: FAQ > 应用框架开发 > Web框架 > Web开发（ArkWeb） > 如何实现系统状态栏颜色随H5改变
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:33+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:bd99dc63718daf5296125d09d1206bfa4562d60cd99700ecd1d8289f4e3bb8c2
---

## 问题现象

Web组件加载部分H5页面时需要改变系统状态栏颜色，且一直持续到Web组件所在页面销毁为止，应如何实现？例如，有三个H5页面A、B、C，要求如下：

* Web组件加载A页面后系统状态栏背景色和内容色应分别变为蓝色（#0A59F7）、灰色（#999999）。
* Web组件加载C页面后系统状态栏背景色和内容色应分别变为绿色（#407B2A）、黑色（#000000）。
* Web组件加载B页面后延续上一个页面的系统状态栏颜色。
* 当从Web所在页面跳转到其他页面时，恢复系统状态栏默认颜色。

## 背景知识

* [setWindowSystemBarProperties](../harmonyos-references/arkts-apis-window-window.md#setwindowsystembarproperties9)：设置主窗口状态栏的属性，使用Promise异步回调。
* [getWindowSystemBarProperties](../harmonyos-references/arkts-apis-window-window.md#getwindowsystembarproperties12)：主窗口获取状态栏的属性。
* [javaScriptProxy](../harmonyos-references/arkts-basic-components-web-attributes.md#javascriptproxy)：将javaScriptProxy中的ArkTS对象注册到Web组件中，该对象将使用[JavaScriptProxy](../harmonyos-references/arkts-basic-components-web-i.md#javascriptproxy12)中指定的名称注册到网页的所有框架中，包括所有iframe，这使得JavaScript可以调用JavaScriptProxy中ArkTS对象的方法。
* [Navigation](../harmonyos-references/ts-basic-components-navigation.md)：Navigation组件是路由导航的根视图容器，一般作为Page页面的根容器使用，其内部默认包含了标题栏、内容区和工具栏，其中内容区默认首页显示导航内容（Navigation的子组件）或非首页显示（NavDestination的子组件），首页和非首页通过路由进行切换。
* [NavDestination](../harmonyos-references/ts-basic-components-navdestination.md)：作为子页面的根容器，用于显示Navigation的内容区。

## 解决方案

要实现该效果，可在H5中调用JSBridge方法改变系统状态栏颜色、在Web组件所在页面的对应页面隐藏的生命周期中恢复系统状态栏颜色。具体步骤及示例代码如下：

1. 首先，基于setWindowSystemBarProperties定义一个设置系统状态栏颜色的方法setStatusBarColor()，参数分别为系统状态栏背景色值、文字色值；基于getWindowSystemBarProperties定义一个获取当前系统状态栏属性的方法getStatusBarColor()。
2. 用JavaScriptProxy将setStatusBarColor()方法注入到H5，在需要改变系统状态栏颜色的H5中调用该方法，参数传入对应的颜色值，调用时机越早越好。
3. 为避免影响非H5页面，需要离开Web组件所在页面时调用setStatusBarColor()方法恢复默认系统状态栏颜色（背景色值'#66000000'，文字色值'#E5FFFFFF'）或应用所设置的系统状态栏颜色，对应的生命周期回调函数为NavDestination的[onWillHide](../harmonyos-references/ts-basic-components-navdestination.md#onwillhide12)。
4. 当返回Web所在页面时，需要恢复离开该页面时的系统状态栏颜色设置。在Web所在页面中声明一个私有变量h5SystemBarProperty（初始值设为空对象{}）来保存该设置，在离开该页面时（对应回调为NavDestination的onWillHide）调用getStatusBarColor()方法获取当前系统状态栏属性并赋值给h5SystemBarProperty变量。在NavDestination的[onWillShow](../harmonyos-references/ts-basic-components-navdestination.md#onwillshow12)回调中，调用setStatusBarColor()方法，传入h5SystemBarProperty对象中系统状态栏背景颜色及文字颜色属性值。当该页面销毁时，h5SystemBarProperty变量被重置。

完整示例参考如下：

```screen
// Index.ets
@Entry
@Component
struct Index {
  pageStack: NavPathStack = new NavPathStack();

  build() {
    Navigation(this.pageStack) {
      Column() {
        Button('点击跳转WebA')
          .width('50%')
          .margin({
            top: 100
          })
          .onClick(() => {
            this.pageStack.pushPath({ name: 'H5Page', param: $rawfile('WebA.html') });
          })
      }
      .height('100%')
      .width('100%')
    }
    .mode(NavigationMode.Auto)
  }
}
```

```screen
// H5Page.ets
import { webview } from '@kit.ArkWeb';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

@Builder
export function PageOneBuilder(name: string, param: Object) {
  H5Page()
}

// 设置状态栏的背景颜色及文字颜色
async function setStatusBarColor(ctx: common.BaseContext, bg: string = '#66000000', content: string = '#E5FFFFFF') {
  const windowClass: window.Window | undefined = await window.getLastWindow(ctx).catch(() => undefined);
  if (!windowClass) {
    return;
  }
  try {
    windowClass.setWindowSystemBarProperties({
      statusBarColor: bg,
      statusBarContentColor: content
    }).then(() => {
      console.info(`Succeeded in setting the system bar properties. Background color: ${bg}, Content color: ${content}`);
    })
      .catch((err: BusinessError) => {
        console.error(`Failed to set the system bar properties. Cause code: ${err.code}, message: ${err.message}`);
      });
  } catch (exception) {
    console.error(`Failed to set the system bar properties. Cause code: ${exception.code}, message: ${exception.message}`);
  }
}

// 获取状态栏属性
async function getStatusBarColor(ctx: common.BaseContext): Promise<window.SystemBarProperties> {
  let result: window.SystemBarProperties = {};
  const windowClass: window.Window | undefined = await window.getLastWindow(ctx).catch(() => undefined);
  if (!windowClass) {
    return result;
  }
  try {
    result = windowClass.getWindowSystemBarProperties();
    console.info('Success in obtaining system bar properties. Property: ' + JSON.stringify(result));
  } catch (err) {
    console.error(`Failed to get system bar properties. Code: ${err.code}, message: ${err.message}`);
  }
  return result;
}

class Bridge {
  context: common.Context;

  constructor(ctx: common.Context) {
    this.context = ctx;
  }

  changeStatusBarColor(bg: string, content: string) {
    setStatusBarColor(this.context, bg, content);
  }
}

@Entry
@Component
struct H5Page {
  context: common.Context = this.getUIContext().getHostContext()!;
  pageStack: NavPathStack = new NavPathStack();
  @State url: ResourceStr = $rawfile('WebA.html');
  controller: webview.WebviewController = new webview.WebviewController();
  // H5设置的系统状态栏属性
  h5SystemBarProperty: window.SystemBarProperties = {};

  build() {
    NavDestination() {
      Button('点击跳转OtherPage')
        .width('50%')
        .onClick(() => {
          this.pageStack.pushPath({ name: 'OtherPage' });
        })
      Web({
        src: this.url,
        controller: this.controller
      })
        .javaScriptProxy({
          name: 'abc',
          object: new Bridge(this.context),
          methodList: ['changeStatusBarColor'],
          controller: this.controller
        })
    }
    .onReady((ctx: NavDestinationContext) => {
      this.pageStack = ctx.pathStack;
      this.url = this.pageStack.getParamByName('H5Page')[0] as ResourceStr;
    })
    .onWillShow(() => {
      // 如果H5设置过系统状态栏颜色，当前页面显示之前恢复该设置
      if (this.h5SystemBarProperty.statusBarColor) {
        setStatusBarColor(this.context, this.h5SystemBarProperty.statusBarColor,
          this.h5SystemBarProperty.statusBarContentColor)
      }
    })
    .onWillHide(() => {
      // 离开该页面时获取系统状态栏属性，赋值给h5SystemBarProperty变量
      getStatusBarColor(this.context).then(res => {
        this.h5SystemBarProperty = res;
      })
      // 恢复系统状态栏颜色设置
      setStatusBarColor(this.context)
    })
  }
}
```

```screen
// OtherPage
@Builder
export function OtherPageBuilder(name: string, param: Object) {
  OtherPage()
}

@Entry
@Component
struct OtherPage {
  @State message: string = 'Hello World';

  build() {
    NavDestination() {
      RelativeContainer() {
        Text(this.message)
          .id('OtherPageHelloWorld')
          .fontSize($r('app.float.page_text_font_size'))
          .fontWeight(FontWeight.Bold)
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
          .onClick(() => {
            this.message = 'Welcome';
          })
      }
      .height('100%')
      .width('100%')
    }
  }
}
```

```screen
<!--WebA.html-->
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no" />
    <title>H1</title>
    <style>
      button {
        width: 200px;
        height: 60px;
        font-size: 20px;
      }
    </style>
    <script>
      if (window.abc) {
        window.abc.changeStatusBarColor("#0A59F7", "#999999");
      }
      function navToH2() {
        location.href = "resource://rawfile/WebB.html";
      }
      function navToH3() {
        location.href = "resource://rawfile/WebC.html";
      }
    </script>
  </head>
  <body>
    <h1>this is WebA Page</h1>
    <button onclick="navToH2()">跳转B页面</button>
    <button onclick="navToH3()">跳转C页面</button>
  </body>
</html>
```

```screen
<!--WebB.html-->
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no" />
    <title>H1</title>
    <style>
      button {
        width: 200px;
        height: 60px;
        font-size: 20px;
      }
    </style>
    <script>
      function navTo() {
        location.href = "resource://rawfile/WebC.html";
      }
      function navBack() {
        history.back();
      }
    </script>
  </head>
  <body>
    <h1>this is WebB Page</h1>
    <button onclick="navBack()">返回上个页面</button>
    <button onclick="navTo()">跳转C页面</button>
  </body>
</html>
```

```screen
<!--WebC.html-->
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no" />
    <title>H1</title>
    <style>
      button {
        width: 200px;
        height: 60px;
        font-size: 20px;
      }
    </style>
    <script>
      if (window.abc) {
        window.abc.changeStatusBarColor("#407B2A", "#000000");
      }
      function navBack() {
        history.back();
      }
    </script>
  </head>
  <body>
    <h1>this is WebC Page</h1>
    <button onclick="navBack()">返回上个页面</button>
  </body>
</html>
```

```screen
// route_map.json
{
  "routerMap": [
    {
      "name": "H5Page",
      "pageSourceFile": "src/main/ets/pages/H5Page.ets",
      "buildFunction": "PageOneBuilder",
      "data": {
        "description": "this is pageOne"
      }
    },
    {
      "name": "OtherPage",
      "pageSourceFile": "src/main/ets/pages/OtherPage.ets",
      "buildFunction": "OtherPageBuilder",
      "data": {
        "description": "this is otherPage"
      }
    }
  ]
}
```

```screen
// module.json5
{
  "module": {
    "name": "entry",
    "type": "entry",
    "description": "$string:module_desc",
    "mainElement": "EntryAbility",
    "pages": "$profile:main_pages",
    "routerMap": "$profile:route_map",
    // ...
  }
}
```

## 常见FAQ

Q：如果应用针对不同非H5页面设置了不同的系统状态栏颜色，且都有可能跳转H5页面，如何实现离开H5页面后恢复跳转前的页面所设置的系统状态栏颜色？

A：在Web组件所在页面的[aboutToAppear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttoappear)生命周期中调用getWindowSystemBarProperties获取到当前主窗口系统状态栏颜色作为默认颜色设置，并声明一个私有变量appSystemBarProperty来保存该设置，在该页面NavDestination的onWillHide回调中调用setStatusBarColor()方法恢复跳转前页面的系统状态栏颜色设置。

```screen
// H5Page.ets
// ...
@Entry
@Component
struct H5Page {
  // ...
  // 应用设置的系统状态栏属性
  appSystemBarProperty: window.SystemBarProperties = {};

  aboutToAppear(): void {
    getStatusBarColor().then(res => {
      // 组件创建时获取系统状态栏属性，赋值给appSystemBarProperty变量
      this.appSystemBarProperty = res;
    })
  }

  build() {
    NavDestination() {
      // ...
      Web({
        src: this.url,
        controller: this.controller
      })
      // ...
    }
    // ...
    .onWillHide(() => {
      // ...
      // 恢复应用的系统状态栏颜色设置
      setStatusBarColor(this.appSystemBarProperty.statusBarColor, this.appSystemBarProperty.statusBarContentColor)
    })
  }
}
```

Q：如果应用未使用Navigation导航方案，应该如何调整代码？

A：NavDestination的onWillShow、onWillHide回调分别对标页面的[onPageShow](../harmonyos-references/ts-custom-component-lifecycle.md#onpageshow)、[onPageHide](../harmonyos-references/ts-custom-component-lifecycle.md#onpagehide)回调，在对应的回调中执行相应代码即可。

Q：如果系统状态栏样式设置需要以单个H5页面为基本维度，而不是以Web组件为维度，即某个H5对系统状态栏样式设置仅对该H5生效、同Web内跳转到其他H5时需要恢复默认设置，如何实现？

A：在H5发生跳转时会触发Web组件的[onNavigationEntryCommitted](../harmonyos-references/arkts-basic-components-web-events.md#onnavigationentrycommitted11)生命周期，在该函数中调用setStatusBarColor()方法恢复默认系统状态栏颜色设置。

Q：若想要Web组件所在页面销毁后重进时，系统状态栏颜色还能保持和上次一致，应如何调整代码？

A：使用[AppStorage](../harmonyos-guides/arkts-appstorage.md)全局存储该状态，即在存储Web组件所在页面的系统状态栏属性的私有变量h5SystemBarProperty前加上[@StorageLink](../harmonyos-guides/arkts-appstorage.md#storagelink)装饰器。另外，若需要该状态不随应用进程的重启而重置，则需使用[PersistentStorage](../harmonyos-guides/arkts-persiststorage.md)持久化存储该AppStorage变量。
