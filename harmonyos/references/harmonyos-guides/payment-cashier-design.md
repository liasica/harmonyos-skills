---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-cashier-design
title: 收银台设计规范
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > 收银台设计规范
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:59+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:32a6a2ecfa2687fe5ce2e968dd8ea6a62b6e8a32b79777a0b765cbc60c8e06c8
---

## 功能需求

开发者可在应用项目中实现支付收银台。应用项目由配置文件（module.json5）、页面代码（ets文件）以及资源文件（图片、字符串等）组成，实现的收银台包含以下功能：展示商户信息、金额、支付方式列表（用户选择的支付方式会变成选中状态）和支付按钮。

实现效果如下（具体实现可参见[示例代码](https://gitcode.com/HarmonyOS_Samples/paymentkit-samplecode-uxcodeproject-arkts)）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/A9EJKLbUTcqdv1zhFRCziQ/zh-cn_image_0000002706835096.png)

## 定义收银台页面容器

定义收银台页面容器用于展示支付收银台。UX规范要求以半模态弹窗展示收银台，使用说明可参考[半模态转场](../harmonyos-references/ts-universal-attributes-sheet-transition.md#示例1不同高度的半模态弹窗)。

半模态容器CashierBindSheetContainer.ets示例代码如下：

```typescript
import { CashierComponent } from './CashierComponent';

@Component
export struct CashierBindSheetContainer {
  @Builder
  cashierBuilder() {
    Column() {
      CashierComponent();
    }
  }

  build() {
    Column() {
      Column() {
      }.bindSheet(true, this.cashierBuilder(), {
        title: () => {},
        height: SheetSize.FIT_CONTENT,
        showClose: true,
        enableOutsideInteractive: false,
        backgroundColor: '#E5FFFFFF',
        blurStyle: BlurStyle.COMPONENT_THICK,
        onWillDismiss: ((action: DismissSheetAction) => {
          // 退出事件监听器处理
        }),
      });
    }.width('100%');
  }
}
```

## 搭建收银台页面

收银台首页CashierComponent.ets从整体上可分为三个部分：头部-商户信息展示、中部-支付方式列表、底部-支付按钮。

**示例代码如下：**

```typescript
import { LengthMetrics } from '@ohos.arkui.node';
import { getBorderRadius, isNewCardPaymentType } from '../util/PaymentUtil';
import { PaymentOrderComp } from './PaymentOrderComp';
import { PaymentItemComp } from './PaymentItemComp';
import { ConfirmButton } from './ConfirmButton';
import { PaymentType } from '../data/PaymentType';
import { paymentTypeList, paymentTypes3PayShow } from '../data/TestData';

@Preview
@Component
export struct CashierComponent {
  // 商户名称
  private mercShortName: string = '华为支付测试商户';
  // 付款金额
  private paymentAmount: string = '0.01';
  @State selectedPaymentType: PaymentType = new PaymentType();
  @State selectedPayTypeSerialNo: string = '';

  // 商家订单信息
  @Builder
  orderDetail() {
    // ...
  }

  // 支付方式列表
  @Builder
  displayHeader() {
    // ...
  }

  // 其他支付方式
  @Builder
  moreBankFooter() {
    // ...
  }

  // 支付方式选择事件
  select(paymentType: PaymentType) {
    // ...
  }

  // 支付方式列表
  @Builder
  paymentListBuilder() {
    // ...
  }

  // 支付方式列表容器
  @Builder
  paymentListContent() {
    Column() {
      this.paymentListBuilder();
    }
    .margin({
      bottom: 12,
    })
  }

  // 按钮区域
  @Builder
  buttonArea() {
    // ...
  }

  // 收银台首页
  @Builder
  cashierUI() {
    // 订单信息区和付款方式区域
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center }) {
      this.orderDetail();
      this.paymentListContent();
    }
    .align(Alignment.Top)
    .padding({
      left: $r('sys.float.ohos_id_elements_margin_horizontal_l'),
      right: $r('sys.float.ohos_id_elements_margin_horizontal_l'),
    })

    // 按钮区域
    Column() {
      this.buttonArea();
      Row()
        .width('100%')
        .height(28)
        .margin({ top: $r('sys.float.ohos_id_elements_margin_vertical_l') })
    }
    .flexShrink(0)
    .padding({
      left: $r('sys.float.ohos_id_elements_margin_horizontal_l'),
      right: $r('sys.float.ohos_id_elements_margin_horizontal_l'),
    })
  }

  // 页面容器
  build() {
    Column() {
      this.cashierUI();
    }
  }
}
```

**运行结果：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/dvTfPUgGQ6SX1iOQ7oJYeA/zh-cn_image_0000002706835096.png)

### 展示商户信息

收银台首页CashierComponent.ets的orderDetail组件为商户信息展示。商户信息竖向居中排列，包含商户名称以及订单金额。

**示例代码如下**：

```typescript
@Builder
orderDetail() {
  Column() {
    PaymentOrderComp({
      mercShortName: this.mercShortName,
      paymentAmount: this.paymentAmount,
    })
      .margin({ bottom: 24 });
  }
  .width('100%')
  .padding({
    top: $r('sys.float.ohos_id_elements_margin_vertical_m'),
  })
}
```

其中商户订单信息类PaymentOrderComp.ets实现如下：

```typescript
import { Amount } from './Amount';

@Component
export struct PaymentOrderComp {
  @Prop mercShortName: ResourceStr = '';
  @Prop paymentAmount: string = '';

  build() {
    Column() {
      Text(this.mercShortName)
        .fontFamily('HarmonyHeiTi')
        .fontSize($r('sys.float.ohos_id_text_size_body2'))
        .fontColor($r('sys.color.ohos_id_color_text_secondary'))
        .textAlign(TextAlign.Center)
        .fontWeight(FontWeight.Normal)

      Amount({
        amount: this.paymentAmount,
      }).margin({ top: 2 })
    }
  }
}
```

其中金额类Amount.ets实现如下：

```typescript
const FONT_FAMILY_HEITI = 'HarmonyHeiTi';

@Component
@Preview
export struct Amount {
  @Prop amount: string = '';
  private currency: string = '¥';
  private color: ResourceStr = $r('sys.color.ohos_id_color_text_primary');

  build() {
    Row() {
      Text() {
        Span(this.currency)
          .fontSize(24)
          .fontFamily(FONT_FAMILY_HEITI)
          .fontWeight(FontWeight.Bold)
          .fontColor(this.color)
          .alignSelf(ItemAlign.Baseline)
        Span(this.amount)
          .fontSize(36)
          .fontFamily(FONT_FAMILY_HEITI)
          .fontWeight(FontWeight.Bold)
          .fontColor(this.color)
      }
    }.justifyContent(FlexAlign.Center)
    .alignItems(VerticalAlign.Bottom)
  }
}
```

**运行结果：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/zbDDWGprTxedpTLleq-sAg/zh-cn_image_0000002736314203.png)

