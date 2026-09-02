---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-307
title: 如何查看触摸热区范围
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何查看触摸热区范围
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:28+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d24b29658aa11f39a3a5d7610c83bde18b1bca7a6035c0768f5c7318467ba9cf
---

通过自定义方式设置responseRegion属性值并结合日志打印的方式，来明确和验证组件的触摸热区范围。

默认情况下，组件的触摸热区即为其自身的位置和大小，与用户看到的视觉范围一致。当开发者显示调用responseRegion()时，系统会以所绑定的热区范围为准，替代默认的布局区域。

通过为组件绑定包含x、y、width、height参数的responseRegion属性来自定义热区，并在点击回调中打印出具体的坐标与尺寸参数，从而确认热区的生效范围。例如，在下面示例代码中，按钮的触摸热区被设置为宽度50%、高度100%。这意味着只有按钮的左半部分（热区内）响应点击事件，右半部分（热区外）点击无效。

参考代码如下：

```ts
@Entry
@Component
struct TouchTargetExample {
  @State text: string = '';
  @State x: number = 0;
  @State y: number = 0;
  @State regWidth: string = '50%';
  @State regHeight: string = '100%';

  build() {
    Column({ space: 20 }) {
      Text(`{x:0,y:0,width:'50%',height:'100%'}`)
      // The width of the hot zone is half of the button, and there is no response when clicking on the right side
      Button('button1')
        .responseRegion({
          x: this.x,
          y: this.y,
          width: this.regWidth,
          height: this.regHeight
        })
        .onClick(() => {
          this.text = 'button1 clicked';
          console.info('button1 clicked: ' + this.x + ' ' + this.y + ' ' + this.regWidth + ' ' + this.regHeight);
        })

      Text(this.text)
        .margin({ top: 10 })
    }
    .width('100%')
    .margin({ top: 100 })
  }
}
```

**参考链接**

[responseRegion](../harmonyos-references/ts-universal-attributes-touch-target.md#responseregion)
