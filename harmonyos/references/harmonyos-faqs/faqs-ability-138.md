---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-138
title: 深色模式下页面白屏
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 深色模式下页面白屏
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:51d44f52dbd5d8b98237322f1a51d3c927dc20db8dfe068a9991f75c25036d0c
---

## 问题现象

页面切换到深色模式下页面白屏，无法展示正常的文本信息。

## 背景知识

[深色模式](../design-guides/dark-mode-0000001823255497.md)（Dark Mode）又称之为暗色模式，是与日常应用使用过程中的浅色模式（Light Mode）相对应的一种UI主题。当系统切换到深色模式后，例如状态栏、弹窗背景色、系统控件等没有进行[深色模式适配](../best-practices/bpta-dark-mode-adaptation.md#section1755912412277)，会导致应用内页面效果错乱。

为应对上述情况，需要对应用进行深色模式下的内容适配，目前该适配主要依靠资源目录。当系统对应的设置项发生变化后（如系统语言、深浅色模式等），应用会自动加载对应资源目录下的资源文件。

## 问题定位

1. 排查页面容器backgroundColor背景色是否设置为白色。
2. 排查文本组件是否设置字体颜色，设置字体颜色非白色，比如蓝色查看是否能正常显示。

## 分析结论

页面代码中，根组件背景色设置成白色，而文本未设置字体颜色，采用默认颜色，便导致了页面出现白屏现象。

## 修改建议

方案一：

参考[深色模式颜色资源适配](../best-practices/bpta-dark-mode-adaptation.md#section1292642062514)，取消页面根组件的背景颜色设置，在资源路径，dark目录中定义同名的资源，实现深色模式下的显示效果。

方案二：

可在EntryAbility中设置应用为浅色模式不跟随系统改变，让页面始终保持浅色模式显示。

```screen
import { ConfigurationConstant, UIAbility} from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';

const DOMAIN = 0x0000;

export default class EntryAbility extends UIAbility {
  onCreate(): void {
    try {
      // 方案二：让页面始终保持浅色模式显示
      this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_LIGHT);
    } catch (err) {
      hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
    }
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
  }

  onDestroy(): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
        return;
      }
      hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
    });
  }

  onWindowStageDestroy(): void {
    // Main window is destroyed, release UI related resources
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
  }

  onForeground(): void {
    // Ability has brought to foreground
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
  }

  onBackground(): void {
    // Ability has back to background
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
  }
}
```

运行效果如下：

| 方案一 | 方案二 |
| --- | --- |
|  |  |
