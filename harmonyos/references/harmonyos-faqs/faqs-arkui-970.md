---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-970
title: 如何解决使用attributeModifier属性会导致防抖方法重复触发的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何解决使用attributeModifier属性会导致防抖方法重复触发的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:05+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:cf64cc579c6016114ccaad198366ff6555c259cbaabcda3808f0649fedc1ef76
---

## 问题现象

组件上同时绑定了onClick和attributeModifier时，点击时给onClick注册的防抖方法会重复触发，不使用attributeModifier属性时则不会。

问题代码如下：

```ts
function debounce(func: (event?: ClickEvent) => void, delay: number, immediate = true): (event?: ClickEvent) => void {
  console.info(`debounce wraped`)
  let timer: number = 0
  return (event?: ClickEvent) => {
    if (immediate && !timer) {
      func(event);
    }
    clearTimeout(timer);
    timer = setTimeout(() => {
      if (!immediate) {
        func(event);
      }
      timer = 0;
    }, delay);
  };
}

class YDItemClickStyles implements AttributeModifier<CommonAttribute> {
  constructor() {
  }

  applyPressedAttribute(instance: CommonAttribute): void {
    instance.backgroundColor(Color.Red);
  }
}

@Entry
@Component
struct Index {
  build() {
    Column() {

      Row() {
        Column() {
          Text('Click Me')
            .fontSize($r('app.float.page_text_font_size'))
            .fontWeight(FontWeight.Bold)
        }
        .attributeModifier(new YDItemClickStyles())
        .onClick(debounce(() => {
          console.info(`click: debounce in`)
        }, 200))
      }

    }
    .height('100%')
    .width('100%')
  }
}
```

未使用attributeModifier属性时，单次点击后只会打印一次click: debounce in：

```log
I     click: debounce in
```

使用attributeModifier属性时，单次点击后会打印两次debounce wraped和一次click: debounce in：

```log
I     debounce wraped
I     debounce wraped
I     click: debounce in
```

## 背景知识

[attributeModifier](../harmonyos-references/ts-universal-attributes-attribute-modifier.md#attributemodifier)是动态设置组件的属性方法。当点击操作发生时，会触发定义的[applyPressedAttribute](../harmonyos-references/ts-universal-attributes-attribute-modifier.md#applypressedattribute)方法，刷新组件状态。

## 问题定位

问题代码中debounce方法作为onClick的参数，在组件创建和刷新时就会触发，而onClick触发时会导致applyPressedAttribute方法触发，使得组件被刷新重建。

## 分析结论

applyPressedAttribute方法触发导致组件刷新时，debounce就会被调用。

## 修改建议

将防抖函数实例化，并将这个实例作为onClick的参数，防止其在组件刷新时被反复调用。

```ts
function debounce(func: (event?: ClickEvent) => void, delay: number, immediate = true): (event?: ClickEvent) => void {
  console.info(`debounce wraped`);
  let timer: number = 0;
  return (event?: ClickEvent) => {
    if (immediate && !timer) {
      func(event);
    }
    clearTimeout(timer);
    timer = setTimeout(() => {
      if (!immediate) {
        func(event);
      }
      timer = 0;
    }, delay);
  };
}

const handleDebouncedClick = debounce(() => {
  console.info(`click: debounce in`);
}, 200);

class YDItemClickStyles implements AttributeModifier<CommonAttribute> {
  constructor() {
  }

  applyPressedAttribute(instance: CommonAttribute): void {
    instance.backgroundColor(Color.Red);
  }
}

@Entry
@Component
struct DebounceTest {
  build() {
    Column() {

      Row() {
        Column() {
          Text('Click Me')
            .fontSize($r('app.float.page_text_font_size'))
            .fontWeight(FontWeight.Bold);
        }
        .attributeModifier(new YDItemClickStyles())
        .onClick(handleDebouncedClick);
      };

    }
    .height('100%')
    .width('100%');
  }
}
```
