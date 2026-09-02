---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-form-11
title: 点击服务卡片有概率无法打开详情页
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 卡片开发（Form） > 点击服务卡片有概率无法打开详情页
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:56+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7e0dc1c1928c84eb3f2d6f1f7aa96f4d4aa48e290f42bb56b7292bb74717b634
---

## 问题现象

桌面添加应用卡片，点击卡片中的内容，有概率无法打开详情页。

## 背景知识

* [onClick](../harmonyos-references/ts-universal-events-click.md#onclick12)点击动作触发该回调。
* 针对动态卡片，ArkTS卡片中提供了[postCardAction](../harmonyos-references/js-apis-postcardaction.md#postcardaction-1)接口用于卡片内部和提供方应用间的交互，当前支持router、message和call三种类型的事件，仅在卡片中可以调用。
* 针对静态卡片，ArkTS卡片提供了[FormLink](../harmonyos-references/ts-container-formlink.md)用于卡片内部和提供方应用间的交互。

## 问题定位

使用[Deveco Testing](../harmonyos-guides/deveco-testing.md)工具中的UIViewer分析卡片的组件结构，使用真机点击卡片中的对应不同组件对应的位置，发现只有文章内容位置可以点击跳转到应用。

## 分析结论

卡片中只对文章内容做了点击跳转事件，其它区域未做点击事件。

## 修改建议

为整个卡片添加点击事件。当点击卡片内容时卡片服务跳转指定页面，其它区域根据业务需要，拉起应用页面。具体跳转操作如下：

在UIAbility中接收router事件并获取参数，根据传递的params不同，选择拉起不同的页面。

```ts
// EntryAbility.ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
export default class EntryAbility extends UIAbility {
  private selectPage: string = '';
  private currentWindowStage: window.WindowStage | null = null;
  // 获取router事件中传递的targetPage参数
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    if (want.parameters !== undefined) {
      let params: Record<string, string> = JSON.parse(JSON.stringify(want.parameters));
      this.selectPage = params.targetPage;
    }
  }
  // 如果UIAbility已在后台运行，在收到Router事件后会触发onNewWant生命周期回调
  onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    if (want.parameters?.params !== undefined) {
      let params: Record<string, string> = JSON.parse(JSON.stringify(want.parameters));
      this.selectPage = JSON.parse(params.params).message
    }
    if (this.currentWindowStage !== null) {
      this.onWindowStageCreate(this.currentWindowStage);
    }
  }
  onWindowStageCreate(windowStage: window.WindowStage): void {
    let targetPage: string='pages/Index';
    if(this.selectPage=='PageB'){
      targetPage='pages/PageB'
    }
    if (this.currentWindowStage === null) {
      this.currentWindowStage = windowStage;
    }
    windowStage.loadContent(targetPage, (err) => {
      if (err.code) {
        return;
      }
    });
  }
}
```
