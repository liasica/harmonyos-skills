---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-176
title: ArkTS重写自定义类方法未生效
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > ArkTS重写自定义类方法未生效
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:54+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a8c43eef5deaeee76baf62adadebf74357fa00f4ba050d5bd9a616a0e8dd2755
---

## 问题现象

页面中实现了一个操作类，包含三个操作方法，并在自定义组件中分别对三个方法进行重写，运行后发现其中某个方法执行的仍是未重写前的操作，问题代码示例参考如下：

```ts
// 富文本配置类。
export namespace CRichText {
  @Observed
  export class CustomRichController {
    addImage: (image: string) => void = () => {
      console.info(`添加图片`);
    }
    addVideo: (video: string) => void = () => {
      console.info(`添加视频`);
    }
    setRichText: (data: string) => void = () => {
      console.info(`设置编辑内容`);
    }
  }
}

@Entry
@Component
struct Index {
  @State controller: CRichText.CustomRichController = new CRichText.CustomRichController();

  aboutToAppear(): void {
    this.controller.setRichText('文字');
  }

  build() {
    Column() {
      testDemo({
        controller: this.controller
      })
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}

@Component
struct testDemo { // 自定义组件
  @ObjectLink controller: CRichText.CustomRichController;

  aboutToAppear(): void { // 重写方法
    this.controller.addImage = () => {
      console.info(`出现了图片`);
    }
    this.controller.addVideo = () => {
      console.info(`出现了视频`);
    }
    this.controller.setRichText = () => {
      console.info(`出现了文字`);
    }
  }

  build() {
    Column() {
      Text('这是一个测试')
        .onClick(() => {
          this.controller.addImage('图片');
          this.controller.addVideo('视频');
        })
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```

## 背景知识

组件和页面首次被创建时会触发[aboutToAppear()](../harmonyos-references/ts-custom-component-lifecycle.md#abouttoappear)函数，可以将数据的初始化操作放在这里执行。

## 问题定位

可以从以下三个方面进行排查：

1. 重写方式：对比问题方法与正常方法的重写方式，发现三个方法的重写方式相同无区别。
2. 调用位置：对比问题方法与正常方法的调用位置，发现正常方法是通过点击事件主动触发，而问题方法的触发则是放在了页面的aboutToAppear()函数内。
3. 执行顺序：类方法的重写放在自定义组件的aboutToAppear()函数内，正常方法的执行是在自定义组件创建完成后，而问题方法则是在组件创建完成之前执行。判断是问题方法的触发与重写顺序颠倒导致。

## 分析结论

问题方法的触发在自定义组件创建之前，导致方法在执行时还未进行重写，从而造成重写失效的现象。

## 修改建议

将方法执行放在重写后：

```ts
// 富文本配置类。
export namespace CRichText {
  @Observed
  export class CustomRichController {
    addImage: (image: string) => void = () => {
      console.info(`添加图片`);
    };
    addVideo: (video: string) => void = () => {
      console.info(`添加视频`);
    };
    setRichText: (data: string) => void = () => {
      console.info(`设置编辑内容`);
    };
  }
}

@Entry
@Component
struct Index {
  @State controller: CRichText.CustomRichController = new CRichText.CustomRichController();

  build() {
    Column() {
      testDemo({
        controller: this.controller
      })
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}

@Component
struct testDemo { // 自定义组件
  @ObjectLink controller: CRichText.CustomRichController;

  aboutToAppear(): void { // 重写方法
    this.controller.addImage = () => {
      console.info(`出现了图片`);
    };
    this.controller.addVideo = () => {
      console.info(`出现了视频`);
    };
    this.controller.setRichText = () => {
      console.info(`出现了文字`);
    };
    this.controller.setRichText('文字'); // 将方法调用移动到重写之后
  }

  build() {
    Column() {
      Text('这是一个测试')
        .onClick(() => {
          this.controller.addImage('图片');
          this.controller.addVideo('视频');
        })
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```
