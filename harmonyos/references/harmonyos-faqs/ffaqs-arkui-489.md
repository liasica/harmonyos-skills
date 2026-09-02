---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/ffaqs-arkui-489
title: 如何解决应用键盘出现遮挡，输入框被拦截一半
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何解决应用键盘出现遮挡，输入框被拦截一半
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:00+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:690611f8f97f8c219786fffefdda5fedc7e761c3737e702561a2ba92adab72f8
---

为了避免组件覆盖，系统规格设计软键盘的[安全间距](../harmonyos-references/ts-universal-attributes-expand-safe-area.md)为16vp。用[offset](../harmonyos-references/js-apis-arkui-componentutils.md#offset)方法设置16vp的间距，示例代码如下：

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { ComponentContent } from '@kit.ArkUI';

class Params {
  text: string = '';

  constructor(text: string) {
    this.text = text;
  }
}

@Builder
function buildText(params: Params) {
  Column() {
    TextInput({ placeholder: 'input your word...' })
      .placeholderColor(Color.Grey)
      .placeholderFont({
        size: 14,
        weight: 400
      })
      .caretColor(Color.Blue)
      .fontColor(Color.Black)
  }
  .backgroundColor('#FFF0F0F0')
  .borderRadius(12)
  .height(350)
  .width('100%')
  .offset({
    x: 0,
    y: 16  // Popup window position, when y equals 16, it is just right.
  })
}

@Entry
@Component
struct Index {
  @State message: string = 'hello';

  build() {
    Row() {
      Column() {
        Button('click me')
          .onClick(() => {
            let uiContext = this.getUIContext();
            let promptAction = uiContext.getPromptAction();
            let contentNode = new ComponentContent(uiContext, wrapBuilder(buildText), new Params(this.message));
            try {
              promptAction.openCustomDialog(contentNode, {
                alignment: DialogAlignment.Bottom,
                offset: {
                  dx: 0,
                  dy: 0
                }
              });
            } catch (error) {
              let message = (error as BusinessError).message;
              let code = (error as BusinessError).code;
              console.error(`OpenCustomDialog args error code is ${code}, message is ${message}`);
            }
          })
      }
      .width('100%')
      .height('100%')
    }
    .height('100%')
  }
}
```
