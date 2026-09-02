---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethod-extraconfig
title: "@ohos.inputMethod.ExtraConfig (输入法扩展信息)"
breadcrumb: API参考 > 应用框架 > IME Kit（输入法开发服务） > ArkTS API > @ohos.inputMethod.ExtraConfig (输入法扩展信息)
category: harmonyos-references
scraped_at: 2026-09-02T15:01:34+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f56bfbf1cec0cfdc5859521ed227c5122bffa64c3d9059d4481832aeb4523796
---

@ohos.inputMethod.ExtraConfig模块提供输入法扩展信息的数据定义，支持ArkUI编辑框在拉起输入法时传递自定义配置信息给输入法应用。

本模块是输入法框架的扩展信息数据模块，定义了InputMethodExtraConfig接口和CustomValueType联合类型，用于承载编辑框应用向输入法应用传递的自定义键值对配置数据。

本模块提供编辑框应用向输入法应用传递个性化配置的能力。编辑框应用可将用户的输入习惯、快捷键设置、主题颜色、输入模式偏好等自定义信息以键值对形式封装，在绑定输入法时一并传递给输入法应用，使输入法应用据此提供个性化体验。信息总长度不超过32KB。

当编辑框应用需要向输入法应用传递额外的配置信息以定制输入行为时使用本模块。典型场景包括：聊天应用希望输入法默认展示表情面板、搜索应用希望输入法使用特定输入模式、笔记应用希望配置输入法的快捷键行为等。

**说明** 

本模块首批接口从API version 22开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块定义了以下关键Interface和数据类型：

| Interface/类型 | 说明 |
| --- | --- |
| InputMethodExtraConfig | 输入法扩展信息接口，包含customSettings属性，用于存储自定义键值对。这些键值对可以是任何与输入法相关的配置信息（如用户输入习惯、快捷键设置、主题颜色等），将在输入法应用绑定时加载，以提供个性化用户体验。信息总长度不超过32KB。 |
| CustomValueType | 扩展信息值的联合类型，支持number、string、boolean三种值类型，接口参数具体类型根据其功能而定。 |

本模块为纯数据定义模块，InputMethodExtraConfig作为数据类型需与其他模块的API组合使用。典型组合为：在TextInput控件的onWillAttachIME方法中，通过IMEClient.setExtraConfig将InputMethodExtraConfig传递给输入法应用，输入法应用侧通过@ohos.inputMethodEngine模块的EditorAttribute接收并处理该配置。

```javascript
// 以下为阐述调用逻辑的伪代码
@Entry
@Component
struct Index2 {
  // 1. 构造输入法扩展信息
  private extraConfig: InputMethodExtraConfig = {
    customSettings: {
      'inputMode': 'chat',
      'showEmojiPanel': true,
      'themeColor': 'dark',
      'autoCapitalize': false
    }
  };

  build() {
    Column() {
      TextInput()
        .onWillAttachIME((client: IMEClient): void => {
          client.setExtraConfig(this.extraConfig);
        })
    }
    .height('100%')
    .width('100%')
  }
}
```

## 导入模块

```ts
import { InputMethodExtraConfig } from '@kit.IMEKit';
```

## CustomValueType22+

type CustomValueType = number | string | boolean

表示扩展信息值的类型，接口参数具体类型根据其功能而定。开发者可根据配置项的含义选择合适的值类型：数值型配置（如字号大小、权重系数等）使用number；文本型配置（如输入模式名称、主题标识等）使用string；开关型配置（如是否启用某功能、是否展示某面板等）使用boolean。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 类型 | 说明 |
| --- | --- |
| number | 表示值类型为数字。 |
| string | 表示值类型为字符串。 |
| boolean | 表示值类型为布尔值。 |

## InputMethodExtraConfig

输入法扩展信息。用于编辑框应用向输入法应用传递自定义键值对配置数据，实现编辑框应用对输入法行为的个性化定制。

* 含义/功能：定义编辑框应用传递给输入法应用的自定义配置键值对，以Record<string, CustomValueType>形式存储。键（key）为配置项名称，值（value）为配置项内容，值类型支持number、string、boolean三种。
* 使用场景：当编辑框应用需要向输入法应用传递额外的个性化配置信息以定制输入行为时使用。例如：聊天应用希望输入法默认展示表情面板、搜索应用希望输入法使用特定输入模式、笔记应用希望配置输入法的快捷键行为等。
* 使用后效果：设置的扩展信息将在输入法应用与编辑框绑定时加载并传递给输入法应用，输入法应用可据此调整输入行为，提供个性化用户体验。若未设置扩展信息，输入法应用将使用默认配置。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| customSettings | Record<string, [CustomValueType](js-apis-inputmethod-extraconfig.md#customvaluetype22)> | 否 | 否 | 输入法扩展信息，用于存储自定义的键值对。这些键值对可以是任何与输入法相关的配置信息。例如用户的输入习惯、快捷键设置、主题颜色等。这些设置信息将在输入法应用绑定时加载，以提供个性化的用户体验。不设置时，输入法应用将使用默认配置。 |

customSettings参数使用建议：

* 取值范围：键（key）为任意非空字符串；值（value）的类型为[CustomValueType](js-apis-inputmethod-extraconfig.md#customvaluetype22)，即number、string或boolean。同一个键只能对应一个值。
* 规格限制：信息的总长度不超过32KB。当总长度超过32KB时，超出部分的信息将不被传递。开发者可通过计算所有键值对的JSON序列化长度来判断是否超出限制。
* 生效机制：扩展信息在编辑框应用通过@ohos.inputMethod模块的InputMethodController.attach()绑定输入法时生效，随TextConfig.extraConfig属性一并传递给输入法应用。未调用attach()或TextConfig中未设置extraConfig时，扩展信息不会被传递。
* 注意事项：
  + 开发建议：键名建议采用有意义的命名规范（如'inputMode'、'showEmojiPanel'），便于输入法应用解析和使用；避免使用过于简短或无意义的键名（如'a'、'x1'），以免降低可读性和可维护性。
  + 开发建议：键名应避免与输入法框架内部使用的键名冲突。建议使用应用专属前缀（如'com.example.chat.inputMode'）以防止命名冲突。
* 相关接口间的配合/制约关系：典型组合为在TextInput控件的onWillAttachIME方法中，通过IMEClient.setExtraConfig将InputMethodExtraConfig传递给输入法应用，输入法应用侧通过@ohos.inputMethodEngine模块的EditorAttribute接收并处理该配置。

**示例：**

```ts
// 以下代码需要在EntryAbility的page页面中执行
@Entry
@Component
struct Index2 {
  // 1. 构造输入法扩展信息
  private extraConfig: InputMethodExtraConfig = {
    customSettings: {
      'inputMode': 'chat',
      'showEmojiPanel': true,
      'themeColor': 'dark',
      'autoCapitalize': false
    }
  };

  build() {
    Column() {
      TextInput()
        .onWillAttachIME((client: IMEClient): void => {
          client.setExtraConfig(this.extraConfig);
        })
    }
    .height('100%')
    .width('100%')
  }
}
```
