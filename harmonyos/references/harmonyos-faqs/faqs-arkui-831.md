---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-831
title: 应用协议弹窗侧滑后关闭导致无法进入应用
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 应用协议弹窗侧滑后关闭导致无法进入应用
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:04+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:98f542eeaee2ec435895b568c121eab2df9a5589ffdcda0fc26f0e391bce9441
---

## 问题现象

应用在首次启动后，通过自定义弹窗实现用户隐私协议授权页面，侧滑返回时弹窗直接消失，导致应用无法正常进入主页面，不符合预期。

## 背景知识

* [Navigation](../harmonyos-references/ts-basic-components-navigation.md)：路由导航的根视图容器，作为page页面的根容器使用，默认包含标题栏、内容区和工具栏。
* [NavDestination](../harmonyos-references/ts-basic-components-navdestination.md)：作为子页面的根容器，用于显示Navigation的内容区。
* [NavDestinationMode](../harmonyos-references/ts-basic-components-navdestination.md#navdestinationmode枚举说明11)：NavDestination类型，包含自定义dialog模式。
* [onBackPressed](../harmonyos-references/ts-basic-components-navdestination.md#onbackpressed10)：当点击返回键或侧滑时，触发该回调。返回值为true时，表示重写返回键逻辑，返回值为false时，表示回退到上一个页面。

## 问题定位

复现问题，抓取Hilog日志，查看进程相关日志进行业务逻辑排查。

1. 自定义弹窗创建。如下日志，进入主界面page后，基于NavDestination创建dialog并显示。焦点由page切换到dialog也可说明当前弹窗逻辑。

   ```shell
   07-08 10:45:20.852   29801-29801   C0390F/应用包名/AceDialog      应用包名         I     [(100000:100000:scope)] dialog GetContext fontScale : 1.000000
   07-08 10:45:20.852   29801-29801   C03922/应用包名/AceNavigation  应用包名         I     [(100000:100000:scope)] fire dialog change to cause navdestination lifecycle: 6
   07-08 10:45:20.852   29801-29801   C03900/应用包名/Ace            应用包名         I     [(100000:100000:scope)] Put node level order. nodeId: 17, levelOrder: 0.000000
   07-08 10:45:20.852   29801-29801   C0390F/应用包名/AceDialog      应用包名         I     [(100000:100000:scope)] Controller/0 create dialog node/17 successfully.
   07-08 10:45:21.022   29801-29801   C0391C/应用包名/AceFocus       应用包名         I     [(100000:100000:scope)] FocusView: Dialog/17 show
   07-08 10:45:21.022   29801-29801   C0391C/应用包名/AceFocus       应用包名         I     [(100000:100000:scope)] FocusView: page/2 lost focus
   07-08 10:45:21.028   29801-29801   C0391C/应用包名/AceFocus       应用包名         I     [(100000:100000:scope)] Request focus on focusView: Dialog/17.
   ```
2. 侧滑返回后弹窗消失。日志显示侧滑返回后触发NavDestination的onBackPressed回调，之后dialog正常关闭，且页面焦点由dialog切换到page。

   ```shell
   07-08 10:54:53.122   29801-31911   C03900/应用包名/Ace            应用包名         I     [(-1:100000:singleton)] [应用包名][entry][100000]: OnBackPressed called
   07-08 10:54:53.124   29801-29801   C03900/应用包名/Ace            应用包名         I     [(100000:100000:scope)] Pop node level order. nodeId: 17, levelOrder: 0.000000
   07-08 10:54:53.124   29801-29801   C0390D/应用包名/AceOverlay     应用包名         I     [(100000:100000:scope)] close dialog animation
   07-08 10:54:53.124   29801-29801   C0390D/应用包名/AceOverlay     应用包名         W     [(100000:100000:scope)] not find mask dialog 17 in maskNodeIdMap
   07-08 10:54:53.124   29801-29801   C03922/应用包名/AceNavigation  应用包名         I     [(100000:100000:scope)] fire dialog change to cause navdestination lifecycle: 4
   07-08 10:54:53.125   29801-29801   C03900/应用包名/Ace            应用包名         I     [(100000:100000:scope)] Overlay consumed backpressed event
   07-08 10:54:53.357   29801-29801   C0390F/应用包名/AceDialog      应用包名         I     [(100000:100000:scope)] post dialog finish event enter
   07-08 10:54:53.358   29801-29801   C0390F/应用包名/AceDialog      应用包名         I     [(100000:100000:scope)] on dialog/17 close event enter
   07-08 10:54:53.358   29801-29801   C0391C/应用包名/AceFocus       应用包名         I     [(100000:100000:scope)] Focus view: Dialog/17 close
   07-08 10:54:53.358   29801-29801   C0391C/应用包名/AceFocus       应用包名         I     [(100000:100000:scope)] FocusView: Dialog/17 lost focus
   07-08 10:54:53.365   29801-29801   C0391C/应用包名/AceFocus       应用包名         I     [(100000:100000:scope)] Request focus on focusView: page/2.
   ```

## 分析结论

应用通过NavDestination的dialog模式创建协议弹窗，在页面侧滑时触发NavDestination的onBackPressed回调，由于onBackPressed返回false未进行拦截，弹窗dialog正常退出回到主页面。

## 修改建议

由于应用是基于Navigation自定义弹窗实现，使用NavDestination的回调函数onBackPressed，当点击物理返回按钮或使用手势滑动时，触发该回调。而当onBackPressed返回值为true时，表示重写返回键逻辑，即可实现拦截，示例如下。

主页面：

```ts
@Entry
@Component
export struct DialogDemo {
  @Provide('NavPathStack') pageStack: NavPathStack = new NavPathStack();

  build() {
    Navigation(this.pageStack) {
      Column() {
        Row() {
          Button('打开弹窗')
            .width('100%')
            .onClick(() => {
              this.pageStack.pushPathByName('SubDialog', null);
            })
        }
        .width('100%')
        .alignItems(VerticalAlign.Center)
        .padding({ left: 16, right: 16 })
      }
      .width('100%')
      .height('100%')
      .justifyContent(FlexAlign.End)
    }
    .hideToolBar(true)
  }
}
```

弹窗页面：

```ts
@Builder
export function myRouter() {
  SubDialog();
}

@Component
export struct SubDialog {
  @Consume('NavPathStack') pageStack: NavPathStack;

  build() {
    NavDestination() {
      Stack({ alignContent: Alignment.Center }) {
        Column() {
          Row() {
            Text('隐私协议')
              .fontSize(20)
              .fontWeight(FontWeight.Bold)
          }
          .justifyContent(FlexAlign.Center)
          .padding({ top: 20 })
          Text('协议协议内容...')
            .fontSize(14)
            .padding({ top: 10 })
            .width('80%')
          Row() {
            Button('取消')
              .backgroundColor(Color.White)
              .fontColor('rgb(65, 105, 225)')
              .fontSize(16)
              .onClick(() => {
                this.pageStack.pop();
              })
            Divider()
              .vertical(true)
              .height(22)
              .color('#E5E5EA')
              .opacity(0.6)
              .margin({ left: 8, right: 8 })
            Button('确认')
              .backgroundColor(Color.White)
              .fontColor('rgb(65, 105, 225)')
              .fontSize(16)
              .onClick(() => {
                this.pageStack.pop();
              })
          }
          .justifyContent(FlexAlign.SpaceAround)
          .padding({ top: 60 })
          .width('80%')
        }
        .width('90%')
        .height('25%')
        .borderRadius(30)
        .backgroundColor(Color.White)
      }
      .height('100%')
      .width('100%')
    }
    .hideTitleBar(true)
    .backgroundColor('rgba(0, 0, 0, 0.3)')
    .mode(NavDestinationMode.DIALOG)
    .onBackPressed(() => { // 拦截侧滑返回
      // 阻止默认行为
      return true;
    })
  }
}
```

[route\_map.json配置如下](../harmonyos-guides/arkts-navigation-cross-package.md#系统路由表)：

```ts
{
  "routerMap": [
    {
      "name": "SubDialog",
      "pageSourceFile": "src/main/ets/pages/SubDialog.ets",
      "buildFunction": "myRouter",
      "data": {
        "description": "this is SubDialog.ets"
      }
    }
  ]
}
```
