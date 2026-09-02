---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-906
title: Navigation自定义标题栏不生效问题如何修改
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Navigation自定义标题栏不生效问题如何修改
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:18+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ffca78c475c855cd41e8bfcef2b14d147180f05e05aeb081996dc73204f8442e
---

## 问题现象

使用Navigation时，自定义了一个标题栏布局，使用其中的title方法无效。

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/tri6awaVTkOYHr-eEUEa2w/zh-cn_image_0000002628399758.png "点击放大")

问题代码示例参考如下：

```ts
@Entry
@Component
struct Index {
  text: string = '标题';
  customTitle: NavigationCustomTitle = {
    builder: this.customTitleBuilder(),
    height: TitleHeight.MainOnly
  };

  @Builder
  customTitleBuilder() {
    Row() {
      Text(this.text);
    };
  }

  build() {
    Navigation() {
      Column() {
        Text('首页')
          .fontSize(40);
      }
      .justifyContent(FlexAlign.Center)
      .width('100%')
      .height('100%');
    }
    .title(this.customTitle);
  }
}
```

## 背景知识

[Navigation](../harmonyos-references/ts-basic-components-navigation.md)是路由容器组件，一般作为首页的根容器。其内部默认包含了标题栏、内容区和工具栏。其中内容区默认首页显示导航内容，标题栏和工具栏均支持传入自定义样式。

## 解决方案

使用ArkUI Inspector查看应用布局，发现TitleBar不可见，标题栏未创建。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/Ji6AST-WSoe94WQ6chcO8Q/zh-cn_image_0000002658799027.png "点击放大")

查看[title](../harmonyos-references/ts-basic-components-navigation.md#title)传入参数类型，其中NavigationCustomTitle和CustomBuilder这两种类型均支持自定义标题栏样式。

代码中使用的NavigationCustomTitle类型变量，自定义标题的方法在传入时，没有绑定当前上下文。在执行时，this指向了NavigationCustomTitle对象，找不到相应的方法，因而无法渲染绘制标题栏。

* **方案一**：NavigationCustomTitle里builder传入方法需要bind(this)。

  ```ts
  @Entry
  @Component
  struct NavTitleSolution1 {
    text: string = '标题';
    customTitle: NavigationCustomTitle = {
      builder: this.customTitleBuilder.bind(this),
      height: TitleHeight.MainOnly
    };

    @Builder
    customTitleBuilder() {
      Row() {
        Text(this.text)
          .fontSize(20);
      }.margin({ left: 18, top: 28 });
    }

    build() {
      Navigation() {
        Column() {
          Text('首页')
            .fontSize(40);
        }
        .justifyContent(FlexAlign.Center)
        .width('100%')
        .height('100%');
      }
      .title(this.customTitle);
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/rMk62wiUToC76vrcmLw15Q/zh-cn_image_0000002628559674.png "点击放大")
* **方案二**：在title中直接传入自定义布局的方法。

  ```ts
  @Entry
  @Component
  struct NavTitleSolution2 {
    text: string = '标题';

    @Builder
    customTitleBuilder() {
      Row() {
        Text(this.text)
          .fontSize(20);
      }.margin({ left: 18, top: 28 });
    }

    build() {
      Navigation() {
        Column() {
          Text('首页')
            .fontSize(40);
        }
        .justifyContent(FlexAlign.Center)
        .width('100%')
        .height('100%');
      }
      .hideBackButton(true)
      .titleMode(NavigationTitleMode.Mini)
      .title(this.customTitleBuilder());
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/2CquOetPTdOMgtO70jb4ag/zh-cn_image_0000002658918981.png "点击放大")

## 常见FAQ

Q：NavDestination怎么修改单个页面标题文字颜色？

A：参考上述解决方案，在title中传入@Builder构建函数实现自定义标题栏，可以指定文字颜色。
