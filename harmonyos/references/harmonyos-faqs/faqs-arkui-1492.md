---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1492
title: 下载完成后，进度条回滚
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 下载完成后，进度条回滚
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2016f3d63018e4a8974e4cd8471da0659b937254e1478052bbc9f88d452e4820
---

## 问题现象

下载文件已成功，但下载进度条达到百分百后，存在回退现象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/7AJZnCOhS9S80UxGfEPlSQ/zh-cn_image_0000002658965031.png "点击放大")

## 背景知识

[Progress](../harmonyos-references/ts-basic-components-progress.md)：进度条组件，用于显示内容加载或操作处理等进度。

## 问题定位

排查代码中Progress组件中value的值，value是指当前进度值。如果value的值在达到100后，重新对value赋值，且赋值小于100，就会产生进度条回退动效。

```ts
// 监听下载进度回调的方法
onProgressUpdate(progress: number) {
  if (progress >= 100) {
    this.getUIContext().getPromptAction().showToast({
      message: '已保存至相册！'
    })
    // 进度条为100时，将进度条赋值为-1
    this.value = -1;
  } else {
    this.value = progress;
  }
}
```

## 分析结论

下载进度条达到百分百后，重新对value赋值，且赋值小于100。

## 修改建议

下载完成后，建议不对value重新赋值。

```ts
@Entry
@Component
struct ProgressTest {
  @State value: number = 40;
  total: number = 100; // 进度总长

  onProgressUpdate(progress: number) {
    if (progress >= 100) {
      // 进度条达到100后，不对value重新赋值
      return;
    } else {
      this.value = progress;
    }
  }

  build() {
    Column({ space: 20 }) {
      Text('进度条')
      Progress({ value: this.value, total: this.total, type: ProgressType.Capsule })
        .color('#FF46B1E3')
        // 限制Progress组件的宽高
        .width(30)
        .height(200)
        .backgroundColor('#4d46b1e3')
        // 旋转180度，进度条方向改为从底部开始向上
        .rotate({
          angle: 180
        })
      Button('value +20')
        .backgroundColor('#0A59F7')
        .onClick(() => {
          this.value += 20;
          this.onProgressUpdate(this.value);
        })
    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/aWcZz3njRHSGTDy30jZNig/zh-cn_image_0000002628605826.png "点击放大")
