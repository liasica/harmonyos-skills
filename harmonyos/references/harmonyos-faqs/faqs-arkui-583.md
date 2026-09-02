---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-583
title: 页面跳转后bindSheet不消失于原页面
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 页面跳转后bindSheet不消失于原页面
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:01+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7d8734a9ef0b64e90e268aa869bf081937175f1f67c0263ac871f132d736c12a
---

## 问题现象

在A页面打开bindSheet后跳转其他页面，希望返回A页面时bindSheet仍是打开状态。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/exZm3qYCQmyKccojDZJrMQ/zh-cn_image_0000002658791767.gif "点击放大")

## 背景知识

* [bindSheet](../harmonyos-references/ts-universal-attributes-sheet-transition.md#bindsheet)为组件绑定半模态页面。
* [Navigation](../harmonyos-references/ts-basic-components-navigation.md)用于页面间的路由导航组件，作为页面的根容器使用，[NavDestination](../harmonyos-references/ts-basic-components-navdestination.md)作为Navigation目的页面的根节点。
* [pushPathByName](../harmonyos-references/ts-basic-components-navigation.md#pushpathbyname11)用于跳转指定的NavDestination页面，同时可以使用onPop回调函数来处理新页面返回的结果。
* onPop的返回类型为[PopInfo](../harmonyos-references/ts-basic-components-navigation.md#popinfo11)，包含一个由开发者定义的对象result，[pop](../harmonyos-references/ts-basic-components-navigation.md#pop11)方法可以触发onPop回调并传入页面处理结果。

## 解决方案

1. 定义状态变量isShow控制bindSheet显隐。
2. 利用onPop回调函数的返回值PopInfo中的result的值决定isShow。在如下代码中，若传回的result的值为1，则令isShow=true。
3. 在子页面中使用pop方法传入result的值。

完整示例参考如下：

页面一：

```ts
@Entry
@Component
struct PageOne {
  // 定义状态变量isShow控制bindSheet显隐
  @State isShow: Boolean = false;
  pageInfo: NavPathStack = new NavPathStack();

  @Builder
  myBuilder() {
    Column() {
      Button('ToSecondPage').fontSize(15).height(50).onClick(() => {
        this.isShow = false;
        this.pageInfo.pushPathByName('SecondPage', '', (onPop) => {
          this.isShow = (onPop.result as number) === 1;
        });
      });

    };
  }

  build() {
    Navigation(this.pageInfo) {
      Column() {
        Button('bindSheet')
          .onClick(() => {
            this.isShow = true;
          })
          .fontSize(20)
          .margin(10)
          .bindSheet($$this.isShow, this.myBuilder(), {
            height: SheetSize.MEDIUM,
            blurStyle: BlurStyle.Thick,
            showClose: true,
            title: { title: 'title', subtitle: 'subtitle' },
            preferType: SheetType.CENTER,
          });
      };
    };
  }
}
```

页面二：

```ts
@Builder
export function SecondPageBulider() {
  SecondPage();
}

@Entry
@Component
export struct SecondPage {
  pageInfo = new NavPathStack();

  onBackPress(): boolean | void {
  }

  build() {
    NavDestination() {
      Column() {
        Button('ToSecondPage').fontSize(15).height(50).onClick(() => {
          this.pageInfo.pop(1);
        });
      };
    }
    .onReady((navctx) => {
      this.pageInfo = navctx.pathStack;
    })
    .width('100%')
    .height('100%');
  }
}
```

在“src/main”目录下的工程配置文件module.json5中的module字段里配置"routerMap": "$profile:router\_map"，并在“src/main/resources/base/profile”目录下新增router\_map.json。

router\_map.json：

```json
{
  "routerMap": [
    {
      "name": "SecondPage",
      "pageSourceFile": "src/main/ets/pages/PageTwo.ets",
      "buildFunction": "SecondPageBulider"
    }
  ]
}
```
