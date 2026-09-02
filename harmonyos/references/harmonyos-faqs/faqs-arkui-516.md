---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-516
title: 对象引用错误导致UI无法刷新
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 对象引用错误导致UI无法刷新
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:20+08:00
doc_updated_at: 2026-07-15
content_hash: sha256:f45f30a85ee285acf7d9ab30b6283a31c9aabfbef599c341d37ec415fc5043cb
---

## 问题现象

在onTouchDown方法中改变状态变量的值后无法引起UI刷新，代码和运行效果如下：

```ts
@Component
struct ContainerView {
  @BuilderParam child: () => void
  onTouchDown = () => {
  } 
  onTouchUp = () => {
  }

  build() {
    Column() {
      Button('长按按钮')
        .onTouch((event) => {
          if (event.type === TouchType.Down) {
            this.onTouchDown()
          } else if (event.type === TouchType.Up) {
            this.onTouchUp()
          }
        })
      this.child()
    }
  }
}

@Entry
@Component
struct MainPage {
  @State title: string = '未点击'

  build() {
    Column() {
      ContainerView(
        {
          onTouchDown: this.onTouchDown,
          onTouchUp: () => {
            this.title = 'onTouchUp'
          }
        }
      ) {
        Text(this.title)
          .fontSize(20)
      }
    }
    .width('100%')
    .height('100%')
    .alignItems(HorizontalAlign.Center)
    .justifyContent(FlexAlign.Center)
  }

  onTouchDown() {
    this.title = 'onTouchDown'
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/q-S9sZRwQK-hSj_KVJh0Nw/zh-cn_image_0000002628391164.png "点击放大")

## 背景知识

* this是HarmonyOS中的一个关键字，代表当前对象的上下文，它指向调用该函数的对象。
* bind方法允许明确设置函数运行时的this值。当this的指向不符合预期时，可以使用bind将this设置为指定的值。

## 问题定位

1. 当直接使用this.onTouchDown时，此时this指针指向的是子组件ContainerView，实际调用的是该组件的onTouchDown空方法。
2. 使用官网提供的适配方案，即利用lambda函数形式，参考链接如下：[bind适配指导案例](../harmonyos-guides/arkts-more-cases.md#bind定义方法)。

## 分析结论

this所指向的对象错误，实际需要调用的方法没有被调用。

## 修改建议

修改onTouchDown函数，具体代码和运行效果如下：

```ts
@Component
struct ContainerView {
  @BuilderParam child: () => void;
  // 实际调用的onTouchDown方法
  onTouchDown = () => {
  };
  onTouchUp = () => {
  };

  build() {
    Column() {
      Button('长按按钮')
        .onTouch((event) => {
          if (event.type === TouchType.Down) {
            this.onTouchDown();
          } else if (event.type === TouchType.Up) {
            this.onTouchUp();
          }
        });
      this.child();
    };
  }
}

@Entry
@Component
struct TouchDownCustom {
  @State title: string = '未点击';

  build() {
    Column() {
      ContainerView(
        {
          // 修改后的代码
          onTouchDown: (): void => this.onTouchDown(),
          onTouchUp: () => {
            this.title = 'onTouchUp';
          }
        }
      ) {
        Text(this.title)
          .fontSize(20);
      };
    }
    .width('100%')
    .height('100%')
    .alignItems(HorizontalAlign.Center)
    .justifyContent(FlexAlign.Center);
  }

  onTouchDown() {
    this.title = 'onTouchDown';
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/Mc1ylV5gQqO8V3UpZXuCeQ/zh-cn_image_0000002658790415.png "点击放大")

## 常见FAQ

Q：为什么在HarmonyOS开发者文档中没有找到bind关键字的详细说明？

A：ArkTS是一种面向HarmonyOS的开发语言，它基于TypeScript扩展而来，专为HarmonyOS的分布式特性和高性能需求进行了优化，可以在TypeScript相关文档中找到bind方法的详细使用说明。
