---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/ability-kit-faq-0003
title: 拉起浏览器应用常见问题
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 常见问题 > 拉起浏览器应用常见问题
category: harmonyos-faqs
scraped_at: 2026-10-21T07:10:24+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:13693b88b8ce253be165f7057400ce75288af78b489e95efc3611fb65e3aec6d
---

**Q：如何拉起浏览器应用？**

**A**：开发者可以通过在 want 参数中隐式指定 action 为 ohos.want.action.viewData 来启动浏览器应用，并在 want的 uri 参数中配置要打开的网页链接。此时，系统将启动设备上的默认浏览器。如果设备上存在多个浏览器应用，并且希望用户能够自行选择要使用的浏览器，需要在 parameters 中设置 ohos.ability.params.showDefaultPicker 为 true。具体代码如下所示。

```ts
import { common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

function startBrowsableAbility(context: common.UIAbilityContext): void {
  let want: Want = {
    action: 'ohos.want.action.viewData',
    entities: ['entity.system.browsable'],
    uri: 'https://www.huawei.com/',
    parameters: {
      'ohos.ability.params.showDefaultPicker': true
    }
  };
  context.startAbility(want)
    .then(() => {
      console.info('Start browsableAbility successfully.');
    })
    .catch((err: BusinessError) => {
      console.error(`Failed to startAbility. Code: ${err.code}, message: ${err.message}`);
    });
}

@Entry
@Component
struct BrowsableAbilityView {
  @State message: string = 'Pull up the browser and open the Huawei official website';

  build() {
    Row() {
      Column() {
        Button(this.message)
          .fontSize(24)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            const context: common.UIAbilityContext = this.getUIContext().getHostContext()! as common.UIAbilityContext;
            startBrowsableAbility(context);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```
