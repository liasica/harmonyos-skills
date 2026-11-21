---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-customize-keyboard
title: 自定义键盘
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用文本 > 自定义键盘
category: harmonyos-guides
scraped_at: 2026-11-21T09:11:06+08:00
doc_updated_at: 2026-11-03
content_hash: sha256:09113eaeb4a9028c08a7fa390124faaeb4cf836b93c5b70f59799d53c77653bb
---

## 概述

自定义键盘是一种简易的键盘替代系统默认键盘，允许用户根据实际业务场景和习惯偏好，调整键盘的布局和位置、添加额外的功能键，使输入更加便捷和舒适，从而提升整体的用户体验。同时自定义键盘也可以增强用户输入的安全性，避免敏感信息被截取或者泄露。

本文将从以下几个方面介绍自定义键盘的实现和使用：

* [自定义键盘的实现](arkts-customize-keyboard.md#自定义键盘的实现)
* [自定义键盘和系统键盘的切换](arkts-customize-keyboard.md#自定义键盘和系统键盘的切换)
* [自定义键盘的布局避让](arkts-customize-keyboard.md#自定义键盘的布局避让)
* [自定义键盘实现防截屏](arkts-customize-keyboard.md#自定义键盘实现防截屏)

## 自定义键盘的实现

自定义键盘的实现包括以下几个步骤：

* [自定义键盘布局实现](arkts-customize-keyboard.md#自定义键盘布局实现)
* [输入控件绑定自定义键盘布局](arkts-customize-keyboard.md#输入控件绑定自定义键盘布局)
* [自定义键盘输入控制](arkts-customize-keyboard.md#自定义键盘输入控制)
* [自定义键盘光标控制](arkts-customize-keyboard.md#自定义键盘光标控制)
* [自定义键盘弹出与收起](arkts-customize-keyboard.md#自定义键盘弹出与收起)

### 自定义键盘布局实现

自定义键盘的布局以自定义组件的方式呈现，根据具体业务场景由开发者实现。自定义键盘的高度通过自定义组件根节点的[height](../harmonyos-references/ts-universal-attributes-size.md#height)属性设置，宽度不可设置，默认为屏幕宽度。

```ts
@Component
export struct CustomKeyboard {
  // ...
  build() {
    Column() {
      // ...
    }
    // ...
    .height(this.getKeyboardHeightVp())
    // ...
  }
}
```

以Grid方式实现数字键盘布局示例：

**图 1**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/R7hVg_kDSMafwmPuUXpaRA/zh-cn_image_0000002821756605.gif?HW-CC-KV=V1&HW-CC-Date=20261121T011106Z&HW-CC-Expire=31536000000&HW-CC-Sign=2019E101600F665529AA34E3434A4AD1BC986A323F6C6E4137B7E208E86FAF61)

```ts
@Component
export struct NumberKeyboard {
  @Consume inputText: string;
  @Consume keyboardController: KeyboardController;
  layoutOptions: GridLayoutOptions = {
    regularSize: [1, 1],
    irregularIndexes: [14, 16],
    onGetIrregularSizeByIndex: (index: number) => {
      if (index === 14) {
        return [2, 1];
      }
      return [1, 2];
    }
  };

  build() {
    Grid(undefined, this.layoutOptions) {
      ForEach(numberKeyboardData, (item: Menu) => {
        GridItem() {
          Button(item.text, { type: ButtonType.Normal })
            .fontColor(Color.Black)
            .backgroundColor(item.backgroundColor)
            .borderRadius(Constants.KEYBOARD_BUTTON_RADIUS)
            .fontSize(Constants.KEYBOARD_BUTTON_FONTSIZE_18)
            .padding(0)
            .width(item.width)
            .height(item.height)
            .onClick(() => {
              this.inputText = this.keyboardController.onInput(item.text);
            })
        }
      }, (item: Menu) => JSON.stringify(item))
    }
    .columnsTemplate('1fr 1fr 1fr 1fr 1fr')
    .rowsGap($r('app.float.number_keyboard_grid_gap'))
    .columnsGap($r('app.float.number_keyboard_grid_gap'))
  }
}
```

### 输入控件绑定自定义键盘布局

输入控件（TextArea、TextInput、RichEditor、Search）支持通过[customKeyboard](../harmonyos-references/ts-basic-components-textinput.md#customkeyboard10)属性绑定自定义键盘布局。绑定自定义键盘后，输入控件获取焦点时，不会拉起系统键盘，而是加载指定的自定义键盘。本文后续以TextInput控件为例进行介绍。

**图 2**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/PasDcxOFRqafgizz9pXYkA/zh-cn_image_0000002793036668.gif?HW-CC-KV=V1&HW-CC-Date=20261121T011106Z&HW-CC-Expire=31536000000&HW-CC-Sign=3F7DCE9C089313BF8C48FA32336A9C8B8CE8EF54598F94FBD967293CD6A82B99)

代码示例如下：

```ts
  build() {
    Column() {
      TextInput({
        placeholder: 'Bind Custom Keyboard',
        text: this.inputText,
        controller: this.textInputController
      })
        // ...
        .customKeyboard(this.isCustomKeyboardAttach ? this.customKeyboard() : null)
          // ...
    }
  }
  @Builder
  customKeyboard() {
    CustomKeyboard()
  }
}
```

### 监听键盘弹出与收起

在输入组件内,使用@Link和@Watch('onChangeKeyboard')修饰isKeyboardShown；

当键盘状态变化后,会调用onChangeKeyboard,此时要收起键盘,则执行和键盘控制器绑定的文字输入控制器的[stopEditing()](../harmonyos-references/ts-text-common.md#stopediting12)方法。

```ts
@Component
export struct TextInputComponent {
  // ...
  @Link @Watch('onChangeKeyboard') isKeyboardShown: boolean;
  // ...
  onChangeKeyboard() {
    if (this.isKeyboardShown === false) {
      this.textInputController.stopEditing();
    }
  }

  // ...
}
```

输入组件内有两个事件：

[onFocus()](../harmonyos-references/ts-universal-focus-event.md#onfocus)代表获得焦点,用户点击输入组件的时候,输入组件会获得焦点从而弹出键盘,此时设定isKeyboardShown为true,表示弹起;

[onBlur()](../harmonyos-references/ts-universal-focus-event.md#onblur)代表失去焦点,当输入组件失去焦点,会被调用, 此时设为isKeyboardShown为false,表示收起;

```ts
.onBlur(() => {
  this.isKeyboardShown = false;
  // ...
})
.onFocus(() => {
  this.isKeyboardShown = true;
  // ...
})
```

页面内的isKeyboardShown要和输入组件TextInputComponent建立双向绑定,用来监听isKeyboardShown变化,响应键盘的弹出与收起.

```ts
@Entry
@Component
struct MainPage {
  // ...
  @State isKeyboardShown: boolean = false;
  // ...
  build() {
    Navigation() {
      Column() {
        // ...
      }
      // ...
    }
    .onClick(() => {
      if (this.isKeyboardShown) {
        this.isKeyboardShown = false;
      }
    })
    .mode(NavigationMode.Stack)
    .titleMode(NavigationTitleMode.Full)
    .title($r('app.string.main_page_title'))
  }
}
```

## 在横竖屏切换时设置键盘高度

在键盘组件CustomKeyboard.ets引入方向检测与动态高度，在键盘组件内对应位置处理。

引入[@ohos.display (屏幕属性)](../harmonyos-references/js-apis-display.md)，新增@State isLandscape保存当前方向。

在aboutToAppear注册监听器display.on('change') ，在aboutToDisappear注销监听器，方向变化时调用updateOrientation(), 通过 [display.getDefaultDisplaySync()](../harmonyos-references/js-apis-display.md#displaygetdefaultdisplaysync9)判断width > height判定横屏。

```ts
@Component
export struct CustomKeyboard {
  // ...

  aboutToAppear(): void {
    this.updateOrientation();
    try {
      display.on('change', this.onDisplayChange);
    } catch (e) {
    }
  }

  aboutToDisappear(): void {
    try {
      display.off('change', this.onDisplayChange);
    } catch (e) {
    }
  }

  private updateOrientation() {
    try {
      const d = display.getDefaultDisplaySync();
      this.isLandscape = d.width > d.height;
    } catch (e) {
      this.isLandscape = false;
    }
  }
  // ...
}
```

重写getKeyboardHeightVp()，判断设备为平板的时候，按照平板的比例给予横屏0.33、竖屏0.22的屏幕高度占比，手机的话固定为0.36的占比高度。

```ts
@Component
export struct CustomKeyboard {
  // ...

  private getKeyboardHeightVp(): number | Resource {
    try {
      const d = display.getDefaultDisplaySync();
      const ui = this.getUIContext();
      const screenHeightVp = ui.px2vp(d.height);
      const shortSideVp = ui.px2vp(Math.min(d.width, d.height));
      const isLargeScreen = shortSideVp >= 600;
      const ratio = isLargeScreen
          ? (this.isLandscape ? 0.33 : 0.22)
          :  0.36;
  
      return Math.floor(screenHeightVp * ratio);
    } catch (e) {
      return $r('app.float.keyboard_total_height');
    }
  }
  // ...
}
```

修改组件高度，将键盘组件的.height(...) 改为.height(this.getKeyboardHeightVp())以采用动态计算值。

```ts
@Component
export struct CustomKeyboard {
  // ...
  build() {
    // ...
    // ...
    .padding({ left: $r('app.float.keyboard_padding'), right: $r('app.float.keyboard_padding') })
    .height(this.getKeyboardHeightVp())
    .width('100%')
    .backgroundColor($r('app.color.keyboard_background_color'))
  }
}
```

### 自定义键盘输入控制

自定义键盘可以拦截手势事件，通过对状态变量的修改，实现文本的输入。

**图 3**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/SC9KoglcT92XpCt1mUmsgQ/zh-cn_image_0000002792876700.gif?HW-CC-KV=V1&HW-CC-Date=20261121T011106Z&HW-CC-Expire=31536000000&HW-CC-Sign=59E82CA3211DD1CE0F61AB13DFA55C845A2662C0A696C2E1098566C64CEAA594)

以英文键盘为例，监听EnglishButton的onClick事件，修改状态变量。

```ts
@Component
struct EnglishButton {
  @Consume inputText: string;
  // ...

  build() {
    Button({ type: ButtonType.Normal })
    // ...
    .onClick(() => {
      this.inputText = this.keyboardController.onInput(this.getEnglishText(this.item));
    })
  }
}
```

通过对状态变量inputText的修改，实现文本输入。

```ts
@Component
export struct TextInputComponent {
  @Provide inputText: string = '';
  // ...
  build() {
    Column() {
      TextInput({
        placeholder: 'Bind Custom Keyboard',
        text: this.inputText,
        controller: this.textInputController
      })
        // ...
    }
  }
  // ...
}
```

### 自定义键盘光标控制

通过监听TextInput的[onTextSelectionChange()](../harmonyos-references/ts-basic-components-textinput.md#ontextselectionchange10)生命周期，获取初始光标位置，文本输入后，调用TextInputController的[caretPosition](../harmonyos-references/ts-basic-components-textinput.md#caretposition8)方法，设置最终光标位置。

**图 4**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/VCc6JBCATHa5oU1CdZcy2w/zh-cn_image_0000002821836605.gif?HW-CC-KV=V1&HW-CC-Date=20261121T011106Z&HW-CC-Expire=31536000000&HW-CC-Sign=95AAC818B287097610B8850ACD57749F5C60E97B97522371321E3707FA66F2D0)

获取光标位置：

```ts
TextInput({
  placeholder: 'Bind Custom Keyboard',
  text: this.inputText,
  controller: this.textInputController
})
  // ...
  .onTextSelectionChange((start: number, end: number) => {
    this.keyboardController.setCaretPosition(start, end);
  })
    // ...
```

设置光标位置：

```ts
onChange(value: string) {
  this.text = value;
  if (this.keyboardType !== 'System') {
    this.textInputController?.caretPosition(this.targetCaretPos);
  }
}
```

### 自定义键盘弹出与收起

通过对焦点进行控制，可以实现键盘的弹出和收起，参考[软键盘的弹出收起和监听](../best-practices/bpta-keyboard-layout-adapt.md#section117216355229)。

开发者也可以通过TextInputController的[stopEditing()](../harmonyos-references/ts-basic-components-textinput.md#stopediting10)方法控制键盘关闭，下面的自定义键盘示例中，点击确认按键关闭自定义键盘。

**图 5**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/JxQoHRCvShue14vOD9-Cxw/zh-cn_image_0000002821756607.gif?HW-CC-KV=V1&HW-CC-Date=20261121T011106Z&HW-CC-Expire=31536000000&HW-CC-Sign=6444DBE015F7E7D5AE0888F380A4FF83F4251B559AD244EC19D1E4D058D92C24)

```ts
onInput(value: string | Resource): string {
  // ...

  switch (value.id) {
    // ...
    case $r('app.string.keyboardButton_finish').id:
      this.textInputController?.stopEditing();
      break;
  // ...
  }
  return this.text;
}
```

## 自定义键盘和系统键盘的切换

当需要实现同一个输入框内可以切换自定义键盘和系统键盘时，可以通过如下方式实现：

Tab栏点击“123”、“ABC”按钮，this.isCustomKeyboardAttach为true，TextInput绑定自定义键盘；点击“中文”按钮，this.isCustomKeyboardAttach为false，切换系统键盘。

**图 6**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/MjfKA5jRTOKfelQvi6vmXA/zh-cn_image_0000002793036670.gif?HW-CC-KV=V1&HW-CC-Date=20261121T011106Z&HW-CC-Expire=31536000000&HW-CC-Sign=D6E41834FD0B9EDE19B4F131DE909C75068F6E4D39F4AEF34C9FFF42946C1268)

```ts
TextInput({
  placeholder: 'Bind Custom Keyboard',
  text: this.inputText,
  controller: this.textInputController
})
  // ...
  .customKeyboard(this.isCustomKeyboardAttach ? this.customKeyboard() : null)
```

## 自定义键盘的布局避让

### 使用系统提供的自定义键盘避让功能

为了确保输入框不被自定义键盘挡住，系统默认提供了输入框避让自定义键盘的能力。在TextInput组件的[customKeyboard](../harmonyos-references/ts-basic-components-search.md#customkeyboard10)属性设置[supportAvoidance](../harmonyos-references/ts-basic-components-richeditor.md#keyboardoptions12)为true，开启系统提供的自定义键盘避让功能。键盘的避让机制和常见问题的解决方法，可以参考[软键盘避让机制](../best-practices/bpta-keyboard-layout-adapt.md#section08221814182316)。

**图 7**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/1OhApZ7eQGGW-fptVlYdBg/zh-cn_image_0000002792876702.gif?HW-CC-KV=V1&HW-CC-Date=20261121T011106Z&HW-CC-Expire=31536000000&HW-CC-Sign=EF3A35E8982FA5F43C280C8191B26D1FC38DAF748CF9BACDA00573289D688768)

```ts
TextInput({
  placeholder: 'Bind Custom Keyboard',
  text: this.inputText,
  controller: this.textInputController
})
  .customKeyboard(this.customKeyboard(), { supportAvoidance: true })
    // ...
```

系统默认的自定义键盘避让功能只能保证输入框不被遮挡，输入框下方的组件可能会被自定义键盘挡住，如上图中所示，输入框下方的tab栏被自定义键盘挡住。为解决这一问题，需要开发者自己实现自定义键盘的避让功能。

### 开发者自己实现自定义键盘的避让功能

开发者需要监听自定义键盘根节点的onAreaChange()生命周期，获取自定义键盘的高度，根据实际场景设置布局的避让。

**图 8**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/Uxo8sYV_TvKk01ewUjo-jQ/zh-cn_image_0000002821836607.gif?HW-CC-KV=V1&HW-CC-Date=20261121T011106Z&HW-CC-Expire=31536000000&HW-CC-Sign=FF79C3AF695BC49EE3EE311F31483D325FC4198EA282C57386C889B82E2FA8EB)

监听自定义键盘布局的[onAreaChange()](../harmonyos-references/ts-universal-component-area-change-event.md#onareachange)生命周期，通过newValue.height获取自定义键盘弹出时的高度，根据实际业务场景计算布局避让高度avoidHeight。

```ts
@Component
export struct CustomKeyboard {
  // ...
  build() {
    Column() {
      // ...
    }
    .onAreaChange((oldValue: Area, newValue: Area) => {
      this.customKeyboardHeight = Number(newValue.height);
      let avoidHeight: number = (this.isCustomKeyboardAttach ? this.customKeyboardHeight : this.systemKeyboardHeight)
        - this.bottomRectHeight;
      this.keyboardController.changeAvoidHeight(avoidHeight);
    })
    // ...
  }
}
```

通过emitter（详见[@ohos.events.emitter (Emitter)](../harmonyos-references/js-apis-emitter.md)）的方式，发送自定义键盘高度变化的通知。

```ts
changeAvoidHeight(value: number) {
  let event: emitter.InnerEvent = {
    eventId: Constants.AVOID_EVENT_ID
  };
  let eventData: emitter.EventData = {
    data: {
      'avoidHeight': value
    }
  };
  emitter.emit(event, eventData);
}
```

接收到高度变化通知后，根据实际业务场景，设置页面的避让高度。

```ts
@Entry
@Component
struct MainPage {
  @State bottomPadding: number = 210;
  @State isKeyboardShown: boolean = false;
  aboutToAppear(): void {
    let event: emitter.InnerEvent = {
      eventId: 1
    }
    emitter.on(event, (eventData: emitter.EventData) => {
      if (eventData.data) {
        let avoidHeight: number = eventData.data['avoidHeight'];
        if (avoidHeight === 0) {
          this.bottomPadding = 210;
        } else {
          this.bottomPadding = avoidHeight;
        }
      }
    })
  }
  build() {
    Navigation() {
      Column() {
        // ...
      }
      .padding({ bottom: this.bottomPadding })
      // ...
    }
    .onClick(() => {
      if (this.isKeyboardShown) {
        this.isKeyboardShown = false;
      }
    })
    .mode(NavigationMode.Stack)
    .titleMode(NavigationTitleMode.Full)
    .title($r('app.string.main_page_title'))
  }
}
```

## 自定义键盘实现防截屏

用户使用自定义键盘输入敏感信息时，可以设置禁止截屏，有效防止他人在未经许可的情况下获取用户的敏感信息，从而保护用户的隐私安全。具体实现参考[如何实现防截屏功能](../doccenter-dev-faq/arkui-uimana-faq-0010.md)。

## 示例代码

* [实现自定义键盘功能](https://gitcode.com/harmonyos_samples/CustomizeKeyboard)
