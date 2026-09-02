---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1510
title: 如何解决父子组件传递私有@Builder函数，内容不显示的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何解决父子组件传递私有@Builder函数，内容不显示的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:24+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8e64bc7773b963b99221e94d12a341007dd3710782211f0db90a7ea8980f1fec
---

## 问题现象

自定义两个父子组件，在父组件中声明了一个@Builder装饰的私有自定义构建函数并传递给子组件，子组件通过@BuilderParam装饰器接收父组件传递的@Builder函数并使用，存在自定义构建函数被子组件调用后，Text组件内容不显示的问题，问题代码示例参考如下：

```ts
// 父组件
@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  @Builder
  contentComponent() {
    Row() {
      Text(this.message)
        .fontSize(15)
        .fontWeight(FontWeight.Bold)
        .onClick(() => {
          this.message = 'Welcome';
        });
    }
    .backgroundColor(Color.Gray)
    .borderRadius(10)
    .justifyContent(FlexAlign.Center)
    .width('90%')
    .height(50);
  }

  build() {
    RelativeContainer() {
      SectionView({
        title: '第一章',
        contentView: this.contentComponent
      });
    }
    .height('100%')
    .width('100%');
  }
}

// 子组件
@Component
export struct SectionView {
  @Prop title: string = '';

  @Builder
  defaultContentView() {
  }

  @BuilderParam contentView: () => void = this.defaultContentView;

  build() {
    Column({
      space: 10
    }) {
      Text(this.title)
        .fontSize(16)
        .width('100%')
        .textAlign(TextAlign.Center);
      this.contentView();
    }
    .backgroundColor(Color.White);
  }
}
```

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/UnEMKGJ8QWOLJqMWqd_WDw/zh-cn_image_0000002628766434.png "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/1xdX4EOxTLyLSi2KEXhfLQ/zh-cn_image_0000002658965769.png "点击放大")

## 背景知识

* [@Builder装饰器](../harmonyos-guides/arkts-builder.md)：自定义构建函数装饰器，可以用于声明[全局自定义构建函数](../harmonyos-guides/arkts-builder.md#全局自定义构建函数)与[私有自定义构建函数](../harmonyos-guides/arkts-builder.md#私有自定义构建函数)。当自定义构建函数在@Component自定义组件内调用，且需要外部传参时，存在以下区别：

| 全局自定义构建函数 | 私有自定义构建函数 |
| --- | --- |
| 若需要传入的参数不是全局变量，是@Component自定义组件内的变量时，必须在调用时通过函数的参数传递的方式获取构建UI需要的数据。 | 由于私有自定义构建函数是@Component组件内定义的，所以在@Component组件调用私有自定义构建函数时，可以不通过函数的参数传递方式，直接采用this指针，指向调用时所在的@Component组件变量。 |

* [@BuilderParam装饰器](../harmonyos-guides/arkts-builderparam.md)用于自定义构建函数的传递，且可以为其添加特定的功能，实现组件定制化的能力。
* [@LocalBuilder装饰器](../harmonyos-guides/arkts-localbuilder.md)比局部@Builder能够更好的确定组件的父子关系和状态管理的父子关系，可以使子组件调用父组件的@LocalBuilder函数时，内部变量的this指针依旧指向父组件的变量。详见官方文档：[@LocalBuilder和局部@Builder使用区别](../harmonyos-guides/arkts-localbuilder.md#localbuilder和局部builder使用区别)。

## 问题定位

本地运行代码，没有报错信息，@Builder函数被成功调用，但是内部的Text文本未显示，推测是传入自定义组件的参数值有问题，通过debug发现contentComponent方法中this.message的值为undefined。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/zOaRtXY_RISfSszSWkUf_A/zh-cn_image_0000002628606556.png "点击放大")

## 分析结论

调用子组件传入contentView: this.contentComponent参数时，contentComponent组件构建函数中this指向的是子组件SectionView，相当于在子组件中使用了this.message，而子组件中没有message这个变量，所以调试显示为undefined，从而导致内容不生效。

## 修改建议

方法一：修改传入子组件的参数，将自定义构建函数的方法放在箭头函数内，直接调用父组件的构建方法。参考问题示例代码，核心修改如下：

```ts
build() {
  RelativeContainer() {
    OptionOneSectionView({
      title: '第一章',
      contentView: () => {
        this.contentComponent();
      }
    });
  }
  .height('100%')
  .width('100%');
}
```

方法二：将@Builder修改为@LocalBuilder，确保组件的父子关系与状态管理的父子关系保持一致。参考问题示例代码，核心修改如下：

```ts
@Entry
@Component
struct OptionTwoIndex {
  @State message: string = 'Hello World';

  @LocalBuilder
  contentComponent() {
    Row() {
      Text(this.message)
        .fontSize(15)
        .fontWeight(FontWeight.Bold)
        .onClick(() => {
          this.message = 'Welcome';
        });
    }
    .backgroundColor(Color.Gray)
    .borderRadius(10)
    .justifyContent(FlexAlign.Center)
    .width('90%')
    .height(50);
  }

  build() {
    RelativeContainer() {
      OptionTwoSectionView({
        title: '第一章',
        contentView: this.contentComponent
      });
    }
    .height('100%')
    .width('100%');
  }
}
```

## 总结

父子组件间传递@Builder私有自定义构建函数时，由于this指针的变化，需要注意其内部this指针指向的变量在子组件中是否调用成功。

拓展知识：若子组件内恰好有同名变量，则@Builder函数会调用子组件内的同名变量。所以可能会出现渲染出的数据不符合预期的问题。
