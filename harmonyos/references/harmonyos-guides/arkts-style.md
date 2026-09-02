---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-style
title: "@Styles装饰器：定义组件重用样式"
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式基本语法 > 组件扩展 > @Styles装饰器：定义组件重用样式
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:15+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:cd98bda1582b6bcdeaceebcda60177a698bc6b26468149725ad485ae7957df25
---

如果每个组件的样式都需要单独设置，在开发过程中会出现大量代码在进行重复样式设置，虽然可以复制粘贴，但为了代码简洁性和后续方便维护，我们推出了可以提炼公共样式进行复用的装饰器[@Styles](../harmonyos-references/ts-custom-component-decorator-styles.md#styles)。

@Styles装饰器可以将多条样式设置提炼成一个方法，直接在组件声明的位置调用。通过@Styles装饰器可以快速定义并复用自定义样式。

**说明** 

从API version 9开始支持。

从API version 9开始，该装饰器支持在ArkTS卡片中使用。

从API version 11开始，该装饰器支持在元服务中使用。

## 装饰器使用说明

* 当前@Styles仅支持[通用属性](../harmonyos-references/ts-component-general-attributes.md)和[通用事件](../harmonyos-references/ts-component-general-events.md)。
* @Styles可以定义在组件内或全局，在全局定义时需在方法名前面添加function关键字，组件内定义时则不需要添加function关键字。请参考用例[组件内styles和全局styles的用法](arkts-style.md#组件内styles和全局styles的用法)。
* 组件内@Styles的优先级高于全局@Styles。框架优先找当前组件内的@Styles，如果找不到，则会全局查找。

**说明** 

只能在当前文件内使用@Styles，不支持export。

若需要实现样式导出，推荐使用[AttributeModifier](arkts-user-defined-extension-attributemodifier.md)。

定义在组件内的@Styles可以通过this访问组件的常量和状态变量，并可以在@Styles里通过事件来改变状态变量的值，示例如下：

```typescript
@Entry
@Component
struct FancyUse {
  @State heightValue: number = 50;

  @Styles
  fancy() {
    .height(this.heightValue)
    .backgroundColor(Color.Blue)
    .onClick(() => {
      this.heightValue = 100;
    })
  }

  build() {
    Column() {
      // 通过fancy给Button提供样式设置
      Button('change height')
        .fancy()
    }
    .height('100%')
    .width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/ewYb4FksRh6OQK44BOc2QA/zh-cn_image_0000002736432327.gif)

## 限制条件

* @Styles方法不支持传入参数，编译期会报错。

```typescript
  // 错误写法： @Styles不支持参数，编译期报错
  @Styles
  function globalFancy (value: number) {
    .width(value)
  }
```

```typescript
// 正确写法
  @Styles
  function globalFancy () {
    .width(100)
  }
```

* 不支持在@Styles方法内使用条件渲染语句，条件渲染语句内的属性不生效。

```typescript
  // 错误写法
  @Styles
  function backgroundColorStyle() {
    if (true) {
      .backgroundColor(Color.Red)
    }
  }
```

```typescript
// 正确写法
  @Styles
  function backgroundColorStyle() {
    .backgroundColor(Color.Red)
  }
```

## 使用场景

### 组件内@Styles和全局@Styles的用法

```typescript
// 定义在全局的@Styles封装的样式
@Styles
function globalFancy1() {
  .width(150)
  .height(100)
  .backgroundColor(Color.Pink)
}

@Entry
@Component
struct GlobalFancy {
  @State heightValue: number = 100;

  // 定义在组件内的@Styles封装的样式
  @Styles
  fancy() {
    .width(200)
    .height(this.heightValue)
    .backgroundColor(Color.Gray)
    .onClick(() => {
      this.heightValue = 200;
    })
  }

  build() {
    Column({ space: 10 }) {
      // 使用全局的@Styles封装的样式
      Text('FancyA')
        .globalFancy1()
        .fontSize(30)
      // 使用组件内的@Styles封装的样式
      Text('FancyB')
        .fancy()
        .fontSize(30)
    }
    .width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/F5FOdX0GQTmkQMKwhbMzpA/zh-cn_image_0000002706833172.gif)
