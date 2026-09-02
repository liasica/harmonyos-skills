---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-share-9
title: 应用中如何拦截弹出分享窗口
breadcrumb: FAQ > 应用服务开发 > 内容分享服务（Share Kit） > 应用中如何拦截弹出分享窗口
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:740842155ff6fa6a261b5e66bc968f74cdab718f186d6d862abc775295dd348b
---

## 问题现象

应用安全管控禁止对外分享，如何拦截弹出分享窗口？

## 背景知识

[Aspect](../harmonyos-references/js-apis-util.md#aspect11)类用于封装提供切面能力（Aspect Oriented Programming，简写AOP）的接口，这些接口可用于对类方法进行前后插桩或替换实现。

## 解决方案

使用[replace](../harmonyos-references/js-apis-util.md#replace11)方法拦截systemShare.ShareController的show接口。

```ts
import { common } from "@kit.AbilityKit";
import { systemShare } from "@kit.ShareKit";
import { util } from '@kit.ArkTS';
import { uniformTypeDescriptor as utd } from '@kit.ArkData';
import { promptAction } from '@kit.ArkUI';

@Entry
@Component
struct BlockSharePage {
  aboutToAppear(): void {
    util.Aspect.replace(systemShare.ShareController, 'show', false, () => {
      this.getUIContext().getPromptAction().showToast({
        message: "禁止分享",
        duration: 2000,
        showMode: promptAction.ToastShowMode.TOP_MOST,
        bottom: 85
      });
    });
  }

  private async shareFile(): Promise<void> {
    let uiContext: UIContext = this.getUIContext();
    let context: common.UIAbilityContext = uiContext.getHostContext() as common.UIAbilityContext;

    let data: systemShare.SharedData = new systemShare.SharedData({
      utd: utd.UniformDataType.HYPERLINK,
      content: '',//替换为真实链接地址
      title: '华为商城',
      description: 'Pura 70 Ultra',
      label: '华为商城' // 单选模式时生效
    });

    let controller: systemShare.ShareController = new systemShare.ShareController(data);
    controller.on('dismiss', () => {
      console.info('Share panel closed');
    });

    controller.show(context, {
      selectionMode: 0,
      excludedAbilities: [systemShare.ShareAbilityType.COPY_TO_PASTEBOARD], // 从操作区排除复制操作
    });
  }

  build() {
    RelativeContainer() {
      Text("文本分享")
        .id('BlockSharePageHelloWorld')
        .fontSize($r('app.float.page_text_font_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          this.shareFile()
        })
    }
    .height('100%')
    .width('100%')
  }
}
```
