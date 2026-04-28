---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pastebutton
title: 使用粘贴控件
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:06+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0752541faacf0058c4c3e05e67ccac82d2057933f3760ffe85b794811605a5d4
---

粘贴控件是一种特殊的系统安全控件，它允许应用在用户的授权下静默读取剪贴板数据。

集成粘贴控件后，单击该控件时，应用读取剪贴板数据不会弹窗提示。适用于任何需要读取剪贴板的应用场景，避免弹窗干扰用户。

例如，用户在应用外（如短信）复制了验证码，要在应用内粘贴验证码。用户原来在进入应用后，还需要长按输入框、在弹出的选项中点击粘贴，才能完成输入。而使用粘贴控件，用户只需进入应用后直接点击粘贴按钮，即可一步到位。

粘贴控件效果如图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/wVo-1g38SWqO2lANhmdJ9A/zh-cn_image_0000002552798710.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234205Z&HW-CC-Expire=86400&HW-CC-Sign=963759ABC0D63B50D0A2B9D5FEDD375F8F9ED761995A1FBC17F18F0556F67C8A)

## 约束与限制

* 临时授权会持续到灭屏、应用切后台或应用退出时终止。
* 应用在授权期间的调用次数无限制。
* 为了保障用户隐私，应用需确保安全控件可见且可识别。开发者应合理配置控件的尺寸和颜色等属性，避免视觉混淆。若因控件样式不合法导致授权失败请检查设备错误日志。

## 开发步骤

以简化用户填写验证码为例，参考以下步骤：单击控件获取临时授权，将内容粘贴到文本框。效果图见上文。

1. 导入剪贴板依赖。

   ```
   1. import { pasteboard } from '@kit.BasicServicesKit';
   ```
2. 添加输入框和粘贴控件。

   粘贴控件是一种类似按钮的安全控件，由图标、文本和背景组成。其中，背景是必选的，而图标和文本至少需要选择其一。图标和文本不支持自定义，仅能在已有的选项中选择。

   应用安全控件的接口时，分为传参和不传参两种情况。不传参时，默认创建包含图标、文本和背景的按钮；传参时，根据传入的参数创建按钮，不包含未配置的元素。

   当前示例使用了默认参数。具体详情，请参见[PasteButton控件](../harmonyos-references/ts-security-components-pastebutton.md)。此外，所有安全控件均继承了[安全控件通用属性](../harmonyos-references/ts-securitycomponent-attributes.md)，可用于自定义样式。

   ```
   1. import { pasteboard, BusinessError } from '@kit.BasicServicesKit';

   3. @Entry
   4. @Component
   5. struct Index {
   6. @State message: string = '';

   8. build() {
   9. Row() {
   10. Column({ space: 10 }) {
   11. TextInput({ placeholder: $r('app.string.input_verify_code'), text: this.message })
   12. .onChange((val: string) => {
   13. this.message = val;
   14. })
   15. PasteButton()
   16. .padding({top: 12, bottom: 12, left: 24, right: 24})
   17. .onClick((event: ClickEvent, result: PasteButtonOnClickResult) => {
   18. if (PasteButtonOnClickResult.SUCCESS === result) {
   19. pasteboard.getSystemPasteboard().getData((err: BusinessError, pasteData: pasteboard.PasteData) => {
   20. if (err) {
   21. console.error(`Failed to get paste data. Code is ${err.code}, message is ${err.message}`);
   22. return;
   23. }
   24. this.message = pasteData.getPrimaryText();
   25. });
   26. }
   27. })
   28. }
   29. .width('100%')
   30. }
   31. .height('100%')
   32. }
   33. }
   ```

   [Paste.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Security/SecurityComponent/entry/src/main/ets/securitycomponent/pages/Paste.ets#L16-L50)
