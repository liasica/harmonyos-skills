---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-181
title: 在catch中调用未定义的方法编译运行无法捕获报错
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 在catch中调用未定义的方法编译运行无法捕获报错
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:54+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:cdd916e01d84af8d692559bb29076e307a973300fd879d418838c2db98ebc411
---

## 问题现象

定义了一个异步函数，使用try-catch来捕获可能出现的异常，如果在catch中调用未定义的方法，代码能正常编译，运行时也没有任何错误提示，但是catch之后的代码不会执行。问题代码示例参考如下：

```ts
export async function getLocalImgOrientation(oriFilePath: string) : Promise<number> {
  let orientation = '';
  try {
    Logger.info('try called');
    let file = fs.openSync(oriFilePath, fs.OpenMode.READ_ONLY);
    let imageSource: image.ImageSource = image.createImageSource(file.fd);
    orientation = await imageSource.getImageProperty(image.PropertyKey.ORIENTATION);
  } catch (e) {
    Logger.info('catch called');
    // sayHello()是一个没有声明和定义的不存在的函数，但是编译不会报错
    e.sayHello();
  }

  // 此处日志不会被打印
  Logger.info('tag one');
  let rotate: number = 0;
  if (orientation.length > 0) {
    rotate = 90;
  }
  return rotate;
}
```

调用代码示例参考如下：

```ts
Button('异步任务中调用不存在函数')
  .onClick(() => {
    // 传入一个错误参数，模拟发生异常
    let path = 'empty';
    getLocalImgOrientation(path).then((r: number) => {
      Logger.info(`r is ${r}`);
    })
  })
```

## 背景知识

[async/await](../harmonyos-guides/async-concurrency-overview.md#asyncawait)：基于Promise的语法糖，async函数本身并不会直接定义微任务，但它内部的异步操作（尤其是await后面的代码）会以微任务的形式执行。

## 解决方案

异常发生时，catch的参数e类型为any，此时调用了未定义的函数编译器无法报错属于正常现象。async函数内部的异步任务是以微任务的形态执行的，执行失败不会导致整个进程crash，也不会导致运行报错。可以通过在调用的外层函数处增加catch来捕获报错。

```ts
// 传入一个错误参数，模拟发生异常
let path = 'empty';
getLocalImgOrientation(path).then((r: number) => {
  console.info(`r is ${r}`);
}).catch((e: BusinessError) => {
  console.error(`code: ${e.code}, ${e.message}`);
});
```

运行后控制台会打印错误日志“code: undefined, undefined is not callable”。

完整示例参考如下：

```ts
import fs from '@ohos.file.fs';
import { image } from '@kit.ImageKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    Column() {
      Button('异步任务中调用不存在函数')
        .onClick(() => {
          // 传入一个错误参数，模拟发生异常
          let path = 'empty';
          getLocalImgOrientation(path).then((r: number) => {
            console.info(`r is ${r}`);
          }).catch((e: BusinessError) => {
            console.error(`code: ${e.code}, ${e.message}`);
          });
        });
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.Center);
  }
}

async function getLocalImgOrientation(oriFilePath: string): Promise<number> {
  let orientation = '';
  try {
    console.info('try called');
    let file = fs.openSync(oriFilePath, fs.OpenMode.READ_ONLY);
    let imageSource: image.ImageSource = image.createImageSource(file.fd);
    orientation = await imageSource.getImageProperty(image.PropertyKey.ORIENTATION);
  } catch (e) {
    console.info('try called');
    // sayHello()是一个没有声明和定义的不存在的函数，但是编译不会报错
    e.sayHello();
  }

  // 此处日志不会被打印
  console.info('tag');
  let rotate: number = 0;
  if (orientation.length > 0) {
    rotate = 90;
  }
  return rotate;
}
```
