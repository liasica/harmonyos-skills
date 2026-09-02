---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-796
title: 使用嵌套弹窗时，无法打开上层弹窗
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 使用嵌套弹窗时，无法打开上层弹窗
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:04+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:498ba627e8bbc3068ec11b7e7a099bd0879a6a132e8821143d6036f97ef6f6df
---

## 问题现象

在弹窗中使用this.dialogController.open()方法打开上层弹窗时，出现闪退现象并报错：

```txt
Error message:Cannot read property open of undefined。
```

问题代码如下：

```ts
@Entry
@Component
export struct Index {
  aDialogParamTwo = new CustomDialogController({
    builder: ADialogParamTwo({
      visitorMode: this.visitorMode
    })
  })
  aDialogParam = new CustomDialogController({
    builder: ADialogOne({}),
  });
  visitorMode() {
    this.aDialogParam.open()
  }
  build() {
    Column() {
      Button('打开aDialogParamTwo弹窗')
        .onClick(() => {
          // 打开aDialogParamTwo弹窗
          this.aDialogParamTwo.open()
        })
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
/**
 * 弹窗一
 * 用于模拟在弹窗二中打开弹窗一
 */
@CustomDialog
export struct ADialogOne {
  controller: CustomDialogController = new CustomDialogController({
    builder: ADialogOne({}),
  })
  build() {
    Column({}) {
      Button() {
        Text('隐私协议')
      }
    }
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}

/**
 * 弹窗二
 * 模拟调用弹窗二的方法来打开弹窗一
 */
@CustomDialog
export struct ADialogParamTwo {
  controller: CustomDialogController = new CustomDialogController({
    builder: ADialogParamTwo({}),
  })
  visitorMode: () => void = () => {
  }
  build() {
    Column({}) {
      Button() {
        Button('click').onClick(() => {
          // 通过aDialogParamTwo弹窗的click按钮调用传入的箭头函数从而调用aDialogParam弹窗的this.aDialogParamTwo.open()方法，打开aDialogParam弹窗。
          this.visitorMode()
        })
      }
    }
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```

问题代码运行效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/g21AMpg7S-iLtxt4x4Kt3g/zh-cn_image_0000002628557640.png "点击放大")

## 背景知识

[CustomDialog](../harmonyos-references/ts-methods-custom-dialog-box.md)是自定义弹出框，可用于广告、中奖、警告、软件更新等与用户交互响应操作。可以通过[CustomDialogController](../harmonyos-references/ts-methods-custom-dialog-box.md#customdialogcontroller)类显示自定义弹出框。

## 问题定位

运行代码时出现报错Error message:Cannot read property open of undefined，确认是aDialogParamTwo对象调用visitorMode()方法导致的报错。在实例化aDialogParamTwo对象时，代码直接使用“传递方法引用”的方式将visitorMode()方法传递aDialogParamTwo的visitorMode参数，使visitorMode()方法中的this关键字指向调用者aDialogParamTwo；但因为aDialogParamTwo中未定义aDialogParam，所以visitorMode()方法内部在调用this.aDialogParam的open()方法的时候出现报错。

## 分析结论

* visitorMode()方法内部使用了this，如果使用“传递类方法引用”将这个方法传递给调用者aDialogParamTwo使用，visitorMode()方法内部的this会指向aDialogParamTwo对象，而不是父组件Index。因为aDialogParamTwo中没有定义aDialogParam对象，导致visitorMode()方法内部调用this.aDialogParam.open()会报错。

  ```ts
    visitorMode() {
        this.aDialogParam.open()
      }
  ```

  ```ts
    aDialogParamTwo = new CustomDialogController({
      builder: ADialogParamTwo({
        // 传递类方法引用
        visitorMode: this.visitorMode
      })
    })
  ```
* 箭头函数没有自己的this，所以使用箭头函数包裹方法时，visitorMode()方法内部的this会继承它外层作用域的this。在这里，箭头函数中的this（外层作用域的this）始终指向父组件Index，所以visitorMode()方法内部的this也会指向父组件Index。由于Index中已定义aDialogParam对象，因此能正确调用this.aDialogParam.open()。

  ```ts
    aDialogParamTwo = new CustomDialogController({
      builder: ADialogParamTwo({
        // 将箭头函数传递给aDialogParamTwo弹窗的visitorMode
        visitorMode: () => {
          // 箭头函数包裹this.visitorMode()
          this.visitorMode()
        }
      })
    })
  ```

## 修改建议

通过箭头函数包裹方法，并将箭头函数传递给aDialogParamTwo对象中的visitorMode参数，示例代码如下：

```ts
@Entry
@Component
export struct Index {
  aDialogParamTwo = new CustomDialogController({
    builder: ADialogParamTwo({
      // 将箭头函数传递给aDialogParamTwo弹窗的visitorMode
      visitorMode: () => {
        // 箭头函数包裹this.visitorMode()
        this.visitorMode();
      }
    })
  });
  aDialogParam = new CustomDialogController({
    builder: ADialogOne({}),
  });
  visitorMode() {
    this.aDialogParam.open();
  }
  build() {
    Column() {
      Button('打开aDialogParamTwo弹窗')
        .onClick(() => {
          // 打开aDialogParamTwo弹窗
          this.aDialogParamTwo.open();
        })
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}

/**
 * 弹窗一
 * 用于模拟在弹窗二中打开弹窗一
 */
@CustomDialog
export struct ADialogOne {
  controller: CustomDialogController = new CustomDialogController({
    builder: ADialogOne({}),
  });
  build() {
    Column({}) {
      Button('隐私协议')
        .onClick(() => {
        })
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.Center)
    .backgroundColor('#d1d1d6')
  }
}

/**
 * 弹窗二
 * 模拟调用弹窗二的方法来打开弹窗一
 */
@CustomDialog
export struct ADialogParamTwo {
  controller: CustomDialogController = new CustomDialogController({
    builder: ADialogParamTwo({}),
  });
  visitorMode: () => void = () => {
  };
  build() {
    Column({}) {
      Button() {
        Button('click').onClick(() => {
          // 通过aDialogParamTwo弹窗的click按钮调用传入的箭头函数从而调用aDialogParam弹窗的this.aDialogParamTwo.open()方法，打开aDialogParam弹窗。
          this.visitorMode();
        })
      }
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.Center)
    .backgroundColor('#f1f3f5')
  }
}
```

运行效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/fBIAdDzhTkSF-z6MDUy_sg/zh-cn_image_0000002658916953.png "点击放大")