### 构造支付方式列表

收银台首页CashierComponent.ets的paymentListBuilder组件为收银台中部信息，包含支付方式列表。用户点击选择的支付方式会变成选中状态。

**示例代码如下**：

```typescript
@Builder
paymentListBuilder() {
  Column() {
    List() {
      ListItemGroup({
        header: this.displayHeader(),
        style: ListItemGroupStyle.CARD,
      }) {
        ForEach(paymentTypeList, (paymentType: PaymentType) => {
          ListItem({ style: ListItemStyle.CARD }) {
            PaymentItemComp({
              paymentType: paymentType,
              canChecked: !isNewCardPaymentType(paymentType),
              isChecked: this.selectedPayTypeSerialNo === paymentType.payTypeSerialNo,
              onSelect: () => {
                if (paymentType.isAvailable) {
                  this.select(paymentType);
                }
              },
            })
          }
          .height(undefined)
          .constraintSize({ minHeight: 48 })
          .backgroundColor(Color.Transparent)
        })

        // 其他支付方式
        ListItem({ style: ListItemStyle.CARD }) {
          this.moreBankFooter();
        }
        .height(undefined)
        .constraintSize({ minHeight: 48 })
        .backgroundColor(Color.Transparent)
      }.divider({
        strokeWidth: 0.5,
        color: $r('sys.color.ohos_id_color_list_separator'),
        startMargin: 48,
        endMargin: 12,
      }).margin({
        left: 0,
        right: 0,
      }).backgroundColor($r('sys.color.comp_background_list_card'))
    }.width('100%')

    // 三方支付方式
    List() {
      ListItemGroup({ style: ListItemGroupStyle.CARD }) {
        ForEach(paymentTypes3PayShow, (paymentType: PaymentType) => {
          ListItem({ style: ListItemStyle.CARD }) {
            PaymentItemComp({
              paymentType: paymentType,
              canChecked: true,
              isChecked: this.selectedPayTypeSerialNo === paymentType.payTypeSerialNo,
              onSelect: () => {
                if (paymentType.isAvailable) {
                  this.select(paymentType);
                }
              },
            })
          }
          .height(undefined)
          .constraintSize({ minHeight: 48 })
          .backgroundColor(Color.Transparent)
        })
      }.divider({
        strokeWidth: 0.5,
        color: $r('sys.color.ohos_id_color_list_separator'),
        startMargin: 48,
        endMargin: 12,
      })
      .margin({
        left: 0,
        right: 0,
      }).backgroundColor($r('sys.color.comp_background_list_card'))
    }
    .width('100%')
    .margin({
      top: 12,
    })
  }
}
```

