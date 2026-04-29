---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-cashier-design
title: 收银台设计规范
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > 收银台设计规范
category: harmonyos-guides
scraped_at: 2026-04-29T13:39:27+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:07964f25a104025683fee153fdbf4877cde0a974c2decd52ecd02f6c19dcfd4d
---

## 功能需求

开发者可在应用项目中实现支付收银台。应用项目由配置文件（module.json5）、页面代码（ets文件）以及资源文件（图片、字符串等）组成，实现的收银台包含以下功能：展示商户信息、金额、支付方式列表（用户选择的支付方式会变成选中状态）和支付按钮。

实现效果如下（具体实现可参见[示例代码](https://gitcode.com/HarmonyOS_Samples/paymentkit-samplecode-uxcodeproject-arkts)）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/5WU338z5RD-Fa5VPDZbhAQ/zh-cn_image_0000002558765574.png?HW-CC-KV=V1&HW-CC-Date=20260429T053926Z&HW-CC-Expire=86400&HW-CC-Sign=22CFD7680523C15AA25A098808D25622A7A63D52D4DFCECCA47F8BC57F95DD17)

## 定义收银台页面容器

定义收银台页面容器用于展示支付收银台。UX规范要求以半模态弹窗展示收银台，使用说明可参考[半模态转场](../harmonyos-references/ts-universal-attributes-sheet-transition.md#示例1不同高度的半模态弹窗)。

半模态容器CashierBindSheetContainer.ets示例代码如下：

```
1. import { CashierComponent } from './CashierComponent';

3. @Component
4. export struct CashierBindSheetContainer {
5. @Builder
6. cashierBuilder() {
7. Column() {
8. CashierComponent();
9. }
10. }

12. build() {
13. Column() {
14. Column() {
15. }.bindSheet(true, this.cashierBuilder(), {
16. title: () => {},
17. height: SheetSize.FIT_CONTENT,
18. showClose: true,
19. enableOutsideInteractive: false,
20. backgroundColor: '#E5FFFFFF',
21. blurStyle: BlurStyle.COMPONENT_THICK,
22. onWillDismiss: ((action: DismissSheetAction) => {
23. // 退出事件监听
24. }),
25. });
26. }.width('100%');
27. }
28. }
```

## 搭建收银台页面

收银台首页CashierComponent.ets从整体上可分为三个部分：头部-商户信息展示、中部-支付方式列表、底部-支付按钮。

**示例代码如下：**

```
1. import { LengthMetrics } from '@kit.ArkUI';
2. import { getBorderRadius, isNewCardPaymentType } from '../util/PaymentUtil';
3. import { PaymentOrderComp } from './PaymentOrderComp';
4. import { PaymentItemComp } from './PaymentItemComp';
5. import { ConfirmButton } from './ConfirmButton';
6. import { PaymentType } from '../data/PaymentType';
7. import { paymentTypeList, paymentTypes3PayShow } from '../data/TestData';

9. @Preview
10. @Component
11. export struct CashierComponent {
12. // 商户名称
13. private mercShortName: string = "华为支付测试商户";
14. // 支付金额（单位为分）
15. private paymentAmount: string = '0.01';
16. // 当前选中的支付方式信息
17. @State selectedPaymentType: PaymentType = new PaymentType();
18. @State selectedPayTypeSerialNo: string = '';

20. // 头部：商户订单信息
21. @Builder
22. orderDetail() {
23. // 后续展示实现
24. }

26. // 中部：支付方式列表的标题
27. @Builder
28. displayHeader() {
29. // 后续展示实现
30. }

32. // 中部：其他支付方式选项
33. @Builder
34. moreBankFooter() {
35. // 后续展示实现
36. }

38. // 中部：选择支付方式事件
39. select(PaymentType: PaymentType) {
40. // 后续展示实现
41. }

43. // 中部：支付方式列表
44. @Builder
45. paymentListBuilder() {
46. // 后续展示实现
47. }

49. // 中部：支付方式列表 容器
50. @Builder
51. paymentListContent() {
52. Column() {
53. this.paymentListBuilder();
54. }
55. .margin({
56. bottom: 12,
57. })
58. }

60. // 底部：按钮区域
61. @Builder
62. buttonArea() {
63. // 后续展示实现
64. }

66. // 收银台首页
67. @Builder
68. cashierUI() {
69. // 订单信息+支付方式区域
70. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center }) {
71. this.orderDetail();
72. this.paymentListContent();
73. }
74. .align(Alignment.Top)
75. .padding({
76. left: $r('sys.float.ohos_id_elements_margin_horizontal_l'),
77. right: $r('sys.float.ohos_id_elements_margin_horizontal_l'),
78. })

80. // 按钮区域
81. Column() {
82. this.buttonArea();
83. // 底部aiBar的高度
84. Row()
85. .width('100%')
86. .height(28)
87. .margin({ top: $r('sys.float.ohos_id_elements_margin_vertical_l') })
88. }
89. .flexShrink(0)
90. .padding({
91. left: $r('sys.float.ohos_id_elements_margin_horizontal_l'),
92. right: $r('sys.float.ohos_id_elements_margin_horizontal_l'),
93. })
94. }

96. // 页面容器
97. build() {
98. Column() {
99. this.cashierUI();
100. }
101. }
102. }
```

**运行结果：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/G4o6LKydR0Kj4BjUMtA45w/zh-cn_image_0000002558765574.png?HW-CC-KV=V1&HW-CC-Date=20260429T053926Z&HW-CC-Expire=86400&HW-CC-Sign=80F55A3E09CB0B27627B49BCAEA48B1D587BEF5C7752FA8EA139D55DCC51A3C8)

### 展示商户信息

收银台首页CashierComponent.ets的orderDetail组件为商户信息展示。商户信息竖向居中排列，包含商户名称以及订单金额。

**示例代码如下**：

```
1. @Builder
2. orderDetail() {
3. Column() {
4. PaymentOrderComp({
5. mercShortName: this.mercShortName,
6. paymentAmount: this.paymentAmount,
7. })
8. .margin({ bottom: 24 });
9. }
10. .width('100%')
11. .padding({
12. top: $r('sys.float.ohos_id_elements_margin_vertical_m'),
13. })
14. }
```

其中商户订单信息类PaymentOrderComp.ets实现如下：

```
1. import { Amount } from "./Amount";

3. @Component
4. export struct PaymentOrderComp {
5. @Prop mercShortName: ResourceStr = '';
6. @Prop paymentAmount: string = '';

8. build() {
9. Column() {
10. Text(this.mercShortName)
11. .fontFamily('HarmonyHeiTi')
12. .fontSize($r('sys.float.ohos_id_text_size_body2'))
13. .fontColor($r('sys.color.ohos_id_color_text_secondary'))
14. .textAlign(TextAlign.Center)
15. .fontWeight(FontWeight.Normal)

17. Amount({
18. amount: this.paymentAmount,
19. }).margin({ top: 2 })
20. }
21. }
22. }
```

其中金额类Amount.ets实现如下：

```
1. const FONT_FAMILY_HEITI = 'HarmonyHeiTi';

3. @Component
4. @Preview
5. export struct Amount {
6. @Prop amount: string = '';
7. private currency: string = '¥';
8. private color: ResourceStr = $r('sys.color.ohos_id_color_text_primary');

10. build() {
11. Row() {
12. Text() {
13. Span(this.currency)
14. .fontSize(24)
15. .fontFamily(FONT_FAMILY_HEITI)
16. .fontWeight(FontWeight.Bold)
17. .fontColor(this.color)
18. .alignSelf(ItemAlign.Baseline)
19. Span(this.amount)
20. .fontSize(36)
21. .fontFamily(FONT_FAMILY_HEITI)
22. .fontWeight(FontWeight.Bold)
23. .fontColor(this.color)
24. }
25. }.justifyContent(FlexAlign.Center)
26. .alignItems(VerticalAlign.Bottom)
27. }
28. }
```

**运行结果：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/KPfjrUKwRua8yDX8sxRMWg/zh-cn_image_0000002558605918.png?HW-CC-KV=V1&HW-CC-Date=20260429T053926Z&HW-CC-Expire=86400&HW-CC-Sign=085E30EFE97199254B2767B2B3A9E11F2F84BA4418B3842E627EDEF0969CE5C3)

