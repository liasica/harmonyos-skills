---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1489
title: 点击进入页面后，页面内的单个组件异常闪动
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 点击进入页面后，页面内的单个组件异常闪动
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:264c049331d7da5c31de97af71198c9a42c3a0f1fe79ba54c0dbcbb8adab8bd3
---

## 问题现象

点击进入页面后，页面内的单个组件突然出现，存在闪动问题。

## 背景知识

[骨架屏](https://gitee.com/harmonyos-cases/cases/tree/master/CommonAppDevelopment/feature/skeletondiagram)用于在数据未完全加载之前占位页面，减少用户等待焦虑，加强用户体验。

## 问题定位

* 排查是否有使用linearGradient属性，设置骨架屏的渐变背景色。
* 排查是否使用translate属性、animation属性以及onAppear事件，实现骨架屏的加载动画。

若上述功能均未实现，则判断未使用骨架屏功能。

## 分析结论

应用没有使用骨架屏占位，部分组件需要在获取数据后才会出现。如果组件突然出现，会导致闪动。

## 修改建议

页面建议使用骨架屏功能，避免组件突然出现造成闪动。

```typescript
@Entry
@Component
struct SkeletonScreen {
  @State translageX: string = '-100%';
  widthValue: number = 100;
  heightValue: number = 28;

  build() {
    Stack() {
      // 背景
      Text()
        .height(this.heightValue)
        .width(this.widthValue)
        .backgroundColor('rgba(220,220,220,1)');
      // 动画
      Text()
        .height(this.heightValue)
        .width(this.widthValue)
        .translate({ x: this.translageX })
        .onAppear(() => {
          this.translageX = '100%';
        })
        .animation({
          duration: 1500,
          iterations: -1,
        })
        .linearGradient({
          angle: 90,
          colors: [
            ['rgba(255,255,255,0)', 0],
            ['rgba(255,255,255,1)', 0.5],
            ['rgba(255,255,255,0)', 1]
          ]
        });
    };
  }
}
```
