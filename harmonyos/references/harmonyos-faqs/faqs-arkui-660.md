---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-660
title: 如何实现弹框跟随自定义UI组件的消失而消失
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现弹框跟随自定义UI组件的消失而消失
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:26+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:aef974c0495e8a97b8c810dbb6b68ca49259a055a9945d1e7cecc64f44641bdb
---

## 问题现象

页面A跳转到页面B，页面B使用UIContext.getPromptAction().openCustomDialog()的方式弹出自定义弹框，此时页面B返回到页面A，但弹框未消失。

需要实现的效果是弹框能在B页面退出后自动跟随消失，即弹窗跟随页面一起消失。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/jEtvRmrPSbqlSYVLLYqY3g/zh-cn_image_0000002658793923.png "点击放大")

## 背景知识

* [@ohos.promptAction (弹窗)](../harmonyos-references/js-apis-promptaction.md)：创建并显示即时反馈、对话框和操作菜单。
* [BaseDialogOptions](../harmonyos-references/js-apis-promptaction.md#basedialogoptions11)：选项中onWillDismiss()交互式关闭回调函数：当用户执行点击遮障层关闭、侧滑（左滑/右滑）、三键back、键盘ESC关闭交互操作时，如果注册该回调函数，则不会立刻关闭弹窗。在回调函数中可以通过reason得到阻拦关闭弹窗的操作类型，从而根据原因选择是否能关闭弹窗。

## 解决方案

创建DialogOne并实现跳转到DialogTwo，使用弹窗组件的onWillDismiss()回调函数对应的枚举值实现关闭弹窗。并跳转回Dialog1页面。同时也可以实现侧滑返回页面A时，页面B与弹窗一起消失。

* Dialog1初始页面，仅用于页面跳转。

  代码如下：

  ```ts
  @Entry
  @Component
  struct DialogOne {
    pageInfo: NavPathStack = new NavPathStack();

    build() {
      Navigation(this.pageInfo) {
        Column() {
          Button('点击跳转')
            .id('Dialog1HelloWorld')
            .backgroundColor('#0a59f7')
            .fontWeight(FontWeight.Bold)
            .onClick(() => {
              this.pageInfo.pushPath({ name: 'DialogTwo' });
            });
        }
        .justifyContent(FlexAlign.Center)
        .padding(16)
        .height('100%')
        .width('100%');
      };
    }
  }
  ```
* DialogTwo页面。@Builder函数customDialogComponent()为弹窗自定义内容，通过使用UIContext中的getPromptAction方法获取当前UI上下文关联的PromptAction对象，拉起弹窗，点击确认返回上一页面。

  ```ts
  @Builder
  export function DialogTwoBuilder() {
    DialogTwo();
  }

  @Component
  export struct DialogTwo {
    private customDialogComponentId: number = 0;
    pageInfo: NavPathStack = new NavPathStack();
    ctx: UIContext = this.getUIContext();

    @Builder
    customDialogComponent() {
      Column() {
        Text('弹窗')
          .fontSize(24)
          .fontWeight(FontWeight.Bold);
        Text('点击确定返回DialogOne并关闭弹窗');
        Row() {
          Button('取消')
            .width('45%')
            .borderRadius(20)
            .backgroundColor(Color.Transparent)
            .fontColor('#0a59f7')
            .onClick(() => {
              try {
                this.ctx.getPromptAction().closeCustomDialog(this.customDialogComponentId);
              } catch (error) {
                console.error(error);
              }
            });
          Button('确认')
            .width('45%')
            .borderRadius(20)
            .onClick(() => {
              // 模拟B页面操作返回
              this.pageInfo.pop();
            });
        }
        .width('100%')
        .justifyContent(FlexAlign.SpaceAround);
      }
      .height(200)
      .padding(16)
      .justifyContent(FlexAlign.SpaceEvenly);
    }

    build() {
      NavDestination() {
        Column({ space: 16 }) {
          Button('点击返回')
            .onClick(() => {
              this.ctx.getPromptAction().openCustomDialog({
                builder: () => {
                  this.customDialogComponent();
                },
                onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
                  console.info(`reason: ${JSON.stringify(dismissDialogAction.reason)}`);
                  console.info('dialog onWillDismiss');
                  if (dismissDialogAction.reason === DismissReason.PRESS_BACK) {
                    this.pageInfo.pop();
                  }
                }
              }).then((dialogId: number) => {
                this.customDialogComponentId = dialogId;
              });
            });
        }
        .onVisibleAreaChange([0.0, 1.0], (isVisible: boolean, currentRatio: number) => {
          this.ctx.getPromptAction().closeCustomDialog(this.customDialogComponentId);
          console.info(`isVisible: ${isVisible}, currentRatio: ${currentRatio}`);
        })
        .padding(16)
        .height('100%');
      }
      .hideTitleBar(true)
      .onReady((value) => {
        this.pageInfo = value.pathStack;
      });
    }
  }
  ```
* router\_map.json路由表：配置详见[系统路由表](../harmonyos-guides/arkts-navigation-cross-package.md#系统路由表)。

  ```json
  {
    "routerMap": [
      {
        "name" : "DialogTwo",
        "pageSourceFile"  : "src/main/ets/pages/DialogTwo.ets",
        "buildFunction" : "DialogTwoBuilder"
      }
    ]
  }
  ```
