---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1121
title: 列表左滑删除时，删除按钮异常滑动到页面最左侧
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 列表左滑删除时，删除按钮异常滑动到页面最左侧
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:12+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3269933a42ec0acbc93b997e2c470fa917d2c04d6edf563fc2e1dd3da187d887
---

## 问题现象

列表项左滑删除时，长距删除区可滑动至撑满列表子组件宽度。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/b3UlXiYPSpizbalB49RMjQ/zh-cn_image_0000002658928727.png "点击放大")

## 背景知识

[swipeAction](../harmonyos-references/ts-container-listitem.md#swipeaction9)：用于设置ListItem的划出组件。

## 问题定位

排查应用List组件是否声明了onAction事件，如果声明了onAction，删除ListItem时，组件进入长距删除区后抬手时触发，这会导致删除按钮可滑动到页面最左侧。

```ts
@Entry
@Component
struct ProblemCode {
  @Builder
  itemEnd() {
    Button('delete')
  }

  build() {
    List({ space: 10 }) {
      ForEach([0, 1, 2, 3, 4, 5], (item: number) => {
        ListItem() {
          Text("item" + item)
            .width('100%')
            .height(100)
            .fontSize(16)
            .textAlign(TextAlign.Center)
            .borderRadius(10)
            .backgroundColor(0xFFFFFF)
        }
        .transition({ type: TransitionType.Delete, opacity: 0 }).swipeAction({
          end: {
            builder: () => {
              this.itemEnd();
            },
            // 声明onAction对象
            onAction: () => {
              this.getUIContext().animateTo({ duration: 1000 }, () => {
              })
            },
            actionAreaDistance: 56,
          },
          edgeEffect: SwipeEdgeEffect.Spring
        })
      }, (item: string) => item)
    }
    .backgroundColor('#F3F4F5')
    .height('100%')
    .padding({ top: 10 })
  }
}
```

## 分析结论

列表声明了onAction对象，导致列表项左滑删除时，长距删除区可滑动至撑满列表子组件宽度。

## 修改建议

删除onAction对象，左滑删除按钮，滑动恢复正常。

```ts
@Entry
@Component
struct CorrectCode {
  @Builder
  itemEnd() {
    Button('delete')
      .backgroundColor('#E84026')
      .margin({ left: 20 })
  }

  build() {
    List({ space: 10 }) {
      ForEach([0, 1, 2, 3, 4, 5], (item: number) => {
        ListItem() {
          Text("item" + item)
            .width('100%')
            .height(100)
            .fontSize(16)
            .textAlign(TextAlign.Center)
            .borderRadius(10)
            .backgroundColor(0xFFFFFF)
        }
        .transition({ type: TransitionType.Delete, opacity: 0 }).swipeAction({
          end: {
            builder: () => {
              this.itemEnd();
            },
            actionAreaDistance: 56,
          },
          edgeEffect: SwipeEdgeEffect.Spring
        })
      }, (item: string) => item)
    }
    .backgroundColor('#F3F4F5')
    .height('100%')
    .padding({ top: 50, left: 16, right: 16 })
  }
}
```
