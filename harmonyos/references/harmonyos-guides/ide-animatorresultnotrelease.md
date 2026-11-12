---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-animatorresultnotrelease
title: AnimatorResultNotRelease
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查规则 > ArkTS代码检查规则 > AnimatorResultNotRelease
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:00+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:569e26b80c9d8339daacd787b6b8ce911388bce11cca6a8f374d5ed7a9cd63bb
---

通过Animator.create()、Animator.createAnimator()方法创建的AnimatorResult对象，使用完毕后，需及时调用finish()或cancel()方法释放对象，避免导致内存泄漏。

## 规则配置

```json
// rules.json
{
  "rules": {
    "arkts": {
      "ResourceLeak": [
        {
          "ruleId": "AnimatorResultNotRelease",
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

```screen
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
