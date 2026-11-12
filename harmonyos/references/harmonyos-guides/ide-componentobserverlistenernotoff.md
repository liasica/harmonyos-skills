---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-componentobserverlistenernotoff
title: ComponentObserverListenerNotOff
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查规则 > ArkTS代码检查规则 > ComponentObserverListenerNotOff
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:00+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:1065510f32b2c1c8603d0eee5886d22cf0d6810f586c1183fc45f0cacedc9587
---

[inspector.ComponentObserver](../doccenter-references/api/js-apis-arkui-inspector.md#componentobserver)为组件布局和组件绘制送显完成回调的句柄，通过句柄向对应的查询条件注册回调，当组件布局完成时会触发该回调。

在.on()方法使用完毕后，需及时调用对应.off()方法注销监听，避免导致内存泄漏。

## 规则配置

```json
// rules.json
{
  "rules": {
    "arkts": {
      "ResourceLeak": [
        {
          "ruleId": "ComponentObserverListenerNotOff",
          "severity": "error",
          "skip": false
        }
      ]
    }
  }
}
```

## 正例

```ts
import { inspector } from '@kit.ArkUI';

/**
 * 正例：正确释放资源
 */
@Component
struct TestRelease {
  private listenerForImage: inspector.ComponentObserver = this.getUIContext().getUIInspector().createComponentObserver('IMAGE_ID')
  private listenerForRow: inspector.ComponentObserver = this.getUIContext().getUIInspector().createComponentObserver('ROW_ID')
  private onLayoutComplete: () => void = (): void => {
    console.log('This is onLayoutComplete callback');
  }
  private onDrawComplete: () => void = (): void => {
    console.log('This is onDrawComplete callback');
  }
  private onDrawChildrenComplete: () => void = (): void => {
    console.log('This is onDrawChildrenComplete callback');
  }
  aboutToAppear() {
    this.listenerForImage.on('layout', this.onLayoutComplete)
    this.listenerForImage.on('draw', this.onDrawComplete)
    this.listenerForRow.on('drawChildren', this.onDrawChildrenComplete)
  }
  aboutToDisappear() {
    this.listenerForImage.off('layout', this.onLayoutComplete)
    this.listenerForImage.off('draw', this.onDrawComplete)
    this.listenerForRow.off('drawChildren', this.onDrawChildrenComplete)
  }
  build() {
    Text('This is build')
  }
}
```

## 反例

```ts
import { inspector } from '@kit.ArkUI';

/**
 * 反例：未释放资源
 */
@Component
struct TestNotRelease {
  private listenerForImage: inspector.ComponentObserver = this.getUIContext().getUIInspector().createComponentObserver('IMAGE_ID')
  private listenerForRow: inspector.ComponentObserver = this.getUIContext().getUIInspector().createComponentObserver('ROW_ID')
  private onLayoutComplete: () => void = (): void => {
    console.log('This is onLayoutComplete callback');
  }
  private onDrawComplete: () => void = (): void => {
    console.log('This is onDrawComplete callback');
  }
  private onDrawChildrenComplete: () => void = (): void => {
    console.log('This is onDrawChildrenComplete callback');
  }
  aboutToAppear() {
    this.listenerForImage.on('layout', this.onLayoutComplete)
    this.listenerForImage.on('draw', this.onDrawComplete) // leak
    this.listenerForRow.on('drawChildren', this.onDrawChildrenComplete)
  }
  aboutToDisappear() {
    this.listenerForImage.off('layout', this.onLayoutComplete)
    this.listenerForRow.off('drawChildren', this.onDrawChildrenComplete)
  }
  build() {
    Text('This is build')
  }
}
```

Code Scanner代码检查规则的配置指导请参考[1.6.3 代码检查工具（codescanner）](ide-command-line-codescanner.md)