### 构造支付方式列表

收银台首页CashierComponent.ets的paymentListBuilder组件为收银台中部信息，包含支付方式列表。用户点击选择的支付方式会变成选中状态。

**示例代码如下**：

```
1. @Builder
2. paymentListBuilder() {
3. Column() {
4. List() {
5. ListItemGroup({
6. header: this.displayHeader(),
7. style: ListItemGroupStyle.CARD,
8. }) {
9. ForEach(paymentTypeList, (paymentType: PaymentType) => {
10. ListItem({ style: ListItemStyle.CARD }) {
11. PaymentItemComp({
12. paymentType: paymentType,
13. canChecked: !isNewCardPaymentType(paymentType),
14. isChecked: this.selectedPayTypeSerialNo === paymentType.payTypeSerialNo,
15. onSelect: () => {
16. if (paymentType.isAvailable) {
17. this.select(paymentType);
18. }
19. },
20. })
21. }
22. .height(undefined)
23. .constraintSize({ minHeight: 48 })
24. .backgroundColor(Color.Transparent)
25. })

27. // 其他支付方式
28. ListItem({ style: ListItemStyle.CARD }) {
29. this.moreBankFooter();
30. }
31. .height(undefined)
32. .constraintSize({ minHeight: 48 })
33. .backgroundColor(Color.Transparent)
34. }.divider({
35. strokeWidth: 0.5,
36. color: $r('sys.color.ohos_id_color_list_separator'),
37. startMargin: 48,
38. endMargin: 12,
39. }).margin({
40. left: 0,
41. right: 0,
42. }).backgroundColor($r('sys.color.comp_background_list_card'))
43. }.width('100%')

45. // 三方支付方式
46. List() {
47. ListItemGroup({ style: ListItemGroupStyle.CARD }) {
48. ForEach(paymentTypes3PayShow, (paymentType: PaymentType) => {
49. ListItem({ style: ListItemStyle.CARD }) {
50. PaymentItemComp({
51. paymentType: paymentType,
52. canChecked: true,
53. isChecked: this.selectedPayTypeSerialNo === paymentType.payTypeSerialNo,
54. onSelect: () => {
55. if (paymentType.isAvailable) {
56. this.select(paymentType);
57. }
58. },
59. })
60. }
61. .height(undefined)
62. .constraintSize({ minHeight: 48 })
63. .backgroundColor(Color.Transparent)
64. })
65. }.divider({
66. strokeWidth: 0.5,
67. color: $r('sys.color.ohos_id_color_list_separator'),
68. startMargin: 48,
69. endMargin: 12,
70. })
71. .margin({
72. left: 0,
73. right: 0,
74. }).backgroundColor($r('sys.color.comp_background_list_card'))
75. }
76. .width('100%')
77. .margin({
78. top: 12,
79. })
80. }
81. }
```

