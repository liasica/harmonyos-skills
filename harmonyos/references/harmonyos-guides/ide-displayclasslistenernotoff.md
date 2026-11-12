---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-displayclasslistenernotoff
title: DisplayClassListenerNotOff
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查规则 > ArkTS代码检查规则 > DisplayClassListenerNotOff
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:00+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:050023fa93a3cb4a8527caecb18e5c8a10796a1e97df05f122adacb2eed8b7c2
---

[display.Display](../doccenter-references/api/js-apis-display.md#display)为屏幕实例，描述Display对象的属性和方法，在.on()方法使用完毕后，需及时调用对应的.off()方法注销监听，避免导致内存泄漏。

**说明** 

调用.on()监听接口后，只要存在对应的.off()调用（即取消全部或部分监听），不产生告警；仅当代码中不存在任何.off()调用时，才产生告警。

## 规则配置

```json
// rules.json
{
  "rules": {
    "arkts": {
      "ResourceLeak": [
        {
          "ruleId": "DisplayClassListenerNotOff",
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
import animator, { AnimatorOptions, AnimatorResult, SimpleAnimatorOptions } from '@ohos.animator';
let simpleOptions: SimpleAnimatorOptions = new SimpleAnimatorOptions(100, 200).duration(2000);

let options: AnimatorOptions = {
  duration: 1500,
  easing: "friction",
  delay: 0,
  fill: "forwards",
  direction: "normal",
  iterations: 3,
  begin: 200.0,
  end: 400.0,
};
/**
 * 正例：正确释放资源
 */
@Component
export struct TestRelease {
  private animator1: AnimatorResult = animator.create(simpleOptions);
  private animator2: AnimatorResult = animator.createAnimator(options);
  aboutToAppear() {
    console.log('Do something else');
  }
  build() {
    Text('Hello TestRelease')
  }
  aboutToDisappear() {
    this.animator1.cancel();
    this.animator2.finish();
  }
}
```

## 反例

```ts
import animator, { AnimatorOptions, AnimatorResult, SimpleAnimatorOptions } from '@ohos.animator';
let simpleOptions: SimpleAnimatorOptions = new SimpleAnimatorOptions(100, 200).duration(2000);

let options: AnimatorOptions = {
  duration: 1500,
  easing: "friction",
  delay: 0,
  fill: "forwards",
  direction: "normal",
  iterations: 3,
  begin: 200.0,
  end: 400.0,
};
/**
 * 反例：未释放资源
 */
@Component
export struct TestNotRelease {
  private animator1: AnimatorResult = animator.create(simpleOptions);
  private animator2: AnimatorResult = animator.createAnimator(options); // leak
  aboutToAppear() {
    console.log('Do something else');
  }
  build() {
    Text('Hello TestNotRelease')
  }
  aboutToDisappear() {
    this.animator1.cancel();
  }
}
```

Code Scanner代码检查规则的配置指导请参考[1.6.3 代码检查工具（codescanner）](ide-command-line-codescanner.md)
