---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-776
title: Navigation中如何关闭removeByName删除页面时的默认动画
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Navigation中如何关闭removeByName删除页面时的默认动画
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:22+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f292872742abcad250f86fbd89b49e3504e2856576901c94ad29c5da0b97092b
---

## 问题现象

Navigation中使用removeByName删除页面时存在从底部滑出的动画，API文档上未提供关闭动画的参数，如何关闭该动画？

目前效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/gMZ2ZD-yTxC_gXoSh8RnrA/zh-cn_image_0000002658915025.png "点击放大")

## 背景知识

[customNavContentTransition](../harmonyos-references/ts-basic-components-navigation.md#customnavcontenttransition11)：设置Navigation自定义转场动画，通过返回的from、to得到退场/进场Destination的页面，其中也包括NavDestination名称、序号等信息，可以区分不同的NavDestination页面。

## 解决方案

可以通过[customNavContentTransition](../harmonyos-references/ts-basic-components-navigation.md#customnavcontenttransition11)设置自定义转场动画，设置退场时无动画实现关闭removeByName的默认动画，如：

Navigation中设置customNavContentTransition，通过返回的name区分页面：

```ts
@Entry
@Component
struct Index {
  @Provide('pageInfos') pageInfo: NavPathStack = new NavPathStack();
  @State flag: boolean = false;

  aboutToAppear(): void {
    let eventhub = this.getUIContext().getHostContext()?.eventHub;
    eventhub!.on('removeByNameEvent', () => {
      this.flag = true;
    });
  }

  build() {
    Navigation(this.pageInfo) {
      Column({ space: 10 }) {
        Button('点我push第二页')
          .onClick(() => {
            this.pageInfo.pushPathByName('SubPage', null, false);
          });
      }
      .alignItems(HorizontalAlign.Center)
      .justifyContent(FlexAlign.Center)
      .width('100%')
      .height('100%');
    }
    // 设置自定义转场动画
    .customNavContentTransition((from: NavContentInfo, to: NavContentInfo, operation: NavigationOperation) => {
      console.info(`current info: ${to.name}, index: ${to.index}, mode: ${to.mode}`);
      console.info(`pre info: ${from.name}, index: ${from.index}, mode: ${from.mode}`);
      console.info(`operation: ${operation}`);
      // 通过name区分具体的页面
      if (from.name == 'SubPage' && this.flag === true) {
        this.flag = false;
        let customAnimation: NavigationAnimatedTransition = {
          onTransitionEnd: (isSuccess: boolean) => {
            console.info(`current transition result is ${isSuccess}`);
          },
          timeout: 100,
          // 转场开始时系统调用该方法，并传入转场上下文代理对象
          transition: () => {
            if (operation == NavigationOperation.POP) {
              this.getUIContext().animateTo({
                duration: 0, // 持续时间设置为0
              }, () => {
              });
            }
          }
        };
        return customAnimation;
      }
      return undefined;
    });
  }
}
```

注册SubPage页面：

```ts
@Builder
export function RegisterBuilder(): void {
  SubPage();
}

@Component
struct SubPage {
  @Consume('pageInfo') pathStack: NavPathStack;

  build() {
    NavDestination() {
      Column({ space: 20 }) {
        Button('removeByName当前页面')
          .onClick(() => {
            let eventhub = this.getUIContext().getHostContext()?.eventHub;
            // 通过eventHub设置removeByName的区分标志区分removeByName和页面返回事件
            eventhub!.emit('removeByNameEvent');
            this.pathStack.removeByName('SubPage');
          });
      }
      .width('100%')
      .height('100%')
      .alignItems(HorizontalAlign.Center)
      .justifyContent(FlexAlign.Center)
      .backgroundColor(Color.Transparent);
    }
    .title('第二页')
    .width('100%')
    .height('100%');
  }
}
```

在src/main目录下的工程配置文件module.json5中的module字段里配置"routerMap": "$profile:router\_map"，并在src/main/resources/base/profile目录下新增router\_map.json。router\_map.json示例如下。

```json
{
  "routerMap": [
    {
      "name": "SubPage",
      "pageSourceFile": "src/main/ets/pages/SubPage.ets",
      "buildFunction": "RegisterBuilder"
    }
  ]
}
```
