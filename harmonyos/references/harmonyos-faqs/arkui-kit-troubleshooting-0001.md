---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-kit-troubleshooting-0001
title: ArkUI-RichEditor键盘弹出与焦点问题定位
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 故障排查 > ArkUI-RichEditor键盘弹出与焦点问题定位
category: harmonyos-faqs
scraped_at: 2026-10-15T07:13:52+08:00
doc_updated_at: 2026-10-14
content_hash: sha256:f4fd1d182a658fe34265a377aed5467c0f166a167cb1027cbfe528b318f6885e
---

## 怎么解决进入RichEditor组件页面无法自动拉起软键盘的问题

### 问题现象

进入到某个含有RichEditor组件的页面，没有自动拉起软键盘，需要点击后才能拉起软键盘。

### 定位过程

RichEditor组件无法拉起软键盘，说明当前页面焦点不在该组件上。因此需要确认当前页面焦点。

1. 首先查看RichEditor组件有没有设置获取焦点。通过实现onFocus获取焦点监听事件，查看是否执行；
2. 排查当前页面默认焦点是否冲突。需要排查当前页面布局下，其他组件（包括自定义组件）是否也获取焦点；
3. 排查具体哪个组件获取了焦点。在所有获取焦点组件下实现onFocus获取焦点监听事件，查看最后具体哪个组件获得了当前页面焦点。

### 分析结论

经过排查，发现是由于某个自定义组件中也设置了defaultFocus属性为true，导致RichEditor没有获取到焦点，无法拉起软键盘。

```ts
@Entry
@Component
struct Index {
  controller: RichEditorController = new RichEditorController();

  build() {
    Column() {
      // 内部设置了defaultFocus属性为true。
      RichEditor({ controller: this.controller })
        .focusable(true)
        .onFocus(() => {
          console.info('RichEditor onfocus')
        })
        .key('editor')
    }
    .width('100%')
    .height('100%')
  }
}
```

### 修改建议

1. 排查删除不必要的组件获取焦点。
2. 设置RichEditor组件获取焦点，具体有如下两种方式：

* 方式一：设置RichEditor组件的defaultFocus属性为true。

  ```ts
  @Component
  struct Solution1 {
    controller: RichEditorController = new RichEditorController();

    build() {
      Column() {
        RichEditor({ controller: this.controller })
          .focusable(true)
          .onFocus(() => {
            console.info('RichEditor onfocus');
          })
          .defaultFocus(true)
          .key('editor')
      }
      .width('100%')
      .height('100%')
    }
  }
  ```
* 方式二：通过requestFocus在页面展示或者组件挂载后获取焦点。

  ```ts
  @Component
  struct Solution2 {
    controller: RichEditorController = new RichEditorController();

    aboutToAppear(): void {
      focusControl.requestFocus('editor'); // 页面展示时获取
    }

    build() {
      Column() {
        RichEditor({ controller: this.controller })
          .focusable(true)
          .onFocus(() => {
            console.info('RichEditor onfocus');
          })
          .key('editor')
          .onAppear(() => {
            focusControl.requestFocus('editor'); // 组件挂载时
          })
      }
      .width('100%')
      .height('100%')
    }
  }
  ```

完整参考代码如下：

```ts
@Entry
@Component
struct RichEditorFocusDemo {
  private controller: TabsController = new TabsController();

  build() {
    Column() {
      Tabs({ barPosition: BarPosition.End, controller: this.controller }) {
        TabContent() {
          Solution1();
        }.width('100%')
        .tabBar('solution1')
        TabContent() {
          Solution2();
        }.width('100%')
        .tabBar('solution2')
      }
    }
    .width('100%')
    .height('100%')
  }
}

@Component
struct Solution1 {
  controller: RichEditorController = new RichEditorController();

  build() {
    Column() {
      RichEditor({ controller: this.controller })
        .focusable(true)
        .onFocus(() => {
          console.info('RichEditor onfocus');
        })
        .defaultFocus(true)
        .key('editor')
    }
    .width('100%')
    .height('100%')
  }
}

@Component
struct Solution2 {
  controller: RichEditorController = new RichEditorController();

  aboutToAppear(): void {
    focusControl.requestFocus('editor'); // 页面展示时获取
  }

  build() {
    Column() {
      RichEditor({ controller: this.controller })
        .focusable(true)
        .onFocus(() => {
          console.info('RichEditor onfocus');
        })
        .key('editor')
        .onAppear(() => {
          focusControl.requestFocus('editor'); // 组件挂载时
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

## 使用customKeyboard设置自定义键盘时，弹出失败

### 问题现象

自定义键盘通过focusController获取焦点的时候，弹出的键盘是系统键盘，而不是预期的自定义键盘。

问题代码如下：

```ts
@Entry
@Component
struct CustomKeyboardPage {
  controller: RichEditorController = new RichEditorController()
  @State keyboardVisible: boolean = false
  customKeyboard: CustomBuilder = () => {
    this.buildCustomKeyboard()
  }