其中列表标题组件displayHeader示例代码如下：

```typescript
@Builder
displayHeader() {
  Column() {
    Flex({ justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
      Image($r('app.media.kit_hwpay_wallet'))
        .borderRadius(getBorderRadius(24))
        .width(24)
        .height(24)
        .margin({ end: LengthMetrics.vp(16) })

      Text($r('app.string.kit_hwpay_desc'))
        .fontSize(16)
        .fontWeight(FontWeight.Medium)
        .fontFamily('HarmonyHeiTi-Medium')
        .fontColor($r('sys.color.ohos_id_color_text_primary'))
    }
    .width('100%')
    .constraintSize({ minHeight: 48 })
    .padding({
      left: 8,
      right: 8,
      top: 12,
      bottom: 12,
    })

    Divider()
      .color($r('sys.color.ohos_id_color_list_separator'))
      .width('100%')
      .margin({
        start: LengthMetrics.vp(48),
        end: LengthMetrics.vp(12),
      })
  }
}
```

其中其它支付方式组件moreBankFooter示例代码如下：

```typescript
@Builder
moreBankFooter() {
  Flex({ justifyContent: FlexAlign.SpaceBetween, alignItems: ItemAlign.Center }) {
    Text($r('app.string.kit_hwpay_change_other_pay_type'))
      .fontSize(16)
      .fontWeight(FontWeight.Medium)
      .fontFamily('HarmonyHeiTi-Medium')
      .fontColor($r('sys.color.ohos_id_color_text_primary'))

    Image($r('app.media.kit_hwpay_right_v2'))
      .matchTextDirection(true)
      .width(12)
      .height(24)
      .fillColor($r('sys.color.ohos_id_color_fourth'))
  }
  .padding({
    top: 12,
    bottom: 12,
  })
  .margin({ start: LengthMetrics.vp(40) })
}
```

其中支付方式组件类PaymentItemComp.ets实现展示可用、不可用的支付方式，添加银行卡以及用户选中支付方式后展示勾选效果。示例代码如下：

