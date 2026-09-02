---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-vision-2
title: 通过页面跳转将CardRecognition控件拍照界面关闭
breadcrumb: FAQ > AI功能开发 > 机器学习 > 场景化视觉（Vision） > 通过页面跳转将CardRecognition控件拍照界面关闭
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:38+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:dce24e148d8c2845c425257d054c94d0de0bc71cd025efef88a99811f744979a
---

## 问题现象

通过设置了两个[setTimeout](../harmonyos-references/js-apis-timer.md#settimeout)定时器控制[CardRecognition（卡证识别控件）](../harmonyos-references/vision-card-recognition.md)实现拍照界面关闭，预期效果是进入页面五秒后，会渲染CardRecognition控件，在进入页面十秒后，会销毁CardRecognition控件。

## 背景知识

当前系统已支持卡证识别控件提供身份证、行驶证、驾驶证、护照、银行卡等证件的结构化识别服务，满足卡证的自动分类功能，系统可自动判断所属卡证类型并返回结构化信息和卡证图片信息。CardRecognition控件会拉起的是一个系统的全模态弹窗，页面组件的显隐状态无法关闭该弹窗。

## 解决方案

将CardRecognition控件单独放在一个页面，设置定时器通过页面路由跳转来实现自主关闭卡证识别拍摄功能。核心代码参考如下：

* Index.ets：

  ```ts
  @Entry
  @Component
  struct Index {
    pathStack: NavPathStack = new NavPathStack();

    // 卡证识别入口按钮
    build() {
      Navigation(this.pathStack) {
        Button('CardRecognition', { stateEffect: true, type: ButtonType.Capsule })
          .width('50%')
          .height(40)
          .onClick(() => {
            this.pathStack.pushPathByName('cardDemoPage', null);
          });
      }.title('卡证识别控件demo')
      .mode(NavigationMode.Stack);
    }
  }
  ```

* CardDemoPage.ets

  ```ts
  import { CardRecognition, CardRecognitionResult, CardType, CardSide, ShootingMode } from '@kit.VisionKit';
  import { hilog } from '@kit.PerformanceAnalysisKit';

  const TAG: string = 'CardRecognitionPage';

  @Builder
  export function CardDemoPageBuilder() {
    CardDemoPage();
  }

  // 卡证识别页，用于加载uiExtensionAbility
  @Component
  export struct CardDemoPage {
    pathStack: NavPathStack = new NavPathStack();
    timerId: number = -1;

    aboutToDisappear(): void {
      // 子页面销毁时清除定时器
      if (this.timerId !== -1) {
        clearTimeout(this.timerId);
      }
    }

    build() {
      NavDestination() {
        CardRecognition({
          // 此处选择身份证类型作为示例
          supportType: CardType.CARD_ID,
          cardSide: CardSide.DEFAULT,
          cardRecognitionConfig: {
            defaultShootingMode: ShootingMode.MANUAL,
            isPhotoSelectionSupported: true
          },
          onResult: ((params: CardRecognitionResult) => {
            hilog.info(0x0001, TAG, `params code: ${params.code}`);
            hilog.info(0x0001, TAG, `params cardInfo front: ${JSON.stringify(params.cardInfo?.front)}`);
            hilog.info(0x0001, TAG, `params cardInfo back: ${JSON.stringify(params.cardInfo?.back)}`);
            // 手动返回或扫描到结果返回上个页面
            this.goBack();
          })
        });
      }
      .width('100%')
      .height('100%')
      .hideTitleBar(true)
      .onReady((context: NavDestinationContext) => {
        this.pathStack = context.pathStack;
        hilog.info(0x0001, TAG, `current page config info is ${JSON.stringify(context.getConfigInRouteMap())}`);
      })
      .onShown(() => {
        // 当该NavDestination页面显示时设置定时器，定时触发路由返回
        this.timerId = setTimeout(() => {
          this.goBack();
        }, 5000);
      });
    }

    /**
     * 1.如果返回的是Navigation根页面需要使用getRouter()返回
     * 2.如果返回的是NavDestination子页面可使用NavPathStack返回
     */
    goBack() {
      this.getUIContext().getRouter().replaceUrl({ url: 'pages/Index' });
    }
  }
  ```
* router\_map.json：

  ```screen
  {
    "routerMap": [
      {
        "name": "cardDemoPage",
        "pageSourceFile": "src/main/ets/pages/CardDemoPage.ets",
        "buildFunction": "CardDemoPageBuilder",
        "data": {
          "description": "this is cardDemoPage"
        }
      }
    ]
  }
  ```

**说明** 

不要在同一界面设置两个定时器，否则第二个定时器执行后也不会关闭拍照界面。
