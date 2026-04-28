---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-universal-attributes-accessibility
title: 无障碍开发指导
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 无障碍与适老化 > 无障碍开发指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:07+08:00
doc_updated_at: 2026-04-03
content_hash: sha256:f24b57cc9710429f997c0549b8811370d6845dbfcdd4bfbe684b5be125bc3d71
---

## 概述

无障碍服务是为保障所有人在任何情况下都能平等、便捷地获取和利用信息打造的系统级无障碍能力体系。其中为视障用户提供的屏幕朗读功能会将设备屏幕上的可见信息转化为语音播报，助力视障用户使用电子设备完成信息的获取和交互。

## 屏幕朗读

屏幕朗读可帮助视障用户在无需查看屏幕的情况下操作设备。[开启屏幕朗读](arkts-universal-attributes-accessibility.md#屏幕朗读操作指导)后，用户通过无障碍手势控制焦点移动，设备将实时语音播报焦点对应的详细信息。

### 能力范围

* 覆盖所有用户交互场景（如按钮点击、文本浏览、图表交互、动态内容更新）。
* 适用于Phone、Tablet设备。

### 亮点特征

1. 拓宽用户覆盖边界：适配屏幕朗读的应用，能精准触达数百万依赖辅助技术的视障用户，打破数字适用壁垒，让产品受众覆盖更全面。
2. 契合合规与设计规范：适配屏幕朗读是遵循全球无障碍设计标准的核心举措，既符合各国数字包容相关法规要求，也契合现代产品“人人可用”的设计理念。
3. 践行社会责任与品牌价值：适配屏幕朗读本质是促进数字公平的具体行动，彰显品牌尊重所有用户、助力无障碍环境建设的责任担当，提升品牌好感度。
4. 优化视障用户体验：在适配过程中聚焦核心体验优化，通过清晰的文本描述和操作提示，以及合理的焦点热区尺寸设计，为视障用户带来更流畅、更友好的使用体验。
5. 轻量级适配不影响核心体验：适配屏幕朗读无需改动应用核心逻辑或UI设计。在实现无障碍支持的同时，完全保留产品的创新特点与视觉风格。

### 屏幕朗读操作指导

支持通过三种方法开启屏幕朗读。

* 快捷手势开启：若已将辅助功能快捷键设置为屏幕朗读，同时长按音量上、下键，便能一键开启屏幕朗读。
* 设置开启：进入系统设置页面，在搜索栏输入“屏幕朗读”，点击功能对应开关，完成开启。
* 语音唤醒：直接通过小艺语音说出“开启屏幕朗读”，即可快速启用该功能。

启用屏幕朗读后，普通手势转为无障碍手势。无障碍手势支持在系统设置中的屏幕朗读->更多设置->自定义快捷手势中自定义，默认手势及对应行为如下。

**表1** 无障碍手势及对应行为

| 手势 | 行为 |
| --- | --- |
| 单指点击 | 单指点击元素，将触发元素的焦点聚焦并播报相关信息。例如单指单击桌面“设置”图标，聚焦后播报“设置，单指双击即可执行......”。 |
| 单指上下/左右滑动 | 单指上下/左右滑动，即可切换焦点至相邻元素。 |
| 单指双击 | 焦点聚焦目标元素后，在屏幕任意位置单指双击，即可触发该元素的点击操作。如聚焦“设置”图标后双击，便可打开设置应用。 |
| 单指双击并长按 | 聚焦目标元素后，单指双击并长按，即可激活元素普通手势下的长按操作。如长按应用图标，可弹出对应快捷操作菜单。 |
| 双指滑动 | 通过拖动操作，实现列表滑动或触发系统返回功能。 |

### 屏幕朗读聚焦原则

1. **浏览顺序**：焦点浏览遵循界面从上至下、从左至右的视觉布局顺序依次切换。
2. **聚焦范围**：仅支持对界面可见组件进行触摸、滑动聚焦，隐藏内容不纳入聚焦范围。
3. **焦点数量**：可视界面内有且仅有1个焦点。
4. **焦点热区大小**：焦点热区大小需合理设置，避免过小导致用户难以触摸感知，或过大遮挡其他无障碍节点、引发焦点丢失。
5. **默认焦点**：新应用界面、同应用新页面、新弹窗弹出时，自动聚焦至页面首个元素。

可以通过无障碍接口，实现上述聚焦原则。

**表2** 焦点控制及对应接口

| 功能 | 实现方案 |
| --- | --- |
| 浏览顺序控制 | 通过[accessibilityNextFocusId](../harmonyos-references/ts-universal-attributes-accessibility.md#accessibilitynextfocusid18)自定义焦点移动逻辑，明确指定焦点切换时的下一个聚焦组件。 |
| 聚焦范围控制 | - 对隐藏/非交互内容，通过[accessibilityLevel](../harmonyos-references/ts-universal-attributes-accessibility.md#accessibilitylevel)('no')禁止其被聚焦选中。  - 针对无实际节点的交互区域，通过[accessibilityVirtualNode](../harmonyos-references/ts-universal-attributes-accessibility.md#accessibilityvirtualnode11)配置虚拟节点作为焦点占位符。 |
| 保证有1个焦点 | 确保页面可见区域内始终有且仅有1个焦点，通过[sendAccessibilityEvent('requestFocusForAccessibility')](../harmonyos-references/js-apis-accessibility.md#accessibilitysendaccessibilityevent9)在无焦点时自动指定默认聚焦目标。 |
| 焦点热区大小 | - 焦点热区过小：建议将语义一致、操作热区更大的父组件通过[accessibilityGroup](../harmonyos-references/ts-universal-attributes-accessibility.md#accessibilitygroup)封装为整体焦点单元。  - 焦点热区过大：建议调整UI组件可聚焦热区范围，避免遮挡其他无障碍节点。 |

### 屏幕朗读播报原则

元素选中时，屏幕朗读会按照：组件状态→文本内容→组件类型→操作提示的优先级顺序组合播报内容，仅播报实际存在的属性内容。

上述4类播报元素均支持开发者自定义内容，如果需要修改某类属性的播报文案，可参照该属性对应的自定义接口进行配置，具体请参考表3。

**表3** 组件选中时基础播报内容配置

| 播报内容 | 配置方法 |
| --- | --- |
| 组件状态 | 通过[accessibilityChecked](../harmonyos-references/ts-universal-attributes-accessibility.md#accessibilitychecked13)、[accessibilitySelected](../harmonyos-references/ts-universal-attributes-accessibility.md#accessibilityselected13)配置组件选中状态的播报文案，如“已选中”、“未选中”。 |
| 文本内容 | 通过[accessibilityText](../harmonyos-references/ts-universal-attributes-accessibility.md#accessibilitytext)配置组件核心文本的朗读内容，如“首页”、“设置”。 |
| 组件类型 | 通过[accessibilityRole](../harmonyos-references/ts-universal-attributes-accessibility.md#accessibilityrole18)声明组件的类型标识，如“按钮”、“编辑框”。 |
| 操作提示 | 通过[accessibilityDescription](../harmonyos-references/ts-universal-attributes-accessibility.md#accessibilitydescription)定义组件的操作指引说明，如“单指双击即可播放”。 |

当焦点未切换，但需实时更新播报内容，如动态数据变更时，可以通过[sendAccessibilityEvent('announceForAccessibility')](../harmonyos-references/js-apis-accessibility.md#accessibilitysendaccessibilityevent9)主动播报接口实现。该接口适用于内容动态变化场景，播报实时变动的信息，如“已下载50%”。例如：

* 组件状态为“已选中”、文本内容为“首页”的焦点，屏幕朗读播报内容为：“已选中，首页”。
* 文本内容为“播放”、组件类型为“按钮”，操作提示为“单指双击即可执行”的焦点，屏幕朗读播报内容为：“播放，按钮，单指双击即可执行”。

## 无障碍属性开发指导

无障碍属性支持开发者自定义组件的状态、文本内容、组件类型及操作提示的无障碍播报文本，精准控制屏幕朗读的播报内容，提升无障碍场景下的使用体验。

| 功能 | 描述 |
| --- | --- |
| [自定义播报内容](arkts-universal-attributes-accessibility.md#设置无障碍文本) | 支持开发者自定义组件的状态、文本内容、组件类型及操作提示的无障碍播报文本，精准控制屏幕朗读的播报内容。 |
| [自定义聚焦](arkts-universal-attributes-accessibility.md#设置无障碍下一个焦点) | 支持自定义焦点组合、可聚焦性和浏览的顺序。 |
| [设置可滚动模式](arkts-universal-attributes-accessibility.md#设置可滚动模式) | 支持设置可滚动模式。 |
| [设置无障碍焦点绘制图层层级](arkts-universal-attributes-accessibility.md#设置无障碍焦点绘制图层层级) | 支持设置无障碍焦点绘制图层层级。 |

### 设置无障碍文本

[accessibilityText](../harmonyos-references/ts-universal-attributes-accessibility.md#accessibilitytext)是用于为组件配置核心无障碍文本内容的专属属性，核心作用是传递组件的关键信息，建议配置的文案简洁、精准且表意完整。

设置无障碍文本需遵循如下原则：

* 请勿在accessibilityText中设置组件状态（如“已选中”）、组件类型（如“按钮”）、操作提醒（如“单指双击即可执行”）等信息。屏幕朗读默认播报内容已包括这些属性，重复配置会导致播报内容冗余。
* 如果组件本身已有可视文本内容，且同时配置了accessibilityText，屏幕朗读将仅播报accessibilityText的内容，因此配置时请确保文案表意完整，无关键信息缺失。

以下将通过2个示例，对比展示如何为无默认文本的按钮配置accessibilityText，补充核心无障碍朗读信息。

说明

该示例运行，需在设备上提前[开启屏幕朗读](arkts-universal-attributes-accessibility.md#屏幕朗读操作指导)，否则无效果。

示例1：无默认文本的按钮，屏幕朗读播报内容为：“按钮，单指双击可执行”，用户无法通过语音播报感知此按钮的功能（播放）。

```
1. @Entry
2. @Component
3. export struct AccessibilityTextCase01 {
4. build() {
5. // ...
6. Column() {
7. Button()
8. .onClick(() => {
9. // 播放音频、视频的核心逻辑
10. })
11. }
12. // ...
13. }
14. }
```

示例2：在示例1的基础上，增加accessibilityText属性，屏幕朗读播报内容为：“播放，按钮，单指双击即可执行”，用户通过语音播报可以感知此按钮的功能。

```
1. @Entry
2. @Component
3. export struct AccessibilityTextCase02 {
4. build() {
5. // ...
6. Column() {
7. // 需确保resource/base/media目录下图标存在，可用其他图标替换演示。
8. Button()
9. .onClick(() => {
10. // 播放音频、视频的核心逻辑
11. })
12. .accessibilityText('播放') // 配置核心无障碍文本
13. }
14. // ...
15. }
16. }
```

### 设置无障碍提醒

[accessibilityDescription](../harmonyos-references/ts-universal-attributes-accessibility.md#accessibilitydescription)属性用于为组件提供操作提醒的说明，帮助用户理解将要执行的操作。例如系统默认的新手提醒不能表达的含义等场景。该信息在文本内容之后播报，并且如果当前控件有默认的新手提醒（如支持点击的组件，默认新手提醒为：单指双击即可执行）时，accessibilityDescription会替代系统的新手提醒，即仅播报accessibilityDescription内容。

关闭屏幕朗读的新手提醒开关后，accessibilityDescription内容也不会播报。

以下给出2个示例，对比介绍在Button组件中，如何设置无障碍提醒。

说明

该示例运行，需在设备上提前[开启屏幕朗读](arkts-universal-attributes-accessibility.md#屏幕朗读操作指导)，否则无效果。

示例1：以Button组件作为视频播放全屏按钮时，聚焦该按钮后屏幕朗读仅播报：“按钮，单指双击即可​执行​”，用户无法明确该操作的具体含义。

```
1. @Entry
2. @Component
3. export struct AccessibilityDescriptionCase01 {
4. build() {
5. // ...
6. Button()
7. .background(Color.Blue)
8. .onClick(() => {
9. // 全屏逻辑
10. })
11. // ...
12. }
13. }
```

示例2：在示例1基础上添加accessibilityDescription，聚焦按钮后屏幕朗读播报“按钮，单指双击即可全屏”，用户可明确操作意图。

```
1. @Entry
2. @Component
3. export struct AccessibilityDescriptionCase02 {
4. build() {
5. // ...
6. Button()
7. .background(Color.Blue)
8. .onClick(() => {
9. // 全屏逻辑
10. })
11. // 业务自定义提示信息
12. .accessibilityDescription('单指双击即可全屏') // 业务自定义提示信息
13. // ...
14. }
15. }
```

### 设置无障碍组件类型

[accessibilityRole](../harmonyos-references/ts-universal-attributes-accessibility.md#accessibilityrole18)属性用于为自定义组件设置无障碍角色类型，帮助用户理解当前操作组件的类型。例如使用Column、Row等基础组件自定义可点击组件时，若希望该组件被屏幕朗读播报为“按钮”，可将无障碍角色属性accessibilityRole设置为BUTTON。

以下给出2个示例，对比介绍如何自定义组件的无障碍角色类型。

说明

该示例运行，需在设备上提前[开启屏幕朗读](arkts-universal-attributes-accessibility.md#屏幕朗读操作指导)，否则无效果。

示例1：本示例以Column组件为例，由于该Column组件并非标准按钮组件，屏幕朗读仅会播报其文本内容“点赞”。

```
1. @Entry
2. @Component
3. export struct AccessibilityRoleCase01 {
4. build() {
5. // ...
6. Column() {
7. Text('点赞')
8. }
9. .onClick(() => {
10. // 业务逻辑
11. })
12. // ...
13. }
14. }
```

示例2：在示例1的基础上，为该Column组件设置accessibilityRole属性值为BUTTON（播报为“按钮”），屏幕朗读最终播报内容为：“点赞，按钮，单指双击即可执行”。

```
1. @Entry
2. @Component
3. export struct AccessibilityRoleCase02 {
4. build() {
5. // ...
6. Column() {
7. Text('点赞')
8. }
9. .onClick(() => {
10. // 业务逻辑
11. })
12. .accessibilityRole(AccessibilityRoleType.BUTTON)
13. // ...
14. }
15. }
```

### 设置无障碍节点是否被选中

[accessibilityChecked](../harmonyos-references/ts-universal-attributes-accessibility.md#accessibilitychecked13)和[accessibilitySelected](../harmonyos-references/ts-universal-attributes-accessibility.md#accessibilityselected13)是两个用于增强无障碍体验的属性，主要用于向屏幕朗读等屏幕朗读传达组件的选中状态。

在支持多选的情况下，设置无障碍节点是否被选中：

[accessibilityChecked](../harmonyos-references/ts-universal-attributes-accessibility.md#accessibilitychecked13)属性，用于表示组件在支持多选的情况下是否被勾选（如复选框、开关按钮等二态或三态组件），适用于需要明确“选中/未选中”语义的场景，支持以下值：

* undefined（默认）：由系统自动判断（依赖组件自身的状态，如Toggle组件的isOn属性）。
* false：未选中。
* true：选中（如复选框打勾）。

以下给出2个示例，介绍accessibilityChecked不同值的播报。

说明

该示例运行，需在设备上提前[开启屏幕朗读](arkts-universal-attributes-accessibility.md#屏幕朗读操作指导)，否则无效果。

示例1：本示例以Text组件为例，设置accessibilityChecked为true时，表示当前组件为被选中状态，当聚焦到“选项1”时，播报“已选中，选项1”。

```
1. @Entry
2. @Component
3. export struct AccessibilityCheckedCase01 {
4. build() {
5. // ...
6. Column() {
7. Text('选项1')
8. .accessibilityChecked(true)
9. }
10. // ...
11. }
12. }
```

示例2：本示例以Text组件为例，设置accessibilityChecked为false时，表示当前组件为未选中状态，当聚焦到“选项1”时，播报“未选中，选项1”。

```
1. @Entry
2. @Component
3. export struct AccessibilityCheckedCase02 {
4. build() {
5. // ...
6. Column() {
7. Text('选项1')
8. .accessibilityChecked(false)
9. }
10. // ...
11. }
12. }
```

在支持单选的情况下，设置无障碍节点是否被选中：

[accessibilitySelected](../harmonyos-references/ts-universal-attributes-accessibility.md#accessibilityselected13)属性，用于表示组件在支持单选的情况下是否被选择（如单选列表项、标签页等），适用于需要区分“当前选中项”的场景（如单选组、导航菜单），支持以下值：

* undefined（默认）：由系统自动判断。
* false：未选中。
* true：当前选中。

以下给出2个示例，介绍accessibilitySelected不同值的播报。

说明

该示例运行，需在设备上提前[开启屏幕朗读](arkts-universal-attributes-accessibility.md#屏幕朗读操作指导)，否则无效果。

示例1：本示例以Text组件为例，设置accessibilitySelected为true时，表示当前组件为被选中状态，当聚焦到“选项1”时，播报“已选中，选项1”。

```
1. @Entry
2. @Component
3. export struct AccessibilitySelectedCase01 {
4. build() {
5. // ...
6. Column() {
7. Text('选项1')
8. .accessibilitySelected(true)
9. }
10. // ...
11. }
12. }
```

示例2：本示例以Text组件为例，设置accessibilitySelected为false时，表示当前组件为未选中状态，当聚焦到“选项1”时，播报“选项1”。

```
1. @Entry
2. @Component
3. export struct AccessibilitySelectedCase02 {
4. build() {
5. // ...
6. Column() {
7. Text('选项1')
8. .accessibilitySelected(false)
9. }
10. // ...
11. }
12. }
```

在ArkUI无障碍属性中，[accessibilityChecked](../harmonyos-references/ts-universal-attributes-accessibility.md#accessibilitychecked13)和[accessibilitySelected](../harmonyos-references/ts-universal-attributes-accessibility.md#accessibilityselected13)均用于表示组件的状态，但二者应用场景与语义含义存在本质差异。以下是二者的对比：

**表4** accessibilityChecked与accessibilitySelected属性对比

| 属性 | [accessibilityChecked](../harmonyos-references/ts-universal-attributes-accessibility.md#accessibilitychecked13) | [accessibilitySelected](../harmonyos-references/ts-universal-attributes-accessibility.md#accessibilityselected13) |
| --- | --- | --- |
| 场景 | 复选框、开关等二态/三态组件。 | 单选列表、标签页等互斥选择场景。 |
| 语义目标 | 控件物理状态（如开关是否打开）。 | 导航焦点项（如列表当前选中项）。 |
| 状态持久性 | 通常需显式保存（如表单提交）。 | 临时性（随焦点移动变化）。 |
| 典型组件 | Checkbox，Toggle。 | List，Tabs。 |
| 播报内容 | true：“已选中”，false：“未选中” | true：“已选中”，false：不播报。 |

### 设置无障碍分组

[accessibilityGroup](../harmonyos-references/ts-universal-attributes-accessibility.md#accessibilitygroup)属性用于配置组件是否启用无障碍分组功能。若启用该功能，该组件及其所有子组件将被视为一个统一的无障碍节点处理，无障碍服务不会再单独识别和处理其下的子组件。该属性支持以下值：

* false（默认值）：不启用无障碍分组，子组件可被无障碍服务单独识别和聚焦。
* true：启用无障碍分组，组件及其所有子组件合并为一个无障碍节点，仅该父组件可被聚焦。

以下给出两个示例，对比介绍在Column组件中使用无障碍分组的作用。

说明

该示例运行，需在设备上提前[开启屏幕朗读](arkts-universal-attributes-accessibility.md#屏幕朗读操作指导)，否则无效果。

示例1：该场景下包含3个可被单独聚焦的Text子组件节点，用户无法连贯感知完整的时间信息，需多次聚焦才能获取全部内容。

```
1. @Entry
2. @Component
3. export struct AccessibilityGroupCase01 {
4. build() {
5. // ...
6. Column() {
7. Text('2026年')
8. Text('1月27日')
9. Text('星期二')
10. }
11. // ...
12. }
13. }
```

示例2：在示例1基础上为Column组件启用accessibilityGroup后，仅Column组件可被聚焦，其下所有Text文本会拼接为“2026年1月27日星期二”播报，且单个Text节点无法被单独聚焦。

```
1. @Entry
2. @Component
3. export struct AccessibilityGroupCase02 {
4. build() {
5. // ...
6. Column() {
7. Text('2026年')
8. Text('1月27日')
9. Text('星期二')
10. }
11. .accessibilityGroup(true)
12. // ...
13. }
14. }
```

### 设置无障碍重要性

[accessibilityLevel](../harmonyos-references/ts-universal-attributes-accessibility.md#accessibilitylevel)属性用于标识组件的无障碍重要性等级，核心作用是控制组件是否可被无障碍服务识别，该属性支持以下取值：

* 'auto'（默认）：由无障碍分组服务和ArkUI进行综合判断组件是否可被无障碍辅助服务所识别。
* 'yes'：当前组件可被无障碍辅助服务所识别。
* 'no'：当前组件不可被无障碍辅助服务所识别。
* 'no-hide-descendants'：当前组件及其所有子组件均不可被无障碍辅助服务所识别。

本示例以Text组件为例，为其设置Text.accessibilityLevel('yes')后，该组件可被屏幕朗读功能识别。若未配置该属性，“文本1”对应的Text组件无法被单独聚焦。

说明

该示例运行，需在设备上提前[开启屏幕朗读](arkts-universal-attributes-accessibility.md#屏幕朗读操作指导)，否则无效果。

```
1. @Entry
2. @Component
3. export struct AccessibilityLevelCase01 {
4. build() {
5. // ...
6. Column() {
7. Text('HelloWorld').fontSize(50).fontWeight(FontWeight.Bold)
8. }
9. .accessibilityGroup(true)
10. .accessibilityLevel('yes')
11. // ...
12. }
13. }
```

[AccessibilityText.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/master/ArkUISample/UIExtensionAndAccessibility/entry/src/main/ets/pages/UniversalAttributesAccessibility/AccessibilityText.ets#L41-L48)

### 设置无障碍虚拟子节点

[accessibilityVirtualNode](../harmonyos-references/ts-universal-attributes-accessibility.md#accessibilityvirtualnode11)属性主要用于为系统无法识别为无障碍节点的自绘制组件添加虚拟无障碍节点，使屏幕朗读可以聚焦并读取该节点的信息。

本示例以Column组件下的Text('文本1')模拟系统无法识别的自绘制组件，为Column设置accessibilityVirtualNode后，Text('文本2')会在Text('文本1')的位置进行无障碍节点占位，屏幕朗读即可聚焦到Text('文本2')并进行播报。

说明

该示例运行，需在设备上提前[开启屏幕朗读](arkts-universal-attributes-accessibility.md#屏幕朗读操作指导)，否则无效果。

```
1. @Entry
2. @Component
3. struct VirtualNodeExample {
4. @Builder customAccessibilityNode() {
5. Text('文本2')
6. .fontSize(50)
7. .fontWeight(FontWeight.Bold)
8. }

10. build() {
11. Column() {
12. Text('文本1')
13. .fontSize(50)
14. .fontWeight(FontWeight.Bold)
15. }
16. .accessibilityVirtualNode(this.customAccessibilityNode)
17. }
18. }
```

[VirtualNodeExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/master/ArkUISample/UIExtensionAndAccessibility/entry/src/main/ets/pages/UniversalAttributesAccessibility/VirtualNodeExample.ets#L16-L38)

### 设置无障碍下一个焦点

[accessibilityNextFocusId](../harmonyos-references/ts-universal-attributes-accessibility.md#accessibilitynextfocusid18)属性用于指定焦点移动过程中下一个被聚焦组件的id。建议开发者将聚焦顺序按照画面显示的自上而下、自左向右方向设置。若实际焦点移动顺序与视觉呈现顺序不一致，可通过此属性调整节点的聚焦顺序。

以下给出2个示例，对比介绍如何改变焦点遍历顺序。

说明

该示例运行，需在设备上提前[开启屏幕朗读](arkts-universal-attributes-accessibility.md#屏幕朗读操作指导)，否则无效果。

示例1：本示例中组件的视觉呈现顺序为“A->C->B->D”，焦点浏览顺序与视觉顺序一致，同样为“A->C->B->D”。

```
1. @Entry
2. @Component
3. export struct AccessibilityNextFocusIdCase01 {
4. build() {
5. // ...
6. Column() {
7. Button('A')
8. Button('C')
9. Button('B')
10. Button('D')
11. }
12. // ...
13. }
14. }
```

示例2：在示例1的基础上，通过accessibilityNextFocusId自定义焦点浏览顺序，最终走焦顺序为“A->B->C->D”

```
1. @Entry
2. @Component
3. export struct AccessibilityNextFocusIdCase02 {
4. build() {
5. // ...
6. Column() {
7. Button('A')
8. .accessibilityNextFocusId('b')
9. Button('C')
10. .id('c')
11. .accessibilityNextFocusId('d')
12. Button('B')
13. .id('b')
14. .accessibilityNextFocusId('c')
15. Button('D')
16. .id('d')
17. }
18. // ...
19. }
20. }
```

说明

* 避免焦点移动陷入死循环。例如为A配置accessibilityNextFocusId为B、为B配置该属性为A后，焦点移动顺序会变为A→B→A→B…，最终陷入死循环，适配无障碍功能时需避免此类情况。
* 非必要情况下，需避免出现节点无法被焦点遍历到的情况。例如组件树包含A、B、C、D、E组件，默认焦点移动顺序为A→B→C→D→E。若仅为B配置accessibilityNextFocusId为D，焦点移动顺序会变为A→B→D→E→A→B→D→E…，导致节点C始终无法被焦点遍历到。

### 设置可滚动模式

[accessibilityScrollTriggerable](../harmonyos-references/ts-universal-attributes-accessibility.md#accessibilityscrolltriggerable18)属性用于设置无障碍组件是否支持滚动触发操作。当用户通过滑动屏幕触发焦点移动时，若容器当前视觉可见范围内无可用的可聚焦组件，屏幕朗读功能会自动发起一次滚动操作。

* true（默认值）：启用自动滚动功能。
* false：不启用自动滚动功能。

以下给出2个示例，对比介绍如何通过配置accessibilityScrollTriggerable属性设置无障碍模式下的滚动触发状态。

说明

该示例运行，需在设备上提前[开启屏幕朗读](arkts-universal-attributes-accessibility.md#屏幕朗读操作指导)，否则无效果。

示例1：本示例以List组件为例，当焦点处于可见范围内列表的最后一个节点，如“第5项”时，若继续向下触发焦点移动，会触发列表的自动滚动，焦点将聚焦到原本不可见的内容节点“第6项”上。

```
1. @Entry
2. @Component
3. export struct AccessibilityScrollTriggerableCase01 {
4. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

6. build() {
7. // ...
8. Column() {
9. List({ space: 20, initialIndex: 0 }) {
10. ForEach(this.arr, (item: number) => {
11. ListItem() {
12. Text(`第${item}项`)
13. .width('100%')
14. .height(100)
15. .textAlign(TextAlign.Center)
16. }
17. }, (item: string) => item)
18. }
19. }
20. .width('100%')
21. .height('100%')
22. // ...
23. }
24. }
```

示例2：在示例1的基础上，为List组件配置accessibilityScrollTriggerable(false)后，当焦点处于可见范围内列表的最后一个节点，如“第5项”时，若继续向下触发焦点移动，将不再触发列表的自动滚动。若再次向下触发焦点移动，焦点会聚焦回页面的首个可聚焦节点。

```
1. @Entry
2. @Component
3. export struct AccessibilityScrollTriggerableCase02 {
4. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

6. build() {
7. // ...
8. Column() {
9. List({ space: 20, initialIndex: 0 }) {
10. ForEach(this.arr, (item: number) => {
11. ListItem() {
12. Text(`第${item}项`)
13. .width('100%')
14. .height(100)
15. .textAlign(TextAlign.Center)
16. }
17. }, (item: string) => item)
18. }
19. .accessibilityScrollTriggerable(false)
20. }
21. .width('100%')
22. .height('100%')
23. // ...
24. }
25. }
```

### 设置无障碍焦点绘制图层层级

[accessibilityFocusDrawLevel](../harmonyos-references/ts-universal-attributes-accessibility.md#accessibilityfocusdrawlevel19)属性用于设置无障碍焦点绿色边框的绘制层级；当标识焦点的绿色边框被更高Z序的图层遮挡覆盖时，可通过配置该属性提升其绘制层级的Z序，确保绿色边框能够清晰显示。

以下给出2个示例，对比介绍如何通过配置accessibilityFocusDrawLevel属性提升无障碍焦点绿色边框绘制的Z序。

说明

该示例运行，需在设备上提前[开启屏幕朗读](arkts-universal-attributes-accessibility.md#屏幕朗读操作指导)，否则无效果。

示例1：“文本1”按钮的焦点绿色边框被“文本2”按钮遮挡裁切，无法完整显示。

```
1. @Entry
2. @Component
3. export struct AccessibilityFocusDrawLevelCase01 {
4. build() {
5. // ...
6. Stack() {
7. Button('文本1')

9. Button('文本2')
10. .accessibilityLevel('no')
11. }
12. // ...
13. }
14. }
```

示例2：在示例1的基础上，为“文本1”按钮配置accessibilityFocusDrawLevel(FocusDrawLevel.TOP)后，该按钮的焦点绿色边框能够完整显示。

```
1. @Entry
2. @Component
3. export struct AccessibilityFocusDrawLevelCase02 {
4. build() {
5. // ...
6. Stack() {
7. Button('文本1')
8. .accessibilityFocusDrawLevel(FocusDrawLevel.TOP)

10. Button('文本2')
11. .accessibilityLevel('no')
12. }
13. // ...
14. }
15. }
```

## 无障碍方法开发指导

无障碍方法主要为开发者提供两类核心能力，主要包括ArkUI组件提供的[无障碍操作回调](../harmonyos-references/accessibility-related.md)以及无障碍服务提供的[状态查询方法](../harmonyos-references/js-apis-accessibility.md)。

本文中所有示例的效果验证，均需开启屏幕朗读后进行。

**表5** 无障碍方法主要功能

| 功能类别 | 方法/属性 | 说明 |
| --- | --- | --- |
| [无障碍焦点状态回调](arkts-universal-attributes-accessibility.md#无障碍焦点状态回调) | [onAccessibilityFocus](../harmonyos-references/ts-universal-accessibility-event.md#onaccessibilityfocus) | 监听组件获取或失去无障碍焦点的状态变化。 |
| [无障碍触屏事件回调](arkts-universal-attributes-accessibility.md#无障碍触屏事件回调) | [onAccessibilityHover](../harmonyos-references/ts-universal-accessibility-hover-event.md#onaccessibilityhover) | 监听单指触摸（悬停）操作，在屏幕朗读模式下触发。 |
| [无障碍点击事件回调](arkts-universal-attributes-accessibility.md#无障碍点击事件回调) | [onAccessibilityActionIntercept](../harmonyos-references/ts-universal-accessibility-event.md#onaccessibilityactionintercept20) | 无障碍点击操作回调，可以拦截消费该事件。 |
| [触摸浏览状态判断](arkts-universal-attributes-accessibility.md#开关状态查询及监听) | [on/off touchGuideStateChange](../harmonyos-references/js-apis-accessibility.md#accessibilityontouchguidestatechange) | 监听触摸浏览功能的启用/关闭状态变化。 |
| [主动聚焦](arkts-universal-attributes-accessibility.md#主动聚焦) | [sendAccessibilityEvent('requestFocusForAccessibility')](../harmonyos-references/js-apis-accessibility.md#accessibilitysendaccessibilityevent9) | 触发焦点的主动聚焦。 |
| [主动播报](arkts-universal-attributes-accessibility.md#主动播报) | [accessibility.sendAccessibilityEvent('announceForAccessibility')](../harmonyos-references/js-apis-accessibility.md#accessibilitysendaccessibilityevent9) | 触发焦点的主动播报。 |

### 无障碍焦点状态回调

[onAccessibilityFocus](../harmonyos-references/ts-universal-accessibility-event.md#onaccessibilityfocus)方法是用于监听组件无障碍焦点获取、失去焦点状态的回调函数，当组件的无障碍焦点状态发生变化时，会触发该回调函数执行。

本示例以Button组件为例，当焦点聚焦至Text组件时，该Button组件显示“未获焦”；当焦点聚焦至Button组件时，因触发onAccessibilityFocus回调且接收到的isFocus参数为true，Button组件的显示文本会被修改为“已获焦”。

```
1. @Entry
2. @Component
3. export struct OnAccessibilityFocusCase01 {
4. @State isFocus: boolean = false;

6. build() {
7. // ...
8. Column() {
9. Text('文本') // 聚焦到此组件时，下面焦点丢失，可验证未获焦状态。
10. Button(this.isFocus ? '已获焦' : '未获焦')
11. .onAccessibilityFocus((isFocus: boolean) => {
12. this.isFocus = isFocus
13. console.info(`current isFocus: ${this.isFocus}`)
14. })
15. }
16. // ...
17. }
18. }
```

### 无障碍触屏事件回调

[onAccessibilityHover](../harmonyos-references/ts-universal-accessibility-hover-event.md#onaccessibilityhover)方法提供对单指触摸操作的无障碍回调监听能力。

以下给出2个示例，对比介绍在开启屏幕朗读功能时，如何监听无障碍触屏事件。

示例1：本示例以Text组件为例，其默认显示文本为“无”。在无障碍读屏模式下，触摸该Text组件时，显示文本无任何变化。

```
1. @Entry
2. @Component
3. export struct OnAccessibilityHoverCase01 {
4. @State hoverText: string = '无';

6. build() {
7. // ...
8. Column() {
9. Text(this.hoverText)
10. .onTouch((event: TouchEvent) => {
11. this.hoverText = '上屏文字';
12. })
13. }
14. // ...
15. }
16. }
```

示例2：通过配置onAccessibilityHover回调函数修改hoverText变量后，当触摸到该Text组件时，其显示文本会变更为“上屏文字”。

```
1. @Entry
2. @Component
3. export struct OnAccessibilityHoverCase02 {
4. @State hoverText: string = '无';

6. build() {
7. // ...
8. Column() {
9. Text(this.hoverText)
10. .onTouch((event: TouchEvent) => {
11. this.hoverText = '上屏文字';
12. })
13. .onAccessibilityHover((isHover: boolean, event: AccessibilityHoverEvent) => {
14. // 模拟单击上屏
15. this.hoverText = '上屏文字';
16. })
17. }
18. // ...
19. }
20. }
```

### 无障碍点击事件回调

[onAccessibilityActionIntercept](../harmonyos-references/ts-universal-accessibility-event.md#onaccessibilityactionintercept20)方法提供无障碍控制操作的拦截回调能力，注册方可通过该回调决定是否拦截当前无障碍操作；若为不支持Click操作的组件注册该回调，则无法触发此回调函数。

以下给出2个示例，对比介绍如何配置onAccessibilityActionIntercept回调函数处理点击事件。

示例1：点击Toggle组件时会弹出弹框，屏幕朗读先播报“开启开关”，再播报弹框弹出的内容“确认开启”。由于间隔很短，导致“确认开启”的播报内容打断“开启开关”的播报。

```
1. @Entry
2. @Component
3. export struct AccessibilityActionInterceptCase01 {
4. @State isOn: boolean = false;

6. build() {
7. // ...
8. Column() {
9. Toggle({ type: ToggleType.Switch, isOn: this.isOn})
10. .onClick(() => {
11. this.getUIContext().showAlertDialog({
12. title: '',
13. message: this.isOn ? '确认关闭' : '确认开启?',
14. primaryButton: {
15. value: '确认',
16. action: () => {
17. this.isOn = !this.isOn;
18. }
19. },
20. secondaryButton: {
21. value: '取消',
22. action: () => {}
23. }
24. })
25. })
26. }
27. // ...
28. }
29. }
```

示例2：通过配置onAccessibilityActionIntercept回调函数，在组件内部消费点击事件后，Toggle被点击时，屏幕朗读不再播报“开启开关”/“关闭开关”，仅播报弹框内容“确认开启”/“确认关闭”。

```
1. @Entry
2. @Component
3. export struct AccessibilityActionInterceptCase02 {
4. @State isOn: boolean = false;

6. build() {
7. // ...
8. Column() {
9. Toggle({ type: ToggleType.Switch, isOn: this.isOn})
10. .onClick(() => {
11. })
12. .onAccessibilityActionIntercept((action: AccessibilityAction) => {
13. // ...
14. if (action == AccessibilityAction.ACCESSIBILITY_CLICK) {
15. this.getUIContext().showAlertDialog({
16. title: '',
17. message: this.isOn ? '确认关闭' : '确认开启?',
18. primaryButton: {
19. value: '确认',
20. action: () => {
21. this.isOn = !this.isOn;
22. }
23. },
24. secondaryButton: {
25. value: '取消',
26. action: () => {}
27. }
28. })
29. return AccessibilityActionInterceptResult.ACTION_INTERCEPT;
30. }
31. return AccessibilityActionInterceptResult.ACTION_CONTINUE;
32. })
33. }
34. // ...
35. }
36. }
```

### 主动聚焦

当页面无默认聚焦元素时，可通过调用[accessibility.sendAccessibilityEvent](../harmonyos-references/js-apis-accessibility.md#accessibilitysendaccessibilityevent9)方法，发送requestFocusForAccessibility类型的无障碍事件，强制将无障碍焦点聚焦至指定组件，以此提升视障用户的操作体验与效率。

以下给出2个示例，对比介绍如何通过调用sendAccessibilityEvent方法触发无障碍主动聚焦。

示例1：本示例以Button组件为例，当“文本1”按钮处于Visibility.Hidden状态时，页面会出现无障碍焦点丢失的问题，即页面无任何焦点。

```
1. @Entry
2. @Component
3. export struct SendAccessibilityEventCase01 {
4. @State isVisible: boolean = true;

6. build() {
7. // ...
8. Column() {
9. Button('文本1')
10. .visibility(this.isVisible ? Visibility.Visible : Visibility.Hidden)
11. .onClick((event: ClickEvent) => {
12. this.isVisible = false;
13. })

15. Button('文本2')
16. }
17. // ...
18. }
19. }
```

示例2：通过调用[accessibility.sendAccessibilityEvent](../harmonyos-references/js-apis-accessibility.md#accessibilitysendaccessibilityevent9)方法发送requestFocusForAccessibility类型的无障碍主动聚焦事件，在“文本1”按钮变为Visibility.Hidden时，主动聚焦到“文本2”按钮，保证页面至少有一个焦点。

```
1. import { accessibility } from '@kit.AccessibilityKit';

3. @Entry
4. @Component
5. export struct SendAccessibilityEventCase02 {
6. @State isVisible: boolean = true;

8. build() {
9. // ...
10. Column() {
11. Button('文本1')
12. .visibility(this.isVisible ? Visibility.Visible : Visibility.Hidden)
13. .onClick(() => {
14. this.isVisible = false;
15. const event: accessibility.EventInfo = {
16. type: "requestFocusForAccessibility",
17. // 需要替换为当前的工程名称
18. bundleName: "com.samples.uiextensionandaccessibility",
19. triggerAction: "common",
20. customId: '123'
21. }
22. accessibility.sendAccessibilityEvent(event);
23. })

25. Button('文本2')
26. .id('123') // 设置组件id
27. }
28. // ...
29. }
30. }
```

### 主动播报

需要触发动态播报时，可通过调用[accessibility.sendAccessibilityEvent](../harmonyos-references/js-apis-accessibility.md#accessibilitysendaccessibilityevent9)方法，发送announceForAccessibility类型的无障碍事件触发主动播报，以此提升视障用户的播报体验。

示例1：当Button组件的文本内容发生变化时，屏幕朗读不会重新播报内容，视障用户难以感知该按钮的功能已发生改变。

```
1. @Entry
2. @Component
3. export struct SendAccessibilityEventCase03 {
4. @State text: string = '暂停';
5. private isPlay: boolean = false;

7. build() {
8. // ...
9. Column() {
10. Button(this.text)
11. .onClick(() => {
12. this.isPlay = !this.isPlay;
13. this.text = this.isPlay ? '暂停' : '播放';
14. })
15. }
16. // ...
17. }
18. }
```

示例2：当Button组件的文本内容发生变化时，通过调用[accessibility.sendAccessibilityEvent](../harmonyos-references/js-apis-accessibility.md#accessibilitysendaccessibilityevent9)方法，发送announceForAccessibility类型的无障碍事件，触发屏幕朗读主动播报 “播放”/“暂停”，实现按钮文本内容变化与播报同步的效果。

```
1. import { accessibility } from '@kit.AccessibilityKit';

3. @Entry
4. @Component
5. export struct SendAccessibilityEventCase04 {
6. @State text: string = '暂停';
7. private isPlay: boolean = false;

9. build() {
10. // ...
11. Column() {
12. Button(this.text)
13. .onClick(() => {
14. this.isPlay = !this.isPlay;
15. this.text = this.isPlay ? '暂停' : '播放';
16. const event: accessibility.EventInfo = {
17. type: "announceForAccessibility",
18. // 需要替换为当前的工程名称
19. bundleName: "com.samples.uiextensionandaccessibility",
20. triggerAction: "common",
21. textAnnouncedForAccessibility: this.text,
22. }
23. accessibility.sendAccessibilityEvent(event);
24. })
25. }
26. // ...
27. }
28. }
```

## 开关状态查询及监听

无障碍支持监听和查询屏幕朗读开关和触摸浏览状态，接口及对应功能参考表6和表7。

**表6** 监听查询屏幕朗读开关状态

| 方法 | 功能 |
| --- | --- |
| [accessibility.on('screenReaderStateChange')](../harmonyos-references/js-apis-accessibility.md#accessibilityonscreenreaderstatechange18) | 监听屏幕朗读功能启用状态变化事件。 |
| [accessibility.off('screenReaderStateChange')](../harmonyos-references/js-apis-accessibility.md#accessibilityoffscreenreaderstatechange18) | 取消监听屏幕朗读功能启用状态变化事件。 |
| [accessibility.isScreenReaderOpenSync(): boolean](../harmonyos-references/js-apis-accessibility.md#accessibilityisscreenreaderopensync18) | 同步检测当前是否开启屏幕朗读模式。 |

**表7** 监听查询触摸浏览开关状态

| 方案 | 功能 |
| --- | --- |
| [accessibility.on('touchGuideStateChange')](../harmonyos-references/js-apis-accessibility.md#accessibilityontouchguidestatechange) | 监听触摸浏览功能启用状态变化事件。 |
| [accessibility.off('touchGuideStateChange')](../harmonyos-references/js-apis-accessibility.md#accessibilityofftouchguidestatechange) | 取消监听触摸浏览功能启用状态变化事件。 |
| [accessibility.isOpenTouchGuideSync()](../harmonyos-references/js-apis-accessibility.md#accessibilityisopentouchguidesync10) | 同步检测当前是否开启触摸浏览模式。 |
