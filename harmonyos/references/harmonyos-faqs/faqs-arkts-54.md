---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-54
title: ArkTS中globalThis无法使用该如何替换
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > ArkTS中globalThis无法使用该如何替换
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:02+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:0072a8f5336afc0faa73d1c2b7442a0ed6545e7d2b966b03141fdcd6adda1a64
---

ArkTS不支持动态更改对象布局，也不支持全局作用域和globalThis。请参考以下替换方案：

1. 通过单例map做中转：

   ```
   1. import { common } from '@kit.AbilityKit';

   3. // Construct singleton objects
   4. export class GlobalThis {
   5. private constructor() {};
   6. private static instance: GlobalThis;
   7. private _uiContexts = new Map<string, common.UIAbilityContext>();
   8. private value = '';

   10. public static getInstance(): GlobalThis {
   11. if (!GlobalThis.instance) {
   12. GlobalThis.instance = new GlobalThis();
   13. }
   14. return GlobalThis.instance;
   15. }

   17. getContext(key: string): common.UIAbilityContext | undefined {
   18. return this._uiContexts.get(key);
   19. }

   21. setContext(key: string, value: common.UIAbilityContext): void {
   22. this._uiContexts.set(key, value);
   23. }

   25. setValue(value:string){
   26. this.value = value
   27. }

   29. getValue():string{
   30. return this.value;
   31. }
   32. }
   ```

   [globalThis.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/utils/globalThis.ets#L6-L37)
2. 使用：

   ```
   1. import { GlobalThis } from '../utils/globalThis';

   3. @Entry
   4. @Component
   5. struct Index {
   6. @State value: string = GlobalThis.getInstance().getValue();

   8. build() {
   9. Row() {
   10. Column() {
   11. Text(this.value)
   12. .fontSize(50)
   13. .fontWeight(FontWeight.Bold)
   14. Button("setValue")
   15. .fontSize(50)
   16. .fontWeight(FontWeight.Bold)
   17. .onClick(() => {
   18. GlobalThis.getInstance().setValue("TEST");
   19. })
   20. Button("getValue")
   21. .fontSize(50)
   22. .fontWeight(FontWeight.Bold)
   23. .onClick(() => {
   24. this.value = GlobalThis.getInstance().getValue();
   25. })
   26. }
   27. .width('100%')
   28. }
   29. .height('100%')
   30. }
   31. }
   ```

   [GlobalThisReplacementInArkTS.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/GlobalThisReplacementInArkTS.ets#L21-L51)

**参考链接**

[arkts-no-globalthis](../harmonyos-guides/arkts-more-cases.md#arkts-no-globalthis)
