---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-phone-numbers
title: 电话号码格式化
breadcrumb: 指南 > 应用框架 > Localization Kit（本地化开发服务） > 应用国际化 > 电话号码格式化
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:01fe9e9b1f5da79baf2aafc62330d516f17f18413739465ff553e2b44309ece4
---

## 功能介绍

不同国家和地区的电话号码在号码位数、组合方式、呈现方式等都存在差异。同时，在不同环境和条件下，电话号码可能存在不同的拨打方式和号码格式。例如，在中国境内跨地区打电话，通常需要先输入“0”，再拨打区号和八位电话号码，而在香港或澳门拨打电话时，需要不同的拨号方式。

通过号码格式化，可以根据需要给用户展示特定格式的电话号码。

## 开发步骤

电话号码格式化通过[PhoneNumberFormat](../harmonyos-references/js-apis-i18n.md#phonenumberformat8)的[format](../harmonyos-references/js-apis-i18n.md#format8)接口实现。

**电话号码格式化选项**

以电话号码158\*\*\*\*2312，所属国家代码CN为例，说明PhoneNumberFormatOptions不同取值和显示效果。

**表1** 电话号码格式化的类型(type)

| 取值 | 显示效果 |
| --- | --- |
| E164 | +86 158\*\*\*\*2312 |
| INTERNATIONAL | +86 158 \*\*\*\* 2312 |
| NATIONAL | 158 \*\*\*\* 2312 |
| RFC3966 | tel:+86-158-\*\*\*\*-2312 |
| TYPING | 158 \*\*\* |

**开发实例**

1. 导入模块。

   ```
   1. import { i18n } from '@kit.LocalizationKit';
   ```

   [PhoneNumberFormatting.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/International/Internationalization/entry/src/main/ets/i18napplication/PhoneNumberFormatting.ets#L18-L20)
2. 处理号码。

   ```
   1. // 格式化电话号码
   2. let phoneNumberFormat: i18n.PhoneNumberFormat = new i18n.PhoneNumberFormat('CN');
   3. let formattedPhoneNumber = phoneNumberFormat.format('158****2312'); // formattedPhoneNumber = '158 **** 2312'

   5. // RFC3966类型的电话号码
   6. let rfcFormat: i18n.PhoneNumberFormat = new i18n.PhoneNumberFormat('CN', { type: 'RFC3966' });
   7. let formattedRFCPhoneNumber = rfcFormat.format('158****2312'); // formattedRFCPhoneNumber = 'tel:+86-158-****-2312'

   9. // 判断电话号码是否有效
   10. let isValid = phoneNumberFormat.isValidNumber('158****2312'); // isValid = true

   12. // 以某种语言显示号码归属地
   13. let locationName = phoneNumberFormat.getLocationName('158****2312', 'en-GB'); // locationName = 'XiAn, Shanxi'

   15. // 拨号中的电话号码格式化
   16. let typingFormat: i18n.PhoneNumberFormat = new i18n.PhoneNumberFormat('CN', { type: 'TYPING' });
   17. let phoneNumber = '0755453';
   18. let formatResult = ''; // 通过如下方式对拨号中的号码格式化后，formatResult = '0755 453'
   19. for (let i = 0; i < phoneNumber.length; i++) {
   20. formatResult += phoneNumber.charAt(i);
   21. formatResult = typingFormat.format(formatResult);
   22. }
   ```

   [PhoneNumberFormatting.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/International/Internationalization/entry/src/main/ets/i18napplication/PhoneNumberFormatting.ets#L35-L58)
