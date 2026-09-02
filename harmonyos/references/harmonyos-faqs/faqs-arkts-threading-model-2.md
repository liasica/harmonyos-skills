---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-threading-model-2
title: 弹窗关闭延迟
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > 弹窗关闭延迟
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:54+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c4e20a1726c0f921fdf81a33fd3cf82c7c37eea5cce1840177ca38484be40619
---

## 问题现象

提示弹窗在页面加载较慢时能够提供良好的用户体验。但若页面加载完成后弹窗仍未关闭，则会影响正常使用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/fc66aZ7USkK-VQtcXglBYw/zh-cn_image_0000002628899074.png "点击放大")

## 背景知识

* [CustomDialog](../harmonyos-references/ts-methods-custom-dialog-box.md)：通过CustomDialogController类显示自定义弹窗。使用弹窗组件时，优先考虑自定义弹窗，便于弹窗样式与内容的自定义。
* [LoadingDialog](../harmonyos-references/ohos-arkui-advanced-dialog.md#loadingdialog)：进度加载类弹出框，操作正在执行时的提示信息。
* [async/await](../harmonyos-guides/async-concurrency-overview.md#asyncawait)是一种用于处理异步操作的Promise语法糖，使得编写异步代码变得更加简单和易读。通过使用async关键字声明一个函数为异步函数，并使用await关键字等待Promise的解析（完成或拒绝），以同步的方式编写异步操作的代码。

## 问题定位

1. 使用DevEco Testing查看问题组件，该问题组件为Dialog组件。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/wDvfRjw5RBu99EhuGHuqxA/zh-cn_image_0000002659258285.png "点击放大")
2. 排查弹窗Dialog的相关设置，应用使用async和await，在加载完成后台数据时才关闭加载弹窗，导致前台页面显示完成时加载弹窗仍在显示。

   ```ts
   @CustomDialog
   @Component
   struct LoadingDialogExample {
     controller?: CustomDialogController;

     build() {
       Row() {
         LoadingProgress()
           .width('40%')
           .height('100%')
           .margin({ left: 10 })
         Text('加载中')
           .fontSize(20)
           .width('40%')
           .height('100%')
           .textAlign(TextAlign.Start)
           .margin({ left: 2 })
       }
       .width('100%')
       .height('100%')
     }
   }

   @Entry
   @Component
   struct Index {
     @State content: string = '';
     dialogController: CustomDialogController = new CustomDialogController({
       builder: LoadingDialogExample(),
       width: 250,
       height: 60,
       cornerRadius: 10
     })

     async aboutToAppear(): Promise<void> {
       this.dialogController.open();
       await loadForeData().then((data) => {
         this.content = data;
       }); // 加载前端数据
       await myAsyncFunction(); // 加载后端数据
       this.dialogController.close();
     }

     build() {
       Column() {
         Text(this.content)
           .fontSize(20)
           .height('10%')
           .width('100%')
           .textAlign(TextAlign.Center)
       }
       .height('100%')
       .width('100%')
     }
   }

   async function myAsyncFunction(): Promise<void> {
     const result: string = await new Promise((resolve: Function) => {
       // 模拟加载数据
       setTimeout(() => {
         resolve('Hello, world!');
       }, 3000);
     });
   }

   async function loadForeData(): Promise<string> {
     const result: string = await new Promise((resolve: Function) => {
       // 模拟加载数据
       setTimeout(() => {
         resolve('Hello, world!');
       }, 1000);
     });
     return '测试页面';
   }
   ```

## 分析结论

应用使用async和await，在加载完成后台数据时才关闭加载弹窗，导致前台页面显示完成时加载弹窗仍在显示。

## 修改建议

加载完成前台数据后及时关闭加载弹窗，不使用await等待后台数据加载完成。

```ts
@CustomDialog
@Component
struct LoadingDialogExample {
  controller?: CustomDialogController;

  build() {
    Row() {
      LoadingProgress()
        .width('40%')
        .height('100%')
        .margin({ left: 10 });
      Text('加载中')
        .fontSize(20)
        .width('40%')
        .height('100%')
        .textAlign(TextAlign.Start)
        .margin({ left: 2 });
    }
    .width('100%')
    .height('100%');
  }
}

@Entry
@Component
struct Dialog {
  @State content: string = '';
  dialogController: CustomDialogController = new CustomDialogController({
    builder: LoadingDialogExample(),
    width: 250,
    height: 60,
    cornerRadius: 10
  });

  async aboutToAppear(): Promise<void> {
    this.dialogController.open();
    await loadForeData().then((data) => {
      this.content = data;
    });
    myAsyncFunction();
    this.dialogController.close();
  }

  build() {
    Column() {
      Text(this.content)
        .fontSize(20)
        .height('10%')
        .width('100%')
        .textAlign(TextAlign.Center);
    }
    .height('100%')
    .width('100%');
  }
}

async function myAsyncFunction(): Promise<void> {
  const result: string = await new Promise((resolve: Function) => {
    // 模拟加载数据
    setTimeout(() => {
      resolve('Hello, world!');
    }, 3000);
  });
  console.info(result);
}

async function loadForeData(): Promise<string> {
  const result: string = await new Promise((resolve: Function) => {
    // 模拟加载数据
    setTimeout(() => {
      resolve('Hello, world!');
    }, 1000);
  });
  console.info(result);
  return '测试页面';
}
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/HecdXxwNTMOe5OFky-WtPQ/zh-cn_image_0000002659138345.png "点击放大")