其中列表标题组件displayHeader示例代码如下：

```
1. @Builder
2. displayHeader() {
3. Column() {
4. Flex({ justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
5. Image($r('app.media.kit_hwpay_wallet'))
6. .borderRadius(getBorderRadius(24))
7. .width(24)
8. .height(24)
9. .margin({ end: LengthMetrics.vp(16) })

11. Text($r('app.string.kit_hwpay_desc'))
12. .fontSize(16)
13. .fontWeight(FontWeight.Medium)
14. .fontFamily('HarmonyHeiTi-Medium')
15. .fontColor($r('sys.color.ohos_id_color_text_primary'))
16. }
17. .width('100%')
18. .constraintSize({ minHeight: 48 })
19. .padding({
20. left: 8,
21. right: 8,
22. top: 12,
23. bottom: 12,
24. })

26. Divider()
27. .color($r('sys.color.ohos_id_color_list_separator'))
28. .width('100%')
29. .margin({
30. start: LengthMetrics.vp(48),
31. end: LengthMetrics.vp(12),
32. })
33. }
34. }
```

其中其它支付方式组件moreBankFooter示例代码如下：

```
1. @Builder
2. moreBankFooter() {
3. Flex({ justifyContent: FlexAlign.SpaceBetween, alignItems: ItemAlign.Center }) {
4. Text($r('app.string.kit_hwpay_change_other_pay_type'))
5. .fontSize(16)
6. .fontWeight(FontWeight.Medium)
7. .fontFamily('HarmonyHeiTi-Medium')
8. .fontColor($r('sys.color.ohos_id_color_text_primary'))

10. Image($r('app.media.kit_hwpay_right_v2'))
11. .matchTextDirection(true)
12. .width(12)
13. .height(24)
14. .fillColor($r('sys.color.ohos_id_color_fourth'))
15. }
16. .padding({
17. top: 12,
18. bottom: 12,
19. })
20. .margin({ start: LengthMetrics.vp(40) })
21. }
```

其中支付方式组件类PaymentItemComp.ets实现展示可用、不可用的支付方式，添加银行卡以及用户选中支付方式后展示勾选效果。示例代码如下：

