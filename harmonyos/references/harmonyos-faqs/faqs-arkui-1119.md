---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1119
title: 组件颜色与界面背景颜色相近
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 组件颜色与界面背景颜色相近
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ed0e9daa2f76be444dc6e152b401e9c04398eebfca8a5a17622b955f319d40e8
---

## 问题现象

应用内组件间颜色相近，如按钮组件背景色与按钮的文本颜色、页面背景色等相近，无法突出显示组件区域和文本内容，影响用户体验。

## 背景知识

* [Button](../harmonyos-references/ts-basic-components-button.md)按钮组件，可快速创建不同样式的按钮。
* [设置文本样式](../harmonyos-references/ts-basic-components-text.md#示例2设置文本样式)，border、borderColor设置文本的边框线、边框颜色。

## 问题定位

1. 排查页面背景色backgroundColor属性以及组件fontColor、backgroundColor属性的值。确认组件背景色、按钮文本颜色和页面背景色相近。
2. 排查组件是否设置边框用以区分组件区域。排查组件是否有使用border等和边框相关的属性。

## 分析结论

1. 应用内按钮文本颜色与按钮背景色相近、按钮背景色和页面背景色相近，导致组件间颜色区分不明显。
2. 组件未使用边框，组件区域和页面区分不明显。

## 修改建议

1. 将按钮组件的文字颜色，设置成与按钮背景色相反的颜色。组件背景色可以设置不同色系，与页面背景色进行区分。

   ```ts
   Button('按钮设置背景颜色', { type: ButtonType.Normal })
     .fontColor(Color.Black)
     .backgroundColor(Color.Gray)
     .margin({ top: 30 });
   ```
2. 给组件添加边框，边框颜色需要和页面背景色有明显区分，突出显示组件边界区域。

   ```ts
   Button('按钮设置边框', { type: ButtonType.Normal })
     .backgroundColor(Color.Gray)
     .border({
       width: 2,
       color: Color.Blue
     });
   ```

完整代码示例：

```ts
@Entry
@Component
struct buttonTest {
  build() {
    Column({ space: 20 }) {
      Button('按钮设置背景颜色', { type: ButtonType.Normal })
        .fontColor(Color.Black)
        .backgroundColor(Color.Gray)
        .margin({ top: 30 });
      Button('按钮设置边框', { type: ButtonType.Normal })
        .backgroundColor(Color.Gray)
        .border({
          width: 2,
          color: Color.Blue
        });
    }
    .backgroundColor(Color.White)
    .height('100%')
    .width('100%');
  }
}
```
