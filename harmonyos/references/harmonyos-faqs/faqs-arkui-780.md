---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-780
title: 自定义router到Navigation中NavDestination子页面的转场动画
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 自定义router到Navigation中NavDestination子页面的转场动画
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:23+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:49c2dd229da0860f0db794e6a4d07b3f85e1ca40e852d33aea55e76f3b8d11f4
---

## 问题现象

在项目中同时使用Router和Navigation时，如何实现从Router页面跳转到Navigation子界面NavDestination的特殊页面转场效果？

## 背景知识

* [Router](../harmonyos-references/arkts-apis-uicontext-router.md)跳转页面通过在pageTransition函数中定义[PageTransitionEnter](../harmonyos-references/ts-page-transition-animation.md#pagetransitionenter)和[PageTransitionExit](../harmonyos-references/ts-page-transition-animation.md#pagetransitionexit)参数，可实现自定义页面转场动画。
* [Navigation](../harmonyos-references/ts-basic-components-navigation.md)的导航控制器[NavPathStack](../harmonyos-references/ts-basic-components-navigation.md#navpathstack10)提供的push、pop、replace等接口支持通过设置[NavigationOptions](../harmonyos-references/ts-basic-components-navigation.md#navigationoptions12)的animated参数控制动画开关（默认值为true启用转场动画），若单次操作设为false可临时关闭动画，后续操作仍会恢复默认动画效果。
* [transition](../harmonyos-references/ts-transition-animation-component.md)接口用于设置组件级过渡参数，当组件[visibility](../harmonyos-references/ts-universal-attributes-visibility.md)属性在可见和不可见之间改变时，触发该组件的transition效果。

## 解决方案

转场动画由关闭页面的退场动画和目标页面的进场动画构成。由于Router的页面级路由跳转与Navigation组件的容器级导航属于不同层级的导航机制，混合使用可能导致动画效果不符合预期。

推荐解决方案：

1. 关闭跨层级动画：
   * 在Router跳转时设置pageTransition函数，关闭转场动画。
   * 在Navigation组件跳转时禁用默认动效，设置animated为false。
2. 配置组件级过渡：
   * 使用transition接口定义组件显隐动效。
   * 通过visibility属性控制组件可见性触发动画。

完整代码如下：

```ts
// 使用router跳转到NavigationPage页面
@Entry
@Component
struct RouterPage {
  @State visibilityState: Visibility = Visibility.Hidden;
  private duration: number = 1000;

  // 关闭router转场动画
  pageTransition() {
    PageTransitionEnter({ type: RouteType.None, duration: 0 });
    PageTransitionExit({ type: RouteType.None, duration: 0 });
  }

  onPageShow(): void {
    this.visibilityState = Visibility.Visible; // 触发入场动画
  }

  build() {
    Column() {
      Text('Router跳转')
        .fontSize(30)
        .fontWeight(FontWeight.Bold)
        .onClick(() => {
          this.visibilityState = Visibility.Hidden; // 触发出场动画
          // 等待转场动画消失后跳转
          setTimeout(() => {
            // 携带页面名称参数，用于Navigation跳转
            this.getUIContext()
              .getRouter()
              .pushUrl({ url: 'pages/NavigationPage', params: { pageName: 'TargetInterfacePage' } });
          }, this.duration);
        });
    }.width('100%').height('100%')
    .justifyContent(FlexAlign.Center)
    .transition(TransitionEffect.OPACITY.animation({ duration: this.duration, curve: Curve.Linear }).combine(
      TransitionEffect.rotate({ z: 1, angle: 180 })
    ))
    .visibility(this.visibilityState);
  }
}
```

```ts
// 使用NavPathStack跳转到TargetInterfacePage页面
interface PageParams {
  pageName: string;
}

@Entry
@Component
struct NavigationPage {
  @State pathStack: NavPathStack = new NavPathStack();

  // 关闭router转场动画
  pageTransition() {
    PageTransitionEnter({ type: RouteType.None, duration: 0 });
    PageTransitionExit({ type: RouteType.None, duration: 0 });
  }

  aboutToAppear(): void {
    // 接收pageName参数并跳转
    const params = this.getUIContext().getRouter().getParams() as PageParams;
    if (params && params.pageName) {
      this.pathStack.pushPath({ name: params.pageName }, false); // 关闭Navigation转场动画
    }
  }

  build() {
    Navigation(this.pathStack) {
    }.title('Navigation首页');
  }
}
```

```ts
// 使用Navigation管理的NavDestination子界面，是跳转的目标界面
const TAG = '目标界面';

@Builder
export function targetInterfacePageBuilder() {
  TargetInterfacePage();
}

@Component
struct TargetInterfacePage {
  pathStack: NavPathStack | undefined = undefined;
  @State visibilityState: Visibility = Visibility.Hidden;
  private duration: number = 1000;

  build() {
    NavDestination() {
    }
    .title(`NavDestination${TAG}`)
    .transition(TransitionEffect.OPACITY.animation({ duration: this.duration, curve: Curve.Linear }))
    .visibility(this.visibilityState)
    .onReady((context: NavDestinationContext) => {
      this.pathStack = context.pathStack;
    })
    .onShown(() => {
      this.visibilityState = Visibility.Visible; // 触发入场动画
    })
    .onBackPressed(() => {
      this.visibilityState = Visibility.Hidden; // 触发出场动画
      // 等待转场动画消失后跳转
      setTimeout(() => {
        this.pathStack?.pop(false);
      }, this.duration);
      return true;
    });
  }
}
```

还需在module.json5和route\_map.json文件添加路由表配置，详细参考：[系统路由表](../harmonyos-guides/arkts-navigation-cross-package.md#系统路由表)。

```json
{
  "routerMap": [
    {
      "name": "TargetInterfacePage",
      "pageSourceFile": "src/main/ets/pages/TargetInterfacePage.ets",
      "buildFunction": "targetInterfacePageBuilder"
    }
  ]
}
```