```typescript
import { LengthMetrics } from '@ohos.arkui.node';
import { PaymentType } from '../data/PaymentType';
import { getBorderRadius } from '../util/PaymentUtil';

export enum ButtonOpacity {
  // 默认不透明度
  PRIMARY = 1,
  // 按钮的透明度设置为灰色
  DISABLED = 0.6,
  // 支付方式的不透明度
  PAYMENT_UNAVAILABLE = 0.38
}

@Component
export struct PaymentItemComp {
  @Prop paymentType: PaymentType;
  @Prop canChecked: boolean = false;
  @Prop isChecked?: boolean = false;
  onSelect: () => void = () => {
  };

  build() {
    Row() {
      Image($r('app.media.payment_logo'))
        .borderRadius(getBorderRadius(24))
        .width(24)
        .height(24)
        .margin({ end: LengthMetrics.vp(16) })

      Flex({ direction: FlexDirection.Column, justifyContent: FlexAlign.Center }) {
        Flex({
          direction: FlexDirection.Row,
          justifyContent: FlexAlign.Start,
          alignItems: ItemAlign.Center,
        }) {
          Text(this.paymentType?.payTypeDesc)
            .fontSize(16)
            .fontWeight(FontWeight.Medium)
            .fontFamily('HarmonyHeiTi-Medium')
            .fontColor($r('sys.color.ohos_id_color_text_primary'))
        }
        .padding({
          top: (this.paymentType?.paymentTypeTip) ? 4 : 0,
        })

        if (this.paymentType?.paymentTypeTip) {
          Row() {
            Text(this.paymentType?.paymentTypeTip)
              .fontSize($r('sys.float.ohos_id_text_size_body3'))
              .fontColor($r('sys.color.comp_focused_secondary'))
              .fontFamily('HarmonyHeiTi')
              .fontWeight(FontWeight.Normal)
              .width('90%')
              .padding({ top: 4, bottom: 4 })
          }
        }
      }
      .layoutWeight(1)

      if (this.canChecked) {
        Radio({ value: this.paymentType?.payTypeSerialNo as string, group: 'aggrPaymentRadioGroup' })
          .visibility(this.isChecked ? Visibility.Visible : Visibility.Hidden)
          .checked(this.isChecked)
          .height(20)
          .width(20)
          .margin(2)
      } else {
        Image($r('app.media.kit_hwpay_right_v2'))
          .width(12)
          .height(24)
          .fillColor($r('sys.color.ohos_id_color_fourth'))
          .visibility(this.paymentType?.isAvailable ? Visibility.Visible : Visibility.None)
      }
    }
    .padding({
      top: 12,
      bottom: 12,
    })
    .opacity(this.paymentType?.isAvailable ? ButtonOpacity.PRIMARY : ButtonOpacity.PAYMENT_UNAVAILABLE)
    .alignItems(VerticalAlign.Center)
    .onClick(() => {
      if (!this.paymentType?.isAvailable) {
        return;
      }
      this.onSelect();
    })
  }
}
```

收银台首页CashierComponent.ets中选择支付方式事件示例代码如下：

```typescript
select(paymentType: PaymentType) {
  this.selectedPaymentType = paymentType;
  this.selectedPayTypeSerialNo = paymentType.payTypeSerialNo || '';
}
```

**运行结果：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/O-pRe5zzQ2OMvPtITzHt5A/zh-cn_image_0000002706675160.png)

### 添加支付按钮

收银台首页CashierComponent.ets的buttonArea组件为收银台底部信息，包含支付按钮。开发者可通过按钮点击事件实现具体支付处理逻辑。

**示例代码如下**：

```typescript
@Builder
buttonArea() {
  ConfirmButton({
    text: $r('app.string.kit_hwpay_checkout_confirm_pay'),
  })
    .margin({
      top: $r('sys.float.ohos_id_elements_margin_vertical_l'),
    });
}
```