```
1. import { LengthMetrics } from '@kit.ArkUI';
2. import { PaymentType } from '../data/PaymentType';
3. import { getBorderRadius } from '../util/PaymentUtil';

5. export enum ButtonOpacity {
6. // 默认不透明度
7. PRIMARY = 1,
8. // 按钮置灰不透明度
9. DISABLED = 0.6,
10. // 支付方式不可用导致的按钮不可用的不透明度
11. PAYMENT_UNAVAILABLE = 0.38
12. }

14. @Component
15. export struct PaymentItemComp {
16. @Prop paymentType: PaymentType;
17. @Prop canChecked: boolean = false;
18. @Prop isChecked?: boolean = false;
19. onSelect: () => void = () => {
20. };

22. build() {
23. Row() {
24. Image($r("app.media.payment_logo"))
25. .borderRadius(getBorderRadius(24))
26. .width(24)
27. .height(24)
28. .margin({ end: LengthMetrics.vp(16) })

30. Flex({ direction: FlexDirection.Column, justifyContent: FlexAlign.Center }) {
31. Flex({
32. direction: FlexDirection.Row,
33. justifyContent: FlexAlign.Start,
34. alignItems: ItemAlign.Center,
35. }) {
36. Text(this.paymentType?.payTypeDesc)
37. .fontSize(16)
38. .fontWeight(FontWeight.Medium)
39. .fontFamily('HarmonyHeiTi-Medium')
40. .fontColor($r('sys.color.ohos_id_color_text_primary'))
41. }
42. .padding({
43. top: (this.paymentType?.paymentTypeTip) ? 4 : 0,
44. })

46. if (this.paymentType?.paymentTypeTip) {
47. Row() {
48. Text(this.paymentType?.paymentTypeTip)
49. .fontSize($r('sys.float.ohos_id_text_size_body3'))
50. .fontColor($r('sys.color.comp_focused_secondary'))
51. .fontFamily('HarmonyHeiTi')
52. .fontWeight(FontWeight.Normal)
53. .width('90%')
54. .padding({ top: 4, bottom: 4 })
55. }
56. }
57. }
58. .layoutWeight(1)

60. if (this.canChecked) {
61. Radio({ value: this.paymentType?.payTypeSerialNo as string, group: 'aggrPaymentRadioGroup' })
62. .visibility(this.isChecked ? Visibility.Visible : Visibility.Hidden)
63. .checked(this.isChecked)
64. .height(20)
65. .width(20)
66. .margin(2)
67. } else {
68. Image($r('app.media.kit_hwpay_right_v2'))
69. .width(12)
70. .height(24)
71. .fillColor($r('sys.color.ohos_id_color_fourth'))
72. .visibility(this.paymentType?.isAvailable ? Visibility.Visible : Visibility.None)
73. }
74. }
75. .padding({
76. top: 12,
77. bottom: 12,
78. })
79. .opacity(this.paymentType?.isAvailable ? ButtonOpacity.PRIMARY : ButtonOpacity.PAYMENT_UNAVAILABLE)
80. .alignItems(VerticalAlign.Center)
81. .onClick(() => {
82. if (!this.paymentType?.isAvailable) {
83. return;
84. }
85. this.onSelect();
86. })
87. }
88. }
```

收银台首页CashierComponent.ets中选择支付方式事件示例代码如下：

```
1. select(PaymentType: PaymentType) {
2. this.selectedPaymentType = PaymentType;
3. this.selectedPayTypeSerialNo = PaymentType.payTypeSerialNo || '';
4. }
```

**运行结果：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/ZrABZPZ1QiGTBl_a_cEPfQ/zh-cn_image_0000002589325445.png?HW-CC-KV=V1&HW-CC-Date=20260429T053926Z&HW-CC-Expire=86400&HW-CC-Sign=093193D301EC1DAD76FE611F750240837B8EBC3769DF01DC4EC09FA0E046BED9)

### 添加支付按钮

收银台首页CashierComponent.ets的buttonArea组件为收银台底部信息，包含支付按钮。开发者可通过按钮点击事件实现具体支付处理逻辑。

**示例代码如下**：

```
1. @Builder
2. buttonArea() {
3. ConfirmButton({
4. text: $r('app.string.kit_hwpay_checkout_confirm_pay'),
5. })
6. .margin({
7. top: $r('sys.float.ohos_id_elements_margin_vertical_l'),
8. });
9. }
```

其中确认支付按钮类ConfirmButton.ets示例代码如下：

