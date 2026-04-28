---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-231
title: 自定义组件如何实现类似系统组件的链式调用
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 自定义组件如何实现类似系统组件的链式调用
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:00+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:0f795b14cf2b7ae9f97dda89df03bfbe79cf82092e7dc840742cb7e22311da31
---

目前ArkTS语法不支持这种链式调用，组件本身无法像普通对象一样调用方法，只能在组件声明时通过参数传递回调方法来修改组件的参数，无法直接使用链式调用来实现。若需要在自定义组件内实现类似系统组件的链式调用，推荐使用modifier用法，示例代码如下：

```
1. @Entry
2. @Component
3. struct CustomComponentChainCall {
4. @Styles
5. pressedStyles() {
6. .backgroundColor(Color.Blue)
7. }

9. build() {
10. Column() {
11. CustomSysComp({
12. textInputModifier: new MyTextInputModifier()
13. .backgroundColor(Color.Blue)
14. .placeholderColor(Color.Red),
15. buttonModifier: new MyButtonModifier()
16. .opacity(0.5)
17. .backgroundColor(Color.Orange)
18. })
19. .width('100%')
20. .height(400)
21. }
22. .width('100%')
23. .height('100%')
24. }
25. }

27. @Component
28. struct CustomSysComp {
29. // Set custom TextInput.
30. textInputModifier: MyTextInputModifier = new MyTextInputModifier();
31. // Set custom Button.
32. buttonModifier: MyButtonModifier = new MyButtonModifier();

34. build() {
35. Column() {
36. TextInput({ placeholder: 'placeholder' })
37. .attributeModifier(this.textInputModifier)
38. Button('button')
39. .attributeModifier(this.buttonModifier)
40. }
41. .width('100%')
42. .height('100%')
43. }
44. }

46. // The provider creates custom classes to implement the system AttributeModifier interface.
47. export class MyTextInputModifier implements AttributeModifier<TextInputAttribute> {
48. // Default Attributes
49. private mWidth: Length = '100%';
50. private mHeight: Length = 100;
51. // custom attribute
52. private mPlaceholderColor: ResourceColor = Color.Gray;

54. placeholderColor(placeholderColor: ResourceColor): MyTextInputModifier {
55. this.mPlaceholderColor = placeholderColor;
56. return this;
57. }

59. private mBackgroundColor: ResourceColor = Color.Orange;

61. backgroundColor(backgroundColor: ResourceColor): MyTextInputModifier {
62. this.mBackgroundColor = backgroundColor;
63. return this;
64. }

66. applyNormalAttribute(instance: TextInputAttribute): void {
67. instance.width(this.mWidth);
68. instance.height(this.mHeight);
69. instance.placeholderColor(this.mPlaceholderColor);
70. instance.backgroundColor(this.mBackgroundColor);
71. }
72. }

74. // The provider creates custom classes to implement the system AttributeModifier interface.
75. export class MyButtonModifier implements AttributeModifier<ButtonAttribute> {
76. // Default Attributes
77. private mWidth: Length = '50%';
78. private mHeight: Length = 100;
79. // custom attribute
80. private mOpacity: number = 0;

82. opacity(opacity: number): MyButtonModifier {
83. this.mOpacity = opacity;
84. return this;
85. }

87. private mBackgroundColor: ResourceColor = Color.Orange;

89. backgroundColor(backgroundColor: ResourceColor): MyButtonModifier {
90. this.mBackgroundColor = backgroundColor;
91. return this;
92. }

94. applyNormalAttribute(instance: ButtonAttribute): void {
95. instance.width(this.mWidth);
96. instance.height(this.mHeight);
97. instance.opacity(this.mOpacity);
98. instance.backgroundColor(this.mBackgroundColor);
99. }
100. }
```

[CustomComponentChainCall.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/4c2db649fbe3175edc1bbc5380847a598a949d4d/ArkUI/entry/src/main/ets/pages/CustomComponentChainCall.ets#L22-L122)