其中确认支付按钮类ConfirmButton.ets示例代码如下：

```typescript
@Component
@Preview
export struct ConfirmButton {
  @Prop text: ResourceStr = '';

  build() {
    Column() {
      Row() {
        Button(this.text) {
          Row() {
            Text(this.text)
              .fontSize($r('sys.float.Body_L'))
              .fontWeight(FontWeight.Medium)
              .fontFamily('HarmonyHeiTi-Medium')
              .fontColor($r('sys.color.ohos_fa_text_contrary'))
              .textAlign(TextAlign.Center)
              .textOverflow({
                overflow: TextOverflow.Ellipsis
              })
              .maxLines(1)
          }
          .alignItems(VerticalAlign.Center)
          .justifyContent(FlexAlign.Center)
        }
        .focusOnTouch(true)
        .type(ButtonType.Normal)
        .borderRadius(20)
        .backgroundColor($r('sys.color.ohos_id_color_floating_button_bg_normal'))
        .constraintSize({
          minWidth: '100%',
          maxWidth: '100%',
          minHeight: 40,
          maxHeight: 40,
        })
        .padding({
          top: 4,
          bottom: 4,
          left: 16,
          right: 16,
        })
        .opacity(1)
        .stateEffect(true)
      }
      .onClick(() => {
        // 按钮点击事件
      })
    }.width('100%')
    .alignItems(HorizontalAlign.Center)
  }
}
```

**运行结果：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/lTgPNKbnRzy6_pMufsGDfQ/zh-cn_image_0000002736434249.png)

## 页面数据定义

### 字符串、图片等资源

文件摆放位置为“src/main/resources”相应的目录下。

### 支付方式及支付类型枚举

支付方式PaymentType.ets类及支付类型枚举CustPayType.ets类定义示例代码如下：

```typescript
export class PaymentType {
  public payTypeSerialNo?: string;
  public payTypeDesc?: string;
  public paymentTypeTip?: string;
  public isAvailable?: boolean;
  public custPayType: string = '';
}
```

```typescript
export enum CustPayType {
  NewBankCard = 'NewBankCard',
}
```

### 支付方式测试数据

测试使用的支付方式数据TestData.ets类定义示例代码如下：

```typescript
import { PaymentType } from './PaymentType';

export const paymentTypeList: PaymentType[] = [
  {
    payTypeSerialNo: '1',
    payTypeDesc: 'xx银行储蓄卡 (0606)',
    isAvailable: true,
    custPayType: 'BankFastPayment',
  },
  {
    payTypeSerialNo: '2',
    payTypeDesc: 'xx银行储蓄卡 (0909)',
    isAvailable: true,
    custPayType: 'BankFastPayment',
  }
];

export const paymentTypes3PayShow: PaymentType[] = [
  {
    payTypeSerialNo: '3',
    payTypeDesc: '云闪付',
    isAvailable: true,
    custPayType: 'CloudFlashPayment',
  },
  {
    payTypeSerialNo: '4',
    payTypeDesc: '微信支付',
    isAvailable: true,
    custPayType: 'WECHAT_MICROPAY',
  }
]
```

### 工具类

支付工具PaymentUtil.ets类定义示例代码如下：

```typescript
import { CustPayType } from '../data/CustPayType';
import { PaymentType } from '../data/PaymentType';

/**
 * 支付工具是否是新卡
 * @param paymentType 支付方式
 * @returns 是否为新卡支付方式
 */
export const isNewCardPaymentType = (paymentType: PaymentType): boolean => {
  if (!paymentType) {
    return false;
  }
  return paymentType.custPayType === CustPayType.NewBankCard;
};

/**
 * 获取图标圆角值
 * @param length 圆角值
 * @returns 图标圆角值
 */
export const getBorderRadius = (length: number): number => {
  // 根据图标边长计算圆角值
  return 7 / 27 * length;
}
```