```
1. @Component
2. @Preview
3. export struct ConfirmButton {
4. @Prop text: ResourceStr = '';

6. build() {
7. Column() {
8. Row() {
9. Button(this.text) {
10. Row() {
11. Text(this.text)
12. .fontSize($r('sys.float.Body_L'))
13. .fontWeight(FontWeight.Medium)
14. .fontFamily('HarmonyHeiTi-Medium')
15. .fontColor($r('sys.color.ohos_fa_text_contrary'))
16. .textAlign(TextAlign.Center)
17. .textOverflow({
18. overflow: TextOverflow.Ellipsis
19. })
20. .maxLines(1)
21. }
22. .alignItems(VerticalAlign.Center)
23. .justifyContent(FlexAlign.Center)
24. }
25. .focusOnTouch(true)
26. .type(ButtonType.Normal)
27. .borderRadius(20)
28. .backgroundColor($r('sys.color.ohos_id_color_floating_button_bg_normal'))
29. .constraintSize({
30. minWidth: '100%',
31. maxWidth: '100%',
32. minHeight: 40,
33. maxHeight: 40,
34. })
35. .padding({
36. top: 4,
37. bottom: 4,
38. left: 16,
39. right: 16,
40. })
41. .opacity(1)
42. .stateEffect(true)
43. }
44. .onClick(() => {
45. // 按钮点击事件
46. })
47. }.width('100%')
48. .alignItems(HorizontalAlign.Center)
49. }
50. }
```

**运行结果：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/L8Rz91U9TlS7LdhiCAggcw/zh-cn_image_0000002589245383.png?HW-CC-KV=V1&HW-CC-Date=20260429T053926Z&HW-CC-Expire=86400&HW-CC-Sign=6D1C91B43235081077B02D9A0B39B780F34760567019A8D5EFE33A06005E0947)

## 页面数据定义

### 字符串、图片等资源

文件摆放位置为“src/main/resources”相应的目录下。

### 支付方式及支付类型枚举

支付方式PaymentType.ets类及支付类型枚举CustPayType.ets类定义示例代码如下：

```
1. // 支付方式：PaymentType.ets
2. export class PaymentType {
3. payTypeSerialNo?: string;
4. payTypeDesc?: string;
5. paymentTypeTip?: string;
6. isAvailable?: boolean;
7. custPayType: string = '';
8. }

10. // 支付类型枚举：CustPayType.ets
11. export enum CustPayType {
12. NewBankCard = 'NewBankCard',
13. }
```

### 支付方式测试数据

测试使用的支付方式数据TestData.ets类定义示例代码如下：

```
1. import { PaymentType } from "./PaymentType";

3. export const paymentTypeList: PaymentType[] = [
4. {
5. payTypeSerialNo: '1',
6. payTypeDesc: 'xx银行储蓄卡 (0606)',
7. isAvailable: true,
8. custPayType: 'BankFastPayment',
9. },
10. {
11. payTypeSerialNo: '2',
12. payTypeDesc: 'xx银行储蓄卡 (0909)',
13. isAvailable: true,
14. custPayType: 'BankFastPayment',
15. }
16. ];

18. export const paymentTypes3PayShow: PaymentType[] = [
19. {
20. payTypeSerialNo: '3',
21. payTypeDesc: '云闪付',
22. isAvailable: true,
23. custPayType: 'CloudFlashPayment',
24. },
25. {
26. payTypeSerialNo: '4',
27. payTypeDesc: '微信支付',
28. isAvailable: true,
29. custPayType: 'WECHAT_MICROPAY',
30. }
31. ]
```

### 工具类

支付工具PaymentUtil.ets类定义示例代码如下：

```
1. import { CustPayType } from "../data/CustPayType";
2. import { PaymentType } from "../data/PaymentType";

4. /**
5. * 支付工具是否是新卡
6. * @param paymentType 支付方式
7. * @returns 是否为新卡支付方式
8. */
9. export const isNewCardPaymentType = (paymentType: PaymentType): boolean => {
10. if (!paymentType) {
11. return false;
12. }
13. return paymentType.custPayType === CustPayType.NewBankCard;
14. };

16. /**
17. * 获取图标圆角值
18. * @param length 圆角值
19. * @returns 图标圆角值
20. */
21. export const getBorderRadius = (length: number): number => {
22. // 正方形图标圆角值为：14 / 54 * 图标边长
23. return 7 / 27 * length;
24. }
```