  build() {
    Column({ space: 10 }) {
      RichEditor({ controller: this.controller })
        .id('RichEditor')
        .height(200)
        .backgroundColor('#99e2dddd')
        .width('90%')
        .borderRadius(15)
        .customKeyboard(this.keyboardVisible ? this.customKeyboard :
          undefined) // 这种写法点击「切换自定义键盘」无法正常调出自定义键盘，弹出的是系统键盘
      Button('切换自定义键盘').onClick(() => {
        this.keyboardVisible = true
        this.getUIContext().getFocusController().requestFocus('RichEditor')
      })
      Button('切换至系统键盘')
        .onClick(() => {
          this.keyboardVisible = false
        })
    }
    .width('100%')
    .justifyContent(FlexAlign.Center)
  }

  // 自定义键盘
  @Builder
  buildCustomKeyboard() {
    Row() {
      Text('自定义键盘')
    }
    .justifyContent(FlexAlign.Center)
    .height('200')
    .width('100%')
    .backgroundColor('#990946cd')
  }
}
```

### 定位过程

1. this.customKeyboard函数未用@Builder装饰器修饰。

   customKeyboard属性的第一个参数[CustomBuilder](../harmonyos-references/ts-types.md#custombuilder8)用于自定义UI描述，必须结合@Builder使用。
2. 由于customKeyboard属性不是实时渲染，在更改this.keyboardVisible变量后，customKeyboard需要更新渲染。

   该问题代码中this.getUIContext().getFocusController().requestFocus("RichEditor")是在当前帧生效。更改this.keyboardVisible变量后，customKeyboard还没有完成渲染，因此第一次依旧会弹出系统键盘。使用focusControl.requestFocus("RichEditor")让控件在下一帧获取焦点即可，此时customKeyboard已完成渲染。

### 分析结论

该问题代码存在以下两个问题：

1. customKeyboard属性内this.customKeyboard函数未使用@Builder装饰器修饰，导致customKeyboard属性设置失效，无法弹出自定义键盘。
2. this.getUIContext().getFocusController().requestFocus("RichEditor")获取焦点是在当前帧生效，由于更改keyboardVisible变量后，customKeyboard未更新渲染完成，导致第一次获取焦点无法弹出自定义键盘。

### 修改建议

1. 采用@Builder装饰器自定义构建函数。修改customKeyboard函数代码：

   ```ts
   @Builder
     customKeyboard() {
       this.buildCustomKeyboard();
     }
   ```
2. customKeyboard属性更新后再获取焦点。采用focusControl.requestFocus方法代替this.getUIContext().getFocusController().requestFocus方法获取组件焦点。

   ```ts
   Button('切换自定义键盘')
           .onClick(() => {
             this.keyboardVisible = true;
             focusControl.requestFocus('RichEditor');
           });
   ```

完整示例如下：

```ts
@Entry
@Component
struct CustomKeyboardPage {
  controller: RichEditorController = new RichEditorController();
  @State keyboardVisible: boolean = false;

  @Builder
  customKeyboard() {
    this.buildCustomKeyboard();
  }

  build() {
    Column({ space: 10 }) {
      RichEditor({ controller: this.controller })
        .id('RichEditor')
        .height(200)
        .backgroundColor('#99e2dddd')
        .width('90%')
        .borderRadius(15)
        .customKeyboard(this.keyboardVisible ? this.customKeyboard :
          undefined); // 这种写法点击「切换自定义键盘」无法正常调出自定义键盘，弹出的是系统键盘
      Button('切换自定义键盘')
        .onClick(() => {
          this.keyboardVisible = true;
          focusControl.requestFocus('RichEditor');
        });
      Button('切换至系统键盘')
        .onClick(() => {
          this.keyboardVisible = false;
        });
    }
    .width('100%')
    .justifyContent(FlexAlign.Center);
  }

  // 自定义键盘
  @Builder
  buildCustomKeyboard() {
    Row() {
      Text('自定义键盘');
    }
    .justifyContent(FlexAlign.Center)
    .height('200')
    .width('100%')
    .backgroundColor('#990946cd');
  }
}
```

实现效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/hH-0qsT-SB-FxkjTFifsFA/zh-cn_image_0000002789281371.png "点击放大")
