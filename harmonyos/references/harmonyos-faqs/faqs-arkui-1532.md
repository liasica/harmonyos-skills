---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1532
title: 如何解决attributeModifier常见报错问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何解决attributeModifier常见报错问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:11+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ba20ce602c2b1a7c3dfe27ac22ce86569fdb1873d22611eab1c67658654d0c60
---

## 问题现象

使用attributeModifier时程序崩溃，报以下几种错误：

* 场景一：Error message:Cannot read property observeComponentCreation2 of undefined。

  ```ts
  class NavigationModifier implements AttributeModifier<NavigationAttribute> {
    applyNormalAttribute(instance: NavigationAttribute): void {
      instance.title({ builder: mainToolbarLayout(), height: 60 }); // 此处入参为CustomBuilder
    }
  }

  @Builder
  function mainToolbarLayout() {
    Row() {
      Text('ceshi');
      Blank();
      Image($r('app.media.startIcon'))
        .width(20)
        .height(20)
        .objectFit(ImageFit.Contain);
    }.padding({ left: 12, right: 12 })
    .height('100%').width('100%');
  }
  ```
* 场景二：Error message:undefined is not callable。

  ```ts
  class TextModifier implements AttributeModifier<TextAttribute> {
    applyNormalAttribute(instance: TextAttribute): void {
      instance.hitTestBehavior(HitTestMode.Default)
        .copyOption(CopyOptions.InApp)
        // bindSelectionMenu第二个入参为CustomBuilder
        .bindSelectionMenu(TextSpanType.TEXT, longPressEmptyMenu, TextResponseType.LONG_PRESS);
    }
  }

  @Builder
  function longPressEmptyMenu() {
    // 需要让Menu组件为空，才能达到长按选中但不出现默认菜单的效果
    Column() {
      Menu() {
      };
    };
  }
  ```

## 背景知识

ArkUI支持动态属性设置，可通过组件的通用方法[attributeModifier](../harmonyos-references/ts-universal-attributes-attribute-modifier.md#attributemodifier)设置组件的多态样式，在使用此方法时，开发者需要自定义class实现attributeModifier接口。

注意：在attributeModifier中设置的属性尽量不要与其他方法设置的属性相同，避免在页面刷新时attributeModifier不生效。

组件的部分属性不支持在attributeModifier中设置：

* 不支持入参或者返回值为CustomBuilder的属性。
* 不支持入参为modifier类型的属性，具体为以下属性方法：attributeModifier，drawModifier和gestureModifier。
* 不支持animation属性、gesture类型的属性、stateStyles属性以及已废弃属性。

## 解决方案

* 场景一：用NavigationAttribute把Navigation的title整理成一个公共的动态属性时，程序报错闪退。

  原因：不支持入参或者返回值为CustomBuilder的属性。Navigation的[title](../harmonyos-references/ts-basic-components-navigation.md#title)方法支持CustomBuilder参数。

  修改建议：直接在组件尾部调用属性或使用[@Extend](../harmonyos-guides/arkts-extend.md)封装。

  ```ts
  @Component
  struct SceneOne {
    build() {
      Navigation() {
      }
      .title({ builder: mainToolbarLayout(), height: 60 })
      .height('100%')
      .width('100%');
    }
  }
  ```
* 场景二：Text组件使用attributeModifier绑定bindSelectionMenu崩溃，程序报错闪退。

  原因：不支持入参或者返回值为CustomBuilder的属性。Text的[bindSelectionMenu](../harmonyos-references/ts-basic-components-text.md#bindselectionmenu11)方法第二个入参为CustomBuilder类型。

  修改建议：直接在组件尾部调用属性或使用[@Extend](../harmonyos-guides/arkts-extend.md)封装。

  ```ts
  @Component
  struct SceneTwo {
    build() {
      Text('hello world')
        .textExt();
    }
  }

  @Extend(Text)
  function textExt() {
    .bindSelectionMenu(TextSpanType.TEXT, longPressEmptyMenu, TextResponseType.LONG_PRESS);
  }
  ```

完整代码如下：

```ts
@Entry
@Component
struct AttributeModifierDemo {
  build() {
    Column() {
      SceneOne();
      SceneTwo();
    };
  }
}

@Component
struct SceneOne {
  build() {
    Navigation() {
    }
    .title({ builder: mainToolbarLayout(), height: 60 })
    .height('100%')
    .width('100%');
  }
}

@Component
struct SceneTwo {
  build() {
    Text('hello world')
      .textExt();
  }
}

@Extend(Text)
function textExt() {
  .bindSelectionMenu(TextSpanType.TEXT, longPressEmptyMenu, TextResponseType.LONG_PRESS);
}

@Builder
function mainToolbarLayout() {
  Row() {
    Text('ceshi');
    Blank();
    Image($r('app.media.startIcon'))
      .width(20)
      .height(20)
      .objectFit(ImageFit.Contain);
  }.padding({ left: 12, right: 12 })
  .height('100%').width('100%');
}

@Builder
function longPressEmptyMenu() {
  // 需要让Menu组件为空，才能达到长按选中但不出现默认菜单的效果
  Column() {
    Menu() {
    };
  };
}
```

## 常见FAQ

Q：上述场景二这种需要封装自定义组件给多个地方使用，attributeModifier不支持bindSelectionMenu属性，应该如何从外部指定呢？

A：使用[@Extend](../harmonyos-guides/arkts-extend.md)封装bindSelectionMenu属性在当前文件内作为公共组件使用，但不支持export导出在其它文件中使用，若是跨文件使用则需重新定义。

Q：设置HdsNavigation的titleBar时，入参中没有填入CustomBuilder，也会报错“undefined is not callable”，为什么？

A：HdsNavigation的titleBar中包含了类型为CustomBuilder的可选参数，因此不支持在动态属性中使用，即使使用过程中没有填入CustomBuilder也会有相应报错。

Q：在API19环境下，attributeModifier使用onVisibleAreaChange属性导致闪退，报错Method not implemented。

A：报错Method not implemented，说明该属性当前不支持attributeModifier。从API20开始，onVisibleAreaChange该接口支持在attributeModifier中调用。

## 总结

在使用attributeModifier遇错时，可以按照以下步骤排查：

1. 检查Attribute是否可以使用attributeModifier封装。详细可查阅[applySelectedAttribute](../harmonyos-references/ts-universal-attributes-attribute-modifier.md#applyselectedattribute)文档下方描述的instance参数支持范围。
2. 判断是否使用了不支持或者未实现的属性。详细可查阅[属性或事件对attributeModifier的支持情况](../harmonyos-guides/arkts-user-defined-extension-attributemodifier.md#属性或事件对attributemodifier的支持情况)。
3. 对于不在2中所列举，但是报错的属性，可以查看此属性详细介绍，判断是否属于背景知识中所列举的不支持情况。

对于无法使用attributeModifier封装的属性，需要在每个组件尾部直接调用属性方法，也可以尝试使用[@Styles装饰器](../harmonyos-guides/arkts-style.md)和[@Extend装饰器](../harmonyos-guides/arkts-extend.md)实现类似attributeModifier的封装效果。
