---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1105
title: openBindSheet引用颜色资源不随系统深浅色模式切换变化
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > openBindSheet引用颜色资源不随系统深浅色模式切换变化
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:27+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3ac167d16d671511e5548460bb9933cd8648d428b4996240c70cd8924ffdf813
---

## 问题现象

使用[openBindSheet](../harmonyos-references/arkts-apis-uicontext-uicontext.md#openbindsheet12)打开半模态弹窗，弹窗内容引用了资源颜色，并且深浅模式下配置颜色不同，切换深浅色模式后，弹窗中内容颜色不会发生变化，需要关闭后重新打开才能生效。问题复现代码如下：

```ts
import { FrameNode, ComponentContent } from "@kit.ArkUI";
import { BusinessError } from '@kit.BasicServicesKit';

class Params {
  text: string = "";
  constructor(text: string) {
    this.text = text;
  }
}

let contentNode: ComponentContent<Params>;

@Builder
function buildText(params: Params) {
  Column() {
    Text(params.text)
      .fontColor($r("app.color.fontcolor"))
}

@Entry
@Component
struct UIContextBindSheet {
  @State message: string = 'BindSheet';
  uiContext = this.getUIContext()

  build() {
    RelativeContainer() {
      Column() {
        Button('Open BindSheet')
          .fontSize(20)
          .onClick(() => {
            contentNode = new ComponentContent(this.uiContext, wrapBuilder(buildText), new Params(this.message));
            let uniqueId = this.getUniqueId();
            let frameNode: FrameNode | null = this.uiContext.getFrameNodeByUniqueId(uniqueId);
            let targetId = frameNode?.getFirstChild()?.getUniqueId();
            this.uiContext.openBindSheet(contentNode, {
              height: SheetSize.MEDIUM,
              backgroundColor: $r("app.color.start_window_background"),
              title: { title: "Title", subtitle: "subtitle" }
            }, targetId)
              .then(() => {
                console.info('openBindSheet success');
              })
              .catch((err: BusinessError) => {
                console.error('openBindSheet error');
              })
          })
      }
    }
    .height('100%')
    .width('100%')
  }
}
```

## 背景知识

* 使用[openBindSheet](../harmonyos-references/arkts-apis-uicontext-uicontext.md#openbindsheet12)创建并弹出以bindSheetContent作为内容的半模态页面，使用Promise异步回调。通过该接口弹出的半模态页面样式完全按照bindSheetContent中设置的样式显示。
* [ColorMode](../harmonyos-references/ts-state-management-environment-variables.md#colormode)系统当前深浅色模式。
* 自定义节点BuilderNode和ComponentContent需手动传递系统环境变化事件，触发节点的全量更新，详细请参考[BuilderNode系统环境变化更新](../harmonyos-references/js-apis-arkui-buildernode.md#updateconfiguration12)。

## 解决方案

openBindSheet中的内容须传入自定义节点[ComponentContent](../harmonyos-references/js-apis-arkui-componentcontent.md)，该节点内容刷新须自行管理，以避免频繁刷新带来的性能开销。从而导致引用颜色资源不随系统深浅色模式变化的现象。解决方案如下：

* **方案一**：使用ComponentContent的[update](../harmonyos-references/js-apis-arkui-componentcontent.md#update)方法更新节点信息，[updateConfiguration](../harmonyos-references/js-apis-arkui-componentcontent.md#updateconfiguration)方法来传递[系统环境变化](../harmonyos-references/js-apis-app-ability-configuration.md)事件，触发节点的全量更新。

  ```ts
  import { FrameNode, ComponentContent } from '@kit.ArkUI';
  import { Configuration, EnvironmentCallback, ConfigurationConstant } from '@kit.AbilityKit';
  import { BusinessError } from '@kit.BasicServicesKit';
  import { resourceManager } from '@kit.LocalizationKit';

  class Params {
    text: string = '';
    colorMode: resourceManager.ColorMode = resourceManager.ColorMode.LIGHT;

    constructor(text: string, colorMode: resourceManager.ColorMode) {
      this.text = text;
      this.colorMode = colorMode;
    }
  }

  @Builder
  function buildText(params: Params) {
    Column() {
      Text(params.text)
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .margin({ bottom: 36 })
        .fontColor($r('app.color.fontcolor'))
    }
  }

  @Entry
  @Component
  struct Index {
    @State message: string = 'hello';
    contentNode: ComponentContent<Params> | null = null;
    callbackId: number | undefined = 0;

    build() {
      Row() {
        Column() {
          Button('click me')
            .onClick(() => {
              let uiContext = this.getUIContext();
              let uniqueId = this.getUniqueId();
              let frameNode: FrameNode | null = uiContext.getFrameNodeByUniqueId(uniqueId);
              let targetId = frameNode?.getFirstChild()?.getUniqueId();
              if (this.contentNode == null && uiContext.getHostContext() != undefined) {
                this.contentNode = new ComponentContent(uiContext, wrapBuilder(buildText), new Params(this.message,
                  uiContext.getHostContext()!!.getApplicationContext()
                    .getApplicationContext()
                    .resourceManager
                    .getConfigurationSync()
                    .colorMode
                ));
              }
              if (this.contentNode == null) {
                return;
              }
              uiContext.openBindSheet(this.contentNode, {
                height: SheetSize.MEDIUM,
                title: { title: 'Title', subtitle: 'subtitle' }
              }, targetId)
                .then(() => {
                  console.info('openBindSheet success');
                })
                .catch((err: BusinessError) => {
                  console.error('openBindSheet error: ' + err.code + ' ' + err.message);
                });
            })
        }
        .width('100%')
        .height('100%')
      }
      .height('100%')
    }

    aboutToAppear(): void {
      let environmentCallback: EnvironmentCallback = {
        onMemoryLevel: (): void => {
          console.log('onMemoryLevel');
        },
        onConfigurationUpdated: (config: Configuration): void => {
          console.log('onConfigurationUpdated ' + JSON.stringify(config));
          let uiContext = this.getUIContext();
          uiContext.getHostContext()?.getApplicationContext()
            .getApplicationContext()
            .resourceManager.getConfiguration((err, config) => {
            // 调用ComponentContent的update更新里面信息
            this.contentNode?.update(new Params(this.message, config.colorMode));
            setTimeout(() => {
              // 调用ComponentContent的updateConfiguration，触发节点的全量更新。
              this.contentNode?.updateConfiguration();
            }, 1000);
          });
        }
      };
      // 注册监听回调
      this.callbackId =
        this.getUIContext().getHostContext()?.getApplicationContext().on('environment', environmentCallback);
      // 设置应用深浅色跟随系统
      this.getUIContext()
        .getHostContext()?.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
    }

    aboutToDisappear(): void {
      // 解注册监听environment的回调
      this.getUIContext().getHostContext()?.getApplicationContext().off('environment', this.callbackId);
      this.contentNode?.dispose();
    }
  }
  ```
* **方案二**：HarmonyOS 6.0以上版本，可以开启系统开关触发深浅色变化，在src/main/module.json5新增"configColorModeChangePerformanceInArkUI"。

  **注**：若在属性设置中使用了函数的方式去适配深浅色变更，开启此开关会导致对应逻辑不生效，需要通过[回调监听](../harmonyos-references/js-apis-app-ability-abilitystage.md#onconfigurationupdate)配置变更，当颜色模式变化时，通过绑定状态变量等手段，定制比如宽高变化、布局更新等特定的业务逻辑。

  ```json
  "metadata": [
    {
      "name": "configColorModeChangePerformanceInArkUI",
      "value": "true"
    }
  ],
  ```
