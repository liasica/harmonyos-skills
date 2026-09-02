---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-179
title: 自定义组件间如何实现从底部滑入滑出的效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 自定义组件间如何实现从底部滑入滑出的效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:28+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3834d7f9128c0f9afeb291aaa2fde4973005d53ab632322e385de1102fe3e681
---

**问题现象**

页面底部默认显示自定义组件A。点击组件A，A消失，自定义组件B从底部出现。点击组件B，B消失，A从底部出现。如何实现这个效果？

**解决措施**

使用transition产生组件转场动画。参数type用于设置组件变化场景，包括新增和删除；参数translate用于设置转场时的平移效果。注意，transition需要配合animateTo才能生效，动效的时长、曲线和延时需跟随animateTo中的配置。参考代码如下：

```ts
@Entry
@Component
struct ComponentTransition {
  @State flag: boolean = true;

  build() {
    Stack({ alignContent: Alignment.Bottom }) {
      if (this.flag) {
        ComponentChild1({ flag: $flag })
          .transition({ type: TransitionType.Insert,translate: { x: 0, y: 200 } })
      }
      if (!this.flag) {
        ComponentChild2({ flag: $flag })
          .transition({ type: TransitionType.Insert, translate: { x: 0, y: 200 } })
      }
    }.height('100%').width('100%')
  }
}

@Component
struct ComponentChild1 {
  @Link flag: boolean

  build() {
    Column() {
      Image($r('app.media.ic_banner01'))// path: resources\base\media
        .width('100%')
        .height(200)
        .onClick(() => {
          this.getUIContext().animateTo({ duration: 1000 }, () => {
            this.flag = !this.flag;
          })
        })
    }
  }
}

@Component
struct ComponentChild2 {
  @Link flag: boolean

  build() {
    Column() {
      Image($r('app.media.ic_banner02'))// path: resources\base\media
        .width('100%')
        .height(200)
        .onClick(() => {
          this.getUIContext().animateTo({ duration: 1000 }, () => {
            this.flag = !this.flag;
          })
        })
    }
  }
}
```

**参考链接**

[组件内转场](../harmonyos-references/ts-transition-animation-component.md)
