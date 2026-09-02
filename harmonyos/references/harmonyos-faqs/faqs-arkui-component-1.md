---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-component-1
title: Button如何实现点击事件透传
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Button如何实现点击事件透传
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:12+08:00
doc_updated_at: 2026-07-02
content_hash: sha256:ef5f1da348cd485528f55310371bcd86fc34747424bd13eb3ac58d5b4d0ef430
---

## 问题现象

点击两个按钮的公共区域，同时输出两个按钮对应的日志内容，如何实现，问题代码如下：

```ts
@Entry
@Component
struct HitTestBehaviorExample {
  build() {
    Stack() {
      Stack() {
        Button('Button1')
          .width(50)
          .height(200)
          .hitTestBehavior(HitTestMode.Transparent)
          .onClick(() => {
            console.debug('Button1',`点击了`)
          })

        Button('Button2')
          .width(200)
          .height(50)
          .backgroundColor('#ff5500')
          .hitTestBehavior(HitTestMode.Transparent)
          .onClick(() => {
            console.debug('Button2',`点击了`)
          })
      }
      .width("100%")
      .height("100%")
    }.width(300).height(300).backgroundColor('#F5F5F5')
  }
}
```

运行结果如下，Button1按钮没有触发点击事件回调：

```txt
09-01 22:18:30.675   6833-6833     A03d00/JSAPP                    com.lee.m...ication2  D     Button2 点击了
```

## 背景知识

* [hitTestBehavior](../harmonyos-references/ts-universal-attributes-hit-test-behavior.md#hittestbehavior)属性用于设置不同的触摸测试响应模式，影响触摸测试收集结果及后续触屏事件分发，具体影响参考[HitTestMode](../harmonyos-references/ts-appendix-enums.md#hittestmode9)枚举说明。
* [onClick](../harmonyos-references/ts-universal-events-click.md#onclick12)为系统手势，为非冒泡事件。当父组件和子组件绑定同类型的手势时，父子组件绑定的手势事件会发生竞争，子组件会优先识别绑定的手势。

## 问题定位

使用hitTestBehavior属性透传Button按钮的onClick点击事件，但是上层组件的onClick不会向下分发，而onTouch触摸事件可以分发到下层组件。

## 分析结论

把onClick点击事件，改为onTouch触摸事件让事件分发到下层实现透传。

## 修改建议

使用onTouch事件透传，修改后的代码如下：

```ts
@Entry
@Component
struct HitTestBehaviorExample {
  build() {
    Stack() {
      Stack() {
        Button('button1')
          .width(50)
          .height(200)
          .hitTestBehavior(HitTestMode.Transparent)
          .onTouch((event: TouchEvent) => {
            if (event.type == TouchType.Down) {
              console.debug('button1', `点击了`);
            }
          });

        Button('button2')
          .width(200)
          .height(50)
          .backgroundColor('#ff5500')
          .hitTestBehavior(HitTestMode.Transparent)
          .onTouch((event: TouchEvent) => {
            if (event.type == TouchType.Down) {
              console.debug('button2', `点击了`);
            }
          });
      }
      .width('100%')
      .height('100%');
    }.width(300).height(300).backgroundColor('#F5F5F5');
  }
}
```

运行结果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/KbxogUPqTDKnIYDOVuaktA/zh-cn_image_0000002631375376.png "点击放大")
